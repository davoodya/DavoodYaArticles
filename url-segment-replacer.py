#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL Segment Replacer Script
این اسکریپت برای اضافه کردن یک segment دلخواه به URLها در مقالات Hugo استفاده می‌شود.

نویسنده: Davoodya Site Manager
تاریخ: 2026-02-10
"""

import os
import re
import sys
import logging
from pathlib import Path
from datetime import datetime
from enum import Enum

# تنظیم logging
log_filename = f"url_segment_replacer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class ReplaceMode(Enum):
    """حالت‌های مختلف جایگزینی"""
    ALL = "all"          # تمام فایل
    FRONT = "front"      # فقط front matter
    BODY = "body"        # فقط بدنه مقاله


class URLSegmentReplacer:
    """کلاس برای جایگزینی URL segment در مقالات Hugo"""
    
    def __init__(self, base_directory, url_segment, replace_mode):
        """
        مقداردهی اولیه
        
        Args:
            base_directory (str): مسیر دایرکتوری پایه برای پردازش
            url_segment (str): segment جدید URL که باید اضافه شود
            replace_mode (ReplaceMode): حالت جایگزینی (all, front, body)
        """
        self.base_directory = Path(base_directory).resolve()
        self.url_segment = url_segment.strip('/')  # حذف / از ابتدا و انتها
        self.replace_mode = replace_mode
        
        # الگوهای جستجو و جایگزینی
        self.find_pattern = "https://davoodya.ir/"
        self.replace_pattern = f"https://davoodya.ir/{self.url_segment}/"
        
        # آمار پردازش
        self.stats = {
            'total_files': 0,
            'processed_files': 0,
            'skipped_files': 0,
            'error_files': 0,
            'total_replacements': 0,
            'frontmatter_replacements': 0,
            'body_replacements': 0
        }
        
        # لیست فایل‌های پردازش شده
        self.processed_files_list = []
        self.skipped_files_list = []
        self.error_files_list = []
        
        logger.info("="*80)
        logger.info("URL Segment Replacer - Starting Process")
        logger.info("="*80)
        logger.info(f"Base Directory: {self.base_directory}")
        logger.info(f"URL Segment: {self.url_segment}")
        logger.info(f"Replace Mode: {self.replace_mode.value}")
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
            tuple: (front_matter, body, delimiter, frontmatter_end_index) 
                   یا (None, content, None, 0) اگر front matter وجود نداشته باشد
        """
        # بررسی برای YAML front matter (---)
        yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        yaml_match = re.match(yaml_pattern, content, re.DOTALL)
        
        if yaml_match:
            frontmatter = yaml_match.group(1)
            body = yaml_match.group(2)
            # محاسبه index پایان front matter
            frontmatter_end = content.find('---', 4) + 3  # پیدا کردن دومین ---
            return frontmatter, body, '---', frontmatter_end
        
        # بررسی برای TOML front matter (+++)
        toml_pattern = r'^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n(.*)$'
        toml_match = re.match(toml_pattern, content, re.DOTALL)
        
        if toml_match:
            frontmatter = toml_match.group(1)
            body = toml_match.group(2)
            # محاسبه index پایان front matter
            frontmatter_end = content.find('+++', 4) + 3  # پیدا کردن دومین +++
            return frontmatter, body, '+++', frontmatter_end
        
        return None, content, None, 0
    
    def replace_urls_in_text(self, text):
        """
        جایگزینی URLها در متن داده شده
        
        Args:
            text (str): متن برای جایگزینی
            
        Returns:
            tuple: (updated_text, replacement_count)
        """
        # شمارش تعداد URLهای قدیمی
        old_urls = text.count(self.find_pattern)
        
        # جایگزینی
        updated_text = text.replace(self.find_pattern, self.replace_pattern)
        
        # شمارش تعداد جایگزینی‌های واقعی
        replacement_count = old_urls
        
        return updated_text, replacement_count
    
    def process_file(self, file_path):
        """
        پردازش یک فایل Markdown
        
        Args:
            file_path (Path): مسیر فایل
            
        Returns:
            tuple: (success, total_replacements, frontmatter_replacements, body_replacements)
        """
        try:
            logger.info(f"Processing: {file_path.relative_to(self.base_directory)}")
            
            # خواندن فایل
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # بررسی اینکه آیا URL قدیمی وجود دارد
            if self.find_pattern not in content:
                logger.info(f"  ℹ Info: Old URL pattern not found - File skipped")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'Old URL pattern does not exist'
                })
                return False, 0, 0, 0
            
            # استخراج front matter
            frontmatter, body, delimiter, frontmatter_end = self.extract_frontmatter(content)
            
            new_content = content
            total_replacements = 0
            frontmatter_replacements = 0
            body_replacements = 0
            
            # بر اساس حالت انتخاب شده، جایگزینی را انجام بده
            if self.replace_mode == ReplaceMode.ALL:
                # جایگزینی در تمام فایل
                new_content, total_replacements = self.replace_urls_in_text(content)
                logger.info(f"  → Mode: ALL - Replacing in entire file")
                
            elif self.replace_mode == ReplaceMode.FRONT:
                # جایگزینی فقط در front matter
                if frontmatter is None:
                    logger.warning(f"  ⚠ Warning: No front matter found - File skipped")
                    self.skipped_files_list.append({
                        'file': str(file_path.relative_to(self.base_directory)),
                        'reason': 'No front matter (FRONT mode selected)'
                    })
                    return False, 0, 0, 0
                
                logger.info(f"  → Mode: FRONT - Replacing only in front matter")
                updated_frontmatter, frontmatter_replacements = self.replace_urls_in_text(frontmatter)
                
                if frontmatter_replacements > 0:
                    new_content = f"{delimiter}\n{updated_frontmatter}\n{delimiter}\n{body}"
                    total_replacements = frontmatter_replacements
                
            elif self.replace_mode == ReplaceMode.BODY:
                # جایگزینی فقط در بدنه مقاله
                if frontmatter is None:
                    logger.info(f"  → Mode: BODY - No front matter, processing entire file")
                    new_content, body_replacements = self.replace_urls_in_text(content)
                else:
                    logger.info(f"  → Mode: BODY - Replacing only in body (after front matter)")
                    updated_body, body_replacements = self.replace_urls_in_text(body)
                    
                    if body_replacements > 0:
                        new_content = f"{delimiter}\n{frontmatter}\n{delimiter}\n{updated_body}"
                
                total_replacements = body_replacements
            
            # بررسی اینکه آیا تغییری انجام شده است
            if total_replacements == 0:
                logger.info(f"  ℹ Info: No replacements made - File skipped")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'No replacements needed in selected mode'
                })
                return False, 0, 0, 0
            
            # نوشتن فایل
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            logger.info(f"  ✓ Success: {total_replacements} replacement(s) made")
            if self.replace_mode == ReplaceMode.ALL:
                logger.info(f"     (Mode: ALL)")
            elif self.replace_mode == ReplaceMode.FRONT:
                logger.info(f"     (Front matter: {frontmatter_replacements})")
            elif self.replace_mode == ReplaceMode.BODY:
                logger.info(f"     (Body: {body_replacements})")
            
            self.processed_files_list.append({
                'file': str(file_path.relative_to(self.base_directory)),
                'total_replacements': total_replacements,
                'frontmatter_replacements': frontmatter_replacements,
                'body_replacements': body_replacements,
                'mode': self.replace_mode.value
            })
            
            return True, total_replacements, frontmatter_replacements, body_replacements
            
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
            
            success, total_repl, front_repl, body_repl = self.process_file(file_path)
            
            if success:
                self.stats['processed_files'] += 1
                self.stats['total_replacements'] += total_repl
                self.stats['frontmatter_replacements'] += front_repl
                self.stats['body_replacements'] += body_repl
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
        logger.info(f"URL Segment: {self.url_segment}")
        logger.info(f"Replace Mode: {self.replace_mode.value}")
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
        if self.replace_mode != ReplaceMode.BODY:
            logger.info(f"  • Front matter replacements: {self.stats['frontmatter_replacements']}")
        if self.replace_mode != ReplaceMode.FRONT:
            logger.info(f"  • Body replacements: {self.stats['body_replacements']}")
        logger.info("="*80)
        
        # ذخیره گزارش جزئیات در فایل
        report_filename = f"url_segment_replacer_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("URL Segment Replacer - Detail Report\n")
            f.write("="*80 + "\n\n")
            
            f.write(f"Directory: {self.base_directory}\n")
            f.write(f"URL Segment: {self.url_segment}\n")
            f.write(f"Replace Mode: {self.replace_mode.value}\n")
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
            f.write(f"Front matter replacements: {self.stats['frontmatter_replacements']}\n")
            f.write(f"Body replacements: {self.stats['body_replacements']}\n\n")
            
            # فایل‌های پردازش شده
            if self.processed_files_list:
                f.write("="*80 + "\n")
                f.write(f"Processed Files ({len(self.processed_files_list)} items):\n")
                f.write("="*80 + "\n")
                for item in self.processed_files_list:
                    f.write(f"\n📄 {item['file']}\n")
                    f.write(f"   - Mode: {item['mode']}\n")
                    f.write(f"   - Total replacements: {item['total_replacements']}\n")
                    if item['frontmatter_replacements'] > 0:
                        f.write(f"   - Front matter: {item['frontmatter_replacements']}\n")
                    if item['body_replacements'] > 0:
                        f.write(f"   - Body: {item['body_replacements']}\n")
            
            # فایل‌های رد شده
            if self.skipped_files_list:
                f.write("\n" + "="*80 + "\n")
                f.write(f"Skipped Files ({len(self.skipped_files_list)} items):\n")
                f.write("="*80 + "\n")
                for item in self.skipped_files_list:
                    f.write(f"\n⚠ {item['file']}\n")
                    f.write(f"   Reason: {item['reason']}\n")
            
            # فایل‌های با خطا
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
    دریافت اطلاعات از کاربر
    
    Returns:
        tuple: (directory_path, url_segment, replace_mode)
    """
    print("="*80)
    print("URL Segment Replacer - Add custom URL segment to Hugo articles")
    print("="*80)
    print("\nThis script adds a custom URL segment to URLs in your articles:")
    print(f"  From: https://davoodya.ir/...")
    print(f"  To:   https://davoodya.ir/YOUR-SEGMENT/...")
    print("-"*80)
    
    # دریافت مسیر دایرکتوری
    user_input = input("\nEnter directory path (Press Enter for default 'content/'): ").strip()
    
    # حذف کوتیشن‌ها اگر وجود داشته باشد
    user_input = user_input.strip('"').strip("'")
    
    # اگر خالی بود، از پیش‌فرض استفاده کن
    if not user_input:
        # پیدا کردن دایرکتوری content نسبت به موقعیت اسکریپت
        script_dir = Path(__file__).parent
        content_dir = script_dir / "content"
        directory_path = str(content_dir)
    else:
        directory_path = user_input
    
    print(f"\nSelected directory: {directory_path}")
    print("-"*80)
    
    # دریافت URL segment
    url_segment = input("\nEnter URL segment to add (e.g., 'knowledge', 'blog', 'docs'): ").strip()
    
    # اعتبارسنجی URL segment
    while not url_segment or '/' in url_segment or ' ' in url_segment:
        print("❌ Error: URL segment cannot be empty or contain '/' or spaces!")
        url_segment = input("Enter URL segment again: ").strip()
    
    print(f"\nURL segment: {url_segment}")
    print(f"Pattern will be: https://davoodya.ir/ → https://davoodya.ir/{url_segment}/")
    print("-"*80)
    
    # دریافت حالت جایگزینی
    print("\nSelect replacement mode:")
    print("  [a] ALL   - Replace in entire file (front matter + body)")
    print("  [f] FRONT - Replace only in front matter")
    print("  [b] BODY  - Replace only in body (after front matter)")
    print()
    
    mode_input = input("Enter mode (a/f/b): ").strip().lower()
    
    # اعتبارسنجی حالت
    while mode_input not in ['a', 'all', 'f', 'front', 'b', 'body']:
        print("❌ Error: Invalid mode! Please enter 'a', 'f', or 'b'")
        mode_input = input("Enter mode (a/f/b): ").strip().lower()
    
    # تبدیل به ReplaceMode
    if mode_input in ['a', 'all']:
        replace_mode = ReplaceMode.ALL
        mode_name = "ALL (entire file)"
    elif mode_input in ['f', 'front']:
        replace_mode = ReplaceMode.FRONT
        mode_name = "FRONT (front matter only)"
    else:  # b or body
        replace_mode = ReplaceMode.BODY
        mode_name = "BODY (body only)"
    
    print(f"\nSelected mode: {mode_name}")
    
    return directory_path, url_segment, replace_mode


def main():
    """تابع اصلی برنامه"""
    try:
        # دریافت ورودی کاربر
        directory_path, url_segment, replace_mode = get_user_input()
        
        print("\n" + "="*80)
        print("Summary:")
        print("="*80)
        print(f"Directory: {directory_path}")
        print(f"URL Segment: {url_segment}")
        print(f"Mode: {replace_mode.value}")
        print(f"From: https://davoodya.ir/...")
        print(f"To:   https://davoodya.ir/{url_segment}/...")
        print("-"*80)
        
        # تایید کاربر
        confirm = input("\nDo you want to continue? (y/n): ").strip().lower()
        
        if confirm not in ['y', 'yes']:
            print("\n❌ Operation cancelled.")
            return
        
        print("\n" + "="*80)
        print("Starting processing...")
        print("="*80 + "\n")
        
        # ایجاد و اجرای replacer
        replacer = URLSegmentReplacer(directory_path, url_segment, replace_mode)
        success = replacer.run()
        
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
