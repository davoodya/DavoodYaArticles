#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian Property Remover & Hugo Frontmatter Adder
==================================================
This script:
1. Extracts Date, tags, and Category from Obsidian properties
2. Removes Obsidian frontmatter properties (between first --- and second ---)
3. Adds Hugo TOML frontmatter (between +++ and +++) with:
   - title (from filename, similar to title-adder.py logic)
   - tags (directory name + extracted Obsidian tags)
   - category (directory name)
   - date (Obsidian date + current time)
   - draft = false

Author: Automated Script
Date: 2026-02-08
"""

import os
import json
import logging
import re
from pathlib import Path
from datetime import datetime
import pytz

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('obsidian_property_remover.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Configuration
TEST_ARTICLES_DIR = Path("test/test-articles")
TRACKING_FILE = "property-delete-tracking.json"
MAX_LINE_CHECK = 20  # Maximum line number to check for closing ---

# Regex pattern to find E-numbers (from title-adder.py)
# Matches: E3, E45, E46, E47 (comma separated), E1 to E5 (range), E10-E11 (hyphen)
E_NUMBER_PATTERN = r'E\d+(?:\s*(?:,\s*E\d+|to\s+E\d+|-\s*E?\d+|-))*\s*[-,]?\s*'


def load_tracking_file():
    """Load the tracking file to see which articles have been processed."""
    if os.path.exists(TRACKING_FILE):
        try:
            with open(TRACKING_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                logger.info(f"Loaded tracking file with {len(data.get('processed_files', []))} processed files")
                return data
        except Exception as e:
            logger.error(f"Error loading tracking file: {e}")
            return {"processed_files": [], "last_run": None}
    else:
        logger.info("No tracking file found, creating new one")
        return {"processed_files": [], "last_run": None}


def save_tracking_file(tracking_data):
    """Save the tracking file with processed articles."""
    try:
        tracking_data["last_run"] = datetime.now().isoformat()
        with open(TRACKING_FILE, 'w', encoding='utf-8') as f:
            json.dump(tracking_data, f, ensure_ascii=False, indent=2)
        logger.info(f"Tracking file saved with {len(tracking_data['processed_files'])} processed files")
    except Exception as e:
        logger.error(f"Error saving tracking file: {e}")


def extract_title_from_filename(filename):
    """
    Extract title from filename by removing E-number patterns.
    Logic taken from title-adder.py
    
    Examples:
        "E3 Virtualization.md" -> "Virtualization"
        "E45, E46, E47 - Cloud.md" -> "Cloud"
        "E10-E11 Something.md" -> "Something"
        "@E16 to E21 - (Cracking Windows Password).md" -> "(Cracking Windows Password)"
    """
    # Remove .md extension
    name = filename.replace('.md', '')
    
    # Remove @ symbol if present at the beginning
    name = name.lstrip('@')
    
    # Remove E-number patterns
    cleaned = re.sub(E_NUMBER_PATTERN, '', name, flags=re.IGNORECASE)
    
    # Clean up extra spaces and leading/trailing separators
    cleaned = cleaned.strip(' -,')
    cleaned = re.sub(r'\s+', ' ', cleaned)  # Replace multiple spaces with single space
    
    return cleaned


def get_directory_name(file_path):
    """
    Get the directory name (category/tag) from file path.
    
    For test/test-articles/file.md -> returns "test-articles"
    For content/cyber-security/file.md -> returns "cyber-security"
    """
    parent_dir = file_path.parent.name
    return parent_dir


def get_current_time_str():
    """
    Get current time in HH:MM:SS format with Tehran timezone.
    Format: "12:38:14"
    """
    # Tehran timezone
    tehran_tz = pytz.timezone('Asia/Tehran')
    now = datetime.now(tehran_tz)
    
    return now.strftime("%H:%M:%S")


def get_current_datetime_str():
    """
    Get current datetime in Hugo format with Tehran timezone.
    Format: "2024-06-20T12:38:14+03:30"
    """
    # Tehran timezone
    tehran_tz = pytz.timezone('Asia/Tehran')
    now = datetime.now(tehran_tz)
    
    # Format: 2024-06-20T12:38:14+03:30
    # strftime with %z gives +0330, we need to add the colon
    dt_str = now.strftime("%Y-%m-%dT%H:%M:%S%z")
    # Insert colon: +0330 -> +03:30
    if len(dt_str) >= 2:
        dt_str = dt_str[:-2] + ':' + dt_str[-2:]
    return dt_str


def parse_obsidian_properties(lines, first_line, second_line):
    """
    Parse Obsidian properties from frontmatter lines.
    Extracts: Date, tags, Category
    
    Returns: dict with keys: date, tags (list), category
    
    Example Obsidian properties:
        Date: 2023-11-20
        tags:
          - tag1
          - tag2
        Category: category1
    """
    properties = {
        'date': None,
        'tags': [],
        'category': None
    }
    
    # Process lines between first_line and second_line
    i = first_line + 1
    while i < second_line:
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Parse Date
        if line.lower().startswith('date:'):
            date_value = line.split(':', 1)[1].strip()
            properties['date'] = date_value
            logger.debug(f"  Found Date: {date_value}")
            i += 1
            continue
        
        # Parse Category
        if line.lower().startswith('category:'):
            category_value = line.split(':', 1)[1].strip()
            properties['category'] = category_value
            logger.debug(f"  Found Category: {category_value}")
            i += 1
            continue
        
        # Parse tags (can be multi-line)
        if line.lower().startswith('tags:'):
            # Check if tags are on same line or next lines
            tags_value = line.split(':', 1)[1].strip()
            
            if tags_value:
                # Tags on same line (e.g., "tags: tag1, tag2")
                # Could be array format: [tag1, tag2]
                if tags_value.startswith('[') and tags_value.endswith(']'):
                    # Array format
                    tags_str = tags_value[1:-1]
                    tags_list = [t.strip().strip('"').strip("'") for t in tags_str.split(',')]
                    properties['tags'].extend([t for t in tags_list if t])
                else:
                    # Comma separated
                    tags_list = [t.strip() for t in tags_value.split(',')]
                    properties['tags'].extend([t for t in tags_list if t])
            else:
                # Tags on next lines (YAML list format)
                i += 1
                while i < second_line:
                    next_line = lines[i].strip()
                    
                    # Check if line starts with dash (list item)
                    if next_line.startswith('- '):
                        tag = next_line[2:].strip()
                        properties['tags'].append(tag)
                        logger.debug(f"  Found tag: {tag}")
                        i += 1
                    elif next_line.startswith('-'):
                        tag = next_line[1:].strip()
                        properties['tags'].append(tag)
                        logger.debug(f"  Found tag: {tag}")
                        i += 1
                    else:
                        # Not a list item, break
                        break
                continue
        
        i += 1
    
    logger.info(f"  Extracted properties: date={properties['date']}, tags={properties['tags']}, category={properties['category']}")
    
    return properties


def generate_hugo_frontmatter(file_path, obsidian_props):
    """
    Generate Hugo TOML frontmatter for the file.
    Uses Obsidian properties if available.
    
    Args:
        file_path: Path to the markdown file
        obsidian_props: dict with 'date', 'tags', 'category' from Obsidian
    
    Returns: string with frontmatter content
    """
    filename = file_path.name
    title = extract_title_from_filename(filename)
    directory = get_directory_name(file_path)
    
    # Build tags list: directory + obsidian tags
    tags_list = [directory]
    if obsidian_props['tags']:
        tags_list.extend(obsidian_props['tags'])
    
    # Format tags for TOML
    tags_str = ', '.join([f'"{tag}"' for tag in tags_list])
    
    # Build date: Obsidian date + current time
    if obsidian_props['date']:
        # Parse Obsidian date (format: 2023-11-20)
        try:
            date_part = obsidian_props['date']
            # Remove any time component if present
            if 'T' in date_part:
                date_part = date_part.split('T')[0]
            
            time_part = get_current_time_str()
            
            # Get timezone
            tehran_tz = pytz.timezone('Asia/Tehran')
            now = datetime.now(tehran_tz)
            tz_str = now.strftime("%z")
            # Insert colon: +0330 -> +03:30
            if len(tz_str) >= 2:
                tz_str = tz_str[:-2] + ':' + tz_str[-2:]
            
            date_str = f"{date_part}T{time_part}{tz_str}"
        except Exception as e:
            logger.warning(f"  Error parsing Obsidian date '{obsidian_props['date']}': {e}")
            date_str = get_current_datetime_str()
    else:
        date_str = get_current_datetime_str()
    
    # Use directory as category (ignore Obsidian category for now)
    category = directory
    
    frontmatter = f'''+++
title = "{title}"
tags = [{tags_str}]
category = "{category}"
date = "{date_str}"
draft = false
+++
'''
    
    return frontmatter


def has_obsidian_properties(lines):
    """
    Check if file has Obsidian properties (frontmatter).
    Returns: (has_properties, first_dash_line, second_dash_line) or (False, -1, -1)
    """
    first_dash_line = -1
    second_dash_line = -1
    
    # Check first 3 lines for opening ---
    for i in range(min(3, len(lines))):
        line = lines[i].strip()
        # Check if line is exactly three dashes (not more)
        if line == "---":
            first_dash_line = i
            logger.debug(f"Found first --- at line {i}")
            break
    
    # If no opening --- found, return False
    if first_dash_line == -1:
        return False, -1, -1
    
    # Look for closing --- between line after first_dash_line and line 20
    for i in range(first_dash_line + 1, min(MAX_LINE_CHECK, len(lines))):
        line = lines[i].strip()
        # Check if line is exactly three dashes (not more)
        if line == "---":
            second_dash_line = i
            logger.debug(f"Found second --- at line {i}")
            break
    
    # If second --- found, we have properties
    if second_dash_line != -1:
        return True, first_dash_line, second_dash_line
    
    return False, -1, -1


def has_hugo_frontmatter(lines):
    """
    Check if file already has Hugo TOML frontmatter (between +++ and +++).
    Returns: True if found, False otherwise
    """
    # Check first 3 lines for opening +++
    for i in range(min(3, len(lines))):
        if lines[i].strip() == "+++":
            # Found opening +++, look for closing +++
            for j in range(i + 1, min(15, len(lines))):
                if lines[j].strip() == "+++":
                    logger.debug(f"Found Hugo frontmatter from line {i} to {j}")
                    return True
    
    return False


def remove_obsidian_properties_and_add_hugo_frontmatter(file_path):
    """
    Remove Obsidian properties from a markdown file and add Hugo TOML frontmatter.
    Extracts Date, tags, Category from Obsidian properties before removal.
    Returns: True if file was modified, False otherwise
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        
        # Check if file already has Hugo frontmatter
        if has_hugo_frontmatter(lines):
            logger.info(f"Hugo frontmatter already exists in: {file_path.name}")
            return False
        
        # Check if file has Obsidian properties
        has_props, first_line, second_line = has_obsidian_properties(lines)
        
        # Default properties if no Obsidian properties found
        obsidian_props = {
            'date': None,
            'tags': [],
            'category': None
        }
        
        if has_props:
            logger.info(f"Found Obsidian properties in {file_path.name} from line {first_line} to line {second_line}")
            
            # Extract properties before removal
            obsidian_props = parse_obsidian_properties(lines, first_line, second_line)
            
            # Remove lines from first_line to second_line (inclusive)
            lines = lines[:first_line] + lines[second_line + 1:]
            
            logger.info(f"✓ Removed Obsidian properties from: {file_path.name}")
            modified = True
        else:
            logger.info(f"No Obsidian properties found in: {file_path.name}")
        
        # Generate Hugo frontmatter with extracted properties
        frontmatter = generate_hugo_frontmatter(file_path, obsidian_props)
        
        # Add Hugo frontmatter at the beginning
        lines.insert(0, frontmatter)
        
        logger.info(f"✓ Added Hugo frontmatter to: {file_path.name}")
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        return False


