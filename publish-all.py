"""
Publish All Articles Script
Author: Davood Yahya
Date: 2026-02-08

This script changes 'draft = true' to 'draft = false' in all markdown files
"""

import os
import re
from pathlib import Path

CONTENT_DIR = "content"

stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'already_published': 0
}

def publish_file(file_path):
    """Change draft = true to draft = false"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has 'draft = true'
        if 'draft = true' in content:
            # Replace it
            new_content = content.replace('draft = true', 'draft = false')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Published: {file_path}")
            stats['files_modified'] += 1
        elif 'draft = false' in content:
            print(f"  Already published: {file_path}")
            stats['already_published'] += 1
        else:
            print(f"  No draft field: {file_path}")
            
    except Exception as e:
        print(f"✗ Error: {file_path}: {e}")

def main():
    print("="*60)
    print("Publish All Articles")
    print("="*60)
    print()
    
    if not os.path.exists(CONTENT_DIR):
        print(f"✗ Directory {CONTENT_DIR} not found!")
        return
    
    # Walk through all .md files
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                stats['files_scanned'] += 1
                publish_file(file_path)
    
    print()
    print("="*60)
    print("Statistics:")
    print("="*60)
    print(f"Files scanned: {stats['files_scanned']}")
    print(f"Files published: {stats['files_modified']}")
    print(f"Already published: {stats['already_published']}")
    print("="*60)
    print()
    
    if stats['files_modified'] > 0:
        print("✓ Articles published successfully!")
        print("Next: Run 'hugo' to build the site")
    else:
        print("ℹ All articles are already published")

if __name__ == "__main__":
    main()
