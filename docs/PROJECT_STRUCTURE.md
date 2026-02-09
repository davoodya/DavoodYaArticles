# ساختار پروژه Hugo - Davoodya

## 📁 ساختار فایل‌ها

```
davoodya/
├── assets/
│   └── css/
│       └── main.css          # فایل CSS اصلی (منبع)
├── content/
│   ├── cyber-security/       # دسته‌بندی امنیت سایبری
│   ├── python/               # دسته‌بندی پایتون
│   ├── seo/                  # دسته‌بندی سئو
│   └── tools/                # دسته‌بندی ابزارها
├── layouts/
│   ├── _default/
│   │   ├── baseof.html      # قالب پایه
│   │   ├── list.html        # قالب لیست دسته‌بندی‌ها
│   │   └── single.html      # قالب تک مقاله
│   └── index.html           # صفحه اصلی (لیست دسته‌بندی‌ها)
├── static/
│   └── assets/
│       └── css/
│           └── main.css     # فایل CSS استاتیک (کپی شده از assets)
└── hugo.toml                # فایل پیکربندی اصلی
```

## 🎨 استایل‌دهی (CSS)

### فایل‌های CSS

- **منبع اصلی**: `assets/css/main.css`
- **فایل استاتیک**: `static/assets/css/main.css`

> **نکته مهم**: برای اعمال تغییرات CSS:
> 1. فایل `assets/css/main.css` را ویرایش کنید
> 2. محتوای آن را به `static/assets/css/main.css` کپی کنید
> 3. سپس Hugo را rebuild کنید

### کلاس‌های CSS اصلی

#### صفحه اصلی (Home)
- `.page-title` - عنوان اصلی صفحه
- `.home-grid` - گرید دسته‌بندی‌ها
- `.category-card` - کارت هر دسته‌بندی
- `.category-description-text` - توضیحات دسته‌بندی
- `.category-meta` - متادیتای دسته‌بندی (تعداد مطالب)
- `.category-count` - تعداد مطالب

#### صفحه لیست مقالات (List)
- `.category-title` - عنوان دسته‌بندی
- `.category-description` - توضیحات دسته‌بندی
- `.articles-grid` - گرید مقالات
- `.article-card` - کارت هر مقاله
- `.article-card-title` - عنوان مقاله
- `.article-card-summary` - خلاصه مقاله
- `.read-more-btn` - دکمه ادامه مطلب

#### صفحه تک مقاله (Single)
- `.article-wrapper` - wrapper اصلی مقاله
- `.article-title` - عنوان مقاله
- `.article-content` - محتوای مقاله

## 📝 قالب‌های HTML

### 1. صفحه اصلی (`layouts/index.html`)
نمایش کارت‌های دسته‌بندی‌ها

### 2. لیست مقالات (`layouts/_default/list.html`)
نمایش کارت‌های مقالات در هر دسته‌بندی با:
- عنوان مقاله
- خلاصه کوتاه (200 کاراکتر)
- دکمه "ادامه مطلب"

### 3. تک مقاله (`layouts/_default/single.html`)
نمایش محتوای کامل مقاله

### 4. قالب پایه (`layouts/_default/baseof.html`)
شامل:
- تگ‌های meta
- لینک به CSS
- Schema Markup (SEO)

## ⚙️ پیکربندی (`hugo.toml`)

```toml
summaryLength = 70          # تعداد کلمات خلاصه
hasCJKLanguage = true       # پشتیبانی از زبان‌های آسیایی
[pagination]
  pagerSize = 10            # تعداد مقالات در هر صفحه
```

## 🚀 دستورات

### اجرای سرور توسعه
```bash
hugo server -D
```

### ساخت سایت نهایی
```bash
hugo
```

### پاک‌سازی
```bash
hugo --cleanDestinationDir
```

## 📋 نکات مهم

### خلاصه مقالات
Hugo از ترتیب زیر برای نمایش خلاصه استفاده می‌کند:
1. اگر `description` در front matter مقاله وجود داشته باشد
2. در غیر این صورت از `.Summary` استفاده می‌کند
3. در غیر این صورت از محتوا استفاده می‌کند

### اضافه کردن مقاله جدید
```bash
hugo new cyber-security/my-article.md
```

### Front Matter مقاله
```yaml
---
title: "عنوان مقاله"
description: "توضیح کوتاه مقاله"
date: 2026-02-07
tags:
  - CyberSecurity
  - Security
---
```

## 🎯 ویژگی‌های پیاده‌سازی شده

✅ نمایش دسته‌بندی‌ها به صورت کارت در صفحه اصلی
✅ نمایش مقالات به صورت کارت در صفحات دسته‌بندی
✅ خلاصه کوتاه مقالات (200 کاراکتر)
✅ دکمه "ادامه مطلب" با استایل مناسب
✅ Pagination برای صفحات دسته‌بندی
✅ طراحی responsive
✅ تم تاریک با رنگ‌های سایبری
✅ انیمیشن‌های hover
✅ RTL support
✅ SEO friendly (Schema Markup)

## 🎨 فونت‌ها

### فونت‌های نصب شده

**فارسی:**
- Vazir (متن اصلی) - `var(--Vazir)`
- Shabnam (عنوان‌ها) - `var(--Shabnam)`
- Sahel - `var(--Sahel)`
- Yekan - `var(--Yekan)`

**لاتین:**
- Fira Code (کد) - `var(--terminal-font)`
- Rajdhani - `var(--content-font)`

### لود فونت‌ها

فونت‌ها از طریق فایل `/assets/css/fonts.css` لود می‌شوند که در `baseof.html` لینک شده است.

## 🏗️ Header و Footer

### Header (`layouts/partials/header.html`)
- لوگو و نام سایت با افکت glow
- منوی اصلی با لینک به دسته‌بندی‌ها
- منوی موبایل (hamburger menu)
- Sticky header با backdrop blur

### Footer (`layouts/partials/footer.html`)
- بخش About
- لینک‌های سریع (Quick Links)
- شبکه‌های اجتماعی
- Copyright و اطلاعات

## 🔧 توسعه بیشتر

### افزودن استایل جدید
1. فایل `assets/css/main.css` را باز کنید
2. استایل‌های خود را اضافه کنید
3. فایل را به static کپی کنید:
   ```bash
   copy "assets\css\main.css" "static\assets\css\main.css"
   ```
4. Hugo را reload کنید یا منتظر hot reload بمانید

### سفارشی‌سازی Header/Footer
فایل‌های `layouts/partials/header.html` و `footer.html` را ویرایش کنید.

## 📚 منابع

- [مستندات Hugo](https://gohugo.io/documentation/)
- [Template Variables](https://gohugo.io/variables/)
- [Content Management](https://gohugo.io/content-management/)
- [راهنمای توسعه کامل](DEVELOPMENT_GUIDE.md)
