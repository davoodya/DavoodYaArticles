#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TOC Remover for Hugo Articles
==============================
This script removes TOC (Table of Contents) sections from markdown files.

Process:
1. Finds TOC headers (# TOC, ## TOC, ### TOC, #### TOC, ##### TOC, ###### TOC)
2. Removes everything from TOC header until the next markdown header (H1-H6)
3. Preserves all other content

Example:
    ## TOC
    - [Link 1](#link1)
    - [Link 2](#link2)
    ---
    ### First Header
    Content here...

    Becomes:
    ### First Header
    Content here...

Author: Automated Script
Date: 2026-02-09
"""

import os
import json
import logging
import re
from pathlib import Path
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('toc_remover.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Configuration
TEST_ARTICLES_DIR = Path("test/test-articles")
TRACKING_FILE = "toc_removal_tracking.json"

# Regex patterns
# Match any header level (# to ######) followed by "TOC"
TOC_PATTERN = re.compile(r'^(#{1,6})\s+TOC\s*$', re.IGNORECASE)
# Match any header (# to ######)
HEADER_PATTERN = re.compile(r'^#{1,6}\s+.+$')


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


def find_toc_section(lines):
    """
    Find TOC section in markdown file.
    
    Returns: (toc_start_line, toc_end_line) or (None, None) if not found
    - toc_start_line: line number where TOC header is found
    - toc_end_line: line number just before the next header (exclusive)
    """
    toc_start = None
    toc_end = None
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # Check if this is a TOC header
        if TOC_PATTERN.match(line_stripped):
            toc_start = i
            logger.debug(f"  Found TOC header at line {i}: {line_stripped}")
            
            # Now find the next header after TOC
            for j in range(i + 1, len(lines)):
                next_line = lines[j].strip()
                
                # Check if this is a header (H1-H6)
                if HEADER_PATTERN.match(next_line):
                    toc_end = j
                    logger.debug(f"  Found next header at line {j}: {next_line}")
                    break
            
            # If we found TOC start, break (we only remove first TOC)
            break
    
    return toc_start, toc_end


def remove_toc_from_file(file_path):
    """
    Remove TOC section from a markdown file.
    
    Returns: True if TOC was found and removed, False otherwise
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Find TOC section
        toc_start, toc_end = find_toc_section(lines)
        
        if toc_start is None:
            logger.info(f"No TOC found in: {file_path.name}")
            return False
        
        if toc_end is None:
            logger.warning(f"TOC found but no ending header in: {file_path.name}")
            logger.warning(f"  TOC starts at line {toc_start}, but no header follows. Skipping.")
            return False
        
        logger.info(f"Found TOC in {file_path.name} from line {toc_start} to line {toc_end - 1}")
        
        # Remove TOC section (from toc_start to toc_end, excluding toc_end)
        new_lines = lines[:toc_start] + lines[toc_end:]
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        logger.info(f"✓ Successfully removed TOC from: {file_path.name}")
        logger.info(f"  Removed {toc_end - toc_start} lines")
        
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
        "toc_removed": 0,
        "no_toc_found": 0,
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
        success = remove_toc_from_file(file_path)
        
        if success:
            stats["toc_removed"] += 1
            # Add to processed files
            processed_files.add(file_name)
            tracking_data["processed_files"] = list(processed_files)
        else:
            stats["no_toc_found"] += 1
            # Still mark as processed (no need to check again)
            processed_files.add(file_name)
            tracking_data["processed_files"] = list(processed_files)
    
    # Save tracking data
    save_tracking_file(tracking_data)
    
    # Print summary
    logger.info(f"\n{'='*60}")
    logger.info("SUMMARY")
    logger.info(f"{'='*60}")
    logger.info(f"Total files found: {stats['total_files']}")
    logger.info(f"Already processed (skipped): {stats['already_processed']}")
    logger.info(f"TOC removed: {stats['toc_removed']}")
    logger.info(f"No TOC found: {stats['no_toc_found']}")
    logger.info(f"Errors: {stats['errors']}")
    logger.info(f"{'='*60}")
    
    # Generate report
    generate_report(stats, tracking_data)


def generate_report(stats, tracking_data):
    """Generate a detailed report file."""
    report_path = "toc_remover_report.txt"
    
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write("TOC REMOVER FOR HUGO ARTICLES\n")
            f.write("EXECUTION REPORT\n")
            f.write("=" * 70 + "\n\n")
            
            f.write(f"Execution Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target Directory: {TEST_ARTICLES_DIR}\n\n")
            
            f.write("-" * 70 + "\n")
            f.write("STATISTICS\n")
            f.write("-" * 70 + "\n")
            f.write(f"Total files found: {stats['total_files']}\n")
            f.write(f"Already processed (skipped): {stats['already_processed']}\n")
            f.write(f"TOC removed: {stats['toc_removed']}\n")
            f.write(f"No TOC found: {stats['no_toc_found']}\n")
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
    logger.info("TOC REMOVER FOR HUGO ARTICLES")
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
