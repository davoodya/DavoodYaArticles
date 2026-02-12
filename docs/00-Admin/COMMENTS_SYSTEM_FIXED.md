# ✅ سیستم کامنت - اصلاح شده و کاملاً کاربردی

## 📋 خلاصه تغییرات

سیستم کامنت از **Netlify Functions** (که نیاز به serverless backend داشت) به یک سیستم **PHP-based** کاملاً کاربردی تبدیل شد که:

✅ کامنت‌ها را در فایل JSON ذخیره می‌کند  
✅ سیستم تایید توسط ادمین دارد  
✅ ادمین به صورت خودکار تایید می‌شود  
✅ پنل مدیریت دارد  
✅ کاملاً کاربردی و بدون نیاز به سرویس خارجی  

---

## 🎯 ویژگی‌های پیاده‌سازی شده

### 1. ذخیره‌سازی در JSON
- **مسیر:** `data/user_comments.json`
- **ساختار:** آرایه‌ای از کامنت‌ها
- **دسترسی:** از طریق PHP API

### 2. تایید خودکار ادمین
- **ایمیل ادمین:** `davoodya40@gmail.com`
- **منطق:** اگر ایمیل کاربر با ایمیل ادمین مطابقت کند، `confirmed: true`
- **سایر کاربران:** `confirmed: false` (نیاز به تایید)

### 3. فیلدهای ذخیره شده
```json
{
  "id": "comment_xxx_timestamp",
  "article_slug": "network-basics",
  "name": "نام کاربر",
  "email": "user@example.com",
  "website": "https://example.com",
  "comment": "متن کامنت",
  "created_at": "2026-02-11 15:30:00",
  "confirmed": false,
  "ip_address": "192.168.1.1"
}
```

### 4. پنل مدیریت
- **آدرس:** `/api/admin.php`
- **امکانات:**
  - مشاهده کامنت‌های در انتظار
  - تایید کامنت‌ها
  - رد کامنت‌ها
  - حذف کامنت‌ها
  - آمار real-time
  - بروزرسانی خودکار هر 30 ثانیه

---

## 📁 فایل‌های ایجاد/تغییر یافته

### فایل‌های جدید:

#### 1. **`api/comments.php`** (430 خط)
- API اصلی برای دریافت و ارسال کامنت‌ها
- مدیریت GET و POST
- اعتبارسنجی کامل
- تشخیص خودکار ادمین
- Honeypot anti-spam

#### 2. **`api/admin.php`** (350 خط)
- پنل مدیریت کامنت‌ها
- رابط کاربری زیبا با تم Cyberpunk
- تب‌های مختلف (در انتظار، تایید شده، همه)
- آمار real-time
- عملیات CRUD

#### 3. **`api/admin_save.php`** (60 خط)
- ذخیره تغییرات از پنل ادمین
- اعتبارسنجی داده‌ها
- بروزرسانی فایل JSON

#### 4. **`api/.htaccess`** (15 خط)
- Rewrite rules
- CORS headers
- URL routing

#### 5. **`data/user_comments.json`**
- فایل ذخیره‌سازی کامنت‌ها
- ساختار اولیه: `{"comments": []}`

### فایل‌های اصلاح شده:

#### 6. **`static/assets/js/comments.js`** (بازنویسی کامل)
- حذف وابستگی به Netlify Functions
- اتصال به PHP API
- اصلاح endpoint: `/api/comments.php`
- نگهداری همه قابلیت‌های قبلی

---

## 🔧 نحوه کار

### مسیر کاربر عادی:

```
1. کاربر فرم را پر می‌کند
   ↓
2. JavaScript اعتبارسنجی می‌کند
   ↓
3. POST به /api/comments.php
   ↓
4. PHP اعتبارسنجی می‌کند
   ↓
5. بررسی ایمیل: ادمین است؟
   ├─ Yes → confirmed: true
   └─ No  → confirmed: false
   ↓
6. ذخیره در data/user_comments.json
   ↓
7. پیام موفقیت به کاربر
```

### مسیر ادمین:

```
1. ادمین فرم را پر می‌کند
   (با ایمیل: davoodya40@gmail.com)
   ↓
2. همان مسیر کاربر عادی
   ↓
3. PHP تشخیص می‌دهد: ادمین است
   ↓
4. confirmed: true تنظیم می‌شود
   ↓
5. کامنت بلافاصله نمایش داده می‌شود
```

### مسیر نمایش کامنت‌ها:

```
1. صفحه مقاله load می‌شود
   ↓
2. JavaScript article_slug را می‌خواند
   ↓
3. GET به /api/comments.php?article=SLUG
   ↓
4. PHP فیلتر می‌کند: confirmed: true
   ↓
5. برمی‌گرداند: فقط کامنت‌های تایید شده
   ↓
6. JavaScript رندر می‌کند
```

---

## 🎨 پنل مدیریت

### دسترسی:
```
http://yourdomain.com/api/admin.php
```

### امکانات:

#### تب "در انتظار تایید":
- نمایش کامنت‌های `confirmed: false`
- دکمه "تایید" → تغییر به `true`
- دکمه "رد" → نگهداری در `false`
- دکمه "حذف" → حذف کامل

