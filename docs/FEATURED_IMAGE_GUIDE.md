# راهنمای تصویر شاخص مقالات در صفحه دسته‌بندی

## 📋 شرح ویژگی

در صفحات دسته‌بندی مقالات (List Pages)، برای هر مقاله یک تصویر شاخص نمایش داده می‌شود که:
- بین عنوان مقاله و توضیح کوتاه قرار دارد
- در وسط کارت نمایش داده می‌شود
- با اندازه ثابت و یکنواخت برای تمام مقالات نمایش داده می‌شود
- Responsive است و در دستگاه‌های مختلف به درستی کار می‌کند

## 🎯 نحوه تعریف تصویر شاخص در Frontmatter

در هر فایل مقاله (`.md`), دو فیلد برای تعریف تصویر شاخص وجود دارد:

### روش اول: `featured_image`
```toml
+++
title = "عنوان مقاله"
featured_image = "/images/tools/MSFConsoleCommands-1.png"
+++
```

### روش دوم: `images` (آرایه)
```toml
+++
title = "عنوان مقاله"
images = ["/images/tools/MSFConsoleCommands-1.png"]
+++
```

### اولویت
- اگر هر دو فیلد وجود داشته باشند، `featured_image` اولویت دارد
- اگر `images` یک آرایه باشد، اولین آیتم به عنوان تصویر شاخص استفاده می‌شود

## 📁 مسیر تصاویر

تصاویر در پوشه `static` قرار دارند:

```
static/
└── images/
    ├── cyber-security/
    ├── linux/
    ├── python/
    ├── seo/
    └── tools/
```

**نکته مهم**: در frontmatter نیازی به نوشتن `static` نیست:
- ❌ اشتباه: `/static/images/tools/image.png`
- ✅ درست: `/images/tools/image.png`

## 🎨 مشخصات تصویر شاخص

### Desktop (بالای 1200px)
- **عرض**: 100% (تمام عرض کارت)
- **ارتفاع**: 200px (ثابت)
- **ارتفاع کارت**: 520px

### Tablet (769px - 1200px)
- **عرض**: 100%
- **ارتفاع**: 180px
- **ارتفاع کارت**: 500px

### Mobile (481px - 768px)
- **عرض**: 100%
- **ارتفاع**: 180px
- **ارتفاع کارت**: 480px

### Mobile Small (زیر 480px)
- **عرض**: 100%
- **ارتفاع**: 160px
- **ارتفاع کارت**: 460px

## 🖼️ ویژگی‌های تصویر

### Object-fit: Cover
تصاویر با استفاده از `object-fit: cover` نمایش داده می‌شوند:
- تصاویر بزرگتر از اندازه مشخص شده، Crop می‌شوند
- تصاویر کوچکتر، بزرگ می‌شوند و Crop می‌شوند
- نسبت ابعاد تصویر حفظ می‌شود
- تصویر همیشه کل فضا را پر می‌کند

### Lazy Loading
تصاویر با `loading="lazy"` لود می‌شوند:
- بهبود Performance
- کاهش استفاده از Bandwidth
- تجربه کاربری بهتر

### Animation
- تصاویر با انیمیشن Fade In نمایش داده می‌شوند
- در Hover، تصویر با Scale 1.05 بزرگ می‌شود
- Border تصویر در Hover تغییر رنگ می‌دهد

## 💻 کد HTML تولید شده

```html
<article class="article-card">
    <h2 class="article-card-title">
        <a href="/path/to/article/">عنوان مقاله</a>
    </h2>
    
    <div class="article-card-image">
        <a href="/path/to/article/">
            <img src="/images/tools/MSFConsoleCommands-1.png" 
                 alt="عنوان مقاله" 
                 loading="lazy">
        </a>
    </div>
    
    <div class="article-card-summary">
        توضیح کوتاه مقاله...
    </div>
    
    <a href="/path/to/article/" class="read-more-btn">
        ادامه مطلب ←
    </a>
</article>
```

## 🎨 CSS اصلی

### Container تصویر
```css
.article-card-image {
    width: 100%;
    height: 200px;
    margin: 1rem 0;
    border-radius: 12px;
    overflow: hidden;
    flex-shrink: 0;
    position: relative;
    background: linear-gradient(135deg, 
        rgba(0, 255, 65, 0.05) 0%, 
        rgba(58, 173, 223, 0.05) 100%);
    border: 2px solid rgba(0, 255, 65, 0.1);
    transition: all 0.3s ease;
}
```

### تصویر
```css
.article-card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    transition: all 0.4s ease;
    display: block;
}
```

### Hover Effect
```css
.article-card:hover .article-card-image img {
    transform: scale(1.05);
    filter: brightness(1.1);
}

.article-card-image:hover {
    border-color: var(--accent-green);
    box-shadow: 0 4px 20px rgba(0, 255, 65, 0.2);
}
```

## 🔄 Fallback (بدون تصویر)

اگر مقاله‌ای تصویر شاخص نداشته باشد:
- تصویر نمایش داده نمی‌شود
- ارتفاع کارت به حالت قبلی (350px در Desktop) برمی‌گردد
- Layout به هم نمی‌ریزد

```css
.article-card:not(:has(.article-card-image)) {
    min-height: 350px;
    max-height: 350px;
    height: 350px;
}
```

## 📱 ساختار Layout

