# راهنمای کامل Badge های اطلاعات مقاله (Article Meta Badges)

## 📋 شرح ویژگی

برای نمایش اطلاعات تکمیلی و ویژگی‌های مقالات، سیستم Badge پیاده‌سازی شده که در دو جای مختلف نمایش داده می‌شود:

1. **صفحه دسته‌بندی (List Page)**: در کارت‌های مقاله، در footer در کنار دکمه "ادامه مطلب"
2. **صفحه مقاله (Single Page)**: بعد از TOC و قبل از شروع محتوای مقاله

---

## 🎯 ویژگی‌های قابل نمایش

### 1. مدت زمان خواندن (readingTime)
- **فیلد Hugo**: `readingTime = 14` 
- **⚠️ توجه**: حتماً نام فیلد را دقیقاً `readingTime` بنویسید (Case Sensitive)
- **واحد**: دقیقه
- **نمایش در Single Page**: "مدت زمان: 14 دقیقه"
- **نمایش در Card**: "14 دقیقه"
- **آیکون**: ساعت ⏱️
- **رنگ**: آبی (accent-blue)

### 2. سطح سختی (difficulty)
- **فیلد Hugo**: `difficulty = "intermediate"`
- **⚠️ توجه**: حتماً نام فیلد را دقیقاً `difficulty` بنویسید (Case Sensitive)
- **مقادیر ممکن**:
  - `"beginner"` → **سطح مبتدی** (در Card: "مبتدی") - سبز
  - `"medium"` → **سطح متوسط** (در Card: "متوسط") - زرد
  - `"intermediate"` → **سطح حرفه‌ای** (در Card: "حرفه‌ای") - نارنجی
  - `"advanced"` → **سطح تخصصی** (در Card: "تخصصی") - بنفش
- **آیکون**: لایه‌ها 📊
- **رنگ**: بسته به سطح متفاوت است

### 3. نیاز به تمرین عملی (lab_required)
- **فیلد Hugo**: `lab_required = true`
- **⚠️ توجه**: حتماً نام فیلد را دقیقاً `lab_required` بنویسید (Case Sensitive)
- **مقادیر**:
  - `true` → نمایش Badge
  - `false` → Badge نمایش داده نمی‌شود (پنهان است)
