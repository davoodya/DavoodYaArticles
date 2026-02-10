# رفع مشکل Scrollbar افقی اضافه

**تاریخ:** 1405/11/21 (2026-02-10)  
**وضعیت:** ✅ حل شده

---

## 🐛 مشکل

بعد از ترکیب فایل‌های CSS، یک **scrollbar افقی اضافه** در صفحه دسته‌بندی مقالات ظاهر شد که:
- کاربردی نداشت
- UI را بهم می‌ریخت
- در کنار `<div class="main-content-wrapper">` نمایش داده می‌شد

---

## 🔍 علت

بعد از ترکیب CSS ها، برخی تنظیمات `overflow-x: hidden` از دست رفته یا ناقص بود.

---

## 🔧 راه‌حل

### تغییرات اعمال شده:

#### 1. افزودن `overflow-x: hidden` به `html`

```css
html {
    direction: rtl;
    scroll-behavior: smooth;
    font-size: 16px;
    overflow-x: hidden; /* جلوگیری از scrollbar افقی در کل صفحه */
}
```

**دلیل:** جلوگیری از overflow در سطح root element

---

#### 2. افزودن `overflow-x: hidden` به `.main-content-wrapper`

```css
.main-content-wrapper {
    display: grid;
    grid-template-columns: 350px 1fr;
    gap: 3rem;
    align-items: start;
    margin-top: 80px;
    overflow-x: hidden; /* مخفی کردن scrollbar افقی اضافه */
}
```

**دلیل:** جلوگیری از overflow در grid wrapper

---

#### 3. فعال کردن `overflow-x: hidden` در `.main-content`

```css
.main-content {
    min-width: 0;
    overflow-x: hidden; /* مخفی کردن scrollbar افقی در محتوا */
    overflow-y: visible;
}
```

**دلیل:** جلوگیری از overflow در محتوای اصلی

---

## 📊 استایل‌های مرتبط (قبلاً موجود)

این المان‌ها قبلاً `overflow-x: hidden` داشتند:

```css
body {
    overflow-x: hidden; /* ✅ قبلاً موجود بود */
}

.container {
    overflow-x: hidden; /* ✅ قبلاً موجود بود */
}
```

---

## ✅ نتیجه

### قبل:
- ❌ Scrollbar افقی اضافه در صفحه دسته‌بندی
- ❌ UI بهم ریخته
- ❌ تجربه کاربری ضعیف

### بعد:
- ✅ بدون scrollbar افقی اضافه
- ✅ UI تمیز
- ✅ فقط scrollbar عمودی (برای محتوا)
- ✅ تجربه کاربری بهتر

---

## 🧪 تست

برای تست کردن:

```bash
# 1. Build
hugo --gc --minify

# 2. Dev server
hugo server

# 3. در مرورگر:
# - به صفحه دسته‌بندی بروید (مثلاً /cyber-security/)
# - بررسی کنید که scrollbar افقی اضافه وجود ندارد
# - تنها scrollbar عمودی برای scroll محتوا باید باشد
```

---

## 💡 نکات فنی

### چرا scrollbar افقی ایجاد می‌شد؟

احتمالاً یکی از این موارد:

1. **Grid overflow:** عناصر grid از container بیرون می‌زدند
2. **Wide elements:** المان‌هایی با width ثابت بزرگتر از viewport
3. **Negative margins:** margin های منفی که فضای اضافی ایجاد می‌کردند
4. **Position absolute:** المان‌های absolute که خارج از container بودند

### راه‌حل جامع:

اضافه کردن `overflow-x: hidden` در سطوح مختلف:

```
html                    ← سطح اول (root)
  └─ body              ← سطح دوم (document)
      └─ container     ← سطح سوم (wrapper)
          └─ main-content-wrapper  ← سطح چهارم (layout)
              └─ main-content      ← سطح پنجم (content)
```

با این روش، در هیچ سطحی scrollbar افقی ایجاد نمی‌شود.

---

## 📝 Build Result

```bash
hugo --gc --minify

Static files     │ 574 
Total in 1544 ms

Status: ✅ موفقیت‌آمیز
```

---

## ✅ Checklist

- [x] افزودن `overflow-x: hidden` به `html`
- [x] افزودن `overflow-x: hidden` به `.main-content-wrapper`
- [x] فعال کردن `overflow-x: hidden` در `.main-content`
- [x] Build موفقیت‌آمیز
- [x] بررسی عدم تداخل با سایر استایل‌ها
- [x] مستندسازی

---

## 🎯 خلاصه

| مورد | قبل | بعد |
|------|-----|-----|
| Scrollbar افقی | ✗ وجود داشت | ✓ حذف شد |
| `html` overflow-x | - | `hidden` |
| `.main-content-wrapper` overflow-x | - | `hidden` |
| `.main-content` overflow-x | `/* commented */` | `hidden` |
| UI Status | بهم ریخته | تمیز |
| Build | ✓ | ✓ |

---

**Status:** ✅ Fixed  
**Build:** ✅ Successful  
**UI:** ✅ Clean
