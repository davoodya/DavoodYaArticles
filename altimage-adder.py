"""
Alt Image Text Adder Script
Author: Davood Yahya
Date: 2026-02-08

This script:
1. Scans all markdown files
2. Extracts title from line 2: title = "..."
3. Finds all images in the article
4. Updates alt text to: title-1, title-2, title-3, etc.
"""

import os
import re
from pathlib import Path
from datetime import datetime

# ==================== SETTINGS ====================

CONTENT_DIR = "content"
LOG_FILE = "altimage_adder.log"

# Pattern to find title in front matter
TITLE_PATTERN = r'^title\s*=\s*["\']([^"\']+)["\']'

# Pattern to find markdown images
# Matches: ![anything](/images/category/image.png)
IMAGE_PATTERN = r'!\[([^\]]*)\]\((/images/[^\)]+)\)'

# ==================== GLOBAL VARIABLES ====================

stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'images_updated': 0,
    'images_skipped': 0,
    'errors': 0
}

# ==================== HELPER FUNCTIONS ====================

def log_message(message, level="INFO"):
    """Log messages to console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}"
    print(log_entry)
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')

def extract_title_from_frontmatter(lines):
    """
    Extract title from front matter (line 2)
    
    Returns: title string or None
    """
    # Check first 15 lines for title
    for i, line in enumerate(lines[:15]):
        match = re.match(TITLE_PATTERN, line.strip())
        if match:
            return match.group(1)
    
    return None

def update_image_alt_texts(file_path):
    """
    Update all image alt texts in a markdown file
    
    Returns: (modified: bool, images_updated: int)
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Extract title from front matter
        title = extract_title_from_frontmatter(lines)
        
        if not title:
            log_message(f"  Warning: No title found in {file_path}", "WARNING")
            return False, 0
        
        # Join lines to work with full content
        content = ''.join(lines)
        
        # Find all images
        images = re.findall(IMAGE_PATTERN, content)
        
        if not images:
            log_message(f"  No images found")
            return False, 0
        
        log_message(f"  Title: '{title}'")
        log_message(f"  Found {len(images)} image(s)")
        
        # Track modifications
        modified = False
        updated_count = 0
        image_counter = 0
        
        # Process each image
        for alt_text, image_path in images:
            image_counter += 1
            
            # Generate new alt text: title-1, title-2, etc.
            new_alt_text = f"{title}-{image_counter}"
            
            # Check if already has correct alt text
            if alt_text == new_alt_text:
                log_message(f"    > Already correct: {alt_text}")
                stats['images_skipped'] += 1
                continue
            
            # Old and new patterns
            old_pattern = f"![{alt_text}]({image_path})"
            new_pattern = f"![{new_alt_text}]({image_path})"
            
            # Replace in content
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                modified = True
                updated_count += 1
                
                log_message(f"    + Updated: '{alt_text}' → '{new_alt_text}'")
                stats['images_updated'] += 1
            else:
                log_message(f"    Warning: Pattern not found for replacement", "WARNING")
        
        # Save file if modified
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            log_message(f"  [Saved] {updated_count} image(s) updated")
            stats['files_modified'] += 1
        
        return modified, updated_count
        
    except Exception as e:
        log_message(f"  X Error processing {file_path}: {e}", "ERROR")
        stats['errors'] += 1
        return False, 0

def scan_and_process():
    """Scan all markdown files and update image alt texts"""
    log_message("="*60)
    log_message("Alt Image Text Adder - Starting...")
    log_message("="*60)
    
    if not os.path.exists(CONTENT_DIR):
        log_message(f"X Directory {CONTENT_DIR} not found!", "ERROR")
        return
    
    # Walk through all .md files
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                stats['files_scanned'] += 1
                
                # Get relative path for better logging
                rel_path = os.path.relpath(file_path, CONTENT_DIR)
                
                log_message(f"\n[File] {rel_path}")
                
                # Process file
                update_image_alt_texts(file_path)

