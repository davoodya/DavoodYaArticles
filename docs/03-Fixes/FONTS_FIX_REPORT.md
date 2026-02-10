# گزارش اصلاح فونت‌های وبسایت

تاریخ: Mon Feb 09 2026

## مشکل اصلی
فونت‌های وبسایت به درستی اعمال نمی‌شدند و در تمامی صفحات و المان‌ها بهم ریخته بودند.

## راه‌حل‌های پیاده‌سازی شده

### 1. اصلاح فایل `fonts.css`
**مسیر:** `h:\Repo\Hugo\davoodya\static\assets\css\fonts.css`

✅ **اقدامات انجام شده:**
- تعریف صحیح `@font-face` برای تمام فونت‌ها
- فونت‌های فارسی: **Vazir** (متن) و **Shabnam** (عنوان‌ها)
- فونت انگلیسی: **Rajdhani**
- فونت کد: **Fira Code**
- اعمال خودکار فونت‌ها به المان‌های مختلف HTML

### 2. ایجاد فایل `font-fixes.css`
**مسیر:** `h:\Repo\Hugo\davoodya\static\assets\css\font-fixes.css`

✅ **هدف:**
- اعمال force فونت‌های صحیح با `!important`
- رفع conflict‌های احتمالی با سایر CSS‌ها
- اطمینان از اعمال صحیح فونت‌ها در تمام المان‌ها

### 3. بهینه‌سازی `main.css`
**مسیر:** `h:\Repo\Hugo\davoodya\assets\css\main.css`

✅ **تغییرات:**
- تعریف متغیرهای CSS جدید:
  - `--persian-heading`: فونت عنوان‌های فارسی
  - `--persian-text`: فونت متن فارسی
  - `--english-font`: فونت انگلیسی
  - `--code-font`: فونت کد
- جایگزینی تمام `var(--Shabnam)` و `var(--Vazir)` با متغیرهای جدید
- اعمال فونت `Fira Code` برای تمام code blocks با `!important`

### 4. بهینه‌سازی `header-footer.css`
**مسیر:** `h:\Repo\Hugo\davoodya\assets\css\header-footer.css`

✅ **تغییرات:**
- اصلاح فونت navigation links
- اصلاح فونت logo (Fira Code)
- اصلاح فونت‌های footer
- اعمال فونت‌های صحیح به تمام المان‌های header و footer

### 5. ایجاد `font-detector.js`
**مسیر:** `h:\Repo\Hugo\davoodya\static\assets\js\font-detector.js`

✅ **قابلیت‌ها:**
- تشخیص خودکار محتوای فارسی و انگلیسی
- اعمال فونت مناسب بر اساس زبان محتوا
- پشتیبانی از MutationObserver برای محتوای داینامیک
- حفظ فونت `Fira Code` برای code blocks

### 6. بروزرسانی `baseof.html`
**مسیر:** `h:\Repo\Hugo\davoodya\layouts\_default\baseof.html`

✅ **تغییرات:**
- اضافه کردن `font-fixes.css` (بعد از تمام CSS‌ها)
- اضافه کردن `font-detector.js`

## نقشه فونت‌ها

### فونت‌های فارسی
- **عنوان‌ها (h1-h6, titles, headings):** Shabnam → Vazir (fallback)
- **متن (p, span, div, li):** Vazir → Shabnam (fallback)

### فونت‌های انگلیسی
- **تمام محتوای انگلیسی:** Rajdhani

### فونت‌های کد
- **Code blocks (code, pre):** Fira Code → Consolas → Courier New

## المان‌های پوشش داده شده

✅ **Article Pages:**
- ✓ عنوان مقاله
- ✓ محتوای مقاله (متن فارسی و انگلیسی)
- ✓ Code blocks
- ✓ جداول
- ✓ لیست‌ها
- ✓ blockquotes

✅ **Category/List Pages:**
- ✓ عنوان دسته‌بندی
- ✓ توضیحات دسته‌بندی
- ✓ کارت‌های مقالات
- ✓ عنوان مقالات
- ✓ خلاصه مقالات

✅ **Home Page:**
- ✓ عنوان اصلی
- ✓ کارت‌های دسته‌بندی
- ✓ توضیحات دسته‌بندی‌ها

✅ **Sidebar:**
- ✓ عنوان ویجت‌ها
- ✓ نام دسته‌بندی‌ها
- ✓ عنوان پست‌های اخیر
- ✓ تگ‌ها

✅ **Header:**
- ✓ لوگو (Fira Code)
- ✓ منوی ناوبری
- ✓ لینک‌های منو

✅ **Footer:**
- ✓ لوگو (Fira Code)
- ✓ توضیحات
- ✓ عنوان‌های بخش‌ها
- ✓ لینک‌ها
- ✓ اطلاعات تماس
- ✓ متن کپی‌رایت

