import re
import os
import json
import time
import asyncio
import google.generativeai as genai
from tqdm import tqdm

# Configure API
API_KEY = "AIzaSyAkUPg7ZGmsWwhyN3yEId5S8Htehzn1AUw"
genai.configure(api_key=API_KEY)

# Use Gemini Flash 2.0 model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define paths
INPUT_FILE = "fixed_solutions_with_headings.md"
OUTPUT_FILE = "fixed_solutions_final.md"
CHECKPOINT_FILE = "checkpoint.json"

# Optimized settings for Tier 1 account
MAX_CONCURRENT_REQUESTS = 50  # Increased from 10/20
BATCH_SIZE = 10  # Process in batches for better error recovery

# Stats dictionary
stats = {
    "start_time": None,
    "end_time": None,
    "total_questions": 0,
    "processed_questions": 0,
    "changed_questions": 0,
    "unchanged_questions": 0,
    "errors": 0
}

# Load checkpoint if exists
def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r') as f:
            return json.load(f)
    return {"processed": {}}

# Save checkpoint
def save_checkpoint(processed_questions):
    checkpoint = {"processed": processed_questions}
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(checkpoint, f)

async def fix_latex_errors(question_id, question_text):
    """Use Gemini API to fix LaTeX errors in a question."""
    # Extract question number for more specific prompting
    question_num_match = re.search(r'# Question (\d+):', question_text)
    question_num = question_num_match.group(1) if question_num_match else "unknown"
    
    prompt = f"""
    Fix any LaTeX and formatting errors in this markdown Question {question_num}.
    
    Fix:
    1. LaTeX formatting: Use $$ for display math, $ for inline math
    2. LaTeX syntax: Fix missing braces, incorrect commands
    3. Consistent formatting: Variables in math mode, units with \\text{{}}
    4. Proper spacing in equations
    5. Correct subscripts and superscripts
    
    Return ONLY the corrected version. Make minimal changes.
    
    Content:
    {question_text}
    """
    
    try:
        response = model.generate_content(prompt)
        corrected_text = response.text
        
        # Check if content was changed
        is_changed = corrected_text.strip() != question_text.strip()
        
        # Update stats
        stats["processed_questions"] += 1
        if is_changed:
            stats["changed_questions"] += 1
        else:
            stats["unchanged_questions"] += 1
            
        return question_id, corrected_text, True
    except Exception as e:
        stats["errors"] += 1
        print(f"Error processing question {question_id}: {str(e)}")
        return question_id, question_text, False

def extract_questions(markdown_text):
    """Extract individual questions from the markdown file with IDs."""
    # Capture header (content before first question)
    header_match = re.match(r'(.*?)(?=<a id=\'oppgave\d+\'></a>)', markdown_text, re.DOTALL)
    header = header_match.group(1) if header_match else ""
    
    # Match question ID and content
    pattern = r'<a id=\'oppgave(\d+)\'></a>\s*\n\s*(# Question \d+.*?)(?=<a id=\'oppgave\d+\'></a>|$)'
    questions = [(match_id, match_text) for match_id, match_text in re.findall(pattern, markdown_text, re.DOTALL)]
    
    return header, questions

async def process_batch(batch, semaphore, checkpoint_data):
    """Process a batch of questions with semaphore for concurrency control."""
    tasks = []
    
    for q_id, q_text in batch:
        # Skip already processed questions
        if q_id in checkpoint_data["processed"]:
            continue
            
        # Create task
        task = asyncio.create_task(process_with_semaphore(q_id, q_text, semaphore))
        tasks.append(task)
    
    # Wait for all tasks in batch to complete
    batch_results = {}
    if tasks:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print(f"Batch error: {result}")
                continue
            
            q_id, q_text, success = result
            if success:
                batch_results[q_id] = q_text
                # Update checkpoint after each successful question
                checkpoint_data["processed"][q_id] = True
                save_checkpoint(checkpoint_data["processed"])
    
    return batch_results

async def process_with_semaphore(q_id, q_text, semaphore):
    """Process a question with semaphore control."""
    async with semaphore:
        return await fix_latex_errors(q_id, q_text)

async def main():
    stats["start_time"] = time.time()
    
    # Load checkpoint
    checkpoint_data = load_checkpoint()
    processed_count = len(checkpoint_data["processed"])
    print(f"Loaded checkpoint with {processed_count} already processed questions")
    
    # Read the input file
    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    
    # Extract questions
    header, questions = extract_questions(markdown_text)
    stats["total_questions"] = len(questions)
    print(f"Found {len(questions)} questions to process")
    
    # Create a semaphore for concurrency control
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    
    # Process in batches
    all_results = {}
    batches = [questions[i:i+BATCH_SIZE] for i in range(0, len(questions), BATCH_SIZE)]
    
    for i, batch in enumerate(tqdm(batches, desc="Processing batches")):
        print(f"\nProcessing batch {i+1}/{len(batches)} ({len(batch)} questions)")
        batch_results = await process_batch(batch, semaphore, checkpoint_data)
        all_results.update(batch_results)
        print(f"Batch complete. Total processed: {len(all_results)}/{len(questions)}")
    
    # Reconstruct the document in original order
    result = header
    for q_id, _ in questions:
        if q_id in all_results:
            result += all_results[q_id]
        else:
            # Use original text if not processed
            original_text = next((text for id, text in questions if id == q_id), "")
            result += original_text
    
    # Write the output file
    print(f"Writing results to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write(result)
    
    # Final statistics
    stats["end_time"] = time.time()
    total_time = stats["end_time"] - stats["start_time"]
    
    print("\nProcessing complete!")
    print(f"Total questions: {stats['total_questions']}")
    print(f"Successfully processed: {stats['processed_questions']}")
    print(f"Questions with changes: {stats['changed_questions']}")
    print(f"Questions unchanged: {stats['unchanged_questions']}")
    print(f"Errors encountered: {stats['errors']}")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Average time per question: {total_time / max(1, stats['processed_questions']):.2f} seconds")

if __name__ == "__main__":
    print("Starting optimized LaTeX error correction...")
    asyncio.run(main()) 