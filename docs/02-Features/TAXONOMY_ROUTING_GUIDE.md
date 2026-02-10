# راهنمای سیستم Taxonomy-Based Routing

## 📋 نمای کلی

این سیستم امکان ایجاد URL های تمیز و SEO-friendly برای Badgeهای مقالات را فراهم می‌کند. هر Badge (به‌جز `readingTime`) به صورت خودکار به صفحه آرشیو فیلترشده مربوط به خود لینک می‌شود.

## 🎯 ویژگی‌های کلیدی

- ✅ URL های تمیز و استاندارد
- ✅ SEO-friendly
- ✅ Mapping فارسی به انگلیسی برای `post_type_fa`
- ✅ Validation کامل
- ✅ 404 برای مقادیر نامعتبر
- ✅ قابل توسعه برای Taxonomyهای جدید
- ✅ Single Source of Truth (Registry مرکزی)

## 📁 ساختار فایل‌ها

```
davoodya/
├── data/
│   └── taxonomies.json              # Registry مرکزی
├── layouts/
│   ├── _default/
│   │   ├── taxonomy.html            # Template عمومی برای صفحات taxonomy
│   │   ├── single.html              # صفحه تک مقاله (با Badgeهای clickable)
│   │   ├── list.html                # صفحه لیست (با Badgeهای clickable)
│   │   └── all-articles.html        # صفحه همه مقالات (با Badgeهای clickable)
│   └── partials/
│       └── taxonomy-url.html        # Helper برای تولید URL
├── content/
│   ├── difficulty/                  # Taxonomy: سطح دشواری
│   │   ├── _index.md
│   │   ├── beginner.md              # /difficulty/beginner/
│   │   ├── medium.md                # /difficulty/medium/
│   │   ├── intermediate.md          # /difficulty/intermediate/
│   │   └── advanced.md              # /difficulty/advanced/
│   ├── lab_required/                # Taxonomy: نیاز به آزمایشگاه
│   │   ├── _index.md
│   │   ├── true.md                  # /lab_required/true/
│   │   └── false.md                 # /lab_required/false/
│   └── type/                        # Taxonomy: نوع محتوا
│       ├── _index.md
│       ├── tutorial.md              # /type/tutorial/
│       ├── article.md               # /type/article/
│       ├── script.md                # /type/script/
│       ├── news.md                  # /type/news/
│       ├── howto.md                 # /type/howto/
│       ├── intro.md                 # /type/intro/
│       └── tool.md                  # /type/tool/
└── assets/
    └── css/
        └── main.css                 # استایل Badgeهای clickable
```

## 🗂️ Registry مرکزی (`data/taxonomies.json`)

```json
{
  "difficulty": {
    "slug": "difficulty",
    "label_fa": "سطح دشواری",
    "values": ["beginner", "medium", "intermediate", "advanced"],
    "labels": {
      "beginner": "مبتدی",
      "medium": "متوسط",
      "intermediate": "حرفه‌ای",
      "advanced": "تخصصی"
    }
  },
  "lab_required": {
    "slug": "lab_required",
    "label_fa": "نیاز به آزمایشگاه",
    "values": ["true", "false"],
    "labels": {
      "true": "نیاز به تمرین عملی",
      "false": "بدون نیاز به آزمایشگاه"
    }
  },
  "post_type_fa": {
    "slug": "type",
    "label_fa": "نوع محتوا",
    "mapping": {
      "آموزشی": "tutorial",
      "مقاله": "article",
      "اسکریپت": "script",
      "خبر": "news",
      "دستور العمل": "howto",
      "معرفی": "intro",
      "ابزار": "tool"
    },
    "reverse_mapping": {
      "tutorial": "آموزشی",
      "article": "مقاله",
      "script": "اسکریپت",
      "news": "خبر",
      "howto": "دستور العمل",
      "intro": "معرفی",
      "tool": "ابزار"
    }
  }
}
```

## 🔗 نحوه تولید URL

### 1. Difficulty

```
Badge: "مبتدی"
URL: /difficulty/beginner/
```

### 2. Lab Required

```
Badge: "نیاز به تمرین عملی"
URL: /lab_required/true/
```

