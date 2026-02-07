# راهنمای توسعه پروژه Davoodya

## 📋 فهرست مطالب
- [نصب و راه‌اندازی](#نصب-و-راه‌اندازی)
- [ساختار پروژه](#ساختار-پروژه)
- [فونت‌ها](#فونت‌ها)
- [استایل‌دهی](#استایل‌دهی)
- [Header و Footer](#header-و-footer)
- [توسعه بیشتر](#توسعه-بیشتر)

---

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- Hugo Extended نسخه 0.120.0 یا بالاتر
- Git

### دستورات اصلی

```bash
# اجرای سرور توسعه
hugo server -D

# ساخت سایت نهایی
hugo

# پاک‌سازی و build مجدد
hugo --cleanDestinationDir
```

---

## 📁 ساختار پروژه

```
davoodya/
├── assets/
│   ├── css/
│   │   ├── main.css              # استایل‌های اصلی (منبع)
│   │   └── fonts/
│   │       └── fonts.min.css     # تعریف فونت‌ها
│   └── fonts/                     # فایل‌های فونت
│       ├── VazirMatn/
│       ├── Shabnam/
│       ├── fira-code/
│       └── Rajdhani/
├── content/
│   ├── cyber-security/
│   ├── python/
│   ├── seo/
│   └── tools/
├── layouts/
│   ├── _default/
│   │   ├── baseof.html          # قالب پایه
│   │   ├── list.html            # لیست مقالات
│   │   └── single.html          # تک مقاله
│   ├── partials/
│   │   ├── header.html          # هدر سایت
│   │   └── footer.html          # فوتر سایت
│   └── index.html               # صفحه اصلی
├── static/
│   └── assets/                   # فایل‌های استاتیک
│       ├── css/
│       │   ├── main.css
│       │   └── fonts.css
│       └── fonts/
└── hugo.toml                     # پیکربندی
```

---

## 🎨 فونت‌ها

### فونت‌های فارسی

#### Vazir (فونت اصلی متن)
```css
font-family: var(--Vazir);
```
- استفاده: متن‌های اصلی، پاراگراف‌ها
- وزن‌ها: 300, 400, 500, 700

#### Shabnam (فونت عنوان‌ها)
```css
font-family: var(--Shabnam);
```
- استفاده: عنوان‌ها، تیترها، دکمه‌ها
- وزن‌ها: 300, 400, 700

#### Sahel
```css
font-family: var(--Sahel);
```
- استفاده: اختیاری
- وزن‌ها: 300, 400, 700

#### Yekan
```css
font-family: var(--Yekan);
```
- استفاده: اختیاری
- وزن‌ها: 300, 400, 700

### فونت‌های لاتین

#### Fira Code (فونت کد)
```css
font-family: var(--terminal-font);
```
- استفاده: کدها، بلوک‌های کد، متن‌های monospace
- وزن‌ها: 300, 400, 500, 600, 700

#### Rajdhani
```css
font-family: var(--content-font);
```
- استفاده: محتوای لاتین
- وزن‌ها: 300, 400, 500, 600, 700

### افزودن فونت جدید

1. فایل‌های فونت را در `assets/fonts/` قرار دهید
2. در `assets/css/fonts/fonts.min.css` تعریف کنید:

```css
@font-face {
    font-family: 'YourFont';
    src: url(/assets/fonts/YourFont/YourFont-Regular.woff2) format('woff2');
    font-weight: 400;
    font-style: normal;
    font-display: swap;
}
```

3. در متغیرهای CSS اضافه کنید:

```css
:root {
    --your-font: 'YourFont', sans-serif;
}
```

4. فونت‌ها را به static کپی کنید:

```bash
xcopy /E /I /Y "assets\fonts" "static\assets\fonts"
copy "assets\css\fonts\fonts.min.css" "static\assets\css\fonts.css"
```

---

## 🎨 استایل‌دهی

### متغیرهای CSS (تم Cyberpunk)

```css
:root {
    /* رنگ‌های پس‌زمینه */
    --dark-bg: #0a0a0a;
    --darker-bg: #050505;
    --card-bg: #0f0f0f;
    
    /* رنگ‌های متن */
    --main-text: #e0e0e0;
    --secondary-text: #b0b0b0;
    --muted-text: #808080;
    
    /* رنگ‌های accent */
    --accent-green: #00ff41;
    --accent-blue: #3aaddf;
    --accent-orange: #e06c11;
    --accent-purple: #c678dd;
    --accent-yellow: #e5c07b;
    
    /* سایه‌ها */
    --glow-shadow: 0 0 10px rgba(0, 255, 65, 0.7);
    --glow-shadow-blue: 0 0 10px rgba(58, 173, 223, 0.6);
}
```

### کلاس‌های اصلی

#### صفحه اصلی
```css
.page-title           /* عنوان صفحه اصلی */
.home-grid            /* گرید دسته‌بندی‌ها */
.category-card        /* کارت دسته‌بندی */
.category-meta        /* اطلاعات دسته‌بندی */
```

#### لیست مقالات
```css
.category-title       /* عنوان دسته‌بندی */
.articles-grid        /* گرید مقالات */
.article-card         /* کارت مقاله */
.article-card-title   /* عنوان مقاله */
.article-card-summary /* خلاصه مقاله */
.read-more-btn        /* دکمه ادامه مطلب */
```

#### صفحه مقاله
```css
.article-wrapper      /* wrapper مقاله */
.article-title        /* عنوان مقاله */
.article-content      /* محتوای مقاله */
```

### اضافه کردن استایل جدید

1. فایل `assets/css/main.css` را باز کنید
2. استایل‌های خود را اضافه کنید:

```css
/* ============================= */
/* Custom Section */
/* ============================= */

.my-custom-class {
    /* استایل‌های شما */
}
```

3. فایل را به static کپی کنید:

```bash
copy "assets\css\main.css" "static\assets\css\main.css"
```

4. Hugo را rebuild کنید یا منتظر hot reload بمانید

---

## 🏗️ Header و Footer

### Header (`layouts/partials/header.html`)

Header شامل بخش‌های زیر است:
- **Logo/Brand**: لوگو و نام سایت
- **Navigation Menu**: منوی اصلی با لینک به دسته‌بندی‌ها
- **Mobile Menu Toggle**: دکمه منوی موبایل

#### سفارشی‌سازی منو

برای تغییر یا اضافه کردن آیتم منو:

```html
<li class="nav-item">
    <a href="/about/" class="nav-link">
        <span class="nav-icon">👤</span>
        <span class="nav-text">درباره من</span>
    </a>
</li>
```

### Footer (`layouts/partials/footer.html`)

Footer شامل بخش‌های زیر است:
- **About Section**: توضیحات کوتاه
- **Quick Links**: لینک‌های سریع
- **Contact/Social**: شبکه‌های اجتماعی
- **Copyright**: اطلاعات کپی‌رایت

#### تغییر لینک‌های اجتماعی

```html
<li>
    <a href="https://twitter.com/yourhandle" target="_blank" class="social-link">
        <span class="social-icon">🐦</span>
        <span class="social-text">Twitter</span>
    </a>
</li>
```

---

## 🎯 تم Things Obsidian

تم مقالات الهام گرفته از Things Obsidian است:

### ویژگی‌های اصلی

1. **عنوان‌های رنگی**
   - H1: سبز (`--accent-green`)
   - H2: آبی (`--accent-blue`) با نشانگر ▸
   - H3: نارنجی (`--accent-orange`)
   - H4: بنفش (`--accent-purple`)

2. **بلوک‌های کد**
   - پس‌زمینه مشکی با border سبز
   - فونت Fira Code
   - سایه‌های نئون

3. **Blockquote**
   - Border آبی در سمت راست
   - پس‌زمینه نیمه‌شفاف
   - نقل‌قول با علامت "

4. **لینک‌ها**
   - رنگ آبی با border نقطه‌چین
   - hover: سبز با افکت glow

5. **جداول**
   - Header سبز
   - Row hover با رنگ آبی کم‌رنگ

---

## 📱 Responsive Design

سایت برای 3 breakpoint بهینه شده:

```css
/* Desktop: > 1024px */
/* Tablet: 768px - 1024px */
/* Mobile: < 768px */
```

### تست Responsive

```bash
# در مرورگر Developer Tools:
# Device Toolbar را فعال کنید
# سایزهای مختلف را تست کنید
```

---

## 🔧 توسعه بیشتر

### اضافه کردن صفحه جدید

```bash
hugo new about.md
```

### اضافه کردن دسته‌بندی جدید

```bash
mkdir content/new-category
hugo new new-category/_index.md
```

### اضافه کردن مقاله جدید

```bash
hugo new cyber-security/my-article.md
```

### Front Matter مقاله

```yaml
---
title: "عنوان مقاله"
description: "توضیح کوتاه برای SEO و لیست"
date: 2026-02-07
tags:
  - CyberSecurity
  - Security
---
```

---

## 🐛 عیب‌یابی

### فونت‌ها لود نمی‌شوند

1. مسیرها را بررسی کنید
2. فونت‌ها را به static کپی کنید
3. Developer Tools > Network را بررسی کنید

### استایل‌ها اعمال نمی‌شوند

1. فایل CSS را به static کپی کنید
2. Cache مرورگر را پاک کنید (Ctrl + Shift + R)
3. Hugo server را restart کنید

### Build خطا می‌دهد

```bash
# پاک‌سازی کامل
hugo --cleanDestinationDir
# Build مجدد
hugo
```

---

## 📚 منابع

- [Hugo Documentation](https://gohugo.io/documentation/)
- [Hugo Templates](https://gohugo.io/templates/)
- [Hugo Variables](https://gohugo.io/variables/)
- [CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

---

## ✅ Checklist توسعه

- [x] فونت‌های فارسی و لاتین
- [x] تم Cyberpunk با رنگ‌های نئون
- [x] Header با منوی responsive
- [x] Footer با لینک‌های اجتماعی
- [x] صفحه اصلی با کارت‌های دسته‌بندی
- [x] لیست مقالات با خلاصه کوتاه
- [x] صفحه مقاله با تم Things Obsidian
- [x] Pagination
- [x] Responsive design
- [ ] منوی موبایل (JavaScript - مرحله بعد)
- [ ] Dark/Light mode toggle (مرحله بعد)
- [ ] Search functionality (مرحله بعد)

---

**نسخه:** 1.0.0  
**تاریخ آخرین بروزرسانی:** {{ now.Format "2006-01-02" }}  
**نویسنده:** Davood Yahya
