# 📝 راهنمای استایل‌نویسی برای صفحات خاص

> **تاریخ**: 2026-02-08

---

## 🎯 هدف

این سیستم به شما اجازه می‌دهد که برای صفحات خاص استایل‌های سفارشی تعریف کنید بدون اینکه روی سایر صفحات تأثیر بگذارد.

---

## 📖 نحوه استفاده

### مرحله 1: تعریف کلاس سفارشی در Front Matter

در فایل markdown صفحه مورد نظر، یک کلاس custom_class تعریف کنید:

```markdown
+++
title = "عنوان صفحه"
tags = ["tag1", "tag2"]
draft = false
custom_class = "my-custom-page"
+++

محتوای صفحه...
```

### مرحله 2: نوشتن استایل‌های سفارشی

در فایل `assets/css/custom-pages.css`، استایل‌های خود را اضافه کنید:

```css
.my-custom-page {
    /* استایل‌های wrapper */
}

.my-custom-page-content {
    /* استایل‌های محتوا */
}

.my-custom-page-content img {
    /* استایل‌های تصاویر */
}
```

---

## 🔍 مثال کامل: صفحه SEO Keywords

### 1. Front Matter:

```markdown
+++
title = "Find Keywords, Website Structure & Necessary HTML Tags for SEO"
custom_class = "seo-keywords-page"
+++
```

### 2. استایل‌های اختصاصی:

```css
/* جلوگیری از horizontal scroll */
.seo-keywords-page {
    max-width: 100% !important;
    overflow-x: hidden !important;
}

.seo-keywords-page-content {
    max-width: 100% !important;
    overflow-x: hidden !important;
}

/* تصاویر responsive */
.seo-keywords-page-content img {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
}

/* جداول responsive */
.seo-keywords-page-content table {
    width: 100% !important;
    display: block !important;
    overflow-x: auto !important;
}
```

### 3. نتیجه:

این صفحه خاص با استایل‌های مخصوص به خود render می‌شود و سایر صفحات تأثیری نمی‌پذیرند.

---

## 🏗️ ساختار HTML تولید شده

وقتی `custom_class` تعریف کنید، Hugo این HTML را تولید می‌کند:

```html
<article class="article-wrapper seo-keywords-page">
    <h1 class="article-title">عنوان</h1>
    <div class="article-content seo-keywords-page-content">
        <!-- محتوا -->
    </div>
</article>
```

### Selector های قابل استفاده:

```css
/* Wrapper اصلی */
.your-class-name { }

/* محتوای صفحه */
.your-class-name-content { }

/* تمام المان‌های داخل محتوا */
.your-class-name-content * { }

/* المان‌های خاص */
.your-class-name-content img { }
.your-class-name-content h1 { }
.your-class-name-content p { }
.your-class-name-content table { }
.your-class-name-content pre { }
.your-class-name-content code { }
```

---

## 📌 نکات مهم

### 1. استفاده از `!important`

برای اطمینان از اعمال استایل‌ها، از `!important` استفاده کنید:

```css
.my-page-content img {
    width: 100% !important;
}
```

### 2. جلوگیری از Horizontal Scroll

برای جلوگیری از scroll افقی:

```css
.my-page {
    max-width: 100% !important;
    overflow-x: hidden !important;
}

.my-page-content {
    max-width: 100% !important;
    overflow-x: hidden !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
}

.my-page-content * {
    max-width: 100% !important;
    box-sizing: border-box !important;
}
```

### 3. تصاویر Responsive

```css
.my-page-content img {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    object-fit: contain !important;
    display: block !important;
}
```

### 4. جداول با Scroll افقی

```css
.my-page-content table {
    width: 100% !important;
    max-width: 100% !important;
    display: block !important;
    overflow-x: auto !important;
}
```

### 5. Code Blocks

```css
.my-page-content pre {
    max-width: 100% !important;
    overflow-x: auto !important;
    white-space: pre !important;
}

.my-page-content code {
    word-wrap: break-word !important;
}
```

---

## 🎨 مثال‌های بیشتر

### مثال 1: صفحه با پس‌زمینه خاص

