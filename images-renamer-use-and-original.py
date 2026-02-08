"""
Images Renamer Script
Author: Davood Yahya
Date: 2026-02-08

This script:
1. Scans all markdown files
2. Finds all images with their alt text
3. Renames images to match alt text (without spaces)
4. Updates markdown files with new image names
5. Renames physical image files in /static/images/
6. Saves mapping to JSON for reference
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# ==================== SETTINGS ====================

CONTENT_DIR = "content"
STATIC_IMAGES_BASE = "static/images"
RENAME_MAPPING_FILE = "images_rename_mapping.json"
LOG_FILE = "images_renamer.log"

# Pattern to find markdown images
# Matches: ![alt text](/images/category/image.png)
IMAGE_PATTERN = r'!\[([^\]]+)\]\((/images/([^/]+)/([^)]+))\)'

# ==================== GLOBAL VARIABLES ====================

rename_mapping = {}  # {old_name: {"new_name": "...", "category": "...", "alt": "..."}}
stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'images_found': 0,
    'images_renamed': 0,
    'physical_files_renamed': 0,
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

def remove_spaces(text):
    """Remove all spaces from text"""
    return text.replace(' ', '')

def sanitize_for_filename(text):
    """Sanitize text for use as filename (remove spaces, keep safe chars)"""
    # Remove spaces
    text = remove_spaces(text)
    
    # Replace invalid Windows filename characters
    # Invalid chars: < > : " / \ | ? *
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        text = text.replace(char, '-')
    
    # Remove multiple consecutive hyphens
    while '--' in text:
        text = text.replace('--', '-')
    
    # Remove leading/trailing hyphens and dots
    text = text.strip('-.')
    
    return text

def generate_new_filename(alt_text, old_filename):
    """
    Generate new filename from alt text
    
    Args:
        alt_text: Alt text from markdown (e.g., "SANS-401-Networking and Protocols (401.1)-6")
        old_filename: Original filename (e.g., "Pastedimage20240620171105.png")
    
    Returns:
        New filename (e.g., "SANS-401-NetworkingandProtocols(401.1)-6.png")
    """
    # Get file extension
    _, ext = os.path.splitext(old_filename)
    
    # Sanitize alt text for filename
    safe_name = sanitize_for_filename(alt_text)
    
    # Add extension
    new_filename = f"{safe_name}{ext}"
    
    return new_filename

def update_markdown_file(file_path):
    """
    Update image references in a markdown file
    
    Returns: (modified: bool, images_processed: int)
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all images
        images = re.findall(IMAGE_PATTERN, content)
        
        if not images:
            return False, 0
        
        log_message(f"  Found {len(images)} image(s)")
        
        modified = False
        processed_count = 0
        
        # Process each image
        for alt_text, full_path, category, old_filename in images:
            stats['images_found'] += 1
            
            # Generate new filename from alt text
            new_filename = generate_new_filename(alt_text, old_filename)
            
            # Check if rename is needed
            if old_filename == new_filename:
                log_message(f"    > Already correct: {old_filename}")
                continue
            
            # Store mapping
            if old_filename not in rename_mapping:
                rename_mapping[old_filename] = {
                    'new_name': new_filename,
                    'category': category,
                    'alt': alt_text
                }
            
            # Old and new patterns in markdown
            old_pattern = f"![{alt_text}](/images/{category}/{old_filename})"
            new_pattern = f"![{alt_text}](/images/{category}/{new_filename})"
            
            # Replace in content
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                modified = True
                processed_count += 1
                
                log_message(f"    + Renamed: {old_filename}")
                log_message(f"      -> {new_filename}")
                stats['images_renamed'] += 1
            else:
                log_message(f"    Warning: Pattern not found: {old_pattern}", "WARNING")
        
        # Save file if modified
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            log_message(f"  [Saved] {processed_count} image(s) renamed in markdown")
            stats['files_modified'] += 1
        
        return modified, processed_count
        
    except Exception as e:
        log_message(f"  X Error processing {file_path}: {e}", "ERROR")
        stats['errors'] += 1
        return False, 0

def scan_and_update_markdown_files():
    """Scan all markdown files and update image references"""
    log_message("="*60)
    log_message("PHASE 1: Updating markdown files...")
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
                update_markdown_file(file_path)

