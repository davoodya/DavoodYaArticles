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
        logger.info("URL و Canonical Updater - شروع پردازش")
        logger.info("="*80)
        logger.info(f"دایرکتوری پایه: {self.base_directory}")
        logger.info(f"الگوی جستجو: {self.find_pattern}")
        logger.info(f"الگوی جایگزین: {self.replace_pattern}")
        logger.info("-"*80)
    
    def validate_directory(self):
        """
        اعتبارسنجی دایرکتوری ورودی
        
        Returns:
            bool: True اگر دایرکتوری معتبر باشد
        """
        if not self.base_directory.exists():
            logger.error(f"خطا: دایرکتوری '{self.base_directory}' وجود ندارد!")
            return False
        
        if not self.base_directory.is_dir():
            logger.error(f"خطا: '{self.base_directory}' یک دایرکتوری نیست!")
            return False
        
        logger.info(f"✓ دایرکتوری معتبر است: {self.base_directory}")
        return True
    
    def find_markdown_files(self):
        """
        یافتن تمام فایل‌های Markdown در دایرکتوری و زیردایرکتوری‌ها
        
        Returns:
            list: لیست مسیرهای فایل‌های Markdown
        """
        logger.info("در حال جستجوی فایل‌های Markdown...")
        markdown_files = []
        
        for root, dirs, files in os.walk(self.base_directory):
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    markdown_files.append(file_path)
        
        logger.info(f"✓ تعداد {len(markdown_files)} فایل Markdown پیدا شد")
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
                    logger.debug(f"  - {count} مورد 'url' به‌روزرسانی شد")
                elif field_type == 'canonical':
                    canonical_count = count
                    logger.debug(f"  - {count} مورد 'canonical' به‌روزرسانی شد")
        
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
            logger.info(f"در حال پردازش: {file_path.relative_to(self.base_directory)}")
            
            # خواندن فایل
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # استخراج front matter
            frontmatter, body, delimiter = self.extract_frontmatter(content)
            
            if frontmatter is None:
                logger.warning(f"  ⚠ هشدار: front matter یافت نشد - فایل رد شد")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'بدون front matter'
                })
                return False, 0, 0, 0
            
            # بررسی اینکه آیا URL های قدیمی وجود دارند
            if self.find_pattern not in frontmatter:
                logger.info(f"  ℹ اطلاع: URL قدیمی یافت نشد - فایل رد شد")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'URL قدیمی وجود ندارد'
                })
                return False, 0, 0, 0
            
            # به‌روزرسانی front matter
            updated_frontmatter, replacement_count, url_count, canonical_count = \
                self.update_frontmatter_urls(frontmatter)
            
            if replacement_count == 0:
                logger.info(f"  ℹ اطلاع: هیچ تغییری لازم نبود - فایل رد شد")
                self.skipped_files_list.append({
                    'file': str(file_path.relative_to(self.base_directory)),
                    'reason': 'نیازی به تغییر نبود'
                })
                return False, 0, 0, 0
            
            # ساخت محتوای جدید
            new_content = f"{delimiter}\n{updated_frontmatter}\n{delimiter}\n{body}"
            
            # نوشتن فایل
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            logger.info(f"  ✓ موفقیت: {replacement_count} مورد جایگزین شد " +
                       f"(url: {url_count}, canonical: {canonical_count})")
            
            self.processed_files_list.append({
                'file': str(file_path.relative_to(self.base_directory)),
                'total_replacements': replacement_count,
                'url_replacements': url_count,
                'canonical_replacements': canonical_count
            })
            
            return True, replacement_count, url_count, canonical_count
            
        except Exception as e:
            logger.error(f"  ✗ خطا در پردازش فایل: {str(e)}")
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
            logger.warning("هیچ فایل Markdown برای پردازش یافت نشد!")
            return
        
        logger.info("-"*80)
        logger.info("شروع پردازش فایل‌ها...")
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
        logger.info("گزارش نهایی پردازش")
        logger.info("="*80)
        logger.info(f"دایرکتوری پردازش شده: {self.base_directory}")
        logger.info(f"تاریخ و زمان: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("-"*80)
        logger.info("آمار کلی:")
        logger.info(f"  • کل فایل‌های یافت شده: {self.stats['total_files']}")
        logger.info(f"  • فایل‌های پردازش شده: {self.stats['processed_files']}")
        logger.info(f"  • فایل‌های رد شده: {self.stats['skipped_files']}")
        logger.info(f"  • فایل‌های با خطا: {self.stats['error_files']}")
        logger.info("-"*80)
        logger.info("آمار جایگزینی:")
        logger.info(f"  • کل جایگزینی‌ها: {self.stats['total_replacements']}")
        logger.info(f"  • جایگزینی URL: {self.stats['url_replacements']}")
        logger.info(f"  • جایگزینی Canonical: {self.stats['canonical_replacements']}")
        logger.info("="*80)
        
        # ذخیره گزارش جزئیات در فایل
        report_filename = f"url_canonical_updater_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("گزارش جزئیات پردازش URL و Canonical\n")
            f.write("="*80 + "\n\n")
            
            f.write(f"دایرکتوری: {self.base_directory}\n")
            f.write(f"تاریخ و زمان: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"الگوی جستجو: {self.find_pattern}\n")
            f.write(f"الگوی جایگزین: {self.replace_pattern}\n\n")
            
            f.write("-"*80 + "\n")
            f.write("آمار کلی:\n")
            f.write("-"*80 + "\n")
            f.write(f"کل فایل‌های یافت شده: {self.stats['total_files']}\n")
            f.write(f"فایل‌های پردازش شده: {self.stats['processed_files']}\n")
            f.write(f"فایل‌های رد شده: {self.stats['skipped_files']}\n")
            f.write(f"فایل‌های با خطا: {self.stats['error_files']}\n\n")
            
            f.write(f"کل جایگزینی‌ها: {self.stats['total_replacements']}\n")
            f.write(f"جایگزینی URL: {self.stats['url_replacements']}\n")
            f.write(f"جایگزینی Canonical: {self.stats['canonical_replacements']}\n\n")
            
            # فایل‌های پردازش شده
            if self.processed_files_list:
                f.write("="*80 + "\n")
                f.write(f"فایل‌های پردازش شده ({len(self.processed_files_list)} مورد):\n")
                f.write("="*80 + "\n")
                for item in self.processed_files_list:
                    f.write(f"\n📄 {item['file']}\n")
                    f.write(f"   - کل جایگزینی‌ها: {item['total_replacements']}\n")
                    f.write(f"   - URL: {item['url_replacements']}\n")
                    f.write(f"   - Canonical: {item['canonical_replacements']}\n")
            
            # فایل‌های رد شده
            if self.skipped_files_list:
                f.write("\n" + "="*80 + "\n")
                f.write(f"فایل‌های رد شده ({len(self.skipped_files_list)} مورد):\n")
                f.write("="*80 + "\n")
                for item in self.skipped_files_list:
                    f.write(f"\n⚠ {item['file']}\n")
                    f.write(f"   دلیل: {item['reason']}\n")
            
            # فایل‌های با خطا
            if self.error_files_list:
                f.write("\n" + "="*80 + "\n")
                f.write(f"فایل‌های با خطا ({len(self.error_files_list)} مورد):\n")
                f.write("="*80 + "\n")
                for item in self.error_files_list:
                    f.write(f"\n✗ {item['file']}\n")
                    f.write(f"   خطا: {item['error']}\n")
        
        logger.info(f"\n✓ گزارش جزئیات در فایل ذخیره شد: {report_filename}")
        logger.info(f"✓ لاگ کامل در فایل ذخیره شد: {log_filename}")
    
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
    print("URL و Canonical Updater - به‌روزرسانی front matter مقالات Hugo")
    print("="*80)
    print("\nاین اسکریپت segment جدید 'knowledge' را به URLها اضافه می‌کند:")
    print(f"  از: https://davoodya.ir/...")
    print(f"  به: https://davoodya.ir/knowledge/...")
    print("-"*80)
    
    # دریافت مسیر
    user_input = input("\nمسیر دایرکتوری را وارد کنید (Enter برای پیش‌فرض 'content/'): ").strip()
    
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
        
        print(f"\nدایرکتوری انتخاب شده: {directory_path}")
        print("-"*80)
        
        # تایید کاربر
        confirm = input("\nآیا می‌خواهید ادامه دهید؟ (y/n): ").strip().lower()
        
        if confirm not in ['y', 'yes', 'بله']:
            print("\n❌ عملیات لغو شد.")
            return
        
        print("\n" + "="*80)
        print("شروع پردازش...")
        print("="*80 + "\n")
        
        # ایجاد و اجرای updater
        updater = URLCanonicalUpdater(directory_path)
        success = updater.run()
        
        if success:
            print("\n" + "="*80)
            print("✓ پردازش با موفقیت تکمیل شد!")
            print("="*80)
        else:
            print("\n" + "="*80)
            print("✗ پردازش با خطا مواجه شد.")
            print("="*80)
            
    except KeyboardInterrupt:
        print("\n\n❌ عملیات توسط کاربر لغو شد.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"خطای غیرمنتظره: {str(e)}", exc_info=True)
        print(f"\n✗ خطای غیرمنتظره: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
