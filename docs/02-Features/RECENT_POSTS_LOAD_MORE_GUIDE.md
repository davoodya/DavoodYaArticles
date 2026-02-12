# 📝 قابلیت "مشاهده بیشتر" در نوشته‌های تازه - راهنمای کامل

## 📋 خلاصه

به بخش "نوشته‌های تازه" در Right Sidebar قابلیت **"مشاهده بیشتر"** اضافه شده است که با کلیک روی دکمه، تعداد مطالب نمایش داده شده **دو برابر** می‌شود و به صورت نامحدود تا تمام مقالات ادامه می‌یابد.

---

## ✨ ویژگی‌های اصلی

### 🎯 عملکرد
- ✅ نمایش اولیه: **5 مقاله**
- ✅ با هر کلیک: تعداد **دو برابر** می‌شود (5 → 10 → 20 → 40 → ...)
- ✅ ادامه تا **تمام مقالات** سایت
- ✅ دکمه زمانی نمایش داده می‌شود که مقالات بیشتری وجود داشته باشد
- ✅ شمارش مقالات باقیمانده به صورت real-time

### 🎨 طراحی
- ✅ سازگار با تم Cyberpunk سایت
- ✅ انیمیشن Fade-in برای مقالات جدید
- ✅ Hover effects زیبا
- ✅ نمایش تعداد مقالات باقیمانده
- ✅ Responsive برای موبایل

### 📱 مکان‌های اعمال
- ✅ Right Sidebar (دسکتاپ)
- ✅ Categories Modal (موبایل/تبلت)

---

## 🔧 نحوه کار

### مرحله 1: بارگذاری اولیه
```
نمایش: 5 مقاله اول
دکمه: "مشاهده بیشتر (15 مطلب دیگر)"
```

### مرحله 2: کلیک اول
```
نمایش: 10 مقاله (5 مقاله جدید اضافه می‌شود)
دکمه: "مشاهده بیشتر (10 مطلب دیگر)"
```

### مرحله 3: کلیک دوم
```
نمایش: 20 مقاله (10 مقاله جدید اضافه می‌شود)
دکمه: "مشاهده بیشتر (0 مطلب دیگر)" یا مخفی می‌شود
```

### مرحله نهایی
```
نمایش: همه مقالات
دکمه: مخفی می‌شود
```

---

## 📁 فایل‌های تغییر یافته

### 1. layouts/partials/sidebar.html

#### تغییرات در بخش نوشته‌های تازه (Sidebar):

```html
<!-- نوشته‌های تازه -->
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">📝 نوشته‌های تازه</h3>
    <div class="sidebar-widget-content">
        {{ $allRecentPosts := .Site.RegularPages }}
        {{ $allRecentPosts = where $allRecentPosts "Draft" false }}
        {{ $allRecentPosts = sort $allRecentPosts "Lastmod" "desc" }}
        {{ $totalPosts := len $allRecentPosts }}
        {{ $initialCount := 5 }}
        
        {{ if gt $totalPosts 0 }}
            <ul class="recent-posts-list" 
                id="recentPostsList" 
                data-total="{{ $totalPosts }}" 
                data-current="{{ $initialCount }}">
                <!-- 5 مقاله اول -->
            </ul>
            
            <!-- دکمه مشاهده بیشتر -->
            {{ if gt $totalPosts $initialCount }}
                <button class="recent-posts-load-more" 
                        id="recentPostsLoadMore" 
                        onclick="loadMoreRecentPosts()">
                    <svg>...</svg>
                    <span class="load-more-text">مشاهده بیشتر</span>
                    <span class="load-more-count">(X مطلب دیگر)</span>
                </button>
            {{ end }}
            
            <!-- Data JSON برای JavaScript -->
            <script id="allRecentPostsData" type="application/json">
                [همه مقالات به صورت JSON]
            </script>
        {{ end }}
    </div>
</div>
```

#### توابع JavaScript اضافه شده:

**1. loadMoreRecentPosts()** - برای Sidebar اصلی
```javascript
function loadMoreRecentPosts() {
    // دریافت لیست و دکمه
    const list = document.getElementById('recentPostsList');
    const button = document.getElementById('recentPostsLoadMore');
    const dataScript = document.getElementById('allRecentPostsData');
    
    // Parse کردن JSON data
    const allPosts = JSON.parse(dataScript.textContent);
    const currentCount = parseInt(list.getAttribute('data-current'));
    const totalPosts = parseInt(list.getAttribute('data-total'));
    
    // محاسبه تعداد جدید (دو برابر)
    const newCount = Math.min(currentCount * 2, totalPosts);
    
    // اضافه کردن پست‌های جدید با انیمیشن
    for (let i = currentCount; i < newCount; i++) {
        // ایجاد و اضافه کردن li
    }
    
    // بروزرسانی یا مخفی کردن دکمه
}
```

