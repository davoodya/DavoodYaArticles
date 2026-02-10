# URL Segment Replacer - Quick Start

## 🚀 Quick Usage

```bash
python url-segment-replacer.py
```

Then answer 4 simple questions:

1. **Directory**: Press Enter for `content/`, or type custom path
2. **URL Segment**: Type segment name (e.g., `knowledge`, `blog`, `docs`)
3. **Mode**: Choose `a` (all), `f` (front), or `b` (body)
4. **Confirm**: Type `y` to start

---

## 📝 What It Does

Adds a custom URL segment to all URLs in your Hugo articles:

```
From: https://davoodya.ir/category/article/
To:   https://davoodya.ir/YOUR-SEGMENT/category/article/
```

---

## 🎯 Three Modes

### Mode A: ALL
- Replaces URLs **everywhere** (front matter + body)
- Most comprehensive

### Mode F: FRONT
- Replaces URLs **only in front matter**
- Body remains unchanged

### Mode B: BODY
- Replaces URLs **only in body**
- Front matter remains unchanged

---

## 📊 Example

**Original File:**
```markdown
---
url = "https://davoodya.ir/cyber-security/article/"
canonical = "https://davoodya.ir/cyber-security/article/"
---

Check out: https://davoodya.ir/network/basics/
Also: https://davoodya.ir/tools/guide/
```

### Result with ALL mode + "knowledge" segment:
```markdown
---
url = "https://davoodya.ir/knowledge/cyber-security/article/"
canonical = "https://davoodya.ir/knowledge/cyber-security/article/"
---

Check out: https://davoodya.ir/knowledge/network/basics/
Also: https://davoodya.ir/knowledge/tools/guide/
```
✅ 4 replacements (2 front matter + 2 body)

### Result with FRONT mode + "knowledge" segment:
```markdown
---
url = "https://davoodya.ir/knowledge/cyber-security/article/"
canonical = "https://davoodya.ir/knowledge/cyber-security/article/"
---

Check out: https://davoodya.ir/network/basics/  ← Unchanged
Also: https://davoodya.ir/tools/guide/  ← Unchanged
```
✅ 2 replacements (only front matter)

### Result with BODY mode + "knowledge" segment:
```markdown
---
url = "https://davoodya.ir/cyber-security/article/"  ← Unchanged
canonical = "https://davoodya.ir/cyber-security/article/"  ← Unchanged
---

Check out: https://davoodya.ir/knowledge/network/basics/
Also: https://davoodya.ir/knowledge/tools/guide/
```
✅ 2 replacements (only body)

---

## ⚠️ Important

### 1. Backup First!
```bash
git add .
git commit -m "Before URL segment replacement"
```

### 2. Test on Small Directory
```bash
# Test on one folder first:
python url-segment-replacer.py
# Enter: content/cyber-security/SANS-401
```

### 3. URL Segment Rules
✅ Good: `knowledge`, `blog`, `docs`
❌ Bad: `my segment`, `my/segment`, `` (empty)

---

## 📈 Complete Example

```
$ python url-segment-replacer.py

Enter directory path: content/
Enter URL segment: knowledge
Select mode (a/f/b): a
Do you want to continue? (y/n): y

✓ Found 45 files
✓ Processed 42 files
✓ Skipped 3 files (no old URLs)
✓ Made 127 replacements
  - Front matter: 84
  - Body: 43

✓ Report saved: url_segment_replacer_report_20260210_125235.txt
✓ Log saved: url_segment_replacer_20260210_125235.log
```

---

## 🧪 Testing

```bash
python test-segment-simple.py a    # Test ALL mode
python test-segment-simple.py f    # Test FRONT mode
python test-segment-simple.py b    # Test BODY mode
```

---

## 📖 Full Documentation

For detailed guide: `docs/URL_SEGMENT_REPLACER_GUIDE.md`

---

## 🆚 vs url-canonical-updater.py

| Feature | url-canonical-updater.py | url-segment-replacer.py |
|---------|-------------------------|------------------------|
| URL Segment | Fixed: `knowledge` | Custom input |
| Replace Location | Front matter only | ALL / FRONT / BODY |
| Flexibility | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Use Case | Specific update | General purpose |

---

## 📌 Quick Reference Card

```
┌─────────────────────────────────────────┐
│  URL SEGMENT REPLACER QUICK GUIDE      │
├─────────────────────────────────────────┤
│  Run: python url-segment-replacer.py   │
│                                         │
│  Inputs:                                │
│  1. Directory    (default: content/)   │
│  2. URL Segment  (e.g., knowledge)     │
│  3. Mode         (a/f/b)               │
│  4. Confirm      (y/n)                 │
│                                         │
│  Modes:                                 │
│  • a = ALL   (entire file)             │
│  • f = FRONT (front matter only)       │
│  • b = BODY  (body only)               │
│                                         │
│  ⚠️  Always backup before running!     │
└─────────────────────────────────────────┘
```

---

**Created**: 2026-02-10  
**Version**: 1.0.0  
**Status**: ✅ Tested & Ready