- **نمایش در Single Page**: "نیاز به تمرین عملی"
- **نمایش در Card**: "تمرین عملی"
- **آیکون**: برق ⚡
- **رنگ**: قرمز (#ff416d)

### 4. نوع پست (post_type_fa)
- **فیلد Hugo**: `post_type_fa = "آموزشی"`
- **⚠️ توجه**: حتماً نام فیلد را دقیقاً `post_type_fa` بنویسید (Case Sensitive)
- **مقادیر**: هر متن فارسی (مقاله، آموزشی، اسکریپت، خبر، ویدیو، ...)
- **نمایش**: همان متن وارد شده
- **آیکون**: سند 📄
- **رنگ**: سبز روشن (#98c379)

---

## 📝 نحوه استفاده

### مثال 1: مقاله Malwares.md

```toml
+++
title = "Malwares"
date = "2024-06-20"

# ویژگی‌های مقاله
readingTime = 14
difficulty = "intermediate"
lab_required = true 
post_type_fa = "آموزشی"

categories = ["cyber-security", "Cryptography"]
tags = ["cyber-security", "Cryptography", "Encryption"]
+++
```

**نمایش در Single Page:**
- مدت زمان: 14 دقیقه
- سطح حرفه‌ای
- نیاز به تمرین عملی
- آموزشی

**نمایش در Card (List Page):**
- 14 دقیقه
- حرفه‌ای
- تمرین عملی
- آموزشی

---

### مثال 2: مقاله ساده

```toml
+++
title = "مبانی شبکه"
date = "2024-06-15"

# ویژگی‌های مقاله
readingTime = 28
difficulty = "beginner"
lab_required = false
post_type_fa = "مقاله"

categories = ["network"]
tags = ["network", "basics"]
+++
```

**نمایش در Single Page:**
- مدت زمان: 28 دقیقه
- سطح مبتدی
- مقاله

**نمایش در Card:**
- 28 دقیقه
- مبتدی
- مقاله

**توجه**: `lab_required = false` است پس Badge "تمرین عملی" نمایش داده نمی‌شود.

---

### مثال 3: مقاله بدون ویژگی

```toml
+++
title = "مقاله بدون Badge"
date = "2024-06-10"

categories = ["linux"]
tags = ["linux"]
+++
```

**نتیجه**: هیچ Badge نمایش داده نمی‌شود (بخش `article-meta-badges` کلاً پنهان است).

---

## 🎨 طراحی و استایل

### Single Page Badges

```
┌─────────────────────────────────────────────────────────┐
│  [⏱️ مدت زمان: 14 دقیقه]  [📊 سطح حرفه‌ای]           │
│  [⚡ نیاز به تمرین عملی]  [📄 آموزشی]                 │
└─────────────────────────────────────────────────────────┘
```

**ویژگی‌های طراحی:**
- پس‌زمینه gradient با opacity کم
- Border رنگی با رنگ سبز
- Shadow برای عمق بیشتر
- Hover effect با scale و shadow
- فونت واضح و خوانا
- فاصله‌گذاری مناسب

### Card Badges (List Page)

```
┌──────────────────────────────────────────────────┐
│  عنوان مقاله                                     │
│  [تصویر شاخص]                                    │
│  خلاصه محتوا...                                  │
│  ┌──────────────────────────────────────────────┐│
│  │ [ادامه مطلب ←]    [⏱️ 14] [📊 حرفه‌ای] [⚡]  ││
│  └──────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

**ویژگی‌های طراحی:**
- سایز کوچکتر نسبت به Single Page
- متن کوتاه‌تر برای صرفه‌جویی در فضا
- چیدمان در کنار دکمه "ادامه مطلب"
- Responsive و تطبیق با موبایل

---

## 📱 Responsive Design

### Desktop (> 768px)

**Single Page:**
- اندازه فونت: 0.95rem
- Padding: 0.7rem 1.2rem
- Gap: 0.9rem
- Layout: Horizontal wrap

**Card:**
- اندازه فونت: 0.8rem
- Padding: 0.45rem 0.85rem
- Gap: 0.6rem
- در کنار دکمه "ادامه مطلب"

### Tablet (≤ 768px)

**Single Page:**
- اندازه فونت: 0.88rem
- Padding: 0.6rem 1rem
- Gap: 0.7rem

**Card:**
- اندازه فونت: 0.75rem
- Padding: 0.4rem 0.75rem
- Gap: 0.5rem

### Mobile (≤ 480px)

**Single Page:**
- اندازه فونت: 0.82rem
- Padding: 0.5rem 0.8rem
- Layout: **تغییر به عمودی** (flex-direction: column)
- Width: 100% برای هر badge
- متن وسط‌چین

**Card:**
- اندازه فونت: 0.7rem
- Padding: 0.35rem 0.65rem
- Footer تبدیل به column می‌شود
- Badge ها در ردیف جداگانه
- دکمه "ادامه مطلب" تمام عرض

---

## 🎨 رنگ‌بندی Badge ها

### مدت زمان (Time)
- **Border**: rgba(58, 173, 223, 0.35)
- **Color**: var(--accent-blue) 
- **Hover Shadow**: rgba(58, 173, 223, 0.45)

### سطح مبتدی (Beginner)
- **Border**: rgba(0, 255, 65, 0.35)
- **Color**: var(--accent-green)
- **Hover Shadow**: rgba(0, 255, 65, 0.5)

### سطح متوسط (Medium)
- **Border**: rgba(229, 192, 123, 0.35)
- **Color**: var(--accent-yellow)
- **Hover Shadow**: rgba(229, 192, 123, 0.5)

### سطح حرفه‌ای (Intermediate)
- **Border**: rgba(224, 108, 17, 0.35)
- **Color**: var(--accent-orange)
- **Hover Shadow**: rgba(224, 108, 17, 0.5)

### سطح تخصصی (Advanced)
- **Border**: rgba(198, 120, 221, 0.35)
- **Color**: var(--accent-purple)
- **Hover Shadow**: rgba(198, 120, 221, 0.5)

### تمرین عملی (Lab)
- **Border**: rgba(255, 65, 108, 0.35)
- **Color**: #ff416d
- **Hover Shadow**: rgba(255, 65, 108, 0.5)

### نوع پست (Type)
- **Border**: rgba(152, 195, 121, 0.35)
- **Color**: #98c379
- **Hover Shadow**: rgba(152, 195, 121, 0.5)

---

## 🔧 ساختار فایل‌ها

### HTML Templates

#### 1. `layouts/_default/single.html`
```html
<!-- بعد از TOC و قبل از محتوا -->
{{ if or .Params.readingTime .Params.difficulty .Params.lab_required .Params.post_type_fa }}
    <div class="article-meta-badges">
        <!-- Badge مدت زمان -->
        {{ if .Params.readingTime }}
            <div class="meta-badge badge-time">
                <svg>...</svg>
                <span class="badge-text">مدت زمان: {{ .Params.readingTime }} دقیقه</span>
            </div>
        {{ end }}
        
        <!-- Badge سطح سختی -->
        {{ if .Params.difficulty }}
            <!-- منطق تشخیص و نمایش -->
        {{ end }}
        
        <!-- Badge تمرین عملی -->
        {{ if .Params.lab_required }}
            <div class="meta-badge badge-lab">
                <svg>...</svg>
                <span class="badge-text">نیاز به تمرین عملی</span>
            </div>
        {{ end }}
        
        <!-- Badge نوع پست -->
        {{ if .Params.post_type_fa }}
            <div class="meta-badge badge-type">
                <svg>...</svg>
                <span class="badge-text">{{ .Params.post_type_fa }}</span>
            </div>
        {{ end }}
    </div>
{{ end }}
```

#### 2. `layouts/_default/list.html`
```html
<div class="article-card-footer">
    <a href="{{ .RelPermalink }}" class="read-more-btn">
        ادامه مطلب ←
    </a>
    
    {{ if or .Params.readingTime .Params.difficulty .Params.lab_required .Params.post_type_fa }}
        <div class="article-card-badges">
            <!-- Badge های کوتاه‌تر برای Card -->
        </div>
    {{ end }}
</div>
```

### CSS Files

#### 1. `assets/css/main.css`
- `.article-meta-badges` - Container برای Single Page
- `.meta-badge` - Badge اصلی Single Page
- `.article-card-badges` - Container برای Card
- `.article-badge` - Badge اصلی Card
- رنگ‌بندی هر Badge
- Media queries responsive

#### 2. `static/css/main.css`
- همان استایل‌های `assets/css/main.css`

---

## ⚠️ نکات مهم

### 1. Case Sensitivity
**خیلی مهم!** Hugo به حروف بزرگ و کوچک حساس است:

✅ **صحیح:**
```toml
readingTime = 14
difficulty = "intermediate"
lab_required = true
post_type_fa = "آموزشی"
```

❌ **اشتباه:**
```toml
readingtime = 14  # اشتباه
ReadingTime = 14  # اشتباه
reading_time = 14  # اشتباه
Difficulty = "intermediate"  # اشتباه
Lab_Required = true  # اشتباه
post_Type_fa = "آموزشی"  # اشتباه
```

### 2. مقادیر difficulty
فقط این 4 مقدار معتبر هستند:
- `"beginner"`
- `"medium"`
- `"intermediate"`
- `"advanced"`

هر مقدار دیگری نمایش داده نمی‌شود.

### 3. lab_required باید boolean باشد
```toml
✅ lab_required = true
✅ lab_required = false

❌ lab_required = "true"  # string است
❌ lab_required = 1  # number است
```

### 4. فونت فارسی
از فونت `var(--persian-text)` استفاده می‌شود که باید در CSS تعریف شده باشد.

### 5. آیکون‌ها
آیکون‌ها با SVG inline پیاده‌سازی شده‌اند و نیازی به فایل خارجی ندارند.

---

## 🧪 تست

### Checklist تست:

#### Single Page
- [x] Badge ها بعد از TOC نمایش داده می‌شوند
- [x] Badge ها قبل از محتوا هستند
- [x] readingTime درست نمایش داده می‌شود
- [x] difficulty با رنگ صحیح نمایش داده می‌شود
- [x] lab_required فقط در true نمایش داده می‌شود
- [x] post_type_fa متن فارسی را درست نشان می‌دهد
- [x] Hover effects کار می‌کنند
- [x] Responsive در موبایل به ستونی تبدیل می‌شود

#### List Page (Card)
- [x] Badge ها در footer کنار دکمه هستند
- [x] Badge ها سمت چپ (روبروی دکمه) قرار دارند
- [x] متن‌ها کوتاه‌تر هستند
- [x] رنگ‌بندی درست است
- [x] Hover effects کار می‌کنند
- [x] در موبایل به ردیف جداگانه می‌روند

#### Responsive
- [x] Desktop: Layout افقی
- [x] Tablet: اندازه متوسط
- [x] Mobile: Layout عمودی در Single / ردیف جدا در Card

---

## 🐛 عیب‌یابی

### Badge ها نمایش داده نمی‌شوند

**1. بررسی Frontmatter:**
```bash
# باز کردن فایل markdown
cat content/cyber-security/Cryptography/Malwares.md | head -30
```

بررسی کنید:
- ✅ نام فیلدها دقیقاً صحیح است؟
- ✅ مقادیر درست هستند؟
- ✅ فرمت TOML صحیح است؟

**2. بررسی Build:**
```bash
hugo --cleanDestinationDir
```

خطایی در Console نمی‌بینید؟

**3. بررسی CSS:**
```bash
# بررسی فایل CSS در public
cat public/css/main.css | grep "article-meta-badges"
```

آیا CSS compile شده است؟

**4. Cache مرورگر:**
- Ctrl+Shift+R برای hard refresh
- Clear cache

### رنگ‌ها درست نیستند

**بررسی CSS Variables:**
```css
:root {
    --accent-blue: #3aaddf;
    --accent-green: #00ff41;
    --accent-yellow: #e5c07b;
    --accent-orange: #e06c11;
    --accent-purple: #c678dd;
}
```

### Badge ها در موبایل overlap می‌شوند

**بررسی Media Queries:**
```bash
# جستجوی media query
cat assets/css/main.css | grep -A 20 "@media (max-width: 480px)"
```

---

## 📚 مستندات مرتبط

- **راهنمای Frontmatter**: `docs/FRONTMATTER_GUIDE.md`
- **راهنمای CSS**: `docs/CSS_GUIDE.md`
- **راهنمای Responsive**: `docs/RESPONSIVE_GUIDE.md`

---

## 🎯 خلاصه

### محل نمایش Badge ها:

1. **Single Page**: بعد از TOC، قبل از محتوا
2. **List Page**: در footer کارت، کنار دکمه "ادامه مطلب"

### Frontmatter Properties:

```toml
readingTime = 14              # عدد (دقیقه)
difficulty = "intermediate"   # string (beginner|medium|intermediate|advanced)
lab_required = true           # boolean (true|false)
post_type_fa = "آموزشی"       # string (هر متن فارسی)
```

### نکات کلیدی:

- ✅ Case Sensitive
- ✅ فقط Badge هایی نمایش داده می‌شوند که مقدار دارند
- ✅ lab_required فقط در true نمایش داده می‌شود
- ✅ Responsive برای Desktop, Tablet, Mobile
- ✅ رنگ‌بندی اختصاصی برای هر Badge
- ✅ Hover effects و انیمیشن

---

**تاریخ ایجاد**: 2026-02-09  
**نسخه**: 2.0  
**وضعیت**: ✅ کامل و آماده استفاده
