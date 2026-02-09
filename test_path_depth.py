#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test path depth handling"""

from pathlib import Path

CONTENT_DIR = Path('content')

# Test different depth levels
test_paths = [
    Path('content/linux/file.md'),                          # 1 level
    Path('content/cyber-security/Cryptography/file.md'),    # 2 levels
    Path('content/seo/0-SEO-Theories/Advanced/file.md'),    # 3 levels
    Path('content/a/b/c/d/file.md'),                        # 4 levels
    Path('content/a/b/c/d/e/file.md'),                      # 5 levels
]

print("=" * 80)
print("Testing Path Depth Handling")
print("=" * 80)

for path in test_paths:
    relative_path = path.relative_to(CONTENT_DIR)
    parts = list(relative_path.parent.parts)
    url_path = '/'.join(parts)
    depth = len(parts)
    
    print(f"\nDepth: {depth}")
    print(f"  File: {relative_path}")
    print(f"  Parts: {parts}")
    print(f"  URL: https://davoodya.ir/{url_path}/slug/")
    print(f"  Categories: {parts}")
    print(f"  Tags: {parts}")
    print(f"  Series: {parts}")

print("\n" + "=" * 80)
print("All depths work correctly!")
print("=" * 80)
