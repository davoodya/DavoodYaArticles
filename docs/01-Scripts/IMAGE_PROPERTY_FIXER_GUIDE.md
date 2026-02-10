# Image Property Fixer Pipeline - Complete Guide

## 📋 Overview

**`image-property-fixer.ps1`** is a PowerShell automation script that orchestrates 7 Python scripts in sequence to import articles from Obsidian to Hugo and fix all image properties.

**Version**: 2.0 (Fixed & Enhanced)  
**Date**: 2026-02-10  
**Type**: PowerShell Pipeline Script

---

## 🎯 What It Does

This script automates the complete workflow:

1. **Import Images** from Obsidian Vault
2. **Add Titles** to articles
3. **Add ALT attributes** to images
4. **Rename Images** with slugified names
5. **Update Image References** in articles
6. **Remove Obsidian TOC**
7. **Add Enhanced Hugo Front Matter**

---

## 🚀 Quick Start

### Run the Script

```powershell
.\image-property-fixer.ps1
```

Or right-click → "Run with PowerShell"

### That's it!
The script will:
- ✅ Verify all Python scripts exist
- ✅ Execute them in the correct order
- ✅ Show colored progress
- ✅ Generate a comprehensive report

---

## 📊 Pipeline Steps

### Step 1: Import New Articles Images
**Script**: `convert_images.py`
- **Source**: Obsidian Vault Attachment folder
- **Destination**: `static/images/[category]/`
- **Process**: Copies only new images (skips existing)

**Example**:
```
Obsidian: D:\Obsidian\Attachments\image.png
→ Hugo: static/images/cyber-security/image.png
```

---

### Step 2: Add Title for New Articles ⚠️ REQUIRED
**Script**: `title-adder.py`
- **Purpose**: Adds `title = "Article Name"` to front matter
- **Process**: Extracts title from filename, removes E-numbers
- **Critical**: This step is REQUIRED for Steps 3, 4, 5

**Example**:
```markdown
Filename: "E3 Virtualization Basics.md"

Before:
+++
date = "2024-01-01"
+++

After:
+++
date = "2024-01-01"
title = "Virtualization Basics"
+++
```

---

### Step 3: Add ALT for Images
**Script**: `altimage-adder.py`
- **Purpose**: Adds ALT attributes to all images
- **Based on**: Article title property (from Step 2)
- **Improves**: SEO and accessibility

**Example**:
```markdown
Article title = "Network Basics"

Before:
![](image.png)

After:
![Network Basics](image.png)
```

---

### Step 4: Rename Images in /static/images
**Script**: `images-renamer.py`
- **Purpose**: Renames all images with slugified names
- **Format**: `lowercase-with-dashes.extension`
- **Handles**: Special characters, spaces, parentheses

**Example**:
```
Before: "Pasted Image 20260203212022.png"
After:  "pasted-image-20260203212022.png"

Before: "SANS-401-Networking(401.1)-1.png"
After:  "sans-401-networking-4011-1.png"
```

---

### Step 5: Update Image References in Articles
**Script**: `image-article-renamer.py`
- **Purpose**: Updates all image paths in markdown files
- **Matches**: New names from Step 4
- **Ensures**: All references are synchronized

**Example**:
```markdown
Before:
![alt](Pasted Image 20260203212022.png)

After:
![alt](pasted-image-20260203212022.png)
```

---

### Step 6: Remove Obsidian TOC
**Script**: `toc-remover.py`
- **Purpose**: Removes Obsidian's Table of Contents
- **Reason**: Hugo generates its own TOC
- **Cleans**: Markdown structure

**Example**:
```markdown
Before:
## TOC
- [[Section 1]]
- [[Section 2]]
---

# Article Content

After:
# Article Content
```

---

### Step 7: Add Enhanced Hugo Front Matter
**Script**: `obsidian-property-remover-enhanced.py`
- **Purpose**: Adds comprehensive Hugo properties
- **Includes**: title, slug, date, categories, tags, SEO, Open Graph
- **Removes**: Old Obsidian properties

**Example**:
```markdown
Before:
---
Date: 2024-01-01
tags: network
---

After:
+++
title = "Network Basics"
slug = "network-basics"
date = "2024-01-01T12:00:00+03:30"
categories = ["network"]
tags = ["network", "basics"]
description = "Learn network fundamentals..."
featured_image = "/images/network/image.png"
readingTime = 5
# ... and 20+ more properties
+++
```

---

## 🎨 Features

### 1. **Beautiful Output**
- ✅ Color-coded messages (Green = Success, Red = Error, Yellow = Warning)
- ✅ Progress indicators for each step
- ✅ Boxed titles and separators
- ✅ Step-by-step status

### 2. **Error Handling**
- ✅ Verifies all scripts exist before starting
- ✅ Captures exit codes
- ✅ Shows errors and warnings
- ✅ Asks to continue if a step fails

