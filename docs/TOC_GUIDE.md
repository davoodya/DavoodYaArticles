# راهنمای Table of Contents (TOC) - فهرست مطالب

## 📋 خلاصه

این راهنما توضیح می‌دهد چگونه Table of Contents (فهرست مطالب) کامل برای تمام مقالات فعال شده است.

---

## ✨ ویژگی‌های TOC

### 1. **نمایش کامل تمام Headings**
- نمایش H1 تا H6
- ساختار سلسله مراتبی
- رنگ‌های متمایز برای هر سطح

### 2. **قابلیت کلیک و Navigation**
- کلیک روی هر آیتم → رفتن به همان بخش
- Smooth scroll انیمیشن
- Highlight کردن heading فعال

### 3. **Responsive Design**
- Desktop: فهرست باز
- Mobile: دکمه Toggle برای باز/بسته کردن

### 4. **Auto-Generated IDs**
- تولید خودکار ID برای headings
- پشتیبانی از حروف فارسی
- جلوگیری از ID تکراری

### 5. **استایل حرفه‌ای Cyberpunk**
- خط رنگی gradient در بالا
- الگوی پس‌زمینه
- انیمیشن hover
- Highlight کردن heading هنگام کلیک

---

## 🎯 تنظیمات انجام شده

### 1. فایل `hugo.toml`

```toml
[markup.tableOfContents]
    startLevel = 1      # شروع از H1
    endLevel = 6        # تا H6
    ordered = false     # لیست غیر شماره‌دار
```

**توضیح:**
- `startLevel = 1`: از H1 شروع می‌شود
- `endLevel = 6`: تا H6 نمایش می‌دهد
- `ordered = false`: از bullet points استفاده می‌کند

---

### 2. فایل `layouts/_default/single.html`

**قبل:**
```html
<article class="article-wrapper">
    <h1 class="article-title">{{ .Title }}</h1>
    <div class="article-content">
        {{ .Content }}
    </div>
</article>
```

**بعد:**
```html
<article class="article-wrapper">
    <h1 class="article-title">{{ .Title }}</h1>
    
    {{/* Table of Contents */}}
    {{ if .TableOfContents }}
        <div class="toc-container">
            <h2 class="toc-title">فهرست مطالب</h2>
            <button class="toc-toggle" onclick="toggleTOC()">نمایش/مخفی کردن فهرست</button>
            <nav id="TableOfContents">
                {{ .TableOfContents }}
            </nav>
        </div>
    {{ end }}
    
    <div class="article-content">
        {{ .Content }}
    </div>
</article>
```

---

### 3. فایل `assets/css/toc.css` (جدید)

شامل:
- استایل‌های container
- استایل‌های navigation
- رنگ‌های مختلف برای سطوح
- انیمیشن‌ها
- Responsive styles

---

### 4. فایل `static/assets/js/heading-ids.js` (جدید)

**کاربرد:**
- تولید خودکار ID برای headings
- پشتیبانی از حروف فارسی و انگلیسی
- جلوگیری از ID تکراری

**مثال:**
```
"مقدمه" → "مقدمه"
"Installation Guide" → "installation-guide"
"نصب و راه‌اندازی" → "نصب-و-راه-اندازی"
```

---

## 🎨 استایل‌های TOC

### رنگ‌های سطوح مختلف:

| سطح | Heading | رنگ | نمونه |
|-----|---------|-----|-------|
| 1 | H1 | سبز (`--accent-green`) | عنوان اصلی |
| 2 | H2 | آبی (`--accent-blue`) | زیر عنوان |
| 3 | H3 | نارنجی (`--accent-orange`) | بخش فرعی |
| 4 | H4 | بنفش (`--accent-purple`) | جزئیات |
| 5 | H5 | زرد (`--accent-yellow`) | توضیحات |
| 6 | H6 | سبز روشن (`#98c379`) | ریز جزئیات |

---

## 📱 Responsive Design

### Desktop (بالای 768px):
- TOC همیشه باز است
- فهرست کامل نمایش داده می‌شود
- دکمه Toggle مخفی است

### Mobile (زیر 768px):
- TOC به صورت پیش‌فرض بسته است
- دکمه Toggle نمایش داده می‌شود
- کاربر می‌تواند فهرست را باز/بسته کند

---

## 🚀 ویژگی‌های JavaScript

### 1. Toggle TOC (موبایل)
```javascript
function toggleTOC() {
    const toc = document.getElementById('TableOfContents');
    toc.classList.toggle('show');
}
```

### 2. Highlight Active Heading
```javascript
function highlightActiveHeading() {
    // پیدا کردن heading فعلی
    // اضافه کردن کلاس 'active' به لینک مربوطه
}
```

### 3. Smooth Scroll
```javascript
// کلیک روی لینک TOC → Smooth scroll به heading
// با offset مناسب برای header
```

---

## 📂 ساختار فایل‌ها

```
davoodya/
├── hugo.toml                                    [✓ تغییر یافت]
├── layouts/
│   └── _default/
│       ├── baseof.html                          [✓ تغییر یافت]
│       └── single.html                          [✓ تغییر یافت]
├── assets/
│   └── css/
│       └── toc.css                              [✓ جدید]
├── static/
│   ├── css/
│   │   └── toc.css                              [✓ کپی شد]
│   └── assets/
│       └── js/
│           └── heading-ids.js                   [✓ جدید]
└── docs/
    └── TOC_GUIDE.md                             [✓ این فایل]
```

