import re
import os
import json
import time
import asyncio
import google.generativeai as genai
from tqdm import tqdm
import traceback

# Configure API
API_KEY = "AIzaSyAkUPg7ZGmsWwhyN3yEId5S8Htehzn1AUw"
genai.configure(api_key=API_KEY)

# Use Gemini Flash 2.0 model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define paths
INPUT_FILE = "fixed_solutions_with_headings.md"
OUTPUT_FILE = "fixed_solutions_improved.md"
STATS_FILE = "processing_stats.json"

# Rate limiting configuration - Tier 1 account
# According to Gemini documentation, Tier 1 accounts have these limits:
# - 60 QPM (queries per minute)
# - Maximum of 100 concurrent requests
MAX_CONCURRENT_REQUESTS = 10  # Conservative setting to avoid rate limit issues
RATE_LIMIT_QPM = 50  # More conservative than the actual limit of 60

# Track statistics
stats = {
    "total_questions": 0,
    "processed_questions": 0,
    "errors": 0,
    "changed_questions": 0,
    "unchanged_questions": 0,
    "processing_times": [],
    "error_details": []
}

async def fix_latex_errors(question_id, question_text):
    """
    Use Gemini API to fix LaTeX errors in a question.
    """
    start_time = time.time()
    
    # Extract question number for more specific prompting
    question_num_match = re.search(r'# Question (\d+):', question_text)
    question_num = question_num_match.group(1) if question_num_match else "unknown"
    
    prompt = f"""
    Analyze and fix any LaTeX and formatting errors in this markdown content from Question {question_num}. 
    
    Focus on:
    1. LaTeX equation formatting:
       - Display math should use $$ (on separate lines)
       - Inline math should use single $
       - Fix any equation syntax errors (missing braces, incorrect commands, etc.)
       
    2. Consistent formatting:
       - Variables should be in italics (in LaTeX math mode)
       - Units should be upright (\\text{{...}} in LaTeX)
       - Proper spacing in equations (use \\, \\: \\; appropriately)
       - Correct subscripts and superscripts
       - Proper use of Greek letters
       
    3. Other markdown formatting:
       - Consistent headings
       - Clean list formatting
       - Proper paragraph breaks
    
    Return ONLY the corrected version of the text. Make minimal changes - only fix actual errors.
    If there are no errors, return the original text exactly.
    
    Here is the content:
    
    {question_text}
    """
    
    try:
        response = model.generate_content(prompt)
        corrected_text = response.text
        
        # Check if content was actually changed
        is_changed = corrected_text.strip() != question_text.strip()
        
        # Update statistics
        stats["processed_questions"] += 1
        if is_changed:
            stats["changed_questions"] += 1
        else:
            stats["unchanged_questions"] += 1
            
        processing_time = time.time() - start_time
        stats["processing_times"].append(processing_time)
        
        return corrected_text, is_changed
    
    except Exception as e:
        error_message = str(e)
        stack_trace = traceback.format_exc()
        print(f"Error processing question {question_id}: {error_message}")
        
        # Update statistics
        stats["errors"] += 1
        stats["error_details"].append({
            "question_id": question_id,
            "error": error_message,
            "stack_trace": stack_trace
        })
        
        return question_text, False

def extract_questions(markdown_text):
    """
    Extract individual questions from the markdown file.
    """
    # Pattern to match each question section starting with # Question and ending before the next question
    pattern = r'(<a id=\'oppgave(\d+)\'></a>\s*\n\s*# Question \d+.*?)(?=<a id=\'oppgave\d+\'></a>|$)'
    question_matches = re.findall(pattern, markdown_text, re.DOTALL)
    
    # Process the extracted groups
    questions = [(match_id, match_text) for match_text, match_id in question_matches]
    
    # Also capture the table of contents and other content before the first question
    header_match = re.match(r'(.*?)(?=<a id=\'oppgave\d+\'></a>)', markdown_text, re.DOTALL)
    header = header_match.group(1) if header_match else ""
    
    return header, questions

async def process_questions(markdown_text):
    """
    Process all questions in the markdown file with rate limiting.
    """
    header, questions = extract_questions(markdown_text)
    stats["total_questions"] = len(questions)
    print(f"Found {len(questions)} questions to process")
    
    # Create a semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    
    async def process_with_rate_limit(question_id, question_text):
        async with semaphore:
            # Add delay to respect rate limits
            await asyncio.sleep(60 / RATE_LIMIT_QPM)
            return await fix_latex_errors(question_id, question_text)
    
    # Create tasks for all questions
    tasks = [process_with_rate_limit(q_id, q_text) for q_id, q_text in questions]
    
    # Process questions with progress bar
    fixed_questions_dict = {}
    progress_bar = tqdm(total=len(tasks), desc="Processing questions")
    
    for i, task in enumerate(asyncio.as_completed(tasks)):
        question_id = questions[i][0]
        fixed_question, was_changed = await task
        fixed_questions_dict[question_id] = fixed_question
        progress_bar.update(1)
        
        # Periodically save statistics
        if i % 10 == 0 or i == len(tasks) - 1:
            save_statistics()
    
    progress_bar.close()
    
    # Combine the fixed questions in the original order
    ordered_fixed_questions = [fixed_questions_dict[q_id] for q_id, _ in questions]
    result = header + "".join(ordered_fixed_questions)
    
    return result

def save_statistics():
    """Save processing statistics to a JSON file"""
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            # Calculate average processing time if available
            if stats["processing_times"]:
                stats["avg_processing_time"] = sum(stats["processing_times"]) / len(stats["processing_times"])
            json.dump(stats, f, indent=2)
    except Exception as e:
        print(f"Error saving statistics: {e}")

async def main():
    # Read the input file
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as file:
            markdown_text = file.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        return
    
    # Process the questions
    print("Processing questions for LaTeX and formatting errors...")
    fixed_markdown = await process_questions(markdown_text)
    
    # Write the output file
    print(f"Writing results to {OUTPUT_FILE}...")
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
            file.write(fixed_markdown)
    except Exception as e:
        print(f"Error writing output file: {e}")
        return
    
    # Final statistics
    print("\nProcessing complete!")
    print(f"Total questions: {stats['total_questions']}")
    print(f"Successfully processed: {stats['processed_questions']}")
    print(f"Questions with changes: {stats['changed_questions']}")
    print(f"Questions unchanged: {stats['unchanged_questions']}")
    print(f"Errors encountered: {stats['errors']}")
    
    if stats["processing_times"]:
        avg_time = sum(stats["processing_times"]) / len(stats["processing_times"])
        print(f"Average processing time per question: {avg_time:.2f} seconds")
        
    print(f"Detailed statistics saved to {STATS_FILE}")

if __name__ == "__main__":
    print("Starting improved LaTeX error correction...")
    asyncio.run(main()) 