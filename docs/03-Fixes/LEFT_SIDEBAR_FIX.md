# Left Sidebar Bug Fixes

**تاریخ:** 2026-02-11  
**وضعیت:** ✅ تکمیل شده

---

## 🐛 باگ‌های گزارش شده

### Bug #1: ترتیب اشتباه Sidebars

**مشکل:**
- Right Sidebar در زیر Left Sidebar قرار گرفته بود
- ترتیب صحیح در RTL layout رعایت نشده بود

**علت:**
- Grid columns در CSS به اشتباه تنظیم شده بود
- Order و grid-column assignment نادرست بود

**راه‌حل:**
```css
/* قبل (اشتباه) */
.three-column-layout {
    grid-template-columns: 280px 1fr 350px;
}
.sidebar-left { grid-column: 1; }
.main-content { grid-column: 2; }
.sidebar { grid-column: 3; }

/* بعد (درست) */
.three-column-layout {
    grid-template-columns: 350px 1fr 280px;
    direction: rtl;
}
.sidebar { grid-column: 1; }        /* Right Sidebar سمت راست */
.main-content { grid-column: 2; }   /* Content وسط */
.sidebar-left { grid-column: 3; }   /* Left Sidebar سمت چپ */
```

---

### Bug #2: Widget مرتب‌سازی در جای اشتباه

**مشکل:**
- Widget "مرتب‌سازی بر اساس" در Right Sidebar باقی مانده بود
- قرار بود به Left Sidebar منتقل شود

**راه‌حل:**

**1. حذف از Right Sidebar:**
- فایل: `layouts/partials/sidebar.html`
- Widget مرتب‌سازی حذف شد

**2. اضافه کردن به Left Sidebar:**
- فایل: `layouts/partials/sidebar-left.html`
- Widget مرتب‌سازی به عنوان آخرین Widget اضافه شد

---

## 📐 Layout نهایی (RTL)

### Desktop (> 1024px)

```
┌────────────────────────────────────────────────────────┐
│                       Header                           │
├──────────────────┬──────────────────┬──────────────────┤
│                  │                  │                  │
│  Right Sidebar   │   Main Content   │  Left Sidebar    │
│  (350px)         │   (Flexible)     │  (280px)         │
│                  │                  │                  │
│  🔍 جستجو        │  📰 مقالات       │  📊 سطح دشواری   │
│  📚 دسته‌بندی‌ها  │  📝 محتوا        │  📄 نوع مطالب    │
│  🏷️ تگ‌ها        │                  │  🔬 آزمایشگاه     │
│  📝 نوشته‌های تازه│                  │  🔄 مرتب‌سازی     │
│                  │                  │                  │
└──────────────────┴──────────────────┴──────────────────┘
```

**CSS:**
```css
.three-column-layout {
    display: grid;
    grid-template-columns: 350px 1fr 280px;
    gap: 2rem;
    direction: rtl;
}

.three-column-layout .sidebar {
    grid-column: 1;  /* سمت راست */
}

.three-column-layout .main-content {
    grid-column: 2;  /* وسط */
    direction: rtl;
}

.three-column-layout .sidebar-left {
    grid-column: 3;  /* سمت چپ */
}
```

---

## 🔧 تغییرات اعمال شده

### 1. فایل CSS

**فایل:** `assets/css/main.css`

**تغییرات:**
```css
/* Three Column Layout - فقط برای صفحات مشخص شده */
.three-column-layout {
    display: grid;
    grid-template-columns: 350px 1fr 280px;  /* تغییر از 280px 1fr 350px */
    gap: 2rem;
    align-items: start;
    margin-top: 80px;
    overflow-x: hidden;
    overflow-y: hidden;
    direction: rtl;  /* اضافه شده */
}

/* در RTL: Right Sidebar سمت راست, Content وسط, Left Sidebar سمت چپ */
.three-column-layout .sidebar {
    grid-column: 1;  /* تغییر از 3 به 1 */
    order: 1;
}

.three-column-layout .main-content {
    grid-column: 2;
    order: 2;
    direction: rtl;  /* اضافه شده */
}

.three-column-layout .sidebar-left {
    grid-column: 3;  /* تغییر از 1 به 3 */
    order: 3;
}
```

---

### 2. Right Sidebar

**فایل:** `layouts/partials/sidebar.html`

**حذف شده:**
```html
<!-- مرتب‌سازی مقالات - در سایدبار -->
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">🔄 مرتب‌سازی بر اساس</h3>
    <div class="sidebar-widget-content">
        <!-- ... Widget content ... -->
    </div>
</div>
```

**Widgets باقی‌مانده در Right Sidebar:**
1. 🔍 جستجو
2. 📚 دسته‌بندی‌ها
3. 🏷️ تگ‌ها
4. 📝 نوشته‌های تازه

---

### 3. Left Sidebar