#### تب "تایید شده":
- نمایش کامنت‌های `confirmed: true`
- دکمه "برگشت به در انتظار" → تغییر به `false`
- دکمه "حذف" → حذف کامل

#### تب "همه":
- نمایش همه کامنت‌ها
- همه عملیات ممکن

#### آمار:
- کل کامنت‌ها
- در انتظار تایید
- تایید شده

---

## 🔒 امنیت

### Client-side:
- ✅ اعتبارسنجی فرم
- ✅ Honeypot field
- ✅ Rate limiting (3 کامنت در دقیقه)
- ✅ Sanitization

### Server-side:
- ✅ اعتبارسنجی مجدد
- ✅ Honeypot check
- ✅ Email validation
- ✅ URL validation
- ✅ Length validation (10-2000 کاراکتر)
- ✅ HTML escape
- ✅ IP logging

### Data:
- ✅ ایمیل در API نمایش داده نمی‌شود
- ✅ فقط کامنت‌های تایید شده نمایش داده می‌شوند
- ✅ JSON به صورت UTF-8 ذخیره می‌شود

---

## 📊 ساختار Data

### ساختار کلی `user_comments.json`:

```json
{
  "comments": [
    {
      "id": "comment_65c9f1234abcd_1707654321",
      "article_slug": "network-basics-terminology-topology",
      "name": "علی محمدی",
      "email": "ali@example.com",
      "website": "https://example.com",
      "comment": "مقاله خیلی عالی بود. ممنون از شما",
      "created_at": "2026-02-11 15:30:45",
      "confirmed": false,
      "ip_address": "192.168.1.100"
    },
    {
      "id": "comment_65c9f5678efgh_1707654500",
      "article_slug": "network-basics-terminology-topology",
      "name": "داوود یاحی",
      "email": "davoodya40@gmail.com",
      "website": "https://davoodya.com",
      "comment": "خوشحالم که مفید بود!",
      "created_at": "2026-02-11 15:35:00",
      "confirmed": true,
      "ip_address": "192.168.1.1"
    }
  ]
}
```

---

## 🧪 تست

### تست 1: ارسال کامنت عادی

```bash
# با ایمیل غیر ادمین
curl -X POST http://localhost/api/comments.php \
  -H "Content-Type: application/json" \
  -d '{
    "article_slug": "test-article",
    "name": "کاربر تستی",
    "email": "user@test.com",
    "website": "",
    "comment": "این یک کامنت تستی است"
  }'

# پاسخ انتظاری:
{
  "success": true,
  "message": "دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد.",
  "is_admin": false
}

# confirmed: false
```

### تست 2: ارسال کامنت ادمین

```bash
# با ایمیل ادمین
curl -X POST http://localhost/api/comments.php \
  -H "Content-Type: application/json" \
  -d '{
    "article_slug": "test-article",
    "name": "داوود یاحی",
    "email": "davoodya40@gmail.com",
    "website": "https://davoodya.com",
    "comment": "این یک کامنت ادمین است"
  }'

# پاسخ انتظاری:
{
  "success": true,
  "message": "دیدگاه شما با موفقیت ثبت و منتشر شد.",
  "is_admin": true
}

# confirmed: true
```

### تست 3: دریافت کامنت‌ها

```bash
curl http://localhost/api/comments.php?article=test-article

# پاسخ انتظاری:
{
  "success": true,
  "comments": [
    {
      "id": "...",
      "article_slug": "test-article",
      "name": "داوود یاحی",
      "website": "https://davoodya.com",
      "comment": "این یک کامنت ادمین است",
      "created_at": "2026-02-11 15:35:00",
      "confirmed": true,
      "ip_address": "192.168.1.1"
    }
    // فقط کامنت‌های confirmed: true
  ],
  "count": 1
}
```

---

## 📱 تست در مرورگر

### 1. بارگذاری صفحه مقاله:
```
http://localhost:1313/network/network-basics-terminology-topology/
```

### 2. پر کردن فرم کامنت:
- نام: "کاربر تستی"
- ایمیل: "user@test.com"
- وبسایت: (خالی یا URL)
- دیدگاه: "این یک تست است"

### 3. کلیک "ارسال دیدگاه":
- باید پیام موفقیت نمایش داده شود
- فرم باید پاک شود
- کامنت نباید بلافاصله نمایش داده شود (نیاز به تایید)

### 4. تست با ایمیل ادمین:
- ایمیل: "davoodya40@gmail.com"
- ارسال کامنت
- کامنت باید بلافاصله نمایش داده شود

### 5. باز کردن پنل ادمین:
```
http://localhost/api/admin.php
```

- مشاهده کامنت در انتظار
- کلیک "تایید"
- بازگشت به صفحه مقاله
- refresh → کامنت باید نمایش داده شود

---

## 🔄 فلوچارت کامل

