# 📚 راهنمای استفاده از اسکریپت‌های Rename تصاویر

> **نویسنده**: Davood Yahya  
> **تاریخ**: 2026-02-08  
> **نسخه**: 2.0

---

## 📋 فهرست مطالب

1. [نمای کلی](#نمای-کلی)
2. [اسکریپت‌ها](#اسکریپت‌ها)
3. [ترتیب استفاده](#ترتیب-استفاده)
4. [مثال عملی](#مثال-عملی)
5. [فایل‌های خروجی](#فایل‌های-خروجی)
6. [نکات مهم](#نکات-مهم)

---

## 🎯 نمای کلی

این سیستم شامل **دو اسکریپت مجزا** است که وظایف مختلفی دارند:

### 1️⃣ `images-renamer.py` - تغییر نام فایل‌های فیزیکی

```
وظیفه: فقط تصاویر اصلی در static/images/ را rename می‌کند
        هیچ تغییری در markdown ها ایجاد نمی‌کند
```

### 2️⃣ `image-article-renamer.py` - به‌روزرسانی مراجع markdown

```
وظیفه: فقط مراجع تصاویر در markdown ها را به‌روز می‌کند
        هیچ تغییری در فایل‌های فیزیکی ایجاد نمی‌کند
```

---

## 🔧 اسکریپت‌ها

### اسکریپت 1: `images-renamer.py`

#### ✅ کارهایی که انجام می‌دهد:
- ✔️ تمام markdown ها را اسکن می‌کند
- ✔️ تصاویر و alt text آنها را پیدا می‌کند
- ✔️ mapping تغییر نام‌ها را ایجاد می‌کند
- ✔️ **فقط** فایل‌های فیزیکی در `static/images/` را rename می‌کند
- ✔️ تصاویر پردازش شده را track می‌کند (`processed_images.json`)

#### ❌ کارهایی که انجام نمی‌دهد:
- ❌ هیچ تغییری در markdown ها ایجاد نمی‌کند
- ❌ تصاویر قبلاً پردازش شده را دوباره rename نمی‌کند

#### 📤 خروجی‌ها:
```
images_rename_mapping.json     # mapping های shared
processed_images.json          # track تصاویر پردازش شده
images_renamer.log            # لاگ کامل
images_renamer_report.txt     # گزارش خلاصه
```

---

### اسکریپت 2: `image-article-renamer.py`

#### ✅ کارهایی که انجام می‌دهد:
- ✔️ mapping را از `images_rename_mapping.json` می‌خواند
- ✔️ **فقط** مراجع تصاویر در markdown ها را به‌روز می‌کند
- ✔️ وجود فایل‌های renamed در `static/images/` را تأیید می‌کند
- ✔️ مقالات پردازش شده را track می‌کند (`processed_articles.json`)

#### ❌ کارهایی که انجام نمی‌دهد:
- ❌ هیچ تغییری در فایل‌های فیزیکی ایجاد نمی‌کند
- ❌ مقالات قبلاً پردازش شده را دوباره به‌روز نمی‌کند

#### 📤 خروجی‌ها:
```
processed_articles.json              # track مقالات پردازش شده
image_article_renamer.log           # لاگ کامل
image_article_renamer_report.txt    # گزارش خلاصه
```

---

## 📝 ترتیب استفاده

### 🔴 مهم: همیشه به ترتیب اجرا کنید!

```bash
# مرحله 1: Rename فایل‌های فیزیکی
python images-renamer.py

# مرحله 2: به‌روزرسانی markdown ها
python image-article-renamer.py
```

### چرا به ترتیب؟

```
images-renamer.py
    ↓
تصاویر فیزیکی rename می‌شوند
    ↓
mapping در images_rename_mapping.json ذخیره می‌شود
    ↓
image-article-renamer.py
    ↓
mapping را می‌خواند و markdown ها را به‌روز می‌کند
    ↓
تأیید می‌کند که فایل‌های renamed وجود دارند
```

---

## 💡 مثال عملی

### سناریو: اضافه کردن مقاله جدید با 3 تصویر

#### 1. ایجاد مقاله:

```markdown
+++
title = "My New Article"
+++

![My Image-1](/images/tools/Pastedimage123.png)
![My Image-2](/images/tools/Pastedimage456.png)
![My Image-3](/images/tools/Pastedimage789.png)
```

#### 2. قرار دادن تصاویر:

```
static/images/tools/
├── Pastedimage123.png
├── Pastedimage456.png
└── Pastedimage789.png
```

#### 3. اجرای اسکریپت اول:

```bash
python images-renamer.py
```

**خروجی:**
```
[File] tools/My New Article.md
  Found 3 image(s)
    + Will rename: Pastedimage123.png
      -> MyImage-1.png
    + Will rename: Pastedimage456.png
      -> MyImage-2.png
    + Will rename: Pastedimage789.png
      -> MyImage-3.png

[Category] tools
  + Renamed: Pastedimage123.png
    -> MyImage-1.png
  + Renamed: Pastedimage456.png
    -> MyImage-2.png
  + Renamed: Pastedimage789.png
    -> MyImage-3.png

Physical files renamed: 3
```

#### 4. وضعیت فایل‌ها بعد از مرحله 1:

```
static/images/tools/
├── MyImage-1.png  ✅ (renamed)
├── MyImage-2.png  ✅ (renamed)
└── MyImage-3.png  ✅ (renamed)

content/tools/My New Article.md
├── ![My Image-1](/images/tools/Pastedimage123.png)  ❌ (هنوز قدیمی)
├── ![My Image-2](/images/tools/Pastedimage456.png)  ❌ (هنوز قدیمی)
└── ![My Image-3](/images/tools/Pastedimage789.png)  ❌ (هنوز قدیمی)
```

#### 5. اجرای اسکریپت دوم:

```bash
python image-article-renamer.py
```

**خروجی:**
```
[File] tools/My New Article.md
  Found 3 image(s)
    + Updated: Pastedimage123.png
      -> MyImage-1.png
    + Updated: Pastedimage456.png
      -> MyImage-2.png
    + Updated: Pastedimage789.png
      -> MyImage-3.png
  [Saved] 3 image(s) updated

Files modified: 1
Images updated: 3
```

#### 6. وضعیت نهایی:

```
static/images/tools/
├── MyImage-1.png  ✅
├── MyImage-2.png  ✅
└── MyImage-3.png  ✅

content/tools/My New Article.md
├── ![My Image-1](/images/tools/MyImage-1.png)  ✅
├── ![My Image-2](/images/tools/MyImage-2.png)  ✅
└── ![My Image-3](/images/tools/MyImage-3.png)  ✅
```

---

## 📁 فایل‌های خروجی

### فایل‌های Mapping و Tracking:

```
images_rename_mapping.json     # 🔄 shared بین دو اسکریپت
├── نقشه تغییر نام‌ها
├── استفاده: هر دو اسکریپت
└── merge می‌شود (نه replace)

processed_images.json         # 📷 tracking تصاویر
├── لیست تصاویر پردازش شده
├── استفاده: images-renamer.py
└── جلوگیری از پردازش مجدد

processed_articles.json       # 📝 tracking مقالات
├── لیست مقالات پردازش شده
├── استفاده: image-article-renamer.py
└── جلوگیری از پردازش مجدد
```

### فایل‌های لاگ و گزارش:

```
images_renamer.log                   # لاگ کامل اسکریپت اول
image_article_renamer.log           # لاگ کامل اسکریپت دوم
images_renamer_report.txt           # گزارش خلاصه اسکریپت اول
image_article_renamer_report.txt    # گزارش خلاصه اسکریپت دوم
```

---

## ⚠️ نکات مهم

### 1. ترتیب اجرا

```
❌ اشتباه:
   1. image-article-renamer.py
   2. images-renamer.py

✅ صحیح:
   1. images-renamer.py
   2. image-article-renamer.py
```

### 2. Backup قبل از اجرا

```bash
# همیشه قبل از اجرا backup بگیرید
cp -r static/images/ static/images_backup/
cp -r content/ content_backup/
```

### 3. فقط فایل‌های جدید پردازش می‌شوند

```
اجرای اول:
- 100 تصویر پردازش شد
- 100 مقاله به‌روز شد

اجرای دوم (با 5 تصویر جدید):
- 5 تصویر پردازش شد ✅
- 95 تصویر skip شد (already processed)
- 5 مقاله به‌روز شد ✅
- 95 مقاله skip شد (already processed)
```

### 4. حذف tracking برای اجرای کامل مجدد

```bash
# اگر می‌خواهید همه چیز را دوباره پردازش کنید:
del processed_images.json
del processed_articles.json

# سپس اجرا:
python images-renamer.py
python image-article-renamer.py
```

### 5. بررسی لاگ‌ها

```bash
# بررسی لاگ اسکریپت اول
type images_renamer.log

# بررسی لاگ اسکریپت دوم
type image_article_renamer.log

# بررسی گزارش‌ها
type images_renamer_report.txt
type image_article_renamer_report.txt
```

---

## 🐛 عیب‌یابی

### خطا: "Rename mapping file not found"

```
X Rename mapping file not found: images_rename_mapping.json
  Please run images-renamer.py first to rename physical files.
```

**راه‌حل:**
```bash
# ابتدا اسکریپت اول را اجرا کنید
python images-renamer.py
```

---

### خطا: "New file doesn't exist"

```
Warning: New file doesn't exist: MyImage-1.png
         Expected at: static/images/tools/MyImage-1.png
         Run images-renamer.py first!
```

**راه‌حل:**
```bash
# فایل فیزیکی هنوز rename نشده
# اسکریپت اول را اجرا کنید
python images-renamer.py
```

---

### خطا: "Category mismatch"

```
Warning: Category mismatch for Pastedimage123.png
         Found: seo, Mapped: tools
```

**راه‌حل:**
- یک تصویر با همان نام در چند دسته وجود دارد
- نام تصویر را manually تغییر دهید
- یا تصویر را به دسته صحیح منتقل کنید

---

## 📊 نمای کلی فایل‌ها

```
davoodya/
├── content/                              # مقالات markdown
│   ├── tools/
│   ├── cyber-security/
│   ├── linux/
│   └── seo/
│
├── static/images/                        # تصاویر فیزیکی
│   ├── tools/
│   ├── cyber-security/
│   ├── linux/
│   └── seo/
│
├── images-renamer.py                     # اسکریپت 1️⃣
├── image-article-renamer.py             # اسکریپت 2️⃣
│
├── images_rename_mapping.json            # 🔄 shared mapping
├── processed_images.json                 # 📷 tracking تصاویر
├── processed_articles.json               # 📝 tracking مقالات
│
├── images_renamer.log                    # لاگ اسکریپت اول
├── image_article_renamer.log            # لاگ اسکریپت دوم
├── images_renamer_report.txt            # گزارش اسکریپت اول
├── image_article_renamer_report.txt     # گزارش اسکریپت دوم
│
├── IMAGES_RENAMER_GUIDE.md              # راهنمای کامل
├── CHANGES_SUMMARY.md                    # خلاصه تغییرات
└── README_SCRIPTS_USAGE.md              # این فایل
```

---

## 🎓 خلاصه

### قبل از استفاده:
1. ✅ Backup از `static/images/` و `content/` بگیرید
2. ✅ تصاویر جدید را در `static/images/` قرار دهید
3. ✅ مقاله جدید را با مراجع تصویر اضافه کنید

### استفاده:
```bash
# 1. Rename فایل‌های فیزیکی
python images-renamer.py

# 2. به‌روزرسانی markdown ها
python image-article-renamer.py
```

### بعد از استفاده:
1. ✅ لاگ‌ها را بررسی کنید
2. ✅ گزارش‌ها را مشاهده کنید
3. ✅ فایل‌های rename شده را تأیید کنید
4. ✅ build و test کنید

---

## 📚 مستندات بیشتر

برای اطلاعات بیشتر:
- [`IMAGES_RENAMER_GUIDE.md`](IMAGES_RENAMER_GUIDE.md) - راهنمای کامل با مثال‌های بیشتر
- [`CHANGES_SUMMARY.md`](CHANGES_SUMMARY.md) - خلاصه تغییرات نسخه 2.0

---

**نویسنده**: Davood Yahya  
**تاریخ**: 2026-02-08  
**نسخه**: 2.0 - Separated physical rename and markdown update

---

## ❓ سؤالات متداول

### ❓ آیا می‌توانم فقط یکی از اسکریپت‌ها را اجرا کنم؟

✅ بله، اما:
- اگر فقط `images-renamer.py` اجرا کنید: فایل‌های فیزیکی rename می‌شوند اما markdown ها قدیمی می‌مانند
- اگر فقط `image-article-renamer.py` اجرا کنید: error می‌گیرید چون mapping یا فایل‌های renamed وجود ندارند

### ❓ اگر دو بار اجرا کنم چه می‌شود؟

✅ مشکلی نیست:
- اسکریپت‌ها فایل‌های قبلاً پردازش شده را skip می‌کنند
- فقط فایل‌های جدید پردازش می‌شوند

### ❓ چگونه همه چیز را reset کنم؟

```bash
del processed_images.json
del processed_articles.json
```

---

**پایان راهنما** 🎉
