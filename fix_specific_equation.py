#!/usr/bin/env python3
"""
Simple script to fix a specific LaTeX equation pattern.

This script demonstrates how to fix the specific equation pattern:
$\text{kW/m}^2 $

Run it with:
python3 fix_specific_equation.py
"""

import re

def fix_specific_equation(latex_string):
    """
    Fix specific problematic LaTeX equation patterns.
    
    Args:
        latex_string (str): The LaTeX string to fix
        
    Returns:
        str: The fixed LaTeX string
    """
    # Fix common unit formatting issues
    
    # 1. Add braces around superscripts
    fixed = re.sub(r'([_^])(\d+)([^{]|$)', r'\1{\2}\3', latex_string)
    
    # 2. Remove extra spaces inside $ delimiters
    fixed = re.sub(r'\$\s+(.*?)\s+\$', r'$\1$', fixed)
    
    # 3. Special case for kW/m^2
    fixed = fixed.replace(r'\text{kW/m}^2', r'\text{kW/m}^{2}')
    
    return fixed

def main():
    # Test cases
    test_cases = [
        r'$\text{kW/m}^2 $',
        r'$ 5 \text{kg} $',
        r'$E = mc^2 $',
        r'$ v^2 = v_0^2 + 2as $',
        r'$\text{m}^3$',
        r'$\text{kg} \cdot \text{m/s}$'
    ]
    
    print("Testing equation fixes:")
    print("-" * 40)
    
    for i, test in enumerate(test_cases, 1):
        fixed = fix_specific_equation(test)
        print(f"Original {i}: {test}")
        print(f"Fixed {i}:    {fixed}")
        print()
    
    # Test with user input
    print("\nEnter a LaTeX equation to fix (or press Enter to quit):")
    while True:
        user_input = input("> ")
        if not user_input:
            break
        
        fixed = fix_specific_equation(user_input)
        print(f"Fixed: {fixed}")

if __name__ == "__main__":
    main() 