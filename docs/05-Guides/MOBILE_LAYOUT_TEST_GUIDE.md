# راهنمای تست Layout موبایل

## 🧪 روش تست

### 1. استفاده از Hugo Server (Development)

```bash
hugo server -D --disableFastRender
```

سپس مرورگر را باز کنید و به آدرس `http://localhost:1313` بروید.

### 2. استفاده از Build شده (Production)

```bash
hugo --cleanDestinationDir
```

سپس فایل‌های داخل پوشه `public` را در یک سرور محلی یا آنلاین باز کنید.

## 📱 مراحل تست در مرورگر

### Chrome DevTools

1. سایت را باز کنید
2. `F12` یا `Ctrl+Shift+I` را فشار دهید
3. روی آیکون 📱 (Toggle device toolbar) کلیک کنید یا `Ctrl+Shift+M`
4. از منوی بالا یک دستگاه موبایل انتخاب کنید:
   - iPhone 12/13/14
   - Samsung Galaxy S20/21
   - Pixel 5
   - یا Responsive

### صفحات برای تست

#### صفحه Single Article
1. به یکی از مقالات بروید:
   - `/cyber-security/cryptography/...`
   - `/linux/60-commands-hacker-should-know-it/`
   - `/python/dir-buster-module/`

2. بررسی کنید:
   - ✅ عنوان مقاله در ابتدا
   - ✅ فهرست مطالب (TOC) بعد از عنوان
   - ✅ محتوای مقاله
   - ✅ Sidebar در آخر (قبل از Footer)

#### صفحه List (دسته‌بندی)
1. به صفحه دسته‌بندی بروید:
   - `/cyber-security/`
   - `/linux/`
   - `/python/`
   - `/seo/`
   - `/tools/`

2. بررسی کنید:
   - ✅ عنوان دسته‌بندی در ابتدا
   - ✅ لیست مقالات (Article Cards)
   - ✅ Pagination (اگر بیش از 10 مقاله باشد)
   - ✅ Sidebar در آخر (قبل از Footer)

### نقاط مهم برای بررسی

#### Desktop (بالای 1024px)
```
┌──────────────────────────────────────────┐
│             Header / Navbar              │
├───────────────┬──────────────────────────┤
│               │                          │
│   Sidebar     │     Main Content         │
│   (350px)     │     (Flex: 1fr)          │
│               │                          │
│               │                          │
└───────────────┴──────────────────────────┘
│             Footer                       │
└──────────────────────────────────────────┘
```

#### Tablet (769px - 1024px)
```
┌──────────────────────────────────────────┐
│             Header / Navbar              │
├──────────────────────────────────────────┤
│                                          │
│          Main Content (Full)             │
│                                          │
├──────────────────────────────────────────┤
│                                          │
│          Sidebar (Full)                  │
│                                          │
└──────────────────────────────────────────┘
│             Footer                       │
└──────────────────────────────────────────┘
```

#### Mobile (زیر 768px)
```
┌──────────────────────────────────────────┐
│             Header / Navbar              │
├──────────────────────────────────────────┤
│                                          │
│          Main Content (Full)             │
│                                          │
├──────────────────────────────────────────┤
│                                          │
│          Sidebar (Full)                  │
│                                          │
└──────────────────────────────────────────┘
│             Footer                       │
└──────────────────────────────────────────┘
```

## 🔍 بررسی با Inspect Element

برای اطمینان از اعمال صحیح CSS:

1. روی محتوای اصلی کلیک راست کنید
2. Inspect Element را انتخاب کنید
3. کلاس‌های زیر را بررسی کنید:
   - `.main-content-wrapper` باید `display: flex` و `flex-direction: column` داشته باشد
   - `.article-wrapper` یا `.main-content` باید `order: 1` داشته باشد
   - `.sidebar` باید `order: 2` داشته باشد

### مثال Expected CSS (Mobile)

```css
.main-content-wrapper {
    display: flex;
    flex-direction: column;
}

.article-wrapper {
    order: 1;
}

.sidebar {
    order: 2;
    margin-top: 3rem;
}
```

## 📏 Breakpoints

برای تست دقیق‌تر، این Breakpoint ها را بررسی کنید:

| دستگاه | عرض | Layout |
|--------|-----|--------|
| Mobile Small | 320px - 480px | Flex Column |
| Mobile | 481px - 768px | Flex Column |
| Tablet | 769px - 1024px | Flex Column |
| Desktop | 1025px+ | Grid 2 Column |

## 🐛 مشکلات احتمالی

### مشکل: Sidebar هنوز بالاست

**راه‌حل:**
1. Cache مرورگر را پاک کنید (`Ctrl+Shift+R`)
2. بررسی کنید که فایل CSS جدید لود شده:
   - DevTools → Network → فیلتر CSS
   - فایل `main.css` را پیدا کنید
   - بررسی کنید که Cache Busting درست کار می‌کند

### مشکل: در دسکتاپ Layout خراب است

**راه‌حل:**
1. بررسی کنید که `@media (min-width: 1025px)` درست کار می‌کند
2. Grid Layout باید فعال باشد

### مشکل: Sidebar فاصله زیادی دارد

**راه‌حل:**
`margin-top: 3rem` روی `.sidebar` در موبایل تنظیم شده. می‌توانید در CSS تغییر دهید:

```css
@media (max-width: 1024px) {
    .sidebar {
        margin-top: 2rem; /* یا هر مقدار دیگری */
    }
}
```

## ✅ Checklist

- [ ] صفحه Single Article در موبایل: محتوا ابتدا، Sidebar بعد
- [ ] صفحه List در موبایل: محتوا ابتدا، Sidebar بعد
- [ ] صفحه Single Article در دسکتاپ: Sidebar راست، محتوا چپ
- [ ] صفحه List در دسکتاپ: Sidebar راست، محتوا چپ
- [ ] Tablet (iPad): محتوا ابتدا، Sidebar بعد
- [ ] Landscape Mode: کار می‌کند
- [ ] Portrait Mode: کار می‌کند

## 🎨 Preview URLs

برای تست سریع:

- **صفحه اصلی**: `http://localhost:1313/`
- **دسته‌بندی Cyber Security**: `http://localhost:1313/cyber-security/`
- **یک مقاله نمونه**: `http://localhost:1313/linux/60-commands-hacker-should-know-it/`

## 📝 یادداشت‌ها

- این تغییرات فقط CSS هستند و نیازی به تغییر HTML نیست
- کد Semantic و Accessible است
- Performance بهینه است
- تمام مرورگرهای مدرن پشتیبانی می‌کنند

---

**توجه**: اگر مشکلی مشاهده کردید، از DevTools Console برای بررسی خطاهای احتمالی استفاده کنید.
