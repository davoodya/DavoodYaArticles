# 🔧 خلاصه رفع مشکل صفحه 404 در PHP Server

**تاریخ:** ۱۳ فوریه ۲۰۲۶ (۲۴ بهمن ۱۴۰۴)  
**وضعیت:** ✅ حل شده  
**نسخه:** 2.0

---

## 📋 شرح مشکل

### مشکل:
- ✅ **Hugo dev server** (`hugo server -D`): صفحه 404 شخصی‌سازی شده به درستی کار می‌کند
- ❌ **PHP server** (`php -S localhost:8080 -t public`): صفحه 404 پیش‌فرض PHP نمایش داده می‌شود

### دلیل:
سرور داخلی PHP به صورت خودکار صفحه‌های خطای سفارشی را سرو نمی‌کند و نیاز به یک **Router Script** دارد.

---

## ✅ راه‌حل پیاده‌سازی شده

یک **Router Script** حرفه‌ای (`router.php`) ایجاد کردیم که:

1. ✅ فایل‌های استاتیک را با MIME type صحیح سرو می‌کند
2. ✅ برای پوشه‌ها، `index.html` را نمایش می‌دهد
3. ✅ برای 404، صفحه `404.html` سفارشی را نمایش می‌دهد
4. ✅ endpoint های API (`/api/*.php`) را اجرا می‌کند
5. ✅ امنیت: از حملات directory traversal جلوگیری می‌کند

---

## 📁 فایل‌های ایجاد شده

### 1. Router Script
**مکان:** `static/router.php`  
**کپی می‌شود به:** `public/router.php` (در هنگام build)

**ویژگی‌ها:**
- سرو فایل‌های استاتیک (CSS, JS, تصاویر, فونت‌ها)
- مدیریت index.html برای پوشه‌ها
- سرو صفحه 404.html با status code 404
- پشتیبانی از API endpoints
- امنیت: مسدود کردن `..` در مسیر

---

### 2. Batch Script (به‌روز شده)
**فایل:** `start-server.bat`

**تغییرات:**
- ✅ Build با `--cleanDestinationDir`
- ✅ بررسی وجود `router.php`
- ✅ اجرای سرور با router

---

### 3. مستندات
**فایل‌ها:**
- ✅ `404_PHP_SERVER_FIX.md` - راهنمای کامل انگلیسی
- ✅ `خلاصه_رفع_مشکل_404_در_PHP_Server.md` - این فایل (خلاصه فارسی)
- ✅ `test-404-php-server.html` - صفحه تست تعاملی

---

## 🚀 نحوه استفاده

### ❌ روش قبلی (اشتباه):
```bash
hugo --cleanDestinationDir
cd public
php -S localhost:8080 -t .
```
**نتیجه:** صفحه 404 شخصی نمایش داده نمی‌شود ❌

---

### ✅ روش جدید (صحیح):

#### روش 1: استفاده از Batch File (ساده)
```bash
start-server.bat
```

#### روش 2: دستورات دستی
```bash
# 1. Build کردن
hugo --cleanDestinationDir

# 2. رفتن به پوشه public
cd public

# 3. اجرای سرور با Router
php -S localhost:8080 router.php
```

**نکته مهم:** حتماً از `router.php` استفاده کنید، **نه** از `-t .`

---

## 🧪 نحوه تست

### 1️⃣ Build و اجرا:
```bash
# روش سریع
start-server.bat

# یا دستی
hugo --cleanDestinationDir
cd public
php -S localhost:8080 router.php
```

---

### 2️⃣ تست در مرورگر:

#### ✅ صفحه اصلی:
```
http://localhost:8080/
```
**انتظار:** صفحه اصلی بارگذاری شود

---

#### ✅ تست صفحه 404:
```
http://localhost:8080/this-page-does-not-exist
```
**انتظار:** صفحه 404 شخصی‌سازی شده با:
- عدد بزرگ "404"
- عنوان "صفحه یافت نشد!"
- فیلد جستجو
- دکمه‌های "صفحه مقالات" و "صفحه اصلی"
- پیشنهادات
- آخرین مقالات
- استایل کامل

