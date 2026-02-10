# اصلاحات اندازه کارت مقالات و توضیحات کوتاه

**تاریخ:** 2026-02-08
**نسخه:** 1.0

## خلاصه تغییرات

این مستند تغییرات اعمال شده برای اصلاح اندازه کارت‌های مقالات و توضیحات کوتاه در صفحات دسته‌بندی را شرح می‌دهد.

---

## مشکلات قبلی

1. **اندازه توضیحات کوتاه**: توضیحات کوتاه خیلی طولانی بود (500 کاراکتر) و فضای زیادی اشغال می‌کرد
2. **نمایش Header در Summary**: هدینگ‌های H1-H6 به صورت Header بزرگ در توضیحات کوتاه نمایش داده می‌شدند
3. **اندازه متغیر کارت‌ها**: کارت‌های مقالات بر اساس محتوا اندازه‌های مختلف داشتند
4. **فضای زیاد**: کارت‌ها فضای بیش از حد اشغال می‌کردند

---

## راه‌حل‌های پیاده‌سازی شده

### 1. کاهش اندازه توضیحات کوتاه

**فایل:** `layouts/_default/list.html`

```html
<!-- قبل -->
{{ .Summary | truncate 500 }}

<!-- بعد -->
{{ .Summary | truncate 200 }}
```

**نتیجه:** طول توضیحات از 500 به 200 کاراکتر کاهش یافت (60% کاهش)

---

### 2. حذف کامل Header‌ها در Summary

**فایل:** `assets/css/main.css`

```css
/* Hide all headings completely */
.article-card-summary h1,
.article-card-summary h2,
.article-card-summary h3,
.article-card-summary h4,
.article-card-summary h5,
.article-card-summary h6 {
    display: none !important;
}
```

**فایل:** `static/assets/js/auto-direction.js`

```javascript
// Remove ALL headings completely
const headings = card.querySelectorAll('h1, h2, h3, h4, h5, h6');
headings.forEach(heading => {
    heading.remove();
});
```

**نتیجه:** هیچ هدینگی در توضیحات کوتاه نمایش داده نمی‌شود

---

### 3. ثابت کردن اندازه کارت‌ها

**فایل:** `assets/css/main.css`

```css
.article-card {
    min-height: 240px;
    max-height: 240px;
    height: 240px;
    /* قبلاً 320px بود */
}
```

**نتیجه:** تمام کارت‌ها دقیقاً 240 پیکسل ارتفاع دارند (25% کاهش)

---

### 4. کاهش اندازه Summary Box

**فایل:** `assets/css/main.css`

```css
.article-card-summary {
    font-size: 0.8rem;        /* قبلاً 0.9rem */
    line-height: 1.5;         /* قبلاً 1.6 */
    max-height: 5.4rem;       /* قبلاً 11.2rem */
    height: 5.4rem;
    -webkit-line-clamp: 4;    /* قبلاً 8 خط */
}
```

**نتیجه:** ارتفاع Summary از 11.2rem به 5.4rem کاهش یافت (52% کاهش)

---

### 5. کاهش اندازه عناصر TOC

**فایل:** `assets/css/main.css`

```css
/* List items in TOC */
.article-card-summary li {
    font-size: 0.75rem;       /* قبلاً 0.85rem */
    line-height: 1.4;
}

/* Nested lists */
.article-card-summary ul ul li {
    font-size: 0.7rem;        /* قبلاً 0.8rem */
}
```

**نتیجه:** آیتم‌های لیست کوچک‌تر و فشرده‌تر شدند

---

### 6. کوچک‌تر کردن تیتر کارت

**فایل:** `assets/css/main.css`

```css
.article-card-title {
    font-size: 1.1rem;        /* قبلاً 1.4rem */
    margin-bottom: 0.7rem;    /* قبلاً 1rem */
    -webkit-line-clamp: 2;    /* محدودیت به 2 خط */
    max-height: 3.1rem;
}
```

**نتیجه:** تیترها کوچک‌تر و در صورت طولانی بودن با "..." نمایش داده می‌شوند

