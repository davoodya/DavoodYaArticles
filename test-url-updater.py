#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست اسکریپت URL Canonical Updater
این فایل برای تست خودکار اسکریپت اصلی استفاده می‌شود.
"""

import sys
import importlib.util
from pathlib import Path

# Import کلاس از فایل اصلی
script_path = Path(__file__).parent / "url-canonical-updater.py"
spec = importlib.util.spec_from_file_location("url_canonical_updater", script_path)
url_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(url_module)
URLCanonicalUpdater = url_module.URLCanonicalUpdater

def test_updater():
    """تست اسکریپت روی دایرکتوری تست"""
    
    print("="*80)
    print("تست URL Canonical Updater")
    print("="*80)
    
    # مسیر دایرکتوری تست
    test_dir = Path(__file__).parent / "test" / "test-url-updater"
    
    print(f"\nدایرکتوری تست: {test_dir}")
    
    if not test_dir.exists():
        print("❌ خطا: دایرکتوری تست وجود ندارد!")
        return False
    
    # نمایش محتوای قبل از تغییر
    print("\n" + "="*80)
    print("محتوای فایل‌ها قبل از تغییر:")
    print("="*80)
    
    for md_file in test_dir.glob("*.md"):
        print(f"\n📄 {md_file.name}:")
        print("-" * 40)
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # نمایش تنها 10 خط اول
            lines = content.split('\n')[:10]
            for line in lines:
                if 'url' in line.lower() or 'canonical' in line.lower():
                    print(f"  → {line}")
    
    # اجرای updater
    print("\n" + "="*80)
    print("در حال اجرای updater...")
    print("="*80 + "\n")
    
    updater = URLCanonicalUpdater(str(test_dir))
    success = updater.run()
    
    # نمایش محتوای بعد از تغییر
    print("\n" + "="*80)
    print("محتوای فایل‌ها بعد از تغییر:")
    print("="*80)
    
    for md_file in test_dir.glob("*.md"):
        print(f"\n📄 {md_file.name}:")
        print("-" * 40)
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')[:10]
            for line in lines:
                if 'url' in line.lower() or 'canonical' in line.lower():
                    print(f"  → {line}")
    
    if success:
        print("\n" + "="*80)
        print("✅ تست با موفقیت انجام شد!")
        print("="*80)
        return True
    else:
        print("\n" + "="*80)
        print("❌ تست با خطا مواجه شد!")
        print("="*80)
        return False

if __name__ == "__main__":
    test_updater()
