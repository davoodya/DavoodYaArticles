# 💬 سیستم کامنت - راهنمای کامل

## 🎯 خلاصه سریع

**پسورد پنل ادمین:** `admin123`

**راه‌اندازی:**
```bash
start-server.bat
```

**پنل ادمین:**
```
http://localhost:1313/api/admin.php
```

---

## ✅ مشکلات حل شده

### 1. خطای JSON Parse ✅
- Frontend اصلاح شد
- مدیریت خطا بهبود یافت
- Console logging اضافه شد

### 2. پسورد پنل ادمین ✅
- سیستم ورود اضافه شد
- پسورد پیش‌فرض: `admin123`
- Session management پیاده‌سازی شد

---

## 📁 فایل‌های مهم

### تنظیمات
```
api/config.php
```
**محتوا:**
- پسورد ادمین
- ایمیل ادمین
- تنظیمات امنیتی

### API Backend
```
api/comments.php      - ثبت و دریافت کامنت
api/admin.php         - پنل مدیریت
api/admin_save.php    - ذخیره تغییرات
```

### Frontend
```
static/assets/js/comments.js
```

### Storage
```
data/user_comments.json
```

---

## 🔧 تغییر تنظیمات

### تغییر پسورد ادمین

**فایل:** `api/config.php`

```php
define('ADMIN_PASSWORD', 'your-new-password');
```

### تغییر ایمیل ادمین

**فایل:** `api/config.php`

```php
define('ADMIN_EMAIL', 'your-email@example.com');
```

**توجه:** کامنت‌های این ایمیل به صورت خودکار تایید می‌شوند.

---

## 🚀 استفاده

### 1. راه‌اندازی سرور

```bash
start-server.bat
```

**یا دستی:**
```bash
hugo
cd public
php -S localhost:1313
```

### 2. ثبت کامنت

1. به مقاله بروید
2. فرم را پر کنید
3. ارسال کنید

**کاربر عادی:**
- کامنت در انتظار تایید می‌ماند

**ادمین (davoodya40@gmail.com):**
- کامنت فوراً نمایش داده می‌شود

### 3. مدیریت کامنت‌ها

**پنل ادمین:**
```
http://localhost:1313/api/admin.php
```

**ورود:**
- پسورد: `admin123`

**عملیات:**
- ✅ مشاهده کامنت‌ها
- ✅ تایید کامنت
- ✅ رد کامنت
- ✅ حذف کامنت
- ✅ فیلتر بر اساس وضعیت

---

## 🔒 امنیت

### پسورد
- پسورد در `api/config.php` ذخیره می‌شود
- Session-based authentication
- باید پسورد پیش‌فرض را تغییر دهید

### ایمیل ادمین
- فقط این ایمیل auto-approve می‌شود
- سایر کامنت‌ها نیاز به تایید دارند

### Validation
- Sanitization ورودی‌ها
- Validation ایمیل و URL
- محدودیت طول کامنت (10-2000 کاراکتر)
- Rate limiting (Frontend)

---

## 🐛 عیب‌یابی

### کامنت ذخیره نمی‌شود

**بررسی:**
1. فایل `data/user_comments.json` وجود دارد؟
2. مجوز نوشتن دارد؟

**راه‌حل:**
```bash
# Windows
icacls data\user_comments.json /grant Everyone:F
```

### خطای JSON

**بررسی Console:**
1. F12 → Console
2. خطا را بخوانید
3. Response text را بررسی کنید

**راه‌حل:**
- بررسی کنید که PHP اجرا شده
- بررسی کنید که فایل `api/comments.php` در دسترس است

### پنل ادمین باز نمی‌شود

**بررسی:**
1. سرور PHP اجرا شده؟
2. آدرس صحیح است؟

**آدرس صحیح:**
```
http://localhost:1313/api/admin.php
```

### پسورد کار نمی‌کند

**بررسی:**
1. پسورد پیش‌فرض: `admin123`
2. فایل `api/config.php` را بررسی کنید
3. سرور را restart کنید

---

## 📊 فلوچارت سیستم

```
User Browser
    ↓
Form Submission
    ↓
static/assets/js/comments.js
    ↓
POST /api/comments.php
    ↓
Validate & Sanitize
    ↓
Check Admin Email?
    ├─ YES → confirmed: true
    └─ NO  → confirmed: false
    ↓
Save to data/user_comments.json
    ↓
Return JSON Response
    ↓
Display Success Message
    ↓
Reload Comments (only confirmed)
```

---

## 📝 مثال JSON

### ساختار فایل `data/user_comments.json`

```json
{
  "comments": [
    {
      "id": "comment_65c3f8b4e1234_1707738000",
      "article_slug": "network-basics",
      "name": "John Doe",
      "email": "john@example.com",
      "website": "https://example.com",
      "comment": "عالی بود!",
      "created_at": "2026-02-12 14:30:00",
      "confirmed": false,
      "ip_address": "127.0.0.1"
    },
    {
      "id": "comment_65c3f8b4e5678_1707738001",
      "article_slug": "network-basics",
      "name": "Admin",
      "email": "davoodya40@gmail.com",
      "website": "",
      "comment": "ممنون از نظرتون",
      "created_at": "2026-02-12 14:31:00",
      "confirmed": true,
      "ip_address": "127.0.0.1"
    }
  ]
}
```

---

## 🎨 ویژگی‌ها

### Frontend
- ✅ Form validation (real-time)
- ✅ Rate limiting (3 comments/minute)
- ✅ Honeypot anti-spam
- ✅ Success/error messages
- ✅ Auto form reset
- ✅ Cache (5 minutes)

### Backend
- ✅ Input sanitization
- ✅ Email validation
- ✅ URL validation
- ✅ Auto-approval for admin
- ✅ JSON storage
- ✅ CORS headers

### Admin Panel
- ✅ Password protection
- ✅ Session management
- ✅ Real-time statistics
- ✅ Filter by status
- ✅ Approve/reject/delete
- ✅ Auto-refresh (30s)

---

## 📚 مستندات مرتبط

- `COMMENTS_QUICK_FIX.md` - راهنمای سریع رفع مشکلات
- `COMMENTS_SYSTEM_COMPLETE.md` - مستندات کامل
- `COMMENTS_VALIDATION_CHECKLIST.md` - چک‌لیست تست

---

## ✅ چک‌لیست آماده‌سازی Production

### قبل از Deploy
- [ ] پسورد پیش‌فرض را تغییر دهید
- [ ] ایمیل ادمین را بررسی کنید
- [ ] مجوز فایل JSON را بررسی کنید
- [ ] Backup از `data/user_comments.json` بگیرید

### بعد از Deploy
- [ ] تست ثبت کامنت
- [ ] تست auto-approval ادمین
- [ ] تست پنل مدیریت
- [ ] تست تایید/رد/حذف

---

## 🆘 پشتیبانی

### لاگ‌ها
- **Browser Console:** F12 → Console
- **Network Tab:** F12 → Network
- **PHP Errors:** در terminal که سرور اجرا شده

### Debug Mode
برای دیدن جزئیات بیشتر، Console browser را باز کنید.

---

## 📞 تماس

- **ایمیل ادمین:** davoodya40@gmail.com
- **پسورد پیش‌فرض:** admin123 (حتماً تغییر دهید!)

---

**موفق باشید! 🚀✨**