---

## 🎯 نحوه استفاده

### برای نویسندگان مقاله:

1. **فقط از Headings استفاده کنید:**
```markdown
# عنوان اصلی (H1)

## زیر عنوان (H2)

### بخش فرعی (H3)

#### جزئیات (H4)
```

2. **TOC به صورت خودکار ساخته می‌شود**

3. **ID ها به صورت خودکار تولید می‌شوند**

---

## 🔍 تست TOC

### مراحل تست:

1. **به یک مقاله بروید:**
   - مثال: "60 Commands Hacker Should Know it"

2. **TOC را بررسی کنید:**
   - آیا تمام headings نمایش داده می‌شوند؟
   - آیا سطح‌بندی درست است؟
   - آیا رنگ‌ها متمایز هستند؟

3. **کلیک روی آیتم‌ها:**
   - آیا smooth scroll کار می‌کند؟
   - آیا به بخش درست می‌رود؟
   - آیا heading highlight می‌شود؟

4. **Responsive را تست کنید:**
   - Desktop: فهرست باز
   - Mobile: دکمه Toggle
   - Tablet: استایل مناسب

---

## 🐛 عیب‌یابی

### مشکل: TOC نمایش داده نمی‌شود

**راه‌حل:**
1. بررسی کنید مقاله حداقل یک heading دارد
2. Cache مرورگر را پاک کنید
3. سایت را rebuild کنید:
   ```bash
   hugo --gc --minify
   ```

### مشکل: Headings ID ندارند

**راه‌حل:**
1. بررسی کنید `heading-ids.js` لود شده باشد
2. Console مرورگر را برای خطاها بررسی کنید
3. مطمئن شوید JavaScript فعال است

### مشکل: کلیک روی TOC کار نمی‌کند

**راه‌حل:**
1. بررسی کنید ID headings با href لینک‌ها match باشد
2. Console را برای خطاها بررسی کنید
3. مطمئن شوید smooth scroll فعال است

---

## 📊 مثال TOC

برای مقاله با ساختار زیر:

```markdown
# عنوان اصلی

## مقدمه

### تاریخچه

## محتوای اصلی

### بخش اول
#### زیر بخش 1
#### زیر بخش 2

### بخش دوم
#### زیر بخش 1

## نتیجه‌گیری
```

**TOC تولید شده:**

```
📑 فهرست مطالب

▸ عنوان اصلی
  ▸ مقدمه
    ▸ تاریخچه
  ▸ محتوای اصلی
    ▸ بخش اول
      ▸ زیر بخش 1
      ▸ زیر بخش 2
    ▸ بخش دوم
      ▸ زیر بخش 1
  ▸ نتیجه‌گیری
```

---

## 🎨 سفارشی‌سازی

### تغییر رنگ سطوح:

در فایل `toc.css`:

```css
/* سطح 1 - H1 */
#TableOfContents > ul > li > a {
    color: var(--accent-green);  /* رنگ دلخواه */
}

/* سطح 2 - H2 */
#TableOfContents > ul > li > ul > li > a {
    color: var(--accent-blue);   /* رنگ دلخواه */
}
```

### تغییر محل نمایش TOC:

در فایل `single.html`:

```html
<!-- نمایش TOC بعد از محتوا -->
<div class="article-content">
    {{ .Content }}
</div>

{{ if .TableOfContents }}
    <div class="toc-container">
        ...
    </div>
{{ end }}
```

---

## 📈 آمار و اطلاعات

- **تعداد سطوح**: 6 (H1 تا H6)
- **تولید خودکار**: بله
- **Responsive**: بله
- **Smooth Scroll**: بله
- **Highlight Active**: بله
- **پشتیبانی از فارسی**: بله
- **پشتیبانی از انگلیسی**: بله

---

## 🔄 تغییرات آینده

پیشنهادات برای بهبود:

- [ ] اضافه کردن قابلیت collapse/expand برای زیر بخش‌ها
- [ ] اضافه کردن شماره‌گذاری خودکار
- [ ] اضافه کردن progress bar هنگام scroll
- [ ] اضافه کردن دکمه "بازگشت به بالا"
- [ ] اضافه کردن قابلیت print-friendly TOC

---

## 📝 نکات مهم

1. **همیشه از Headings منظم استفاده کنید:**
   - H1 → H2 → H3 (✓ صحیح)
   - H1 → H3 → H2 (✗ نادرست)

2. **از ID های منحصر به فرد استفاده کنید:**
   - سیستم خودکار ID می‌سازد
   - در صورت نیاز می‌توانید ID دستی اضافه کنید

3. **TOC فقط در صفحات Single نمایش داده می‌شود:**
   - نه در Home page
   - نه در List pages
   - فقط در Article pages

---

## 👤 نویسنده

تغییرات توسط Davood Yahya انجام شده است.

---

## 📞 پشتیبانی

در صورت مشکل:

1. Cache مرورگر را پاک کنید
2. سایت را rebuild کنید
3. فایل‌های CSS و JS را بررسی کنید
4. Console مرورگر را برای خطاها بررسی کنید

---

**تاریخ ایجاد**: 2026-02-09  
**آخرین به‌روزرسانی**: 2026-02-09