**فایل:** `layouts/partials/sidebar-left.html`

**اضافه شده:**
```html
{{/* Widget 4: Sort - مرتب‌سازی بر اساس */}}
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">🔄 مرتب‌سازی بر اساس</h3>
    <div class="sidebar-widget-content">
        <div class="sort-dropdown-container">
            <button class="sort-dropdown-toggle" id="sidebarSortToggle" onclick="toggleSidebarSortDropdown()">
                <span class="sort-current-label" id="sidebarSortLabel">جدیدترین</span>
                <svg class="dropdown-arrow" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 10l5 5 5-5z"/>
                </svg>
            </button>
            <ul class="sort-dropdown-menu" id="sidebarSortMenu">
                <li class="sort-option active" data-value="newest" onclick="applySidebarSort('newest')">
                    <svg class="option-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z"/>
                    </svg>
                    <span class="option-label">جدیدترین</span>
                    <svg class="check-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                    </svg>
                </li>
                <li class="sort-option" data-value="oldest" onclick="applySidebarSort('oldest')">
                    <svg class="option-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"/>
                    </svg>
                    <span class="option-label">قدیمی‌ترین</span>
                    <svg class="check-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                    </svg>
                </li>
            </ul>
        </div>
    </div>
</div>
```

**Widgets در Left Sidebar (به ترتیب):**
1. 📊 سطح دشواری
2. 📄 نوع مطالب
3. 🔬 نیاز به آزمایشگاه
4. 🔄 مرتب‌سازی بر اساس

---

## ✅ تست‌ها

### 1. Build Test

```bash
hugo --cleanDestinationDir
```

**نتیجه:**
- ✅ Pages: 263
- ✅ Build time: ~1.6s
- ✅ هیچ خطایی گزارش نشد

### 2. HTML Validation

**Home Page:**
```html
<div class="main-content-wrapper three-column-layout">
  <!-- Left Sidebar با 4 Widget -->
  <aside class="sidebar sidebar-left">
    <div class="sidebar-widget">📊 سطح دشواری</div>
    <div class="sidebar-widget">📄 نوع مطالب</div>
    <div class="sidebar-widget">🔬 نیاز به آزمایشگاه</div>
    <div class="sidebar-widget">🔄 مرتب‌سازی بر اساس</div>
  </aside>
  
  <!-- Main Content -->
  <div class="main-content">...</div>
  
  <!-- Right Sidebar با 4 Widget -->
  <aside class="sidebar">
    <div class="sidebar-widget">🔍 جستجو</div>
    <div class="sidebar-widget">📚 دسته‌بندی‌ها</div>
    <div class="sidebar-widget">🏷️ تگ‌ها</div>
    <div class="sidebar-widget">📝 نوشته‌های تازه</div>
  </aside>
</div>
```

**نتیجه:** ✅ ترتیب صحیح

### 3. CSS Grid Validation

**Computed Values:**
- Right Sidebar: `grid-column: 1` ✅
- Main Content: `grid-column: 2` ✅
- Left Sidebar: `grid-column: 3` ✅
- Direction: `rtl` ✅

### 4. Widget Validation

**Right Sidebar:**
- ✅ Widget "مرتب‌سازی" حذف شده
- ✅ 4 Widget باقی‌مانده

**Left Sidebar:**
- ✅ Widget "مرتب‌سازی" اضافه شده
- ✅ در انتهای لیست Widgets
- ✅ عملکرد JavaScript صحیح

---

## 📊 خلاصه تغییرات

| بخش | قبل | بعد | وضعیت |
|-----|-----|-----|--------|
| Grid Columns | `280px 1fr 350px` | `350px 1fr 280px` | ✅ |
| Direction | - | `rtl` | ✅ |
| Right Sidebar Position | Column 3 | Column 1 | ✅ |
| Left Sidebar Position | Column 1 | Column 3 | ✅ |
| Sort Widget Location | Right Sidebar | Left Sidebar | ✅ |
| Widget Count (Right) | 5 | 4 | ✅ |
| Widget Count (Left) | 3 | 4 | ✅ |

---

## 🎯 نتیجه‌گیری

تمام باگ‌های گزارش شده برطرف شدند:

✅ **Right Sidebar در مکان صحیح** (سمت راست)  
✅ **Left Sidebar در مکان صحیح** (سمت چپ)  
✅ **Widget مرتب‌سازی به Left Sidebar منتقل شد**  
✅ **Widget مرتب‌سازی در انتهای Left Sidebar قرار دارد**  
✅ **RTL Layout به درستی اعمال شد**  
✅ **Build بدون خطا**  
✅ **تست‌های HTML و CSS موفق**  

---

**برطرف شده توسط:** AI Assistant  
**تاریخ:** 2026-02-11  
**وضعیت نهایی:** ✅ **تایید شده و تست شده**