### 3. Post Type (با Mapping)

```
Badge: "آموزشی" (فارسی)
URL: /type/tutorial/ (انگلیسی)
```

## 🧩 نحوه استفاده در Templates

### تولید URL برای Badge:

```go
{{ $difficultyUrl := partial "taxonomy-url.html" (dict "taxonomy" "difficulty" "value" .Params.difficulty "context" .) }}
<a href="{{ $difficultyUrl }}" class="meta-badge badge-difficulty">
    <span class="badge-text">{{ $difficultyText }}</span>
</a>
```

### مثال کامل (از `single.html`):

```go
{{/* سطح سختی - با لینک */}}
{{ if .Params.difficulty }}
    {{ $difficultyText := "" }}
    {{ $difficultyClass := "" }}
    {{ if eq .Params.difficulty "beginner" }}
        {{ $difficultyText = "سطح مبتدی" }}
        {{ $difficultyClass = "badge-beginner" }}
    {{ else if eq .Params.difficulty "medium" }}
        {{ $difficultyText = "سطح متوسط" }}
        {{ $difficultyClass = "badge-medium" }}
    {{ else if eq .Params.difficulty "intermediate" }}
        {{ $difficultyText = "سطح حرفه‌ای" }}
        {{ $difficultyClass = "badge-intermediate" }}
    {{ else if eq .Params.difficulty "advanced" }}
        {{ $difficultyText = "سطح تخصصی" }}
        {{ $difficultyClass = "badge-advanced" }}
    {{ end }}
    {{ $difficultyUrl := partial "taxonomy-url.html" (dict "taxonomy" "difficulty" "value" .Params.difficulty "context" .) }}
    <a href="{{ $difficultyUrl }}" class="meta-badge badge-difficulty {{ $difficultyClass }}" title="مشاهده همه مقالات {{ $difficultyText }}">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
        </svg>
        <span class="badge-text">{{ $difficultyText }}</span>
    </a>
{{ end }}
```

## 📄 ساختار صفحه Taxonomy

هر صفحه taxonomy باید این فیلدها را داشته باشد:

```markdown
+++
title = "مقالات سطح متوسط"
description = "مشاهده همه مقالات با سطح دشواری متوسط"
draft = false
layout = "taxonomy"
taxonomy_slug = "difficulty"
taxonomy_value = "medium"
+++
```

## 🎨 استایل Badgeها

Badgeهای clickable دارای این ویژگی‌ها هستند:

```css
/* Badge قابل کلیک */
a.meta-badge {
    position: relative;
    overflow: hidden;
    cursor: pointer;
    text-decoration: none;
}

/* انیمیشن hover */
a.meta-badge::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.5s ease;
}

a.meta-badge:hover::before {
    left: 100%;
}

/* Badge مدت زمان - بدون لینک */
.meta-badge.badge-time {
    cursor: default;
}
```

## 🔄 منطق فیلتر در Template

Template `taxonomy.html` به صورت خودکار:

1. ✅ Registry را بارگذاری می‌کند
2. ✅ `taxonomy_slug` و `taxonomy_value` را از frontmatter می‌خواند
3. ✅ Validation انجام می‌دهد
4. ✅ برای `post_type_fa` از `reverse_mapping` استفاده می‌کند
5. ✅ مقالات را فیلتر می‌کند
6. ✅ SEO metadata تولید می‌کند
7. ✅ در صورت عدم وجود مقاله، پیام Empty State نمایش می‌دهد

## ✅ معیارهای پذیرش

سیستم زمانی صحیح کار می‌کند که:

- [x] هر Badge (به‌جز readingTime) clickable باشد
- [x] URL تمیز و بدون فارسی باشد
- [x] صفحات Taxonomy فقط مقالات مرتبط را نمایش دهند
- [x] Mapping فارسی → انگلیسی درست انجام شود
- [x] هیچ مقدار Hardcode خارج از Registry نباشد
- [x] خطای 404 برای موارد نامعتبر کار کند
- [x] SEO metadata به‌درستی تولید شود

## 🚀 نحوه توسعه

### اضافه کردن Taxonomy جدید:

