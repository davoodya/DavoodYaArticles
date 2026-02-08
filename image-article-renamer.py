"""
Image Article Renamer Script
Author: Davood Yahya
Date: 2026-02-08

This script:
1. Reads images_rename_mapping.json
2. Updates image references in markdown files ONLY
3. Does NOT rename physical files (that's done by images-renamer.py)
4. Tracks processed articles to avoid re-processing
5. Syncs with already renamed physical files in static/images/

Example:
  Before: ![MSFConsole Commands-1](/images/tools/Pastedimage123.png)
  After:  ![MSFConsole Commands-1](/images/tools/MSFConsoleCommands-1.png)
  
Note: Run images-renamer.py FIRST to rename physical files,
      then run this script to update markdown references.
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
PROCESSED_ARTICLES_FILE = "processed_articles.json"
LOG_FILE = "image_article_renamer.log"

# Pattern to find markdown images
# Matches: ![alt text](/images/category/image.png)
IMAGE_PATTERN = r'!\[([^\]]+)\]\((/images/([^/]+)/([^)]+))\)'

# ==================== GLOBAL VARIABLES ====================

rename_mapping = {}  # Loaded from JSON
processed_articles = {}  # Track already processed articles
stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'files_skipped_already_processed': 0,
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

def load_rename_mapping():
    """Load rename mapping from JSON"""
    global rename_mapping
    
    if os.path.exists(RENAME_MAPPING_FILE):
        try:
            with open(RENAME_MAPPING_FILE, 'r', encoding='utf-8') as f:
                rename_mapping = json.load(f)
            log_message(f"Loaded {len(rename_mapping)} rename mapping(s) from {RENAME_MAPPING_FILE}")
            
            if not rename_mapping:
                log_message("WARNING: Rename mapping is empty!", "WARNING")
                log_message("         Run images-renamer.py first to generate mapping.", "WARNING")
                return False
            
            return True
        except Exception as e:
            log_message(f"Error loading rename mapping: {e}", "ERROR")
            return False
    else:
        log_message(f"X Rename mapping file not found: {RENAME_MAPPING_FILE}", "ERROR")
        log_message("  Please run images-renamer.py first to rename physical files.", "ERROR")
        return False

def load_processed_articles():
    """Load list of already processed articles"""
    global processed_articles
    
    if os.path.exists(PROCESSED_ARTICLES_FILE):
        try:
            with open(PROCESSED_ARTICLES_FILE, 'r', encoding='utf-8') as f:
                processed_articles = json.load(f)
            log_message(f"Loaded {len(processed_articles)} processed article(s) from {PROCESSED_ARTICLES_FILE}")
        except Exception as e:
            log_message(f"Error loading processed articles: {e}", "WARNING")
            processed_articles = {}
    else:
        log_message(f"No processed articles file found. Starting fresh.")
        processed_articles = {}

def save_processed_articles():
    """Save processed articles to JSON"""
    try:
        with open(PROCESSED_ARTICLES_FILE, 'w', encoding='utf-8') as f:
            json.dump(processed_articles, f, ensure_ascii=False, indent=2)
        log_message(f"Saved {len(processed_articles)} processed articles to {PROCESSED_ARTICLES_FILE}")
    except Exception as e:
        log_message(f"Error saving processed articles: {e}", "ERROR")

def get_file_hash(file_path):
    """Get a simple hash of file to detect changes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Simple hash: just count of images found
        images = re.findall(IMAGE_PATTERN, content)
        return len(images)
    except:
        return 0

def should_process_article(file_path):
    """Check if article needs processing"""
    # Get relative path as key
    rel_path = os.path.relpath(file_path, CONTENT_DIR)
    
    # Check if already processed
    if rel_path in processed_articles:
        # Get current file hash
        current_hash = get_file_hash(file_path)
        stored_hash = processed_articles[rel_path].get('image_count', 0)
        
        # If hash matches, skip
        if current_hash == stored_hash:
            return False, "already_processed"
    
    return True, "needs_processing"

