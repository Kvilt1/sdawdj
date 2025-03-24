import re
import os
import time
import asyncio
import google.generativeai as genai
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# Configure API
API_KEY = "AIzaSyAkUPg7ZGmsWwhyN3yEId5S8Htehzn1AUw"
genai.configure(api_key=API_KEY)

# Use Gemini Flash 2.0 model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define paths
INPUT_FILE = "fixed_solutions_with_headings.md"
OUTPUT_FILE = "fixed_solutions_final.md"

# Rate limiting configuration - Tier 1 account
# According to Gemini documentation, Tier 1 accounts have these limits:
# - 60 QPM (queries per minute)
# - Maximum of 100 concurrent requests
MAX_CONCURRENT_REQUESTS = 20  # Conservative setting to avoid rate limit issues
RATE_LIMIT_QPM = 60  # Queries per minute

async def fix_latex_errors(question_text):
    """
    Use Gemini API to fix LaTeX errors in a question.
    """
    prompt = f"""
    Review the following markdown content and fix any LaTeX errors, formatting issues, or inconsistencies.
    Pay special attention to:
    1. Properly formatted LaTeX equations (ensure they use $$ for display math and $ for inline math)
    2. Correct LaTeX syntax (fix any syntax errors, missing braces, etc.)
    3. Consistent formatting of variables, units, and mathematical expressions
    4. Ensure proper spacing in LaTeX equations
    5. Make sure subscripts and superscripts are properly formatted
    
    Return the fully corrected version with all fixes applied, maintaining the original markdown structure.
    If there are no errors, return the original text unchanged.
    
    Here is the content:
    
    {question_text}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error processing content: {str(e)}")
        return question_text  # Return original if there's an error

def extract_questions(markdown_text):
    """
    Extract individual questions from the markdown file.
    """
    # Pattern to match each question section starting with # Question and ending before the next question
    pattern = r'(<a id=\'oppgave\d+\'></a>\s*\n\s*# Question \d+.*?)(?=<a id=\'oppgave\d+\'></a>|$)'
    questions = re.findall(pattern, markdown_text, re.DOTALL)
    
    # Also capture the table of contents and other content before the first question
    header_match = re.match(r'(.*?)(?=<a id=\'oppgave\d+\'></a>)', markdown_text, re.DOTALL)
    header = header_match.group(1) if header_match else ""
    
    return header, questions

async def process_questions(markdown_text):
    """
    Process all questions in the markdown file with rate limiting.
    """
    header, questions = extract_questions(markdown_text)
    print(f"Found {len(questions)} questions to process")
    
    fixed_questions = []
    
    # Create a semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    
    async def process_with_rate_limit(question):
        async with semaphore:
            # Add delay to respect rate limits if needed
            await asyncio.sleep(60 / RATE_LIMIT_QPM)  # Distribute requests evenly within the minute
            return await fix_latex_errors(question)
    
    # Create tasks for all questions
    tasks = [process_with_rate_limit(question) for question in questions]
    
    # Process questions with progress bar
    fixed_questions = []
    for task in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Processing questions"):
        fixed_question = await task
        fixed_questions.append(fixed_question)
    
    # Combine the fixed questions
    result = header + "".join(fixed_questions)
    
    return result

async def main():
    # Read the input file
    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    
    # Process the questions
    print("Processing questions for LaTeX and formatting errors...")
    fixed_markdown = await process_questions(markdown_text)
    
    # Write the output file
    print(f"Writing results to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write(fixed_markdown)
    
    print("Done!")

if __name__ == "__main__":
    print("Starting LaTeX error correction...")
    asyncio.run(main()) 