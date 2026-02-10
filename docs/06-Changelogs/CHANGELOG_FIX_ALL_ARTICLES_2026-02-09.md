# Changelog - رفع مشکلات صفحه "تمام مقالات"
## تاریخ: 2026-02-09 (بروزرسانی دوم)

## 🐛 مشکلات برطرف شده

### 1. رفع مشکل تعداد اشتباه مقالات (60 به جای 30)

**مشکل**: 
- پس از پاک شدن دایرکتوری `all-articles` و قرار دادن مقالات در آن، تعداد مقالات دوبرابر نمایش داده می‌شد
- دلیل: مقالات هم در دسته‌بندی‌های اصلی و هم در `all-articles` وجود داشتند

**راه‌حل**:
1. بازسازی دایرکتوری `all-articles` با ساختار صحیح
2. اضافه کردن فیلتر در template برای حذف خود section از لیست:

```go
{{ $allPages := where site.RegularPages "Section" "!=" "all-articles" }}
{{ $allPages = where $allPages "Draft" false }}
```

### 2. رفع مشکل نمایش "تمام مقالات" در dropdown سایر دسته‌بندی‌ها

**مشکل**:
- دایرکتوری `all-articles` به عنوان یک Section شناخته می‌شد
- در dropdown "سایر دسته‌بندی‌ها" نمایش داده می‌شد
- Badge آن تعداد 1 (فقط فایل `_index.md`) نشان می‌داد

**راه‌حل**:
فیلتر کردن Sections در sidebar:

```go
{{ $categories := slice }}
{{ range .Site.Sections }}
    {{ if ne .Section "all-articles" }}
        {{ $categories = $categories | append . }}
    {{ end }}
{{ end }}
```

### 3. رفع مشکل Badge با تعداد 1

**مشکل**:
- اگر `all-articles` در dropdown ظاهر می‌شد، badge آن تعداد 1 نشان می‌داد
- این عدد فقط تعداد فایل `_index.md` بود نه تمام مقالات

**راه‌حل**:
- با حذف `all-articles` از لیست Sections، این مشکل حل شد
- فقط آیتم اول با استایل ویژه باقی ماند که badge صحیح (30) را نشان می‌دهد

---

## 📝 فایل‌های ایجاد شده

### 1. بازسازی دایرکتوری all-articles
```
content/all-articles/
├── _index.md          # فایل اصلی صفحه
├── README.md          # راهنمای هشدار
└── .gitkeep          # حفظ دایرکتوری در Git
```

**محتوای `_index.md`:**
```markdown
+++
title = "تمام مقالات"
description = "مشاهده تمام مقالات منتشر شده در سایت به صورت یکجا"
featured_image = "/images/general/gohugo-default-sample-hero-image.jpg"
layout = "all-articles"
+++

این صفحه تمام مقالات منتشر شده در وبسایت را نمایش می‌دهد.
```

### 2. فایل README.md
یک راهنمای جامع که توضیح می‌دهد:
- چرا این دایرکتوری را نباید پاک کرد
- چرا نباید مقاله در آن قرار داد
- چگونه فیلتر کار می‌کند

### 3. فایل .gitkeep
برای اطمینان از حفظ دایرکتوری در Git repository

---

## 🔧 فایل‌های ویرایش شده

### 1. `layouts/_default/all-articles.html`

**قبل:**
```go
{{ $allPages := .Site.RegularPages }}
{{ $allPages = where $allPages "Draft" false }}
```

**بعد:**
```go
{{/* محاسبه تعداد واقعی مقالات */}}
{{ $realArticles := where site.RegularPages "Section" "!=" "all-articles" }}
{{ $realArticles = where $realArticles "Draft" false }}

{{/* فیلتر کردن صفحات برای نمایش */}}
{{ $allPages := where site.RegularPages "Section" "!=" "all-articles" }}
{{ $allPages = where $allPages "Draft" false }}
```

**تاثیر:**
- تعداد مقالات از 60 به 30 کاهش یافت
- فقط مقالات واقعی نمایش داده می‌شوند
- خود صفحه `all-articles` در لیست نیست

### 2. `layouts/partials/sidebar.html`

**قبل:**
```go
{{ $categories := slice }}
{{ range .Site.Sections }}
    {{ $categories = $categories | append . }}
{{ end }}
```

**بعد:**
```go
{{/* فیلتر کردن دسته‌بندی‌ها و حذف all-articles */}}
{{ $categories := slice }}
{{ range .Site.Sections }}
    {{ if ne .Section "all-articles" }}
        {{ $categories = $categories | append . }}
    {{ end }}
{{ end }}
```

**تاثیر:**
- `all-articles` دیگر در dropdown ظاهر نمی‌شود
- فقط به عنوان آیتم اول با استایل ویژه باقی می‌ماند
- Badge صحیح (30) را نشان می‌دهد

### 3. `docs/ALL_ARTICLES_PAGE_GUIDE.md`

