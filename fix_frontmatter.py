"""
Fix Front Matter Script
Author: Davood Yahya
Date: 2026-02-08

This script fixes front matter issues in markdown files:
- Converts YAML-style arrays in TOML to proper TOML format
- Fixes inconsistent key-value pairs (mix of : and =)
- Ensures proper TOML syntax
"""

import os
import re
from pathlib import Path

CONTENT_DIR = "content"
LOG_FILE = "frontmatter_fix.log"

stats = {
    'files_scanned': 0,
    'files_fixed': 0,
    'errors': 0
}

def log_message(message):
    """Log messages"""
    print(message)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def fix_frontmatter(content):
    """Fix TOML front matter format"""
    # Check if file has front matter
    if not content.startswith('+++'):
        return content, False
    
    # Split front matter and body
    parts = content.split('+++', 2)
    if len(parts) < 3:
        return content, False
    
    frontmatter = parts[1]
    body = parts[2]
    
    # Check if needs fixing
    needs_fix = False
    
    # Pattern 1: YAML-style arrays (tags:\n  - item)
    if re.search(r'\w+:\s*\n\s+-', frontmatter):
        needs_fix = True
    
    # Pattern 2: Mixed : and = syntax
    if ':' in frontmatter and '=' in frontmatter:
        needs_fix = True
    
    if not needs_fix:
        return content, False
    
    # Fix the front matter
    lines = frontmatter.strip().split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Check for YAML-style array
        if ':' in line and '=' not in line:
            key_value = line.split(':', 1)
            if len(key_value) == 2:
                key = key_value[0].strip()
                value = key_value[1].strip()
                
                # If value is empty and next lines are array items
                if not value and i + 1 < len(lines) and lines[i + 1].strip().startswith('-'):
                    # Collect array items
                    array_items = []
                    i += 1
                    while i < len(lines) and lines[i].strip().startswith('-'):
                        item = lines[i].strip()[1:].strip()
                        array_items.append(f'"{item}"')
                        i += 1
                    
                    # Create TOML array
                    fixed_lines.append(f'{key} = [{", ".join(array_items)}]')
                    continue
                else:
                    # Regular key-value pair, convert to TOML
                    if value:
                        # Remove quotes if already present and re-add
                        value = value.strip("'\"")
                        fixed_lines.append(f'{key} = "{value}"')
                    else:
                        fixed_lines.append(f'{key} = ""')
        
        # Line already in TOML format (has =)
        elif '=' in line:
            # Just ensure proper quote style
            parts = line.split('=', 1)
            key = parts[0].strip()
            value = parts[1].strip()
            
            # Standardize quotes to double quotes
            if value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
                value = f'"{value}"'
            elif not value.startswith('"') and not value.startswith('['):
                # Not quoted and not an array
                if value.lower() in ['true', 'false']:
                    # Boolean
                    fixed_lines.append(f'{key} = {value}')
                else:
                    # String
                    value = value.strip("'\"")
                    fixed_lines.append(f'{key} = "{value}"')
            else:
                fixed_lines.append(line)
        else:
            # Unknown format, keep as is
            fixed_lines.append(line)
        
        i += 1
    
    # Reconstruct content
    new_frontmatter = '\n'.join(fixed_lines)
    new_content = f"+++\n{new_frontmatter}\n+++{body}"
    
    return new_content, True

def fix_file(file_path):
    """Fix front matter in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, was_fixed = fix_frontmatter(content)
        
        if was_fixed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            log_message(f"  [FIXED] {file_path}")
            stats['files_fixed'] += 1
        
    except Exception as e:
        log_message(f"  [ERROR] {file_path}: {e}")
        stats['errors'] += 1

def scan_and_fix():
    """Scan all markdown files and fix front matter"""
    log_message("="*60)
    log_message("Front Matter Fix - Starting...")
    log_message("="*60)
    
    if not os.path.exists(CONTENT_DIR):
        log_message(f"ERROR: {CONTENT_DIR} not found!")
        return
    
    # Walk through all .md files
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                stats['files_scanned'] += 1
                fix_file(file_path)
    
    # Print statistics
    log_message("\n" + "="*60)
    log_message("STATISTICS:")
    log_message("="*60)
    log_message(f"Files scanned: {stats['files_scanned']}")
    log_message(f"Files fixed: {stats['files_fixed']}")
    log_message(f"Errors: {stats['errors']}")
    log_message("="*60)
    
    if stats['files_fixed'] > 0:
        log_message("\n[SUCCESS] Front matter fixed successfully!")
    else:
        log_message("\n[INFO] No files needed fixing")

if __name__ == "__main__":
    try:
        scan_and_fix()
    except Exception as e:
        log_message(f"UNEXPECTED ERROR: {e}")
        import traceback
        log_message(traceback.format_exc())
