#!/usr/bin/env python3
"""
Script to apply question headings from a reference file to a solutions file.

This script reads question headings from a reference file (e.g., "Question names.md")
and applies them to a solutions file where questions are labeled without headings.
It modifies both the main question headings and the table of contents entries.

Usage:
    python3 apply_headings.py [--input INPUT] [--names NAMES] [--output OUTPUT]

Options:
    --input INPUT   Input solutions file (default: fixed_solutions_improved.md)
    --names NAMES   Reference file with question names (default: Question names.md)
    --output OUTPUT Output file with applied headings (default: fixed_solutions_with_headings.md)
"""

import re
import os
import argparse

def extract_question_headings(filename):
    """
    Extract question numbers and their headings from a reference file.
    
    Args:
        filename (str): Path to the reference file with question names
        
    Returns:
        dict: Dictionary mapping question numbers to their headings
    """
    headings = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Question '):
                # Extract question number and heading
                match = re.match(r'Question (\d+)\s+(.*)', line)
                if match:
                    question_num = int(match.group(1))
                    heading = match.group(2).strip()
                    headings[question_num] = heading
    return headings

def apply_headings_to_file(input_filename, output_filename, headings):
    """
    Apply the extracted headings to the solutions file.
    
    Args:
        input_filename (str): Path to the input solutions file
        output_filename (str): Path to the output file with applied headings
        headings (dict): Dictionary mapping question numbers to their headings
    """
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    
    # Regular expressions for matching question headings and TOC entries
    heading_pattern = re.compile(r'^# Question (\d+)$')
    toc_pattern = re.compile(r'^- \[Question (\d+)\]\(#oppgave(\d+)\)$')
    
    for line in lines:
        # Check for main headings
        heading_match = heading_pattern.match(line.strip())
        if heading_match:
            question_num = int(heading_match.group(1))
            if question_num in headings:
                line = f'# Question {question_num}: {headings[question_num]}\n'
        
        # Check for table of contents entries
        toc_match = toc_pattern.match(line.strip())
        if toc_match:
            question_num = int(toc_match.group(1))
            if question_num in headings:
                line = f'- [Question {question_num}: {headings[question_num]}](#oppgave{question_num})\n'
        
        new_lines.append(line)
    
    # Write the updated content to the output file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Headings applied successfully. Result saved to {output_filename}")
    print(f"Applied headings to {len(headings)} questions.")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Apply question headings from a reference file to a solutions file.')
    parser.add_argument('--input', default='fixed_solutions_improved.md',
                        help='Input solutions file (default: fixed_solutions_improved.md)')
    parser.add_argument('--names', default='Question names.md',
                        help='Reference file with question names (default: Question names.md)')
    parser.add_argument('--output', default='fixed_solutions_with_headings.md',
                        help='Output file with applied headings (default: fixed_solutions_with_headings.md)')
    return parser.parse_args()

def main():
    """Main function to run the script."""
    args = parse_args()
    
    # Check if input files exist
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        return
    
    if not os.path.exists(args.names):
        print(f"Error: Question names file '{args.names}' not found.")
        return
    
    # Extract headings from the reference file
    headings = extract_question_headings(args.names)
    print(f"Extracted {len(headings)} question headings from '{args.names}'")
    
    # Apply headings to the solutions file
    apply_headings_to_file(args.input, args.output, headings)

if __name__ == '__main__':
    main() 