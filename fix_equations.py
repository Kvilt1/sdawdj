#!/usr/bin/env python3
"""
Script to fix LaTeX equation formatting issues in markdown files.

This script addresses multiple issues with LaTeX equations in markdown:
1. Extra whitespace around equations
2. Missing 'times' symbols (should be \times)
3. Missing spaces between equations and text
4. Other formatting issues that cause rendering problems
5. Unit formatting issues with superscripts
"""

import re
import argparse
import os

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
    
    # Properly format commonly problematic units
    # Fix kW/m^2 pattern
    fixed_content = fixed_content.replace(r'\text{kW/m}^2', r'\text{kW/m}^{2}')
    
    # Fix general unit formatting with superscripts
    unit_pattern = r'\\text\{([^}]+)\}\^(\d+)'
    unit_replacement = r'\\text{\1}^{\2}'
    fixed_content = re.sub(unit_pattern, unit_replacement, fixed_content)
    
    # Ensure proper brace formatting for all superscripts and subscripts
    fixed_content = re.sub(r'([_^])(\d+)([^{]|$)', r'\1{\2}\3', fixed_content)
    
    # Fix spacing in inline equations with units
    fixed_content = re.sub(r'(\d+)\\text', r'\1 \\text', fixed_content)
    
    # Ensure spaces between text and inline equations
    # Fix: text$equation$ -> text $equation$
    fixed_content = re.sub(r'([a-zA-Z0-9,.;:])(\$[^$]+\$)', r'\1 \2', fixed_content)
    # Fix: $equation$text -> $equation$ text
    fixed_content = re.sub(r'(\$[^$]+\$)([a-zA-Z0-9])', r'\1 \2', fixed_content)
    
    # Fix inline equations with extra internal spacing
    inline_pattern = r'\$\s+(.*?)\s+\$'
    inline_replacement = r'$\1$'
    fixed_content = re.sub(inline_pattern, inline_replacement, fixed_content)
    
    # Remove trailing spaces inside inline equations
    fixed_content = re.sub(r'\$([^$]*?)\s+\$', r'$\1$', fixed_content)
    
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
    
    # Special case for division in text mode
    fixed_content = fixed_content.replace(r'\text{kW/m}', r'\text{kW/m}')
    
    return fixed_content

def process_file(input_file, output_file=None):
    """
    Process a file to fix equation formatting
    
    Args:
        input_file (str): Path to the input file
        output_file (str, optional): Path to the output file. If None, overwrites the input file.
    """
    # If no output file is specified, use the input file
    if output_file is None:
        output_file = input_file
    
    try:
        # Read the content of the file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the equations
        fixed_content = fix_equations(content)
        
        # Write the fixed content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"Equations fixed successfully. Result saved to {output_file}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Fix LaTeX equation formatting issues in markdown files.')
    parser.add_argument('input', help='Input file path')
    parser.add_argument('--output', help='Output file path (if not specified, overwrites the input file)')
    return parser.parse_args()

def main():
    """Main function"""
    args = parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        return
    
    # Process the file
    process_file(args.input, args.output)

if __name__ == '__main__':
    main() 