#### 1. به‌روزرسانی Registry (`data/taxonomies.json`):

```json
{
  "new_taxonomy": {
    "slug": "new-slug",
    "label_fa": "برچسب فارسی",
    "values": ["value1", "value2"],
    "labels": {
      "value1": "برچسب 1",
      "value2": "برچسب 2"
    }
  }
}
```

#### 2. ایجاد فولدر محتوا:

```
content/
└── new-slug/
    ├── _index.md
    ├── value1.md
    └── value2.md
```

#### 3. اضافه کردن Badge در Templates:

```go
{{ if .Params.new_taxonomy }}
    {{ $url := partial "taxonomy-url.html" (dict "taxonomy" "new_taxonomy" "value" .Params.new_taxonomy "context" .) }}
    <a href="{{ $url }}" class="meta-badge badge-new">
        <span class="badge-text">{{ .Params.new_taxonomy }}</span>
    </a>
{{ end }}
```

## 🧪 تست سیستم

### تست URLها:

```
✅ /difficulty/beginner/
✅ /difficulty/medium/
✅ /difficulty/intermediate/
✅ /difficulty/advanced/
✅ /lab_required/true/
✅ /lab_required/false/
✅ /type/tutorial/
✅ /type/article/
✅ /type/script/
✅ /type/news/
✅ /type/howto/
✅ /type/intro/
✅ /type/tool/
```

### تست Validation:

```
❌ /difficulty/invalid/ → باید 404 برگرداند
❌ /type/آموزشی/ → باید 404 برگرداند (باید از mapped value استفاده شود)
❌ /invalid-taxonomy/value/ → باید 404 برگرداند
```

## 📊 مثال‌های Metadata

### صفحه /difficulty/medium/:

```html
<title>مقالات سطح متوسط - سایت</title>
<meta name="description" content="مشاهده همه مقالات با سطح دشواری متوسط">
<link rel="canonical" href="https://example.com/difficulty/medium/">
<h1>مقالات سطح متوسط</h1>
```

### صفحه /type/tutorial/:

```html
<title>مقالات آموزشی - سایت</title>
<meta name="description" content="مشاهده همه مقالات آموزشی">
<link rel="canonical" href="https://example.com/type/tutorial/">
<h1>مقالات آموزشی</h1>
```

## 🔍 SEO Benefits

1. ✅ URL های تمیز و قابل فهم
2. ✅ Canonical URLs
3. ✅ Structured headings (H1, H2, ...)
4. ✅ Meta descriptions
5. ✅ Internal linking
6. ✅ User-friendly navigation

## 🛠️ Troubleshooting

### مشکل: Badge لینک ندارد

**راه حل:**
- بررسی کنید که در Registry تعریف شده باشد
- بررسی کنید که partial به درستی فراخوانی شده باشد
- بررسی کنید که CSS استایل `a.meta-badge` اعمال شده باشد

### مشکل: 404 برای صفحه معتبر

**راه حل:**
- بررسی کنید که فایل `.md` در content وجود داشته باشد
- بررسی کنید که frontmatter درست باشد
- بررسی کنید که `draft = false` باشد

### مشکل: Mapping فارسی به انگلیسی کار نمی‌کند

**راه حل:**
- بررسی کنید که `reverse_mapping` در Registry صحیح باشد
- بررسی کنید که مقدار فارسی دقیقاً مطابق با Registry باشد
- بررسی کنید که از `taxonomy_slug = "post_type_fa"` استفاده شده باشد

## 📚 منابع مرتبط

- `layouts/_default/taxonomy.html` - Template اصلی
- `layouts/partials/taxonomy-url.html` - Helper تولید URL
- `data/taxonomies.json` - Registry مرکزی
- `assets/css/main.css` - استایل Badgeها

## 🎉 نتیجه

این سیستم یک راه‌حل کامل، مقیاس‌پذیر و SEO-friendly برای مدیریت Taxonomyها و Badgeها در Hugo فراهم می‌کند. با استفاده از Registry مرکزی، تمام تغییرات از یک نقطه قابل مدیریت هستند و سیستم به راحتی قابل توسعه است.
