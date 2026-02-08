# راهنمای انتشار (Deploy) - وبسایت مقالات

## 📋 توضیحات

این وبسایت به عنوان **بخش مقالات** وبسایت اصلی `davoodya.ir` طراحی شده و در مسیر `/articles/` قرار می‌گیرد.

## 🔧 تنظیمات انجام شده

### BaseURL
```toml
baseURL = "https://davoodya.ir/articles/"
```

### تنظیمات URL
```toml
relativeURLs = false
canonifyURLs = true
```

این تنظیمات باعث می‌شود:
- همه URL‌ها به صورت مطلق (absolute) باشند
- prefix `/articles/` به همه لینک‌ها اضافه شود

## 📁 ساختار نهایی در سرور

```
davoodya.ir/
├── index.html                 # صفحه اصلی وبسایت (وبسایت اصلی شما)
├── about/
├── services/
├── ...
└── articles/                  # 👈 پوشه Hugo (این پروژه)
    ├── index.html            # صفحه اصلی مقالات
    ├── cyber-security/       # دسته‌بندی امنیت سایبری
    ├── python/               # دسته‌بندی پایتون
    ├── seo/                  # دسته‌بندی سئو
    ├── tools/                # دسته‌بندی ابزارها
    ├── assets/               # فایل‌های CSS, JS, Fonts
    ├── index.json            # داده‌های جستجو
    └── sitemap.xml           # نقشه سایت
```

## 🚀 نحوه انتشار

### 1. Build وبسایت

```bash
cd h:\Repo\Hugo\davoodya
hugo --cleanDestinationDir
```

این دستور پوشه `public/` را با فایل‌های آماده برای انتشار می‌سازد.

### 2. محتویات پوشه public/

پس از build، پوشه `public/` شامل موارد زیر است:

```
public/
├── index.html
├── index.json
├── index.xml
├── sitemap.xml
├── robots.txt
├── 404.html
├── assets/
│   ├── css/
│   ├── js/
│   └── fonts/
├── cyber-security/
│   ├── index.html
│   └── [مقالات...]
├── python/
├── seo/
├── tools/
├── tags/
└── categories/
```

### 3. آپلود به سرور

#### روش 1: FTP/SFTP

1. اتصال به سرور با FTP Client (مثل FileZilla)
2. رفتن به مسیر `/public_html/` یا `/www/`
3. ایجاد پوشه `articles/` (اگر وجود ندارد)
4. آپلود **محتویات** پوشه `public/` به `/articles/`

```
سرور:
/public_html/
    └── articles/         👈 اینجا
        ├── index.html
        ├── assets/
        └── ...
```

#### روش 2: Git Deploy

اگر از Git برای deploy استفاده می‌کنید:

```bash
# 1. Build
hugo --cleanDestinationDir

# 2. Copy به repository deploy
cp -r public/* /path/to/deploy-repo/articles/

# 3. Commit و Push
cd /path/to/deploy-repo
git add .
git commit -m "Update articles"
git push
```

#### روش 3: rsync (Linux/Mac)

```bash
rsync -avz --delete public/ user@server:/path/to/public_html/articles/
```

### 4. تنظیمات .htaccess (اختیاری)

برای سئو بهتر، فایل `.htaccess` در پوشه `articles/` ایجاد کنید:

```apache
# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}/articles/$1 [L,R=301]

# Remove trailing slashes (except for directories)
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.+)/$ /articles/$1 [L,R=301]

# Custom 404
ErrorDocument 404 /articles/404.html

# Enable Gzip Compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css text/javascript application/javascript application/json
</IfModule>

# Browser Caching
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType font/woff2 "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
</IfModule>
```

## 🔗 URL های نهایی

پس از انتشار، URL‌ها به شکل زیر خواهند بود:

```
https://davoodya.ir/articles/                           # صفحه اصلی مقالات
https://davoodya.ir/articles/cyber-security/            # دسته‌بندی
https://davoodya.ir/articles/cyber-security/e1-seo/     # مقاله
https://davoodya.ir/articles/tags/cybersecurity/        # تگ
https://davoodya.ir/articles/index.json                 # داده‌های جستجو
```