---

### 7. کوچک‌تر کردن دکمه "ادامه مطلب"

**فایل:** `assets/css/main.css`

```css
.read-more-btn {
    padding: 0.5rem 1.2rem;   /* قبلاً 0.75rem 1.75rem */
    font-size: 0.85rem;       /* قبلاً 0.95rem */
    margin-top: auto;
    flex-shrink: 0;
}
```

**نتیجه:** دکمه کوچک‌تر ولی همیشه قابل مشاهده است

---

### 8. حذف HR (خطوط افقی)

**فایل:** `assets/css/main.css`

```css
.article-card-summary hr {
    display: none !important;
}
```

**فایل:** `static/assets/js/auto-direction.js`

```javascript
// Remove HR (horizontal rules)
card.querySelectorAll('hr').forEach(hr => {
    hr.remove();
});
```

**نتیجه:** خطوط افقی در Summary نمایش داده نمی‌شوند

---

### 9. Responsive Design

**فایل:** `assets/css/main.css`

#### موبایل (768px و کمتر)
```css
@media (max-width: 768px) {
    .article-card {
        height: 240px;
        min-height: 240px;
        max-height: 240px;
    }
    
    .article-card-title {
        font-size: 1rem;
    }
}
```

#### موبایل کوچک (480px و کمتر)
```css
@media (max-width: 480px) {
    .article-card {
        height: 230px;
        min-height: 230px;
        max-height: 230px;
    }
    
    .article-card-summary {
        font-size: 0.75rem;
        max-height: 5rem;
    }
    
    .read-more-btn {
        padding: 0.45rem 1rem;
        font-size: 0.8rem;
    }
}
```

**نتیجه:** در تمام اندازه صفحات، کارت‌ها به درستی نمایش داده می‌شوند

---

## مقایسه قبل و بعد

### نسخه اولیه (قبل از تغییرات):
- **ارتفاع کارت:** 320px
- **ارتفاع Summary:** 11.2rem (~179px)
- **تعداد خطوط:** 8 خط
- **اندازه فونت:** 0.9rem
- **طول متن:** 500 کاراکتر
- **Header:** نمایش داده می‌شد
- **Grid:** 3 ستونی

### نسخه 1.0 (تغییرات اول - خیلی کوچک):
- **ارتفاع کارت:** 240px ❌ (خیلی کوچک)
- **ارتفاع Summary:** 5.4rem ❌ (خیلی کوچک)
- **تعداد خطوط:** 4 خط ❌
- **اندازه فونت:** 0.8rem ❌ (خوانایی پایین)
- **طول متن:** 200 کاراکتر ✅
- **Header:** حذف شد ✅
- **Grid:** 3 ستونی ❌

### نسخه 2.0 (تغییرات نهایی - بهینه):
- **ارتفاع کارت:** 360px ✅ (1.5x بهتر، خوانا)
- **ارتفاع Summary:** 10rem ✅ (بهینه)
- **تعداد خطوط:** 6 خط ✅ (مناسب)
- **اندازه فونت:** 0.95rem ✅ (خوانا)
- **طول متن:** 200 کاراکتر ✅ (مناسب)
- **Header:** حذف شد ✅
- **Grid:** 2 ستونی ✅ (بهتر و واضح‌تر)
- **Scroll:** کل صفحه ✅ (نه فقط بخش مقالات)

---

## نسخه 2.0 - بهبودهای بزرگ (2026-02-08)

### مشکلات نسخه 1.0:
1. ❌ کارت‌ها خیلی کوچک بودند (240px)
2. ❌ خوانایی متن پایین بود (0.8rem)
3. ❌ 3 ستونی بودن باعث شلوغی می‌شد
4. ❌ Scroll داخلی بخش مقالات (اشتباه)
5. ❌ صفحه مقالات خالی نمایش داده می‌شد

### راه‌حل‌های نسخه 2.0:

#### 1. افزایش سایز کارت به 1.5 برابر

