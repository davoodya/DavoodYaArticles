# اصلاح نمایش "نوشته‌های تازه" در Sidebar

## 🐛 مشکل

مقالات جدیدی که در دایرکتوری‌های مختلف `content/` اضافه می‌شدند (مانند `network/`) در بخش "نوشته‌های تازه" Sidebar نمایش داده نمی‌شدند.

---

## 🔍 علت مشکل

در فایل `layouts/partials/sidebar.html`، کد زیر استفاده می‌شد:

```go
{{ $recentPosts := where .Site.RegularPages "Type" "in" (slice "cyber-security" "python" "seo" "tools") }}
```

این کد فقط مقالاتی را نمایش می‌داد که `Type` آن‌ها در لیست مشخص شده بود:
- cyber-security ✅
- python ✅
- seo ✅
- tools ✅
- **network ❌ (نبود!)**
- **linux ❌ (نبود!)**

---

## ✅ راه‌حل

کد را به صورت زیر تغییر دادیم تا **همه مقالات** از **تمام دایرکتوری‌ها** را نمایش دهد:

```go
{{/* گرفتن همه صفحات معمولی (نه section pages) و مرتب‌سازی بر اساس تاریخ */}}
{{ $recentPosts := where .Site.RegularPages "Kind" "page" }}
{{ $recentPosts = where $recentPosts "Draft" false }}
{{ $recentPosts = first 5 (sort $recentPosts "Date" "desc") }}
```

### توضیح کد:

1. **`.Site.RegularPages`**: همه صفحات معمولی سایت
2. **`where ... "Kind" "page"`**: فقط صفحات مقاله (نه صفحات Section/Taxonomy)
3. **`where ... "Draft" false`**: فقط مقالات منتشر شده (نه Draft)
4. **`sort ... "Date" "desc"`**: مرتب‌سازی بر اساس تاریخ (جدیدترین اول)
5. **`first 5`**: فقط 5 مقاله اول (جدیدترین‌ها)

---

## 🎯 نتیجه

حالا:
- ✅ همه مقالات از **تمام دایرکتوری‌ها** نمایش داده می‌شوند
- ✅ مقالات **بر اساس تاریخ** مرتب می‌شوند
- ✅ فقط **5 مقاله جدیدترین** نمایش داده می‌شوند
- ✅ مقالات **Draft نمایش داده نمی‌شوند**
- ✅ از این به بعد **هر مقاله جدید** در هر دایرکتوری به صورت خودکار در "نوشته‌های تازه" نمایش داده می‌شود

---

## 📋 فایل تغییر یافته

- `layouts/partials/sidebar.html`

---

## 🧪 تست

### قبل از تغییر:
```
نوشته‌های تازه:
- مقاله 1 (cyber-security)
- مقاله 2 (python)
- مقاله 3 (seo)
- مقاله 4 (tools)
- مقاله 5 (cyber-security)

❌ مقالات network نمایش داده نمی‌شدند
```

### بعد از تغییر:
```
نوشته‌های تازه:
- مقاله شبکه 1 (network) ✅ جدید!
- مقاله شبکه 2 (network) ✅ جدید!
- مقاله 1 (cyber-security)
- مقاله 2 (linux) ✅ جدید!
- مقاله 3 (python)

✅ همه مقالات از همه دایرکتوری‌ها نمایش داده می‌شوند
```

---

## 💡 نکات مهم

### 1. تاریخ مقاله مهم است

مقالات بر اساس فیلد `date` در frontmatter مرتب می‌شوند:

```toml
+++
title = "مقاله جدید"
date = "2026-02-09"  # ← این فیلد برای مرتب‌سازی استفاده می‌شود
+++
```

### 2. مقالات Draft نمایش داده نمی‌شوند

```toml
+++
title = "مقاله Draft"
date = "2026-02-09"
draft = true  # ← این مقاله در "نوشته‌های تازه" نمایش داده نمی‌شود
+++
```

### 3. فقط صفحات مقاله نمایش داده می‌شوند

- ✅ مقالات معمولی: `/network/article.md`
- ✅ مقالات در زیرشاخه: `/cyber-security/cryptography/article.md`
- ❌ صفحات Section: `/network/_index.md`
- ❌ صفحات Taxonomy: `/tags/linux/`

---

## 🔄 نحوه کار

### Workflow:

1. شما مقاله جدید به `content/network/new-article.md` اضافه می‌کنید
2. Hugo build می‌گیرید
3. Hugo تمام صفحات را چک می‌کند
4. صفحات را بر اساس `date` مرتب می‌کند
5. 5 مقاله جدیدترین را انتخاب می‌کند
6. در Sidebar نمایش می‌دهد

### مثال:

```bash
content/
├── network/
│   └── new-article.md  # date: 2026-02-09 ← جدیدترین!
├── cyber-security/
│   └── old-article.md  # date: 2024-06-20
├── linux/
│   └── article.md      # date: 2025-01-15
└── python/
    └── article.md      # date: 2025-12-01
```

**نتیجه در Sidebar:**
1. new-article (network) - 2026-02-09
2. article (python) - 2025-12-01
3. article (linux) - 2025-01-15
4. ... (بعدی‌ها)
5. old-article (cyber-security) - 2024-06-20

---

## 🚀 دستورات Build

```bash
# Build production
hugo --cleanDestinationDir

# Dev server
hugo server -D

# Dev server با نمایش drafts
hugo server -D --buildDrafts
```

---

## 📊 مقایسه قبل و بعد

| ویژگی | قبل | بعد |
|-------|-----|-----|
| دایرکتوری‌های پشتیبانی شده | فقط 4 تا | همه |
| مقالات network | ❌ | ✅ |
| مقالات linux | ❌ | ✅ |
| افزودن دایرکتوری جدید | نیاز به تغییر کد | خودکار ✅ |
| مرتب‌سازی | بر اساس تاریخ | بر اساس تاریخ |
| فیلتر Draft | ندارد | دارد ✅ |

---

## 🎓 یادگیری

### Hugo Functions استفاده شده:

1. **`.Site.RegularPages`**: آرایه همه صفحات معمولی
2. **`where X "Field" Y`**: فیلتر کردن بر اساس فیلد
3. **`sort X "Field" "order"`**: مرتب‌سازی
4. **`first N X`**: گرفتن N تای اول
5. **`"Kind" "page"`**: نوع صفحه

### مثال ساده:

```go
{{ $allPages := .Site.RegularPages }}           // همه صفحات
{{ $onlyArticles := where $allPages "Kind" "page" }}  // فقط مقالات
{{ $notDraft := where $onlyArticles "Draft" false }}  // غیر Draft
{{ $sorted := sort $notDraft "Date" "desc" }}         // مرتب شده
{{ $recent := first 5 $sorted }}                      // 5 تای اول
```

---

## ✅ Checklist

- [x] کد قدیمی حذف شد
- [x] کد جدید اضافه شد
- [x] Build موفق بود
- [x] مقالات network نمایش داده می‌شوند
- [x] مقالات linux نمایش داده می‌شوند
- [x] مرتب‌سازی بر اساس تاریخ کار می‌کند
- [x] فیلتر Draft کار می‌کند
- [x] مستندات نوشته شد

---

**تاریخ اصلاح**: 2026-02-09  
**فایل**: `layouts/partials/sidebar.html`  
**وضعیت**: ✅ اصلاح شده و تست شده
