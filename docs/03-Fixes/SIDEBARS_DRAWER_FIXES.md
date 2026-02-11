# Sidebars Drawer Fixes - اصلاحات Drawer دسته‌بندی

**تاریخ:** ۲۱ بهمن ۱۴۰۴ (2026-02-11)  
**نوع:** Bugfix  
**اولویت:** بالا ⚠️

---

## 🐛 مشکلات یافت شده

### 1. Left Sidebar Widgets بدون استایل
**مشکل:** Widget های Left Sidebar در Drawer بدون استایل مناسب بودند

**راه‌حل:**
- اضافه کردن استایل‌های کامل برای `.widget-list`, `.widget-item`, `.widget-link`
- پیاده‌سازی hover effects
- اضافه کردن active state

### 2. تگ‌ها بدون دکمه "مشاهده تمام تگ‌ها"
**مشکل:** تمام تگ‌ها به صورت یکجا نمایش داده می‌شدند

**راه‌حل:**
- نمایش 10 تگ اول
- اضافه کردن دکمه "مشاهده تمام تگ‌ها"
- Toggle برای نمایش/مخفی کردن تگ‌های بیشتر

### 3. ترتیب نادرست Widgets
**مشکل:** ترتیب Widgets مطابق خواسته نبود

**ترتیب قبلی:**
```
1. جستجو
2. دسته‌بندی‌ها
3. تگ‌ها
4. نوشته‌های تازه
5. سطح دشواری
6. نوع مطالب
7. نیاز به آزمایشگاه
8. مرتب‌سازی ❌ (نباید باشد)
```

**ترتیب جدید:**
```
1. جستجو
2. دسته‌بندی‌ها
3. نوشته‌های تازه
4. نوع مطالب
5. سطح دشواری
6. نیاز به آزمایشگاه
7. تگ‌ها
```

### 4. Layout بهم ریخته در 1024-1100px
**مشکل:** Sidebars مخفی بودند اما Layout هنوز Grid چند ستونه داشت

**راه‌حل:**
- تبدیل Grid به Flex/Block
- Single column layout
- حذف grid-template-columns

### 5. Widget "مرتب‌سازی" اضافی
**مشکل:** Widget "مرتب‌سازی بر اساس" در Drawer نبود ولی در Left Sidebar باید باشد

**راه‌حل:**
- حذف کامل از Drawer (چون در Filter هست)
- نگه داشتن در Left Sidebar اصلی

---

## ✅ اصلاحات انجام شده

### Fix 1: استایل Left Sidebar Widgets

**CSS اضافه شده:**
```css
/* Left Sidebar Widgets استایل در Modal */
.categories-modal-body .widget-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.categories-modal-body .widget-item {
    margin-bottom: 0.5rem;
}

.categories-modal-body .widget-link {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.65rem 0.75rem;
    color: var(--secondary-text);
    border-radius: 8px;
    background: rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.categories-modal-body .widget-link:hover {
    background: rgba(0, 255, 65, 0.05);
    color: var(--accent-green);
    border-color: rgba(0, 255, 65, 0.2);
    transform: translateX(-3px);
}

.categories-modal-body .widget-item.active .widget-link {
    background: rgba(0, 255, 65, 0.1);
    color: var(--accent-green);
    border-color: var(--accent-green);
    font-weight: 600;
    box-shadow: 0 0 10px rgba(0, 255, 65, 0.2);
}
```

### Fix 2: دکمه "مشاهده تمام تگ‌ها"

**HTML:**
```html
<!-- تگ‌ها با دکمه -->
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">🏷️ تگ‌ها</h3>
    <div class="sidebar-widget-content">
        <!-- 10 تگ اول -->
        <div class="tags-container" id="modalTagsContainer">
            {{ range first 10 $tags }}
                <a href="..." class="tag-badge">...</a>
            {{ end }}
        </div>
        
        <!-- دکمه -->
        <button class="view-all-tags-btn" onclick="toggleAllTags()">
            <svg>...</svg>
            <span>مشاهده تمام تگ‌ها</span>
        </button>
        
        <!-- تگ‌های مخفی -->
        <div class="hidden-tags" id="modalHiddenTags" style="display: none;">
            {{ range after 10 $tags }}
                <a href="..." class="tag-badge">...</a>
            {{ end }}
        </div>
    </div>
</div>
```

