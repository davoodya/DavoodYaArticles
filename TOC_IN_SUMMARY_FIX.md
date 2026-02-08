# 📋 اصلاح نمایش TOC در توضیحات کوتاه

> **تاریخ**: 2026-02-08  
> **نسخه**: 3.0

---

## 🎯 هدف

نمایش TOC (Table of Contents) در توضیحات کوتاه مقالات به صورت **فرمت شده** (HTML) به جای Plain Text.

---

## ❌ مشکل قبلی

### Template قبلی:

```html
<div class="article-card-summary">
    {{ .Summary | plainify | truncate 200 }}
</div>
```

### نتیجه:

```
## E6 to E9 - Find Keywords... - [Find Keywords](#Find Keywords)...
```

**مشکلات:**
- ❌ فرمت markdown حذف شده (plainify)
- ❌ لینک‌ها کار نمی‌کنند
- ❌ لیست‌ها به صورت plain text
- ❌ headings به صورت plain text
- ❌ خوانایی پایین

---

## ✅ راه‌حل

### 1. حذف `plainify` از Template

**فایل**: `layouts/_default/list.html`

```html
<!-- قبل -->
<div class="article-card-summary">
    {{ .Summary | plainify | truncate 200 }}
</div>

<!-- بعد -->
<div class="article-card-summary">
    {{ .Summary | truncate 500 }}
</div>
```

**تغییرات:**
- ✅ حذف `plainify` → HTML render می‌شود
- ✅ افزایش `truncate` از 200 به 500 → TOC کامل نمایش داده می‌شود
- ✅ استفاده از `.Summary` به جای `.Content`

---

### 2. اضافه کردن استایل CSS برای TOC

**فایل**: `assets/css/main.css`

```css
/* Style lists in summary (TOC) */
.article-card-summary ul,
.article-card-summary ol {
    padding-right: 1.5rem;
    padding-left: 0;
    margin: 0.5rem 0;
}

.article-card-summary li {
    margin-bottom: 0.3rem;
    line-height: 1.6;
}

.article-card-summary ul li::marker {
    color: var(--accent-green);
}

.article-card-summary ol li::marker {
    color: var(--accent-blue);
}

/* Style headings in summary */
.article-card-summary h2,
.article-card-summary h3,
.article-card-summary h4 {
    color: var(--accent-green);
    font-size: 1rem;
    margin: 0.5rem 0;
    font-weight: 600;
}

/* Style links in summary (TOC links) */
.article-card-summary a {
    color: var(--accent-blue);
    text-decoration: none;
    transition: all 0.3s ease;
    border-bottom: 1px dashed transparent;
}

.article-card-summary a:hover {
    color: var(--accent-green);
    border-bottom-color: var(--accent-green);
}

/* Nested lists in summary */
.article-card-summary ul ul,
.article-card-summary ul ol,
.article-card-summary ol ul,
.article-card-summary ol ol {
    margin-top: 0.2rem;
    margin-bottom: 0.2rem;
    padding-right: 1rem;
}
```

---

### 3. بهبود JavaScript

**فایل**: `static/assets/js/auto-direction.js`

```javascript
function processArticleCards() {
    document.querySelectorAll('.article-card-summary').forEach(card => {
        if (card.getAttribute('data-processed')) return;
        
        // Hide images with CSS (but keep TOC and text)
        card.querySelectorAll('img').forEach(img => {
            img.style.display = 'none';
        });
        
        // Make sure TOC links are styled properly
        card.querySelectorAll('a').forEach(link => {
            link.style.pointerEvents = 'auto';
            link.style.cursor = 'pointer';
        });
        
        card.setAttribute('data-processed', 'true');
    });
}
```

---

## 📊 مقایسه Before/After

### Before (Plain Text):

```
## E6 to E9 - (Find Keywords, Website Structure...) - [Find Keywords](#Find Keywords) - [Google Ads](#Google Ads) - [Basic & Concepts](#Basic & Concepts)...
```

**مشکلات:**
- ❌ بدون فرمت
- ❌ لینک‌ها plain text
- ❌ لیست‌ها نامرتب
- ❌ خوانایی پایین

---

### After (Formatted HTML):

```html
<h2>E6 to E9 - (Find Keywords, Website Structure...)</h2>
<ul>
  <li>
    <a href="#Find-Keywords">Find Keywords</a>
    <ul>
      <li><a href="#Google-Ads">Google Ads</a></li>
      <li><a href="#Competitors">Competitor's</a></li>
    </ul>
  </li>
  <li>
    <a href="#Website-Structure">Website Structure</a>
  </li>
  <li>
    <a href="#HTML-Tags-for-SEO">HTML Tags for SEO</a>
  </li>
</ul>
```

**نمایش:**

