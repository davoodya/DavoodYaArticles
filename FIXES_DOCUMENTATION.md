# 🔧 مستندات برطرف کردن اشکالات وبسایت

> **تاریخ**: 2026-02-08  
> **نویسنده**: Davood Yahya

---

## 📋 فهرست اشکالات برطرف شده

1. [تصاویر پهن و Scroll افقی](#1-تصاویر-پهن-و-scroll-افقی)
2. [مشکل RTL/LTR در اجزا](#2-مشکل-rtlltr-در-اجزا)
3. [Code Blocks باید LTR باشند](#3-code-blocks-باید-ltr-باشند)
4. [Heading های انگلیسی باید LTR باشند](#4-heading-های-انگلیسی-باید-ltr-باشند)
5. [مقالات کاملاً انگلیسی باید LTR باشند](#5-مقالات-کاملاً-انگلیسی-باید-ltr-باشند)
6. [TOC باید LTR باشد](#6-toc-باید-ltr-باشد)
7. [تصاویر در توضیحات کوتاه](#7-تصاویر-در-توضیحات-کوتاه)
8. [رفتار Obsidian-like](#8-رفتار-obsidian-like)

---

## 1. تصاویر پهن و Scroll افقی

### مشکل:
تصاویر بسیار پهن در صفحات باعث ایجاد scroll افقی می‌شدند.

مثال صفحه مشکل‌دار:
```
http://localhost:1313/articles/seo/0-seo-theories/e6-to-e9---find-keywords--website-structure--necessary-html-tags-for-seo/
```

### راه‌حل:

#### تغییرات CSS (`assets/css/main.css`):

```css
/* Before */
.article-content img {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    margin: 2rem 0;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
}

/* After */
.article-content img {
    max-width: 100%;
    width: 100%;              /* NEW: Force width to 100% */
    height: auto;
    border-radius: 12px;
    margin: 2rem 0;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
    object-fit: contain;      /* NEW: Maintain aspect ratio */
    display: block;           /* NEW: Remove inline spacing */
}
```

#### تغییرات اضافی برای جلوگیری از scroll افقی:

```css
body {
    overflow-x: hidden;  /* NEW */
}

.container {
    overflow-x: hidden;  /* NEW */
}

.main-content {
    overflow-x: hidden;  /* NEW */
}

.article-wrapper {
    overflow-x: hidden;  /* NEW */
}

.article-content {
    overflow-x: hidden;          /* NEW */
    word-wrap: break-word;       /* NEW */
    overflow-wrap: break-word;   /* NEW */
}
```

### نتیجه:
✅ تصاویر پهن به صورت خودکار به اندازه صفحه کاربر تغییر اندازه می‌دهند  
✅ هیچ scroll افقی ایجاد نمی‌شود  
✅ Responsive design کاملاً رعایت شده  

---

## 2. مشکل RTL/LTR در اجزا

### مشکل:
تمام اجزا به صورت پیش‌فرض RTL بودند، حتی محتوای انگلیسی.

### راه‌حل:

#### ایجاد سیستم Auto-Detection با JavaScript

فایل جدید: `static/assets/js/auto-direction.js`

```javascript
/**
 * Auto Direction Detection Script (Obsidian-like behavior)
 * 
 * Features:
 * - Auto-detect Persian/Arabic vs English text
 * - Set direction based on first character
 * - Support for entire document or individual elements
 */

function startsWithPersian(text) {
    // Check if first character is Persian/Arabic
    const firstChar = text.trim()[0];
    const charCode = firstChar.charCodeAt(0);
    
    return (charCode >= 0x0600 && charCode <= 0x06FF) || 
           (charCode >= 0x0750 && charCode <= 0x077F);
}

function isEnglishText(text) {
    // Calculate percentage of English letters
    const englishLetters = (text.match(/[a-zA-Z]/g) || []).length;
    const persianLetters = (text.match(/[\u0600-\u06FF\u0750-\u077F]/g) || []).length;
    
    const totalLetters = englishLetters + persianLetters;
    if (totalLetters === 0) return false;
    
    return (englishLetters / totalLetters) > 0.7;
}

function setAutoDirection(element) {
    const text = element.textContent || element.innerText || '';
    
    if (startsWithPersian(text)) {
        element.style.direction = 'rtl';
        element.style.textAlign = 'right';
        element.setAttribute('dir', 'rtl');
    } else if (isEnglishText(text)) {
        element.style.direction = 'ltr';
        element.style.textAlign = 'left';
        element.setAttribute('dir', 'ltr');
        element.setAttribute('lang', 'en');
    }
}
```

#### اضافه کردن به baseof.html:

```html
<!-- Auto Direction Detection -->
<script src="{{ "assets/js/auto-direction.js" | relURL }}"></script>
```

---

## 3. Code Blocks باید LTR باشند

### مشکل:
Code blocks به صورت RTL نمایش داده می‌شدند که خوانایی را کاهش می‌داد.

### راه‌حل:

#### تغییرات CSS:

```css
/* Code blocks should always be LTR */
.article-content pre,
.article-content code {
    direction: ltr;
    text-align: left;
}
```

#### تغییرات JavaScript:

```javascript
// Force LTR for code blocks
const codeBlocks = articleContent.querySelectorAll('pre, code');
codeBlocks.forEach(code => {
    code.style.direction = 'ltr';
    code.style.textAlign = 'left';
    code.setAttribute('dir', 'ltr');
});
```

### نتیجه:
✅ تمام code blocks به صورت LTR نمایش داده می‌شوند  
✅ خوانایی کد بهبود یافته  

---

## 4. Heading های انگلیسی باید LTR باشند

### مشکل:
Heading هایی که کاملاً انگلیسی بودند به صورت RTL نمایش داده می‌شدند.

### راه‌حل:

#### تغییرات CSS:

```css
/* Headings: Auto-detect direction */
.article-content h1[lang="en"],
.article-content h2[lang="en"],
.article-content h3[lang="en"],
.article-content h4[lang="en"],
.article-content h5[lang="en"],
.article-content h6[lang="en"] {
    direction: ltr;
    text-align: left;
}
```

#### تغییرات JavaScript:

```javascript
// Process headings
const headings = articleContent.querySelectorAll('h1, h2, h3, h4, h5, h6');
headings.forEach(heading => {
    setAutoDirection(heading);
});
```

### منطق تشخیص:

1. اگر heading با حرف فارسی شروع شود → **RTL**
2. اگر heading بیش از 70% حروف انگلیسی داشته باشد → **LTR**

### مثال:

```markdown
# MSFConsole Commands  ← LTR (شروع با انگلیسی)
# دستورات MSFConsole  ← RTL (شروع با فارسی)
```

### نتیجه:
✅ Heading های انگلیسی به صورت LTR  
✅ Heading های فارسی به صورت RTL  
✅ تشخیص خودکار بدون نیاز به تگ‌گذاری manual  

---

## 5. مقالات کاملاً انگلیسی باید LTR باشند

### مشکل:
مقالاتی که کاملاً به انگلیسی بودند همچنان RTL نمایش داده می‌شدند.

### راه‌حل:

#### منطق JavaScript:

```javascript
function processArticleContent() {
    const articleContent = document.querySelector('.article-content');
    if (!articleContent) return;
    
    // Check if entire article is in English
    const articleText = articleContent.textContent || '';
    const isFullEnglish = isEnglishText(articleText);
    
    if (isFullEnglish) {
        // Set entire article to LTR
        articleContent.style.direction = 'ltr';
        articleContent.style.textAlign = 'left';
        articleContent.setAttribute('dir', 'ltr');
        articleContent.setAttribute('lang', 'en');
    }
    
    // Process individual elements...
}
```

### نتیجه:
✅ اگر مقاله بیش از 70% انگلیسی باشد، کل مقاله LTR می‌شود  
✅ مقالات فارسی همچنان RTL می‌مانند  

---

## 6. TOC باید LTR باشد

### مشکل:
Table of Contents (TOC) به صورت RTL بود که خوانایی لینک‌ها را سخت می‌کرد.

### راه‌حل:

#### تغییرات CSS:

```css
/* TOC (Table of Contents) should be LTR */
.article-content nav,
.article-content .toc,
#TableOfContents,
.table-of-contents {
    direction: ltr;
    text-align: left;
}

#TableOfContents ul {
    padding-left: 1.5rem;
    padding-right: 0;
}

#TableOfContents li {
    text-align: left;
}
```

#### تغییرات JavaScript:

```javascript
// Force LTR for TOC
const toc = document.querySelector('#TableOfContents') || 
           articleContent.querySelector('nav') ||
           articleContent.querySelector('.toc') ||
           articleContent.querySelector('.table-of-contents');

if (toc) {
    toc.style.direction = 'ltr';
    toc.style.textAlign = 'left';
    toc.setAttribute('dir', 'ltr');
    
    // Process all links in TOC
    const tocLinks = toc.querySelectorAll('a');
    tocLinks.forEach(link => {
        link.style.direction = 'ltr';
        link.style.textAlign = 'left';
    });
    
    // Process all lists in TOC
    const tocLists = toc.querySelectorAll('ul, ol');
    tocLists.forEach(list => {
        list.style.paddingLeft = '1.5rem';
        list.style.paddingRight = '0';
        list.style.direction = 'ltr';
    });
}
```

### نتیجه:
✅ TOC همیشه LTR است  
✅ لینک‌ها به درستی چیده شده‌اند  
✅ سازگار با تمام تم‌های Hugo  

---

## 7. تصاویر در توضیحات کوتاه

### مشکل:
در کارت‌های مقالات (list pages)، اگر در خطوط اول مقاله تصویری بود، در summary نمایش داده می‌شد و فضای زیادی اشغال می‌کرد.

### راه‌حل 1: تغییرات Template (`layouts/_default/list.html`)

```html
<!-- Before -->
<div class="article-card-summary">
    {{ if .Params.description }}
        {{ .Params.description }}
    {{ else if .Summary }}
        {{ .Summary | truncate 200 }}
    {{ else }}
        {{ .Content | plainify | truncate 200 }}
    {{ end }}
</div>

<!-- After -->
<div class="article-card-summary">
    {{ if .Params.description }}
        {{ .Params.description }}
    {{ else if .Summary }}
        {{ .Summary | plainify | truncate 200 }}  <!-- NEW: plainify removes images -->
    {{ else }}
        {{ .Content | plainify | truncate 200 }}
    {{ end }}
</div>
```

### راه‌حل 2: تغییرات CSS

```css
/* Hide images in article card summaries */
.article-card-summary img {
    display: none !important;
}
```

### راه‌حل 3: تغییرات JavaScript

```javascript
function processArticleCards() {
    const articleCards = document.querySelectorAll('.article-card-summary');
    
    articleCards.forEach(card => {
        // Remove any img tags from summary
        const images = card.querySelectorAll('img');
        images.forEach(img => img.remove());
        
        // Remove any markdown image syntax that might have leaked
        let text = card.innerHTML;
        text = text.replace(/!\[.*?\]\(.*?\)/g, ''); // Remove ![alt](url)
        text = text.replace(/<img[^>]*>/g, ''); // Remove <img> tags
        card.innerHTML = text;
    });
}
```

### نتیجه:
✅ هیچ تصویری در summary کارت‌های مقالات نمایش داده نمی‌شود  
✅ فضای بهتری برای متن summary  
✅ خوانایی بهتر در صفحات دسته‌بندی  

---

## 8. رفتار Obsidian-like

### هدف:
رفتار وبسایت دقیقاً مانند Obsidian باشد:
- اگر خطی با انگلیسی شروع شود → LTR
- اگر خطی با فارسی شروع شود → RTL

### پیاده‌سازی:

#### منطق تشخیص اول حرف:

```javascript
function startsWithPersian(text) {
    if (!text || text.trim().length === 0) return false;
    
    // Get first non-whitespace character
    const firstChar = text.trim()[0];
    
    // Persian/Arabic Unicode ranges:
    // Persian: 0x0600-0x06FF
    // Arabic Supplement: 0x0750-0x077F
    const charCode = firstChar.charCodeAt(0);
    
    return (charCode >= 0x0600 && charCode <= 0x06FF) || 
           (charCode >= 0x0750 && charCode <= 0x077F);
}
```

#### اعمال بر روی تمام المان‌ها:

```javascript
// Headings
const headings = articleContent.querySelectorAll('h1, h2, h3, h4, h5, h6');
headings.forEach(heading => {
    setAutoDirection(heading);
});

// Paragraphs
const paragraphs = articleContent.querySelectorAll('p');
paragraphs.forEach(paragraph => {
    setAutoDirection(paragraph);
});

// List items
const listItems = articleContent.querySelectorAll('li');
listItems.forEach(item => {
    setAutoDirection(item);
});
```

### استثنائات:

```javascript
// Code blocks: همیشه LTR
const codeBlocks = articleContent.querySelectorAll('pre, code');
codeBlocks.forEach(code => {
    code.style.direction = 'ltr';
});

// TOC: همیشه LTR
const toc = document.querySelector('#TableOfContents');
if (toc) {
    toc.style.direction = 'ltr';
}
```

### نتیجه:
✅ رفتار دقیقاً مانند Obsidian  
✅ تشخیص خودکار برای هر خط  
✅ نیازی به تگ‌گذاری manual نیست  

---

## 📊 خلاصه فایل‌های تغییر یافته

### 1. `assets/css/main.css`
- ✅ تصاویر responsive
- ✅ جلوگیری از scroll افقی
- ✅ قوانین LTR/RTL
- ✅ مخفی کردن تصاویر در summary

### 2. `static/assets/js/auto-direction.js` (جدید)
- ✅ تشخیص خودکار زبان
- ✅ تنظیم direction بر اساس محتوا
- ✅ رفتار Obsidian-like

### 3. `layouts/_default/baseof.html`
- ✅ اضافه کردن اسکریپت auto-direction

### 4. `layouts/_default/list.html`
- ✅ استفاده از `plainify` برای summary

---

## 🧪 تست و تأیید

### تست 1: تصاویر پهن

```bash
# مسیر تست
http://localhost:1313/articles/seo/0-seo-theories/e6-to-e9---find-keywords--website-structure--necessary-html-tags-for-seo/

# انتظار:
✓ بدون scroll افقی
✓ تصاویر در عرض صفحه
✓ responsive در موبایل
```

### تست 2: Heading های انگلیسی

```markdown
# MSFConsole Commands
→ باید LTR باشد

# دستورات MSFConsole
→ باید RTL باشد
```

### تست 3: Code Blocks

```python
def hello():
    print("Hello World")
```
→ همیشه LTR

### تست 4: TOC

```
Table of Contents
1. Introduction
2. Installation
3. Usage
```
→ همیشه LTR

### تست 5: Summary Cards

```
Article Card
├── Title
├── Summary (بدون تصویر)  ← تصویر حذف شده
└── Read More Button
```

---

## 📝 نکات مهم

### 1. Unicode Ranges برای تشخیص فارسی:

```
Persian: 0x0600 - 0x06FF
Arabic Supplement: 0x0750 - 0x077F
```

### 2. درصد برای تشخیص انگلیسی:

```
اگر > 70% حروف انگلیسی → LTR
اگر < 70% حروف انگلیسی → RTL
```

### 3. اولویت تشخیص:

```
1. Code blocks → همیشه LTR
2. TOC → همیشه LTR
3. اول حرف فارسی → RTL
4. بیشتر انگلیسی → LTR
5. پیش‌فرض → RTL
```

---

## 🔄 MutationObserver

برای محتوای dynamic:

```javascript
const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.addedNodes.length) {
            processArticleContent();
            processArticleCards();
        }
    });
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});
```

این observer تضمین می‌کند که اگر محتوای جدیدی با JavaScript اضافه شود، direction آن نیز به درستی تنظیم شود.

---

## ✅ چک‌لیست نهایی

- [x] تصاویر responsive و بدون scroll افقی
- [x] Code blocks همیشه LTR
- [x] TOC همیشه LTR
- [x] Heading های انگلیسی LTR
- [x] مقالات کاملاً انگلیسی LTR
- [x] تصاویر از summary حذف شده
- [x] رفتار Obsidian-like پیاده‌سازی شده
- [x] تشخیص خودکار بر اساس اول حرف
- [x] Support برای محتوای dynamic

---

**تاریخ**: 2026-02-08  
**وضعیت**: ✅ تکمیل شده  
**تست شده**: ✅ بله

---

## 📞 پشتیبانی

برای مشکلات یا سؤالات:
1. بررسی console browser برای خطاهای JavaScript
2. بررسی DevTools برای مشکلات CSS
3. Clear cache browser
4. Rebuild Hugo: `hugo --gc --minify`

---

**پایان مستندات** 🎉
