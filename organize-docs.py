#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Documentation Organization Script
==================================
Organizes all documentation files into categorized directories
Author: Davoodya Team
Date: 2026-02-10
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List

# Color codes for output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    RESET = '\033[0m'

# Documentation categories and their patterns
DOC_CATEGORIES = {
    '01-Scripts': {
        'patterns': [
            'ALL_JOBS_GUIDE',
            'IMAGE_PROPERTY_FIXER_GUIDE',
            'IMAGES_RENAMER_GUIDE',
            'IMPORT_PIPELINE_GUIDE',
            'README_SCRIPTS_USAGE',
            'SCRIPTS_EXCLUSION_UPDATE',
            'URL_CANONICAL_UPDATER_GUIDE',
            'URL_SEGMENT_REPLACER_GUIDE',
            'URL_UPDATER_ENGLISH_VERSION',
            'URL_SEGMENT_REPLACER_README',
            'URL_UPDATER_README',
            'PIPELINE_COMPARISON'
        ],
        'description': 'Python scripts documentation and guides'
    },
    
    '02-Features': {
        'patterns': [
            'ALL_ARTICLES_PAGE_GUIDE',
            'ARTICLE_META_BADGES_GUIDE',
            'CACHE_BUSTING_GUIDE',
            'CATEGORY_FEATURED_IMAGE_GUIDE',
            'CLIENT_SIDE_PAGINATION_GUIDE',
            'FILTER_MODAL_UNIFIED_GUIDE',
            'FILTER_SYSTEM_GUIDE',
            'LOAD_MORE_IMPLEMENTATION_GUIDE',
            'SEARCH_GUIDE',
            'SIDEBAR_GUIDE',
            'SIDEBAR_SORT_DROPDOWN_GUIDE',
            'TAG_LINKS_IN_ARTICLE_CARDS',
            'TAXONOMY_ROUTING_GUIDE',
            'TOC_GUIDE',
            'UNIFIED_FILTER_USER_GUIDE',
            'FEATURED_IMAGE_GUIDE',
            'FEATURED_IMAGE_SUMMARY',
            'IMAGES_GUIDE',
            'NEW_FEATURES',
            'SORT_FEATURE_IMPLEMENTATION',
            'TOC_FLOATING_GUIDE',
            'TOC_SUMMARY'
        ],
        'description': 'Feature documentation and implementation guides'
    },
    
    '03-Fixes': {
        'patterns': [
            'ARTICLE_CARD_SIZE_FIX',
            'BUGFIX_LOAD_MORE',
            'CODE_BLOCKS_IMPROVEMENT',
            'CSS_CLEANUP_REPORT',
            'CSS_FILES_CLEANUP',
            'CSS_FILES_ISSUE_FIX',
            'DEBUG_CRASH_FIX',
            'FILTER_DEBUG_GUIDE',
            'FILTER_FIX_FINAL',
            'FILTER_SYSTEM_FIX_GUIDE',
            'FIXES_DOCUMENTATION',
            'FONTS_FIX_REPORT',
            'MOBILE_LAYOUT_FIX',
            'QUICK_FIX_GUIDE',
            'SCROLLBAR_FIX',
            'SIDEBAR_RECENT_POSTS_FIX',
            'SIDEBAR_SORT_DROPDOWN_FIX',
            'SIDEBAR_SORT_FIX',
            'SUMMARY_AND_DIRECTION_FIX',
            'TOC_IN_SUMMARY_FIX',
            'continue-badge-urlize'
        ],
        'description': 'Bug fixes and improvements documentation'
    },
    
    '04-Deployment': {
        'patterns': [
            'DEPLOY_GUIDE',
            'DEPLOYMENT',
            'README_DEPLOYMENT'
        ],
        'description': 'Deployment guides and instructions'
    },
    
    '05-Guides': {
        'patterns': [
            'CUSTOM_PAGE_STYLES_GUIDE',
            'DEVELOPMENT_GUIDE',
            'FONTS_USAGE',
            'LOAD_MORE_TEST_CHECKLIST',
            'MOBILE_LAYOUT_TEST_GUIDE',
            'PROJECT_STRUCTURE',
            'README_HOME_PAGE_IMAGES',
            'README_IMAGES'
        ],
        'description': 'General guides and usage instructions'
    },
    
    '06-Changelogs': {
        'patterns': [
            'CHANGELOG',
            'CHANGELOG_2026-02-09',
            'CHANGELOG_ALL_ARTICLES_2026-02-09',
            'CHANGELOG_FILTER_SYSTEM_2026-02-09',
            'CHANGELOG_FIX_ALL_ARTICLES_2026-02-09',
            'CHANGES_SUMMARY',
            'FILTER_FIX_SUMMARY',
            'FILTER_SYSTEM_IMPLEMENTATION_SUMMARY',
            'LOAD_MORE_CHANGELOG',
            'UNIFIED_FILTER_CHANGELOG',
            'LOAD_MORE_README',
            'IMPLEMENTATION_COMPLETE',
            'FINAL_SUMMARY_FA'
        ],
        'description': 'Change logs and version history'
    }
}

