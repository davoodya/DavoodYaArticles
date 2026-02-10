# راهنمای سیستم فیلتر یکپارچه - Unified Filter Modal

## 📋 خلاصه تغییرات

### تاریخ: 2026-02-10
### نسخه: 3.0 - Unified Modal System

---

## 🎯 هدف

تبدیل سیستم فیلتر از حالت دوگانه (Desktop Sidebar + Mobile Modal) به **یک سیستم یکپارچه** که در تمام حالت‌های Desktop, Tablet و Mobile از **دکمه شناور** و **مودال باز شونده** استفاده می‌کند.

---

## 🔄 تغییرات اصلی

### قبل از تغییرات:
```
Desktop  → Sidebar (فیلترها در سایدبار)
Tablet   → Mobile Modal (دکمه شناور + مودال)
Mobile   → Mobile Modal (دکمه شناور + مودال)
```

### بعد از تغییرات:
```
Desktop  → Unified Modal (دکمه شناور + مودال)
Tablet   → Unified Modal (دکمه شناور + مودال)
Mobile   → Unified Modal (دکمه شناور + مودال)
```

---

## 📁 فایل‌های تغییر یافته

### 1. `layouts/partials/sidebar.html`

#### ✂️ حذف شده:
- بخش "فیلتر بر اساس ویژگی" از Sidebar
- فیلترهای Desktop در Sidebar
- دکمه‌های `applyFilters()` و `resetFilters()` از Sidebar

#### ➕ اضافه شده:
- **دکمه شناور یکپارچه** (برای همه دستگاه‌ها)
- **مودال یکپارچه** (جایگزین mobile-filter-modal)
- استفاده از یک نام واحد برای input‌ها

#### کد جدید:
```html
<!-- Floating Filter Button (All Devices) -->
<button class="floating-filter-btn" onclick="openFilterModal()" aria-label="فیلترها">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z"/>
    </svg>
    <span>فیلتر</span>
</button>

<!-- Universal Filter Modal -->
<div class="filter-modal" id="filterModal">
    <div class="filter-modal-content">
        <!-- محتوای مودال -->
    </div>
</div>

<div class="filter-modal-overlay" id="filterModalOverlay"></div>
```

---

### 2. `static/assets/js/filters.js`

#### 🔄 تغییرات:

**حذف توابع Mobile جداگانه:**
```javascript
// ❌ حذف شد
window.applyMobileFilters = function() { ... }
window.resetMobileFilters = function() { ... }
window.openMobileFilters = function() { ... }
window.closeMobileFilters = function() { ... }
```

**اضافه توابع یکپارچه:**
```javascript
// ✅ اضافه شد
window.openFilterModal = function() {
    const modal = document.getElementById('filterModal');
    const overlay = document.getElementById('filterModalOverlay');
    
    if (modal && overlay) {
        modal.classList.add('active');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
        updateFilterResults();
    }
}

window.closeFilterModal = function() {
    const modal = document.getElementById('filterModal');
    const overlay = document.getElementById('filterModalOverlay');
    
    if (modal && overlay) {
        modal.classList.remove('active');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }
}
```

**اصلاح تابع applyFilters:**
```javascript
window.applyFilters = function() {
    // ... منطق فیلتر
    filterArticles(minTime, maxTime, selectedDifficulties, selectedLabRequired, selectedPostTypes);
    closeFilterModal(); // ✅ بستن مودال بعد از اعمال فیلتر
};
```

**حذف Setup دوگانه Range Sliders:**
```javascript
// قبل:
function setupRangeSliders() {
    setupSliderPair('readingTimeMinRange', ...);     // Desktop
    setupSliderPair('mobileReadingTimeMinRange', ...); // Mobile
}

// بعد:
function setupRangeSliders() {
    setupSliderPair('readingTimeMinRange', ...); // یکپارچه
}
```

---

### 3. `assets/css/main.css`

#### 🎨 تغییرات CSS:

**حذف کلاس‌های Mobile:**
```css
/* ❌ حذف شد */
.mobile-filter-modal { }
.mobile-filter-content { }
.mobile-filter-header { }
.mobile-filter-body { }
.mobile-filter-footer { }
.mobile-filter-close { }
.mobile-filter-overlay { }
```

**اضافه کلاس‌های یکپارچه:**
```css
/* ✅ اضافه شد */
.filter-modal { }
.filter-modal-content { }
.filter-modal-header { }
.filter-modal-body { }
.filter-modal-footer { }
.filter-modal-close { }
.filter-modal-overlay { }
```

**نمایش دائمی دکمه شناور:**
```css
/* قبل */
@media (max-width: 1024px) {
    .floating-filter-btn {
        display: flex;
    }
}

/* بعد */
.floating-filter-btn {
    display: flex; /* همیشه نمایش داده شود */
}
```

**Responsive Design مودال:**
```css
/* Desktop: مودال مرکزی */
@media (min-width: 769px) {
    .filter-modal-content {
        width: 90%;
        max-width: 600px;
        max-height: 90vh;
        border-radius: 16px;
        transform: scale(0.9);
    }
    
    .filter-modal.active .filter-modal-content {
        transform: scale(1);
    }
}

/* Mobile/Tablet: تمام صفحه */
@media (max-width: 768px) {
    .filter-modal-content {
        width: 100%;
        height: 100%;
        border-radius: 0;
        transform: translateY(100%);
    }
    
    .filter-modal.active .filter-modal-content {
        transform: translateY(0);
    }
}
```

---

