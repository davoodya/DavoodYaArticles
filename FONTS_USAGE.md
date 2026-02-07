# راهنمای استفاده از فونت‌ها

## 📖 فهرست

- [فونت‌های نصب شده](#فونت‌های-نصب-شده)
- [نحوه استفاده](#نحوه-استفاده)
- [مثال‌های عملی](#مثال‌های-عملی)
- [بهینه‌سازی](#بهینه‌سازی)

---

## 🎨 فونت‌های نصب شده

### فونت‌های فارسی

#### 1. Vazir (وزیرمتن)
- **مسیر:** `assets/fonts/VazirMatn/`
- **استفاده:** متن اصلی، پاراگراف‌ها، محتوای عادی
- **وزن‌ها:** 
  - Light (300)
  - Regular (400)
  - Medium (500)
  - Bold (700)

**خصوصیات:**
- خوانایی عالی در اندازه‌های مختلف
- مناسب برای متن‌های طولانی
- پشتیبانی کامل از حروف فارسی و عربی

#### 2. Shabnam (شبنم)
- **مسیر:** `assets/fonts/shabnam/`
- **استفاده:** عنوان‌ها، تیترها، دکمه‌ها
- **وزن‌ها:**
  - Light (300)
  - Regular (400)
  - Bold (700)

**خصوصیات:**
- طراحی مدرن و جذاب
- مناسب برای عنوان‌ها
- قابلیت خوانش بالا در اندازه‌های بزرگ

#### 3. Sahel (ساحل)
- **مسیر:** `assets/fonts/sahel/`
- **استفاده:** اختیاری - برای تنوع در طراحی
- **وزن‌ها:** 300, 400, 700

#### 4. Yekan (ایران یکان)
- **مسیر:** `assets/fonts/IRANYekanX/`
- **استفاده:** اختیاری - مناسب برای UI
- **وزن‌ها:** 300, 400, 700

### فونت‌های لاتین

#### 1. Fira Code
- **مسیر:** `assets/fonts/fira-code/`
- **استفاده:** بلوک‌های کد، monospace
- **وزن‌ها:** 300, 400, 500, 600, 700

**خصوصیات:**
- Font ligatures برای کد
- خوانایی عالی در کد
- طراحی مخصوص terminal

#### 2. Rajdhani
- **مسیر:** `assets/fonts/Rajdhani/`
- **استفاده:** محتوای لاتین، UI
- **وزن‌ها:** 300, 400, 500, 600, 700

**خصوصیات:**
- طراحی فوتوریستی
- مناسب برای تم Cyberpunk
- خوانایی خوب

---

## 💻 نحوه استفاده

### در CSS

```css
/* استفاده از متغیرهای از پیش تعریف شده */
.my-text {
    font-family: var(--Vazir);
}

.my-title {
    font-family: var(--Shabnam);
}

.my-code {
    font-family: var(--terminal-font);
}

/* استفاده مستقیم */
.custom-class {
    font-family: 'Shabnam', sans-serif;
    font-weight: 700;
}
```

### متغیرهای CSS موجود

```css
:root {
    --Vazir: 'Vazir', sans-serif;
    --Shabnam: 'Shabnam', sans-serif;
    --Sahel: 'Sahel', sans-serif;
    --Yekan: 'Yekan', sans-serif;
    --terminal-font: 'Fira Code', 'Courier New', monospace;
    --content-font: 'Rajdhani', 'Segoe UI', sans-serif;
}
```

---

## 📝 مثال‌های عملی

### مثال 1: کارت با فونت‌های مختلف

```css
.card {
    font-family: var(--Vazir);  /* متن اصلی */
}

.card-title {
    font-family: var(--Shabnam);  /* عنوان */
    font-weight: 700;
}

.card-code {
    font-family: var(--terminal-font);  /* کد */
}
```

### مثال 2: مقاله با فونت‌های بهینه

```css
.article-content {
    font-family: var(--Vazir);
    font-size: 1.05rem;
    line-height: 1.9;
}

.article-content h1,
.article-content h2 {
    font-family: var(--Shabnam);
    font-weight: 700;
}

.article-content code {
    font-family: var(--terminal-font);
}
```

### مثال 3: دکمه با فونت سفارشی

```css
.btn {
    font-family: var(--Shabnam);
    font-weight: 700;
    font-size: 0.95rem;
    letter-spacing: 0.5px;
}
```

---

## 🎯 استفاده در مقالات

### عنوان‌ها (Headings)

```markdown
# این عنوان با فونت Shabnam نمایش داده می‌شود
## این هم همینطور
### و این هم
```

**CSS مربوطه:**
```css
.article-content h1,
.article-content h2,
.article-content h3 {
    font-family: var(--Shabnam);
}
```

### متن عادی (Paragraphs)

```markdown
این یک پاراگراف متن است که با فونت Vazir نمایش داده می‌شود.
این فونت برای خوانایی بالا طراحی شده است.
```

**CSS مربوطه:**
```css
.article-content p {
    font-family: var(--Vazir);
}
```

### بلوک‌های کد (Code Blocks)

```markdown
\```python
def hello():
    print("این کد با فونت Fira Code نمایش داده می‌شود")
\```
```

**CSS مربوطه:**
```css
.article-content pre code {
    font-family: var(--terminal-font);
}
```

### کد درون خطی (Inline Code)

```markdown
برای اجرای دستور `hugo server` از فونت Fira Code استفاده می‌شود.
```

---

## ⚡ بهینه‌سازی فونت‌ها

### 1. Font Display Strategy

تمام فونت‌ها با `font-display: swap` تعریف شده‌اند:

```css
@font-face {
    font-family: 'Vazir';
    src: url(/assets/fonts/VazirMatn/Vazirmatn-Regular.woff2) format('woff2');
    font-display: swap;  /* 👈 بارگذاری سریع */
}
```

**مزایا:**
- متن سریع‌تر نمایش داده می‌شود
- بدون FOIT (Flash of Invisible Text)
- تجربه کاربری بهتر

### 2. فرمت WOFF2

همه فونت‌ها در فرمت WOFF2 هستند:
- فشرده‌سازی بهتر (30% کوچک‌تر از WOFF)
- پشتیبانی در تمام مرورگرهای مدرن
- بارگذاری سریع‌تر

### 3. Preload (اختیاری)

برای بارگذاری سریع‌تر فونت‌های مهم:

```html
<link rel="preload" href="/assets/fonts/VazirMatn/Vazirmatn-Regular.woff2" as="font" type="font/woff2" crossorigin>
```

---

## 🔧 عیب‌یابی

### فونت‌ها لود نمی‌شوند

**بررسی 1: مسیرها**
```css
/* ✅ صحیح */
src: url(/assets/fonts/VazirMatn/Vazirmatn-Regular.woff2)

/* ❌ اشتباه */
src: url(../fonts/VazirMatn/Vazirmatn-Regular.woff2)
```

**بررسی 2: فایل fonts.css**
```html
<!-- در baseof.html -->
<link rel="stylesheet" href="/assets/css/fonts.css" type="text/css">
```

**بررسی 3: فایل‌های فونت در static**
```
static/
└── assets/
    └── fonts/
        ├── VazirMatn/
        ├── Shabnam/
        └── ...
```

### فونت به درستی نمایش داده نمی‌شود

**بررسی وزن فونت:**
```css
/* ✅ صحیح - وزن 700 تعریف شده */
.title {
    font-family: var(--Shabnam);
    font-weight: 700;
}

/* ❌ اشتباه - وزن 900 تعریف نشده */
.title {
    font-family: var(--Shabnam);
    font-weight: 900;  /* این وزن وجود ندارد */
}
```

---

## 📊 اولویت‌بندی فونت‌ها

### اولویت بالا (Critical)
این فونت‌ها در ابتدای صفحه لود می‌شوند:
- Vazir Regular (400) - متن اصلی
- Shabnam Bold (700) - عنوان‌ها

### اولویت متوسط
- Vazir Medium (500)
- Vazir Bold (700)
- Shabnam Regular (400)

### اولویت پایین (Lazy Load)
- Vazir Light (300)
- Shabnam Light (300)
- Fira Code (کدها)
- Sahel & Yekan (اختیاری)

---

## 🎨 ترکیب‌های پیشنهادی

### ترکیب 1: کلاسیک
```css
body {
    font-family: var(--Vazir);
}

h1, h2, h3 {
    font-family: var(--Shabnam);
}
```

### ترکیب 2: مدرن
```css
body {
    font-family: var(--Yekan);
}

h1, h2, h3 {
    font-family: var(--Shabnam);
}
```

### ترکیب 3: Technical
```css
body {
    font-family: var(--Sahel);
}

code, pre {
    font-family: var(--terminal-font);
}
```

---

## 📱 فونت‌ها در Responsive

```css
/* Desktop */
body {
    font-size: 16px;
}

/* Tablet */
@media (max-width: 1024px) {
    body {
        font-size: 15px;
    }
}

/* Mobile */
@media (max-width: 768px) {
    body {
        font-size: 14px;
    }
}
```

---

## ✅ Checklist فونت‌ها

- [x] فونت‌ها در `assets/fonts/` کپی شده‌اند
- [x] فونت‌ها در `static/assets/fonts/` کپی شده‌اند
- [x] فایل `fonts.css` ایجاد شده
- [x] فایل `fonts.css` در `baseof.html` لینک شده
- [x] متغیرهای CSS تعریف شده‌اند
- [x] فونت‌ها در مقالات به درستی نمایش داده می‌شوند
- [x] `font-display: swap` فعال است
- [x] فرمت WOFF2 استفاده شده

---

**نکته:** برای اطلاعات بیشتر به [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md) مراجعه کنید.
