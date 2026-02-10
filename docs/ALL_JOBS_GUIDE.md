# All Jobs Pipeline - Complete Guide

## 📋 Overview

**`all-jobs.py`** is a Python automation script that orchestrates 7 Python scripts in sequence to import articles from Obsidian to Hugo and fix all image properties.

This is the **Python equivalent** of `image-property-fixer.ps1` PowerShell script.

**Version**: 2.0 (Python Edition)  
**Date**: 2026-02-10  
**Language**: Python 3.6+

---

## 🎯 What It Does

Exactly the same as `image-property-fixer.ps1`:

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

```bash
python all-jobs.py
```

### That's it!
The script will:
- ✅ Show beautiful colored output
- ✅ Verify all Python scripts exist
- ✅ Execute them in the correct order
- ✅ Show detailed progress
- ✅ Generate a comprehensive report

---

## 🎨 Features

### 1. **Beautiful Colored Output**

```
================================================================================
       HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER PIPELINE
================================================================================

[INFO] Verifying Python scripts...
  [OK] convert_images.py
  [OK] title-adder.py
  [OK] altimage-adder.py
  ...

[OK] All scripts found. Ready to execute.

Press Enter to start pipeline execution...

================================================================================
STEP 1 of 7: Import New Articles Images
================================================================================
Description: Import images from Obsidian Vault to Hugo static/images
Script:      convert_images.py

[INFO] Starting execution...

--------------------------------------------------------------------------------
Found 150 images in Obsidian Vault
Copied 45 new images
--------------------------------------------------------------------------------

[OK] Completed successfully in 2.3s
```

**Color Scheme**:
- 🟢 **Green**: Success messages
- 🔴 **Red**: Error messages
- 🟡 **Yellow**: Warnings
- 🔵 **Cyan**: Info messages
- ⚪ **White**: Normal text
- ⚫ **Gray**: Subtle text

---

### 2. **ANSI Colors (Cross-platform)**

```python
class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
```

Works on:
- ✅ Windows 10+ (with ANSI support)
- ✅ Linux
- ✅ macOS
- ✅ VS Code terminal
- ✅ PyCharm terminal

---

### 3. **Comprehensive Error Handling**

```python
try:
    result_proc = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    exit_code = result_proc.returncode
    
    if exit_code == 0:
        print_status_message("Completed successfully", "success")
    else:
        print_status_message(f"Failed with exit code: {exit_code}", "error")
        
except Exception as e:
    print_status_message(f"Exception: {str(e)}", "error")
```

**Handles**:
- ✅ Script not found
- ✅ Non-zero exit codes
- ✅ Exceptions
- ✅ Keyboard interrupt (Ctrl+C)
- ✅ UTF-8 encoding issues

---

### 4. **Detailed Progress Tracking**

```python
class PipelineStats:
    def __init__(self):
        self.start_time = datetime.now()
        self.total_steps = 7
        self.completed_steps = 0
        self.failed_steps = 0
        self.skipped_steps = 0
        self.step_results = []
```

Tracks:
- ⏱️ Start/end time
- 📊 Steps completed/failed/skipped
- 📈 Duration per step
- ✅ Success rate

---

### 5. **Comprehensive Report Generation**

Generates `pipeline-execution-report.txt` with:

```
================================================================================
              HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER REPORT
================================================================================

Execution Summary
--------------------------------------------------------------------------------
Start Time:           2026-02-10 14:15:00
End Time:             2026-02-10 14:15:13
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

... (all 7 steps)

================================================================================
                            STEP-BY-STEP SUMMARY
================================================================================

1. Import New Articles Images
   - Source: Obsidian Vault Attachment folder
   - Destination: static/images/[category]/
   - Process: Copy new images only (skips existing)

... (detailed descriptions)

================================================================================
                             INDIVIDUAL REPORTS
================================================================================

Step 1: image_migration_report.txt - Available
Step 2: title_adder_report.txt - Available
...

================================================================================
                                  NOTES
================================================================================

- All scripts use tracking files to avoid re-processing files
- Only new/modified files are processed in subsequent runs
...
```

