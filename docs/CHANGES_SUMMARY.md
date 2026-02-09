# خلاصه تغییرات سیستم Rename تصاویر

## تاریخ: 2026-02-08

---

## تغییرات اعمال شده

### 1. جداسازی وظایف اسکریپت‌ها

#### `images-renamer.py` (تغییرات عمده)

**قبل از تغییر:**
- هم تصاویر فیزیکی را rename می‌کرد
- هم مراجع markdown را به‌روز می‌کرد
- تمام فایل‌ها را در هر اجرا دوباره پردازش می‌کرد

**بعد از تغییر:**
- **فقط** تصاویر فیزیکی در `static/images/` را rename می‌کند
- **هیچ تغییری** در فایل‌های markdown ایجاد نمی‌کند
- فقط تصاویر جدید را پردازش می‌کند (tracking با `processed_images.json`)
- mapping ها را در `images_rename_mapping.json` ذخیره می‌کند

**ویژگی‌های جدید:**
```python
# Load/Save processed images
processed_images = {}  # Track already renamed images
load_processed_images()   # بارگذاری لیست تصاویر پردازش شده
save_processed_images()   # ذخیره لیست تصاویر پردازش شده

# Skip already processed images
if image_key in processed_images:
    log_message(f"    > Already processed: {old_filename}")
    stats['images_skipped_already_processed'] += 1
    continue
```

---

#### `image-article-renamer.py` (تغییرات عمده)

**قبل از تغییر:**
- از alt text برای تولید نام جدید استفاده می‌کرد
- وابسته به اجرای همزمان با `images-renamer.py` بود
- تمام مقالات را در هر اجرا دوباره پردازش می‌کرد

**بعد از تغییر:**
- **فقط** مراجع تصاویر در markdown را به‌روز می‌کند
- **هیچ تغییری** در فایل‌های فیزیکی ایجاد نمی‌کند
- از `images_rename_mapping.json` برای دریافت نام‌های جدید استفاده می‌کند
- فقط مقالات جدید را پردازش می‌کند (tracking با `processed_articles.json`)
- وجود فایل‌های renamed را در `static/images/` تأیید می‌کند

**ویژگی‌های جدید:**
```python
# Load rename mapping from JSON
rename_mapping = {}
load_rename_mapping()  # بارگذاری mapping از فایل JSON

# Track processed articles
processed_articles = {}
load_processed_articles()
save_processed_articles()

# Check mapping instead of generating new name
if old_filename not in rename_mapping:
    log_message(f"    > No mapping for: {old_filename}")
    continue

# Verify physical file exists
new_file_path = os.path.join(STATIC_IMAGES_BASE, img_category, new_filename)
if not os.path.exists(new_file_path):
    log_message(f"    Warning: New file doesn't exist: {new_filename}")
    log_message(f"             Run images-renamer.py first!")
    continue
```

---

### 2. سیستم Tracking برای جلوگیری از پردازش مجدد

#### `processed_images.json` (جدید)
```json
{
  "tools/Pastedimage123.png": {
    "old_name": "Pastedimage123.png",
    "new_name": "MSFConsoleCommands-1.png",
    "category": "tools",
    "status": "renamed"
  },
  "tools/MSFConsoleCommands-2.png": {
    "old_name": "MSFConsoleCommands-2.png",
    "new_name": "MSFConsoleCommands-2.png",
    "category": "tools",
    "status": "already_correct"
  }
}
```

#### `processed_articles.json` (جدید)
```json
{
  "tools/MSFConsole Commands.md": {
    "image_count": 43,
    "updated_count": 43,
    "last_processed": "2026-02-08 14:30:00"
  },
  "seo/0-SEO-Theories/E12- Woorank(Check Website SEO).md": {
    "image_count": 5,
    "updated_count": 5,
    "last_processed": "2026-02-08 14:30:15"
  }
}
```

---

### 3. Workflow جدید