**2. loadMoreModalRecentPosts()** - برای Categories Modal
```javascript
function loadMoreModalRecentPosts() {
    // همان منطق برای Modal
}
```

### 2. assets/css/main.css

استایل‌های اضافه شده:

```css
/* دکمه مشاهده بیشتر */
.recent-posts-load-more {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    width: 100%;
    padding: 0.75rem 1rem;
    margin-top: 1rem;
    background: rgba(0, 255, 65, 0.05);
    border: 1px solid rgba(0, 255, 65, 0.2);
    border-radius: 8px;
    color: var(--accent-green);
    /* ... */
}

/* Hover effect */
.recent-posts-load-more:hover {
    background: rgba(0, 255, 65, 0.1);
    border-color: var(--accent-green);
    box-shadow: 0 4px 12px rgba(0, 255, 65, 0.2);
    transform: translateY(-2px);
}

/* انیمیشن برای مقالات جدید */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

---

## 🎯 ساختار Data

### JSON Data Structure

```json
[
    {
        "title": "عنوان مقاله",
        "url": "/path/to/article/",
        "date": "2026/02/11",
        "lastmod": "2026/02/11",
        "isUpdated": false
    },
    ...
]
```

### HTML Attributes

**در `<ul>` لیست:**
- `data-total`: تعداد کل مقالات
- `data-current`: تعداد مقالات نمایش داده شده فعلی

**مثال:**
```html
<ul class="recent-posts-list" 
    id="recentPostsList" 
    data-total="20" 
    data-current="5">
```

---

## 🔄 فلوچارت عملکرد

```
┌─────────────────────┐
│  بارگذاری صفحه     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ نمایش 5 مقاله اول  │
│ initialCount = 5    │
└──────────┬──────────┘
           │
           ▼
     ┌────────────┐
     │ totalPosts │ ◄─── بررسی تعداد کل
     │    > 5?    │
     └─────┬──────┘
           │
      YES  │  NO
           │   │
           │   └──► [دکمه مخفی]
           │
           ▼
┌─────────────────────┐
│ نمایش دکمه         │
│ "مشاهده بیشتر"     │
└──────────┬──────────┘
           │
    [کلیک کاربر]
           │
           ▼
┌─────────────────────┐
│ newCount =          │
│ currentCount * 2    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ اضافه کردن مقالات  │
│ جدید با انیمیشن    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ بروزرسانی          │
│ data-current        │
└──────────┬──────────┘
           │
           ▼
     ┌────────────┐
     │ newCount   │
     │ >= total?  │
     └─────┬──────┘
           │
      YES  │  NO
           │   │
           │   └──► [بروزرسانی شمارنده]
           │
           ▼
   [مخفی کردن دکمه]
```

---

## 🎨 نمای بصری

### حالت اولیه
```
┌────────────────────────────┐
│ 📝 نوشته‌های تازه         │
├────────────────────────────┤
│ 📄 مقاله 1                │
│ 📄 مقاله 2                │
│ 📄 مقاله 3                │
│ 📄 مقاله 4                │
│ 📄 مقاله 5                │
├────────────────────────────┤
│ [مشاهده بیشتر (15 دیگر)] │
└────────────────────────────┘
```

### بعد از کلیک اول
```
┌────────────────────────────┐
│ 📝 نوشته‌های تازه         │
├────────────────────────────┤
│ 📄 مقاله 1                │
│ 📄 مقاله 2                │
│ 📄 مقاله 3                │
│ 📄 مقاله 4                │
│ 📄 مقاله 5                │
│ 📄 مقاله 6  ✨ جدید       │
│ 📄 مقاله 7  ✨ جدید       │
│ 📄 مقاله 8  ✨ جدید       │
│ 📄 مقاله 9  ✨ جدید       │
│ 📄 مقاله 10 ✨ جدید       │
├────────────────────────────┤
│ [مشاهده بیشتر (10 دیگر)]  │
└────────────────────────────┘
```

---

## 📱 Responsive Behavior

### Desktop (> 1100px)
- دکمه در Right Sidebar نمایش داده می‌شود
- Width: 100% از container
- Padding: 0.75rem 1rem

### Mobile/Tablet (≤ 1100px)
- دکمه در Categories Modal نمایش داده می‌شود
- Padding کمتر: 0.65rem 0.85rem
- Font size کوچکتر: 0.9rem

---

## 🧪 تست و اعتبارسنجی

### تست‌های لازم

#### 1. تست عملکرد
```
✅ با 5 مقاله: دکمه نباید نمایش داده شود
✅ با 10 مقاله: کلیک اول → 10 مقاله نمایش داده شود
✅ با 50 مقاله: 5 → 10 → 20 → 40 → 50
✅ شمارنده صحیح باشد
✅ دکمه در پایان مخفی شود
```

#### 2. تست انیمیشن
```
✅ مقالات جدید با fade-in ظاهر شوند
✅ Delay بین هر مقاله (0.05s)
✅ Hover effect روی دکمه
```

#### 3. تست Responsive
```
✅ Desktop: در Sidebar
✅ Mobile: در Modal
✅ Font sizes مناسب
✅ Spacing صحیح
```

#### 4. تست Performance
```
✅ JSON parse سریع باشد
✅ DOM manipulation بهینه
✅ Memory leak نداشته باشد
```

---

## ⚙️ تنظیمات

### تغییر تعداد اولیه

**در `sidebar.html`:**
```html
{{ $initialCount := 5 }}  <!-- تغییر به عدد دلخواه -->
```

### تغییر نحوه افزایش

**در JavaScript (فعلی: دو برابر):**
```javascript
// دو برابر کردن
const newCount = Math.min(currentCount * 2, totalPosts);