## E6 to E9 - (Find Keywords, Website Structure...)
- **[Find Keywords](#Find-Keywords)** ← کلیک می‌شود
  - [Google Ads](#Google-Ads)
  - [Competitor's](#Competitors)
- **[Website Structure](#Website-Structure)**
- **[HTML Tags for SEO](#HTML-Tags-for-SEO)**

**مزایا:**
- ✅ فرمت شده و خوانا
- ✅ لینک‌ها کار می‌کنند
- ✅ ساختار سلسله مراتبی
- ✅ استایل‌های رنگی

---

## 🎨 استایل‌های اعمال شده

### Headings:
```css
color: var(--accent-green)  /* سبز */
font-size: 1rem
font-weight: 600
```

### Links:
```css
color: var(--accent-blue)   /* آبی */
hover: var(--accent-green)  /* سبز در hover */
border-bottom: dashed       /* خط زیر دش دار */
```

### List Items:
```css
padding-right: 1.5rem       /* فاصله از راست */
margin-bottom: 0.3rem       /* فاصله بین آیتم‌ها */
```

### Markers:
```css
ul li::marker: green        /* نقطه سبز */
ol li::marker: blue         /* شماره آبی */
```

---

## 🔗 نحوه کار لینک‌ها

### لینک در Summary Card:

```html
<a href="/articles/seo/.../#Find-Keywords">Find Keywords</a>
```

**کلیک روی لینک:**
1. کاربر به صفحه مقاله می‌رود
2. مرورگر به بخش `#Find-Keywords` scroll می‌کند
3. بخش مورد نظر نمایش داده می‌شود

---

## 📝 مثال کامل

### Markdown مقاله:

```markdown
+++
title = "SEO Tutorial"
+++

## Table of Contents
- [Introduction](#introduction)
  - [What is SEO](#what-is-seo)
  - [Why SEO](#why-seo)
- [Keywords](#keywords)
- [Optimization](#optimization)

### Introduction
#### What is SEO
...
```

### نمایش در Summary Card:

```html
<div class="article-card-summary">
  <h2>Table of Contents</h2>
  <ul>
    <li>
      <a href="/articles/seo-tutorial/#introduction">Introduction</a>
      <ul>
        <li><a href="/articles/seo-tutorial/#what-is-seo">What is SEO</a></li>
        <li><a href="/articles/seo-tutorial/#why-seo">Why SEO</a></li>
      </ul>
    </li>
    <li><a href="/articles/seo-tutorial/#keywords">Keywords</a></li>
    <li><a href="/articles/seo-tutorial/#optimization">Optimization</a></li>
  </ul>
</div>
```

---

## ⚙️ تنظیمات Hugo

### در `hugo.toml`:

```toml
# Summary settings
summaryLength = 70  # تعداد کلمات در summary
```

**نکته:** اگر مقاله `<!--more-->` داشته باشد، Hugo آن را به عنوان summary استفاده می‌کند.

---

## 🧪 تست

### مرحله 1: Rebuild Hugo

```bash
hugo --gc --minify
```

### مرحله 2: اجرای سرور

```bash
hugo server -D
```

### مرحله 3: باز کردن صفحه دسته‌بندی

```
http://localhost:1313/articles/seo/
```

### انتظار:

✅ TOC به صورت لیست فرمت شده  
✅ لینک‌ها با رنگ آبی  
✅ Hover روی لینک → سبز می‌شود  
✅ کلیک روی لینک → به صفحه مقاله + scroll به بخش  
✅ تصاویر مخفی  
✅ ساختار سلسله مراتبی مشخص  

---

## 📂 فایل‌های تغییر یافته

### 1. `layouts/_default/list.html`
```diff
- {{ .Summary | plainify | truncate 200 }}
+ {{ .Summary | truncate 500 }}
```

### 2. `assets/css/main.css`
```css
+ .article-card-summary ul, ol { ... }
+ .article-card-summary li { ... }
+ .article-card-summary h2, h3, h4 { ... }
+ .article-card-summary a { ... }
```

### 3. `static/assets/js/auto-direction.js`
```javascript
+ card.querySelectorAll('a').forEach(link => {
+     link.style.pointerEvents = 'auto';
+     link.style.cursor = 'pointer';
+ });
```

---

## 🎯 ویژگی‌های آینده

### 1. کلیک روی لینک بدون بارگذاری صفحه

```javascript
document.querySelectorAll('.article-card-summary a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const url = link.href;
        // AJAX load content
        // Smooth scroll to section
    });
});
```

### 2. Collapse/Expand TOC

```javascript
const tocHeader = card.querySelector('h2');
tocHeader.addEventListener('click', () => {
    card.classList.toggle('collapsed');
});
```

### 3. Highlight کردن بخش فعال

```javascript
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Highlight corresponding TOC item
        }
    });
});
```

---

## 🐛 عیب‌یابی

### مشکل: TOC هنوز plain text است

**راه‌حل:**
1. Clear browser cache (Ctrl+Shift+Del)
2. Hugo rebuild: `hugo --gc --minify`
3. بررسی HTML source:

```javascript
// در console browser:
document.querySelector('.article-card-summary').innerHTML
```

**انتظار:** باید HTML باشد نه plain text.

---

### مشکل: لینک‌ها کار نمی‌کنند

**راه‌حل:**
1. بررسی که `pointer-events: auto` است
2. بررسی console برای خطاهای JavaScript
3. بررسی که لینک‌ها href صحیح دارند:

```javascript
document.querySelectorAll('.article-card-summary a').forEach(link => {
    console.log(link.href);
});
```

---

### مشکل: استایل‌ها اعمال نمی‌شوند

**راه‌حل:**
1. بررسی که CSS load شده
2. بررسی specificity:

```css
/* اگر کار نکرد، !important اضافه کنید */
.article-card-summary ul {
    padding-right: 1.5rem !important;
}
```

---

## ✅ چک‌لیست

- [x] حذف `plainify` از template
- [x] افزایش `truncate` به 500
- [x] اضافه کردن استایل CSS برای lists
- [x] اضافه کردن استایل CSS برای links
- [x] اضافه کردن استایل CSS برای headings
- [x] بهبود JavaScript برای links
- [x] تست در Chrome
- [x] تست در Firefox
- [x] تست در mobile

---

## 📚 منابع

- [Hugo Summary Documentation](https://gohugo.io/content-management/summaries/)
- [Hugo Template Functions](https://gohugo.io/functions/)
- [CSS Lists Styling](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style)

---

**نویسنده**: Davood Yahya  
**تاریخ**: 2026-02-08  
**نسخه**: 3.0

---

**پایان مستندات** 🎉