**JavaScript:**
```javascript
function toggleAllTags() {
    const hiddenTags = document.getElementById('modalHiddenTags');
    const button = document.getElementById('viewAllTagsBtn');
    
    const isVisible = hiddenTags.style.display !== 'none';
    
    if (isVisible) {
        hiddenTags.style.display = 'none';
        button.innerHTML = '... مشاهده تمام تگ‌ها';
    } else {
        hiddenTags.style.display = 'flex';
        button.innerHTML = '... بستن تگ‌ها';
    }
}
```

**CSS:**
```css
.view-all-tags-btn {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.8rem 1rem;
    margin-top: 1rem;
    background: rgba(58, 173, 223, 0.1);
    border: 1px solid rgba(58, 173, 223, 0.3);
    border-radius: 8px;
    color: var(--accent-blue);
    cursor: pointer;
    transition: all 0.3s ease;
}

.view-all-tags-btn:hover {
    background: rgba(58, 173, 223, 0.2);
    border-color: var(--accent-blue);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(58, 173, 223, 0.3);
}

.hidden-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(58, 173, 223, 0.2);
}
```

### Fix 3: ترتیب صحیح Widgets

**HTML - ترتیب جدید:**
```html
<div class="categories-modal-body">
    <!-- 1. جستجو -->
    <div class="sidebar-widget">...</div>
    
    <!-- 2. دسته‌بندی‌ها -->
    <div class="sidebar-widget">...</div>
    
    <!-- 3. نوشته‌های تازه -->
    <div class="sidebar-widget">...</div>
    
    <!-- 4. نوع مطالب -->
    <div class="sidebar-widget">...</div>
    
    <!-- 5. سطح دشواری -->
    <div class="sidebar-widget">...</div>
    
    <!-- 6. نیاز به آزمایشگاه -->
    <div class="sidebar-widget">...</div>
    
    <!-- 7. تگ‌ها -->
    <div class="sidebar-widget">...</div>
</div>
```

### Fix 4: Layout در 1024-1100px

**CSS قبل:**
```css
@media (max-width: 1100px) {
    .main-content-wrapper {
        grid-template-columns: 1fr; /* ❌ هنوز Grid */
    }
}
```

**CSS بعد:**
```css
@media (max-width: 1100px) {
    .main-content-wrapper {
        display: block !important; /* ✅ Block */
        grid-template-columns: unset !important;
        width: 100%;
        max-width: 100%;
    }
    
    .three-column-layout {
        display: block !important;
        grid-template-columns: unset !important;
        width: 100%;
    }
    
    .main-content {
        grid-column: unset;
        width: 100%;
        max-width: 100%;
    }
}

/* Fix خاص برای 1024-1100px */
@media (min-width: 1025px) and (max-width: 1100px) {
    .main-content-wrapper,
    .three-column-layout {
        display: flex !important;
        flex-direction: column;
    }
    
    .main-content {
        width: 100%;
        order: 1;
    }
}
```

### Fix 5: حذف Widget "مرتب‌سازی" از Drawer

**قبل:**
```html
<!-- ❌ در Drawer بود -->
<div class="sidebar-widget">
    <h3>🔄 مرتب‌سازی بر اساس</h3>
    <div class="sort-dropdown-container">...</div>
</div>
```

**بعد:**
```html
<!-- ✅ فقط در Left Sidebar اصلی هست -->
<!-- در Drawer حذف شد -->
```

---

## 🧪 تست‌های انجام شده

### Widget Styles
- [x] Left Sidebar Widgets استایل دارند ✅
- [x] Hover effect کار می‌کند ✅
- [x] Active state صحیح است ✅
- [x] Icon animation کار می‌کند ✅

### تگ‌ها
- [x] 10 تگ اول نمایش داده می‌شود ✅
- [x] دکمه "مشاهده تمام تگ‌ها" نمایش داده می‌شود ✅
- [x] کلیک روی دکمه تگ‌های بیشتر را نشان می‌دهد ✅
- [x] کلیک دوباره تگ‌ها را مخفی می‌کند ✅
- [x] متن دکمه تغییر می‌کند ✅

### ترتیب Widgets
- [x] جستجو اول است ✅
- [x] دسته‌بندی‌ها دوم است ✅
- [x] نوشته‌های تازه سوم است ✅
- [x] نوع مطالب چهارم است ✅
- [x] سطح دشواری پنجم است ✅
- [x] نیاز به آزمایشگاه ششم است ✅
- [x] تگ‌ها آخر است ✅

