# راهنمای عیب‌یابی سیستم فیلتر مقالات

## 🐛 مشکل: فیلترها کار نمی‌کنند

اگر فیلترها نمایش داده می‌شوند اما مقالات فیلتر نمی‌شوند، این راهنما به شما کمک می‌کند مشکل را پیدا کنید.

---

## 🔍 گام 1: بررسی Console در مرورگر

### چگونه Console را باز کنیم؟

1. **Chrome/Edge/Firefox**: کلید `F12` را فشار دهید
2. رفتن به تب **Console**
3. رفرش کردن صفحه (`Ctrl + R`)

### چه چیزی باید ببینیم؟

اگر همه چیز درست باشد، باید این پیام‌ها را ببینید:

```
[Filter System] Initializing...
[Filter System] Found articles: 8
[Filter System] Extracting article data from 8 articles
[Article 1] Found 4 badges
[Article 1][Badge 1] Text: "14 دقیقه"
[Article 1] Reading Time: 14 minutes
[Article 1][Badge 2] Text: "حرفه‌ای"
[Article 1] Difficulty: intermediate
[Article 1][Badge 3] Text: "تمرین عملی"
[Article 1] Lab Required: true
[Article 1][Badge 4] Text: "آموزشی"
[Article 1] Post Type: آموزشی
[Article 1] Final data: {readingTime: 14, difficulty: "intermediate", labRequired: true, postType: "آموزشی"}
...
[Filter System] Data extraction complete
[Filter System] Setting up range sliders
[Filter System] Initialization complete
```

### اگر خطا دیدید:

#### خطا: `filters.js:xxx Uncaught ReferenceError: ...`
**معنی**: فایل JavaScript لود نشده است.

**راه‌حل:**
1. بررسی کنید که فایل `static/assets/js/filters.js` وجود دارد
2. Build کنید: `hugo --gc --minify`
3. بررسی کنید که فایل `public/assets/js/filters.js` ایجاد شده
4. رفرش کامل صفحه: `Ctrl + Shift + R`

#### خطا: `[Filter System] Found articles: 0`
**معنی**: هیچ article-card در صفحه وجود ندارد.

**راه‌حل:**
1. بررسی کنید که در یک صفحه لیست (مثل `/network/`) هستید نه صفحه تکی
2. بررسی کنید که مقالاتی در آن دسته‌بندی وجود دارد

---

## 🔍 گام 2: بررسی Badge ها در HTML

### چگونه HTML را بررسی کنیم?

1. باز کردن Developer Tools (`F12`)
2. رفتن به تب **Elements** (یا Inspector در Firefox)
3. یافتن یک `.article-card`
4. باز کردن بخش `.article-card-badges`

### ساختار صحیح Badge ها:

```html
<div class="article-card-badges">
    <!-- Reading Time Badge -->
    <span class="article-badge badge-time">
        <span class="badge-text">14 دقیقه</span>
    </span>
    
    <!-- Difficulty Badge -->
    <span class="article-badge badge-difficulty badge-intermediate">
        <span class="badge-text">حرفه‌ای</span>
    </span>
    
    <!-- Lab Required Badge -->
    <span class="article-badge badge-lab">
        <span class="badge-text">تمرین عملی</span>
    </span>
    
    <!-- Post Type Badge -->
    <span class="article-badge badge-type">
        <span class="badge-text">آموزشی</span>
    </span>
</div>
```

### نکات مهم:

- ✅ باید کلاس `article-badge` وجود داشته باشد
- ✅ باید کلاس نوع Badge (`badge-time`, `badge-difficulty`, ...) وجود داشته باشد
- ✅ باید یک `<span class="badge-text">` داخل Badge باشد
- ✅ متن داخل `badge-text` باید خوانا باشد

---

## 🔍 گام 3: بررسی Data Attributes

پس از لود شدن صفحه، JavaScript باید `data-*` attributes را به `.article-card` اضافه کند.

### چگونه بررسی کنیم?

1. باز کردن Developer Tools (`F12`)
2. رفتن به تب **Elements**
3. یافتن یک `.article-card`
4. بررسی attribute ها

### باید این attribute ها را ببینید:

```html
<article class="article-card" 
         data-reading-time="14" 
         data-difficulty="intermediate" 
         data-lab-required="true" 
         data-post-type="آموزشی">
```

### اگر attribute ها وجود نداشتند:

**مشکل**: JavaScript به درستی اجرا نشده است.

**راه‌حل:**
1. بررسی Console برای خطا
2. رفرش کامل صفحه: `Ctrl + Shift + R`
3. بررسی که JavaScript لود شده: تب Network → `filters.js` باید Status Code 200 باشد

---

## 🔍 گام 4: تست دستی فیلتر

### در Console این دستورات را اجرا کنید:

```javascript
// بررسی تعداد مقالات
document.querySelectorAll('.article-card').length

// بررسی اولین مقاله
const firstArticle = document.querySelector('.article-card');
console.log({
    readingTime: firstArticle.dataset.readingTime,
    difficulty: firstArticle.dataset.difficulty,
    labRequired: firstArticle.dataset.labRequired,
    postType: firstArticle.dataset.postType
});

// تست اعمال فیلتر
applyFilters();
```

### نتیجه باید باشد:

```
8  // تعداد مقالات
{
    readingTime: "14",
    difficulty: "intermediate",
    labRequired: "true",
    postType: "آموزشی"
}
[Filter System] Applying filters (Desktop)...
[Filter System] Filter criteria: {...}
...
[Filter System] Filter complete. Visible: 5/8
```

