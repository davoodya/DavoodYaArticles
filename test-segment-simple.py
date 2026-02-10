#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست ساده اسکریپت URL Segment Replacer
"""

import sys
import importlib.util
from pathlib import Path

# Import کلاس از فایل اصلی
script_path = Path(__file__).parent / "url-segment-replacer.py"
spec = importlib.util.spec_from_file_location("url_segment_replacer", script_path)
url_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(url_module)
URLSegmentReplacer = url_module.URLSegmentReplacer
ReplaceMode = url_module.ReplaceMode


def test_mode(mode_name, mode_enum):
    """تست یک حالت"""
    print("="*80)
    print(f"Testing Mode: {mode_name}")
    print("="*80)
    
    test_dir = Path(__file__).parent / "test" / "test-segment-replacer"
    test_file = test_dir / "test-article-1.md"
    
    print(f"\nTest file: {test_file}")
    
    # نمایش محتوای قبل
    print("\n--- BEFORE ---")
    with open(test_file, 'r', encoding='utf-8') as f:
        before = f.read()
        print(before)
    
    # اجرای replacer
    print("\n--- PROCESSING ---")
    replacer = URLSegmentReplacer(str(test_dir), "knowledge", mode_enum)
    replacer.run()
    
    # نمایش محتوای بعد
    print("\n--- AFTER ---")
    with open(test_file, 'r', encoding='utf-8') as f:
        after = f.read()
        print(after)
    
    print("\n" + "="*80)
    print(f"Test completed! Mode: {mode_name}")
    print("="*80)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode in ['a', 'all']:
            test_mode("ALL (entire file)", ReplaceMode.ALL)
        elif mode in ['f', 'front']:
            test_mode("FRONT (front matter only)", ReplaceMode.FRONT)
        elif mode in ['b', 'body']:
            test_mode("BODY (body only)", ReplaceMode.BODY)
        else:
            print("Usage: python test-segment-simple.py [a|f|b]")
    else:
        # پیش‌فرض: تست حالت ALL
        test_mode("ALL (entire file)", ReplaceMode.ALL)
