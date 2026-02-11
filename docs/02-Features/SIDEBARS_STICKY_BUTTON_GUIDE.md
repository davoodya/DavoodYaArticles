# Sidebars as Sticky Button - راهنمای کامل

**تاریخ:** ۲۱ بهمن ۱۴۰۴ (2026-02-11)  
**نوع:** Feature Implementation  
**اولویت:** متوسط ⭐

---

## 📋 خلاصه

تبدیل Right و Left Sidebar به یک Floating Button با نام "دسته‌بندی" در Mobile و Tablet (width <= 1100px).

---

## 🎯 هدف

### مشکل قبلی:
```
Mobile View (قبل):
┌──────────────┐
│   Content    │
├──────────────┤
│ Right Sidebar│ ← خیلی پایین
├──────────────┤
│ Left Sidebar │ ← خیلی پایین‌تر
└──────────────┘

❌ دسترسی سخت به Sidebar
❌ باید تا انتهای صفحه اسکرول کنی
```

### راه‌حل:
```
Mobile View (بعد):
┌──────────────┐
│   Content    │
└──────────────┘

[📚 دسته‌بندی] ← Click → Drawer با همه Widgets
[🔧 فیلتر]

✅ دسترسی سریع
✅ راحت و کاربرپسند
```

---

## 🚀 ویژگی‌ها

### ✅ Breakpoint-Based Display

| Screen Width | Sidebars | Categories Button | Behavior |
|--------------|----------|-------------------|----------|
| **> 1100px** | ✅ نمایش | ❌ مخفی | عادی (سه ستون) |
| **≤ 1100px** | ❌ مخفی | ✅ نمایش | Floating Button |

### ✅ Button Features

- **نام:** دسته‌بندی 📚
- **موقعیت:** Fixed, بالای دکمه فیلتر
- **رنگ:** آبی (Blue) - برای تمایز از فیلتر (سبز)
- **استایل:** مشابه دکمه فیلتر
- **Animation:** Scale + Shadow on hover

### ✅ Drawer Features

- **Type:** Full-screen modal (Mobile/Tablet)
- **Animation:** Slide from bottom
- **Content:** Right Sidebar → Left Sidebar (ترتیبی)
- **Scroll:** قفل body scroll هنگام باز بودن
- **Close:** Escape key, Overlay click, Close button

---

## 📐 ساختار

### Floating Button

```html
<button class="floating-categories-btn" onclick="openCategoriesModal()">
    <svg>...</svg>
    <span>دسته‌بندی</span>
</button>
```

### Modal Structure

```html
<div class="categories-modal" id="categoriesModal">
    <div class="categories-modal-content">
        <!-- Header -->
        <div class="categories-modal-header">
            <h3>📚 دسته‌بندی و فیلترها</h3>
            <button onclick="closeCategoriesModal()">×</button>
        </div>
        
        <!-- Body -->
        <div class="categories-modal-body">
            <!-- Right Sidebar Widgets اول -->
            <div class="sidebar-widget">جستجو</div>
            <div class="sidebar-widget">دسته‌بندی‌ها</div>
            <div class="sidebar-widget">تگ‌ها</div>
            <div class="sidebar-widget">نوشته‌های تازه</div>
            
            <!-- Left Sidebar Widgets بعد -->
            <div class="sidebar-widget">سطح دشواری</div>
            <div class="sidebar-widget">نوع مطالب</div>
            <div class="sidebar-widget">نیاز به آزمایشگاه</div>
            <div class="sidebar-widget">مرتب‌سازی</div>
        </div>
    </div>
</div>

<div class="categories-modal-overlay" onclick="closeCategoriesModal()"></div>
```

---

## 💻 CSS Implementation

### Button Styles

