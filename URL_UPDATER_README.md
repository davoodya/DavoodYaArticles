# URL Canonical Updater - Quick Guide

## 🚀 Quick Start

### 1. Run the Script
```bash
python url-canonical-updater.py
```

### 2. Enter Path
- **To process all content**: Just press Enter
- **For specific path**: Type the path

Example:
```
content/cyber-security
```

### 3. Confirm
When asked "Do you want to continue?" type: `y`

---

## 📝 What Does It Do?

This script finds all URLs in front matter and adds `/knowledge/` to them:

**Before:**
```markdown
url = "https://davoodya.ir/cyber-security/article/"
canonical = "https://davoodya.ir/cyber-security/article/"
```

**After:**
```markdown
url = "https://davoodya.ir/knowledge/cyber-security/article/"
canonical = "https://davoodya.ir/knowledge/cyber-security/article/"
```

---

## ✅ Features

- ✅ Supports TOML (`---`) and YAML (`+++`)
- ✅ Supports different formats: `url = "..."` and `url: "..."`
- ✅ Handles spaces in paths
- ✅ Processes subdirectories recursively
- ✅ Complete reporting and detailed logging

---

## ⚠️ Important Notes

### 1. Backup Before Running!
```bash
git add .
git commit -m "Before URL update"
```

### 2. Test on a Small Folder First
For example:
```
content/cyber-security/SANS-401
```

### 3. Check Results After Running
- Log file: `url_canonical_updater_YYYYMMDD_HHMMSS.log`
- Report file: `url_canonical_updater_report_YYYYMMDD_HHMMSS.txt`

---

## 📊 Outputs

After running, two files are created:

1. **Log File**: All processing details
2. **Report File**: Statistics summary and list of processed files

---

## 🔍 Complete Example

```bash
# Run the script
python url-canonical-updater.py

# Answer the questions:
# Directory path: [Press Enter for content/]
# Continue?: y

# Result:
# ✓ Found 45 files
# ✓ Processed 42 files
# ✓ Skipped 3 files (didn't have old URLs)
# ✓ Made 84 replacements
```

---

## 📖 Complete Guide

For more details, read:
```
docs/URL_CANONICAL_UPDATER_GUIDE.md
```

---

## 🧪 Testing

To test the script:
```bash
python test-url-updater.py
```

This processes test files in `test/test-url-updater/`.

---

## ❓ FAQ

### What if I run it by mistake?
Restore from Git:
```bash
git checkout -- content/
```

### Can I run it again?
Yes! If you run it again, files that were already updated will be skipped.

### Why are some files skipped?
Possible reasons:
- No front matter
- Don't have old URLs
- Already updated

---

## 📌 Checklist

Before running:
- [ ] Made a backup?
- [ ] Tested on a few files?
- [ ] Checked the path?

After running:
- [ ] Reviewed the log file?
- [ ] Read the report?
- [ ] Manually checked some files?
- [ ] Built Hugo?

---

**Created**: 2026-02-10  
**Version**: 1.0.0

For support, refer to the documentation.
