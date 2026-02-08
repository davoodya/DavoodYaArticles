# راهنمای مدیریت تصاویر - Hugo

## 🎯 هدف

تبدیل لینک‌های تصویر از فرمت Obsidian به فرمت Hugo و مدیریت فایل‌های تصویر.

## 📝 فرمت‌ها

### فرمت فعلی (Obsidian)
```markdown
![[Pasted image 20260205202337.png]]
```

### فرمت مورد نیاز (Hugo)
```markdown
![توضیح تصویر](/images/posts/category/image-name.png)
```

## 🗂️ ساختار پوشه‌ها

```
davoodya/
├── static/
│   └── images/
│       └── posts/
│           ├── cyber-security/
│           │   ├── image1.png
│           │   └── image2.jpg
│           ├── python/
│           ├── seo/
│           └── tools/
└── content/
    ├── cyber-security/
    │   └── article.md  (لینک به /images/posts/cyber-security/image1.png)
    ├── python/
    ├── seo/
    └── tools/
```

## 🚀 روش‌های اجرا

### روش 1: استفاده از اسکریپت Python (پیشنهادی)

#### مرحله 1: اجرای اسکریپت
```bash
cd h:\Repo\Hugo\davoodya
python convert_images.py
```

این کار انجام می‌دهد:
- ✅ تمام فایل‌های markdown را اسکن می‌کند
- ✅ لینک‌های `![[image.png]]` را پیدا می‌کند
- ✅ آنها را به `![image](/images/posts/category/image.png)` تبدیل می‌کند
- ✅ پوشه‌های `static/images/posts/` را ایجاد می‌کند
- ✅ لیست تصاویر را در `images_list.txt` ذخیره می‌کند
- ✅ اسکریپت کپی در `copy_images.bat` ایجاد می‌کند

#### مرحله 2: کپی تصاویر

**روش A: اگر همه تصاویر در یک پوشه هستند**

1. اسکریپت را ویرایش کنید:
```python
SOURCE_IMAGES_DIR = "C:\\Path\\To\\Your\\Images"
```

2. دوباره اجرا کنید:
```bash
python convert_images.py
```

**روش B: استفاده از اسکریپت batch**

1. فایل `copy_images.bat` را باز کنید
2. مسیر را تنظیم کنید:
```batch
set SOURCE_DIR=C:\Path\To\Your\Images
```
3. اجرا کنید:
```bash
copy_images.bat
```

**روش C: کپی دستی**

1. فایل `images_list.txt` را باز کنید
2. برای هر تصویر:
   - تصویر اصلی را پیدا کنید
   - آن را به مسیر مشخص شده کپی کنید

### روش 2: تبدیل و کپی دستی

#### مرحله 1: ایجاد پوشه‌ها

```bash
mkdir static\images\posts\cyber-security
mkdir static\images\posts\python
mkdir static\images\posts\seo
mkdir static\images\posts\tools
```

#### مرحله 2: تبدیل لینک‌ها

برای هر فایل markdown:

**قبل:**
```markdown
![[Pasted image 20260205202337.png]]
```

**بعد:**
```markdown
![Pasted image](/images/posts/cyber-security/pasted_image_20260205202337.png)
```

#### مرحله 3: کپی تصاویر

1. نام فایل تصویر را از markdown پیدا کنید
2. تصویر را از پوشه اصلی پیدا کنید
3. آن را به `static/images/posts/[category]/` کپی کنید
4. نام را تمیز کنید (حذف فضا، کاراکترهای خاص)

## 📋 نام‌گذاری تصاویر

### قوانین نام‌گذاری:

1. **حروف کوچک**: `Image.PNG` → `image.png`
2. **فضای خالی**: `My Image.png` → `my_image.png`
3. **کاراکترهای خاص**: `Image (1).png` → `image_1.png`

### مثال:
```
Pasted image 20260205202337.png
↓
pasted_image_20260205202337.png
```

## 🔍 پیدا کردن تصاویر در Markdown

### دستور Search در VSCode:

```regex
!\[\[([^\]]+\.(png|jpg|jpeg|gif|webp|svg))\]\]
```

این regex تمام تصاویر Obsidian را پیدا می‌کند.

### دستور Replace:

```
![توضیح]($1)
```

## ✅ تست تصاویر

### 1. بررسی مسیرها

```bash
# بررسی وجود تصویر
dir static\images\posts\cyber-security\image.png

# لیست تمام تصاویر
dir /s static\images\posts\*.png
```

### 2. تست در Hugo

```bash
hugo server -D
```

سپس:
- رفتن به مقاله
- بررسی نمایش تصویر
- چک کردن Console برای 404 errors