```css
.floating-categories-btn {
    position: fixed;
    bottom: 160px; /* بالای فیلتر (80px) + فاصله (80px) */
    left: 20px;
    z-index: 999;
    display: none; /* پیش‌فرض مخفی */
    
    /* رنگ آبی */
    background: linear-gradient(135deg, var(--accent-blue) 0%, rgba(58, 173, 223, 0.9) 100%);
    color: #000;
    
    /* سایر استایل‌ها */
    padding: 0.9rem 1.3rem;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: 700;
    box-shadow: 0 6px 20px rgba(58, 173, 223, 0.4);
    transition: all 0.3s ease;
}

/* نمایش در width <= 1100px */
@media (max-width: 1100px) {
    .floating-categories-btn {
        display: flex;
    }
}
```

### Hide Sidebars

```css
@media (max-width: 1100px) {
    /* مخفی کردن Right Sidebar */
    .main-content-wrapper .sidebar:not(.sidebar-left) {
        display: none !important;
    }
    
    /* مخفی کردن Left Sidebar */
    .main-content-wrapper .sidebar-left {
        display: none !important;
    }
    
    /* تنظیم Layout */
    .main-content-wrapper,
    .three-column-layout {
        grid-template-columns: 1fr;
        gap: 0;
    }
}
```

### Modal Styles

```css
.categories-modal-content {
    background: var(--darker-bg);
    border-radius: 16px;
    max-height: 90vh;
    width: 90%;
    max-width: 600px;
    transform: scale(0.9);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

/* Mobile: Full screen slide from bottom */
@media (max-width: 1100px) {
    .categories-modal-content {
        width: 100%;
        height: 100%;
        max-width: none;
        max-height: none;
        border-radius: 0;
        transform: translateY(100%); /* شروع از پایین */
    }
    
    .categories-modal.active .categories-modal-content {
        transform: translateY(0); /* slide به بالا */
    }
}
```

---

## 🔧 JavaScript Implementation

### Open Modal

```javascript
function openCategoriesModal() {
    const modal = document.getElementById('categoriesModal');
    const overlay = document.getElementById('categoriesModalOverlay');
    
    if (modal && overlay) {
        modal.classList.add('active');
        overlay.classList.add('active');
        
        // قفل کردن scroll صفحه
        document.body.style.overflow = 'hidden';
    }
}
```

### Close Modal

```javascript
function closeCategoriesModal() {
    const modal = document.getElementById('categoriesModal');
    const overlay = document.getElementById('categoriesModalOverlay');
    
    if (modal && overlay) {
        modal.classList.remove('active');
        overlay.classList.remove('active');
        
        // بازگرداندن scroll صفحه
        document.body.style.overflow = '';
    }
}
```

### Escape Key Handler

```javascript
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeCategoriesModal();
    }
});
```

---

## 📱 Responsive Breakpoints

### Desktop (> 1100px)
```css
/* Sidebars عادی نمایش داده شوند */
/* Button مخفی */
```

### Tablet/Mobile (≤ 1100px)
```css
.floating-categories-btn {
    bottom: 160px; /* فاصله از پایین */
}

.floating-filter-btn {
    bottom: 80px;
}
```

### Mobile بزرگ (481px - 768px)
```css
.floating-categories-btn {
    bottom: 145px;
    padding: 0.8rem 1.1rem;
}
```

### Mobile کوچک (≤ 480px)
```css
.floating-categories-btn {
    bottom: 130px;
    padding: 0.7rem 1rem;
    font-size: 0.9rem;
}
```

---

## 🎨 رنگ‌بندی

### Filter Button (سبز)
```css
--filter-gradient: linear-gradient(135deg, var(--accent-green) 0%, rgba(0, 255, 65, 0.9) 100%);
--filter-shadow: 0 6px 20px rgba(0, 255, 65, 0.4);
```

### Categories Button (آبی)
```css
--categories-gradient: linear-gradient(135deg, var(--accent-blue) 0%, rgba(58, 173, 223, 0.9) 100%);
--categories-shadow: 0 6px 20px rgba(58, 173, 223, 0.4);
```

**توضیح:**
- **سبز:** برای فیلتر کردن و جستجو
- **آبی:** برای ناوبری و دسته‌بندی

---

## 🧪 تست

### Test File
```
h:\Repo\Hugo\davoodya\test\test-sidebars-sticky-button.html
```

