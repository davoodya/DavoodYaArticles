# راهنمای سریع: تصویر شاخص صفحه اصلی

## 📸 نمایش تصاویر شاخص در صفحه اصلی

هر دسته‌بندی در صفحه اصلی می‌تواند یک تصویر شاخص داشته باشد.

## 🚀 نحوه استفاده

### گام 1: باز کردن فایل `_index.md` دسته‌بندی

```bash
content/
  └── your-category/
      └── _index.md
```

### گام 2: اضافه کردن تصویر شاخص

```toml
+++
title = "عنوان دسته‌بندی"
description = "توضیحات دسته‌بندی"

# 👇 این دو خط را اضافه کنید
featured_image = "/images/your-category/your-image.png"
images = ["/images/your-category/your-image.png"]

[params.opengraph]
  image = "/images/your-category/your-image.png"

[params.twitter]
  image = "/images/your-category/your-image.png"
+++
```

### گام 3: قرار دادن تصویر در دایرکتوری مناسب

```bash
static/
  └── images/
      └── your-category/
          └── your-image.png
```

## ⚠️ نکات مهم

1. **مسیر تصویر:** بدون `/static/` بنویسید
   - ✅ صحیح: `/images/category/image.png`
   - ❌ اشتباه: `/static/images/category/image.png`

2. **اندازه تصویر:** حداقل 800x600 پیکسل

3. **فرمت:** PNG یا JPG

4. **حجم:** کمتر از 500KB

## 📱 اندازه‌ها

- **دسکتاپ:** 220px ارتفاع
- **تبلت:** 180px ارتفاع
- **موبایل:** 160px ارتفاع

## 📝 مثال کامل

```toml
+++
title = "امنیت سایبری"
description = "مجموعه مقالات تخصصی امنیت سایبری"

tags = ["cyber-security", "Pentest"]
series = ["cyber-security"]

keywords = ["Cyber Security", "cyber-security", "Pentest"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/knowledge/cyber-security/"

featured_image = "/images/cyber-security/Basic-Encryption-1.png"
images = ["/images/cyber-security/Basic-Encryption-1.png"]

[params.opengraph]
  title = "امنیت سایبری"
  description = "مجموعه مقالات تخصصی امنیت سایبری"
  image = "/images/cyber-security/Basic-Encryption-1.png"
  url = "https://davoodya.ir/knowledge/cyber-security/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "امنیت سایبری"
  description = "مجموعه مقالات تخصصی امنیت سایبری"
  image = "/images/cyber-security/Basic-Encryption-1.png"
+++
```

## 🧪 تست

```bash
# شروع سرور
hugo server -D

# باز کردن مرورگر
http://localhost:1313/
```

## ❓ عیب‌یابی

### تصویر نمایش داده نمی‌شود؟

1. ✅ بررسی مسیر: بدون `/static/` است؟
2. ✅ بررسی فایل: در `static/images/` وجود دارد؟
3. ✅ بررسی نام: دقیقاً مطابقت دارد؟
4. ✅ بررسی frontmatter: `featured_image` یا `images` نوشته شده؟
5. ✅ Clear cache: Ctrl+Shift+R

## 📚 مستندات کامل

برای جزئیات بیشتر:
- **راهنمای کامل:** `docs/CATEGORY_FEATURED_IMAGE_GUIDE.md`
- **خلاصه تغییرات:** `docs/FEATURED_IMAGE_SUMMARY.md`

---

**تاریخ:** 2026-02-09  
**نسخه:** 1.0