### 3. **Comprehensive Reporting**
- ✅ Real-time console output
- ✅ Final summary with statistics
- ✅ Detailed report file: `pipeline-execution-report.txt`
- ✅ Individual reports from each Python script

### 4. **Smart Execution**
- ✅ Dynamic script directory detection
- ✅ UTF-8 encoding support
- ✅ Proper process handling
- ✅ Clean temporary files

---

## 📈 Example Output

### Console Output

```
================================================================================
       HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER PIPELINE
================================================================================

Start Time:        2026-02-10 13:45:00
Working Directory: H:\Repo\Hugo\davoodya
Total Steps:       7

[INFO] Verifying Python scripts...
  [OK] convert_images.py
  [OK] title-adder.py
  [OK] altimage-adder.py
  [OK] images-renamer.py
  [OK] image-article-renamer.py
  [OK] toc-remover.py
  [OK] obsidian-property-remover-enhanced.py

[OK] All scripts found. Ready to execute.

Press any key to start pipeline execution...

================================================================================
STEP 1 of 7: Import New Articles Images
================================================================================
Description: Import images from Obsidian Vault to Hugo static/images
Script:      convert_images.py

[INFO] Starting execution...

--------------------------------------------------------------------------------
Found 150 images in Obsidian Vault
Copied 45 new images
Skipped 105 existing images
--------------------------------------------------------------------------------

[OK] Completed successfully in 2.3s

================================================================================
STEP 2 of 7: Add Title for New Articles
================================================================================
Description: Add Hugo front matter title based on filename
Script:      title-adder.py
Note:        Required for next steps (image renaming)

[INFO] Starting execution...

--------------------------------------------------------------------------------
Files scanned: 50
Titles added: 12
Titles already existed: 38
--------------------------------------------------------------------------------

[OK] Completed successfully in 1.5s

... (Steps 3-7 continue) ...

================================================================================
                          EXECUTION SUMMARY
================================================================================

Pipeline Execution Completed

Duration:     12.8 seconds
Total Steps:  7
Completed:    7
Success Rate: 100%

--------------------------------------------------------------------------------

STEP RESULTS:

  [OK] Step 1: Import New Articles Images (2.3s)
  [OK] Step 2: Add Title for New Articles (1.5s)
  [OK] Step 3: Add ALT for Images (1.8s)
  [OK] Step 4: Rename Images in /static/images (2.1s)
  [OK] Step 5: Update Image References in Articles (1.9s)
  [OK] Step 6: Remove Obsidian TOC (1.2s)
  [OK] Step 7: Add Enhanced Hugo Front Matter (2.0s)

--------------------------------------------------------------------------------

DETAILED REPORT:

  H:\Repo\Hugo\davoodya\pipeline-execution-report.txt

All Steps Completed Successfully!
All images imported and properties fixed.
```

---

## 📄 Report File Structure

### `pipeline-execution-report.txt`

```
================================================================================
              HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER REPORT
================================================================================

Execution Summary
--------------------------------------------------------------------------------
Start Time:           2026-02-10 13:45:00
End Time:             2026-02-10 13:45:13
Total Duration:       12.8 seconds
Total Steps:          7
Completed Steps:      7
Failed Steps:         0
Skipped Steps:        0
Success Rate:         100%

================================================================================
                          PIPELINE STEPS DETAILS
================================================================================

Step 1: Import New Articles Images
--------------------------------------------------------------------------------
Script:         convert_images.py
Status:         [OK] Success
Duration:       2.3s
Exit Code:      0

... (All steps) ...

================================================================================
                            STEP-BY-STEP SUMMARY
================================================================================

1. Import New Articles Images
   - Source: Obsidian Vault Attachment folder
   - Destination: static/images/[category]/
   - Process: Copy new images only (skips existing)

... (Detailed description of each step) ...

================================================================================
                             INDIVIDUAL REPORTS
================================================================================

Step 1: image_migration_report.txt - Available
Step 2: title_adder_report.txt - Available
Step 3: altimage_adder_report.txt - Available
Step 4: images_renamer_report.txt - Available
Step 5: image_article_renamer_report.txt - Available
Step 6: toc_remover_report.txt - Available
Step 7: obsidian_property_remover_enhanced_report.txt - Available

================================================================================
                                  NOTES
================================================================================

- All scripts use tracking files to avoid re-processing files
- Only new/modified files are processed in subsequent runs
- Each script generates its own detailed report
- Check individual report files for specific details
```

---

## ⚠️ Important Notes

### 1. Step 2 is CRITICAL
**Step 2 (title-adder.py) MUST succeed** for the following steps to work correctly:
- Step 3 (ALT attributes) needs the title
- Step 4 (Image renaming) uses the title
- Step 5 (Reference updates) depends on Step 4