```css
.article-card {
    height: 360px;          /* قبلاً 240px */
    padding: 2rem;          /* قبلاً 1.5rem */
}
```

#### 2. افزایش سایز فونت‌ها

```css
/* Title */
.article-card-title {
    font-size: 1.4rem;      /* قبلاً 1.1rem */
    line-height: 1.5;
    max-height: 4.2rem;
}

/* Summary */
.article-card-summary {
    font-size: 0.95rem;     /* قبلاً 0.8rem */
    line-height: 1.6;
    max-height: 10rem;      /* قبلاً 5.4rem */
    -webkit-line-clamp: 6;  /* قبلاً 4 */
}

/* List items */
.article-card-summary li {
    font-size: 0.9rem;      /* قبلاً 0.75rem */
    margin-bottom: 0.3rem;
}

/* Nested lists */
.article-card-summary ul ul li {
    font-size: 0.85rem;     /* قبلاً 0.7rem */
}

/* Button */
.read-more-btn {
    font-size: 0.95rem;     /* قبلاً 0.85rem */
    padding: 0.7rem 1.5rem; /* قبلاً 0.5rem 1.2rem */
}
```

#### 3. تبدیل به 2 ستونی

```css
.articles-grid {
    grid-template-columns: repeat(2, 1fr);  /* قبلاً repeat(3, 1fr) */
    gap: 2.5rem;                            /* قبلاً 2rem */
}
```

**مزایا:**
- ✅ کارت‌ها بزرگ‌تر و واضح‌تر
- ✅ فضای بیشتر برای هر مقاله
- ✅ خوانایی بهتر

#### 4. حذف Scroll داخلی و اعمال Scroll کلی

```css
.main-content {
    overflow-y: visible;    /* Scroll به کل صفحه منتقل شد */
}
```

**قبل:** Scroll فقط برای بخش مقالات (سمت چپ)
**بعد:** Scroll برای کل صفحه (سمت راست)
**Sidebar:** Scroll مستقل خودش را دارد ✅

#### 5. رفع مشکل صفحه خالی مقالات

**مشکل:** با کلیک روی کارت یا "ادامه مطلب"، صفحه خالی نشان داده می‌شد

**علت:** baseURL در hugo.toml به `/articles/` ختم می‌شد ولی سرور روی `/` اجرا می‌شد

**راه‌حل:**
```bash
hugo server -D --baseURL http://localhost:1313/
```

#### 6. Responsive Design کامل

**Tablet (≤768px):**
```css
.article-card {
    height: 340px;
    padding: 1.8rem;
}

.article-card-title {
    font-size: 1.3rem;
}

.article-card-summary {
    font-size: 0.9rem;
    max-height: 9rem;
}

.articles-grid {
    grid-template-columns: 1fr;  /* تک ستونی */
}
```

**Mobile (≤480px):**
```css
.article-card {
    height: 320px;
    padding: 1.5rem;
}

.article-card-title {
    font-size: 1.2rem;
}

.article-card-summary {
    font-size: 0.85rem;
    max-height: 8rem;
}

.read-more-btn {
    padding: 0.6rem 1.3rem;
    font-size: 0.9rem;
}
```

---

## فایل‌های تغییر یافته

1. ✅ `layouts/_default/list.html` - کاهش truncate از 500 به 200
2. ✅ `assets/css/main.css` - تمام تغییرات CSS
3. ✅ `static/assets/css/main.css` - کپی از assets
4. ✅ `static/assets/js/auto-direction.js` - حذف کامل Header‌ها و HR
5. ✅ `public/assets/js/auto-direction.js` - کپی شده از static
6. ✅ `public/` - Rebuild شده با Hugo

---

## نتایج نهایی (نسخه 2.0)

