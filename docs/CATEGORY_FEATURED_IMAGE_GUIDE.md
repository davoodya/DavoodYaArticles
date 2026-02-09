# راهنمای تصویر شاخص دسته‌بندی‌ها

## نمای کلی

این راهنما نحوه نمایش تصاویر شاخص برای دسته‌بندی‌ها در صفحه اصلی وبسایت را توضیح می‌دهد.

## ویژگی‌ها

### ✅ تصاویر با اندازه ثابت
- **ارتفاع دسکتاپ:** 220px
- **ارتفاع تبلت:** 180px  
- **ارتفاع موبایل:** 160px
- تمام تصاویر با استفاده از `object-fit: cover` به اندازه مشخص force می‌شوند

### ✅ طراحی Responsive
تصاویر در تمام دستگاه‌ها به صورت خودکار تنظیم می‌شوند:
- 📱 موبایل (< 480px)
- 📱 تبلت (< 768px)  
- 💻 دسکتاپ (> 768px)

### ✅ انیمیشن Hover
هنگام hover روی کارت دسته‌بندی، تصویر با افکت zoom (scale 1.1) نمایش داده می‌شود.

---

## پیکربندی

### مرحله 1: اضافه کردن تصویر به `_index.md`

برای هر دسته‌بندی در فایل `content/<category>/_index.md`:

```toml
+++
title = "عنوان دسته‌بندی"
description = "توضیحات دسته‌بندی"

# ✅ تنظیم تصویر شاخص
featured_image = "/images/general/image1.png"
images = ["/images/general/image1.png"]

[params.opengraph]
  image = "/images/general/image1.png"

[params.twitter]
  image = "/images/general/image1.png"
+++
```

### مرحله 2: مسیر تصاویر

**⚠️ نکته مهم:** مسیر تصاویر باید بدون `static/` باشد:

```bash
# ❌ اشتباه
featured_image = "/static/images/general/image1.png"

# ✅ صحیح  
featured_image = "/images/general/image1.png"
```

**توضیح:** Hugo به صورت خودکار تمام فایل‌های داخل `static/` را در root سایت قرار می‌دهد.

---

## نمونه‌های عملی

### دسته‌بندی امنیت سایبری

```toml
+++
title = "امنیت سایبری"
description = "مجموعه مقالات تخصصی امنیت سایبری"

featured_image = "/images/cyber-security/Basic-Encryption-1.png"
images = ["/images/cyber-security/Basic-Encryption-1.png"]

[params.opengraph]
  image = "/images/cyber-security/Basic-Encryption-1.png"

[params.twitter]
  image = "/images/cyber-security/Basic-Encryption-1.png"
+++
```

### دسته‌بندی لینوکس

```toml
+++
title = "لینوکس"
description = "آموزش لینوکس از مفاهیم پایه تا پیشرفته"

featured_image = "/images/linux/60CommandsHackerShouldKnowit-1.png"
images = ["/images/linux/60CommandsHackerShouldKnowit-1.png"]

[params.opengraph]
  image = "/images/linux/60CommandsHackerShouldKnowit-1.png"

[params.twitter]
  image = "/images/linux/60CommandsHackerShouldKnowit-1.png"
+++
```

### دسته‌بندی سئو

```toml
+++
title = "سئو"
description = "مقالات آموزش سئو و بهینه‌سازی"

featured_image = "/images/seo/FindKeywords,WebsiteStructure&NecessaryHTMLTagsforSEO-1.png"
images = ["/images/seo/FindKeywords,WebsiteStructure&NecessaryHTMLTagsforSEO-1.png"]

[params.opengraph]
  image = "/images/seo/FindKeywords,WebsiteStructure&NecessaryHTMLTagsforSEO-1.png"

[params.twitter]
  image = "/images/seo/FindKeywords,WebsiteStructure&NecessaryHTMLTagsforSEO-1.png"
+++
```

---

## ساختار HTML

در فایل `layouts/index.html`:

```html
<article class="category-card">
  <!-- تصویر شاخص -->
  {{ if $imageUrl }}
  <div class="category-image-wrapper">
    <img src="{{ $imageUrl | relURL }}" 
         alt="{{ .Title }}" 
         class="category-featured-image" 
         loading="lazy">
  </div>
  {{ end }}
  
  <!-- محتوای دسته‌بندی -->
  <div class="category-content">
    <h2><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
    <p class="category-description-text">{{ .Params.description }}</p>
    <div class="category-meta">
      <span class="category-count">📚 <strong>{{ len .Pages }}</strong> مطلب</span>
    </div>
  </div>
</article>
```

---

## استایل CSS

### کارت دسته‌بندی

```css
.category-card {
    padding: 0;
    border-radius: 16px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}
```

### تصویر شاخص

```css
.category-image-wrapper {
    width: 100%;
    height: 220px;
    overflow: hidden;
    border-radius: 16px 16px 0 0;
    background: linear-gradient(135deg, rgba(0, 255, 65, 0.05), rgba(58, 173, 223, 0.05));
}

.category-featured-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.category-card:hover .category-featured-image {
    transform: scale(1.1);
}
```

### محتوای کارت

```css
.category-content {
    padding: 2rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}
```

---

## Responsive Design

### تبلت (< 768px)

```css
@media (max-width: 768px) {
    .category-image-wrapper {
        height: 180px;
    }
    
    .category-content {
        padding: 1.5rem 1.2rem;
    }
}
```