```markdown
+++
title = "صفحه من"
custom_class = "special-background"
+++
```

```css
.special-background {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 3rem;
}

.special-background-content {
    background: rgba(255, 255, 255, 0.1);
    padding: 2rem;
    border-radius: 20px;
}
```

---

### مثال 2: صفحه با فونت بزرگ‌تر

```markdown
+++
title = "صفحه من"
custom_class = "large-font"
+++
```

```css
.large-font-content {
    font-size: 1.3rem !important;
    line-height: 2.2 !important;
}

.large-font-content h1 {
    font-size: 3rem !important;
}

.large-font-content h2 {
    font-size: 2.5rem !important;
}
```

---

### مثال 3: صفحه با عرض کمتر

```markdown
+++
title = "صفحه من"
custom_class = "narrow-width"
+++
```

```css
.narrow-width {
    max-width: 800px !important;
    margin: 0 auto !important;
}

.narrow-width-content {
    padding: 0 2rem !important;
}
```

---

## 🔄 الگوی کلی

### قالب Front Matter:

```markdown
+++
title = "عنوان صفحه"
tags = ["tag1", "tag2"]
Category = "category"
draft = false
custom_class = "your-unique-class-name"
+++
```

### قالب CSS:

```css
/* Container */
.your-unique-class-name {
    /* استایل‌های wrapper */
}

/* Content */
.your-unique-class-name-content {
    /* استایل‌های محتوا */
}

/* All child elements */
.your-unique-class-name-content * {
    /* استایل‌های همه المان‌ها */
}

/* Specific elements */
.your-unique-class-name-content img { }
.your-unique-class-name-content h1 { }
.your-unique-class-name-content h2 { }
.your-unique-class-name-content h3 { }
.your-unique-class-name-content p { }
.your-unique-class-name-content ul { }
.your-unique-class-name-content ol { }
.your-unique-class-name-content table { }
.your-unique-class-name-content pre { }
.your-unique-class-name-content code { }
.your-unique-class-name-content blockquote { }
```

---

## 📂 فایل‌های مربوطه

### 1. Template:
```
layouts/_default/single.html
```

### 2. استایل‌ها:
```
assets/css/custom-pages.css
```

### 3. محتوا:
```
content/seo/0-SEO-Theories/E6 to E9 - Find Keywords...md
```

---

## ✅ چک‌لیست استفاده

- [ ] کلاس custom_class در front matter تعریف شده
- [ ] کلاس منحصر به فرد است (تکراری نیست)
- [ ] استایل‌ها در `custom-pages.css` اضافه شده
- [ ] از `!important` برای اطمینان استفاده شده
- [ ] برای جلوگیری از scroll افقی تست شده
- [ ] در mobile و desktop تست شده
- [ ] Hugo rebuild شده: `hugo --gc`

---

## 🐛 عیب‌یابی

### مشکل: استایل‌ها اعمال نمی‌شوند

**راه‌حل:**
1. Clear browser cache (Ctrl+Shift+Del)
2. Hugo rebuild: `hugo --gc --minify`
3. بررسی console browser برای خطاها
4. بررسی selector ها با Developer Tools

---

### مشکل: هنوز horizontal scroll دارد

**راه‌حل:**
1. اضافه کردن `overflow-x: hidden` به wrapper
2. اضافه کردن `max-width: 100%` به تمام المان‌ها
3. بررسی عرض تصاویر با Developer Tools
4. Check inline styles on elements

---

### مشکل: استایل‌ها روی صفحات دیگر هم اعمال می‌شوند

**راه‌حل:**
- مطمئن شوید selector شما شامل `custom_class` است:
```css
/* درست */
.your-class-name-content img { }

/* اشتباه */
img { }  /* روی همه صفحات اعمال می‌شود */
```

---

## 📚 منابع

- [Hugo Custom Variables](https://gohugo.io/variables/)
- [CSS Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)
- [Responsive Images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)

---

**نویسنده**: Davood Yahya  
**تاریخ**: 2026-02-08  
**نسخه**: 1.0

---

**پایان راهنما** 🎉
