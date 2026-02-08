# راهنمای استفاده از سیستم Rename تصاویر

## نمای کلی

این سیستم شامل دو اسکریپت مجزا است که به ترتیب باید اجرا شوند:

### 1. `images-renamer.py` - تغییر نام فایل‌های فیزیکی
- **وظیفه**: فقط تصاویر اصلی در `static/images/category-name/` را تغییر نام می‌دهد
- **کار نمی‌کند**: روی فایل‌های markdown تغییری ایجاد نمی‌کند
- **خروجی**: 
  - `images_rename_mapping.json` - نقشه تغییر نام‌ها
  - `processed_images.json` - لیست تصاویر پردازش شده
  - `images_renamer.log` - لاگ کامل
  - `images_renamer_report.txt` - گزارش خلاصه

### 2. `image-article-renamer.py` - به‌روزرسانی مراجع در markdown
- **وظیفه**: فقط مراجع تصاویر در فایل‌های markdown را به‌روز می‌کند
- **کار نمی‌کند**: روی تصاویر فیزیکی تغییری ایجاد نمی‌کند
- **ورودی**: از `images_rename_mapping.json` استفاده می‌کند
- **خروجی**:
  - `processed_articles.json` - لیست مقالات پردازش شده
  - `image_article_renamer.log` - لاگ کامل
  - `image_article_renamer_report.txt` - گزارش خلاصه

---

## ترتیب اجرا

### مرحله 1: تغییر نام فایل‌های فیزیکی
```bash
python images-renamer.py
```

این اسکریپت:
1. تمام فایل‌های `.md` را اسکن می‌کند
2. تصاویر و alt text آنها را پیدا می‌کند
3. نقشه تغییر نام را ایجاد می‌کند
4. **فقط** فایل‌های فیزیکی در `static/images/` را تغییر نام می‌دهد
5. تصاویری که قبلاً پردازش شده‌اند را دوباره پردازش نمی‌کند

**مثال:**
```
Before: static/images/tools/Pastedimage20250703164923.png
After:  static/images/tools/MSFConsoleCommands-1.png
```

### مرحله 2: به‌روزرسانی مراجع markdown
```bash
python image-article-renamer.py
```

این اسکریپت:
1. فایل `images_rename_mapping.json` را می‌خواند
2. فایل‌های markdown را اسکن می‌کند
3. **فقط** مراجع تصاویر را در markdown به‌روز می‌کند
4. وجود فایل‌های جدید در `static/images/` را تأیید می‌کند
5. مقالاتی که قبلاً پردازش شده‌اند را دوباره پردازش نمی‌کند

**مثال:**
```markdown
Before: ![MSFConsole Commands-1](/images/tools/Pastedimage20250703164923.png)
After:  ![MSFConsole Commands-1](/images/tools/MSFConsoleCommands-1.png)
```

---

## ویژگی‌های کلیدی

### 1. جلوگیری از پردازش مجدد
- **تصاویر**: فایل `processed_images.json` تصاویری که قبلاً rename شده‌اند را ردیابی می‌کند
- **مقالات**: فایل `processed_articles.json` مقالاتی که قبلاً به‌روز شده‌اند را ردیابی می‌کند
- **نتیجه**: فقط تصاویر و مقالات جدید پردازش می‌شوند

### 2. امنیت داده‌ها
- اگر فایل مقصد از قبل وجود داشته باشد، تغییر نام انجام نمی‌شود
- قبل از به‌روزرسانی markdown، وجود فایل جدید تأیید می‌شود
- تمام عملیات در لاگ ثبت می‌شوند

### 3. سازگاری
- هر دو اسکریپت از یک `images_rename_mapping.json` استفاده می‌کنند
- mapping ها merge می‌شوند، نه replace
- از نام‌گذاری یکسان برای تبدیل alt text استفاده می‌کنند

---

## اضافه کردن مقالات و تصاویر جدید

### سناریو: مقاله جدید با تصاویر جدید

1. **مقاله جدید را اضافه کنید** با نام‌های پیشفرض تصاویر:
```markdown
+++
title = "My New Article"
+++

![My Image-1](/images/tools/Pastedimage123.png)
![My Image-2](/images/tools/Pastedimage456.png)
```

2. **تصاویر را در `static/images/tools/` قرار دهید**:
```
static/images/tools/Pastedimage123.png
static/images/tools/Pastedimage456.png
```

3. **اجرای اسکریپت اول** (تغییر نام فیزیکی):
```bash
python images-renamer.py
```

خروجی:
```
[File] tools/My New Article.md
  Found 2 image(s)
    + Will rename: Pastedimage123.png
      -> MyImage-1.png
    + Will rename: Pastedimage456.png
      -> MyImage-2.png

[Category] tools
  + Renamed: Pastedimage123.png
    -> MyImage-1.png
  + Renamed: Pastedimage456.png
    -> MyImage-2.png

Physical files renamed: 2
```

4. **اجرای اسکریپت دوم** (به‌روزرسانی markdown):
```bash
python image-article-renamer.py
```

