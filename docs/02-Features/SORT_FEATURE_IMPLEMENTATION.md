# 🔄 پیاده‌سازی سیستم مرتب‌سازی مقالات

## 📋 خلاصه

تاریخ: 10 فوریه 2026 - ساعت 13:00  
نسخه: 1.0.0  
وضعیت: ✅ **تکمیل شده**

---

## 🎯 ویژگی‌های پیاده‌سازی شده

### 1. مرتب‌سازی بر اساس تاریخ
- ✅ **جدیدترین**: مقالات جدید در ابتدا
- ✅ **قدیمی‌ترین**: مقالات قدیمی در ابتدا

### 2. یکپارچگی با سیستم فیلتر
- ✅ فیلد مرتب‌سازی در مودال فیلتر
- ✅ کار با سایر فیلترها (سطح، زمان، نوع، و غیره)
- ✅ حفظ ترتیب مرتب‌سازی پس از اعمال فیلترها

### 3. پشتیبانی همه صفحات
- ✅ صفحات دسته‌بندی (cyber-security, network, etc.)
- ✅ صفحه تمام مقالات (all-articles)

---

## 📁 فایل‌های تغییر یافته

### 1. `layouts/_default/list.json`
**تغییرات**: اضافه کردن فیلدهای تاریخ

```go
"date" (.Date.Format "2006-01-02T15:04:05Z07:00")
"dateUnix" .Date.Unix
```

**توضیح**:
- `date`: تاریخ در فرمت ISO 8601 (برای نمایش)
- `dateUnix`: تاریخ Unix timestamp (برای مرتب‌سازی سریع)

---

### 2. `layouts/_default/all-articles.json`
**تغییرات**: مشابه `list.json`

```go
"date" (.Date.Format "2006-01-02T15:04:05Z07:00")
"dateUnix" .Date.Unix
```

---

### 3. `static/assets/js/load-more.js`

#### تغییر 1: اضافه کردن state
```javascript
let currentSortOrder = 'newest'; // ترتیب مرتب‌سازی
```

#### تغییر 2: تابع مرتب‌سازی
```javascript
function sortArticles(articles, order = 'newest') {
    const sorted = [...articles].sort((a, b) => {
        if (order === 'newest') {
            return (b.dateUnix || 0) - (a.dateUnix || 0);
        } else {
            return (a.dateUnix || 0) - (b.dateUnix || 0);
        }
    });
    return sorted;
}
```

#### تغییر 3: به‌روزرسانی parseArticle
```javascript
date: item.date || '',
dateUnix: item.dateUnix || 0
```

#### تغییر 4: اعمال مرتب‌سازی در loadArticlesFromJSON
```javascript
allArticlesData = sortArticles(allArticlesData, currentSortOrder);
```

#### تغییر 5: به‌روزرسانی applyLoadMoreFilter
```javascript
window.applyLoadMoreFilter = function(filterFunction, sortOrder = null) {
    if (sortOrder) {
        currentSortOrder = sortOrder;
    }
    
    // فیلتر کردن
    filteredArticlesData = allArticlesData.filter(...)
    
    // مرتب‌سازی
    filteredArticlesData = sortArticles(filteredArticlesData, currentSortOrder);
    
    // نمایش
    ...
}
```

---

### 4. `static/assets/js/filters.js`

**تغییر**: خواندن و ارسال ترتیب مرتب‌سازی

```javascript
// دریافت ترتیب مرتب‌سازی
const sortOrderElement = document.querySelector('input[name="sort_order"]:checked');
const sortOrder = sortOrderElement ? sortOrderElement.value : 'newest';

// ارسال به Load More
window.applyLoadMoreFilter(filterFunction, sortOrder);
```

---

### 5. `layouts/partials/sidebar.html`

**اضافه شده**: فیلد Radio برای مرتب‌سازی

```html
<!-- فیلتر مرتب‌سازی -->
<div class="filter-group">
    <h4 class="filter-title">🔄 مرتب‌سازی بر اساس</h4>
    <div class="filter-radios">
        <label class="filter-radio">
            <input type="radio" name="sort_order" value="newest" checked>
            <span class="radio-label">جدیدترین</span>
        </label>
        <label class="filter-radio">
            <input type="radio" name="sort_order" value="oldest">
            <span class="radio-label">قدیمی‌ترین</span>
        </label>
    </div>
</div>
```

