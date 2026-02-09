# خلاصه فعال‌سازی Table of Contents (TOC)

## ✅ انجام شد

Table of Contents (فهرست مطالب) برای تمام مقالات با موفقیت فعال شد!

---

## 🎯 ویژگی‌ها

✅ نمایش **تمام Headings** (H1 تا H6)  
✅ **ساختار سلسله مراتبی** با رنگ‌های متمایز  
✅ **کلیک و Navigation** با Smooth Scroll  
✅ **Highlight** کردن heading فعال  
✅ **Responsive** - دکمه Toggle در موبایل  
✅ **Auto-Generated IDs** برای headings  
✅ **استایل Cyberpunk** حرفه‌ای  

---

## 📁 فایل‌های تغییر یافته

1. **hugo.toml** - تنظیمات TOC
2. **layouts/_default/single.html** - اضافه شدن TOC
3. **layouts/_default/baseof.html** - لینک CSS و JS
4. **assets/css/toc.css** - استایل‌های TOC (جدید)
5. **static/assets/js/heading-ids.js** - تولید ID ها (جدید)

---

## 🚀 نحوه استفاده

```bash
# Build سایت
hugo --gc --minify

# یا Development mode
hugo server
```

سپس به هر مقاله بروید - TOC به صورت خودکار نمایش داده می‌شود!

---

## 🎨 نمای TOC

```
📑 فهرست مطالب
├─ عنوان اصلی (سبز)
│  ├─ زیر عنوان (آبی)
│  │  └─ بخش فرعی (نارنجی)
│  └─ زیر عنوان دیگر (آبی)
└─ نتیجه‌گیری (سبز)
```

---

## 🔍 تست

مقاله مثال: **"60 Commands Hacker Should Know it"**

1. TOC در بالای مقاله نمایش داده می‌شود
2. کلیک روی هر آیتم → رفتن به بخش مربوطه
3. Heading فعال highlight می‌شود
4. در موبایل: دکمه Toggle برای باز/بسته کردن

---

## 📚 مستندات کامل

برای جزئیات بیشتر: **`docs/TOC_GUIDE.md`**

---

## 💡 نکات

- TOC فقط اگر مقاله heading داشته باشد نمایش داده می‌شود
- ID ها به صورت خودکار برای headings ساخته می‌شوند
- از حروف فارسی و انگلیسی پشتیبانی می‌کند
- Smooth scroll با offset مناسب برای header

---

**تاریخ**: 2026-02-09  
**نویسنده**: Davood Yahya