خروجی:
```
[File] tools/My New Article.md
  Found 2 image(s)
    + Updated: Pastedimage123.png
      -> MyImage-1.png
    + Updated: Pastedimage456.png
      -> MyImage-2.png
  [Saved] 2 image(s) updated

Files modified: 1
Images updated: 2
```

5. **نتیجه نهایی**:
```markdown
![My Image-1](/images/tools/MyImage-1.png)
![My Image-2](/images/tools/MyImage-2.png)
```

```
static/images/tools/MyImage-1.png
static/images/tools/MyImage-2.png
```

---

## اجرای مجدد روی مقالات موجود

اگر اسکریپت‌ها را دوباره اجرا کنید:

```bash
python images-renamer.py
```
خروجی:
```
Files scanned: 10
Images found: 50
Images skipped (already processed): 50
Physical files renamed: 0

[INFO] No new images needed renaming
```

```bash
python image-article-renamer.py
```
خروجی:
```
Files scanned: 10
Files skipped (already processed): 10
Files modified: 0

[INFO] No new image references needed updating
```

---

## حذف tracking برای اجرای مجدد

اگر می‌خواهید همه چیز را دوباره پردازش کنید:

```bash
# حذف فایل‌های tracking
del processed_images.json
del processed_articles.json

# اجرای مجدد اسکریپت‌ها
python images-renamer.py
python image-article-renamer.py
```

**هشدار**: این کار تمام تصاویر و مقالات را دوباره پردازش می‌کند!

---

## بررسی mapping ها

### مشاهده mapping های ایجاد شده:
```bash
type images_rename_mapping.json
```

خروجی نمونه:
```json
{
  "Pastedimage20250703164923.png": {
    "new_name": "MSFConsoleCommands-1.png",
    "category": "tools",
    "alt": "MSFConsole Commands-1"
  },
  "Pastedimage20240620171105.png": {
    "new_name": "SANS-401-NetworkingandProtocols(401.1)-1.png",
    "category": "cyber-security",
    "alt": "SANS-401-Networking and Protocols (401.1)-1"
  }
}
```

### مشاهده تصاویر پردازش شده:
```bash
type processed_images.json
```

### مشاهده مقالات پردازش شده:
```bash
type processed_articles.json
```

---

## عیب‌یابی

### خطا: "Rename mapping file not found"
```
X Rename mapping file not found: images_rename_mapping.json
  Please run images-renamer.py first to rename physical files.
```
**راه‌حل**: ابتدا `images-renamer.py` را اجرا کنید.

---

### خطا: "New file doesn't exist"
```
Warning: New file doesn't exist: MyImage-1.png
         Expected at: static/images/tools/MyImage-1.png
         Run images-renamer.py first!
```
**راه‌حل**: فایل فیزیکی هنوز rename نشده. `images-renamer.py` را اجرا کنید.

---

### خطا: "Category mismatch"
```
Warning: Category mismatch for Pastedimage123.png
         Found: seo, Mapped: tools
```
**راه‌حل**: یک تصویر با همان نام در چند دسته وجود دارد. نام تصویر را manually تغییر دهید.

---

## ساختار فایل‌ها

```
davoodya/
├── content/
│   ├── tools/
│   │   └── MSFConsole Commands.md    # markdown files
│   ├── cyber-security/
│   └── ...
├── static/images/
│   ├── tools/
│   │   └── MSFConsoleCommands-1.png  # renamed physical files
│   ├── cyber-security/
│   └── ...
├── images-renamer.py                  # Script 1: Rename physical files
├── image-article-renamer.py          # Script 2: Update markdown refs
├── images_rename_mapping.json        # Shared mapping file
├── processed_images.json             # Tracking: processed images
├── processed_articles.json           # Tracking: processed articles
├── images_renamer.log                # Log for script 1
├── image_article_renamer.log         # Log for script 2
└── IMAGES_RENAMER_GUIDE.md           # This file
```

---

## نکات مهم

1. **همیشه به ترتیب اجرا کنید**:
   - اول: `images-renamer.py` (فایل‌های فیزیکی)
   - دوم: `image-article-renamer.py` (مراجع markdown)

2. **قبل از اجرا backup بگیرید**:
   - از فولدر `static/images/` و `content/` backup تهیه کنید

3. **لاگ‌ها را بررسی کنید**:
   - `images_renamer.log`
   - `image_article_renamer.log`

4. **mapping ها حفظ می‌شوند**:
   - `images_rename_mapping.json` برای مراجع آینده نگهداری می‌شود
   - mapping های جدید به موارد قبلی اضافه می‌شوند

5. **فقط فایل‌های جدید پردازش می‌شوند**:
   - فایل‌های tracking از پردازش مجدد جلوگیری می‌کنند
   - برای اجرای کامل، فایل‌های tracking را حذف کنید

---

## پشتیبانی

برای مشکلات، لاگ‌ها را بررسی کنید:
- `images_renamer.log`
- `image_article_renamer.log`
- `images_renamer_report.txt`
- `image_article_renamer_report.txt`

---

**نویسنده**: Davood Yahya  
**تاریخ**: 2026-02-08  
**نسخه**: 2.0 - Separated physical rename and markdown update