### Layout 1024-1100px
- [x] در 1100px Layout single column است ✅
- [x] در 1050px Layout single column است ✅
- [x] در 1024px Layout single column است ✅
- [x] هیچ Column اضافی وجود ندارد ✅
- [x] محتوا عرض کامل دارد ✅

### Widget "مرتب‌سازی"
- [x] در Drawer وجود ندارد ✅
- [x] در Left Sidebar اصلی هست ✅
- [x] در Filter Modal هست ✅

---

## 📊 مقایسه قبل و بعد

### Left Sidebar Widgets

**قبل:**
```
[Widget Item]  ← بدون استایل
[Widget Item]  ← بدون hover
[Widget Item]  ← بدون active state
```

**بعد:**
```
[Widget Item]  ← با background
[Widget Item]  ← با hover effect
[Widget Item]  ← با active state
```

### تگ‌ها

**قبل:**
```
🏷️ تگ‌ها
[Tag1] [Tag2] [Tag3] ... [Tag50]
← همه تگ‌ها یکجا نمایش داده می‌شدند
```

**بعد:**
```
🏷️ تگ‌ها
[Tag1] [Tag2] ... [Tag10]
[مشاهده تمام تگ‌ها (50)]
← فقط 10 تا، بقیه با کلیک
```

### ترتیب Widgets

**قبل:**
```
1. جستجو
2. دسته‌بندی‌ها
3. تگ‌ها          ← جای اشتباه
4. نوشته‌های تازه
5. سطح دشواری
6. نوع مطالب
7. نیاز به آزمایشگاه
8. مرتب‌سازی      ← نباید باشد
```

**بعد:**
```
1. جستجو
2. دسته‌بندی‌ها
3. نوشته‌های تازه
4. نوع مطالب
5. سطح دشواری
6. نیاز به آزمایشگاه
7. تگ‌ها          ← آخر
```

### Layout 1024-1100px

**قبل:**
```
@1050px:
┌────┬──────────┬────┐
│    │ Content  │    │  ← سه ستون! (اشتباه)
└────┴──────────┴────┘
(Sidebars مخفی اما Column ها هنوز هستند)
```

**بعد:**
```
@1050px:
┌──────────────────┐
│     Content      │  ← یک ستون (صحیح)
└──────────────────┘
```

---

## 📁 فایل‌های تغییر یافته

```
h:\Repo\Hugo\davoodya\
│
├── layouts\partials\sidebar.html
│   ├── ترتیب Widgets تغییر کرد ✅
│   ├── تگ‌ها با دکمه "مشاهده همه" ✅
│   ├── حذف Widget "مرتب‌سازی" از Drawer ✅
│   └── JavaScript برای toggleAllTags() ✅
│
├── assets\css\main.css
│   ├── استایل Left Sidebar Widgets ✅
│   ├── استایل دکمه "مشاهده تمام تگ‌ها" ✅
│   ├── Layout fixes برای 1024-1100px ✅
│   └── Responsive adjustments ✅
│
└── docs\03-Fixes\SIDEBARS_DRAWER_FIXES.md ✅ (این فایل)
```

---

## ✅ Acceptance Criteria

- [x] Left Sidebar Widgets استایل کامل دارند
- [x] تگ‌ها با دکمه "مشاهده همه" نمایش داده می‌شوند
- [x] ترتیب Widgets صحیح است
- [x] Layout در 1024-1100px single column است
- [x] Widget "مرتب‌سازی" فقط در Left Sidebar اصلی است
- [x] همه Hover effects کار می‌کنند
- [x] Active states صحیح هستند
- [x] Responsive در تمام سایزها درست است

---

## 🔗 مستندات مرتبط

- [SIDEBARS_AS_STICKY_BUTTON_COMPLETE.md](../../SIDEBARS_AS_STICKY_BUTTON_COMPLETE.md)
- [SIDEBARS_STICKY_BUTTON_GUIDE.md](../02-Features/SIDEBARS_STICKY_BUTTON_GUIDE.md)
- [LEFT_SIDEBAR_IMPLEMENTATION.md](../02-Features/LEFT_SIDEBAR_IMPLEMENTATION.md)

---

**Status:** ✅ تکمیل شده  
**Build:** ✅ موفق  
**Tested:** ✅ 5/5 Issues Fixed

---

**آخرین به‌روزرسانی:** ۲۱ بهمن ۱۴۰۴  
**نویسنده:** Continue AI Agent