### موبایل (< 480px)

```css
@media (max-width: 480px) {
    .category-image-wrapper {
        height: 160px;
    }
    
    .category-content {
        padding: 1.2rem 1rem;
    }
    
    .category-card h2 {
        font-size: 1.3rem;
    }
}
```

---

## اولویت نمایش تصویر

Hugo به ترتیب زیر تصویر را انتخاب می‌کند:

1. **featured_image** - اولویت اول
2. **images[0]** - اگر featured_image خالی باشد
3. **بدون تصویر** - اگر هیچ‌کدام موجود نباشد

```go
{{ $featuredImage := .Params.featured_image }}
{{ $images := .Params.images }}
{{ $imageUrl := "" }}

{{ if $featuredImage }}
  {{ $imageUrl = $featuredImage }}
{{ else if $images }}
  {{ $imageUrl = index $images 0 }}
{{ end }}
```

---

## نکات مهم

### ✅ بهترین روش‌ها

1. **اندازه تصاویر:** حداقل 800x600 پیکسل
2. **نسبت تصویر:** 16:9 یا 4:3
3. **فرمت:** PNG یا JPG
4. **حجم:** حداکثر 500KB برای سرعت بهتر
5. **lazy loading:** تصاویر با `loading="lazy"` بارگذاری می‌شوند

### ⚠️ موارد احتیاط

- مسیر تصویر باید بدون `/static` باشد
- تصویر باید در دایرکتوری `static/images/` موجود باشد
- اطمینان حاصل کنید نام فایل و مسیر دقیقاً مطابقت دارند
- برای SEO بهتر است تصاویر alt text مناسب داشته باشند

---

## تست و بررسی

### بررسی صفحه اصلی

```bash
# شروع سرور توسعه
hugo server -D

# مشاهده صفحه اصلی
http://localhost:1313/
```

### بررسی Responsive

1. باز کردن DevTools (F12)
2. Toggle device toolbar (Ctrl+Shift+M)
3. تست در اندازه‌های مختلف:
   - iPhone SE (375px)
   - iPad (768px)
   - Desktop (1920px)

---

## عیب‌یابی

### تصویر نمایش داده نمی‌شود

**چک‌لیست:**

1. ✅ مسیر تصویر بدون `/static` است؟
2. ✅ فایل تصویر در `static/images/` موجود است؟
3. ✅ نام فایل و مسیر دقیقاً مطابقت دارد؟ (حساس به حروف بزرگ و کوچک)
4. ✅ `featured_image` یا `images` در frontmatter تنظیم شده؟

### تصویر کشیده یا فشرده است

**راه‌حل:**  
استفاده از `object-fit: cover` که به صورت خودکار در CSS پیاده‌سازی شده.

### تصویر در موبایل بزرگ است

**راه‌حل:**  
Media queries به صورت خودکار ارتفاع را تنظیم می‌کنند:
- دسکتاپ: 220px
- تبلت: 180px
- موبایل: 160px

---

## فایل‌های تغییر یافته

### 1. `layouts/index.html`
- اضافه شدن نمایش تصویر شاخص
- لاجیک انتخاب تصویر از `featured_image` یا `images`

### 2. `assets/css/main.css` و `static/css/main.css`
- استایل `.category-image-wrapper`
- استایل `.category-featured-image`
- استایل `.category-content`
- Media queries برای responsive

### 3. فایل‌های `_index.md` دسته‌بندی‌ها
- `content/cyber-security/_index.md`
- `content/linux/_index.md`
- `content/seo/_index.md`
- `content/tools/_index.md`

---

## مثال کامل

یک دسته‌بندی جدید با تصویر شاخص:

```bash
# ایجاد دایرکتوری دسته‌بندی
mkdir content/new-category

# ایجاد فایل _index.md
```

```toml
+++
title = "دسته‌بندی جدید"
description = "توضیحات دسته‌بندی جدید"

tags = ["tag1", "tag2"]
series = ["series-name"]

keywords = ["keyword1", "keyword2"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/knowledge/new-category/"

# ✅ تصویر شاخص
featured_image = "/images/new-category/featured.png"
images = ["/images/new-category/featured.png"]

[params.opengraph]
  title = "دسته‌بندی جدید"
  description = "توضیحات دسته‌بندی جدید"
  image = "/images/new-category/featured.png"
  url = "https://davoodya.ir/knowledge/new-category/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "دسته‌بندی جدید"
  description = "توضیحات دسته‌بندی جدید"
  image = "/images/new-category/featured.png"
+++
```

```bash
# کپی تصویر به دایرکتوری مناسب
mkdir static/images/new-category
cp /path/to/image.png static/images/new-category/featured.png
```

---

## نتیجه‌گیری

با این پیاده‌سازی:

✅ تصاویر شاخص در صفحه اصلی برای هر دسته‌بندی نمایش داده می‌شوند  
✅ تمام تصاویر با اندازه ثابت و responsive هستند  
✅ انیمیشن hover برای تجربه کاربری بهتر  
✅ lazy loading برای بهبود سرعت  
✅ سازگاری با تمام دستگاه‌ها  
✅ مدیریت آسان از طریق frontmatter

---

**تاریخ ایجاد:** 2026-02-09  
**نسخه:** 1.0  
**نویسنده:** Davood Yahay