### 2. Script Execution Order
**DO NOT change the order** of scripts. They depend on each other:
```
1 → 2 → 3 → 4 → 5 → 6 → 7
    ↓   ↓   ↓   ↓
  Required for these steps
```

### 3. Re-running the Pipeline
You can safely re-run the pipeline:
- Scripts use **tracking files** to skip already processed files
- Only **new or modified** files will be processed
- No duplicate work or conflicts

### 4. Tracking Files
The pipeline uses these tracking files:
- `processed_images.json` - Imported images
- `processed_articles.json` - Processed articles
- `images_rename_mapping.json` - Image name mappings
- `toc_removal_tracking.json` - TOC removal tracking
- `property-delete-tracking-enhanced.json` - Front matter tracking

**Don't delete these files** unless you want to re-process everything!

---

## 🔍 Troubleshooting

### Issue: "Script not found"
**Solution**: Make sure all 7 Python scripts are in the same directory as the PowerShell script.

### Issue: "Python not found"
**Solution**: Install Python and add it to PATH, or use full path to python.exe.

### Issue: Step 2 fails
**Solution**: 
- Check that articles have valid filenames
- Check `title_adder.log` for details
- This is a critical step - fix it before continuing

### Issue: Images not renamed
**Solution**: 
- Make sure Step 2 (Add Titles) completed successfully
- Check `images_renamer_report.txt` for details

### Issue: Script hangs
**Solution**: 
- Check if any Python script is waiting for input
- Kill the process and check individual script logs

---

## 🎯 Use Cases

### Use Case 1: First-Time Import
```powershell
.\image-property-fixer.ps1
```
- All 7 steps will process all files
- Takes longer (processes everything)

### Use Case 2: Adding New Articles
```powershell
.\image-property-fixer.ps1
```
- Only new articles/images are processed
- Existing items are skipped (fast)

### Use Case 3: Fixing Properties
```powershell
.\image-property-fixer.ps1
```
- Re-processes files that need fixing
- Tracking files ensure no duplication

---

## 📊 Statistics Example

After a full run, you might see:

```
EXECUTION SUMMARY
-----------------
Duration:     25.6 seconds
Total Steps:  7
Completed:    7
Failed:       0
Success Rate: 100%

Files Processed:
- Images imported: 45
- Titles added: 12
- ALT attributes added: 78
- Images renamed: 45
- References updated: 134
- TOCs removed: 23
- Front matter added: 18
```

---

## 🆚 vs. Original Script

| Feature | Original | image-property-fixer.ps1 |
|---------|----------|-------------------------|
| Error Handling | Basic | Comprehensive |
| Output | Plain text | Color-coded |
| Reporting | Minimal | Detailed report file |
| Script Verification | None | Pre-checks all scripts |
| Exit Code Handling | Weak | Proper process handling |
| Continue on Failure | No | Asks user |
| Visual Design | Plain | Boxed titles, separators |
| UTF-8 Support | Partial | Full support |
| Individual Reports | No list | Lists all report files |

---

## 📌 Best Practices

1. **Before Running**:
   - ✅ Backup your content folder
   - ✅ Make sure all Python scripts are present
   - ✅ Verify Python is installed

2. **During Execution**:
   - ✅ Watch for errors/warnings
   - ✅ Don't close the window
   - ✅ If Step 2 fails, fix it before continuing

3. **After Running**:
   - ✅ Check the pipeline report
   - ✅ Review individual script reports
   - ✅ Test Hugo site: `hugo server`
   - ✅ Commit changes to Git

---

## 🚀 Quick Reference

```powershell
# Run the pipeline
.\image-property-fixer.ps1

# Location of reports
.\pipeline-execution-report.txt          # Main report
.\image_migration_report.txt             # Step 1 report
.\title_adder_report.txt                 # Step 2 report
.\altimage_adder_report.txt              # Step 3 report
.\images_renamer_report.txt              # Step 4 report
.\image_article_renamer_report.txt       # Step 5 report
.\toc_remover_report.txt                 # Step 6 report
.\obsidian_property_remover_enhanced_report.txt  # Step 7 report

# Tracking files (don't delete!)
.\processed_images.json
.\processed_articles.json
.\images_rename_mapping.json
.\toc_removal_tracking.json
.\property-delete-tracking-enhanced.json
```

---

## ✅ Checklist

Before running:
- [ ] All 7 Python scripts are present
- [ ] Python is installed and in PATH
- [ ] Backed up content folder
- [ ] Obsidian Vault path is configured

After running:
- [ ] All steps completed successfully
- [ ] Checked pipeline-execution-report.txt
- [ ] Reviewed any errors/warnings
- [ ] Tested Hugo site
- [ ] Images display correctly
- [ ] Front matter is complete

---

**Version**: 2.0 (Fixed & Enhanced)  
**Status**: ✅ Ready for Production  
**Last Updated**: 2026-02-10