def process_articles():
    """Process all markdown files in the test articles directory."""
    
    # Check if directory exists
    if not TEST_ARTICLES_DIR.exists():
        logger.error(f"Directory not found: {TEST_ARTICLES_DIR}")
        return
    
    # Load tracking data
    tracking_data = load_tracking_file()
    processed_files = set(tracking_data.get("processed_files", []))
    
    # Get all markdown files
    markdown_files = list(TEST_ARTICLES_DIR.glob("*.md"))
    
    if not markdown_files:
        logger.warning(f"No markdown files found in {TEST_ARTICLES_DIR}")
        return
    
    logger.info(f"Found {len(markdown_files)} markdown files to check")
    logger.info(f"Already processed: {len(processed_files)} files")
    
    # Statistics
    stats = {
        "total_files": len(markdown_files),
        "already_processed": 0,
        "newly_processed": 0,
        "no_changes": 0,
        "errors": 0
    }
    
    # Process each file
    for file_path in markdown_files:
        file_name = file_path.name
        
        # Skip if already processed
        if file_name in processed_files:
            logger.info(f"⊙ Skipping already processed file: {file_name}")
            stats["already_processed"] += 1
            continue
        
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing: {file_name}")
        logger.info(f"{'='*60}")
        
        # Try to process file
        success = remove_obsidian_properties_and_add_hugo_frontmatter(file_path)
        
        if success:
            # Add to processed files
            processed_files.add(file_name)
            tracking_data["processed_files"] = list(processed_files)
            stats["newly_processed"] += 1
        else:
            stats["no_changes"] += 1
    
    # Save tracking data
    save_tracking_file(tracking_data)
    
    # Print summary
    logger.info(f"\n{'='*60}")
    logger.info("SUMMARY")
    logger.info(f"{'='*60}")
    logger.info(f"Total files found: {stats['total_files']}")
    logger.info(f"Already processed (skipped): {stats['already_processed']}")
    logger.info(f"Newly processed (modified): {stats['newly_processed']}")
    logger.info(f"No changes needed: {stats['no_changes']}")
    logger.info(f"Errors: {stats['errors']}")
    logger.info(f"{'='*60}")
    
    # Generate report
    generate_report(stats, tracking_data)