---

## 📊 Example Output

### Full Execution Flow

```
================================================================================
       HUGO ARTICLE IMPORT & IMAGE PROPERTY FIXER PIPELINE
================================================================================

Start Time:        2026-02-10 14:15:00
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

Press Enter to start pipeline execution...
(or Ctrl+C to cancel)

================================================================================
STEP 1 of 7: Import New Articles Images
================================================================================
Description: Import images from Obsidian Vault to Hugo static/images
Script:      convert_images.py

[INFO] Starting execution...

--------------------------------------------------------------------------------
Found 150 images in Obsidian Vault
Copied 45 new images to static/images
Skipped 105 existing images
Total processing time: 2.1s
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
Excluded files (all-articles): 5
Total processing time: 1.3s
--------------------------------------------------------------------------------

[OK] Completed successfully in 1.5s

... (Steps 3-7 continue similarly)

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

================================================================================

Press Enter to exit...
```

---

## 🆚 Python vs PowerShell

| Feature | image-property-fixer.ps1 | all-jobs.py |
|---------|-------------------------|-------------|
| Language | PowerShell | Python |
| Cross-platform | Windows only | Windows/Linux/macOS |
| Colors | PowerShell colors | ANSI colors |
| Subprocess | Start-Process | subprocess.run |
| Exit code | $LASTEXITCODE | returncode |
| Error handling | Try/Catch | try/except |
| File operations | PowerShell cmdlets | pathlib |
| Unicode | UTF-8 BOM | UTF-8 |
| Execution | .ps1 | python script.py |

**Both scripts**:
- ✅ Same functionality
- ✅ Same 7-step pipeline
- ✅ Same reports
- ✅ Same error handling
- ✅ Same user experience

---

## 🔧 Requirements

### Python Version
```bash
python --version
# Python 3.6 or higher required
```

### Dependencies
**None!** All built-in modules:
- `os`
- `sys`
- `subprocess`
- `time`
- `pathlib`
- `datetime`
- `typing`

---

## 📝 Pipeline Steps

### Step 1: Import New Articles Images
**Script**: `convert_images.py`

### Step 2: Add Title for New Articles ⚠️
**Script**: `title-adder.py`
- **CRITICAL**: Required for Steps 3, 4, 5

### Step 3: Add ALT for Images
**Script**: `altimage-adder.py`

### Step 4: Rename Images
**Script**: `images-renamer.py`

### Step 5: Update Image References
**Script**: `image-article-renamer.py`

### Step 6: Remove Obsidian TOC
**Script**: `toc-remover.py`

### Step 7: Add Enhanced Hugo Front Matter
**Script**: `obsidian-property-remover-enhanced.py`

(See `IMAGE_PROPERTY_FIXER_GUIDE.md` for detailed descriptions)

---

## 🎯 Usage

### Basic Usage
```bash
python all-jobs.py
```

### With Python 3 Explicitly
```bash
python3 all-jobs.py
```

### On Unix Systems
```bash
chmod +x all-jobs.py
./all-jobs.py
```

---

## ⚠️ Important Notes

### 1. Step 2 is CRITICAL
Must succeed for Steps 3, 4, 5 to work properly

### 2. Script Order
**DO NOT change the order** - they depend on each other

### 3. Tracking Files
Scripts use these files to avoid re-processing:
- `processed_images.json`
- `processed_articles.json`
- `images_rename_mapping.json`
- `toc_removal_tracking.json`
- `property-delete-tracking-enhanced.json`

### 4. Re-running
You can safely re-run - only new/modified files are processed

---

## 🔍 Troubleshooting

### Issue: Colors don't show on Windows
**Solution**: 
- Use Windows 10+ with ANSI support
- Or use Windows Terminal
- Or run in VS Code terminal

### Issue: "Python not found"
**Solution**: 
```bash
# Install Python 3
# Add to PATH
# Verify:
python --version
```

