# راهنمای کامل Badge های اطلاعات مقاله (Article Meta Badges)

## 📋 شرح ویژگی

برای نمایش اطلاعات تکمیلی و ویژگی‌های مقالات، سیستم Badge پیاده‌سازی شده که در دو جای مختلف نمایش داده می‌شود:

1. **صفحه دسته‌بندی (List Page)**: در کارت‌های مقاله
2. **صفحه مقاله (Single Page)**: در بالای محتوا، بعد از عنوان

---

## 🎯 ویژگی‌های قابل نمایش

### 1. مدت زمان خواندن (readingTime)
- **فیلد**: `readingTime = 14`
- **واحد**: دقیقه
- **نمایش**: "14 دقیقه"
- **آیکون**: ساعت ⏱️
- **رنگ**: آبی (accent-blue)

### 2. سطح سختی (difficulty)
- **فیلد**: `difficulty = "intermediate"`
- **مقادیر ممکن**:
  - `"beginner"` → **سطح مبتدی** (سبز)
  - `"medium"` → **سطح متوسط** (زرد)
  - `"intermediate"` → **سطح حرفه‌ای** (نارنجی)
  - `"advanced"` → **سطح تخصصی** (بنفش)
- **آیکون**: لایه‌ها 📊
- **رنگ**: بسته به سطح متفاوت است

### 3. نیاز به تمرین عملی (lab_required)
- **فیلد**: `lab_required = true`
- **مقادیر**:
  - `true` → نمایش Badge "نیاز به تمرین عملی"
  - `false` → Badge نمایش داده نمی‌شود
