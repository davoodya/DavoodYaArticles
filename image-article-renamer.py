"""
Image Article Renamer Script
Author: Davood Yahya
Date: 2026-02-08

This script:
1. Reads title from each article
2. Finds all images in the article
3. Updates image filenames to match their alt text (without spaces)
4. Syncs with physical filenames in static/images/

Example:
  Alt text: "MSFConsole Commands-1"
  Old: ![MSFConsole Commands-1](/images/tools/Pastedimage123.png)
  New: ![MSFConsole Commands-1](/images/tools/MSFConsoleCommands-1.png)
"""

import os
import re
from pathlib import Path
from datetime import datetime

# ==================== SETTINGS ====================

CONTENT_DIR = "content"
STATIC_IMAGES_BASE = "static/images"
LOG_FILE = "image_article_renamer.log"

# Pattern to extract title from front matter
TITLE_PATTERN = r'^title\s*=\s*["\']([^"\']+)["\']'

# Pattern to find markdown images
# Matches: ![alt text](/images/category/image.png)
IMAGE_PATTERN = r'!\[([^\]]+)\]\((/images/([^/]+)/([^)]+))\)'

# ==================== GLOBAL VARIABLES ====================

stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'images_found': 0,
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
    
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    except:
        pass  # Skip log file write if encoding issues

def remove_spaces(text):
    """Remove all spaces from text"""
    return text.replace(' ', '')

def extract_title_from_frontmatter(lines):
    """Extract title from front matter"""
    for i, line in enumerate(lines[:15]):
        match = re.match(TITLE_PATTERN, line.strip())
        if match:
            return match.group(1)
    return None

def get_category_from_path(file_path):
    """Extract category from file path"""
    parts = Path(file_path).parts
    if len(parts) >= 2 and parts[0] == 'content':
        return parts[1]
    return None

def generate_new_filename_from_alt(alt_text, old_filename):
    """
    Generate new filename from alt text (without spaces)
    
    Args:
        alt_text: "MSFConsole Commands-1"
        old_filename: "Pastedimage123.png"
    
    Returns:
        "MSFConsoleCommands-1.png"
    """
    # Get extension from old filename
    _, ext = os.path.splitext(old_filename)
    
    # Remove spaces from alt text
    new_name = remove_spaces(alt_text)
    
    # Add extension
    return f"{new_name}{ext}"