def update_article_images(file_path):
    """
    Update all image references in a single article
    Uses mapping from images_rename_mapping.json
    
    Returns: (modified: bool, updated_count: int)
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
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
            
            # Check if this image is in our rename mapping
            if old_filename not in rename_mapping:
                log_message(f"    > No mapping for: {old_filename}")
                stats['images_skipped'] += 1
                continue
            
            # Get new filename from mapping
            mapping_data = rename_mapping[old_filename]
            new_filename = mapping_data.get('new_name')
            mapped_category = mapping_data.get('category')
            
            # Verify category matches
            if img_category != mapped_category:
                log_message(f"    Warning: Category mismatch for {old_filename}", "WARNING")
                log_message(f"             Found: {img_category}, Mapped: {mapped_category}", "WARNING")
                stats['errors'] += 1
                continue
            
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
                log_message(f"             Run images-renamer.py first!", "WARNING")
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
            
            # Mark as processed
            rel_path = os.path.relpath(file_path, CONTENT_DIR)
            processed_articles[rel_path] = {
                'image_count': len(images),
                'updated_count': updated_count,
                'last_processed': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        
        return modified, updated_count
        
    except Exception as e:
        log_message(f"  X Error: {e}", "ERROR")
        stats['errors'] += 1
        return False, 0

def scan_and_process():
    """Scan all markdown files and update image references"""
    log_message("="*60)
    log_message("Updating markdown image references...")
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
                
                # Check if needs processing
                should_process, reason = should_process_article(file_path)
                
                if not should_process:
                    log_message(f"  [Skip] Already processed")
                    stats['files_skipped_already_processed'] += 1
                    continue
                
                # Process file
                update_article_images(file_path)

def print_statistics():
    """Display final statistics"""
    log_message("\n" + "="*60)
    log_message("FINAL STATISTICS:")
    log_message("="*60)
    log_message(f"Files scanned: {stats['files_scanned']}")
    log_message(f"Files skipped (already processed): {stats['files_skipped_already_processed']}")
    log_message(f"Files modified: {stats['files_modified']}")
    log_message(f"Images found: {stats['images_found']}")
    log_message(f"Images updated: {stats['images_updated']}")
    log_message(f"Images skipped (no mapping/already correct): {stats['images_skipped']}")
    log_message(f"Errors: {stats['errors']}")
    log_message(f"Total processed articles tracked: {len(processed_articles)}")
    log_message("="*60)
    
    if stats['images_updated'] > 0:
        log_message("\n[SUCCESS] Image references updated successfully!")
        log_message(f"Processed articles tracked in: {PROCESSED_ARTICLES_FILE}")
        log_message(f"Full log: {LOG_FILE}")
    else:
        log_message("\n[INFO] No new image references needed updating")

def verify_setup():
    """Verify directories and mapping exist"""
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

def create_summary_report():
    """Create a summary report"""
    report_file = "image_article_renamer_report.txt"
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("Image Article Renamer Report\n")
            f.write("="*60 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            f.write("Statistics:\n")
            f.write(f"- Files scanned: {stats['files_scanned']}\n")
            f.write(f"- Files skipped (already processed): {stats['files_skipped_already_processed']}\n")
            f.write(f"- Files modified: {stats['files_modified']}\n")
            f.write(f"- Images found: {stats['images_found']}\n")
            f.write(f"- Images updated: {stats['images_updated']}\n")
            f.write(f"- Images skipped: {stats['images_skipped']}\n")
            f.write(f"- Errors: {stats['errors']}\n")
            f.write(f"- Total processed articles: {len(processed_articles)}\n\n")
            
            f.write("Processed Articles:\n")
            f.write("-"*60 + "\n")
            
            for article, data in sorted(processed_articles.items()):
                f.write(f"\n{article}:\n")
                f.write(f"  - Images found: {data.get('image_count', 0)}\n")
                f.write(f"  - Images updated: {data.get('updated_count', 0)}\n")
                f.write(f"  - Last processed: {data.get('last_processed', 'N/A')}\n")
        
        log_message(f"[Report] Summary report created: {report_file}")
        
    except Exception as e:
        log_message(f"X Error creating report: {e}", "ERROR")

# ==================== MAIN FUNCTION ====================

def main():
    """Main function"""
    print("\n" + "="*60)
    print("Image Article Renamer Tool (Markdown References Only)")
    print("="*60)
    print(f"Author: Davood Yahya")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    print("\nThis script will:")
    print("1. Load rename mapping from images_rename_mapping.json")
    print("2. Update image references in markdown files ONLY")
    print("3. Track processed articles to avoid re-processing")
    print("4. Verify renamed files exist in static/images/")
    print("\nNOTE: Run images-renamer.py FIRST to rename physical files!")
    print("\nExample:")
    print("  Before: ![MSFConsole Commands-1](/images/tools/Pastedimage123.png)")
    print("  After:  ![MSFConsole Commands-1](/images/tools/MSFConsoleCommands-1.png)")
    print("="*60 + "\n")
    
    # Start logging
    log_message("="*60)
    log_message("Starting image article renamer process")
    log_message("="*60)
    
    # Load rename mapping
    if not load_rename_mapping():
        log_message("\nX Process stopped: Could not load rename mapping", "ERROR")
        log_message("  Please run images-renamer.py first!", "ERROR")
        return
    
    # Load processed articles
    load_processed_articles()
    
    # Verify setup
    if not verify_setup():
        log_message("\nX Process stopped: Setup verification failed", "ERROR")
        return
    
    # Scan and process files
    scan_and_process()
    
    # Save processed articles
    save_processed_articles()
    
    # Display statistics
    print_statistics()
    
    # Create report if changes made
    if stats['files_modified'] > 0:
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