#### قبل (Workflow قدیمی):
```
1. اجرای images-renamer.py
   ├── Rename فایل‌های فیزیکی
   └── به‌روزرسانی markdown ها
   
نتیجه: همه چیز با یک اسکریپت
مشکل: پردازش مجدد در هر اجرا
```

#### بعد (Workflow جدید):
```
1. اجرای images-renamer.py
   ├── اسکن markdown ها
   ├── تولید mapping
   ├── Rename فقط فایل‌های فیزیکی
   ├── Track تصاویر پردازش شده
   └── ذخیره mapping در JSON

2. اجرای image-article-renamer.py
   ├── خواندن mapping از JSON
   ├── به‌روزرسانی فقط markdown ها
   ├── تأیید وجود فایل‌های renamed
   └── Track مقالات پردازش شده

نتیجه: جداسازی کامل وظایف
مزایا:
  ✓ فقط فایل‌های جدید پردازش می‌شوند
  ✓ امنیت بیشتر (تأیید وجود فایل‌ها)
  ✓ قابلیت اجرای مستقل
```

---

### 4. مقایسه رفتار

#### سناریو: اضافه کردن مقاله جدید

**قبل:**
```bash
# اجرای images-renamer.py
Processing 10 files (including old ones)
Renamed 50 images (including duplicates)
Updated 50 markdown references (including duplicates)
```

**بعد:**
```bash
# اجرای images-renamer.py
Files scanned: 10
Images found: 50
Images skipped (already processed): 48  # فایل‌های قدیمی
Physical files renamed: 2  # فقط فایل‌های جدید

# اجرای image-article-renamer.py
Files scanned: 10
Files skipped (already processed): 9  # مقالات قدیمی
Files modified: 1  # فقط مقاله جدید
Images updated: 2  # فقط تصاویر جدید
```

---

### 5. فایل‌های خروجی

#### قبل:
```
images_rename_mapping.json  # mapping ها
images_renamer.log          # لاگ
images_renamer_report.txt   # گزارش
```

#### بعد:
```
# اسکریپت اول (images-renamer.py)
images_rename_mapping.json     # mapping های shared
processed_images.json          # NEW: tracking تصاویر
images_renamer.log            # لاگ اسکریپت اول
images_renamer_report.txt     # گزارش اسکریپت اول

# اسکریپت دوم (image-article-renamer.py)
processed_articles.json              # NEW: tracking مقالات
image_article_renamer.log           # لاگ اسکریپت دوم
image_article_renamer_report.txt    # گزارش اسکریپت دوم
```

---

### 6. تغییرات در آمار (Statistics)

#### `images-renamer.py`:
```python
# قبل
stats = {
    'files_scanned': 0,
    'files_modified': 0,        # حذف شد
    'images_found': 0,
    'images_renamed': 0,        # حذف شد
    'physical_files_renamed': 0,
    'errors': 0
}

# بعد
stats = {
    'files_scanned': 0,
    'images_found': 0,
    'images_skipped_already_processed': 0,  # NEW
    'images_skipped_already_correct': 0,    # NEW
    'physical_files_renamed': 0,
    'errors': 0
}
```

#### `image-article-renamer.py`:
```python
# بعد (با tracking)
stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'files_skipped_already_processed': 0,  # NEW
    'images_found': 0,
    'images_updated': 0,
    'images_skipped': 0,
    'errors': 0
}
```

---

## مزایای تغییرات

### 1. **کارایی بهتر** ⚡
- فقط فایل‌های جدید پردازش می‌شوند
- جلوگیری از پردازش مجدد فایل‌های قدیمی
- سرعت بالا در اجراهای بعدی

### 2. **امنیت بیشتر** 🔒
- تأیید وجود فایل‌های renamed قبل از به‌روزرسانی markdown
- جداسازی مراحل (کاهش خطر)
- tracking کامل عملیات

### 3. **قابلیت نگهداری** 🛠️
- کد واضح‌تر و ساده‌تر
- وظایف جدا از هم
- debugging آسان‌تر