- **آیکون**: برق ⚡
- **رنگ**: قرمز (#ff416d)

### 4. نوع پست (post_type_fa)
- **فیلد**: `post_type_fa = "آموزشی"`
- **مقادیر**: هر متن فارسی (مقاله، آموزشی، اسکریپت، خبر، ...)
- **آیکون**: سند 📄
- **رنگ**: سبز روشن (#98c379)

### 5. تگ‌ها (tags)
- **فیلد**: `tags = ["cyber-security", "Cryptography", "Encryption"]`
- **نمایش**: لیست تگ‌ها
- **استایل**: بدون آیکون، فقط فونت زیبا
- **رنگ**: آبی روشن (accent-blue)

---

## 📄 تعریف در Frontmatter

### مثال کامل:

```toml
+++
title = "Malwares"
date = "2024-06-20T13:07:52+03:30"
categories = ["cyber-security", "Cryptography"]
tags = ["cyber-security", "Cryptography", "Encryption"]

# ویژگی‌های مقاله
readingTime = 14
difficulty = "intermediate"
lab_required = true
post_type_fa = "آموزشی"

# سایر تنظیمات
toc = true
math = false
type = "posts"
+++
```

### مثال ساده:

```toml
+++
title = "عنوان مقاله"
tags = ["tools", "python", "linux", "cmd"]

readingTime = 28
difficulty = "beginner"
lab_required = false
post_type_fa = "مقاله"
+++
```

---

## 🎨 نمایش در صفحات

### 1. صفحه دسته‌بندی (List Page)

#### موقعیت قرارگیری:

```
┌────────────────────────────────┐
│      عنوان مقاله              │
├────────────────────────────────┤
│      [تصویر شاخص]             │
├────────────────────────────────┤
│  توضیح کوتاه مقاله...         │
├────────────────────────────────┤
│  Tags: tag1, tag2, tag3        │ ← تگ‌ها در بالای Footer
├────────────────────────────────┤
│  [ادامه مطلب]    [Badges]     │ ← Badge ها سمت چپ دکمه
└────────────────────────────────┘
```

#### Badge های نمایش داده شده:
- ✅ مدت زمان (اگر وجود داشته باشد)
- ✅ سطح سختی (اگر وجود داشته باشد)
- ✅ نیاز به تمرین عملی (فقط اگر `true` باشد)
- ✅ نوع پست (اگر وجود داشته باشد)

#### تگ‌ها:
- نمایش حداکثر 4 تگ اول
- در بالای دکمه "ادامه مطلب"
- استایل ساده و خوانا

---

### 2. صفحه مقاله (Single Page)

#### موقعیت قرارگیری:

```
┌────────────────────────────────┐
│      عنوان مقاله              │
├────────────────────────────────┤
│  [Badge Container]             │ ← Badge ها بعد از عنوان
│  🕐 مدت زمان: 14 دقیقه        │
│  📊 سطح حرفه‌ای                │
│  ⚡ نیاز به تمرین عملی        │
│  📄 آموزشی                     │
├────────────────────────────────┤
│  🏷️ تگ‌ها:                     │ ← تگ‌ها بعد از Badge ها
│  tag1 tag2 tag3 tag4 ...       │
├────────────────────────────────┤
│  📑 فهرست مطالب               │ ← TOC بعد از تگ‌ها
├────────────────────────────────┤
│  محتوای مقاله...              │
└────────────────────────────────┘
```

#### Badge های نمایش داده شده:
- ✅ همه Badge ها با جزئیات بیشتر
- ✅ آیکون‌های واضح‌تر
- ✅ فضای بیشتر
- ✅ تگ‌ها در بخش جداگانه

---

## 🎨 طراحی و استایل

### رنگ‌بندی Badge ها:

| ویژگی | رنگ | کد رنگ | آیکون |
|-------|-----|---------|-------|
| مدت زمان | آبی | `#3aaddf` (accent-blue) | 🕐 |
| سطح مبتدی | سبز | `#00ff41` (accent-green) | 📊 |
| سطح متوسط | زرد | `#e5c07b` (accent-yellow) | 📊 |
| سطح حرفه‌ای | نارنجی | `#e06c11` (accent-orange) | 📊 |
| سطح تخصصی | بنفش | `#c678dd` (accent-purple) | 📊 |
| تمرین عملی | قرمز | `#ff416d` | ⚡ |
| نوع پست | سبز روشن | `#98c379` | 📄 |
| تگ‌ها | آبی روشن | `#3aaddf` | 🏷️ |

### ویژگی‌های طراحی:

#### Badge ها:
- **Shape**: Rounded (border-radius: 15-20px)
- **Border**: 1.5-2px solid با opacity
- **Background**: Gradient تیره با blur effect
- **Hover**: Transform translateY(-2px) + Box Shadow
- **Font**: Vazir/Shabnam برای فارسی، Rajdhani برای انگلیسی
- **Size**: متوسط (padding: 0.4-0.6rem)

#### تگ‌ها:
- **Style**: ساده‌تر از Badge ها
- **Border**: نازک‌تر (1px)
- **Background**: شفاف‌تر
- **Font**: English Font
- **Hover**: Scale کم + Border رنگی

---

## 📱 Responsive Design

### Desktop (1200px+)
```css
.article-card {
    height: 620px;
}

.article-badge {
    font-size: 0.75rem;
    padding: 0.4rem 0.7rem;
}

.meta-badge {
    font-size: 0.9rem;
    padding: 0.6rem 1rem;
}
```

### Tablet (769-1200px)
```css
.article-card {
    height: 600px;
}

.article-badge {
    font-size: 0.72rem;
    padding: 0.38rem 0.65rem;
}
```

### Mobile (481-768px)
```css
.article-card {
    height: 580px;
}

.article-card-footer {
    flex-direction: column;
}

.article-badge {
    font-size: 0.7rem;
}

.meta-badge {
    font-size: 0.85rem;
}
```

### Mobile Small (< 480px)
```css
.article-card {
    height: 560px;
}

.article-badge {
    font-size: 0.65rem;
}

.meta-badge {
    width: 100%;
    justify-content: center;
}

.tags-section {
    flex-direction: column;
}
```

---

## 💻 کد HTML تولید شده

### صفحه دسته‌بندی (List):

```html
<article class="article-card">
    <h2 class="article-card-title">
        <a href="/path/">عنوان مقاله</a>
    </h2>
    
    <div class="article-card-image">...</div>
    
    <div class="article-card-summary">...</div>
    
    <!-- تگ‌ها -->
    <div class="article-card-tags">
        <span class="article-tag">cyber-security</span>
        <span class="article-tag">Cryptography</span>
        <span class="article-tag">Encryption</span>
    </div>
    
    <!-- Footer با Badge ها -->
    <div class="article-card-footer">
        <a href="/path/" class="read-more-btn">ادامه مطلب ←</a>
        
        <div class="article-card-badges">
            <span class="article-badge badge-time">
                <svg>...</svg>
                14 دقیقه
            </span>
            <span class="article-badge badge-intermediate">
                <svg>...</svg>
                سطح حرفه‌ای
            </span>
            <span class="article-badge badge-lab">
                <svg>...</svg>
                نیاز به تمرین عملی
            </span>
            <span class="article-badge badge-type">
                <svg>...</svg>
                آموزشی
            </span>
        </div>
    </div>
</article>
```

### صفحه مقاله (Single):

```html
<article class="article-wrapper">
    <h1 class="article-title">Malwares</h1>
    
    <!-- Badge ها -->
    <div class="article-meta-badges">
        <div class="meta-badge badge-time">
            <svg>...</svg>
            <span class="badge-label">مدت زمان:</span>
            <span class="badge-value">14 دقیقه</span>
        </div>
        <div class="meta-badge badge-intermediate">
            <svg>...</svg>
            <span class="badge-value">سطح حرفه‌ای</span>
        </div>
        <div class="meta-badge badge-lab">
            <svg>...</svg>
            <span class="badge-value">نیاز به تمرین عملی</span>
        </div>
        <div class="meta-badge badge-type">
            <svg>...</svg>
            <span class="badge-value">آموزشی</span>
        </div>
    </div>
    
    <!-- تگ‌ها -->
    <div class="article-tags-section">
        <div class="tags-label">
            <svg>...</svg>
            <span>تگ‌ها:</span>
        </div>
        <div class="tags-list">
            <span class="article-tag-item">cyber-security</span>
            <span class="article-tag-item">Cryptography</span>
            <span class="article-tag-item">Encryption</span>
        </div>
    </div>
    
    <!-- TOC -->
    <div class="toc-container">...</div>
    
    <!-- محتوا -->
    <div class="article-content">...</div>
</article>
```

---

## 🧪 مثال‌های کاربردی

### مثال 1: مقاله آموزشی پیشرفته

```toml
+++
title = "Advanced Penetration Testing"
readingTime = 45
difficulty = "advanced"
lab_required = true
post_type_fa = "آموزشی"
tags = ["pentest", "security", "advanced"]
+++
```

**نمایش Badge ها:**
- 🕐 مدت زمان: 45 دقیقه (آبی)
- 📊 سطح تخصصی (بنفش)
- ⚡ نیاز به تمرین عملی (قرمز)
- 📄 آموزشی (سبز روشن)
- 🏷️ تگ‌ها: pentest, security, advanced

---

### مثال 2: مقاله مبتدی

```toml
+++
title = "Introduction to Linux"
readingTime = 10
difficulty = "beginner"
lab_required = false
post_type_fa = "مقاله"
tags = ["linux", "basics", "tutorial"]
+++
```

**نمایش Badge ها:**
- 🕐 مدت زمان: 10 دقیقه (آبی)
- 📊 سطح مبتدی (سبز)
- 📄 مقاله (سبز روشن)
- 🏷️ تگ‌ها: linux, basics, tutorial

**توجه**: Badge "نیاز به تمرین عملی" نمایش داده نمی‌شود چون `false` است.

---

### مثال 3: اسکریپت متوسط

```toml
+++
title = "Python Web Scraper"
readingTime = 20
difficulty = "medium"
lab_required = true
post_type_fa = "اسکریپت"
tags = ["python", "scripting", "automation"]
+++
```

**نمایش Badge ها:**
- 🕐 مدت زمان: 20 دقیقه (آبی)
- 📊 سطح متوسط (زرد)
- ⚡ نیاز به تمرین عملی (قرمز)
- 📄 اسکریپت (سبز روشن)
- 🏷️ تگ‌ها: python, scripting, automation

---

## 📊 مزایا

### 1. تجربه کاربری بهتر
- کاربر سریع‌تر اطلاعات مقاله را می‌بیند
- تصمیم‌گیری آسان‌تر برای خواندن مقاله
- درک سریع از سطح و نوع محتوا

### 2. SEO و دسته‌بندی
- سازمان‌دهی بهتر محتوا
- نمایش اطلاعات structured
- بهبود Engagement

### 3. طراحی زیبا
- Badge های رنگی و جذاب
- هماهنگ با تم سایت
- Responsive و Mobile-friendly

### 4. انعطاف‌پذیری
- اضافه کردن Badge های جدید آسان است
- هر مقاله می‌تواند ویژگی‌های مختلفی داشته باشد
- برخی Badge ها اختیاری هستند

---

## 🔧 تنظیمات پیشرفته

### اضافه کردن Badge جدید:

#### 1. اضافه کردن به Frontmatter:
```toml
custom_badge = "ویژه"
```

#### 2. اضافه کردن به HTML (`list.html` یا `single.html`):
```html
{{ if .Params.custom_badge }}
    <span class="article-badge badge-custom">
        <svg>...</svg>
        {{ .Params.custom_badge }}
    </span>
{{ end }}
```

#### 3. اضافه کردن CSS:
```css
.badge-custom {
    border-color: rgba(100, 200, 255, 0.3);
    color: #64c8ff;
}

.badge-custom svg {
    fill: #64c8ff;
}
```

---

## 📁 فایل‌های تغییر یافته

1. **`layouts/_default/list.html`**
   - اضافه شدن تگ‌ها
   - اضافه شدن Badge ها در Footer
   - ساختار جدید Footer

2. **`layouts/_default/single.html`**
   - اضافه شدن `.article-meta-badges`
   - اضافه شدن `.article-tags-section`
   - قرارگیری قبل از TOC

3. **`assets/css/main.css`**
   - CSS برای `.article-meta-badges`
   - CSS برای `.article-tags-section`
   - CSS برای `.article-card-badges`
   - CSS برای `.article-card-tags`
   - Responsive styles

4. **`content/**/*.md`**
   - اضافه شدن property ها به Frontmatter

---

## 🚀 نحوه استفاده

### برای مقالات موجود:

1. فایل مقاله را باز کنید
2. به بخش Frontmatter بروید
3. ویژگی‌های زیر را اضافه کنید:

```toml
readingTime = 15
difficulty = "medium"
lab_required = true
post_type_fa = "آموزشی"
```

4. فایل را ذخیره کنید
5. Hugo را rebuild کنید:
```bash
hugo --cleanDestinationDir
```

---

## ✅ Checklist

- [x] Badge ها در صفحه List نمایش داده می‌شوند
- [x] Badge ها در صفحه Single نمایش داده می‌شوند
- [x] تگ‌ها نمایش داده می‌شوند
- [x] رنگ‌بندی درست است
- [x] Responsive در همه اندازه‌ها کار می‌کند
- [x] Hover effects فعال است
- [x] SVG آیکون‌ها نمایش داده می‌شوند
- [x] فونت‌ها هماهنگ هستند

---

**تاریخ**: 09 فوریه 2026  
**نسخه**: 1.0.0  
**وضعیت**: ✅ تکمیل شده

