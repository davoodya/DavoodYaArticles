# راهنمای برطرف‌سازی مشکل CSS Files

تاریخ: Mon Feb 09 2026

## 🔴 مشکل

شما فایل‌های CSS را در `/static/assets/css/` ویرایش می‌کردید، اما:
- تغییرات در real-time اعمال می‌شدند
- بعد از restart کردن `hugo server`، تغییرات از بین می‌رفتند
- سایت دوباره به حالت قبلی برمی‌گشت

## 🔍 علت مشکل

Hugo دو سیستم مختلف برای مدیریت فایل‌های static دارد:

### 1. پوشه `/assets/` (Hugo Pipes)
- فایل‌ها توسط Hugo **پردازش** می‌شوند
- می‌توانند minify، bundle و optimize شوند
- این فایل‌ها به `public/` کپی می‌شوند **بعد از پردازش**

### 2. پوشه `/static/`
- فایل‌ها **مستقیماً** و **بدون تغییر** به `public/` کپی می‌شوند
- هیچ پردازشی روی آن‌ها انجام نمی‌شود

## 🚨 مشکل شما

شما **دو نسخه** از فایل‌های CSS داشتید:

```
/assets/css/main.css         ← نسخه اصلی (که Hugo از آن استفاده می‌کند)
/static/assets/css/main.css  ← نسخه دوم (که شما ویرایش می‌کردید)
```

**جریان کار:**
1. شما `/static/assets/css/main.css` را ویرایش می‌کردید
2. Hugo فایل را از `/static/` به `public/` کپی می‌کرد (تغییرات موقتاً قابل مشاهده بودند)
3. Hugo restart می‌شد
4. Hugo فایل از `/assets/css/main.css` را می‌خواند و پردازش می‌کرد
5. فایل پردازش شده `/assets/css/main.css` به `public/` منتقل می‌شد و فایل `/static/` را overwrite می‌کرد
6. تغییرات شما از بین می‌رفتند! 😢

## ✅ راه‌حل

### مرحله 1: حذف فایل‌های تکراری در `/static/`

تمام فایل‌های CSS که در `/assets/css/` موجود بودند، از `/static/assets/css/` حذف شدند:

```bash
❌ حذف شد: /static/assets/css/main.css
❌ حذف شد: /static/assets/css/fonts.css
❌ حذف شد: /static/assets/css/font-fixes.css
❌ حذف شد: /static/assets/css/header-footer.css
❌ حذف شد: /static/assets/css/search.css
```

### مرحله 2: استفاده از `/assets/css/` به عنوان منبع اصلی

حالا تمام فایل‌های CSS در `/assets/css/` قرار دارند:

```
✅ /assets/css/main.css
✅ /assets/css/fonts.css
✅ /assets/css/font-fixes.css
✅ /assets/css/header-footer.css
✅ /assets/css/search.css
✅ /assets/css/custom-pages.css
```

### مرحله 3: تنظیم `baseURL` در `hugo.toml`

**قبل:**
```toml
baseURL = "https://davoodya.ir/"
relativeURLs = false
canonifyURLs = true
```

**بعد (برای development):**
```toml
baseURL = "/"
relativeURLs = true
canonifyURLs = false
```

این تنظیم باعث می‌شود که سایت هم در `http://127.0.0.1:1313/` و هم در `https://davoodya.ir/` به درستی کار کند.

## 📝 قوانین مهم

### ✅ چه زمانی از `/assets/` استفاده کنیم؟

از `/assets/` برای فایل‌هایی استفاده کنید که:
- نیاز به پردازش دارند (CSS, JS, SCSS, etc.)
- می‌خواهید minify یا bundle شوند
- ممکن است در آینده تغییر کنند

**مثال:**
```
/assets/css/main.css
/assets/js/app.js
/assets/scss/styles.scss
```

### ✅ چه زمانی از `/static/` استفاده کنیم؟

از `/static/` برای فایل‌هایی استفاده کنید که:
- نباید پردازش شوند
- باید دقیقاً همان‌طور که هستند کپی شوند
- تصاویر، فونت‌ها، فایل‌های PDF، etc.

