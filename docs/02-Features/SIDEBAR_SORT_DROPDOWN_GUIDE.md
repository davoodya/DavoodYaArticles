# راهنمای Dropdown مرتب‌سازی در Sidebar

تاریخ: 2026-02-10

## خلاصه

یک منوی Drop Down برای مرتب‌سازی مقالات در Sidebar اضافه شده است که به کاربر امکان می‌دهد مقالات را بر اساس **جدیدترین** یا **قدیمی‌ترین** مرتب کند.

## ویژگی‌ها

### 1. موقعیت در Sidebar
- منوی مرتب‌سازی **بعد از بخش "نوشته‌های تازه"** در Sidebar قرار دارد
- عنوان بخش: **🔄 مرتب‌سازی بر اساس**

### 2. گزینه‌های مرتب‌سازی
- **جدیدترین**: مقالات جدید در ابتدا (پیش‌فرض)
- **قدیمی‌ترین**: مقالات قدیمی در ابتدا

### 3. طراحی و استایل
- استایل هماهنگ با سایر المان‌های Sidebar (دسته‌بندی‌ها، تگ‌ها)
- رنگ‌ها و افکت‌های Cyberpunk Theme
- انیمیشن‌های smooth برای باز و بسته شدن منو
- آیکون‌های بصری برای هر گزینه
- علامت ✓ (check icon) برای گزینه فعال

### 4. عملکرد

#### 4.1. باز و بسته کردن منو
- کلیک روی دکمه اصلی → باز/بسته شدن منو
- کلیک خارج از منو → بسته شدن خودکار
- فلش dropdown با انیمیشن چرخش 180 درجه

#### 4.2. انتخاب گزینه
- کلیک روی هر گزینه → اعمال مرتب‌سازی فوری
- تغییر label دکمه اصلی
- بروزرسانی active state گزینه انتخاب شده
- بسته شدن خودکار منو

#### 4.3. همزمان‌سازی با Filter Modal
- وقتی از sidebar sort استفاده می‌شود، radio button در modal filter هم به‌روز می‌شود
- وقتی از modal filter استفاده می‌شود، sidebar sort label هم به‌روز می‌شود
- **یک حالت همیشه در هر دو جا سینک است**

### 5. سازگاری با سیستم‌های موجود

مرتب‌سازی با سه سیستم زیر سازگار است:

1. **Load More System** (اولویت اول)
   - استفاده از `window.applyLoadMoreFilter()`
   - مرتب‌سازی با `sortOrder` parameter

2. **Articles Loader** (fallback دوم)
   - استفاده از `window.applyArticlesFilter()`

3. **DOM-based Filter** (fallback سوم)
   - استفاده از `filterArticles()`

## فایل‌های تغییر یافته

### 1. `layouts/partials/sidebar.html`
```html
<!-- مرتب‌سازی مقالات - در سایدبار -->
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

### 2. `static/css/main2.css` و `assets/css/main2.css`
استایل‌های زیر اضافه شده:

- `.sort-dropdown-container`: Container اصلی
- `.sort-dropdown-toggle`: دکمه اصلی dropdown
- `.sort-current-label`: Label فعلی (جدیدترین/قدیمی‌ترین)
- `.dropdown-arrow`: فلش با انیمیشن چرخش
- `.sort-dropdown-menu`: منوی dropdown با انیمیشن fade
- `.sort-option`: هر گزینه در منو
- `.option-icon`: آیکون هر گزینه
- `.option-label`: متن هر گزینه
- `.check-icon`: علامت تیک برای گزینه فعال

### 3. `static/assets/js/filters.js`
توابع زیر اضافه شده:

#### `toggleSidebarSortDropdown()`
باز و بسته کردن dropdown

#### `applySidebarSort(sortValue)`
- دریافت مقدار مرتب‌سازی ('newest' یا 'oldest')
- بروزرسانی label و active state
- همزمان‌سازی با modal filter
- اعمال فیلترهای فعلی با ترتیب مرتب‌سازی جدید

#### Event Listener: Click Outside
- بستن dropdown هنگام کلیک خارج از آن

## نحوه استفاده

### برای کاربران
1. به هر صفحه list (دسته‌بندی یا all-articles) بروید
2. در sidebar، بخش "🔄 مرتب‌سازی بر اساس" را پیدا کنید (بعد از نوشته‌های تازه)
3. روی دکمه کلیک کنید تا منو باز شود
4. گزینه مورد نظر را انتخاب کنید
5. مقالات به‌صورت خودکار مرتب‌سازی می‌شوند

### تست

برای تست عملکرد:

```bash
# 1. Build کردن سایت
hugo --gc --minify