def print_statistics():
    """Display final statistics"""
    log_message("\n" + "="*60)
    log_message("FINAL STATISTICS:")
    log_message("="*60)
    log_message(f"Files scanned: {stats['files_scanned']}")
    log_message(f"Files modified: {stats['files_modified']}")
    log_message(f"Images updated: {stats['images_updated']}")
    log_message(f"Images skipped (already correct): {stats['images_skipped']}")
    log_message(f"Errors: {stats['errors']}")
    log_message("="*60)
    
    if stats['images_updated'] > 0:
        log_message("\n[SUCCESS] Image alt texts updated successfully!")
        log_message(f"Full log: {LOG_FILE}")
    else:
        log_message("\n[INFO] All images already have correct alt texts")

def create_summary_report():
    """Create a summary report"""
    report_file = "altimage_adder_report.txt"
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("Image Alt Text Update Report\n")
            f.write("="*60 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            f.write("Statistics:\n")
            f.write(f"- Files scanned: {stats['files_scanned']}\n")
            f.write(f"- Files modified: {stats['files_modified']}\n")
            f.write(f"- Images updated: {stats['images_updated']}\n")
            f.write(f"- Images skipped: {stats['images_skipped']}\n")
            f.write(f"- Errors: {stats['errors']}\n\n")
            
            f.write("Description:\n")
            f.write("This script updates image alt texts to match the article title\n")
            f.write("Format: ![title-1](/images/category/image.png)\n")
            f.write("\n")
            
            f.write("Example:\n")
            f.write("Title: 'SANS-401-Defense-in-Depth (401.2)'\n")
            f.write("Alt texts: SANS-401-Defense-in-Depth (401.2)-1, -2, -3, etc.\n")
        
        log_message(f"\n[Report] Summary report created: {report_file}")
        
    except Exception as e:
        log_message(f"X Error creating report: {e}", "ERROR")

def test_patterns():
    """Test regex patterns"""
    log_message("\n" + "="*60)
    log_message("Testing patterns:")
    log_message("="*60)
    
    # Test title pattern
    test_titles = [
        'title = "SANS-401-Defense-in-Depth (401.2)"',
        "title = 'My Article Title'",
        'title="No Space Title"',
    ]
    
    log_message("\nTitle Pattern Tests:")
    for test in test_titles:
        match = re.match(TITLE_PATTERN, test)
        if match:
            log_message(f"  ✓ '{test}' → '{match.group(1)}'")
        else:
            log_message(f"  ✗ '{test}' → NO MATCH")
    
    # Test image pattern
    test_images = [
        "![Alt text](/images/cyber-security/image.png)",
        "![Old Alt](/images/seo/test.jpg)",
        "![](/images/tools/pic.png)",
    ]
    
    log_message("\nImage Pattern Tests:")
    for test in test_images:
        match = re.search(IMAGE_PATTERN, test)
        if match:
            log_message(f"  ✓ '{test}'")
            log_message(f"    Alt: '{match.group(1)}', Path: '{match.group(2)}'")
        else:
            log_message(f"  ✗ '{test}' → NO MATCH")

# ==================== MAIN FUNCTION ====================

def main():
    """Main function"""
    print("\n" + "="*60)
    print("Image Alt Text Adder Tool")
    print("="*60)
    print(f"Author: Davood Yahya")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("\nThis script will:")
    print("1. Extract title from each article")
    print("2. Find all images in the article")
    print("3. Update alt text to: title-1, title-2, title-3, etc.")
    print("="*60 + "\n")
    
    # Start logging
    log_message("="*60)
    log_message("Starting image alt text update process")
    log_message("="*60)
    
    # Test patterns
    test_patterns()
    
    # Scan and process all files
    scan_and_process()
    
    # Display statistics
    print_statistics()
    
    # Create summary report
    if stats['images_updated'] > 0:
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