### Issue: Script hangs
**Solution**: 
- Press Ctrl+C to cancel
- Check if waiting for input
- Run individual scripts to debug

### Issue: Step 2 fails
**Solution**: 
- This is critical - must fix it
- Check `title_adder.log`
- Verify article filenames are valid

---

## 🎨 Code Structure

```python
# Classes
class Colors:              # ANSI color codes
class PipelineStats:       # Statistics tracking

# Helper Functions
clear_screen()             # Clear terminal
print_boxed_title()        # Boxed titles
print_step_header()        # Step headers
print_status_message()     # Colored messages
execute_python_script()    # Execute a script
generate_final_report()    # Generate report
show_final_summary()       # Show summary
verify_all_scripts()       # Verify scripts exist
get_user_confirmation()    # Ask for confirmation
ask_continue_after_failure() # Ask to continue

# Main
main()                     # Main execution
```

---

## 📊 Statistics Example

```python
stats = PipelineStats()

# After execution:
stats.start_time = 2026-02-10 14:15:00
stats.end_time = 2026-02-10 14:15:13
stats.total_steps = 7
stats.completed_steps = 7
stats.failed_steps = 0
stats.skipped_steps = 0
stats.get_duration() = 12.8
stats.get_success_rate() = 100.0
```

---

## 🎯 Use Cases

### Use Case 1: Windows User (No PowerShell Experience)
```bash
python all-jobs.py
```
Easier than PowerShell for Python developers!

### Use Case 2: Linux/macOS User
```bash
python all-jobs.py
```
PowerShell not available? Use Python!

### Use Case 3: Automation/CI/CD
```python
import subprocess

result = subprocess.run(
    ['python', 'all-jobs.py'],
    capture_output=True
)

if result.returncode == 0:
    print("Success!")
```

### Use Case 4: Scheduled Task
```bash
# Cron job (Linux)
0 2 * * * cd /path/to/repo && python all-jobs.py

# Task Scheduler (Windows)
python.exe C:\path\to\all-jobs.py
```

---

## 🔄 Comparison Summary

### When to use `image-property-fixer.ps1`:
- ✅ Windows user
- ✅ Familiar with PowerShell
- ✅ Want native Windows integration

### When to use `all-jobs.py`:
- ✅ Cross-platform (Windows/Linux/macOS)
- ✅ Python developer
- ✅ Need automation/CI/CD
- ✅ No PowerShell available

---

## 📋 Checklist

Before running:
- [ ] Python 3.6+ installed
- [ ] All 7 Python scripts present
- [ ] Backed up content folder
- [ ] Obsidian Vault path configured

After running:
- [ ] Check console output
- [ ] Review `pipeline-execution-report.txt`
- [ ] Check individual script reports
- [ ] Test Hugo site: `hugo server`
- [ ] Verify images display correctly

---

## 🎉 Features Summary

✅ **Identical functionality** to PowerShell version  
✅ **Cross-platform** (Windows/Linux/macOS)  
✅ **Beautiful colored output** with ANSI codes  
✅ **Comprehensive error handling**  
✅ **Detailed progress tracking**  
✅ **Full report generation**  
✅ **No external dependencies**  
✅ **Clean, readable code**  
✅ **Type hints** for better IDE support  
✅ **Docstrings** for all functions  

---

## 🚀 Quick Reference

```bash
# Run the pipeline
python all-jobs.py

# Or with Python 3 explicitly
python3 all-jobs.py

# Make executable on Unix
chmod +x all-jobs.py
./all-jobs.py
```

**Output Files**:
- `pipeline-execution-report.txt` - Main report
- Individual script reports (7 files)
- Tracking JSON files (5 files)

**Execution Time**: ~10-15 seconds for typical run

---

**Version**: 2.0 (Python Edition)  
**Status**: ✅ Ready for Production  
**Last Updated**: 2026-02-10  
**Compatibility**: Python 3.6+