## ✅ چک‌لیست قبل از انتشار

- [ ] Build موفقیت‌آمیز انجام شده
- [ ] فایل `public/index.html` وجود دارد
- [ ] فایل `public/index.json` وجود دارد
- [ ] پوشه `public/assets/` کامل است
- [ ] تمام دسته‌بندی‌ها در `public/` هستند
- [ ] robots.txt و sitemap.xml وجود دارند
- [ ] BaseURL در `hugo.toml` درست است
- [ ] تست local انجام شده: `hugo server`

## 🧪 تست پس از انتشار

### 1. بررسی صفحه اصلی
```
https://davoodya.ir/articles/
```
✅ باید صفحه دسته‌بندی‌ها نمایش داده شود

### 2. بررسی دسته‌بندی
```
https://davoodya.ir/articles/cyber-security/
```
✅ باید لیست مقالات نمایش داده شود

### 3. بررسی مقاله
```
https://davoodya.ir/articles/cyber-security/[slug]/
```
✅ باید محتوای مقاله نمایش داده شود

### 4. بررسی جستجو
- کلیک روی دکمه جستجو
- تایپ یک کلمه
- ✅ باید نتایج نمایش داده شوند

### 5. بررسی Responsive
- باز کردن در موبایل/تبلت
- ✅ باید کاملاً responsive باشد

### 6. بررسی SEO
```
https://davoodya.ir/articles/sitemap.xml
```
✅ باید sitemap نمایش داده شود

## 🔄 بروزرسانی مقالات

### اضافه کردن مقاله جدید

1. ایجاد فایل markdown در `content/[category]/`
2. نوشتن محتوا با front matter
3. Build مجدد: `hugo`
4. آپلود فایل‌های جدید

### ویرایش مقاله موجود

1. ویرایش فایل markdown
2. Build مجدد: `hugo`
3. آپلود فایل‌های بروز شده

## 🌐 ادغام با وبسایت اصلی

### لینک کردن از وبسایت اصلی

در وبسایت اصلی `davoodya.ir`، لینک به بخش مقالات:

```html
<a href="/articles/">مقالات</a>
```

یا در منو:

```html
<nav>
    <a href="/">خانه</a>
    <a href="/about/">درباره من</a>
    <a href="/articles/">مقالات</a>  👈 این
    <a href="/contact/">تماس</a>
</nav>
```

## 📊 Google Search Console

### ثبت Sitemap

1. رفتن به Google Search Console
2. انتخاب property: `davoodya.ir`
3. رفتن به Sitemaps
4. اضافه کردن: `https://davoodya.ir/articles/sitemap.xml`

## 🐛 عیب‌یابی

### مشکل: لینک‌ها 404 می‌دهند

**راه حل:**
- بررسی BaseURL در `hugo.toml`
- مطمئن شوید پوشه `articles/` در مسیر درست است
- بررسی فایل `.htaccess`

### مشکل: CSS/JS لود نمی‌شوند

**راه حل:**
- بررسی مسیر فایل‌ها در `public/assets/`
- مطمئن شوید `canonifyURLs = true` است
- چک کردن permissions فایل‌ها

### مشکل: جستجو کار نمی‌کند

**راه حل:**
- بررسی وجود `index.json` در سرور
- مطمئن شوید `[outputs]` در `hugo.toml` درست است
- چک کردن Console browser برای خطاهای JavaScript

## 📝 نکات مهم

1. ✅ **همیشه** قبل از آپلود، build کنید
2. ✅ پس از هر تغییر، cache مرورگر را پاک کنید
3. ✅ sitemap را در Google Search Console بروز کنید
4. ✅ robots.txt را بررسی کنید
5. ✅ SSL certificate فعال باشد (HTTPS)

## 🎯 آماده برای انتشار!

وبسایت شما کاملاً آماده است و می‌توانید آن را در `/articles/` منتشر کنید! 🚀

---

**نویسنده:** Davood Yahya  
**تاریخ:** 2026-02-08  
**نسخه:** 1.0.0
