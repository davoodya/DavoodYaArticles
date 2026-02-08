# 🚀 راهنمای انتشار (Deployment Guide)

این راهنما مراحل انتشار سایت مقالات به آدرس `https://davoodya.ir/articles/` را توضیح می‌دهد.

---

## 📋 پیش‌نیازها

قبل از شروع، اطمینان حاصل کنید که:

1. ✅ Hugo نصب شده است (`hugo version`)
2. ✅ تمام تغییرات commit شده‌اند
3. ✅ تصاویر در `static/images/` قرار دارند
4. ✅ محتوای جدید در `content/` اضافه شده است

---

## 🔧 تنظیمات BaseURL

سایت برای اجرا روی **Subdirectory** تنظیم شده است:

```toml
# hugo.toml
baseURL = "https://davoodya.ir/articles/"
```

این تنظیم باعث می‌شود:
- تمام لینک‌ها نسبی به `/articles/` باشند
- جستجو به درستی کار کند
- تصاویر با مسیر صحیح بارگذاری شوند

---

## 🏗️ ساخت نسخه Production

### روش 1: استفاده از اسکریپت (پیشنهادی)

**در Windows:**
```bash
build-production.bat
```

**در Linux/Mac:**
```bash
chmod +x build-production.sh
./build-production.sh
```

### روش 2: دستور مستقیم Hugo

```bash
hugo --minify --cleanDestinationDir --gc
```

پارامترها:
- `--minify`: فشرده‌سازی HTML, CSS, JS
- `--cleanDestinationDir`: پاک کردن فایل‌های اضافی
- `--gc`: جمع‌آوری زباله (garbage collection)

---

## 🧪 تست محلی

قبل از آپلود، سایت را محلی تست کنید:

### روش 1: با Hugo Server

```bash
hugo server --baseURL="https://davoodya.ir/articles/" --bind 0.0.0.0
```

سپس در مرورگر: `http://localhost:1313/articles/`

### روش 2: با Python HTTP Server

```bash
cd public
python -m http.server 8000
```

سپس در مرورگر: `http://localhost:8000/articles/`

**نکته مهم:** در محیط محلی، ممکن است برخی لینک‌ها کار نکنند. این طبیعی است.

---

## 📤 آپلود به سرور

### مرحله 1: آماده‌سازی

1. پوشه `public/` ساخته شده را پیدا کنید
2. محتوای آن را آماده آپلود کنید

### مرحله 2: آپلود

**مسیر هدف در سرور:**
```
/public_html/articles/
```

یا

```
/var/www/html/articles/
```

### مرحله 3: تنظیم Permissions

```bash
# در سرور
cd /public_html/articles/
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;
```

---

## 🔍 بررسی پس از انتشار

بعد از آپلود، موارد زیر را چک کنید:

### 1️⃣ صفحه اصلی
```
https://davoodya.ir/articles/
```

### 2️⃣ جستجو
- دکمه جستجو را کلیک کنید
- چیزی جستجو کنید (مثلاً "security")
- بررسی کنید که نتایج نمایش داده شوند

### 3️⃣ سایدبار
- جستجوی inline در سایدبار
- لینک‌های دسته‌بندی
- لینک‌های مقالات اخیر

### 4️⃣ تصاویر
- باز کردن یک مقاله با تصویر
- بررسی اینکه تصاویر بارگذاری می‌شوند

### 5️⃣ JSON Index
```
https://davoodya.ir/articles/index.json
```

این فایل باید لیست تمام مقالات را نمایش دهد.

---

## 🐛 عیب‌یابی مشکلات رایج

### مشکل: جستجو کار نمی‌کند

**علت:** فایل `index.json` بارگذاری نمی‌شود

**راه‌حل:**
1. بررسی کنید که فایل `public/index.json` وجود دارد
2. آپلود مجدد فایل
3. پاک کردن cache مرورگر: `Ctrl+Shift+Delete`
4. بررسی Console مرورگر: `F12` → Console

### مشکل: تصاویر نمایش داده نمی‌شوند

**علت:** مسیر تصاویر اشتباه است

**راه‌حل:**
1. بررسی کنید که پوشه `static/images/` در `public/images/` کپی شده
2. بررسی لینک‌های تصاویر در markdown: `/images/category/image.png`
3. اجرای مجدد اسکریپت تبدیل تصاویر

### مشکل: CSS/JS بارگذاری نمی‌شود

**علت:** مسیرهای استاتیک نادرست

**راه‌حل:**
1. بررسی `hugo.toml` → `baseURL = "https://davoodya.ir/articles/"`
2. Build مجدد سایت
3. پاک کردن cache مرورگر

### مشکل: 404 برای صفحات

**علت:** تنظیمات وب سرور

**راه‌حل:** اضافه کردن `.htaccess` در root:

```apache
# .htaccess
RewriteEngine On
RewriteBase /articles/

# Handle index files
DirectoryIndex index.html

# Trailing slash redirect
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_URI} !/$
RewriteRule ^(.*[^/])$ $1/ [L,R=301]

# Clean URLs
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ $1/index.html [L]
```

---

## 📊 بررسی SEO پس از انتشار

1. **Google Search Console:**
   - ثبت URL: `https://davoodya.ir/articles/`
   - ارسال Sitemap: `https://davoodya.ir/articles/sitemap.xml`

2. **بررسی Robots.txt:**
   ```
   https://davoodya.ir/articles/robots.txt
   ```

3. **بررسی Structured Data:**
   - استفاده از [Google Rich Results Test](https://search.google.com/test/rich-results)
   - تست یک مقاله

---

## 🔄 به‌روزرسانی محتوا

برای اضافه کردن مقاله جدید:

1. ✅ فایل markdown جدید در `content/category/` بسازید
2. ✅ تصاویر را با `convert_images.py` منتقل کنید
3. ✅ Title ها را با `title-adder.py` بررسی کنید
4. ✅ Build production: `./build-production.bat`
5. ✅ تست محلی
6. ✅ آپلود فقط فایل‌های تغییر یافته

---

## 📝 Checklist پیش از انتشار

- [ ] تمام تصاویر در `static/images/` هستند
- [ ] Front matter تمام مقالات صحیح است
- [ ] Title ها اضافه شده‌اند
- [ ] `hugo.toml` → baseURL صحیح است
- [ ] Build بدون خطا انجام شد
- [ ] تست محلی موفق بود
- [ ] Backup از نسخه قبلی گرفته شد

---

## 🆘 پشتیبانی

در صورت بروز مشکل:

1. 📋 لاگ‌های Hugo را بررسی کنید
2. 🔍 Console مرورگر را چک کنید (`F12`)
3. 📧 با تیم فنی تماس بگیرید
4. 📚 مستندات Hugo را مطالعه کنید: [gohugo.io/documentation](https://gohugo.io/documentation/)

---

## 📅 تاریخچه نسخه‌ها

- **v1.0.0** (2026-02-08): نسخه اولیه با پشتیبانی subdirectory

---

✅ **سایت آماده انتشار است!**