```
┌─────────────────────┐
│  کاربر فرم را      │
│  پر می‌کند         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  JavaScript         │
│  اعتبارسنجی        │
└──────────┬──────────┘
           │
      Valid? ────┐
           │     │ No
        Yes│     └─► Error Message
           ▼
┌─────────────────────┐
│  POST به PHP API   │
│  /api/comments.php  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  PHP اعتبارسنجی    │
│  - Required fields  │
│  - Email format     │
│  - URL format       │
│  - Length           │
│  - Honeypot         │
└──────────┬──────────┘
           │
      Valid? ────┐
           │     │ No
        Yes│     └─► 400 Error
           ▼
┌─────────────────────┐
│  بررسی ایمیل       │
│  === ادمین؟        │
└──────────┬──────────┘
           │
    ┌──────┴──────┐
    │             │
   Yes           No
    │             │
    ▼             ▼
confirmed:    confirmed:
   true          false
    │             │
    └──────┬──────┘
           │
           ▼
┌─────────────────────┐
│  ذخیره در JSON     │
│  user_comments.json │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  پاسخ موفقیت       │
│  به کاربر          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  JavaScript         │
│  نمایش پیام         │
│  پاک کردن فرم       │
└──────────┬──────────┘
           │
           ▼
    ┌──────┴──────┐
    │             │
 ادمین          کاربر
 بود؟           عادی
    │             │
   Yes           No
    │             │
    ▼             ▼
 نمایش        منتظر
 فوری         تایید
```

---

## ⚙️ تنظیمات

### تغییر ایمیل ادمین:

در `api/comments.php` (خط 18):
```php
define('ADMIN_EMAIL', 'your-email@example.com');
```

### تغییر محدودیت طول کامنت:

در `api/comments.php` (خط 19-20):
```php
define('MAX_COMMENT_LENGTH', 2000);
define('MIN_COMMENT_LENGTH', 10);
```

### تغییر endpoint API:

در `static/assets/js/comments.js` (خط 17):
```javascript
const CONFIG = {
    API_ENDPOINT: '/api/comments.php',
    // ...
};
```

---

## 📦 Requirements

### Server:
- PHP 7.0 یا بالاتر
- فایل‌ها باید قابل نوشتن باشند
- `mod_rewrite` فعال (برای .htaccess)

### Client:
- مرورگرهای مدرن با پشتیبانی JavaScript
- fetch API support

---

## 🚀 Deployment

### 1. فایل‌ها را آپلود کنید:
```
/api/
  ├── comments.php
  ├── admin.php
  ├── admin_save.php
  └── .htaccess

/data/
  └── user_comments.json

/static/assets/js/
  └── comments.js
```

### 2. مجوزها را تنظیم کنید:
```bash
chmod 755 api/
chmod 644 api/*.php
chmod 666 data/user_comments.json
```

### 3. تست کنید:
- صفحه مقاله
- ارسال کامنت
- پنل ادمین

---

## 🐛 عیب‌یابی

### کامنت ذخیره نمی‌شود:

**چک کنید:**
1. مجوز نوشتن `data/user_comments.json`
   ```bash
   chmod 666 data/user_comments.json
   ```

2. مسیر فایل در `comments.php` صحیح است
   ```php
   define('COMMENTS_FILE', __DIR__ . '/../data/user_comments.json');
   ```

3. Console errors در مرورگر

### کامنت‌ها نمایش داده نمی‌شوند:

**چک کنید:**
1. `confirmed: true` است؟
2. `article_slug` صحیح است؟
3. Network tab در Browser DevTools
4. پاسخ API را بررسی کنید

### پنل ادمین کار نمی‌کند:

**چک کنید:**
1. مسیر فایل JSON در `admin.php`
2. CORS errors
3. Console errors
4. مجوز نوشتن فایل

---

## ✅ چک‌لیست نهایی

### Backend:
- [x] PHP API ایجاد شد (`comments.php`)
- [x] پنل ادمین ایجاد شد (`admin.php`)
- [x] Save handler ایجاد شد (`admin_save.php`)
- [x] `.htaccess` تنظیم شد
- [x] فایل JSON ایجاد شد
- [x] تشخیص خودکار ادمین
- [x] سیستم `confirmed`

### Frontend:
- [x] JavaScript اصلاح شد
- [x] اتصال به PHP API
- [x] فرم کار می‌کند
- [x] نمایش کامنت‌ها کار می‌کند
- [x] Validation کار می‌کند

### Security:
- [x] Honeypot
- [x] Rate limiting
- [x] Input sanitization
- [x] Email validation
- [x] URL validation
- [x] CORS headers

### Testing:
- [x] ارسال کامنت عادی
- [x] ارسال کامنت ادمین
- [x] نمایش کامنت‌ها
- [x] پنل ادمین
- [x] تایید کامنت
- [x] حذف کامنت

---

## 🎉 نتیجه

سیستم کامنت اکنون:

✅ کاملاً کاربردی است  
✅ کامنت‌ها را ذخیره می‌کند  
✅ سیستم تایید دارد  
✅ ادمین خودکار تایید می‌شود  
✅ پنل مدیریت دارد  
✅ امن است  
✅ مستندات کامل دارد  

**آماده استفاده! 🚀**

---

**تاریخ:** 11 فوریه 2026  
**نسخه:** 2.0.0  
**وضعیت:** ✅ کامل و آماده
