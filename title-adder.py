"""
Title Adder Script
Author: Davood Yahya
Date: 2026-02-08

This script:
1. Scans all markdown files in /content/
2. Checks if 'title = ""' exists in lines 0-15
3. If not, adds 'title = "FILE-NAME"' to line 2
4. Removes E-number patterns (E3, E45, E46, etc.) from filename
5. Saves all article titles to JSON
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# ==================== SETTINGS ====================

CONTENT_DIR = "content"
OUTPUT_JSON = "article_titles.json"
LOG_FILE = "title_adder.log"

# Excluded directories - these will not be processed
EXCLUDED_DIRS = ["all-articles"]  # List of directory names to exclude

# Regex pattern to find E-numbers: E3, E45, E46, E47, etc.
# Matches various patterns:
# - E3, E45, E46, E47 (comma separated)
# - E1 to E5 (range)
# - E10-E11 (hyphen separated)
# - E12- (trailing hyphen)
E_NUMBER_PATTERN = r'E\d+(?:\s*(?:,\s*E\d+|to\s+E\d+|-\s*E?\d+|-))*\s*[-,]?\s*'

# ==================== GLOBAL VARIABLES ====================

stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'titles_added': 0,
    'titles_existed': 0,
    'errors': 0
}

article_titles = {}  # {file_path: title}

# ==================== HELPER FUNCTIONS ====================

def log_message(message, level="INFO"):
    """Log messages to console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}"
    print(log_entry)
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')

def extract_title_from_filename(filename):
    """
    Extract title from filename by removing E-number patterns
    
    Examples:
        "E3 Virtualization.md" -> "Virtualization"
        "E45, E46, E47 - Cloud.md" -> "Cloud"
        "E10-E11 Something.md" -> "Something"
    """
    # Remove .md extension
    name = filename.replace('.md', '')
    
    # Remove E-number patterns
    # Pattern matches: E3, E45, E46, E47, etc. with various separators
    cleaned = re.sub(E_NUMBER_PATTERN, '', name, flags=re.IGNORECASE)
    
    # Clean up extra spaces and leading/trailing separators
    cleaned = cleaned.strip(' -,')
    cleaned = re.sub(r'\s+', ' ', cleaned)  # Replace multiple spaces with single space
    
    return cleaned

def check_title_exists(lines):
    """
    Check if 'title = ""' exists in first 15 lines
    
    Returns: (exists: bool, line_number: int or None)
    """
    for i, line in enumerate(lines[:15]):
        # Check for title = "..." pattern
        if re.match(r'^\s*title\s*=\s*["\']', line.strip()):
            return True, i
    
    return False, None

