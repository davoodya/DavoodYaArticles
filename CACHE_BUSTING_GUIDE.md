# راهنمای Cache Busting و Asset Fingerprinting

تاریخ: Mon Feb 09 2026

## 🔴 مشکل: تغییرات CSS اعمال نمی‌شوند

شما فایل `/assets/css/main.css` را ویرایش می‌کنید اما:
- تغییرات در مرورگر دیده نمی‌شوند
- مرورگر همچنان فایل قدیمی را نمایش می‌دهد
- حتی با F5 و Refresh هم تغییری ندارد

## 🔍 علت مشکل

مشکل از **Browser Cache** است. مرورگر فایل CSS را cache می‌کند تا بارگذاری سریع‌تر شود، اما وقتی شما فایل را تغییر می‌دهید، مرورگر نمی‌داند که نسخه جدید موجود است.

## ✅ راه‌حل: Hugo Asset Fingerprinting

Hugo می‌تواند برای هر فایل CSS یک **hash منحصر به فرد** (fingerprint) ایجاد کند. وقتی فایل تغییر می‌کند، hash هم تغییر می‌کند و مرورگر مجبور است نسخه جدید را دانلود کند.

### قبل (بدون fingerprinting):
```html
<link rel="stylesheet" href="/assets/css/main.css">
```
مرورگر این فایل را cache می‌کند و تغییرات را نمی‌بیند.

### بعد (با fingerprinting):
```html
<link rel="stylesheet" href="/css/main.95cb97a8c9d80678786fa4a8d7ed5b881f4677ffa712c963713230d6e95d75b4.css">
```
وقتی `main.css` تغییر کند، hash تغییر می‌کند:
```html
<link rel="stylesheet" href="/css/main.02bb3c3bba7405e6965c8d1d19619426d3b7f0e9c6d6f29a9edb5dd1ba7f9bb6.css">
```
مرورگر می‌بیند که این فایل جدید است و آن را دانلود می‌کند.

## 📝 تغییرات اعمال شده

### فایل: `layouts/_default/baseof.html`

**قبل:**
```html
<link rel="stylesheet" href="{{ "/assets/css/main.css" | relURL }}" type="text/css">
```

**بعد:**
```html
{{ $main := resources.Get "css/main.css" | resources.Fingerprint }}
<link rel="stylesheet" href="{{ $main.RelPermalink }}" integrity="{{ $main.Data.Integrity }}">
```

### تمام فایل‌های CSS:
1. ✅ `fonts.css`
2. ✅ `header-footer.css`
3. ✅ `main.css`
4. ✅ `custom-pages.css`
5. ✅ `search.css`
6. ✅ `font-fixes.css`

## 🎯 مزایای این روش

### 1. Cache Busting خودکار
- هر بار که CSS را تغییر دهید، hash جدید ایجاد می‌شود
- مرورگر به صورت خودکار نسخه جدید را دانلود می‌کند
- نیازی به hard refresh (Ctrl+F5) نیست

### 2. Subresource Integrity (SRI)
```html
integrity="sha256-ALvMOYm8wBa...="
```
- امنیت بیشتر: مرورگر تأیید می‌کند که فایل تغییر نکرده
- جلوگیری از حملات Man-in-the-Middle
- اطمینان از یکپارچگی فایل

### 3. Performance بهتر
- مرورگر می‌تواند فایل‌های قدیمی را cache کند
- فقط زمانی که فایل تغییر کند، دوباره دانلود می‌شود
- سرعت بارگذاری بهتر برای کاربران

## 🚀 نحوه استفاده

### مرحله 1: ویرایش CSS
فایل `/assets/css/main.css` را ویرایش کنید:

```css
.article-card {
    min-height: 300px; /* تغییر شما */
}
```

### مرحله 2: Build کردن
```bash
hugo --cleanDestinationDir
```

Hugo به صورت خودکار:
- فایل CSS را می‌خواند
- hash جدید محاسبه می‌کند
- فایل با نام جدید ساخته می‌شود
- HTML ها را با لینک جدید به‌روزرسانی می‌کند