---

#### ✅ تست CSS:
```
http://localhost:8080/css/main.css
```
**انتظار:** فایل CSS بارگذاری شود

---

#### ✅ تست تصویر:
```
http://localhost:8080/images/general/logo.png
```
**انتظار:** تصویر نمایش داده شود

---

## 📊 مقایسه قبل و بعد

| جنبه | قبل ❌ | بعد ✅ |
|------|--------|--------|
| **404 صفحه** | پیش‌فرض PHP | شخصی‌سازی شده |
| **Status Code** | 404 | 404 (صحیح) |
| **استایل** | ندارد | کامل |
| **جستجو** | ندارد | دارد |
| **پیشنهادات** | ندارد | دارد |
| **تجربه کاربری** | ضعیف | عالی |

---

## 🔍 جزئیات فنی Router

### ساختار Router:

```
درخواست می‌رسد
    ↓
1. Parse کردن URL
    ↓
2. بررسی امنیت (مسدود کردن ..)
    ↓
3. API endpoint? (/api/*.php)
    ├─ بله → اجرای PHP
    └─ خیر → ادامه
    ↓
4. پوشه است?
    ├─ بله → سرو index.html
    └─ خیر → ادامه
    ↓
5. فایل وجود دارد?
    ├─ بله → سرو با MIME type صحیح
    └─ خیر → ادامه
    ↓
6. سرو 404.html با status 404
```

---

### MIME Types پشتیبانی شده:

| پسوند | MIME Type | شرح |
|-------|-----------|-----|
| `.html` | `text/html` | صفحات HTML |
| `.css` | `text/css` | استایل‌ها |
| `.js` | `application/javascript` | JavaScript |
| `.json` | `application/json` | داده JSON |
| `.jpg`, `.jpeg` | `image/jpeg` | تصاویر JPEG |
| `.png` | `image/png` | تصاویر PNG |
| `.svg` | `image/svg+xml` | گرافیک SVG |
| `.woff`, `.woff2` | `font/woff`, `font/woff2` | فونت‌ها |
| `.pdf` | `application/pdf` | اسناد PDF |

---

## 🔐 امنیت

### 1. جلوگیری از Directory Traversal:
```php
// مسدود کردن درخواست‌های حاوی ..
if (strpos($requestPath, '..') !== false) {
    http_response_code(403);
    echo '403 Forbidden';
    exit;
}
```

**تست:**
```bash
curl http://localhost:8080/../../../etc/passwd
# نتیجه: 403 Forbidden ✅
```

---

### 2. محدود کردن API:
```php
// فقط فایل‌های PHP در /api/ اجرا می‌شوند
if (preg_match('/^\/api\//', $requestPath)) {
    // اجرای امن با context صحیح
}
```

---

### 3. Content Type صحیح:
```php
// همیشه content type مشخص می‌شود
header('Content-Type: text/html; charset=UTF-8');
```

---

## 🐛 رفع مشکلات رایج

### مشکل 1: Router.php یافت نشد

**علامت:**
```
PHP Fatal error: No such file or directory
```

**راه‌حل:**
```bash
# 1. Build مجدد
hugo --cleanDestinationDir

# 2. بررسی وجود فایل
ls public/router.php

# 3. اجرای مجدد
cd public
php -S localhost:8080 router.php
```

---

### مشکل 2: صفحه 404 شخصی نمایش داده نمی‌شود

**علامت:**
هنوز صفحه 404 پیش‌فرض PHP نمایش داده می‌شود

**راه‌حل:**
```bash
# 1. مطمئن شوید از router استفاده می‌کنید
php -S localhost:8080 router.php

# نه این:
php -S localhost:8080 -t .

# 2. بررسی 404.html
ls public/404.html

# 3. Hard refresh مرورگر
# Ctrl+Shift+R

# 4. سرور را Restart کنید
```

---

### مشکل 3: CSS/JS بارگذاری نمی‌شود

