# 🆕 ویژگی‌های جدید اضافه شده

> **تاریخ**: 2026-02-08  
> **نسخه**: 3.0

---

## 📋 فهرست ویژگی‌های جدید

1. [Syntax Highlighting با Highlight.js](#1-syntax-highlighting)
2. [بهبود توضیحات کوتاه مقالات](#2-بهبود-توضیحات-کوتاه)
3. [جلوگیری کامل از Horizontal Scroll](#3-جلوگیری-از-horizontal-scroll)

---

## 1. Syntax Highlighting

### مشکل قبلی:
Code blocks فقط یک syntax highlighting ساده داشتند که برای زبان‌های مختلف کامل نبود.

### راه‌حل:

#### اضافه کردن Highlight.js

**فایل**: `layouts/_default/baseof.html`

```html
<!-- Highlight.js for Syntax Highlighting -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">

<!-- Scripts -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/javascript.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/java.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/csharp.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/php.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/ruby.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/go.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/rust.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/bash.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/sql.min.js"></script>
<script>hljs.highlightAll();</script>
```

### زبان‌های پشتیبانی شده:

- ✅ Python
- ✅ JavaScript
- ✅ Java
- ✅ C#
- ✅ PHP
- ✅ Ruby
- ✅ Go
- ✅ Rust
- ✅ Bash/Shell
- ✅ SQL
- ✅ HTML/CSS (built-in)

### نحوه استفاده:

#### در Markdown:

```markdown
```python
def hello_world():
    print("Hello, World!")
    return True
\```

```javascript
function helloWorld() {
    console.log("Hello, World!");
    return true;
}
\```

```bash
#!/bin/bash
echo "Hello, World!"
\```
```

### تم:
استفاده از تم **Atom One Dark** که با تم cyberpunk وبسایت هماهنگی دارد.

### مزایا:
- ✅ Auto-detection زبان
- ✅ Syntax highlighting کامل
- ✅ رنگ‌بندی حرفه‌ای
- ✅ سازگار با تمام زبان‌های برنامه‌نویسی محبوب
- ✅ سبک و سریع (CDN)

---

## 2. بهبود توضیحات کوتاه

### مشکل قبلی:
توضیحات کوتاه شامل:
- ❌ Heading ها (H1, H2, H3, ...)
- ❌ TOC (Table of Contents)
- ❌ لیست‌ها
- ❌ تصاویر

### راه‌حل:

#### الگوریتم استخراج پاراگراف اول

**فایل**: `static/assets/js/auto-direction.js`

```javascript
function extractFirstParagraph(text) {
    if (!text) return '';
    
    // Remove all heading patterns
    text = text.replace(/^#+\s+.*$/gm, '');
    
    // Remove TOC patterns
    text = text.replace(/^-\s+\[.*?\]\(.*?\)$/gm, '');
    text = text.replace(/^\s*TOC\s*$/gmi, '');
    
    // Remove list patterns
    text = text.replace(/^[\*\-]\s+.*$/gm, '');
    
    // Remove numbered lists
    text = text.replace(/^\d+\.\s+.*$/gm, '');
    
    // Remove empty lines
    text = text.replace(/^\s*[\r\n]/gm, '');
    
    // Get first paragraph
    const paragraphs = text.split(/\n\n+/);
    for (let para of paragraphs) {
        para = para.trim();
        if (para.length > 30 && !para.match(/^#+/) && !para.match(/^[\-\*]/)) {
            return para;
        }
    }
    
    return text.substring(0, 200);
}
```

### مثال:

#### محتوای مقاله:
```markdown
# TOC
- [Introduction](#introduction)
- [Setup](#setup)

## Introduction

امنیت شبکه مجموعه‌ای از تکنولوژی‌ها و فناوری‌هاست که از قابلیت 
Usability(استفاده) و Integrity(تجمیع) شبکه و زیرساخت یک شرکت محافظت می‌کند.
از امنیت شبکه برای جلوگیری از ورود یا تکثیر بدافزارها و تهدیدات 
بالقوه درون شبکه استفاده می‌شود.
```

#### توضیحات کوتاه نمایش داده شده:
```
امنیت شبکه مجموعه‌ای از تکنولوژی‌ها و فناوری‌هاست که از قابلیت 
Usability(استفاده) و Integrity(تجمیع) شبکه و زیرساخت یک شرکت محافظت می‌کند.
از امنیت شبکه برای جلوگیری از ورود یا تکثیر بدافزارها و تهدیدات 
بالقوه درون شبکه استفاده می‌شود.
```

### مزایا:
- ✅ فقط پاراگراف اول
- ✅ بدون heading ها
- ✅ بدون TOC
- ✅ بدون لیست‌ها
- ✅ بدون تصاویر
- ✅ خلاصه واقعی محتوا

---

## 3. جلوگیری از Horizontal Scroll

### مشکل قبلی:
بعضی صفحات (مثل SEO articles) width بیشتر از 100% داشتند:
```
مسیر مشکل‌دار:
content/seo/0-SEO-Theories/E6 to E9 - Find Keywords, Website Structure & Necessary HTML Tags for SEO.md
```

### راه‌حل:

#### 1. Global Rules

**فایل**: `assets/css/main.css`

```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    max-width: 100%;  /* NEW */
}

/* Allow specific elements to exceed 100% width */
body, html, .container, .main-content-wrapper, 
.main-content, .article-wrapper {
    max-width: none;
}
```

#### 2. HTML و Body

```css
html {
    direction: rtl;
    scroll-behavior: smooth;
    font-size: 16px;
    overflow-x: hidden;      /* NEW */
    max-width: 100vw;        /* NEW */
}

body {
    overflow-x: hidden;      /* NEW */
}
```

#### 3. Main Content Wrapper

```css
.main-content-wrapper {
    display: grid;
    grid-template-columns: 350px 1fr;
    gap: 3rem;
    max-width: 100%;         /* NEW */
    overflow-x: hidden;      /* NEW */
}
```

#### 4. Images (قبلاً اضافه شده)

```css
.article-content img {
    max-width: 100%;
    width: 100%;
    height: auto;
    object-fit: contain;
    display: block;
}
```

#### 5. Tables

```css
.article-content table {
    width: 100%;
    max-width: 100%;         /* NEW */
    display: block;          /* NEW */
    overflow-x: auto;        /* NEW: Scroll only for table */
}
```

#### 6. Pre/Code Blocks

```css
.article-content pre {
    max-width: 100%;
    overflow-x: auto;        /* Scroll only for code */
    white-space: pre;
}
```

### استراتژی:

```
قوانین کلی:
├── همه المان‌ها: max-width: 100%
├── Containers: overflow-x: hidden
├── Images: width: 100% + object-fit: contain
├── Tables: display: block + overflow-x: auto
└── Code blocks: overflow-x: auto
```

### نتیجه:
- ✅ هیچ صفحه‌ای horizontal scroll ندارد
- ✅ تصاویر بزرگ به صورت خودکار resize می‌شوند
- ✅ Table های بزرگ فقط خودشان scroll می‌شوند
- ✅ Code های طولانی فقط خودشان scroll می‌شوند
- ✅ کاملاً responsive

---

## 📊 خلاصه تغییرات فایل‌ها

### تغییر یافته:

1. ✅ `layouts/_default/baseof.html`
   - اضافه کردن Highlight.js CSS
   - اضافه کردن Highlight.js Scripts

2. ✅ `assets/css/main.css`
   - Global max-width rules
   - overflow-x: hidden
   - بهبود responsive

3. ✅ `static/assets/js/auto-direction.js`
   - تابع extractFirstParagraph()
   - بهبود processArticleCards()

4. ✅ `layouts/_default/list.html`
   - ساده‌سازی summary

5. ✅ `hugo.toml`
   - تنظیمات markup

---

## 🧪 تست

### 1. Syntax Highlighting:

```bash
# باز کردن مقاله‌ای با code blocks
http://localhost:1313/articles/tools/msfconsole-commands/
```

**انتظار:**
- Code blocks رنگ‌آمیزی شده
- زبان به درستی تشخیص داده شده
- تم Atom One Dark

---

### 2. توضیحات کوتاه:

```bash
# باز کردن صفحه دسته‌بندی
http://localhost:1313/articles/cyber-security/
```

**انتظار:**
- فقط پاراگراف اول
- بدون heading
- بدون TOC
- بدون تصویر

---

### 3. Horizontal Scroll:

```bash
# باز کردن صفحه SEO
http://localhost:1313/articles/seo/0-seo-theories/e6-to-e9---find-keywords--website-structure--necessary-html-tags-for-seo/
```

**انتظار:**
- بدون horizontal scroll
- تصاویر در عرض صفحه
- responsive کامل

---

## ✨ مزایای کلی

### عملکرد:
- ⚡ Syntax highlighting سریع (CDN)
- ⚡ No re-processing of already processed elements
- ⚡ بهینه‌سازی شده برای mobile

### کاربری:
- 👁️ خوانایی بهتر کدها
- 👁️ توضیحات کوتاه واضح‌تر
- 👁️ تجربه کاربری بهتر (no horizontal scroll)

### SEO:
- 🔍 توضیحات کوتاه بهتر برای search engines
- 🔍 محتوای واقعی در summaries
- 🔍 structure بهتر

---

## 📝 نکات مهم

### 1. افزودن زبان جدید به Highlight.js:

```html
<!-- Add new language -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/kotlin.min.js"></script>
```

### 2. تغییر تم Syntax Highlighting:

```html
<!-- Change theme -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/monokai.min.css">
```

تم‌های محبوب:
- atom-one-dark (فعلی)
- monokai
- dracula
- github-dark
- vs2015

### 3. غیرفعال کردن استخراج خودکار پاراگراف:

اگر می‌خواهید برای یک مقاله خاص از `description` استفاده کنید:

```markdown
+++
title = "مقاله من"
description = "این توضیحات دستی من است"
+++
```

---

## 🔧 عیب‌یابی

### مشکل: Code ها رنگ‌آمیزی نمی‌شوند

**راه‌حل:**
1. Clear browser cache
2. Check console for errors
3. Verify Highlight.js loaded: `console.log(hljs)`

---

### مشکل: توضیحات کوتاه هنوز شامل TOC است

**راه‌حل:**
1. Clear browser cache
2. Refresh page (Ctrl+F5)
3. Check console for JavaScript errors

---

### مشکل: هنوز horizontal scroll دارم

**راه‌حل:**
1. Clear browser cache
2. Hugo rebuild: `hugo --gc --minify`
3. بررسی Developer Tools برای element عریض
4. Check for inline styles on images

---

**تاریخ**: 2026-02-08  
**وضعیت**: ✅ تکمیل شده  
**نسخه**: 3.0

---

**پایان مستندات** 🎉
