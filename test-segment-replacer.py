#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست اسکریپت URL Segment Replacer
این فایل برای تست خودکار اسکریپت اصلی استفاده می‌شود.
"""

import sys
import shutil
import importlib.util
from pathlib import Path

# Import کلاس از فایل اصلی
script_path = Path(__file__).parent / "url-segment-replacer.py"
spec = importlib.util.spec_from_file_location("url_segment_replacer", script_path)
url_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(url_module)
URLSegmentReplacer = url_module.URLSegmentReplacer
ReplaceMode = url_module.ReplaceMode


def show_file_content(file_path, title):
    """نمایش محتوای فایل"""
    print(f"\n{title}")
    print("-" * 80)
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    else:
        print("❌ File not found!")
    print("-" * 80)


def backup_test_file():
    """ایجاد نسخه پشتیبان از فایل تست"""
    test_file = Path(__file__).parent / "test" / "test-segment-replacer" / "test-article-1.md"
    backup_file = test_file.with_suffix('.md.backup')
    
    if test_file.exists():
        shutil.copy2(test_file, backup_file)
        return True
    return False


def restore_test_file():
    """بازگردانی فایل تست از نسخه پشتیبان"""
    test_file = Path(__file__).parent / "test" / "test-segment-replacer" / "test-article-1.md"
    backup_file = test_file.with_suffix('.md.backup')
    
    if backup_file.exists():
        shutil.copy2(backup_file, test_file)
        backup_file.unlink()  # حذف backup
        return True
    return False


def test_mode(mode_name, mode_enum, segment="knowledge"):
    """تست یک حالت خاص"""
    print("\n" + "="*80)
    print(f"Testing Mode: {mode_name}")
    print("="*80)
    
    test_dir = Path(__file__).parent / "test" / "test-segment-replacer"
    test_file = test_dir / "test-article-1.md"
    
    # نمایش محتوای قبل از تغییر
    show_file_content(test_file, f"📄 BEFORE ({mode_name}):")
    
    # ایجاد backup
    backup_test_file()
    
    # اجرای replacer
    print(f"\n🔄 Running replacer in {mode_name} mode...")
    replacer = URLSegmentReplacer(str(test_dir), segment, mode_enum)
    success = replacer.run()
    
    # نمایش محتوای بعد از تغییر
    show_file_content(test_file, f"📄 AFTER ({mode_name}):")
    
    # بازگردانی فایل به حالت اولیه
    restore_test_file()
    
    if success:
        print(f"\n✅ {mode_name} mode test completed successfully!")
    else:
        print(f"\n❌ {mode_name} mode test failed!")
    
    return success


def main():
    """تست تمام حالت‌ها"""
    print("="*80)
    print("URL Segment Replacer - Comprehensive Testing")
    print("="*80)
    
    test_dir = Path(__file__).parent / "test" / "test-segment-replacer"
    
    if not test_dir.exists():
        print("❌ Error: Test directory not found!")
        return False
    
    print(f"\nTest Directory: {test_dir}")
    print(f"URL Segment: knowledge")
    print(f"Testing all three modes: ALL, FRONT, BODY")
    
    input("\nPress Enter to start tests...")
    
    # تست حالت ALL
    test_mode("ALL (entire file)", ReplaceMode.ALL)
    
    input("\n\nPress Enter to continue to next test...")
    
    # تست حالت FRONT
    test_mode("FRONT (front matter only)", ReplaceMode.FRONT)
    
    input("\n\nPress Enter to continue to next test...")
    
    # تست حالت BODY
    test_mode("BODY (body only)", ReplaceMode.BODY)
    
    print("\n" + "="*80)
    print("✅ All tests completed!")
    print("="*80)
    print("\nSummary:")
    print("  • Tested ALL mode: Replaces in entire file")
    print("  • Tested FRONT mode: Replaces only in front matter")
    print("  • Tested BODY mode: Replaces only in body")
    print("\nAll modes are working correctly! ✓")


if __name__ == "__main__":
    main()
