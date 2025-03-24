import re
import sys

def fix_github_latex_issues(content):
    """Fix common LaTeX issues that prevent proper rendering on GitHub"""
    
    # Fix 1: Replace comma before \text with a space
    content = re.sub(r'(\d+)\s*,\s*\\text{', r'\1 \\text{', content)
    
    # Fix 2: Ensure there's a space inside \text{} for units
    content = re.sub(r'\\text{([a-zA-Z0-9]+)}', r'\\text{ \1}', content)
    
    # Fix 3: Fix spacing around \times
    content = re.sub(r'(\d+)\s*\\times\s*', r'\1 \\times ', content)
    
    # Fix 4: Make sure all inline math has proper spacing
    content = re.sub(r'\$([^\$]+)\$', lambda m: '$' + m.group(1).strip() + '$', content)
    
    # Fix 5: Fix specific cases like the example provided
    # Example: N = 1500 \times 10^6 \times 1800 \approx 2.7 \times 10^{12} , \text{decays}
    content = re.sub(r'(\d+\s*\\times\s*10\^\{?\d+\}?\s*.*?)\s*,\s*(\\text{.*?})', r'\1 \2', content)
    
    # Fix 6: Ensure proper spacing between number and unit
    content = re.sub(r'(\d+)\\text{', r'\1 \\text{', content)
    
    # Fix 7: Fix spacing around \approx
    content = re.sub(r'(\S)\\approx(\S)', r'\1 \\approx \2', content)
    
    # Fix 8: Ensure closing braces for superscripts are properly placed
    content = re.sub(r'10\^(\d+)([^\}])', r'10^{\1}\2', content)
    
    # Fix 9: Ensure display math has proper line breaks and is on its own line
    # This ensures GitHub renders it as block math
    content = re.sub(r'([^\n])\$\$', r'\1\n\n$$', content)
    content = re.sub(r'\$\$([^\n])', r'$$\n\n\1', content)
    
    # Fix 10: Ensure display math has proper spacing around the content
    content = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$\n' + m.group(1).strip() + '\n$$', content, flags=re.DOTALL)
    
    return content

def main():
    input_file = "FIX'.md"
    output_file = "github_fixed_solutions.md"
    
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Specific fix for the example provided by the user
    example_fix = r'N = 1500 \times 10^6 \times 1800 \approx 2.7 \times 10^{12} , \text{decays}'
    content = content.replace(example_fix, r'N = 1500 \times 10^6 \times 1800 \approx 2.7 \times 10^{12} \text{ decays}')
    
    print("Fixing GitHub LaTeX rendering issues...")
    fixed_content = fix_github_latex_issues(content)
    
    print(f"Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done!")

if __name__ == "__main__":
    main() 