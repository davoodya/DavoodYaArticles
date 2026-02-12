# 🔧 راه‌اندازی محیط توسعه برای سیستم کامنت

## ⚠️ مشکل و راه‌حل

### مشکل:
- Hugo Server فایل‌های PHP را اجرا نمی‌کند
- `/api/comments.php` با 404 مواجه می‌شود
- کامنت‌ها ذخیره نمی‌شوند

### راه‌حل:
اجرای **دو سرور همزمان**:
1. **Hugo Server** (پورت 1313) - برای محتوا
2. **PHP Server** (پورت 8080) - برای API

---

## 🚀 نحوه اجرا

### روش 1: PowerShell Script (توصیه می‌شود)

```powershell
.\start-dev-server.ps1
```

این اسکریپت:
- ✅ PHP Server را روی پورت 8080 راه‌اندازی می‌کند
- ✅ Hugo Server را روی پورت 1313 راه‌اندازی می‌کند
- ✅ با Ctrl+C هر دو را متوقف می‌کند

### روش 2: دو ترمینال جداگانه

**ترمینال 1 (PHP Server):**
```bash
php -S localhost:8080 -t .
```

**ترمینال 2 (Hugo Server):**
```bash
hugo server -D
```

---

## 🔗 آدرس‌ها

بعد از اجرا:

| سرویس | آدرس |
|--------|------|
| 🌐 **وبسایت Hugo** | http://localhost:1313 |
| 🔌 **API کامنت‌ها** | http://localhost:8080/api/comments.php |
| 🛡️ **پنل ادمین** | http://localhost:8080/api/admin.php |

---

## ✅ تست

### 1. تست API:
```bash
# GET - دریافت کامنت‌ها
curl "http://localhost:8080/api/comments.php?article=test"

# POST - ارسال کامنت
curl -X POST http://localhost:8080/api/comments.php \
  -H "Content-Type: application/json" \
  -d '{
    "article_slug": "test",
    "name": "تست",
    "email": "test@example.com",
    "comment": "این یک تست است"
  }'
```

### 2. تست در مرورگر:
1. باز کنید: http://localhost:1313
2. به یک مقاله بروید
3. فرم کامنت را پر کنید
4. "ارسال دیدگاه" کلیک کنید
5. باید پیام موفقیت ببینید

### 3. بررسی ذخیره:
```bash
# مشاهده محتوای فایل JSON
cat data/user_comments.json
```

---

## 🐛 عیب‌یابی

### مشکل 1: "CORS Error"

**علت:** دو origin مختلف (1313 و 8080)

**راه‌حل:** ✅ قبلاً اضافه شده
```php
header('Access-Control-Allow-Origin: *');
```

### مشکل 2: "Connection refused"

**علت:** PHP Server اجرا نشده

**راه‌حل:**
```bash
php -S localhost:8080 -t .
```

### مشکل 3: "JSON Parse Error"

**علت:** خروجی اضافی در PHP

**راه‌حل:** ✅ قبلاً با `ob_end_clean()` برطرف شد

### مشکل 4: "Permission denied"

**علت:** مجوز نوشتن روی فایل JSON

**راه‌حل:**
```bash
chmod 666 data/user_comments.json
```

---

## 📝 نکات مهم

### 1. تنظیم ایمیل ادمین:
```php
// در api/comments.php
define('ADMIN_EMAIL', 'davoodya40@gmail.com');
```

### 2. مجوز فایل JSON:
```bash
# Windows (PowerShell)
icacls data\user_comments.json /grant Everyone:F

# Linux/Mac
chmod 666 data/user_comments.json
```

### 3. تنظیم endpoint در JavaScript:
```javascript
// در static/assets/js/comments.js
API_ENDPOINT: 'http://localhost:8080/api/comments.php',
```

---

## 🌐 Production Deployment

### روی سرور واقعی:

1. **Hugo را build کنید:**
```bash
hugo --gc --minify
```

2. **فایل‌ها را آپلود کنید:**
```
public/           → Root سایت
api/              → /api/
data/             → /data/
```

3. **Apache/Nginx را تنظیم کنید:**

**Apache (.htaccess):**
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^api/comments$ api/comments.php [L,QSA]
```

**Nginx:**
```nginx
location /api/comments {
    try_files $uri /api/comments.php?$args;
}
```

4. **JavaScript endpoint را تغییر دهید:**
```javascript
API_ENDPOINT: '/api/comments.php',  // حذف localhost:8080
```

---

## 🎯 چک‌لیست قبل از Production

- [ ] ایمیل ادمین تنظیم شد
- [ ] مجوز فایل JSON صحیح است
- [ ] Hugo build موفق بود
- [ ] API endpoint درست تنظیم شد
- [ ] تست ارسال کامنت
- [ ] تست پنل ادمین
- [ ] backup از user_comments.json

---

## 📊 معماری

```
┌─────────────────────────────────────┐
│  Browser                             │
│  http://localhost:1313               │
└───────────────┬─────────────────────┘
                │
                │ HTML/CSS/JS
                │
┌───────────────▼─────────────────────┐
│  Hugo Server (Port 1313)             │
│  - Serve static files                │
│  - Hot reload                        │
└──────────────────────────────────────┘

┌─────────────────────────────────────┐
│  Browser                             │
└───────────────┬─────────────────────┘
                │
                │ AJAX (fetch)
                │
┌───────────────▼─────────────────────┐
│  PHP Server (Port 8080)              │
│  /api/comments.php                   │
│  - GET: Retrieve comments            │
│  - POST: Save comments               │
└───────────────┬─────────────────────┘
                │
                │ Read/Write
                │
┌───────────────▼─────────────────────┐
│  data/user_comments.json             │
└──────────────────────────────────────┘
```

---

## 🎉 خلاصه

### Development:
```bash
# یک دستور:
.\start-dev-server.ps1

# یا دو ترمینال:
php -S localhost:8080 -t .    # Terminal 1
hugo server -D                 # Terminal 2
```

### آدرس‌ها:
- وبسایت: http://localhost:1313
- API: http://localhost:8080/api/comments.php
- ادمین: http://localhost:8080/api/admin.php

### Production:
- فایل‌ها را build و deploy کنید
- endpoint را به `/api/comments.php` تغییر دهید
- مجوزها را تنظیم کنید

---

**🚀 حالا آماده استفاده است!**