### 4. **انعطاف‌پذیری** 🔄
- امکان اجرای مستقل هر اسکریپت
- امکان reset کردن tracking
- سازگاری با workflow های مختلف

### 5. **گزارش‌دهی دقیق‌تر** 📊
- آمار جداگانه برای هر مرحله
- tracking دقیق فایل‌های پردازش شده
- لاگ‌های مجزا

---

## نحوه استفاده (خلاصه)

### برای مقالات و تصاویر جدید:

```bash
# مرحله 1: Rename فایل‌های فیزیکی
python images-renamer.py

# مرحله 2: به‌روزرسانی markdown ها
python image-article-renamer.py
```

### برای حذف tracking و اجرای مجدد:

```bash
# حذف فایل‌های tracking
del processed_images.json
del processed_articles.json

# اجرای مجدد
python images-renamer.py
python image-article-renamer.py
```

---

## فایل‌های تغییر یافته

1. ✅ `images-renamer.py` - بازنویسی کامل
2. ✅ `image-article-renamer.py` - بازنویسی کامل
3. ✅ `IMAGES_RENAMER_GUIDE.md` - راهنمای کامل (جدید)
4. ✅ `CHANGES_SUMMARY.md` - این فایل (جدید)

---

## فایل‌های جدید ایجاد شده

1. `processed_images.json` - tracking تصاویر پردازش شده
2. `processed_articles.json` - tracking مقالات پردازش شده
3. `image_article_renamer.log` - لاگ اسکریپت دوم
4. `image_article_renamer_report.txt` - گزارش اسکریپت دوم

---

## تست و تأیید

### بررسی mapping صحیح:
```bash
# مشاهده mapping های فعلی
type images_rename_mapping.json

# اجرای تست
python images-renamer.py
python image-article-renamer.py

# بررسی لاگ‌ها
type images_renamer.log
type image_article_renamer.log
```

---

## نکات مهم ⚠️

1. **همیشه به ترتیب اجرا کنید**
   - اول: `images-renamer.py`
   - دوم: `image-article-renamer.py`

2. **قبل از اجرا backup بگیرید**
   - `static/images/`
   - `content/`

3. **mapping های قدیمی حفظ می‌شوند**
   - فایل `images_rename_mapping.json` merge می‌شود

4. **برای reset کامل**
   - فایل‌های `processed_*.json` را حذف کنید

---

---

## 📝 به‌روزرسانی: 09 فوریه 2026

### تغییرات جدید اضافه شده:

#### 1. رفع مشکل Layout موبایل ✅
- **مشکل**: در موبایل Sidebar ابتدا و محتوا بعد نمایش داده می‌شد
- **راه‌حل**: استفاده از CSS Flexbox Order
- **نتیجه**: در موبایل محتوا ابتدا و Sidebar بعد نمایش داده می‌شود
- **فایل تغییر یافته**: `assets/css/main.css`
- **مستندات**: `docs/MOBILE_LAYOUT_FIX.md`

#### 2. اضافه شدن تصویر شاخص به کارت‌های مقاله ✅
- **ویژگی**: نمایش تصویر شاخص در صفحات دسته‌بندی
- **منبع تصویر**: `featured_image` یا `images` در frontmatter
- **اندازه ثابت**: 200px در Desktop، Responsive در موبایل
- **ویژگی‌ها**: Object-fit Cover, Lazy Loading, Hover Effects
- **فایل‌های تغییر یافته**: 
  - `layouts/_default/list.html`
  - `assets/css/main.css`
- **مستندات**: 
  - `docs/FEATURED_IMAGE_GUIDE.md`
  - `docs/FEATURED_IMAGE_SUMMARY.md`

---

**نویسنده**: Davood Yahya  
**تاریخ اولیه**: 2026-02-08  
**آخرین به‌روزرسانی**: 2026-02-09  
**نسخه**: 2.1