def generate_report(stats, tracking_data):
    """Generate a detailed report file."""
    report_path = "obsidian_property_remover_report.txt"
    
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write("OBSIDIAN PROPERTY REMOVER & HUGO FRONTMATTER ADDER\n")
            f.write("EXECUTION REPORT\n")
            f.write("=" * 70 + "\n\n")
            
            f.write(f"Execution Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target Directory: {TEST_ARTICLES_DIR}\n\n")
            
            f.write("-" * 70 + "\n")
            f.write("STATISTICS\n")
            f.write("-" * 70 + "\n")
            f.write(f"Total files found: {stats['total_files']}\n")
            f.write(f"Already processed (skipped): {stats['already_processed']}\n")
            f.write(f"Newly processed (modified): {stats['newly_processed']}\n")
            f.write(f"No changes needed: {stats['no_changes']}\n")
            f.write(f"Errors: {stats['errors']}\n\n")
            
            f.write("-" * 70 + "\n")
            f.write("PROCESSED FILES LIST\n")
            f.write("-" * 70 + "\n")
            for idx, file_name in enumerate(sorted(tracking_data['processed_files']), 1):
                f.write(f"{idx}. {file_name}\n")
            
            f.write("\n" + "=" * 70 + "\n")
            f.write("Report generated successfully\n")
            f.write("=" * 70 + "\n")
        
        logger.info(f"\n✓ Report saved to: {report_path}")
        
    except Exception as e:
        logger.error(f"Error generating report: {e}")


def main():
    """Main execution function."""
    logger.info("\n" + "=" * 70)
    logger.info("OBSIDIAN PROPERTY REMOVER & HUGO FRONTMATTER ADDER")
    logger.info("SCRIPT STARTED")
    logger.info("=" * 70 + "\n")
    
    try:
        process_articles()
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
    
    logger.info("\n" + "=" * 70)
    logger.info("SCRIPT EXECUTION COMPLETED")
    logger.info("=" * 70 + "\n")


if __name__ == "__main__":
    main()
