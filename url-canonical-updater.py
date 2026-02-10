#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL و Canonical Updater Script
این اسکریپت برای اضافه کردن segment جدید 'knowledge' به URLها در front matter مقالات Hugo استفاده می‌شود.

نویسنده: Davoodya Site Manager
تاریخ: 2026-02-10
"""

import os
import re
import sys
import logging
from pathlib import Path
from datetime import datetime

# تنظیم logging
log_filename = f"url_canonical_updater_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class URLCanonicalUpdater:
    """کلاس برای به‌روزرسانی URL و Canonical در front matter مقالات"""
    
    def __init__(self, base_directory):
        """
        مقداردهی اولیه
        
        Args:
            base_directory (str): مسیر دایرکتوری پایه برای پردازش
        """
        self.base_directory = Path(base_directory).resolve()
        self.find_pattern = "https://davoodya.ir/"
        self.replace_pattern = "https://davoodya.ir/knowledge/"
        
        # آمار پردازش
        self.stats = {
            'total_files': 0,
            'processed_files': 0,
            'skipped_files': 0,
            'error_files': 0,
            'total_replacements': 0,
            'url_replacements': 0,
            'canonical_replacements': 0
        }
        
        # لیست فایل‌های پردازش شده
        self.processed_files_list = []
        self.skipped_files_list = []
        self.error_files_list = []
        
        logger.info("="*80)
        logger.info("URL & Canonical Updater - Starting Process")
        logger.info("="*80)
        logger.info(f"Base Directory: {self.base_directory}")
        logger.info(f"Search Pattern: {self.find_pattern}")
        logger.info(f"Replace Pattern: {self.replace_pattern}")
        logger.info("-"*80)
    
    def validate_directory(self):
        """
        اعتبارسنجی دایرکتوری ورودی
        
        Returns:
            bool: True اگر دایرکتوری معتبر باشد
        """
        if not self.base_directory.exists():
            logger.error(f"Error: Directory '{self.base_directory}' does not exist!")
            return False
        
        if not self.base_directory.is_dir():
            logger.error(f"Error: '{self.base_directory}' is not a directory!")
            return False
        
        logger.info(f"✓ Directory is valid: {self.base_directory}")
        return True
    
    def find_markdown_files(self):
        """
        یافتن تمام فایل‌های Markdown در دایرکتوری و زیردایرکتوری‌ها
        
        Returns:
            list: لیست مسیرهای فایل‌های Markdown
        """
        logger.info("Searching for Markdown files...")
        markdown_files = []
        
        for root, dirs, files in os.walk(self.base_directory):
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    markdown_files.append(file_path)
        
        logger.info(f"✓ Found {len(markdown_files)} Markdown files")
        return markdown_files
    
    def extract_frontmatter(self, content):
        """
        استخراج front matter از محتوای فایل
        
        Args:
            content (str): محتوای کامل فایل
            
        Returns:
            tuple: (front_matter, body, delimiter) یا (None, content, None) اگر front matter وجود نداشته باشد
        """
        # بررسی برای YAML front matter (---)
        yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        yaml_match = re.match(yaml_pattern, content, re.DOTALL)
        
        if yaml_match:
            return yaml_match.group(1), yaml_match.group(2), '---'
        
        # بررسی برای TOML front matter (+++)
        toml_pattern = r'^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n(.*)$'
        toml_match = re.match(toml_pattern, content, re.DOTALL)
        
        if toml_match:
            return toml_match.group(1), toml_match.group(2), '+++'
        
        return None, content, None
    
    def update_frontmatter_urls(self, frontmatter):
        """
        به‌روزرسانی URL و Canonical در front matter
        
        Args:
            frontmatter (str): محتوای front matter
            
        Returns:
            tuple: (updated_frontmatter, replacement_count, url_count, canonical_count)
        """
        updated_frontmatter = frontmatter
        url_count = 0
        canonical_count = 0
        
        # الگوی برای یافتن url و canonical
        # پشتیبانی از فرمت‌های مختلف: url = "...", url: "...", url="..."
        patterns = [
            # برای url
            (r'(url\s*[=:]\s*["\'])' + re.escape(self.find_pattern), 
             r'\1' + self.replace_pattern, 
             'url'),
            # برای canonical
            (r'(canonical\s*[=:]\s*["\'])' + re.escape(self.find_pattern), 
             r'\1' + self.replace_pattern, 
             'canonical')
        ]
        
        for pattern, replacement, field_type in patterns:
            matches = re.findall(pattern, updated_frontmatter)
            if matches:
                updated_frontmatter = re.sub(pattern, replacement, updated_frontmatter)
                count = len(matches)
                
                if field_type == 'url':
                    url_count = count
                    logger.debug(f"  - Updated {count} 'url' field(s)")
                elif field_type == 'canonical':
                    canonical_count = count
                    logger.debug(f"  - Updated {count} 'canonical' field(s)")
        
        total_count = url_count + canonical_count
        return updated_frontmatter, total_count, url_count, canonical_count
    
    def process_file(self, file_path):
        """
        پردازش یک فایل Markdown
        
        Args:
            file_path (Path): مسیر فایل
            
        Returns:
            tuple: (success, replacement_count, url_count, canonical_count)
        """
        try:
            logger.info(f"Processing: {file_path.relative_to(self.base_directory)}")
            
            # خواندن فایل
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # استخراج front matter
            frontmatter, body, delimiter = self.extract_frontmatter(content)
            
            if frontmatter is None:
                logger.warning(f"  ⚠ Warning: No front matter found - File skipped")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'No front matter'
                })
                return False, 0, 0, 0
            
            # Check if old URLs exist
            if self.find_pattern not in frontmatter:
                logger.info(f"  ℹ Info: Old URL not found - File skipped")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'Old URL does not exist'
                })
                return False, 0, 0, 0
            
            # به‌روزرسانی front matter
            updated_frontmatter, replacement_count, url_count, canonical_count = \
                self.update_frontmatter_urls(frontmatter)
            
            if replacement_count == 0:
                logger.info(f"  ℹ Info: No changes needed - File skipped")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'No changes needed'
                })
                return False, 0, 0, 0
            
            # ساخت محتوای جدید
            new_content = f"{delimiter}\n{updated_frontmatter}\n{delimiter}\n{body}"
            
            # نوشتن فایل
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            logger.info(f"  ✓ Success: {replacement_count} replacement(s) made " +
                       f"(url: {url_count}, canonical: {canonical_count})")
            
            self.processed_files_list.append({
                'file': str(file_path.relative_to(self.base_directory)),
                'total_replacements': replacement_count,
                'url_replacements': url_count,
                'canonical_replacements': canonical_count
            })
            
            return True, replacement_count, url_count, canonical_count
            
        except Exception as e:
            logger.error(f"  ✗ Error processing file: {str(e)}")
            self.error_files_list.append({
                'file': str(file_path.relative_to(self.base_directory)),
                'error': str(e)
            })
            return False, 0, 0, 0
    
    def process_all_files(self):
        """پردازش تمام فایل‌های Markdown"""
        # یافتن فایل‌ها
        markdown_files = self.find_markdown_files()
        self.stats['total_files'] = len(markdown_files)
        
        if self.stats['total_files'] == 0:
            logger.warning("No Markdown files found for processing!")
            return
        
        logger.info("-"*80)
        logger.info("Starting file processing...")
        logger.info("-"*80)
        
        # پردازش هر فایل
        for idx, file_path in enumerate(markdown_files, 1):
            logger.info(f"\n[{idx}/{self.stats['total_files']}] ", extra={'end': ''})
            
            success, total_repl, url_repl, canonical_repl = self.process_file(file_path)
            
            if success:
                self.stats['processed_files'] += 1
                self.stats['total_replacements'] += total_repl
                self.stats['url_replacements'] += url_repl
                self.stats['canonical_replacements'] += canonical_repl
            elif total_repl == 0:
                self.stats['skipped_files'] += 1
            else:
                self.stats['error_files'] += 1
    
    def generate_report(self):
        """تولید گزارش نهایی"""
        logger.info("\n" + "="*80)
        logger.info("Final Processing Report")
        logger.info("="*80)
        logger.info(f"Processed Directory: {self.base_directory}")
        logger.info(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("-"*80)
        logger.info("General Statistics:")
        logger.info(f"  • Total files found: {self.stats['total_files']}")
        logger.info(f"  • Files processed: {self.stats['processed_files']}")
        logger.info(f"  • Files skipped: {self.stats['skipped_files']}")
        logger.info(f"  • Files with errors: {self.stats['error_files']}")
        logger.info("-"*80)
        logger.info("Replacement Statistics:")
        logger.info(f"  • Total replacements: {self.stats['total_replacements']}")
        logger.info(f"  • URL replacements: {self.stats['url_replacements']}")
        logger.info(f"  • Canonical replacements: {self.stats['canonical_replacements']}")
        logger.info("="*80)
        
        # ذخیره گزارش جزئیات در فایل
        report_filename = f"url_canonical_updater_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("URL & Canonical Processing Detail Report\n")
            f.write("="*80 + "\n\n")
            
            f.write(f"Directory: {self.base_directory}\n")
            f.write(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Search Pattern: {self.find_pattern}\n")
            f.write(f"Replace Pattern: {self.replace_pattern}\n\n")
            
            f.write("-"*80 + "\n")
            f.write("General Statistics:\n")
            f.write("-"*80 + "\n")
            f.write(f"Total files found: {self.stats['total_files']}\n")
            f.write(f"Files processed: {self.stats['processed_files']}\n")
            f.write(f"Files skipped: {self.stats['skipped_files']}\n")
            f.write(f"Files with errors: {self.stats['error_files']}\n\n")
            
            f.write(f"Total replacements: {self.stats['total_replacements']}\n")
            f.write(f"URL replacements: {self.stats['url_replacements']}\n")
            f.write(f"Canonical replacements: {self.stats['canonical_replacements']}\n\n")
            
            # Processed files
            if self.processed_files_list:
                f.write("="*80 + "\n")
                f.write(f"Processed Files ({len(self.processed_files_list)} items):\n")
                f.write("="*80 + "\n")
                for item in self.processed_files_list:
                    f.write(f"\n📄 {item['file']}\n")
                    f.write(f"   - Total replacements: {item['total_replacements']}\n")
                    f.write(f"   - URL: {item['url_replacements']}\n")
                    f.write(f"   - Canonical: {item['canonical_replacements']}\n")
            
            # Skipped files
            if self.skipped_files_list:
                f.write("\n" + "="*80 + "\n")
                f.write(f"Skipped Files ({len(self.skipped_files_list)} items):\n")
                f.write("="*80 + "\n")
                for item in self.skipped_files_list:
                    f.write(f"\n⚠ {item['file']}\n")
                    f.write(f"   Reason: {item['reason']}\n")
            
            # Files with errors
            if self.error_files_list:
                f.write("\n" + "="*80 + "\n")
                f.write(f"Files with Errors ({len(self.error_files_list)} items):\n")
                f.write("="*80 + "\n")
                for item in self.error_files_list:
                    f.write(f"\n✗ {item['file']}\n")
                    f.write(f"   Error: {item['error']}\n")
        
        logger.info(f"\n✓ Detail report saved to file: {report_filename}")
        logger.info(f"✓ Complete log saved to file: {log_filename}")
    
    def run(self):
        """اجرای کامل پردازش"""
        if not self.validate_directory():
            return False
        
        self.process_all_files()
        self.generate_report()
        
        return True


def get_user_input():
    """
    دریافت مسیر دایرکتوری از کاربر
    
    Returns:
        str: مسیر دایرکتوری
    """
    print("="*80)
    print("URL & Canonical Updater - Update Hugo articles front matter")
    print("="*80)
    print("\nThis script adds the new 'knowledge' segment to URLs:")
    print(f"  From: https://davoodya.ir/...")
    print(f"  To:   https://davoodya.ir/knowledge/...")
    print("-"*80)
    
    # Get path from user
    user_input = input("\nEnter directory path (Press Enter for default 'content/'): ").strip()
    
    # حذف کوتیشن‌ها اگر وجود داشته باشد
    user_input = user_input.strip('"').strip("'")
    
    # اگر خالی بود، از پیش‌فرض استفاده کن
    if not user_input:
        # پیدا کردن دایرکتوری content نسبت به موقعیت اسکریپت
        script_dir = Path(__file__).parent
        content_dir = script_dir / "content"
        return str(content_dir)
    
    return user_input


def main():
    """تابع اصلی برنامه"""
    try:
        # دریافت ورودی کاربر
        directory_path = get_user_input()
        
        print(f"\nSelected directory: {directory_path}")
        print("-"*80)
        
        # User confirmation
        confirm = input("\nDo you want to continue? (y/n): ").strip().lower()
        
        if confirm not in ['y', 'yes']:
            print("\n❌ Operation cancelled.")
            return
        
        print("\n" + "="*80)
        print("Starting processing...")
        print("="*80 + "\n")
        
        # ایجاد و اجرای updater
        updater = URLCanonicalUpdater(directory_path)
        success = updater.run()
        
        if success:
            print("\n" + "="*80)
            print("✓ Processing completed successfully!")
            print("="*80)
        else:
            print("\n" + "="*80)
            print("✗ Processing encountered errors.")
            print("="*80)
            
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        print(f"\n✗ Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