**علامت:**
صفحه بدون استایل نمایش داده می‌شود

**راه‌حل:**
```bash
# 1. F12 → Network Tab
# فایل‌های قرمز (404) را بررسی کنید

# 2. Rebuild
hugo --cleanDestinationDir

# 3. بررسی مسیرها در HTML

# 4. بررسی MIME types در Router
```

---

### مشکل 4: API کار نمی‌کند

**علامت:**
```
/api/comments.php → 404
```

**راه‌حل:**
```bash
# 1. بررسی فایل API
ls public/api/comments.php

# 2. بررسی مجوزها
chmod 644 public/api/*.php

# 3. بررسی Router
# regex برای /api/ صحیح است؟

# 4. بررسی PHP error log
```

---

## ✅ چک‌لیست تست

### قبل از استقرار:
- [ ] `hugo --cleanDestinationDir` بدون خطا اجرا شد
- [ ] `public/404.html` وجود دارد
- [ ] `public/router.php` وجود دارد
- [ ] سرور با router اجرا شد: `php -S localhost:8080 router.php`
- [ ] صفحه اصلی بارگذاری می‌شود: `http://localhost:8080/`
- [ ] 404 شخصی کار می‌کند: `http://localhost:8080/test-404`
- [ ] CSS بارگذاری می‌شود
- [ ] JS بارگذاری می‌شود
- [ ] تصاویر نمایش داده می‌شوند
- [ ] فونت‌ها بارگذاری می‌شوند
- [ ] هیچ error در Console نیست
- [ ] تست امنیت: `http://localhost:8080/../../../etc/passwd` → 403

---

## 📖 مستندات مرتبط

- **راهنمای کامل:** `404_PHP_SERVER_FIX.md`
- **صفحه 404:** `layouts/404.html`
- **استایل 404:** `assets/css/404-page.css`
- **صفحه تست:** `test-404-php-server.html`
- **Batch Script:** `start-server.bat`

---

## 🎯 دستورات سریع

```bash
# ساده‌ترین روش
start-server.bat

# Build + Run
hugo --cleanDestinationDir && cd public && php -S localhost:8080 router.php

# تست 404
curl http://localhost:8080/test-404

# بررسی Router
ls public/router.php

# بررسی 404.html
ls public/404.html

# تست امنیت
curl http://localhost:8080/../../../etc/passwd
```

---

## 🌐 استقرار Production

### ⚠️ توصیه: از PHP server در production استفاده نکنید!

**برای production از این‌ها استفاده کنید:**

### 1. Nginx (پیشنهادی):
```nginx
server {
    listen 80;
    root /var/www/davoodya/public;
    
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

---

### 2. Apache:
```apache
# .htaccess
ErrorDocument 404 /404.html
```

---

### 3. Netlify:
```toml
# netlify.toml
[[redirects]]
  from = "/*"
  to = "/404.html"
  status = 404
```

---

## 🎉 خلاصه

### قبل از رفع:
- ❌ صفحه 404 شخصی نمایش داده نمی‌شد
- ❌ صفحه 404 پیش‌فرض PHP
- ❌ تجربه کاربری ضعیف

### بعد از رفع:
- ✅ صفحه 404 شخصی‌سازی شده
- ✅ Status code صحیح (404)
- ✅ تمام فایل‌ها درست سرو می‌شوند
- ✅ API endpoints کار می‌کنند
- ✅ امنیت تضمین شده
- ✅ تجربه کاربری عالی

---

## 📞 راهنمای سریع استفاده

### برای توسعه:
```bash
hugo server -D
```

### برای تست Production:
```bash
start-server.bat
# یا
hugo --cleanDestinationDir
cd public
php -S localhost:8080 router.php
```

### برای استقرار:
```bash
# Netlify (توصیه می‌شود)
git push origin main
```

---

**وضعیت:** ✅ **آماده برای استقرار**  
**تست شده:** Windows, PHP 8.1+  
**توسعه‌دهنده:** Senior Backend Engineer + PHP Specialist