## 🎨 ویژگی‌های طراحی

### Desktop (≥769px):
- ✅ مودال مرکزی با عرض 600px
- ✅ گوشه‌های گرد (16px)
- ✅ انیمیشن Scale (کوچک به بزرگ)
- ✅ Backdrop Blur
- ✅ دکمه بستن با انیمیشن چرخش

### Tablet/Mobile (<768px):
- ✅ مودال تمام صفحه
- ✅ بدون گوشه گرد
- ✅ انیمیشن Slide Up (از پایین به بالا)
- ✅ Overlay تیره‌تر

---

## 🎯 مزایای سیستم جدید

### 1. **یکپارچگی UI/UX**
- تجربه کاربری یکسان در همه دستگاه‌ها
- کاربران Desktop هم از مودال استفاده می‌کنند
- کد ساده‌تر و قابل نگهداری بهتر

### 2. **بهبود فضای Sidebar**
- Sidebar فقط شامل: جستجو، دسته‌بندی‌ها، تگ‌ها، نوشته‌های تازه
- فضای بیشتر برای محتوای اصلی
- تمرکز بهتر روی مقالات

### 3. **کد تمیزتر**
```javascript
// قبل: 2 سیستم جداگانه
applyFilters()        // Desktop
applyMobileFilters()  // Mobile

// بعد: 1 سیستم یکپارچه
applyFilters()        // همه دستگاه‌ها
```

### 4. **نگهداری آسان‌تر**
- یک مودال برای همه
- یک مجموعه input برای همه
- یک مجموعه تابع برای همه

---

## 🧪 تست سیستم

### تست Desktop (≥769px):
```
1. باز کردن صفحه: http://localhost:1313/network/
2. کلیک روی دکمه شناور "فیلتر" (پایین سمت راست)
3. مودال مرکزی باز می‌شود
4. تغییر فیلترها
5. کلیک "اعمال فیلتر" → مودال بسته + فیلتر اعمال می‌شود
6. مجدداً باز کردن → تنظیمات قبلی حفظ شده
7. کلیک روی × یا Overlay → مودال بسته می‌شود
8. کلیک ESC → مودال بسته می‌شود
```

### تست Tablet (481px-768px):
```
همان تست Desktop اما:
- مودال تمام صفحه باز می‌شود
- انیمیشن از پایین به بالا
```

### تست Mobile (≤480px):
```
همان تست Tablet
```

---

## 📊 مقایسه قبل و بعد

| ویژگی | قبل | بعد |
|-------|-----|-----|
| Desktop Filter | Sidebar | Modal |
| Mobile Filter | Modal | Modal |
| تعداد کد JavaScript | 2 سیستم | 1 سیستم |
| تعداد Input Names | 2 مجموعه | 1 مجموعه |
| تعداد Range Sliders | 4 slider | 2 slider |
| نگهداری کد | سخت | آسان |
| یکپارچگی UI | کم | زیاد |

---

## 🔧 نکات فنی

### 1. **Event Listeners**
```javascript
// بستن با ESC در همه دستگاه‌ها
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const modal = document.getElementById('filterModal');
        if (modal && modal.classList.contains('active')) {
            closeFilterModal();
        }
    }
});
```

### 2. **Prevent Body Scroll**
```javascript
// باز کردن مودال
document.body.style.overflow = 'hidden';

// بستن مودال
document.body.style.overflow = '';
```

### 3. **CSS Animations**
```css
/* Desktop: Scale Animation */
.filter-modal-content {
    transform: scale(0.9);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.filter-modal.active .filter-modal-content {
    transform: scale(1);
}

/* Mobile: Slide Up Animation */
@media (max-width: 768px) {
    .filter-modal-content {
        transform: translateY(100%);
    }
    
    .filter-modal.active .filter-modal-content {
        transform: translateY(0);
    }
}
```

---

## 🚀 استقرار

### Build Production:
```bash
cd h:\Repo\Hugo\davoodya
hugo --cleanDestinationDir --minify
```

### Run Development:
```bash
hugo server -D
```

### تست سریع:
```
http://localhost:1313/network/
http://localhost:1313/cyber-security/
http://localhost:1313/all-articles/
```

---

## 📚 فایل‌های مرتبط

```
layouts/partials/sidebar.html          ← UI مودال
static/assets/js/filters.js            ← منطق JavaScript
assets/css/main.css                    ← استایل‌ها
public/assets/js/filters.js            ← فایل compiled
```

---

## ✅ Checklist نهایی

- [x] حذف فیلترها از Sidebar
- [x] ایجاد مودال یکپارچه
- [x] حذف توابع Mobile جداگانه
- [x] یکپارچه‌سازی JavaScript
- [x] یکپارچه‌سازی CSS
- [x] تست Desktop
- [x] تست Tablet
- [x] تست Mobile
- [x] بررسی Responsive
- [x] بررسی Animations
- [x] تست ESC key
- [x] تست Overlay click
- [x] مستندسازی

---

## 🎉 نتیجه

سیستم فیلتر اکنون:
- ✅ یکپارچه در همه دستگاه‌ها
- ✅ دکمه شناور در همه حالت‌ها
- ✅ مودال باز شونده در همه حالت‌ها
- ✅ کد تمیزتر و قابل نگهداری
- ✅ تجربه کاربری بهتر
- ✅ انیمیشن‌های حرفه‌ای
- ✅ Responsive Design کامل

---

**تاریخ**: 2026-02-10  
**نسخه**: 3.0  
**وضعیت**: ✅ Production Ready
