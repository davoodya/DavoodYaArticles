# URL Segment Replacer - Complete Guide

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Replace Modes](#replace-modes)
- [Examples](#examples)
- [Outputs](#outputs)
- [Important Notes](#important-notes)

---

## 📖 Overview

**URL Segment Replacer** is an advanced Python script designed to add a custom URL segment to all URLs in your Hugo articles. This is the flexible version that allows you to:

1. **Choose any URL segment** (not limited to 'knowledge')
2. **Choose where to replace**: entire file, front matter only, or body only

### What it does:

```
From: https://davoodya.ir/category/article/
To:   https://davoodya.ir/YOUR-SEGMENT/category/article/
```

---

## ✨ Features

### 1. **Custom URL Segment**
You can specify any URL segment you want:
- `knowledge`
- `blog`
- `docs`
- `tutorials`
- `guides`
- Or any other segment name

### 2. **Three Replace Modes**

#### a) **ALL Mode** - Entire File
- Replaces URLs everywhere in the file
- Both front matter AND body
- Most comprehensive option

#### b) **FRONT Mode** - Front Matter Only
- Replaces URLs only in front matter
- Body content remains unchanged
- Perfect for updating metadata

#### c) **BODY Mode** - Body Only
- Replaces URLs only in article body
- Front matter remains unchanged
- Perfect for updating article links

### 3. **Universal Features**
- ✅ Recursive directory processing
- ✅ Supports TOML (`---`) and YAML (`+++`)
- ✅ Handles spaces in paths
- ✅ Complete logging and reporting
- ✅ Safe error handling
- ✅ User confirmation before processing

---

## 🚀 Usage

### Basic Usage

```bash
python url-segment-replacer.py
```

Then follow the prompts:

1. **Enter directory path**: Press Enter for default `content/`, or type a custom path
2. **Enter URL segment**: Type your desired segment (e.g., `knowledge`)
3. **Select mode**: Choose `a` (all), `f` (front), or `b` (body)
4. **Confirm**: Type `y` to start processing

### Example Session

```
================================================================================
URL Segment Replacer - Add custom URL segment to Hugo articles
================================================================================

This script adds a custom URL segment to URLs in your articles:
  From: https://davoodya.ir/...
  To:   https://davoodya.ir/YOUR-SEGMENT/...
--------------------------------------------------------------------------------

Enter directory path (Press Enter for default 'content/'): content/cyber-security

Selected directory: content/cyber-security
--------------------------------------------------------------------------------

Enter URL segment to add (e.g., 'knowledge', 'blog', 'docs'): knowledge

URL segment: knowledge
Pattern will be: https://davoodya.ir/ → https://davoodya.ir/knowledge/
--------------------------------------------------------------------------------

Select replacement mode:
  [a] ALL   - Replace in entire file (front matter + body)
  [f] FRONT - Replace only in front matter
  [b] BODY  - Replace only in body (after front matter)

Enter mode (a/f/b): a

Selected mode: ALL (entire file)

================================================================================
Summary:
================================================================================
Directory: content/cyber-security
URL Segment: knowledge
Mode: all
From: https://davoodya.ir/...
To:   https://davoodya.ir/knowledge/...
--------------------------------------------------------------------------------

Do you want to continue? (y/n): y
```

---

## 🎯 Replace Modes

### Mode A: ALL (Entire File)

**When to use:**
- You want to update ALL URLs in the articles
- Both front matter and body need updating

**Example:**

**Before:**
```markdown
---
url = "https://davoodya.ir/cyber-security/article/"
canonical = "https://davoodya.ir/cyber-security/article/"
---

Check out: https://davoodya.ir/network/basics/
```

**After (ALL mode with segment "knowledge"):**
```markdown
---
url = "https://davoodya.ir/knowledge/cyber-security/article/"
canonical = "https://davoodya.ir/knowledge/cyber-security/article/"
---

Check out: https://davoodya.ir/knowledge/network/basics/
```

**Result:** ✅ 3 replacements (2 in front matter + 1 in body)

---

### Mode F: FRONT (Front Matter Only)

**When to use:**
- You only want to update metadata URLs
- Body links should remain unchanged

**Example:**

**Before:**
```markdown
---
url = "https://davoodya.ir/cyber-security/article/"
canonical = "https://davoodya.ir/cyber-security/article/"
---

Check out: https://davoodya.ir/network/basics/
```

**After (FRONT mode with segment "knowledge"):**
```markdown
---
url = "https://davoodya.ir/knowledge/cyber-security/article/"
canonical = "https://davoodya.ir/knowledge/cyber-security/article/"
---

Check out: https://davoodya.ir/network/basics/  ← Unchanged!
```

**Result:** ✅ 2 replacements (only in front matter)

---

### Mode B: BODY (Body Only)

**When to use:**
- You only want to update links in article content
- Front matter should remain unchanged

**Example:**

**Before:**
```markdown
---
url = "https://davoodya.ir/cyber-security/article/"
canonical = "https://davoodya.ir/cyber-security/article/"
---

Check out: https://davoodya.ir/network/basics/
Also: https://davoodya.ir/tools/guide/
```

**After (BODY mode with segment "knowledge"):**
```markdown
---
url = "https://davoodya.ir/cyber-security/article/"  ← Unchanged!
canonical = "https://davoodya.ir/cyber-security/article/"  ← Unchanged!
---

Check out: https://davoodya.ir/knowledge/network/basics/
Also: https://davoodya.ir/knowledge/tools/guide/
```

**Result:** ✅ 2 replacements (only in body)

---

## 📊 Outputs

The script generates two files:

### 1. Log File
**Name:** `url_segment_replacer_YYYYMMDD_HHMMSS.log`

**Content:**
```
2026-02-10 12:52:35 - INFO - URL Segment Replacer - Starting Process
2026-02-10 12:52:35 - INFO - Base Directory: H:\Repo\Hugo\davoodya\content
2026-02-10 12:52:35 - INFO - URL Segment: knowledge
2026-02-10 12:52:35 - INFO - Replace Mode: all
2026-02-10 12:52:35 - INFO - ✓ Found 45 Markdown files
2026-02-10 12:52:35 - INFO - [1/45] Processing: article-1.md
2026-02-10 12:52:35 - INFO -   → Mode: ALL - Replacing in entire file
2026-02-10 12:52:35 - INFO -   ✓ Success: 5 replacement(s) made
...
```

### 2. Report File
**Name:** `url_segment_replacer_report_YYYYMMDD_HHMMSS.txt`

**Content:**
```
================================================================================
URL Segment Replacer - Detail Report
================================================================================

Directory: H:\Repo\Hugo\davoodya\content
URL Segment: knowledge
Replace Mode: all
Date & Time: 2026-02-10 12:52:35

--------------------------------------------------------------------------------
General Statistics:
--------------------------------------------------------------------------------
Total files found: 45
Files processed: 42
Files skipped: 3
Files with errors: 0

Total replacements: 127
Front matter replacements: 84
Body replacements: 43

================================================================================
Processed Files (42 items):
================================================================================

📄 cyber-security/SANS-401/article-1.md
   - Mode: all
   - Total replacements: 5
   - Front matter: 2
   - Body: 3
...
```

---

## ⚠️ Important Notes

### 1. Backup Before Running!

**Always create a backup before processing:**

```bash
# Using Git (recommended)
git add .
git commit -m "Before URL segment replacement"

# Or manual copy
cp -r content content_backup
```

### 2. Test on a Small Directory First

Test the script on a small subset before running on all files:

```bash
python url-segment-replacer.py
# Enter: content/cyber-security/SANS-401
# Segment: knowledge
# Mode: a
```

### 3. URL Segment Rules

The URL segment:
- ❌ Cannot be empty
- ❌ Cannot contain `/` (slashes)
- ❌ Cannot contain spaces
- ✅ Use lowercase and hyphens: `my-segment`

**Good examples:**
- `knowledge`
- `blog`
- `docs`
- `my-articles`

**Bad examples:**
- ❌ `my segment` (contains space)
- ❌ `my/segment` (contains slash)
- ❌ `` (empty)

### 4. Choose the Right Mode

| Scenario | Mode |
|----------|------|
| Update everything | ALL |
| Fix metadata only | FRONT |
| Update article links only | BODY |
| Already updated front matter | BODY |
| Already updated body | FRONT |

### 5. Files That Will Be Skipped

The script skips files that:
- Don't contain the old URL pattern
- Have no front matter (in FRONT mode)
- Have no replacements to make

### 6. Re-running the Script

You can safely re-run the script:
- Already updated files will be skipped
- Only files with old URL patterns will be processed

---

## 🧪 Testing

### Quick Test

```bash
python test-segment-simple.py a    # Test ALL mode
python test-segment-simple.py f    # Test FRONT mode
python test-segment-simple.py b    # Test BODY mode
```

### Test Results

**ALL Mode:**
- ✅ 5 replacements (2 in front matter + 3 in body)

**FRONT Mode:**
- ✅ 2 replacements (only front matter)
- ✅ Body remains unchanged

**BODY Mode:**
- ✅ 3 replacements (only body)
- ✅ Front matter remains unchanged

---

## 🔍 Troubleshooting

### Issue: "Directory does not exist"
**Solution:** Check the path you entered. Use full/absolute path.

### Issue: "URL segment cannot be empty"
**Solution:** Enter a valid segment name (e.g., `knowledge`, `blog`).

### Issue: No files processed
**Solution:** 
- Check if files contain the old URL pattern
- Verify you're in the correct directory
- Check if files have `.md` extension

### Issue: "No front matter found" in FRONT mode
**Solution:** 
- Use ALL or BODY mode instead
- Or add front matter to your files

---

## 📋 Checklist

### Before Running:
- [ ] Created a backup (Git commit or manual copy)
- [ ] Tested on a small directory first
- [ ] Verified the URL segment is correct
- [ ] Selected the appropriate mode
- [ ] Ready to review logs and reports

### After Running:
- [ ] Reviewed the log file
- [ ] Checked the report file
- [ ] Manually inspected some processed files
- [ ] Verified URLs are correct
- [ ] Tested Hugo build: `hugo server`

---

## 💡 Use Cases

### Use Case 1: Add 'knowledge' to All URLs
```
Mode: ALL
Segment: knowledge
Result: All URLs get /knowledge/ added
```

### Use Case 2: Add 'blog' to Article Links Only
```
Mode: BODY
Segment: blog
Result: Only article body links get /blog/ added
```

### Use Case 3: Fix Front Matter URLs
```
Mode: FRONT
Segment: docs
Result: Only front matter URLs get /docs/ added
```

---

## 📞 Support

If you encounter issues:
1. Check the log file for detailed error messages
2. Verify your input (directory, segment, mode)
3. Test on a single file first
4. Review this documentation

---

## 📅 Version History

### Version 1.0.0 (2026-02-10)
- Initial release
- Three replace modes: ALL, FRONT, BODY
- Custom URL segment input
- Complete logging and reporting
- Full test coverage

---

## ⚡ Quick Reference

```bash
# Run the script
python url-segment-replacer.py

# Inputs needed:
# 1. Directory path (default: content/)
# 2. URL segment (e.g., knowledge)
# 3. Mode: a/f/b (all/front/body)
# 4. Confirmation: y

# Test the script
python test-segment-simple.py [a|f|b]
```

---

**Remember:** Always backup your files before running the script! 🔒