def update_article_images(file_path):
    """
    Update all image references in a single article
    
    Returns: (modified: bool, updated_count: int)
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Extract title
        title = extract_title_from_frontmatter(lines)
        if not title:
            log_message(f"  Warning: No title found", "WARNING")
            return False, 0
        
        # Get category
        category = get_category_from_path(file_path)
        if not category:
            log_message(f"  Warning: No category found", "WARNING")
            return False, 0
        
        log_message(f"  Title: '{title}'")
        log_message(f"  Category: {category}")
        
        # Join lines to work with content
        content = ''.join(lines)
        
        # Find all images
        images = re.findall(IMAGE_PATTERN, content)
        
        if not images:
            log_message(f"  No images found")
            return False, 0
        
        log_message(f"  Found {len(images)} image(s)")
        
        modified = False
        updated_count = 0
        
        # Process each image
        for alt_text, full_path, img_category, old_filename in images:
            stats['images_found'] += 1
            
            # Generate new filename from alt text (without spaces)
            new_filename = generate_new_filename_from_alt(alt_text, old_filename)
            
            # Check if already correct
            if old_filename == new_filename:
                log_message(f"    > Already correct: {new_filename}")
                stats['images_skipped'] += 1
                continue
            
            # Verify that new file exists in static/images/
            new_file_path = os.path.join(STATIC_IMAGES_BASE, img_category, new_filename)
            if not os.path.exists(new_file_path):
                log_message(f"    Warning: New file doesn't exist: {new_filename}", "WARNING")
                log_message(f"             Expected at: {new_file_path}", "WARNING")
                stats['errors'] += 1
                continue
            
            # Old and new patterns
            old_pattern = f"![{alt_text}](/images/{img_category}/{old_filename})"
            new_pattern = f"![{alt_text}](/images/{img_category}/{new_filename})"
            
            # Replace in content
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                modified = True
                updated_count += 1
                
                log_message(f"    + Updated: {old_filename}")
                log_message(f"      -> {new_filename}")
                stats['images_updated'] += 1
            else:
                log_message(f"    Warning: Pattern not found in content", "WARNING")
                stats['errors'] += 1
        
        # Save file if modified
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            log_message(f"  [Saved] {updated_count} image(s) updated")
            stats['files_modified'] += 1
        
        return modified, updated_count
        
    except Exception as e:
        log_message(f"  X Error: {e}", "ERROR")
        stats['errors'] += 1
        return False, 0

def scan_and_process():
    """Scan all markdown files and update image references"""
    log_message("="*60)
    log_message("Image Article Renamer - Starting...")
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
                
                # Get relative path
                rel_path = os.path.relpath(file_path, CONTENT_DIR)
                
                log_message(f"\n[File] {rel_path}")
                
                # Process file
                update_article_images(file_path)

def print_statistics():
    """Display final statistics"""
    log_message("\n" + "="*60)
    log_message("FINAL STATISTICS:")
    log_message("="*60)
    log_message(f"Files scanned: {stats['files_scanned']}")
    log_message(f"Files modified: {stats['files_modified']}")
    log_message(f"Images found: {stats['images_found']}")
    log_message(f"Images updated: {stats['images_updated']}")
    log_message(f"Images skipped (already correct): {stats['images_skipped']}")
    log_message(f"Errors: {stats['errors']}")
    log_message("="*60)
    
    if stats['images_updated'] > 0:
        log_message("\n[SUCCESS] Image references updated successfully!")
        log_message(f"Full log: {LOG_FILE}")
    else:
        log_message("\n[INFO] All images already have correct filenames")

def verify_setup():
    """Verify directories exist"""
    log_message("\n" + "="*60)
    log_message("Verifying setup:")
    log_message("="*60)
    
    # Check content
    if os.path.exists(CONTENT_DIR):
        log_message(f"+ Content directory: {CONTENT_DIR}")
    else:
        log_message(f"X Content directory not found: {CONTENT_DIR}", "ERROR")
        return False
    
    # Check static/images
    if os.path.exists(STATIC_IMAGES_BASE):
        log_message(f"+ Static images: {STATIC_IMAGES_BASE}")
        
        # Count categories
        categories = [d for d in os.listdir(STATIC_IMAGES_BASE) 
                     if os.path.isdir(os.path.join(STATIC_IMAGES_BASE, d))]
        log_message(f"  Categories: {', '.join(categories)}")
        
        # Count total images
        total_images = 0
        for cat in categories:
            cat_path = os.path.join(STATIC_IMAGES_BASE, cat)
            images = [f for f in os.listdir(cat_path) 
                     if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            total_images += len(images)
            log_message(f"    {cat}: {len(images)} images")
        
        log_message(f"  Total images: {total_images}")
    else:
        log_message(f"X Static images not found: {STATIC_IMAGES_BASE}", "ERROR")
        return False
    
    return True

def test_filename_generation():
    """Test filename generation"""
    log_message("\n" + "="*60)
    log_message("Testing filename generation:")
    log_message("="*60)
    
    test_cases = [
        ("MSFConsole Commands-1", "Pastedimage20250703164923.png"),
        ("SANS-401-Networking and Protocols (401.1)-12", "Pastedimage123.png"),
        ("Page Rank-2", "oldimage.jpg"),
    ]
    
    for alt_text, old_name in test_cases:
        new_name = generate_new_filename_from_alt(alt_text, old_name)
        log_message(f"  Alt: '{alt_text}'")
        log_message(f"  Old: '{old_name}'")
        log_message(f"  New: '{new_name}'")
        log_message("")

# ==================== MAIN FUNCTION ====================

def main():
    """Main function"""
    print("\n" + "="*60)
    print("Image Article Renamer Tool")
    print("="*60)
    print(f"Author: Davood Yahya")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("\nThis script will:")
    print("1. Read title from each article")
    print("2. Find all images in the article")
    print("3. Update filenames to match alt text (no spaces)")
    print("4. Sync with physical files in static/images/")
    print("\nExample:")
    print("  Before: ![MSFConsole Commands-1](/images/tools/Pastedimage123.png)")
    print("  After:  ![MSFConsole Commands-1](/images/tools/MSFConsoleCommands-1.png)")
    print("="*60 + "\n")
    
    # Start logging
    log_message("="*60)
    log_message("Starting image article renamer process")
    log_message("="*60)
    
    # Test filename generation
    test_filename_generation()
    
    # Verify setup
    if not verify_setup():
        log_message("\nX Process stopped: Setup verification failed", "ERROR")
        return
    
    # Scan and process files
    scan_and_process()
    
    # Display statistics
    print_statistics()
    
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
