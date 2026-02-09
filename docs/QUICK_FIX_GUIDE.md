# راهنمای سریع رفع مشکلات رایج

**تاریخ:** 2026-02-08

---

## 🔴 مشکل: صفحه مقالات خالی است

### علت:
baseURL در `hugo.toml` با آدرس سرور مطابقت ندارد.

### راه‌حل:
```bash
# به جای این:
hugo server -D

# از این استفاده کنید:
hugo server -D --baseURL http://localhost:1313/
```

---

## 🔴 مشکل: تغییرات CSS اعمال نمی‌شود

### راه‌حل:
```bash
# 1. کپی فایل CSS از assets به static
powershell -Command "Copy-Item -Path 'assets/css/main.css' -Destination 'static/assets/css/main.css' -Force"

# 2. Rebuild کردن Hugo
hugo --gc --minify

# 3. Clear cache مرورگر
Ctrl + Shift + R (Chrome/Edge)
Ctrl + F5 (Firefox)
```

---

## 🔴 مشکل: Scroll داخلی به جای Scroll کلی صفحه

### علت:
`overflow-y` یا `max-height` روی `.main-content` یا `.articles-grid` تنظیم شده.

### راه‌حل:
```css
/* در assets/css/main.css */
.main-content {
    overflow-y: visible;  /* نه auto یا scroll */
}

.articles-grid {
    /* نباید max-height داشته باشد */
}
```

---

## 🔴 مشکل: کارت‌ها اندازه‌های مختلف دارند

### راه‌حل:
```css
.article-card {
    min-height: 360px;
    max-height: 360px;
    height: 360px;  /* سه‌تای اینها باید یکسان باشند */
}
```

---

## 🔴 مشکل: فونت‌ها خیلی کوچک هستند

### راه‌حل:
```css
/* Title */
.article-card-title {
    font-size: 1.4rem;  /* حداقل 1.2rem */
}

/* Summary */
.article-card-summary {
    font-size: 0.95rem;  /* حداقل 0.9rem */
}

/* List items */
.article-card-summary li {
    font-size: 0.9rem;  /* حداقل 0.85rem */
}
```

---

## 🔴 مشکل: Grid 3 ستونی خیلی شلوغ است

### راه‌حل:
```css
.articles-grid {
    grid-template-columns: repeat(2, 1fr);  /* به جای 3 */
}
```

---

## 🔴 مشکل: Header‌ها در Summary نمایش داده می‌شوند

### راه‌حل 1 (CSS):
```css
.article-card-summary h1,
.article-card-summary h2,
.article-card-summary h3,
.article-card-summary h4,
.article-card-summary h5,
.article-card-summary h6 {
    display: none !important;
}
```

### راه‌حل 2 (JavaScript):
```javascript
// در static/assets/js/auto-direction.js
const headings = card.querySelectorAll('h1, h2, h3, h4, h5, h6');
headings.forEach(heading => {
    heading.remove();
});
```

---

## 🟢 دستورات مفید

### Build و Deploy
```bash
# Development
hugo server -D --baseURL http://localhost:1313/

# Production Build
hugo --gc --minify --environment production

# بررسی خطاها
hugo --debug
```

### کپی فایل‌ها
```bash
# CSS
powershell -Command "Copy-Item -Path 'assets/css/main.css' -Destination 'static/assets/css/main.css' -Force"

# JavaScript
powershell -Command "Copy-Item -Path 'static/assets/js/auto-direction.js' -Destination 'public/assets/js/auto-direction.js' -Force"
```

### پاک کردن Cache
```bash
hugo --gc
```

---

## 🟢 چک‌لیست تست

قبل از Deploy، موارد زیر را بررسی کنید:

- [ ] سرور با `--baseURL` صحیح اجرا می‌شود
- [ ] صفحات مقالات به درستی نمایش داده می‌شوند
- [ ] کارت‌ها همه یک اندازه هستند
- [ ] Header‌ها در Summary نمایش داده نمی‌شوند
- [ ] فونت‌ها خوانا هستند (حداقل 0.9rem)
- [ ] Scroll برای کل صفحه است (نه داخلی)
- [ ] در Desktop: 2 ستونی
- [ ] در Tablet: 1 ستونی
- [ ] در Mobile: 1 ستونی
- [ ] دکمه "ادامه مطلب" دیده می‌شود

---

## 📁 فایل‌های مهم

```
davoodya/
├── layouts/_default/
│   ├── list.html          # Grid مقالات
│   └── single.html        # صفحه تک مقاله
├── assets/css/
│   └── main.css           # استایل‌های اصلی
├── static/assets/
│   ├── css/main.css       # کپی از assets
│   └── js/auto-direction.js
└── hugo.toml              # تنظیمات اصلی
```

---

## 🔧 مقادیر بهینه

### Desktop (>1200px)
```css
.article-card { height: 360px; }
.article-card-title { font-size: 1.4rem; }
.article-card-summary { font-size: 0.95rem; }
.articles-grid { grid-template-columns: repeat(2, 1fr); }
```

### Tablet (768px-1200px)
```css
.article-card { height: 340px; }
.article-card-title { font-size: 1.3rem; }
.article-card-summary { font-size: 0.9rem; }
.articles-grid { grid-template-columns: 1fr; }
```

### Mobile (<480px)
```css
.article-card { height: 320px; }
.article-card-title { font-size: 1.2rem; }
.article-card-summary { font-size: 0.85rem; }
.articles-grid { grid-template-columns: 1fr; }
```

---

**نکته:** همیشه بعد از تغییر فایل‌ها، Hugo را rebuild کنید:
```bash
hugo --gc --minify
```