# 2. اجرای dev server
hugo server

# 3. باز کردن مرورگر و رفتن به یک صفحه list
# مثال: http://localhost:1313/cyber-security/
# یا: http://localhost:1313/all-articles/

# 4. تست موارد زیر:
# - باز و بسته شدن dropdown
# - تغییر مرتب‌سازی و بررسی ترتیب مقالات
# - همزمان‌سازی با modal filter
# - کلیک خارج از dropdown
# - responsive بودن در موبایل/تبلت
```

## نکات فنی

### 1. State Management
- Label dropdown همیشه با ترتیب مرتب‌سازی فعلی همزمان است
- Active state با CSS class `.active` مدیریت می‌شود

### 2. Event Handling
- از `onclick` در HTML استفاده شده (سازگار با modal filter)
- Event listener برای کلیک خارج به `document` اضافه شده

### 3. Filter Integration
- فیلترهای فعلی حفظ می‌شوند
- فقط ترتیب مرتب‌سازی تغییر می‌کند
- از همان تابع `matchesFilter()` برای consistency استفاده می‌شود

### 4. Fallback System
- سه سطح fallback برای سازگاری با سیستم‌های مختلف
- همیشه یکی از سیستم‌ها کار می‌کند

## مشکلات احتمالی و راه‌حل

### مشکل: Dropdown باز نمی‌شود
**راه‌حل:**
- بررسی console برای خطاهای JavaScript
- مطمئن شوید `filters.js` لود شده است
- بررسی ID های المان‌ها (`sidebarSortToggle`, `sidebarSortMenu`)

### مشکل: مرتب‌سازی اعمال نمی‌شود
**راه‌حل:**
- بررسی console برای لاگ‌های `[Sidebar Sort]`
- مطمئن شوید `load-more.js` یا `articles-loader.js` لود شده است
- بررسی `data-value` در گزینه‌ها

### مشکل: همزمان‌سازی با modal کار نمی‌کند
**راه‌حل:**
- بررسی `name` و `value` radio button‌ها در modal
- مطمئن شوید توابع `applyFilters()` و `applySidebarSort()` هر دو به‌روز شده‌اند

## تغییرات آینده (پیشنهادی)

1. **افزودن گزینه‌های بیشتر:**
   - مرتب‌سازی بر اساس محبوبیت
   - مرتب‌سازی بر اساس مدت زمان مطالعه
   - مرتب‌سازی الفبایی

2. **بهبود UX:**
   - نمایش تعداد مقالات در هر حالت
   - انیمیشن smooth برای تغییر ترتیب مقالات
   - ذخیره ترجیح کاربر در localStorage

3. **Accessibility:**
   - افزودن ARIA labels
   - پشتیبانی کامل از keyboard navigation
   - Screen reader friendly

## مراجع

- `layouts/partials/sidebar.html` - ساختار HTML
- `static/css/main2.css` - استایل‌های sidebar sort
- `static/assets/js/filters.js` - منطق JavaScript
- `static/assets/js/load-more.js` - سیستم مرتب‌سازی مقالات
- `docs/FILTER_MODAL_UNIFIED_GUIDE.md` - راهنمای سیستم فیلتر
- `docs/LOAD_MORE_IMPLEMENTATION_GUIDE.md` - راهنمای Load More

---

**نسخه:** 1.0.0  
**تاریخ آخرین بروزرسانی:** 2026-02-10  
**وضعیت:** ✅ کامل و تست شده