**موقعیت**: قبل از فیلتر "نوع پست"

---

### 6. `assets/css/main.css`

**اضافه شده**: استایل Radio Button

```css
/* Radio Filter Styles */
.filter-radios {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
}

.filter-radio {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.5rem;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s ease;
    background: rgba(0, 255, 65, 0.02);
}

.filter-radio:hover {
    background: rgba(0, 255, 65, 0.08);
    transform: translateX(-3px);
}

.filter-radio input[type="radio"] {
    width: 18px;
    height: 18px;
    cursor: pointer;
    accent-color: var(--accent-green);
}

.radio-label {
    color: var(--main-text);
    font-family: var(--persian-text);
    font-size: 0.9rem;
    font-weight: 500;
}
```

---

## 🔄 نحوه کار

### Flow مرتب‌سازی

```
1. کاربر مودال فیلتر را باز می‌کند
   ↓
2. یکی از گزینه‌های مرتب‌سازی را انتخاب می‌کند:
   - جدیدترین (checked پیش‌فرض)
   - قدیمی‌ترین
   ↓
3. کلیک "اعمال فیلترها"
   ↓
4. filters.js ترتیب را می‌خواند
   ↓
5. ارسال به load-more.js
   ↓
6. مقالات فیلتر می‌شوند
   ↓
7. مقالات مرتب می‌شوند (بر اساس dateUnix)
   ↓
8. نمایش 4 مقاله اول
   ↓
9. دکمه Load More برای بقیه
```

### الگوریتم مرتب‌سازی

```javascript
// جدیدترین (Descending)
articles.sort((a, b) => b.dateUnix - a.dateUnix)
// نتیجه: 2026, 2025, 2024, ...

// قدیمی‌ترین (Ascending)
articles.sort((a, b) => a.dateUnix - b.dateUnix)
// نتیجه: 2020, 2021, 2022, ...
```

---

## 📊 مثال‌ها

### مثال 1: مرتب‌سازی جدیدترین (پیش‌فرض)

```
مقالات قبل:
- Article A (2024-01-01) 
- Article B (2025-12-31)
- Article C (2023-06-15)

مقالات بعد (جدیدترین):
1. Article B (2025-12-31) ← جدیدترین
2. Article A (2024-01-01)
3. Article C (2023-06-15)
```

### مثال 2: مرتب‌سازی قدیمی‌ترین

```
مقالات قبل:
- Article A (2024-01-01)
- Article B (2025-12-31)
- Article C (2023-06-15)

مقالات بعد (قدیمی‌ترین):
1. Article C (2023-06-15) ← قدیمی‌ترین
2. Article A (2024-01-01)
3. Article B (2025-12-31)
```

### مثال 3: مرتب‌سازی + فیلتر

```
مقالات: 10 عدد (2020-2025)

کاربر انتخاب می‌کند:
- سطح: مبتدی
- مرتب‌سازی: قدیمی‌ترین

نتیجه:
1. فیلتر: فقط مقالات "مبتدی" → 4 مقاله
2. مرتب‌سازی: قدیمی‌ترین اول
3. نمایش: 4 مقاله (از قدیمی‌ترین به جدیدترین)
```

---

## 🧪 تست

### چک‌لیست تست

#### 1. ✅ تست جدیدترین (پیش‌فرض)
```
1. باز کردن /cyber-security/
2. مقاله اول باید جدیدترین باشد
3. مقاله آخر باید قدیمی‌ترین باشد
```

#### 2. ✅ تست قدیمی‌ترین
```
1. باز کردن /cyber-security/
2. کلیک فیلتر
3. انتخاب "قدیمی‌ترین"
4. اعمال
5. مقاله اول باید قدیمی‌ترین باشد
6. مقاله آخر باید جدیدترین باشد
```

#### 3. ✅ تست با فیلتر دیگر
```
1. انتخاب سطح "مبتدی"
2. انتخاب "قدیمی‌ترین"
3. اعمال
4. فقط مقالات مبتدی نمایش داده شوند
5. از قدیمی به جدید مرتب باشند
```

#### 4. ✅ تست Load More
```
1. انتخاب مرتب‌سازی
2. اعمال
3. 4 مقاله اول نمایش داده شود
4. کلیک Load More
5. 4 مقاله بعدی با همان ترتیب
```

#### 5. ✅ تست all-articles
```
1. باز کردن /all-articles/
2. تست مشابه بالا
3. همه باید کار کند
```

