# پیاده‌سازی Dropdown مرتب‌سازی در Sidebar

**تاریخ:** 1405/11/21 (2026-02-10)  
**نسخه:** 1.0.0  
**وضعیت:** ✅ تکمیل شده

---

## 📋 خلاصه

یک منوی **Drop Down** برای مرتب‌سازی مقالات در **Sidebar** اضافه شده است که به کاربر امکان می‌دهد مقالات را بر اساس **جدیدترین** یا **قدیمی‌ترین** مرتب کند.

این ویژگی کاملاً با سیستم فیلتر موجود (Filter Modal) همزمان‌سازی می‌شود.

---

## 🎯 هدف

قبلاً فیلتر مرتب‌سازی فقط در **Filter Modal** (صفحه فیلترهای باز شونده) موجود بود. حالا همین قابلیت در **Sidebar** هم اضافه شده تا کاربر بدون باز کردن modal بتواند مقالات را مرتب کند.

---

## ✨ ویژگی‌های جدید

### 1️⃣ موقعیت در Sidebar
- منوی مرتب‌سازی **بعد از "نوشته‌های تازه"** در Sidebar قرار دارد
- عنوان: **🔄 مرتب‌سازی بر اساس**

### 2️⃣ گزینه‌های مرتب‌سازی
- **جدیدترین** (پیش‌فرض): مقالات جدید ابتدا نمایش داده می‌شوند
- **قدیمی‌ترین**: مقالات قدیمی ابتدا نمایش داده می‌شوند

