#!/usr/bin/env python3
"""
Markdown validation script based on STYLE_GUIDE.md
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

class MarkdownValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        
        # Regex patterns for validation
        self.rules = {
            'h1_time_marker': r'^#\s+.*\(.*\d+.*min.*\)',
            'h1_hours': r'^#\s+.*\(.*\d+.*h.*\)',
            'h1_difficulty': r'^#\s+.*\(.*Advanced.*\)',
            'h1_emoji': r'^#\s+.*[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002600-\U000026FF\U00002700-\U000027BF]',
            'h2_type_repeat': r'^##\s+(Kodutöö|Labor|Lisapraktika)\s+',
            'h2_bad_heading': r'^##\s+(Lab\'i eesmärk|Eesmärk)$',
            'forbidden_metadata': r'\*\*(Kestus|Aeg|Sihtgrupp|Õpetajale|Vorm):\*\*',
            'code_no_lang': r'^```$\n',
            'inline_checkmarks': r'\-\s*✅.*\-\s*✅',
            'emoji_in_heading': r'^#+\s+.*[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002600-\U000026FF\U00002700-\U000027BF]',
            'emoji_in_list': r'^-\s+[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002600-\U000026FF\U00002700-\U000027BF]',
        }

    def validate_file(self, filepath: Path) -> List[str]:
        """Validate a single markdown file"""
        errors = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            return [f"ERROR: Could not read file: {e}"]

        filename = filepath.name
        
        # Check H1 count
        h1_count = sum(1 for line in lines if line.startswith('# '))
        if h1_count != 1:
            errors.append(f"ERROR: Must have exactly 1 H1, found {h1_count}")
        
        # Check for forbidden H1 patterns
        for line in lines:
            if line.startswith('# '):
                for rule_name, pattern in self.rules.items():
                    if rule_name.startswith('h1_') and re.search(pattern, line):
                        errors.append(f"ERROR: {rule_name} violated: {line[:50]}...")
        
        # Check H2 structure based on file type
        if filename in ['loeng.md', 'labor.md']:
            if '## Õpiväljundid' not in content:
                errors.append("ERROR: Missing '## Õpiväljundid' heading")
        elif filename in ['kodutoo.md', 'lisapraktika.md']:
            if '## Õpiväljundid' in content:
                errors.append("ERROR: '## Õpiväljundid' not allowed in this file type")
        
        # Check for forbidden H2 patterns
        for line in lines:
            if line.startswith('## '):
                for rule_name, pattern in self.rules.items():
                    if rule_name.startswith('h2_') and re.search(pattern, line):
                        errors.append(f"ERROR: {rule_name} violated: {line[:50]}...")
        
        # Check for forbidden metadata
        for rule_name, pattern in self.rules.items():
            if rule_name == 'forbidden_metadata':
                matches = re.findall(pattern, content)
                if matches:
                    errors.append(f"ERROR: {rule_name} violated: {matches[0]}")
        
        # Check code blocks
        code_blocks = re.findall(r'```(\w*)\n', content)
        for i, lang in enumerate(code_blocks):
            if not lang.strip():
                errors.append(f"ERROR: Code block {i+1} missing language tag")
        
        # Check inline checkmarks
        if re.search(self.rules['inline_checkmarks'], content):
            errors.append("ERROR: Inline checkmarks found - convert to proper list")
        
        # Check emoji usage
        for line in lines:
            if line.startswith('#'):
                if re.search(self.rules['emoji_in_heading'], line):
                    errors.append(f"ERROR: Emoji in heading: {line[:50]}...")
            elif line.startswith('- '):
                if re.search(self.rules['emoji_in_list'], line):
                    errors.append(f"ERROR: Emoji in list: {line[:50]}...")
        
        # Check paragraph length
        paragraphs = content.split('\n\n')
        for i, para in enumerate(paragraphs):
            if para.strip() and not para.startswith('#') and not para.startswith('```'):
                sentences = len(re.split(r'[.!?]+\s+', para))
                if sentences > 4:
                    errors.append(f"WARNING: Paragraph {i+1} too long ({sentences} sentences, max 4)")
        
        # Check bold usage
        sections = content.split('\n\n')
        for i, section in enumerate(sections):
            if section.strip() and not section.startswith('#'):
                bold_count = len(re.findall(r'\*\*.*?\*\*', section))
                if bold_count > 3:
                    errors.append(f"WARNING: Section {i+1} has {bold_count} bold terms (max 3)")
        
        return errors

    def validate_directory(self, directory: Path) -> Dict[str, List[str]]:
        """Validate all markdown files in directory"""
        results = {}
        
        for md_file in directory.rglob('*.md'):
            if md_file.name.startswith('.'):
                continue
                
            errors = self.validate_file(md_file)
            if errors:
                results[str(md_file)] = errors
        
        return results

def main():
    """Main validation function"""
    validator = MarkdownValidator()
    
    # Get the docs directory
    docs_dir = Path('docs')
    if not docs_dir.exists():
        print("ERROR: docs directory not found")
        sys.exit(1)
    
    print("🔍 Validating Markdown files according to STYLE_GUIDE.md...")
    print("=" * 60)
    
    results = validator.validate_directory(docs_dir)
    
    if not results:
        print("✅ All files pass validation!")
        return
    
    total_errors = 0
    for filepath, errors in results.items():
        print(f"\n📄 {filepath}:")
        for error in errors:
            print(f"  {error}")
            total_errors += 1
    
    print(f"\n{'=' * 60}")
    print(f"❌ Found {total_errors} violations across {len(results)} files")
    
    if total_errors > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