def print_colored(text: str, color: str):
    """Print colored text"""
    print(f"{color}{text}{Colors.RESET}")

def get_category_for_file(filename: str) -> str:
    """Determine which category a file belongs to"""
    # Remove .md extension for matching
    base_name = filename.replace('.md', '')
    
    # Check each category's patterns
    for category, info in DOC_CATEGORIES.items():
        for pattern in info['patterns']:
            if pattern.lower() in base_name.lower():
                return category
    
    # Default to Archive if no match
    return '07-Archive'

def move_file(src: Path, dest: Path, dry_run: bool = False) -> bool:
    """Move a file to destination"""
    try:
        if dry_run:
            print(f"  Would move: {src.name} → {dest.parent.name}/")
            return True
        else:
            # Create parent directory if needed
            dest.parent.mkdir(parents=True, exist_ok=True)
            
            # Move file
            shutil.move(str(src), str(dest))
            return True
    except Exception as e:
        print_colored(f"  Error moving {src.name}: {e}", Colors.RED)
        return False

def organize_docs(dry_run: bool = False):
    """Main function to organize documentation"""
    root = Path('.')
    docs_dir = Path('docs')
    
    # Statistics
    stats = {
        'root_moved': 0,
        'docs_moved': 0,
        'total_files': 0,
        'errors': 0
    }
    
    # Category counters
    category_stats = {cat: 0 for cat in DOC_CATEGORIES.keys()}
    category_stats['07-Archive'] = 0
    
    print()
    print_colored("=" * 80, Colors.CYAN)
    print_colored("Documentation Organization Script", Colors.CYAN)
    print_colored("=" * 80, Colors.CYAN)
    print()
    
    if dry_run:
        print_colored("DRY RUN MODE - No files will be moved", Colors.YELLOW)
        print()
    
    # Step 1: Move markdown files from root to docs
    print_colored("Step 1: Moving markdown files from root to docs/", Colors.CYAN)
    print("-" * 80)
    
    root_md_files = list(root.glob('*.md'))
    root_md_files = [f for f in root_md_files if f.parent == root]  # Only root level
    
    if root_md_files:
        for md_file in root_md_files:
            category = get_category_for_file(md_file.name)
            dest = docs_dir / category / md_file.name
            
            if move_file(md_file, dest, dry_run):
                stats['root_moved'] += 1
                category_stats[category] += 1
                print_colored(f"  ✓ {md_file.name} → {category}/", Colors.GREEN)
            else:
                stats['errors'] += 1
    else:
        print("  No markdown files found in root")
    
    print()
    
    # Step 2: Organize existing docs files
    print_colored("Step 2: Organizing existing files in docs/", Colors.CYAN)
    print("-" * 80)
    
    # Get all markdown files directly in docs (not in subdirectories)
    docs_md_files = [f for f in docs_dir.glob('*.md') if f.parent == docs_dir]
    
    if docs_md_files:
        for md_file in docs_md_files:
            category = get_category_for_file(md_file.name)
            dest = docs_dir / category / md_file.name
            
            # Skip if already in the right place
            if md_file.parent.name == category:
                continue
            
            if move_file(md_file, dest, dry_run):
                stats['docs_moved'] += 1
                category_stats[category] += 1
                print_colored(f"  ✓ {md_file.name} → {category}/", Colors.GREEN)
            else:
                stats['errors'] += 1
    else:
        print("  No markdown files to organize in docs/")
    
    print()
    
    # Step 3: Create README files for each category
    if not dry_run:
        print_colored("Step 3: Creating README files for categories", Colors.CYAN)
        print("-" * 80)
        
        for category, info in DOC_CATEGORIES.items():
            readme_path = docs_dir / category / 'README.md'
            
            if not readme_path.exists():
                try:
                    with open(readme_path, 'w', encoding='utf-8') as f:
                        f.write(f"# {category.split('-', 1)[1]}\n\n")
                        f.write(f"{info['description']}\n\n")
                        f.write("## Files in this category\n\n")
                        
                        # List files in this category
                        cat_files = sorted((docs_dir / category).glob('*.md'))
                        cat_files = [f for f in cat_files if f.name != 'README.md']
                        
                        if cat_files:
                            for file in cat_files:
                                f.write(f"- [{file.name}](./{file.name})\n")
                        else:
                            f.write("*No files yet*\n")
                        
                        f.write(f"\n---\n\n")
                        f.write(f"*Category: {category}*\n")
                    
                    print_colored(f"  ✓ Created {category}/README.md", Colors.GREEN)
                except Exception as e:
                    print_colored(f"  Error creating README for {category}: {e}", Colors.RED)
        
        # Create Archive README
        archive_readme = docs_dir / '07-Archive' / 'README.md'
        if not archive_readme.exists():
            try:
                with open(archive_readme, 'w', encoding='utf-8') as f:
                    f.write("# Archive\n\n")
                    f.write("Miscellaneous documentation files that don't fit other categories.\n\n")
                    f.write("## Files in this category\n\n")
                    
                    arc_files = sorted((docs_dir / '07-Archive').glob('*.md'))
                    arc_files = [f for f in arc_files if f.name != 'README.md']
                    
                    if arc_files:
                        for file in arc_files:
                            f.write(f"- [{file.name}](./{file.name})\n")
                    else:
                        f.write("*No files yet*\n")
                    
                    f.write("\n---\n\n")
                    f.write("*Category: 07-Archive*\n")
                
                print_colored(f"  ✓ Created 07-Archive/README.md", Colors.GREEN)
            except Exception as e:
                print_colored(f"  Error creating Archive README: {e}", Colors.RED)
        
        print()
    
    # Summary
    stats['total_files'] = stats['root_moved'] + stats['docs_moved']
    
    print_colored("=" * 80, Colors.CYAN)
    print_colored("Summary", Colors.CYAN)
    print_colored("=" * 80, Colors.CYAN)
    print()
    print(f"Files moved from root:        {stats['root_moved']}")
    print(f"Files organized in docs:      {stats['docs_moved']}")
    print(f"Total files processed:        {stats['total_files']}")
    print(f"Errors:                       {stats['errors']}")
    print()
    
    print_colored("Files per category:", Colors.YELLOW)
    for category in sorted(category_stats.keys()):
        count = category_stats[category]
        if count > 0:
            cat_name = category.split('-', 1)[1] if '-' in category else category
            print(f"  {category} ({cat_name}): {count} files")
    
    print()
    print_colored("=" * 80, Colors.CYAN)
    
    if dry_run:
        print()
        print_colored("This was a DRY RUN. Run without --dry-run to actually move files.", Colors.YELLOW)
    else:
        print()
        print_colored("Documentation organization completed!", Colors.GREEN)
    
    print()