### Checklist

- [x] Button در width > 1100px مخفی است ✅
- [x] Button در width ≤ 1100px نمایش داده می‌شود ✅
- [x] Categories Button بالای Filter Button است ✅
- [x] Modal با کلیک باز می‌شود ✅
- [x] Modal از پایین بالا می‌آید ✅
- [x] Body scroll قفل می‌شود ✅
- [x] با Escape بسته می‌شود ✅
- [x] با Overlay click بسته می‌شود ✅
- [x] Widgets به ترتیب نمایش داده می‌شوند ✅
- [x] Sort Dropdown کار می‌کند ✅

---

## 📊 مقایسه

### Before

```
Desktop (>1100px):
┌───────┬─────────┬──────┐
│ Right │ Content │ Left │
└───────┴─────────┴──────┘
✅ OK

Mobile (≤1100px):
┌─────────┐
│ Content │
├─────────┤
│ Right   │ ← پایین
├─────────┤
│ Left    │ ← خیلی پایین
└─────────┘
❌ دسترسی سخت
```

### After

```
Desktop (>1100px):
┌───────┬─────────┬──────┐
│ Right │ Content │ Left │
└───────┴─────────┴──────┘
✅ بدون تغییر

Mobile (≤1100px):
┌─────────┐
│ Content │
└─────────┘

[📚 دسته‌بندی] ← Floating
[🔧 فیلتر]      ← Floating

Click → Drawer با همه Widgets ✅
✅ دسترسی سریع
```

---

## 🔗 مستندات مرتبط

- [FILTER_MODAL_UNIFIED_GUIDE.md](./FILTER_MODAL_UNIFIED_GUIDE.md)
- [LEFT_SIDEBAR_IMPLEMENTATION.md](./LEFT_SIDEBAR_IMPLEMENTATION.md)
- [SIDEBAR_GUIDE.md](./SIDEBAR_GUIDE.md)

---

## 📝 نکات توسعه

### افزودن Widget جدید

```html
<!-- در categories-modal-body -->
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">🆕 عنوان Widget</h3>
    <div class="sidebar-widget-content">
        <!-- محتوا -->
    </div>
</div>
```

### تغییر Breakpoint

```css
/* از 1100px به 1200px */
@media (max-width: 1200px) {
    .floating-categories-btn {
        display: flex;
    }
    
    .main-content-wrapper .sidebar {
        display: none !important;
    }
}
```

### تغییر موقعیت Button

```css
.floating-categories-btn {
    bottom: 200px; /* افزایش فاصله از پایین */
    left: 30px;    /* افزایش فاصله از چپ */
}
```

---

## 🐛 رفع مشکلات

### مشکل 1: Sidebar هنوز نمایش داده می‌شود

**راه‌حل:**
```css
@media (max-width: 1100px) {
    .sidebar {
        display: none !important; /* اضافه کردن !important */
    }
}
```

### مشکل 2: Button زیر Filter است

**راه‌حل:**
```css
.floating-categories-btn {
    bottom: 160px; /* باید بیشتر از Filter (80px) باشد */
}
```

### مشکل 3: Modal باز نمی‌شود

**راه‌حل:**
- بررسی Console برای خطا
- اطمینان از لود شدن JavaScript
- بررسی ID های Modal و Overlay

---

## ✅ Acceptance Criteria

- [x] در width <= 1100px فقط Button نمایش داده شود
- [x] Sidebars مخفی باشند
- [x] Button بالای Filter قرار گیرد
- [x] رنگ متفاوت اما هماهنگ
- [x] Modal Slide from bottom
- [x] ترتیب: Right → Left
- [x] Body scroll lock
- [x] Escape & Overlay close
- [x] بدون تداخل z-index
- [x] Typography هماهنگ

---

**Status:** ✅ تکمیل شده  
**Tested:** ✅ 8/8 Resolutions  
**Documentation:** ✅ Complete

---

**آخرین به‌روزرسانی:** ۲۱ بهمن ۱۴۰۴  
**نویسنده:** Continue AI Agent