**مثال:**
```
/static/assets/fonts/Vazir.woff2
/static/assets/images/logo.png
/static/robots.txt
```

## 🔄 نحوه ویرایش صحیح CSS

از این به بعد، برای ویرایش CSS:

### ❌ اشتباه:
```bash
# ویرایش کردن /static/assets/css/main.css
```

### ✅ صحیح:
```bash
# ویرایش کردن /assets/css/main.css
```

## 🚀 نحوه اجرای سایت

### Development (توسعه محلی):
```bash
hugo server -D
```

سایت در `http://localhost:1313/` قابل دسترسی است.

### Production Build:
```bash
hugo --cleanDestinationDir
```

فایل‌های آماده در `/public/` قرار می‌گیرند.

### تغییر baseURL برای Production:

قبل از deploy کردن، `hugo.toml` را ویرایش کنید:

```toml
baseURL = "https://davoodya.ir/"
relativeURLs = false
canonifyURLs = true
```

بعد build کنید:
```bash
hugo --cleanDestinationDir
```

## 📊 ساختار نهایی فایل‌ها

```
davoodya/
├── assets/
│   ├── css/
│   │   ├── main.css              ← فایل اصلی CSS (ویرایش کنید)
│   │   ├── fonts.css             ← تعاریف فونت‌ها
│   │   ├── font-fixes.css        ← اصلاحات فونت
│   │   ├── header-footer.css     ← استایل header/footer
│   │   ├── search.css            ← استایل search
│   │   └── custom-pages.css      ← استایل صفحات custom
│   └── fonts/                    ← فونت‌ها (نگهداری)
│
├── static/
│   └── assets/
│       ├── fonts/                ← فونت‌ها (استفاده در production)
│       ├── images/               ← تصاویر
│       └── js/                   ← JavaScript files
│
├── layouts/
│   └── _default/
│       └── baseof.html           ← لینک CSS files
│
├── public/                       ← خروجی build (تولید خودکار)
│
└── hugo.toml                     ← تنظیمات Hugo
```

## 🎯 خلاصه

1. **همیشه فایل‌های CSS را در `/assets/css/` ویرایش کنید**
2. **هرگز فایل‌های CSS را در `/static/` قرار ندهید** (مگر اینکه بخواهید مستقیماً کپی شوند)
3. **فونت‌ها را در `/static/assets/fonts/` نگه دارید** (چون نیازی به پردازش ندارند)
4. **baseURL را برای development و production متفاوت تنظیم کنید**
5. **بعد از هر تغییر در CSS، Hugo server را restart کنید** (یا از live reload استفاده کنید)

## ✅ وضعیت فعلی

- ✅ تمام فایل‌های تکراری حذف شدند
- ✅ فایل‌های CSS در مسیر صحیح قرار گرفتند (`/assets/css/`)
- ✅ تغییرات شما در `main.css` حفظ شدند:
  - `grid-template-columns: repeat(1, 1fr)` در `.articles-grid`
  - `overflow-x` کامنت شده در `.main-content`
  - `max-height` و `overflow-y` کامنت شده در `.sidebar`
- ✅ baseURL برای development تنظیم شد
- ✅ سایت با موفقیت build شد

## 🔧 تست

برای اطمینان از درست بودن تغییرات:

1. سایت را اجرا کنید:
   ```bash
   hugo server -D
   ```

2. مرورگر را باز کنید: `http://localhost:1313/`

3. F12 را فشار دهید → Elements → Computed → بررسی کنید که:
   - فونت‌ها صحیح هستند
   - `.articles-grid` دارای `grid-template-columns: 1fr` است
   - sidebar بدون محدودیت ارتفاع است

4. اگر تغییری در CSS می‌خواهید:
   - فایل `/assets/css/main.css` را ویرایش کنید
   - ذخیره کنید (Hugo به صورت خودکار rebuild می‌کند)
   - صفحه را refresh کنید

---

**نکته مهم:** همیشه قبل از deploy کردن به production، `hugo.toml` را بررسی کنید و `baseURL` را به `https://davoodya.ir/` برگردانید! 🚀
