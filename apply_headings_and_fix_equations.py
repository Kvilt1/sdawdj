#!/usr/bin/env python3
"""
Script to apply question headings and fix LaTeX equation formatting issues in markdown files.

This script:
1. Applies headings from a reference file to questions in a solutions file
2. Fixes LaTeX equation formatting issues:
   - Extra whitespace around equations
   - Missing 'times' symbols (should be \times)
   - Missing spaces between equations and text
   - Other formatting issues that cause rendering problems

Usage:
    python3 apply_headings_and_fix_equations.py [--input INPUT] [--names NAMES] [--output OUTPUT]

Options:
    --input INPUT   Input solutions file (default: fixed_solutions_improved.md)
    --names NAMES   Reference file with question names (default: Question names.md)
    --output OUTPUT Output file with applied headings and fixed equations (default: fixed_solutions_final.md)
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

def apply_headings(content, headings):
    """
    Apply the extracted headings to the solutions file content.
    
    Args:
        content (str): Content of the solutions file
        headings (dict): Dictionary mapping question numbers to their headings
        
    Returns:
        str: Content with applied headings
    """
    lines = content.split('\n')
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
                line = f'# Question {question_num}: {headings[question_num]}'
        
        # Check for table of contents entries
        toc_match = toc_pattern.match(line.strip())
        if toc_match:
            question_num = int(toc_match.group(1))
            if question_num in headings:
                line = f'- [Question {question_num}: {headings[question_num]}](#oppgave{question_num})'
        
        new_lines.append(line)
    
    return '\n'.join(new_lines)

def fix_equations(content):
    """
    Fix LaTeX equations with formatting issues
    
    Args:
        content (str): The content of the file to be fixed
        
    Returns:
        str: The fixed content
    """
    # First, fix block equations with extra whitespace
    # Pattern: newline + whitespace + newline + $$ + equation + $$ + whitespace + newline
    block_pattern = r'\n\s+\n\$\$\s*(.*?)\s*\$\$\s*\n\s+\n'
    block_replacement = r'\n\n$$\n\1\n$$\n\n'
    fixed_content = re.sub(block_pattern, block_replacement, content, flags=re.DOTALL)
    
    # Fix times symbol in different variations
    fixed_content = fixed_content.replace(r'imes', r'\times')
    fixed_content = fixed_content.replace(r'\t\times', r'\times')
    
    # Fix other common LaTeX errors or inconsistencies
    fixed_content = fixed_content.replace(r'\text{kg} \cdot \text{m/s}', r'\text{kg} \cdot \text{m/s}')
    
    # Ensure spaces between text and inline equations
    # Fix: text$equation$ -> text $equation$
    fixed_content = re.sub(r'([a-zA-Z0-9,.;:])(\$[^$]+\$)', r'\1 \2', fixed_content)
    # Fix: $equation$text -> $equation$ text
    fixed_content = re.sub(r'(\$[^$]+\$)([a-zA-Z0-9])', r'\1 \2', fixed_content)
    
    # Fix inline equations with extra internal spacing
    inline_pattern = r'\$\s+(.*?)\s+\$'
    inline_replacement = r'$\1$'
    fixed_content = re.sub(inline_pattern, inline_replacement, fixed_content)
    
    # Fix missing line breaks before and after block equations
    # Before: text$$ -> text\n\n$$
    fixed_content = re.sub(r'([a-zA-Z0-9,.;:])(\$\$)', r'\1\n\n\2\n', fixed_content)
    # After: $$text -> $$\n\ntext
    fixed_content = re.sub(r'(\$\$\n)([a-zA-Z0-9])', r'\1\n\2', fixed_content)
    
    # Fix equations without proper spacing
    fixed_content = re.sub(r'(\$\$)([^\n])', r'\1\n\2', fixed_content)
    fixed_content = re.sub(r'([^\n])(\$\$)', r'\1\n\2', fixed_content)
    
    # Make sure block equations have proper line breaks within them
    # This ensures the equation appears on its own line between the $$ markers
    equations_pattern = r'\$\$(.*?)\$\$'
    
    def add_newlines_to_equation(match):
        eq = match.group(1).strip()
        return f"$$\n{eq}\n$$"
    
    fixed_content = re.sub(equations_pattern, add_newlines_to_equation, fixed_content, flags=re.DOTALL)
    
    return fixed_content

def process_file(input_file, names_file, output_file):
    """
    Process a file to apply headings and fix equation formatting
    
    Args:
        input_file (str): Path to the input file
        names_file (str): Path to the file with question names
        output_file (str): Path to the output file
    """
    try:
        # Read the content of the file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract headings from the reference file
        headings = extract_question_headings(names_file)
        print(f"Extracted {len(headings)} question headings from '{names_file}'")
        
        # Apply headings to the solutions file
        content_with_headings = apply_headings(content, headings)
        
        # Fix the equations
        fixed_content = fix_equations(content_with_headings)
        
        # Write the final content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"Headings applied and equations fixed successfully. Result saved to {output_file}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Apply question headings and fix LaTeX equations in markdown files.')
    parser.add_argument('--input', default='fixed_solutions_improved.md',
                        help='Input solutions file (default: fixed_solutions_improved.md)')
    parser.add_argument('--names', default='Question names.md',
                        help='Reference file with question names (default: Question names.md)')
    parser.add_argument('--output', default='fixed_solutions_final.md',
                        help='Output file with applied headings and fixed equations (default: fixed_solutions_final.md)')
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
    
    # Process the file
    process_file(args.input, args.names, args.output)

if __name__ == '__main__':
    main() 