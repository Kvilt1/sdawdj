import os
import re

OUTPUT_FILE = "fixed_solutions_final.md"

def check_progress():
    if os.path.exists(OUTPUT_FILE):
        size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
        print(f"Output file exists. Size: {size_mb:.2f} MB")
        
        # Count the number of questions in the output file
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
            # Use regex to find question ID tags
            question_count = len(re.findall(r'<a id=\'oppgave\d+\'></a>', content))
            print(f"Number of questions processed: {question_count}/98")
    else:
        print(f"Output file {OUTPUT_FILE} does not exist yet")

if __name__ == "__main__":
    check_progress() 