### 3. بررسی لینک‌های شکسته

اگر تصویر نمایش داده نمی‌شود:

1. **بررسی مسیر**:
   ```markdown
   # درست
   ![alt](/images/posts/category/image.png)
   
   # غلط
   ![alt](images/posts/category/image.png)
   ![alt](/static/images/posts/category/image.png)
   ```

2. **بررسی نام فایل**:
   - حساس به حروف بزرگ/کوچک
   - فضای خالی → `_`
   - کاراکترهای خاص حذف شوند

3. **بررسی وجود فایل**:
   ```bash
   ls static/images/posts/category/
   ```

## 🎨 بهینه‌سازی تصاویر

### قبل از آپلود:

1. **فشرده‌سازی**:
   - PNG: استفاده از TinyPNG یا ImageOptim
   - JPG: کیفیت 80-85%

2. **تغییر اندازه**:
   - عرض حداکثر: 1200px
   - برای thumbnail: 400px

3. **فرمت مناسب**:
   - عکس: JPG
   - لوگو/آیکون: PNG
   - انیمیشن: GIF یا WebP

### ابزارهای پیشنهادی:

- **TinyPNG**: https://tinypng.com/
- **Squoosh**: https://squoosh.app/
- **ImageMagick** (command line):
  ```bash
  magick convert input.png -resize 1200x output.png
  magick convert input.png -quality 85 output.jpg
  ```

## 📊 گزارش تصاویر

پس از اجرای اسکریپت، فایل‌های زیر ایجاد می‌شوند:

### 1. images_list.txt
```
لیست تصاویر مورد نیاز
============================================================

Pasted image 20260205202337.png → static/images/posts/cyber-security/pasted_image_20260205202337.png
Screenshot 2026-02-01.png → static/images/posts/seo/screenshot_2026-02-01.png
...
```

### 2. copy_images.bat (Windows)
```batch
@echo off
set SOURCE_DIR=C:\Path\To\Your\Images
copy "%SOURCE_DIR%\image1.png" "static\images\posts\category\image1.png"
...
```

### 3. copy_images.sh (Linux/Mac)
```bash
#!/bin/bash
SOURCE_DIR="/path/to/your/images"
cp "$SOURCE_DIR/image1.png" "static/images/posts/category/image1.png"
...
```

## 🐛 عیب‌یابی

### مشکل 1: تصویر نمایش داده نمی‌شود

**راه حل:**
```markdown
# بررسی کنید مسیر با / شروع شود
![alt](/images/posts/category/image.png)  ✅
![alt](images/posts/category/image.png)   ❌
```

### مشکل 2: تصویر در local کار می‌کند اما در production نه

**راه حل:**
- بررسی نام فایل (حروف بزرگ/کوچک)
- مطمئن شوید تصویر در `public/images/` کپی شده
- rebuild کنید: `hugo --cleanDestinationDir`

### مشکل 3: تصاویر خیلی بزرگ هستند

**راه حل:**
```css
/* در CSS اضافه کنید */
.article-content img {
    max-width: 100%;
    height: auto;
}
```

## 📝 نکات مهم

1. ✅ **همیشه** از مسیر مطلق استفاده کنید: `/images/...`
2. ✅ نام فایل‌ها را **تمیز** کنید (بدون فضا و کاراکتر خاص)
3. ✅ تصاویر را **بهینه** کنید (فشرده‌سازی)
4. ✅ **alt text** برای SEO اضافه کنید
5. ✅ قبل از deploy، تمام تصاویر را **تست** کنید

## 🎯 خلاصه مراحل

```bash
# 1. اجرای اسکریپت
python convert_images.py

# 2. بررسی فایل images_list.txt
notepad images_list.txt

# 3. کپی تصاویر (یکی از روش‌ها)
# - تنظیم SOURCE_IMAGES_DIR و اجرای مجدد
# - اجرای copy_images.bat
# - کپی دستی با راهنمای images_list.txt

# 4. تست
hugo server -D

# 5. Build نهایی
hugo --cleanDestinationDir
```

## 📚 مثال کامل

### قبل:
```markdown
# مقاله من

این یک تصویر است:

![[Pasted image 20260205202337.png]]

متن بعد از تصویر.
```

### بعد:
```markdown
# مقاله من

این یک تصویر است:

![نمای کلی سیستم](/images/posts/cyber-security/pasted_image_20260205202337.png)

متن بعد از تصویر.
```

### ساختار فایل:
```
static/images/posts/cyber-security/pasted_image_20260205202337.png
content/cyber-security/article.md
```

---

**آماده برای استفاده!** 🖼️✨

اگر سؤال یا مشکلی داشتید، به این راهنما مراجعه کنید.