### مرحله 3: تست
1. سایت را باز کنید: `http://localhost:1313/`
2. F12 → Network → بررسی کنید که فایل CSS با hash جدید لود شده
3. تغییرات شما به صورت خودکار اعمال شده‌اند! 🎉

## 🔧 راه‌حل‌های اضافی

### 1. اگر همچنان تغییرات دیده نمی‌شوند:

#### روش 1: Hard Refresh
- **Windows/Linux:** `Ctrl + F5` یا `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`

#### روش 2: پاک کردن کش مرورگر
```
F12 → Network → Disable cache (checkbox) → Refresh
```

#### روش 3: پاک کردن public و rebuild
```bash
# پاک کردن public
Remove-Item -Recurse -Force public

# Build دوباره
hugo --cleanDestinationDir
```

### 2. برای Development:

استفاده از `hugo server` با live reload:

```bash
hugo server -D --disableFastRender
```

با این دستور:
- Hugo به صورت خودکار تغییرات را می‌بیند
- صفحه را refresh می‌کند
- fingerprint جدید ایجاد می‌شود

### 3. بررسی fingerprint در HTML:

بعد از build، فایل `public/index.html` را باز کنید:

```html
<link rel="stylesheet" href="/css/main.02bb3c3bba7405e6965c8d1d19619426d3b7f0e9c6d6f29a9edb5dd1ba7f9bb6.css" integrity="sha256-ALvMOYm8wBaFyNHRlhkmbTt38OnG1vKantXdG6f5u7Y=">
```

اگر این hash را می‌بینید، یعنی fingerprinting کار می‌کند! ✅

## 📊 مقایسه: قبل و بعد

### قبل (بدون fingerprinting):
```
/public/css/main.css         (34092 bytes)
```
- همیشه همین فایل load می‌شد
- تغییرات دیده نمی‌شدند
- مرورگر cache قدیمی را استفاده می‌کرد

### بعد (با fingerprinting):
```
/public/css/main.95cb97a8c9d80678786fa4a8d7ed5b881f4677ffa712c963713230d6e95d75b4.css
```
بعد از تغییر:
```
/public/css/main.02bb3c3bba7405e6965c8d1d19619426d3b7f0e9c6d6f29a9edb5dd1ba7f9bb6.css
```
- هر تغییر = hash جدید
- مرورگر فایل جدید را دانلود می‌کند
- تغییرات به صورت خودکار اعمال می‌شوند

## 🛠️ دیگر قابلیت‌های Hugo Pipes

### 1. Minify (فشرده‌سازی):
```go
{{ $main := resources.Get "css/main.css" | resources.Minify | resources.Fingerprint }}
```

### 2. PostCSS:
```go
{{ $main := resources.Get "css/main.css" | resources.PostCSS | resources.Fingerprint }}
```

### 3. Bundle کردن چند فایل:
```go
{{ $styles := slice (resources.Get "css/main.css") (resources.Get "css/header.css") }}
{{ $bundle := $styles | resources.Concat "css/bundle.css" | resources.Minify | resources.Fingerprint }}
```

## 📚 منابع بیشتر

- [Hugo Asset Pipeline](https://gohugo.io/hugo-pipes/)
- [Hugo resources.Fingerprint](https://gohugo.io/hugo-pipes/fingerprint/)
- [Subresource Integrity (SRI)](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)

## ✅ چک‌لیست

بعد از اعمال این تغییرات:

- [x] فایل‌های CSS با fingerprint ساخته می‌شوند
- [x] تغییرات به صورت خودکار اعمال می‌شوند
- [x] مشکل cache برطرف شد
- [x] SRI برای امنیت بیشتر فعال شد
- [x] Performance بهتر شد

## 🎉 نتیجه

با اعمال Hugo Asset Fingerprinting:
- **دیگر نیازی به hard refresh نیست**
- **تغییرات به صورت خودکار اعمال می‌شوند**
- **مشکل cache برای همیشه حل شد**

از این به بعد، هر تغییری که در `/assets/css/main.css` انجام دهید، به صورت خودکار با یک hash جدید ساخته می‌شود و مرورگر آن را دانلود می‌کند! 🚀

---

**آخرین بروزرسانی:** Mon Feb 09 2026