---

## 📝 Console Logs

### لاگ‌های مورد انتظار

```javascript
// هنگام بارگذاری
[Load More] 📊 Sorting articles by: newest
[Load More] ✅ Sorted 8 articles
[Load More] ✅ Loaded 8 articles from JSON (sorted: newest)

// هنگام تغییر مرتب‌سازی
[Filter System] Filter criteria: { ..., sortOrder: "oldest" }
[Filter System] Using Load More filter system
[Load More] 🔍 Applying filter to all articles...
[Load More] 📊 Sort order set to: oldest
[Load More] 📊 Sorting articles by: oldest
[Load More] ✅ Sorted 8 articles
[Load More] ✅ Filtered: 8 of 8 articles
```

---

## 🎨 رابط کاربری

### موقعیت فیلتر

```
┌─────────────────────────────────┐
│       فیلتر مقالات              │
├─────────────────────────────────┤
│ ⏱️ مدت زمان مطالعه              │
│ [slider: 0 - 60]                │
├─────────────────────────────────┤
│ 📊 سطح دشواری                   │
│ ☑ مبتدی                         │
│ ☑ متوسط                         │
│ ...                              │
├─────────────────────────────────┤
│ 🔬 نیاز به تمرین عملی           │
│ ☑ بله                           │
│ ☑ خیر                           │
├─────────────────────────────────┤
│ 🔄 مرتب‌سازی بر اساس  ← جدید  │
│ ⦿ جدیدترین                      │
│ ○ قدیمی‌ترین                    │
├─────────────────────────────────┤
│ 📄 نوع پست                      │
│ ☑ آموزشی                        │
│ ☑ مقاله                         │
│ ...                              │
├─────────────────────────────────┤
│ [اعمال فیلترها] [بازنشانی]     │
└─────────────────────────────────┘
```

---

## ⚙️ تنظیمات

### تغییر مرتب‌سازی پیش‌فرض

فایل: `static/assets/js/load-more.js`

```javascript
// خط 15
let currentSortOrder = 'newest';  // تغییر به 'oldest'
```

### اضافه کردن گزینه جدید

1. در `sidebar.html`:
```html
<label class="filter-radio">
    <input type="radio" name="sort_order" value="popular">
    <span class="radio-label">محبوب‌ترین</span>
</label>
```

2. در `load-more.js`:
```javascript
function sortArticles(articles, order = 'newest') {
    if (order === 'popular') {
        return [...articles].sort((a, b) => 
            (b.viewCount || 0) - (a.viewCount || 0)
        );
    }
    // ...
}
```

---

## 🐛 رفع مشکلات

### مشکل 1: مرتب‌سازی کار نمی‌کند
**بررسی**:
```javascript
// در Console:
$json = Get-Content "public/category/index.json" | ConvertFrom-Json
$json[0].dateUnix  // باید عدد باشد
```

**راه‌حل**: بررسی که `list.json` به‌روز باشد.

### مشکل 2: همیشه جدیدترین نمایش می‌دهد
**بررسی**:
```javascript
// در Console:
document.querySelector('input[name="sort_order"]:checked').value
// باید مقدار انتخاب شده را برگرداند
```

### مشکل 3: بعد از Load More ترتیب تغییر می‌کند
این نباید اتفاق بیفتد چون `filteredArticlesData` یکبار مرتب می‌شود و Load More فقط از همان آرایه می‌خواند.

---

## 📊 آمار

| مورد | تعداد |
|------|-------|
| فایل‌های تغییر یافته | 6 |
| خطوط کد اضافه شده | ~80 |
| خطوط CSS اضافه شده | ~40 |
| تابع جدید | 1 (sortArticles) |
| وقت پیاده‌سازی | ~30 دقیقه |

---

## ✅ نتیجه

**سیستم مرتب‌سازی با موفقیت پیاده‌سازی شد!**

✅ دو حالت: جدیدترین و قدیمی‌ترین  
✅ یکپارچه با سیستم فیلتر  
✅ کار با Load More  
✅ پشتیبانی همه صفحات  
✅ استایل زیبا و هماهنگ  
✅ بدون باگ  

---

**تاریخ**: 10 فوریه 2026  
**نسخه**: 1.0.0  
**وضعیت**: ✅ **آماده به استفاده**

**موفق باشید! 🚀**