---

## 🔍 گام 5: بررسی فیلترهای انتخاب شده

### چک کردن checkboxها:

```javascript
// سطح دشواری
Array.from(document.querySelectorAll('input[name="difficulty"]:checked'))
    .map(i => i.value)

// نیاز به تمرین
Array.from(document.querySelectorAll('input[name="lab_required"]:checked'))
    .map(i => i.value)

// نوع پست
Array.from(document.querySelectorAll('input[name="post_type"]:checked'))
    .map(i => i.value)
```

### نتیجه باید آرایه‌ای از مقادیر باشد:

```javascript
["beginner", "medium", "intermediate", "advanced"]
["true", "false"]
["آموزشی", "مقاله", "اسکریپت", ...]
```

---

## 🔍 گام 6: تست با فایل HTML ساده

یک فایل تست ساده ایجاد کرده‌ایم:

**مسیر**: `test/test-filter.html`

### نحوه استفاده:

1. باز کردن فایل در مرورگر
2. تست کردن فیلترها
3. مشاهده Console Output در پایین صفحه
4. بررسی که آیا مقالات فیلتر می‌شوند

---

## 🛠️ راه‌حل‌های متداول

### مشکل 1: فیلتر اعمال نمی‌شود

**علت**: دکمه "اعمال فیلتر" به تابع متصل نیست

**راه‌حل:**
```javascript
// در Console اجرا کنید:
window.applyFilters
// باید تابعی بازگردانده شود، نه undefined
```

اگر `undefined` بود:
1. فایل `filters.js` لود نشده
2. خطای JavaScript وجود دارد
3. بررسی Console برای خطا

---

### مشکل 2: همه مقالات مخفی می‌شوند

**علت**: فیلترها خیلی محدود هستند

**راه‌حل:**
1. روی "بازنشانی" کلیک کنید
2. بررسی کنید که همه checkboxها تیک خورده‌اند
3. Range slider را به 0-60 تنظیم کنید

---

### مشکل 3: Badge ها نمایش داده نمی‌شوند

**علت**: Front Matter در مقالات درست تنظیم نشده

**راه‌حل:**
بررسی Front Matter مقالات:

```toml
+++
readingTime = 14                    # باید عدد باشد
difficulty = "intermediate"         # باید یکی از: beginner, medium, intermediate, advanced
lab_required = true                 # باید true یا false باشد (بدون کوتیشن)
post_type_fa = "آموزشی"           # باید یکی از 7 مقدار معتبر باشد
+++
```

---

### مشکل 4: JavaScript در موبایل کار نمی‌کند

**علت**: احتمالاً مشکل Cache است

**راه‌حل:**
1. پاک کردن Cache مرورگر
2. رفرش سخت: `Ctrl + Shift + R` (موبایل: Settings → Clear Cache)
3. باز کردن در حالت Incognito/Private

---

## 📊 Check List نهایی

قبل از گزارش مشکل، این موارد را بررسی کنید:

- [ ] Console را باز کرده‌اید و خطا بررسی شده
- [ ] فایل `filters.js` لود شده (تب Network)
- [ ] مقالات در صفحه وجود دارند
- [ ] Badge ها در HTML صحیح هستند
- [ ] Data attributes به article-card اضافه شده‌اند
- [ ] دکمه "اعمال فیلتر" تابع `applyFilters()` را صدا می‌زند
- [ ] Cache مرورگر پاک شده
- [ ] Build جدید گرفته شده (`hugo --gc --minify`)

---

## 🆘 گزارش مشکل

اگر همه موارد بالا را بررسی کردید و مشکل همچنان وجود دارد:

### اطلاعات مورد نیاز:

1. **مرورگر و نسخه**: (مثلاً Chrome 120)
2. **سیستم‌عامل**: (مثلاً Windows 11)
3. **URL صفحه**: (مثلاً `/network/`)
4. **خطاهای Console**: (کپی کامل پیام‌های خطا)
5. **Screenshot**: (تصویر صفحه و Console)
6. **مراحل بازتولید مشکل**:
   - گام 1: ...
   - گام 2: ...
   - نتیجه: ...

---

## 🎯 نکات مهم

### 1. Cache مرورگر
همیشه بعد از تغییرات، Cache را پاک کنید:
- **Chrome/Edge**: `Ctrl + Shift + Del` → Clear Browsing Data
- **Firefox**: `Ctrl + Shift + Del` → Clear Recent History

### 2. Developer Mode
برای Debug بهتر، Developer Mode را فعال کنید:
```javascript
// در Console:
localStorage.setItem('filterDebug', 'true');
// سپس رفرش کنید
```

### 3. فایل تست
استفاده از `test/test-filter.html` برای تست سریع:
- مستقل از Hugo
- Console Output خودکار
- مقالات تست ساده

---

## 📞 منابع بیشتر

- [FILTER_SYSTEM_GUIDE.md](./FILTER_SYSTEM_GUIDE.md) - راهنمای کامل
- [CHANGELOG_FILTER_SYSTEM_2026-02-09.md](./CHANGELOG_FILTER_SYSTEM_2026-02-09.md) - تغییرات
- [MDN - Using Data Attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)
- [Chrome DevTools Guide](https://developer.chrome.com/docs/devtools/)

---

**تاریخ ایجاد**: 2026-02-09  
**آخرین به‌روزرسانی**: 2026-02-09  
**نسخه**: 1.0.0
