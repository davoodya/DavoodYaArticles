"""
Image Migration Script - Step 1, 2 & 3
Author: Davood Yahya
Date: 2026-02-08

This script:
1. Scans all markdown files for Obsidian image links
2. Finds images in H:\Files\Obsidian\Handouts\VaultData\Attachments\
3. Copies them to /static/images/category-name/
4. Renames them by removing spaces (e.g., "Pasted image.png" -> "Pastedimage.png")
5. Converts Obsidian format to standard Markdown with correct paths
"""

import os
import re
import shutil
import json
from pathlib import Path
from datetime import datetime

# ==================== SETTINGS ====================

# Obsidian images directory path
OBSIDIAN_IMAGES_DIR = r"H:\Files\Obsidian\Handouts\VaultData\Attachments"

# Content folder path
CONTENT_DIR = "content"

# Static images base path
STATIC_IMAGES_BASE = "static/images"

# JSON file to track processed images
PROCESSED_IMAGES_FILE = "processed_images.json"

# Log file
LOG_FILE = "image_migration.log"

# Pattern to find Obsidian image links
# Example: ![[Pasted image 20260205202337.png]]
OBSIDIAN_IMAGE_PATTERN = r'!\[\[([^\]]+?\.(png|jpg|jpeg|gif|webp|svg|bmp|tiff))\]\]'

# ==================== GLOBAL VARIABLES ====================

# Track images: {original_name_with_spaces: {"new_name": "...", "category": "..."}}
processed_images = {}