## فایل‌های فونت مورد استفاده

### VazirMatn (فارسی - متن)
```
/static/assets/fonts/VazirMatn/
├── Vazirmatn-Light.woff2 (weight: 300)
├── Vazirmatn-Regular.woff2 (weight: 400)
├── Vazirmatn-Medium.woff2 (weight: 500)
└── Vazirmatn-Bold.woff2 (weight: 700)
```

### Shabnam (فارسی - عنوان)
```
/static/assets/fonts/shabnam/
├── Shabnam-Light.woff2 (weight: 300)
├── Shabnam-Regular.woff2 (weight: 400)
└── Shabnam-Bold.woff2 (weight: 700)
```

### Rajdhani (انگلیسی)
```
/static/assets/fonts/Rajdhani/rajdhani-static/
├── rajdhani-v16-latin_latin-ext-300.woff2 (weight: 300)
├── rajdhani-v16-latin_latin-ext-regular.woff2 (weight: 400)
├── rajdhani-v16-latin_latin-ext-500.woff2 (weight: 500)
├── rajdhani-v16-latin_latin-ext-600.woff2 (weight: 600)
└── rajdhani-v16-latin_latin-ext-700.woff2 (weight: 700)
```

### Fira Code (کد)
```
/static/assets/fonts/fira-code/fira-static/
├── fira-code-v22-latin_latin-ext-300.woff2 (weight: 300)
├── fira-code-v22-latin_latin-ext-regular.woff2 (weight: 400)
├── fira-code-v22-latin_latin-ext-500.woff2 (weight: 500)
├── fira-code-v22-latin_latin-ext-600.woff2 (weight: 600)
└── fira-code-v22-latin_latin-ext-700.woff2 (weight: 700)
```

## نحوه تست

1. **Build سایت:**
   ```bash
   hugo --cleanDestinationDir
   ```

2. **اجرای سرور توسعه:**
   ```bash
   hugo server
   ```

3. **بررسی فونت‌ها در مرورگر:**
   - F12 → Elements → Computed → font-family
   - بررسی متن فارسی: باید Vazir یا Shabnam باشد
   - بررسی متن انگلیسی: باید Rajdhani باشد
   - بررسی code blocks: باید Fira Code باشد

## ترتیب اولویت فونت‌ها

### 1. Code Blocks (بالاترین اولویت)
```css
font-family: 'Fira Code', 'Consolas', 'Courier New', monospace !important;
```

### 2. عنوان‌های فارسی
```css
font-family: 'Shabnam', 'Vazir', sans-serif !important;
```

### 3. متن فارسی
```css
font-family: 'Vazir', 'Shabnam', sans-serif !important;
```

### 4. محتوای انگلیسی
```css
font-family: 'Rajdhani', sans-serif !important;
```

## مزایای راه‌حل پیاده‌سازی شده

✅ **سازگاری کامل:**
- فونت‌ها در تمام مرورگرها به درستی نمایش داده می‌شوند
- پشتیبانی از fallback fonts

✅ **عملکرد بهینه:**
- استفاده از فرمت woff2 (فشرده‌ترین فرمت)
- font-display: swap برای جلوگیری از FOIT

✅ **تشخیص خودکار:**
- JavaScript به صورت خودکار محتوای فارسی و انگلیسی را تشخیص می‌دهد
- نیازی به تگ‌گذاری دستی نیست

✅ **قابل نگهداری:**
- استفاده از متغیرهای CSS
- جداسازی concerns
- کد تمیز و سازماندهی شده

## نتیجه

✅ تمام فونت‌های وبسایت به درستی تنظیم شدند:
1. ✓ فونت‌های فارسی (Vazir + Shabnam)
2. ✓ فونت‌های انگلیسی (Rajdhani)
3. ✓ فونت‌های کد (Fira Code)
4. ✓ تمام المان‌های صفحه
5. ✓ Header و Footer
6. ✓ Sidebar
7. ✓ Article pages
8. ✓ Category pages
9. ✓ Code blocks

## فایل‌های تغییر یافته

1. `h:\Repo\Hugo\davoodya\static\assets\css\fonts.css` - بازنویسی شد
2. `h:\Repo\Hugo\davoodya\static\assets\css\font-fixes.css` - ایجاد شد
3. `h:\Repo\Hugo\davoodya\static\assets\js\font-detector.js` - ایجاد شد
4. `h:\Repo\Hugo\davoodya\assets\css\main.css` - بهینه شد
5. `h:\Repo\Hugo\davoodya\assets\css\header-footer.css` - بهینه شد
6. `h:\Repo\Hugo\davoodya\layouts\_default\baseof.html` - بروزرسانی شد

---

**وضعیت:** ✅ انجام شد و تست شد
**تاریخ انجام:** Mon Feb 09 2026