def rename_physical_files():
    """Rename physical image files in /static/images/"""
    log_message("\n" + "="*60)
    log_message("PHASE 2: Renaming physical image files...")
    log_message("="*60)
    
    if not rename_mapping:
        log_message("No files to rename")
        return
    
    log_message(f"Processing {len(rename_mapping)} file(s)")
    
    # Group by category
    by_category = {}
    for old_name, data in rename_mapping.items():
        category = data['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append((old_name, data))
    
    # Process each category
    for category, files in sorted(by_category.items()):
        log_message(f"\n[Category] {category}")
        category_path = os.path.join(STATIC_IMAGES_BASE, category)
        
        if not os.path.exists(category_path):
            log_message(f"  Warning: Directory not found: {category_path}", "WARNING")
            continue
        
        # Process each file in this category
        for old_name, data in files:
            new_name = data['new_name']
            
            old_path = os.path.join(category_path, old_name)
            new_path = os.path.join(category_path, new_name)
            
            # Check if source file exists
            if not os.path.exists(old_path):
                log_message(f"  Warning: File not found: {old_name}", "WARNING")
                continue
            
            # Check if destination already exists
            if os.path.exists(new_path):
                if os.path.samefile(old_path, new_path):
                    log_message(f"  > Already renamed: {old_name}")
                    stats['physical_files_renamed'] += 1
                    continue
                else:
                    log_message(f"  Warning: Destination exists: {new_name}", "WARNING")
                    continue
            
            # Rename file
            try:
                os.rename(old_path, new_path)
                log_message(f"  + Renamed: {old_name}")
                log_message(f"    -> {new_name}")
                stats['physical_files_renamed'] += 1
            except Exception as e:
                log_message(f"  X Error renaming {old_name}: {e}", "ERROR")
                stats['errors'] += 1

def save_rename_mapping():
    """Save rename mapping to JSON"""
    try:
        with open(RENAME_MAPPING_FILE, 'w', encoding='utf-8') as f:
            json.dump(rename_mapping, f, ensure_ascii=False, indent=2)
        log_message(f"\n[JSON] Saved {len(rename_mapping)} mappings to {RENAME_MAPPING_FILE}")
    except Exception as e:
        log_message(f"X Error saving JSON: {e}", "ERROR")

def print_statistics():
    """Display final statistics"""
    log_message("\n" + "="*60)
    log_message("FINAL STATISTICS:")
    log_message("="*60)
    log_message(f"Files scanned: {stats['files_scanned']}")
    log_message(f"Files modified: {stats['files_modified']}")
    log_message(f"Images found: {stats['images_found']}")
    log_message(f"Images renamed in markdown: {stats['images_renamed']}")
    log_message(f"Physical files renamed: {stats['physical_files_renamed']}")
    log_message(f"Errors: {stats['errors']}")
    log_message(f"Total mappings: {len(rename_mapping)}")
    log_message("="*60)
    
    if stats['images_renamed'] > 0 or stats['physical_files_renamed'] > 0:
        log_message("\n[SUCCESS] Images renamed successfully!")
        log_message(f"Mapping saved to: {RENAME_MAPPING_FILE}")
        log_message(f"Full log: {LOG_FILE}")
    else:
        log_message("\n[INFO] No images needed renaming")

def create_summary_report():
    """Create a summary report"""
    report_file = "images_renamer_report.txt"
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("Images Rename Report\n")
            f.write("="*60 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            f.write("Statistics:\n")
            f.write(f"- Files scanned: {stats['files_scanned']}\n")
            f.write(f"- Files modified: {stats['files_modified']}\n")
            f.write(f"- Images found: {stats['images_found']}\n")
            f.write(f"- Images renamed: {stats['images_renamed']}\n")
            f.write(f"- Physical files renamed: {stats['physical_files_renamed']}\n")
            f.write(f"- Errors: {stats['errors']}\n")
            f.write(f"- Total mappings: {len(rename_mapping)}\n\n")
            
            f.write("Rename Mappings by Category:\n")
            f.write("-"*60 + "\n")
            
            # Group by category
            by_category = {}
            for old_name, data in rename_mapping.items():
                category = data.get('category', 'unknown')
                if category not in by_category:
                    by_category[category] = []
                by_category[category].append((old_name, data))
            
            for category, files in sorted(by_category.items()):
                f.write(f"\n{category.upper()} ({len(files)} files):\n")
                for old_name, data in sorted(files):
                    new_name = data.get('new_name')
                    alt = data.get('alt', '')
                    f.write(f"  [{alt}]\n")
                    f.write(f"  {old_name}\n")
                    f.write(f"  -> {new_name}\n\n")
        
        log_message(f"[Report] Summary report created: {report_file}")
        
    except Exception as e:
        log_message(f"X Error creating report: {e}", "ERROR")

def test_filename_generation():
    """Test filename generation"""
    log_message("\n" + "="*60)
    log_message("Testing filename generation:")
    log_message("="*60)
    
    test_cases = [
        ("SANS-401-Networking and Protocols (401.1)-6", "Pastedimage20240620171105.png"),
        ("My Test Image-1", "Pastedimage123.jpg"),
        ("Test (With) Spaces-2", "oldname.png"),
    ]
    
    for alt_text, old_name in test_cases:
        new_name = generate_new_filename(alt_text, old_name)
        log_message(f"  Alt: '{alt_text}'")
        log_message(f"  Old: '{old_name}'")
        log_message(f"  New: '{new_name}'")
        log_message("")

def verify_directories():
    """Verify that required directories exist"""
    log_message("\n" + "="*60)
    log_message("Verifying directories:")
    log_message("="*60)
    
    # Check content directory
    if os.path.exists(CONTENT_DIR):
        log_message(f"+ Content directory: {CONTENT_DIR}")
    else:
        log_message(f"X Content directory not found: {CONTENT_DIR}", "ERROR")
        return False
    
    # Check static/images directory
    if os.path.exists(STATIC_IMAGES_BASE):
        log_message(f"+ Static images directory: {STATIC_IMAGES_BASE}")
        
        # List categories
        categories = [d for d in os.listdir(STATIC_IMAGES_BASE) 
                     if os.path.isdir(os.path.join(STATIC_IMAGES_BASE, d))]
        log_message(f"  Categories: {', '.join(categories)}")
    else:
        log_message(f"X Static images directory not found: {STATIC_IMAGES_BASE}", "ERROR")
        return False
    
    return True

# ==================== MAIN FUNCTION ====================

def main():
    """Main function"""
    print("\n" + "="*60)
    print("Images Renamer Tool")
    print("="*60)
    print(f"Author: Davood Yahya")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("\nThis script will:")
    print("1. Scan all markdown files")
    print("2. Find images and their alt text")
    print("3. Rename images based on alt text (no spaces)")
    print("4. Update markdown files")
    print("5. Rename physical image files")
    print("6. Save mapping to JSON")
    print("\nExample:")
    print("  Before: ![Alt Text](/images/cat/Pastedimage123.png)")
    print("  After:  ![Alt Text](/images/cat/AltText.png)")
    print("="*60 + "\n")
    
    # Start logging
    log_message("="*60)
    log_message("Starting image rename process")
    log_message("="*60)
    
    # Test filename generation
    test_filename_generation()
    
    # Verify directories
    if not verify_directories():
        log_message("\nX Process stopped: Required directories not found", "ERROR")
        return
    
    # Phase 1: Update markdown files
    scan_and_update_markdown_files()
    
    # Save mapping
    save_rename_mapping()
    
    # Phase 2: Rename physical files
    rename_physical_files()
    
    # Display statistics
    print_statistics()
    
    # Create summary report
    if stats['images_renamed'] > 0:
        create_summary_report()
    
    log_message("\n[COMPLETE] Process finished")
    log_message("="*60 + "\n")
    
    # Show warning if there are mismatches
    if stats['images_renamed'] != stats['physical_files_renamed']:
        log_message("\nWARNING: Mismatch between markdown updates and physical renames!", "WARNING")
        log_message(f"  Markdown: {stats['images_renamed']}", "WARNING")
        log_message(f"  Physical: {stats['physical_files_renamed']}", "WARNING")
        log_message("  Please check the log file for details.", "WARNING")

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