stats = {
    'files_scanned': 0,
    'images_found': 0,
    'images_copied': 0,
    'images_renamed': 0,
    'images_skipped': 0,
    'files_converted': 0,
    'links_converted': 0,
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

def load_processed_images():
    """Load previously processed images"""
    global processed_images
    
    if os.path.exists(PROCESSED_IMAGES_FILE):
        try:
            with open(PROCESSED_IMAGES_FILE, 'r', encoding='utf-8') as f:
                processed_images = json.load(f)
            log_message(f"Loaded {len(processed_images)} previously processed images")
        except Exception as e:
            log_message(f"Error loading JSON: {e}", "ERROR")
            processed_images = {}
    else:
        processed_images = {}
        log_message("No previous JSON file found - starting fresh")

def save_processed_images():
    """Save processed images to JSON"""
    try:
        with open(PROCESSED_IMAGES_FILE, 'w', encoding='utf-8') as f:
            json.dump(processed_images, f, ensure_ascii=False, indent=2)
        log_message(f"Saved {len(processed_images)} images to JSON")
    except Exception as e:
        log_message(f"Error saving JSON: {e}", "ERROR")

def remove_spaces_from_filename(filename):
    """Remove all spaces from filename"""
    # Split into name and extension
    name, ext = os.path.splitext(filename)
    # Remove spaces
    name_no_spaces = name.replace(' ', '')
    # Return filename without spaces
    return name_no_spaces + ext

def get_category_from_path(file_path):
    """Extract category name from file path"""
    # Example: content/cyber-security/article.md -> cyber-security
    parts = Path(file_path).parts
    
    if len(parts) >= 2 and parts[0] == 'content':
        return parts[1]
    
    return None

def is_image_already_processed(original_name, category):
    """Check if image has been processed before"""
    if original_name in processed_images:
        data = processed_images[original_name]
        if isinstance(data, dict):
            return data.get('category') == category
        else:
            # Old format compatibility
            return True
    return False

def get_new_filename(original_name):
    """Get new filename (without spaces) for an image"""
    if original_name in processed_images:
        data = processed_images[original_name]
        if isinstance(data, dict):
            return data.get('new_name', remove_spaces_from_filename(original_name))
        else:
            # Old format - data is the new name
            return data
    else:
        # Generate new name by removing spaces
        return remove_spaces_from_filename(original_name)

def copy_and_rename_image(original_name, category):
    """
    Copy image from Obsidian to static/images/category-name/ and rename by removing spaces
    
    Args:
        original_name: Original filename (may contain spaces)
        category: Category name for subdirectory
        
    Returns:
        tuple: (success: bool, new_name: str)
    """
    # Generate new filename without spaces
    new_name = remove_spaces_from_filename(original_name)
    
    # Source path in Obsidian
    source_path = os.path.join(OBSIDIAN_IMAGES_DIR, original_name)
    
    # Destination directory: static/images/category-name/
    dest_dir = os.path.join(STATIC_IMAGES_BASE, category)
    dest_path = os.path.join(dest_dir, new_name)
    
    # Check if source exists
    if not os.path.exists(source_path):
        log_message(f"  X Image not found in Obsidian: {original_name}", "WARNING")
        stats['errors'] += 1
        return False, None
    
    # Check if already copied
    if os.path.exists(dest_path):
        # Verify file size to ensure it's the same file
        if os.path.getsize(source_path) == os.path.getsize(dest_path):
            log_message(f"  > Already exists (skipped): {new_name}")
            stats['images_skipped'] += 1
            return True, new_name
    
    # Create static/images/category-name/ directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)
        log_message(f"+ Created directory: {dest_dir}")
    
    # Copy file
    try:
        shutil.copy2(source_path, dest_path)
        log_message(f"  + Copied: {original_name}")
        log_message(f"    -> {new_name}")
        stats['images_copied'] += 1
        
        # If name changed (had spaces)
        if original_name != new_name:
            stats['images_renamed'] += 1
            log_message(f"    (Renamed: removed spaces)")
        
        return True, new_name
        
    except Exception as e:
        log_message(f"  X Error copying {original_name}: {e}", "ERROR")
        stats['errors'] += 1
        return False, None

def find_images_in_file(file_path):
    """Find all Obsidian image references in a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references
        images = re.findall(OBSIDIAN_IMAGE_PATTERN, content, re.IGNORECASE)
        
        # Return list of image names (first group from regex)
        return [img[0] for img in images]
        
    except Exception as e:
        log_message(f"X Error reading {file_path}: {e}", "ERROR")
        stats['errors'] += 1
        return []

def convert_markdown_file(file_path):
    """Convert Obsidian image links to standard Markdown format"""
    category = get_category_from_path(file_path)
    
    if not category:
        log_message(f"Warning: No category found for {file_path}", "WARNING")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references
        images = re.findall(OBSIDIAN_IMAGE_PATTERN, content, re.IGNORECASE)
        
        if not images:
            return  # No images in this file
        
        modified = False
        converted_count = 0
        
        for image_name, ext in images:
            # Get new filename (without spaces)
            new_name = get_new_filename(image_name)
            
            # Old pattern: ![[Pasted image 20260205202337.png]]
            old_pattern = f"![[{image_name}]]"
            
            # New pattern: ![Alt text](/images/category-name/Pastedimage20260205202337.png)
            # Path starts with /images/ (not /static/images/)
            new_pattern = f"![Alt text](/images/{category}/{new_name})"
            
            # Replace in content
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                modified = True
                converted_count += 1
                log_message(f"    Converted: {image_name}")
                log_message(f"    -> {new_pattern}")
        
        # Save file if modified
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            log_message(f"  [Saved] {converted_count} link(s) converted")
            stats['files_converted'] += 1
            stats['links_converted'] += converted_count
            
    except Exception as e:
        log_message(f"X Error converting {file_path}: {e}", "ERROR")
        stats['errors'] += 1

def scan_and_copy_images():
    """Scan all markdown files and copy images"""
    log_message("\n" + "="*60)
    log_message("PHASE 1: Scanning markdown files for images...")
    log_message("="*60)
    
    if not os.path.exists(CONTENT_DIR):
        log_message(f"X Directory {CONTENT_DIR} does not exist!", "ERROR")
        return
    
    # Collect images with their categories: {image_name: [categories]}
    images_by_category = {}
    
    # Walk through all .md files
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                stats['files_scanned'] += 1
                
                category = get_category_from_path(file_path)
                if not category:
                    continue
                
                # Find images in this file
                images = find_images_in_file(file_path)
                
                if images:
                    log_message(f"\n[File] {file_path}")
                    log_message(f"  Category: {category}")
                    log_message(f"  Found {len(images)} image(s)")
                    
                    for img in images:
                        if img not in images_by_category:
                            images_by_category[img] = set()
                        images_by_category[img].add(category)
                        stats['images_found'] += 1
    
    # Summary of found images
    unique_images = len(images_by_category)
    log_message(f"\n" + "="*60)
    log_message(f"SUMMARY: Found {stats['images_found']} image references")
    log_message(f"         ({unique_images} unique images)")
    log_message("="*60)
    
    # Now copy all images to their respective categories
    log_message("\n" + "="*60)
    log_message("PHASE 2: Copying images from Obsidian...")
    log_message("="*60)
    
    if not images_by_category:
        log_message("No images to copy")
        return
    
    for original_name, categories in sorted(images_by_category.items()):
        # If image is used in multiple categories, use the first one
        category = sorted(categories)[0]
        
        if len(categories) > 1:
            log_message(f"\n  Note: {original_name} used in multiple categories: {categories}")
            log_message(f"        Using category: {category}")
        
        # Check if already processed
        if is_image_already_processed(original_name, category):
            data = processed_images[original_name]
            if isinstance(data, dict):
                new_name = data.get('new_name')
            else:
                new_name = data
            log_message(f"  > Already processed: {original_name} -> {new_name}")
            stats['images_skipped'] += 1
            continue
        
        # Copy and rename
        success, new_name = copy_and_rename_image(original_name, category)
        
        if success and new_name:
            # Mark as processed
            processed_images[original_name] = {
                'new_name': new_name,
                'category': category
            }

def verify_obsidian_directory():
    """Verify Obsidian directory exists"""
    if not os.path.exists(OBSIDIAN_IMAGES_DIR):
        log_message(f"X Obsidian directory not found: {OBSIDIAN_IMAGES_DIR}", "ERROR")
        log_message("Please check the path in the script", "ERROR")
        return False
    
    log_message(f"+ Obsidian directory found: {OBSIDIAN_IMAGES_DIR}")
    
    # Count available images
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.tiff')
    try:
        image_count = len([f for f in os.listdir(OBSIDIAN_IMAGES_DIR) 
                           if f.lower().endswith(image_extensions)])
        log_message(f"+ Total images in Obsidian: {image_count}")
    except Exception as e:
        log_message(f"Warning: Error reading Obsidian images: {e}", "WARNING")
    
    return True

def convert_all_markdown_files():
    """Convert Obsidian image links to Markdown in all files"""
    log_message("\n" + "="*60)
    log_message("PHASE 3: Converting image links in markdown files...")
    log_message("="*60)
    
    if not os.path.exists(CONTENT_DIR):
        log_message(f"X Directory {CONTENT_DIR} does not exist!", "ERROR")
        return
    
    # Walk through all .md files
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                
                # Get category
                category = get_category_from_path(file_path)
                if not category:
                    continue
                
                # Find images in this file first
                images = find_images_in_file(file_path)
                
                if images:
                    log_message(f"\n[File] {file_path}")
                    log_message(f"  Category: {category}")
                    convert_markdown_file(file_path)

def print_statistics():
    """Display final statistics"""
    log_message("\n" + "="*60)
    log_message("FINAL STATISTICS:")
    log_message("="*60)
    log_message(f"Files scanned: {stats['files_scanned']}")
    log_message(f"Image references found: {stats['images_found']}")
    log_message(f"Images copied: {stats['images_copied']}")
    log_message(f"Images renamed (spaces removed): {stats['images_renamed']}")
    log_message(f"Images skipped (already exist): {stats['images_skipped']}")
    log_message(f"Files converted: {stats['files_converted']}")
    log_message(f"Links converted: {stats['links_converted']}")
    log_message(f"Errors: {stats['errors']}")
    log_message(f"Total processed images: {len(processed_images)}")
    log_message("="*60)
    
    if stats['images_copied'] > 0 or stats['files_converted'] > 0:
        log_message("\n[SUCCESS] Process completed successfully!")
        log_message(f"Images saved to: {STATIC_IMAGES_BASE}/category-name/")
        log_message(f"Tracking data: {PROCESSED_IMAGES_FILE}")
        log_message(f"Full log: {LOG_FILE}")
    else:
        log_message("\n[INFO] No new images to process")

def create_summary_report():
    """Create a summary report"""
    report_file = "image_migration_report.txt"
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("Image Migration Report - Phase 1 & 2\n")
        f.write("="*60 + "\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*60 + "\n\n")
        
        f.write("Statistics:\n")
        f.write(f"- Files scanned: {stats['files_scanned']}\n")
        f.write(f"- Image references found: {stats['images_found']}\n")
        f.write(f"- Images copied: {stats['images_copied']}\n")
        f.write(f"- Images renamed: {stats['images_renamed']}\n")
        f.write(f"- Images skipped: {stats['images_skipped']}\n")
        f.write(f"- Errors: {stats['errors']}\n")
        f.write(f"- Total processed: {len(processed_images)}\n\n")
        
        f.write("Processed Images:\n")
        f.write("-"*60 + "\n")
        
        for original, data in sorted(processed_images.items()):
            if isinstance(data, dict):
                new_name = data.get('new_name', original)
                category = data.get('category', 'unknown')
                if original != new_name:
                    f.write(f"  [{category}] {original}\n  -> {new_name}\n\n")
                else:
                    f.write(f"  [{category}] {original} (no rename needed)\n\n")
            else:
                # Old format
                if original != data:
                    f.write(f"  {original}\n  -> {data}\n\n")
                else:
                    f.write(f"  {original} (no rename needed)\n\n")
        
        f.write("="*60 + "\n")
        f.write("Conversion Details:\n")
        f.write(f"- Files converted: {stats['files_converted']}\n")
        f.write(f"- Links converted: {stats['links_converted']}\n\n")
        
        f.write("Paths:\n")
        f.write(f"- Obsidian source: {OBSIDIAN_IMAGES_DIR}\n")
        f.write(f"- Destination: {STATIC_IMAGES_BASE}/category-name/\n")
        f.write(f"- JSON tracking: {PROCESSED_IMAGES_FILE}\n")
        f.write(f"- Log file: {LOG_FILE}\n")
    
    log_message(f"\n[Report] Summary report created: {report_file}")

def verify_paths():
    """Verify and display path information"""
    log_message("\n" + "="*60)
    log_message("PATH VERIFICATION:")
    log_message("="*60)
    
    current_dir = os.getcwd()
    log_message(f"Current directory: {current_dir}")
    
    # Check content directory
    content_path = os.path.join(current_dir, CONTENT_DIR)
    if os.path.exists(content_path):
        log_message(f"+ Content directory: {content_path}")
    else:
        log_message(f"X Content directory not found: {content_path}", "ERROR")
    
    # Check static directory (will be created if needed)
    static_path = os.path.join(current_dir, STATIC_IMAGES_BASE)
    if os.path.exists(static_path):
        log_message(f"+ Static directory: {static_path}")
    else:
        log_message(f"  Static directory (will be created): {static_path}")
    
    # Check Obsidian directory
    if os.path.exists(OBSIDIAN_IMAGES_DIR):
        log_message(f"+ Obsidian directory: {OBSIDIAN_IMAGES_DIR}")
    else:
        log_message(f"X Obsidian directory not found: {OBSIDIAN_IMAGES_DIR}", "ERROR")
    
    log_message("="*60)

# ==================== MAIN FUNCTION ====================

def main():
    """Main function"""
    print("\n" + "="*60)
    print("Image Migration Tool - Complete")
    print("="*60)
    print(f"Author: Davood Yahya")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("\nThis script will:")
    print("1. Find all images used in markdown files")
    print("2. Copy them from Obsidian to /static/images/category-name/")
    print("3. Remove spaces from filenames")
    print("4. Convert Obsidian links to standard Markdown")
    print("   Format: ![Alt text](/images/category-name/image.png)")
    print("="*60 + "\n")
    
    # Start logging
    log_message("="*60)
    log_message("Starting image migration process")
    log_message("="*60)
    
    # Verify paths
    verify_paths()
    
    # Verify Obsidian directory
    if not verify_obsidian_directory():
        log_message("\nX Process stopped: Obsidian directory not found", "ERROR")
        return
    
    # Load previously processed images
    load_processed_images()
    
    # Phase 1 & 2: Scan and copy images
    scan_and_copy_images()
    
    # Save processed images after copying
    save_processed_images()
    
    # Phase 3: Convert markdown files
    convert_all_markdown_files()
    
    # Display statistics
    print_statistics()
    
    # Create summary report
    if stats['images_copied'] > 0 or len(processed_images) > 0:
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