### 3️⃣ طراحی
- استایل هماهنگ با تم Cyberpunk و سایر المان‌های Sidebar
- رنگ‌بندی سبز نئونی (#00ff41)
- انیمیشن‌های نرم برای باز/بسته شدن
- آیکون‌های بصری برای هر گزینه
- علامت تیک (✓) برای گزینه فعال

### 4️⃣ عملکرد

#### باز و بسته کردن
- کلیک روی دکمه → باز/بسته شدن منو
- کلیک خارج از منو → بسته شدن خودکار
- فلش dropdown چرخش 180 درجه با انیمیشن

#### انتخاب گزینه
- کلیک روی گزینه → اعمال فوری مرتب‌سازی
- تغییر label دکمه به گزینه انتخابی
- بسته شدن خودکار منو

#### همزمان‌سازی (Sync)
- ✅ تغییر در **Sidebar Sort** → بروزرسانی **Modal Filter**
- ✅ تغییر در **Modal Filter** → بروزرسانی **Sidebar Sort**
- همیشه یک حالت در هر دو جا

---

## 🔧 فایل‌های تغییر یافته

### 1. `layouts/partials/sidebar.html`
بخش جدید اضافه شده:

```html
<!-- مرتب‌سازی مقالات - در سایدبار -->
<div class="sidebar-widget">
    <h3 class="sidebar-widget-title">🔄 مرتب‌سازی بر اساس</h3>
    <div class="sidebar-widget-content">
        <div class="sort-dropdown-container">
            <button class="sort-dropdown-toggle" id="sidebarSortToggle">
                <span class="sort-current-label" id="sidebarSortLabel">جدیدترین</span>
                <svg class="dropdown-arrow">...</svg>
            </button>
            <ul class="sort-dropdown-menu" id="sidebarSortMenu">
                <li class="sort-option active" data-value="newest">
                    جدیدترین
                </li>
                <li class="sort-option" data-value="oldest">
                    قدیمی‌ترین
                </li>
            </ul>
        </div>
    </div>
</div>
```

**موقعیت:** بعد از `<!-- نوشته‌های تازه -->`

### 2. `static/css/main2.css` و `assets/css/main2.css`
استایل‌های جدید:

- `.sort-dropdown-container` - Container اصلی
- `.sort-dropdown-toggle` - دکمه باز کردن dropdown
- `.sort-current-label` - label فعلی
- `.dropdown-arrow` - فلش با انیمیشن چرخش
- `.sort-dropdown-menu` - منوی dropdown
- `.sort-option` - هر گزینه
- `.option-icon` - آیکون هر گزینه
- `.option-label` - متن هر گزینه
- `.check-icon` - علامت تیک برای گزینه فعال

### 3. `static/assets/js/filters.js`
توابع جدید:

#### `toggleSidebarSortDropdown()`
باز و بسته کردن dropdown با toggle کردن class `active`

#### `applySidebarSort(sortValue)`
- دریافت مقدار ('newest' یا 'oldest')
- بروزرسانی label دکمه
- بروزرسانی active state گزینه‌ها
- همزمان‌سازی با modal filter
- اعمال مرتب‌سازی با حفظ فیلترهای فعلی

#### Event Listener
بسته شدن dropdown هنگام کلیک خارج

---

## 🔄 نحوه کار

### مثال: کاربر روی "قدیمی‌ترین" کلیک می‌کند

```
1. applySidebarSort('oldest') اجرا می‌شود

2. Label دکمه تغییر می‌کند:
   "جدیدترین" → "قدیمی‌ترین"

3. Active state به‌روز می‌شود:
   - گزینه "جدیدترین": class 'active' حذف
   - گزینه "قدیمی‌ترین": class 'active' اضافه
   - علامت تیک ظاهر می‌شود

4. همزمان‌سازی با Modal:
   - radio button "قدیمی‌ترین" در modal checked می‌شود

5. اعمال فیلتر:
   - فیلترهای فعلی حفظ می‌شوند
   - فقط ترتیب به 'oldest' تغییر می‌کند
   - applyLoadMoreFilter() با sortOrder='oldest' اجرا می‌شود

6. مقالات مرتب‌سازی می‌شوند:
   - مقالات قدیمی‌تر در ابتدا
   - با انیمیشن fadeInUp

7. Dropdown بسته می‌شود
```

---

## 🧪 تست

### مراحل تست:

```bash
# 1. Build
hugo --gc --minify

# 2. Dev server
hugo server

# 3. باز کردن مرورگر
# مثال: http://localhost:1313/cyber-security/
```

### موارد تست:

✅ **عملکرد پایه:**
- [ ] باز شدن dropdown با کلیک روی دکمه
- [ ] بسته شدن با کلیک مجدد
- [ ] بسته شدن با کلیک خارج
- [ ] تغییر label هنگام انتخاب

✅ **مرتب‌سازی:**
- [ ] مرتب‌سازی بر اساس جدیدترین
- [ ] مرتب‌سازی بر اساس قدیمی‌ترین
- [ ] بررسی ترتیب واقعی مقالات (تاریخ‌ها)

✅ **همزمان‌سازی:**
- [ ] تغییر در sidebar → بروزرسانی modal
- [ ] تغییر در modal → بروزرسانی sidebar

✅ **ترکیب با فیلتر:**
- [ ] اعمال فیلتر + تغییر ترتیب
- [ ] تغییر ترتیب + اعمال فیلتر
- [ ] reset فیلتر → بازگشت به جدیدترین

✅ **Responsive:**
- [ ] Desktop (> 1024px)
- [ ] Tablet (768px - 1024px)
- [ ] Mobile (< 768px)

✅ **Browser Compatibility:**
- [ ] Chrome
- [ ] Firefox
- [ ] Edge
- [ ] Safari (اگر در دسترس است)

---

## 🛠️ نکات فنی

### 1. سازگاری با سیستم‌های مختلف

```javascript
// اولویت اول: Load More System
if (typeof window.applyLoadMoreFilter === 'function') {
    // استفاده از load-more.js
}

// اولویت دوم: Articles Loader
else if (typeof window.applyArticlesFilter === 'function') {
    // استفاده از articles-loader.js
}

// Fallback
else {
    // استفاده از filterArticles()
}
```

### 2. State Management

```javascript
// همیشه sync هستند:
- sidebarSortLabel.textContent
- active class در sidebarSortMenu
- checked state در modal radio buttons
- currentSortOrder در load-more.js
```

### 3. Event Handling

```html
<!-- در HTML -->
<button onclick="toggleSidebarSortDropdown()">

<li onclick="applySidebarSort('newest')">
```

```javascript
// در JavaScript
document.addEventListener('click', function(e) {
    // Close dropdown on click outside
});
```

---

## 📊 مقایسه قبل و بعد

### قبل:
- ❌ فقط از طریق Modal Filter قابل دسترسی
- ❌ نیاز به باز کردن modal
- ❌ 3 کلیک: باز کردن modal → انتخاب → اعمال فیلتر

### بعد:
- ✅ دسترسی مستقیم از Sidebar
- ✅ بدون نیاز به modal
- ✅ 2 کلیک: باز کردن dropdown → انتخاب (اعمال خودکار)
- ✅ همزمان‌سازی کامل با modal

---

## 🐛 مشکلات احتمالی

### مشکل 1: Dropdown باز نمی‌شود
**علت:**
- خطا در JavaScript
- `filters.js` لود نشده
- ID های المان‌ها اشتباه

**راه‌حل:**
```javascript
// بررسی console:
[Filter System] Loaded successfully

// بررسی المان‌ها:
document.getElementById('sidebarSortToggle')
document.getElementById('sidebarSortMenu')
```

### مشکل 2: مرتب‌سازی اعمال نمی‌شود
**علت:**
- `load-more.js` لود نشده
- `data-value` اشتباه در گزینه‌ها

**راه‌حل:**
```javascript
// بررسی console:
[Sidebar Sort] Applying sort: newest
[Load More] Sorting articles by: newest

// بررسی data-value:
<li data-value="newest">
<li data-value="oldest">
```

### مشکل 3: Sync کار نمی‌کند
**علت:**
- `name` یا `value` radio button‌ها اشتباه
- تابع `applyFilters()` یا `applySidebarSort()` قدیمی

**راه‌حل:**
```html
<!-- در modal باید باشد: -->
<input type="radio" name="sort_order" value="newest">
<input type="radio" name="sort_order" value="oldest">
```

---

## 🚀 بهبودهای آینده (پیشنهادی)

### Phase 2:
- [ ] مرتب‌سازی بر اساس محبوبیت (تعداد بازدید)
- [ ] مرتب‌سازی بر اساس مدت زمان مطالعه
- [ ] مرتب‌سازی الفبایی (حروف فارسی)

### Phase 3:
- [ ] ذخیره ترجیح کاربر در `localStorage`
- [ ] نمایش تعداد مقالات در هر حالت
- [ ] انیمیشن smooth برای جابجایی کارت‌ها

### Phase 4 (Accessibility):
- [ ] ARIA labels کامل
- [ ] پشتیبانی کامل از صفحه‌کلید
- [ ] Screen reader optimization
- [ ] Focus management

---

## 📚 مستندات مرتبط

- `docs/SIDEBAR_SORT_DROPDOWN_GUIDE.md` - راهنمای کامل فنی
- `docs/FILTER_MODAL_UNIFIED_GUIDE.md` - راهنمای سیستم فیلتر
- `docs/LOAD_MORE_IMPLEMENTATION_GUIDE.md` - راهنمای Load More
- `docs/SIDEBAR_GUIDE.md` - راهنمای Sidebar
- `SORT_FEATURE_IMPLEMENTATION.md` - پیاده‌سازی فیلتر مرتب‌سازی اولیه

---

## ✅ Checklist تکمیل

- [x] طراحی UI/UX
- [x] پیاده‌سازی HTML در sidebar.html
- [x] پیاده‌سازی CSS در main2.css
- [x] پیاده‌سازی JavaScript در filters.js
- [x] همزمان‌سازی با modal filter
- [x] سازگاری با Load More System
- [x] Fallback برای سیستم‌های قدیمی
- [x] Build موفقیت‌آمیز
- [x] مستندسازی کامل
- [x] آماده برای تست

---

## 👨‍💻 توسعه‌دهنده

**توسط:** AI Assistant (Chad)  
**تاریخ:** 1405/11/21  
**زمان توسعه:** ~30 دقیقه

---

**Status:** ✅ Ready for Testing  
**Priority:** High  
**Type:** Feature Enhancement
