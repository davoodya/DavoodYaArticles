#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian Property Remover & Hugo Enhanced Frontmatter Adder
============================================================
This script:
1. Extracts Date, tags, and Category from Obsidian properties
2. Removes Obsidian frontmatter properties (between first --- and second ---)
3. Adds Hugo TOML frontmatter (between +++ and +++) with Enhanced SEO properties:
   - Basic: title, slug, date, lastmod, draft
   - Taxonomy: categories, tags, series
   - SEO: description, keywords, author, robots, canonical
   - Images: featured_image, images array
   - Open Graph & Twitter Cards
   - Reading metrics: readingTime, difficulty, toc, math, lab_required
   - Control: layout (commented), type

Author: Enhanced Script
Date: 2026-02-09
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
        logging.FileHandler('obsidian_property_remover_enhanced.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Configuration
CONTENT_DIR = Path("content")  # Changed from test/test-articles to content
TRACKING_FILE = "property-delete-tracking-enhanced.json"
MAX_LINE_CHECK = 20  # Maximum line number to check for closing ---
SITE_URL = "https://davoodya.ir"
AUTHOR_NAME = "Davood Yahay"

# Regex pattern to find E-numbers (from title-adder.py)
# Matches: E3, E45, E46, E47 (comma separated), E1 to E5 (range), E10-E11 (hyphen)
E_NUMBER_PATTERN = r'E\d+(?:\s*(?:,\s*E\d+|to\s+E\d+|-\s*E?\d+|-))*\s*[-,]?\s*'

# Regex to find markdown images: ![alt](path)
IMAGE_PATTERN = r'!\[\[([^\]]+)\]\]|!\[([^\]]*)\]\(([^\)]+)\)'


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


def slugify(text):
    """
    Convert text to URL-friendly slug.
    Replaces spaces with dashes, removes special characters.
    
    Example:
        "Google Trends" -> "google-trends"
        "OFF Page SEO" -> "off-page-seo"
    """
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with dashes
    text = text.replace(' ', '-')
    # Remove special characters except dashes
    text = re.sub(r'[^\w\-]', '', text)
    # Replace multiple dashes with single dash
    text = re.sub(r'-+', '-', text)
    # Remove leading/trailing dashes
    text = text.strip('-')
    return text


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
    Extracts: Date, tags, Category (both can be lists)
    
    Returns: dict with keys: date, tags (list), categories (list)
    
    Example Obsidian properties:
        Date: 2023-11-20
        tags:
          - tag1
          - tag2
        Category:
          - category1
          - category2
    """
    properties = {
        'date': None,
        'tags': [],
        'categories': []
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
        
        # Parse Category (can be multi-line like tags)
        if line.lower().startswith('category:'):
            # Check if category is on same line or next lines
            category_value = line.split(':', 1)[1].strip()
            
            if category_value:
                # Category on same line (e.g., "Category: cat1, cat2")
                # Could be array format: [cat1, cat2]
                if category_value.startswith('[') and category_value.endswith(']'):
                    # Array format
                    cats_str = category_value[1:-1]
                    cats_list = [c.strip().strip('"').strip("'") for c in cats_str.split(',')]
                    properties['categories'].extend([c for c in cats_list if c])
                else:
                    # Comma separated
                    cats_list = [c.strip() for c in category_value.split(',')]
                    properties['categories'].extend([c for c in cats_list if c])
            else:
                # Categories on next lines (YAML list format)
                i += 1
                while i < second_line:
                    next_line = lines[i].strip()
                    
                    # Check if line starts with dash (list item)
                    if next_line.startswith('- '):
                        cat = next_line[2:].strip()
                        properties['categories'].append(cat)
                        logger.debug(f"  Found category: {cat}")
                        i += 1
                    elif next_line.startswith('-'):
                        cat = next_line[1:].strip()
                        properties['categories'].append(cat)
                        logger.debug(f"  Found category: {cat}")
                        i += 1
                    else:
                        # Not a list item, break
                        break
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
    
    logger.info(f"  Extracted properties: date={properties['date']}, tags={properties['tags']}, categories={properties['categories']}")
    
    return properties


def extract_first_image(content_lines):
    """
    Extract the first image from article content.
    Supports both Obsidian format ![[image.png]] and Markdown format ![alt](path)
    
    Returns: image path or None
    Example: "Pasted image 20260203212022.png" -> "/images/test-articles/pasted-image-20260203212022.png"
    """
    for line in content_lines:
        # Check for Obsidian format: ![[image.png]]
        match = re.search(r'!\[\[([^\]]+)\]\]', line)
        if match:
            image_name = match.group(1)
            logger.debug(f"  Found Obsidian image: {image_name}")
            return image_name
        
        # Check for Markdown format: ![alt](path)
        match = re.search(r'!\[([^\]]*)\]\(([^\)]+)\)', line)
        if match:
            image_path = match.group(2)
            logger.debug(f"  Found Markdown image: {image_path}")
            return image_path
    
    return None


def format_image_path(image_name, directory):
    """
    Format image name to proper path.
    
    Example:
        "Pasted image 20260203212022.png", "test-articles" 
        -> "/images/test-articles/pasted-image-20260203212022.png"
    """
    if not image_name:
        return None
    
    # If already a path (starts with / or contains /images/), return as is
    if image_name.startswith('/') or '/images/' in image_name:
        return image_name
    
    # Slugify the image name
    name_without_ext = os.path.splitext(image_name)[0]
    extension = os.path.splitext(image_name)[1]
    slug_name = slugify(name_without_ext)
    
    return f"/images/{directory}/{slug_name}{extension}"


def extract_description(content_lines, max_chars=150):
    """
    Extract first 150 characters from article content.
    Skips headings (lines starting with #), ## TOC section, separators (---), and Obsidian links.
    
    Returns: description string (max 150 chars)
    """
    description = ""
    skip_toc = False
    toc_end_marker = "---"
    
    for line in content_lines:
        line_stripped = line.strip()
        
        # Skip empty lines
        if not line_stripped:
            continue
        
        # Skip separator lines (---, ======, etc.)
        if re.match(r'^[-=]{3,}$', line_stripped):
            continue
        
        # Check if we're in TOC section
        if line_stripped == "## TOC" or line_stripped.startswith("## TOC"):
            skip_toc = True
            continue
        
        # Check if TOC section ended (look for ### or another heading)
        if skip_toc and line_stripped.startswith("###"):
            skip_toc = False
            # Don't skip this line, process it
        
        # Skip lines while in TOC
        if skip_toc:
            continue
        
        # Skip headings (lines starting with #)
        if line_stripped.startswith('#'):
            continue
        
        # Skip markdown images
        if line_stripped.startswith('!'):
            continue
        
        # Skip Obsidian links at start of line (like "1. [[Link]]")
        if re.match(r'^\d+\.\s*\[\[', line_stripped):
            continue
        
        # Skip markdown links at start of line
        if line_stripped.startswith('['):
            continue
        
        # Remove Obsidian links from line [[link]] -> link
        line_cleaned = re.sub(r'\[\[([^\]]+)\]\]', r'\1', line_stripped)
        
        # Remove markdown links [text](url) -> text
        line_cleaned = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line_cleaned)
        
        # Remove bold/italic markers
        line_cleaned = re.sub(r'\*\*([^\*]+)\*\*', r'\1', line_cleaned)
        line_cleaned = re.sub(r'\*([^\*]+)\*', r'\1', line_cleaned)
        
        # Skip if line is too short after cleaning (likely a list number or bullet)
        if len(line_cleaned.strip()) < 3:
            continue
        
        # Add line to description
        description += line_cleaned + " "
        
        # Check if we have enough characters
        if len(description) >= max_chars:
            break
    
    # Truncate to max_chars and clean up
    description = description[:max_chars].strip()
    
    # Remove trailing incomplete word
    if len(description) >= max_chars and ' ' in description:
        description = description.rsplit(' ', 1)[0]
    
    # Add ellipsis if truncated
    if len(description) >= max_chars - 3 or not description.endswith('.'):
        description = description.rstrip() + "..."
    
    # If description is empty, use a default
    if not description or description == "...":
        description = "مقاله آموزشی و کاربردی"
    
    return description


def calculate_reading_time(content_lines):
    """
    Calculate reading time based on character count.
    Rule: 1000 characters = 1 minute
    
    Returns: reading time in minutes (rounded)
    """
    total_chars = sum(len(line) for line in content_lines)
    reading_time = round(total_chars / 1000)
    
    # Minimum 1 minute
    if reading_time < 1:
        reading_time = 1
    
    logger.debug(f"  Total characters: {total_chars}, Reading time: {reading_time} minutes")
    
    return reading_time


def generate_hugo_frontmatter(file_path, obsidian_props, content_lines):
    """
    Generate Enhanced Hugo TOML frontmatter for the file.
    Uses Obsidian properties if available.
    
    Args:
        file_path: Path to the markdown file
        obsidian_props: dict with 'date', 'tags', 'categories' from Obsidian
        content_lines: list of content lines (for extracting description, images, reading time)
    
    Returns: string with frontmatter content
    """
    filename = file_path.name
    title = extract_title_from_filename(filename)
    directory = get_directory_name(file_path)
    slug = slugify(title)
    
    # Build tags list: directory + obsidian tags
    tags_list = [directory]
    if obsidian_props['tags']:
        tags_list.extend(obsidian_props['tags'])
    
    # Remove duplicates from tags while preserving order
    seen_tags = set()
    tags_list = [x for x in tags_list if not (x in seen_tags or seen_tags.add(x))]
    
    # Format tags for TOML
    tags_str = ', '.join([f'"{tag}"' for tag in tags_list])
    
    # Build categories list: directory + obsidian categories
    categories_list = [directory]
    if obsidian_props.get('categories'):
        categories_list.extend(obsidian_props['categories'])
    
    # Remove duplicates from categories while preserving order
    seen_cats = set()
    categories_list = [x for x in categories_list if not (x in seen_cats or seen_cats.add(x))]
    
    # Format categories for TOML
    categories_str = ', '.join([f'"{cat}"' for cat in categories_list])
    
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
    
    # lastmod: current date and time
    lastmod_str = get_current_datetime_str()
    
    # Series (same as directory only)
    series_str = f'"{directory}"'
    
    # Extract description (150 chars from content)
    description = extract_description(content_lines, max_chars=150)
    
    # Build keywords: title + tags + categories + filename + directory
    keywords_list = [title]
    keywords_list.extend(tags_list)
    keywords_list.extend(categories_list)
    keywords_list.append(slugify(filename.replace('.md', '')))
    # Remove duplicates while preserving order
    seen = set()
    keywords_list = [x for x in keywords_list if not (x in seen or seen.add(x))]
    keywords_str = ', '.join([f'"{kw}"' for kw in keywords_list])
    
    # Canonical URL
    canonical_url = f"{SITE_URL}/{directory}/{slug}/"
    
    # Extract first image
    first_image_name = extract_first_image(content_lines)
    featured_image = format_image_path(first_image_name, directory) if first_image_name else ""
    
    # Images array (same as featured_image for now)
    images_str = f'"{featured_image}"' if featured_image else ""
    
    # Calculate reading time
    reading_time = calculate_reading_time(content_lines)
    
    # Build frontmatter
    frontmatter = f'''+++
title = "{title}"
slug = "{slug}"
date = "{date_str}"
lastmod = "{lastmod_str}"
draft = false

categories = [{categories_str}]
tags = [{tags_str}]
series = [{series_str}]

description = "{description}"
keywords = [{keywords_str}]
author = "{AUTHOR_NAME}"
robots = "index, follow"
canonical = "{canonical_url}"

featured_image = "{featured_image}"
images = [{images_str}]

[params.opengraph]
  title = "{title}"
  description = "{description}"
  image = "{featured_image}"
  url = "{canonical_url}"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "{title}"
  description = "{description}"
  image = "{featured_image}"

readingTime = {reading_time}
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
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
    Returns: (has_frontmatter, first_plus_line, second_plus_line) or (False, -1, -1)
    """
    first_plus_line = -1
    second_plus_line = -1
    
    # Check first 3 lines for opening +++
    for i in range(min(3, len(lines))):
        if lines[i].strip() == "+++":
            first_plus_line = i
            # Found opening +++, look for closing +++
            for j in range(i + 1, min(50, len(lines))):  # Extended to 50 for enhanced frontmatter
                if lines[j].strip() == "+++":
                    second_plus_line = j
                    logger.debug(f"Found Hugo frontmatter from line {i} to {j}")
                    return True, first_plus_line, second_plus_line
            break
    
    return False, -1, -1


def remove_obsidian_properties_and_add_hugo_frontmatter(file_path):
    """
    Remove Obsidian properties from a markdown file and add Hugo TOML frontmatter.
    Also replaces old simple Hugo frontmatter with enhanced version.
    Extracts Date, tags, Category from Obsidian properties before removal.
    Returns: True if file was modified, False otherwise
    """
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        
        # Check if file already has Hugo frontmatter
        has_hugo, hugo_first, hugo_second = has_hugo_frontmatter(lines)
        
        # Check if file has Obsidian properties
        has_props, obs_first, obs_second = has_obsidian_properties(lines)
        
        # Default properties if no Obsidian properties found
        obsidian_props = {
            'date': None,
            'tags': [],
            'categories': []
        }
        
        content_lines = lines  # For extracting description, images, etc.
        
        # Step 1: Remove old Hugo frontmatter if exists
        if has_hugo:
            logger.info(f"Found old Hugo frontmatter in {file_path.name} from line {hugo_first} to line {hugo_second}")
            
            # Try to extract date and tags from old frontmatter
            for i in range(hugo_first + 1, hugo_second):
                line = lines[i].strip()
                
                # Extract date
                if line.startswith('date ='):
                    date_match = re.search(r'date\s*=\s*"([^"]+)"', line)
                    if date_match and not obsidian_props['date']:
                        obsidian_props['date'] = date_match.group(1).split('T')[0]
                        logger.debug(f"  Extracted date from old frontmatter: {obsidian_props['date']}")
                
                # Extract tags
                if line.startswith('tags ='):
                    tags_match = re.search(r'tags\s*=\s*\[([^\]]+)\]', line)
                    if tags_match:
                        tags_str = tags_match.group(1)
                        old_tags = [t.strip().strip('"').strip("'") for t in tags_str.split(',')]
                        # Keep non-directory tags
                        for tag in old_tags:
                            if tag and tag != get_directory_name(file_path) and tag not in obsidian_props['tags']:
                                obsidian_props['tags'].append(tag)
                        logger.debug(f"  Extracted tags from old frontmatter: {obsidian_props['tags']}")
            
            # Remove old Hugo frontmatter
            content_lines = lines[:hugo_first] + lines[hugo_second + 1:]
            logger.info(f"✓ Removed old Hugo frontmatter from: {file_path.name}")
            modified = True
        
        # Step 2: Remove Obsidian properties if exists (on updated content_lines)
        if has_props:
            # Re-check positions after Hugo removal
            has_props_new, obs_first_new, obs_second_new = has_obsidian_properties(content_lines)
            
            if has_props_new:
                logger.info(f"Found Obsidian properties in {file_path.name} from line {obs_first_new} to line {obs_second_new}")
                
                # Extract properties before removal
                obs_props_extracted = parse_obsidian_properties(content_lines, obs_first_new, obs_second_new)
                
                # Merge with properties from old Hugo frontmatter (Obsidian takes priority)
                if obs_props_extracted['date']:
                    obsidian_props['date'] = obs_props_extracted['date']
                if obs_props_extracted['tags']:
                    obsidian_props['tags'].extend(obs_props_extracted['tags'])
                if obs_props_extracted['categories']:
                    obsidian_props['categories'].extend(obs_props_extracted['categories'])
                
                # Remove Obsidian properties
                content_lines = content_lines[:obs_first_new] + content_lines[obs_second_new + 1:]
                
                logger.info(f"✓ Removed Obsidian properties from: {file_path.name}")
                modified = True
        
        # Generate Hugo enhanced frontmatter with all extracted properties
        frontmatter = generate_hugo_frontmatter(file_path, obsidian_props, content_lines)
        
        # Add Hugo frontmatter at the beginning
        content_lines.insert(0, frontmatter)
        
        logger.info(f"✓ Added Enhanced Hugo frontmatter to: {file_path.name}")
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(content_lines)
        
        return True
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        return False


def process_articles():
    """Process all markdown files recursively in content directory and subdirectories."""
    
    # Check if directory exists
    if not CONTENT_DIR.exists():
        logger.error(f"Directory not found: {CONTENT_DIR}")
        return
    
    # Load tracking data
    tracking_data = load_tracking_file()
    processed_files = set(tracking_data.get("processed_files", []))
    
    # Get all markdown files recursively from content directory
    markdown_files = list(CONTENT_DIR.rglob("*.md"))  # rglob for recursive search
    
    if not markdown_files:
        logger.warning(f"No markdown files found in {CONTENT_DIR}")
        return
    
    logger.info(f"Found {len(markdown_files)} markdown files to check (including subdirectories)")
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
        # Use relative path as unique identifier
        relative_path = str(file_path.relative_to(CONTENT_DIR))
        
        # Skip if already processed
        if relative_path in processed_files:
            logger.info(f"⊙ Skipping already processed file: {relative_path}")
            stats["already_processed"] += 1
            continue
        
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing: {relative_path}")
        logger.info(f"{'='*60}")
        
        # Try to process file
        success = remove_obsidian_properties_and_add_hugo_frontmatter(file_path)
        
        if success:
            # Add to processed files (using relative path)
            processed_files.add(relative_path)
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
    report_path = "obsidian_property_remover_enhanced_report.txt"
    
    try:
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write("OBSIDIAN PROPERTY REMOVER & HUGO ENHANCED FRONTMATTER ADDER\n")
            f.write("EXECUTION REPORT\n")
            f.write("=" * 70 + "\n\n")
            
            f.write(f"Execution Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target Directory: {CONTENT_DIR} (recursive)\n\n")
            
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
    logger.info("OBSIDIAN PROPERTY REMOVER & HUGO ENHANCED FRONTMATTER ADDER")
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