✅ **اندازه بهینه کارت‌ها:** 360px (Desktop), 340px (Tablet), 320px (Mobile)
✅ **Grid دو ستونی:** کارت‌ها واضح‌تر و بزرگ‌تر نمایش داده می‌شوند
✅ **حذف Header:** هیچ هدینگی در Summary نمایش داده نمی‌شود
✅ **خوانایی بالا:** فونت‌ها بزرگ‌تر شدند (0.95rem برای متن اصلی)
✅ **Scroll صحیح:** Scroll به کل صفحه اعمال شد (نه فقط بخش مقالات)
✅ **Responsive کامل:** در تمام دیوایس‌ها به خوبی کار می‌کند
✅ **دکمه ادامه مطلب:** بزرگ‌تر و همیشه قابل مشاهده
✅ **رفع مشکل صفحه خالی:** مقالات به درستی نمایش داده می‌شوند
✅ **TOC خوانا:** لیست‌ها با فونت مناسب نمایش داده می‌شوند

---

## دستورات Build

برای rebuild کردن سایت:

```bash
# Development build
hugo --gc --minify

# Production build
hugo --gc --minify --environment production

# Local server
hugo server -D
```

---

## Testing

برای تست تغییرات:

1. **سرور را اجرا کنید:**
   ```bash
   hugo server -D --baseURL http://localhost:1313/
   ```

2. **به صفحه اصلی بروید:**
   ```
   http://localhost:1313/
   ```

3. **به صفحات دسته‌بندی بروید:**
   - `http://localhost:1313/cyber-security/`
   - `http://localhost:1313/linux/`
   - `http://localhost:1313/python/`

4. **بررسی کنید:**
   - ✅ کارت‌ها 2 ستونی هستند (نه 3 ستونی)
   - ✅ اندازه کارت‌ها 360px است (بزرگ و خوانا)
   - ✅ هیچ Header بزرگی نمایش داده نمی‌شود
   - ✅ فونت‌ها خوانا هستند (0.95rem)
   - ✅ دکمه "ادامه مطلب" بزرگ و واضح است
   - ✅ Scroll برای کل صفحه است (نه فقط بخش مقالات)
   - ✅ Sidebar Scroll مستقل خودش را دارد

5. **کلیک روی مقاله:**
   - ✅ صفحه مقاله به درستی نمایش داده می‌شود
   - ✅ استایل‌ها صحیح هستند
   - ✅ محتوا کامل است

6. **تست Responsive:**
   - **Desktop (>1200px):** 2 ستونی، کارت 360px
   - **Tablet (768px-1200px):** 1 ستونی، کارت 340px
   - **Mobile (<480px):** 1 ستونی، کارت 320px

---

## یادداشت‌ها

- این تغییرات بر روی تمام صفحات لیست (دسته‌بندی‌ها) اعمال می‌شود
- تغییرات بر صفحات تک مقاله تأثیری ندارد
- CSS در هر دو مسیر `assets/` و `static/` آپدیت شده است
- JavaScript فقط بر روی کارت‌های مقالات اعمال می‌شود و بر محتوای مقاله تأثیری ندارد

---

---

## خلاصه تغییرات نسخه 2.0

| ویژگی | قبل (v1.0) | بعد (v2.0) | تغییر |
|------|-----------|-----------|-------|
| ارتفاع کارت | 240px | 360px | +50% ⬆️ |
| Grid Layout | 3 ستونی | 2 ستونی | واضح‌تر ✅ |
| فونت متن | 0.8rem | 0.95rem | +18% ⬆️ |
| فونت تیتر | 1.1rem | 1.4rem | +27% ⬆️ |
| تعداد خطوط | 4 | 6 | +50% ⬆️ |
| Scroll | داخلی ❌ | کلی ✅ | رفع شد ✅ |
| صفحه مقاله | خالی ❌ | کامل ✅ | رفع شد ✅ |

---

## دستورات مهم

```bash
# راه‌اندازی سرور (Development)
hugo server -D --baseURL http://localhost:1313/

# Build برای Production
hugo --gc --minify --environment production

# بررسی سرعت Build
hugo --gc --minify --templateMetrics
```

---

**تهیه‌کننده:** Davood Yahya  
**نسخه:** 2.0 (بهبود یافته)  
**تاریخ آخرین به‌روزرسانی:** 2026-02-08