def add_title_to_file(file_path):
    """
    Add title to file if it doesn't exist, or fix incorrect titles
    
    Returns: (modified: bool, title: str)
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Check if title already exists
        title_exists, title_line = check_title_exists(lines)
        
        # Extract filename
        filename = os.path.basename(file_path)
        
        # Generate title from filename
        title = extract_title_from_filename(filename)
        
        if title_exists:
            # Extract existing title value
            existing_line = lines[title_line].strip()
            match = re.search(r'title\s*=\s*["\']([^"\']*)["\']', existing_line)
            if match:
                existing_title = match.group(1)
                
                # Check if existing title is incorrect (starts with "to ", etc.)
                # This happens when E-numbers were not properly removed
                if (existing_title.startswith('to ') or 
                    existing_title != title and 
                    title not in existing_title and
                    len(existing_title) < len(title)):
                    
                    # Fix the incorrect title
                    new_line = f'title = "{title}"\n'
                    lines[title_line] = new_line
                    
                    # Write back
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                    
                    log_message(f"  ! Fixed title: '{existing_title}' -> '{title}'")
                    stats['files_modified'] += 1
                    stats['titles_added'] += 1
                    return True, title
                else:
                    log_message(f"  > Title exists: '{existing_title}'")
                    stats['titles_existed'] += 1
                    return False, existing_title
            else:
                log_message(f"  > Title exists but couldn't extract value")
                stats['titles_existed'] += 1
                return False, title
        
        # Title doesn't exist - add it to line 2 (index 1)
        new_line = f'title = "{title}"\n'
        
        # Insert at line 2 (index 1)
        if len(lines) > 1:
            lines.insert(1, new_line)
        else:
            # If file has less than 2 lines, append
            lines.append(new_line)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        log_message(f"  + Added title: '{title}'")
        stats['titles_added'] += 1
        stats['files_modified'] += 1
        
        return True, title
        
    except Exception as e:
        log_message(f"  X Error processing {file_path}: {e}", "ERROR")
        stats['errors'] += 1
        return False, None

def is_excluded_path(file_path):
    """
    Check if file path contains any excluded directory.
    
    Args:
        file_path: String path of the file
    
    Returns:
        bool: True if path should be excluded, False otherwise
    """
    # Normalize path separators
    normalized_path = file_path.replace('\\', '/')
    path_parts = normalized_path.split('/')
    
    # Check if any excluded directory is in the path
    for excluded_dir in EXCLUDED_DIRS:
        if excluded_dir in path_parts:
            return True
    
    return False


def scan_and_process():
    """Scan all markdown files and add titles"""
    log_message("="*60)
    log_message("Title Adder - Starting...")
    log_message("="*60)
    
    if not os.path.exists(CONTENT_DIR):
        log_message(f"X Directory {CONTENT_DIR} not found!", "ERROR")
        return
    
    # Track excluded files
    excluded_count = 0
    
    # Walk through all .md files
    for root, dirs, files in os.walk(CONTENT_DIR):
        # Skip excluded directories at the walk level (more efficient)
        # This prevents os.walk from even entering excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                
                # Double-check: Skip if in excluded directory (safety check)
                if is_excluded_path(file_path):
                    excluded_count += 1
                    rel_path = os.path.relpath(file_path, CONTENT_DIR)
                    log_message(f"\n[Excluded] {rel_path}")
                    continue
                
                stats['files_scanned'] += 1
                
                # Get relative path for better logging
                rel_path = os.path.relpath(file_path, CONTENT_DIR)
                
                log_message(f"\n[File] {rel_path}")
                
                # Process file
                modified, title = add_title_to_file(file_path)
                
                # Store title in dictionary
                if title:
                    article_titles[rel_path] = title
    
    # Log excluded count
    if excluded_count > 0:
        log_message(f"\n[INFO] Excluded {excluded_count} files from {EXCLUDED_DIRS} directories")
    
    # Store excluded count in stats
    stats['excluded_files'] = excluded_count

def save_titles_to_json():
    """Save all article titles to JSON"""
    try:
        # Sort by path for better readability
        sorted_titles = dict(sorted(article_titles.items()))
        
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(sorted_titles, f, ensure_ascii=False, indent=2)
        
        log_message(f"\n[JSON] Saved {len(article_titles)} titles to {OUTPUT_JSON}")
        
    except Exception as e:
        log_message(f"X Error saving JSON: {e}", "ERROR")

def print_statistics():
    """Display final statistics"""
    log_message("\n" + "="*60)
    log_message("FINAL STATISTICS:")
    log_message("="*60)
    log_message(f"Files scanned: {stats['files_scanned']}")
    log_message(f"Excluded files (all-articles): {stats.get('excluded_files', 0)}")
    log_message(f"Files modified: {stats['files_modified']}")
    log_message(f"Titles added: {stats['titles_added']}")
    log_message(f"Titles already existed: {stats['titles_existed']}")
    log_message(f"Errors: {stats['errors']}")
    log_message(f"Total articles tracked: {len(article_titles)}")
    log_message("="*60)
    
    if stats['titles_added'] > 0:
        log_message("\n[SUCCESS] Titles added successfully!")
        log_message(f"Article list saved to: {OUTPUT_JSON}")
        log_message(f"Full log: {LOG_FILE}")
    else:
        log_message("\n[INFO] All files already have titles")
        log_message(f"Article list saved to: {OUTPUT_JSON}")

def create_summary_report():
    """Create a summary report"""
    report_file = "title_adder_report.txt"
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("Title Adder Report\n")
            f.write("="*60 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            f.write("Statistics:\n")
            f.write(f"- Files scanned: {stats['files_scanned']}\n")
            f.write(f"- Excluded files (all-articles): {stats.get('excluded_files', 0)}\n")
            f.write(f"- Files modified: {stats['files_modified']}\n")
            f.write(f"- Titles added: {stats['titles_added']}\n")
            f.write(f"- Titles existed: {stats['titles_existed']}\n")
            f.write(f"- Errors: {stats['errors']}\n")
            f.write(f"- Total articles: {len(article_titles)}\n\n")
            
            f.write("Article Titles:\n")
            f.write("-"*60 + "\n")
            
            # Group by category
            by_category = {}
            for path, title in sorted(article_titles.items()):
                category = path.split(os.sep)[0] if os.sep in path else 'root'
                if category not in by_category:
                    by_category[category] = []
                by_category[category].append((path, title))
            
            for category, items in sorted(by_category.items()):
                f.write(f"\n{category.upper()} ({len(items)} articles):\n")
                for path, title in items:
                    f.write(f"  [{path}]\n")
                    f.write(f"  Title: {title}\n\n")
        
        log_message(f"[Report] Summary report created: {report_file}")
        
    except Exception as e:
        log_message(f"X Error creating report: {e}", "ERROR")

def test_e_number_removal():
    """Test the E-number removal function"""
    log_message("\n" + "="*60)
    log_message("Testing E-number removal:")
    log_message("="*60)
    
    test_cases = [
        "E3 Virtualization & Cloud Infrastructure(401.1).md",
        "E45, E46, E47 - Virtualization.md",
        "E10-E11 Something Important.md",
        "E1 to E5 - SEO Intro.md",
        "Regular File Without E Number.md",
        "E100 Test File.md",
    ]
    
    for test in test_cases:
        result = extract_title_from_filename(test)
        log_message(f"  '{test}'")
        log_message(f"  -> '{result}'")

# ==================== MAIN FUNCTION ====================

def main():
    """Main function"""
    print("\n" + "="*60)
    print("Title Adder Tool")
    print("="*60)
    print(f"Author: Davood Yahya")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("\nThis script will:")
    print("1. Scan all markdown files in /content/")
    print("2. Check if 'title = \"\"' exists in first 15 lines")
    print("3. If not, add title to line 2")
    print("4. Remove E-numbers from filename (E3, E45, etc.)")
    print("5. Save all titles to JSON")
    print("="*60 + "\n")
    
    # Start logging
    log_message("="*60)
    log_message("Starting title addition process")
    log_message("="*60)
    
    # Test E-number removal
    test_e_number_removal()
    
    # Scan and process all files
    scan_and_process()
    
    # Save titles to JSON
    save_titles_to_json()
    
    # Display statistics
    print_statistics()
    
    # Create summary report
    create_summary_report()
    
    log_message("\n[COMPLETE] Process finished")
    log_message("="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nWarning: Process stopped by user")
        log_message("Process stopped by user", "WARNING")
    except Exception as e:
        print(f"\n\nX Unexpected error: {e}")
        log_message(f"Unexpected error: {e}", "ERROR")
        import traceback
        log_message(traceback.format_exc(), "ERROR")