اضافه شدن:
- بخش troubleshooting با 5 مشکل رایج
- راه‌حل برای مشکل dropdown
- Checklist نگهداری

---

## 📊 مقایسه قبل و بعد

### تعداد مقالات در صفحه all-articles
- ❌ قبل: 60 مقاله (شامل تکراری‌ها)
- ✅ بعد: 30 مقاله (فقط مقالات واقعی)

### Badge در سایدبار
- ❌ قبل: 30 (صحیح) یا 0 (اشتباه)
- ✅ بعد: 30 (همیشه صحیح)

### نمایش در dropdown
- ❌ قبل: "تمام مقالات" با badge 1 در dropdown
- ✅ بعد: حذف شده، فقط آیتم ویژه در ابتدای لیست

### آمار صفحه
- ❌ قبل: تعداد کل مقالات: 60
- ✅ بعد: تعداد کل مقالات: 30

---

## 🎯 منطق فیلتر

### چرا از این فیلتر استفاده می‌کنیم؟

```go
{{ if ne .Section "all-articles" }}
```

این فیلتر مطمئن می‌شود که:
1. دایرکتوری `all-articles` به عنوان یک Section شناخته نمی‌شود
2. در لیست دسته‌بندی‌های عادی قرار نمی‌گیرد
3. فقط به عنوان یک آیتم ویژه (با استایل خاص) نمایش داده می‌شود
4. Badge آن تعداد کل مقالات را نشان می‌دهد نه تعداد فایل‌های درون آن

### جریان کار:

```
1. دریافت تمام Sections
   ↓
2. فیلتر کردن: ne .Section "all-articles"
   ↓
3. نتیجه: فقط دسته‌بندی‌های واقعی (network, linux, seo, ...)
   ↓
4. نمایش در لیست معمولی با badge صحیح
```

---

## ⚠️ نکات مهم

### 1. ساختار صحیح دایرکتوری all-articles
```
content/all-articles/
├── _index.md     ✅ فقط این فایل
├── README.md     ✅ راهنما (اختیاری)
└── .gitkeep      ✅ حفظ دایرکتوری (اختیاری)
```

**ممنوع:**
```
content/all-articles/
├── _index.md
├── article1.md   ❌ نباید مقاله اینجا باشد
└── article2.md   ❌ نباید مقاله اینجا باشد
```

### 2. مقالات باید در دسته‌بندی‌های خودشان باشند
```
✅ content/network/IP-Mac-Address.md
✅ content/linux/60-Commands.md
✅ content/seo/SEO-Theories.md
❌ content/all-articles/any-article.md
```

### 3. دایرکتوری را حذف نکنید
- بدون این دایرکتوری، صفحه `/all-articles/` کار نمی‌کند
- لینک‌ها خطای 404 می‌دهند
- دکمه‌ها و لینک‌ها معطل می‌مانند

---

## ✅ Checklist نهایی

- [x] دایرکتوری `all-articles` با ساختار صحیح ایجاد شد
- [x] فیلتر در `all-articles.html` اضافه شد
- [x] فیلتر در `sidebar.html` اضافه شد
- [x] تعداد مقالات صحیح نمایش داده می‌شود (30)
- [x] `all-articles` در dropdown نمایش داده نمی‌شود
- [x] Badge سایدبار تعداد صحیح را نشان می‌دهد
- [x] آمار صفحه all-articles صحیح است
- [x] مستندات به‌روز شده است
- [x] فایل README.md اضافه شده
- [x] فایل .gitkeep اضافه شده

---

## 🚀 تست‌ها

### تست 1: بررسی تعداد مقالات
```bash
# دسترسی به صفحه
http://localhost:1313/all-articles/

# نتیجه مورد انتظار:
✅ تعداد کل مقالات: 30
✅ 30 مقاله در لیست
✅ بدون تکراری
```

### تست 2: بررسی sidebar
```bash
# بررسی آیتم "تمام مقالات"
✅ Badge: 30

# بررسی dropdown "سایر دسته‌بندی‌ها"
✅ "تمام مقالات" در لیست نیست
✅ فقط دسته‌بندی‌های واقعی
```

### تست 3: بررسی دایرکتوری
```bash
ls content/all-articles/

# نتیجه مورد انتظار:
_index.md
README.md
.gitkeep
```

---

## 📚 منابع

- [Hugo Sections](https://gohugo.io/content-management/sections/)
- [Hugo where Function](https://gohugo.io/functions/where/)
- [Hugo Filtering](https://gohugo.io/templates/lists/#filtering)

---

## 🎉 نتیجه

تمام مشکلات برطرف شدند:
- ✅ تعداد مقالات صحیح است
- ✅ دایرکتوری بازسازی شد
- ✅ فیلترها کار می‌کنند
- ✅ UI تمیز و بدون تکراری است
- ✅ مستندات کامل است

**توسعه‌دهنده**: Davood Yahay  
**تاریخ**: 2026-02-09  
**نسخه**: 1.0.1 (Fix)