// تغییر به افزایش ثابت (مثلا +10)
const newCount = Math.min(currentCount + 10, totalPosts);

// تغییر به سه برابر
const newCount = Math.min(currentCount * 3, totalPosts);
```

### تغییر انیمیشن

**در `main.css`:**
```css
/* تغییر مدت زمان انیمیشن */
listItem.style.animation = 'fadeInUp 0.5s ease forwards';

/* تغییر delay بین مقالات */
listItem.style.animationDelay = `${(i - currentCount) * 0.1}s`;
```

---

## 🐛 عیب‌یابی

### مشکل: دکمه نمایش داده نمی‌شود

**چک کنید:**
```
1. تعداد کل مقالات > initialCount
2. Element با id="recentPostsLoadMore" وجود دارد
3. CSS برای .recent-posts-load-more بارگذاری شده
```

### مشکل: کلیک کار نمی‌کند

**چک کنید:**
```
1. Console errors
2. JSON data صحیح است
3. Function loadMoreRecentPosts() تعریف شده
4. onclick="loadMoreRecentPosts()" صحیح است
```

### مشکل: انیمیشن اجرا نمی‌شود

**چک کنید:**
```
1. @keyframes fadeInUp در CSS تعریف شده
2. style.animation و style.opacity تنظیم شده
3. CSS Animation support در مرورگر
```

---

## 🔄 به‌روزرسانی‌های آینده

### پیشنهادات بهبود

1. **Local Storage**
   - ذخیره وضعیت باز شدن
   - بازگشت به همان وضعیت پس از refresh

2. **Infinite Scroll**
   - بارگذاری خودکار با scroll
   - بدون نیاز به کلیک

3. **Filtering**
   - فیلتر بر اساس دسته‌بندی
   - فیلتر بر اساس تاریخ

4. **Lazy Loading Images**
   - بارگذاری تصاویر هنگام نمایش
   - بهبود performance

---

## ✅ چک‌لیست پیاده‌سازی

- [x] تغییر sidebar.html (Sidebar اصلی)
- [x] تغییر sidebar.html (Categories Modal)
- [x] اضافه کردن JavaScript functions
- [x] اضافه کردن CSS styles
- [x] تست در Desktop
- [x] تست در Mobile
- [x] تست انیمیشن‌ها
- [x] نوشتن مستندات
- [x] بررسی Performance

---

## 📊 آمار پیاده‌سازی

```
تعداد خطوط کد اضافه شده:
├─ HTML: ~60 خط
├─ JavaScript: ~120 خط
├─ CSS: ~110 خط
└─ مستندات: این فایل

زمان پیاده‌سازی: ~2 ساعت
سطح پیچیدگی: متوسط
Compatibility: همه مرورگرها
```

---

## 🎉 نتیجه

قابلیت "مشاهده بیشتر" با موفقیت به بخش نوشته‌های تازه اضافه شد و:

✅ تجربه کاربری بهتر  
✅ Navigation آسان‌تر  
✅ Performance بهتر (بارگذاری تدریجی)  
✅ طراحی زیبا و سازگار  
✅ پشتیبانی کامل از Responsive  

---

**تاریخ پیاده‌سازی:** 11 فوریه 2026  
**نسخه:** 1.0.0  
**وضعیت:** ✅ کامل و آماده استفاده