### با تصویر شاخص:
```
┌────────────────────────────┐
│      عنوان مقاله          │
├────────────────────────────┤
│                            │
│      [تصویر شاخص]         │ ← 200px (Desktop)
│                            │
├────────────────────────────┤
│  توضیح کوتاه مقاله...     │
│                            │
├────────────────────────────┤
│    [ادامه مطلب →]         │
└────────────────────────────┘
```

### بدون تصویر شاخص:
```
┌────────────────────────────┐
│      عنوان مقاله          │
├────────────────────────────┤
│  توضیح کوتاه مقاله...     │
│  (فضای بیشتر)              │
│                            │
├────────────────────────────┤
│    [ادامه مطلب →]         │
└────────────────────────────┘
```

## 🧪 تست

### 1. مقاله با تصویر

ایجاد یک مقاله تست:
```toml
+++
title = "تست تصویر شاخص"
date = 2026-02-09
featured_image = "/images/test-image.png"
description = "این یک مقاله تست است"
+++

محتوای مقاله...
```

### 2. مقاله بدون تصویر

```toml
+++
title = "تست بدون تصویر"
date = 2026-02-09
description = "این یک مقاله بدون تصویر است"
+++

محتوای مقاله...
```

### 3. مقاله با آرایه تصاویر

```toml
+++
title = "تست آرایه تصاویر"
date = 2026-02-09
images = [
    "/images/image1.png",
    "/images/image2.png"
]
description = "اولین تصویر به عنوان تصویر شاخص استفاده می‌شود"
+++

محتوای مقاله...
```

## 📊 مثال‌های واقعی

### مقاله MSFConsole Commands

```toml
+++
title = "MSFConsole Commands"
date = 2025-01-15T00:00:00Z
featured_image = "/images/tools/MSFConsoleCommands-1.png"
images = ["/images/tools/MSFConsoleCommands-1.png"]
description = "راهنمای کامل دستورات MSFConsole"
categories = ["Tools", "Burpsuite"]
tags = ["pentest_tools", "metasploit"]
+++
```

### مقاله 60 Commands Hacker

```toml
+++
title = "60 Commands Hacker Should Know it"
date = 2025-01-04T00:00:00Z
featured_image = "/images/linux/60CommandsHacker-1.png"
images = ["/images/linux/60CommandsHacker-1.png"]
description = "60 دستور لینوکس که هر هکر باید بداند"
categories = ["Linux"]
tags = ["linux", "command_line"]
+++
```

## 🎯 بهترین روش‌ها (Best Practices)

### 1. اندازه تصویر
- **توصیه شده**: 800x400px (نسبت 2:1)
- **حداقل**: 600x300px
- **فرمت**: JPG, PNG, WebP
- **حجم**: کمتر از 200KB

### 2. نامگذاری فایل
- از نام‌های معنادار استفاده کنید
- از کاراکترهای خاص خودداری کنید
- از فضای خالی استفاده نکنید

✅ **درست**:
- `MSFConsoleCommands-1.png`
- `linux-commands-guide.jpg`
- `python-tutorial-01.webp`

❌ **اشتباه**:
- `image (1).png`
- `عکس مقاله.jpg`
- `my photo 2024.png`

### 3. Alt Text
Hugo به طور خودکار عنوان مقاله را به عنوان `alt` استفاده می‌کند:
```html
<img src="/images/..." alt="{{ .Title }}">
```

### 4. سازمان‌دهی پوشه‌ها
تصاویر را بر اساس دسته‌بندی سازمان‌دهی کنید:
```
static/images/
├── cyber-security/
│   ├── cryptography/
│   └── sans-401/
├── linux/
├── python/
├── seo/
└── tools/
    └── burpsuite/
```

## 🔧 عیب‌یابی (Troubleshooting)

### تصویر نمایش داده نمی‌شود

**بررسی کنید:**
1. مسیر تصویر درست است؟
2. فایل در پوشه `static` وجود دارد؟
3. نام فایل و پسوند درست است؟
4. Cache مرورگر پاک شده؟

### تصویر کشیده شده است

**راه‌حل:**
- از `object-fit: cover` استفاده می‌شود
- نسبت ابعاد تصویر اصلی مهم نیست
- تصویر به صورت خودکار Crop می‌شود

### تصویر در موبایل بزرگ است

**راه‌حل:**
- CSS Responsive برای موبایل تنظیم شده
- ارتفاع تصویر در موبایل کمتر است (160-180px)
- بررسی کنید که CSS به درستی لود شده

## 📄 فایل‌های تغییر یافته

### 1. `layouts/_default/list.html`
- اضافه شدن منطق تشخیص تصویر شاخص
- اضافه شدن HTML برای نمایش تصویر

### 2. `assets/css/main.css`
- اضافه شدن CSS برای `.article-card-image`
- تنظیم ارتفاع کارت‌ها
- Responsive Styles
- Animation و Hover Effects

## 🔄 تاریخچه

- **تاریخ**: 09 فوریه 2026
- **نسخه**: 1.0.0
- **وضعیت**: ✅ تکمیل شده

## 📚 منابع مرتبط

- [راهنمای تصاویر Hugo](https://gohugo.io/content-management/image-processing/)
- [CSS Object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
- [Lazy Loading Images](https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading)

---

**نکته**: این ویژگی فقط در صفحات دسته‌بندی (List Pages) فعال است و در صفحه اصلی (Home Page) تاثیری ندارد.
