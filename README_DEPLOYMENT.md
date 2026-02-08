# 🚀 Quick Deployment Guide

## مراحل سریع برای انتشار

### 1️⃣ آماده‌سازی محتوا

```bash
# تبدیل تصاویر Obsidian
python convert_images.py

# اضافه کردن/اصلاح title ها
python title-adder.py

# منتشر کردن تمام مقالات (draft = false)
python publish-all.py
```

### 2️⃣ Build برای Production

**Windows:**
```bash
build-production.bat
```

**Linux/Mac:**
```bash
./build-production.sh
```

### 3️⃣ تست محلی

```bash
cd public
python -m http.server 8000
```

بروید به: `http://localhost:8000/articles/`

### 4️⃣ آپلود به سرور

آپلود محتوای پوشه `public/` به:
```
https://davoodya.ir/articles/
```

---

## ✅ Checklist

- [ ] تصاویر تبدیل شدند
- [ ] Title ها اضافه شدند
- [ ] مقالات منتشر شدند (draft = false)
- [ ] Build موفق بود
- [ ] تست محلی OK
- [ ] جستجو کار می‌کند
- [ ] تصاویر نمایش داده می‌شوند

---

## 📋 تنظیمات مهم

### BaseURL
```toml
# hugo.toml
baseURL = "https://davoodya.ir/articles/"
```

### Search
- فایل: `public/index.json` (باید شامل 20 مقاله باشد)
- JavaScript: `static/assets/js/search.js`
- استفاده از meta tag `base-url`

### Images
- مسیر در markdown: `/images/category/image.png`
- مسیر فیزیکی: `static/images/category/image.png`
- در production: `public/images/category/image.png`

---

## 🐛 مشکلات رایج

**جستجو کار نمی‌کند:**
- بررسی `https://davoodya.ir/articles/index.json`
- پاک کردن cache مرورگر
- بررسی Console: `F12`

**تصاویر نمایش داده نمی‌شوند:**
- بررسی مسیر: `/images/category/image.png`
- بررسی فایل در `public/images/`

**404 Errors:**
- بررسی `.htaccess`
- بررسی baseURL در `hugo.toml`

---

## 📚 مستندات کامل

مستندات تفصیلی: [DEPLOYMENT.md](DEPLOYMENT.md)

---

✅ **همه چیز آماده است!**