def create_main_index():
    """Create main README.md in docs folder"""
    docs_dir = Path('docs')
    readme_path = docs_dir / 'README.md'
    
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Documentation Index\n\n")
            f.write("Welcome to the Davoodya Hugo Project documentation.\n\n")
            f.write("All documentation is organized into the following categories:\n\n")
            
            # List categories
            for category, info in DOC_CATEGORIES.items():
                cat_name = category.split('-', 1)[1]
                f.write(f"## [{cat_name}](./{category}/)\n\n")
                f.write(f"{info['description']}\n\n")
                
                # Count files
                cat_path = docs_dir / category
                if cat_path.exists():
                    files = list(cat_path.glob('*.md'))
                    files = [file for file in files if file.name != 'README.md']
                    f.write(f"📄 **{len(files)}** documents\n\n")
                else:
                    f.write("📄 **0** documents\n\n")
            
            # Archive
            f.write("## [Archive](./07-Archive/)\n\n")
            f.write("Miscellaneous documentation files.\n\n")
            archive_path = docs_dir / '07-Archive'
            if archive_path.exists():
                files = list(archive_path.glob('*.md'))
                files = [file for file in files if file.name != 'README.md']
                f.write(f"📄 **{len(files)}** documents\n\n")
            
            f.write("---\n\n")
            f.write("*Last updated: 2026-02-10*\n")
        
        print_colored(f"✓ Created main docs/README.md", Colors.GREEN)
        return True
    except Exception as e:
        print_colored(f"Error creating main README: {e}", Colors.RED)
        return False

if __name__ == "__main__":
    import sys
    
    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv
    
    # Run organization
    organize_docs(dry_run=dry_run)
    
    # Create main index
    if not dry_run:
        print()
        create_main_index()
