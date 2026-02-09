# راهنمای جستجوی پیشرفته - وبسایت Davoodya

## 📋 توضیحات کلی

سیستم جستجوی AJAX با دو حالت پیاده‌سازی شده است:
1. **جستجوی Header** (Overlay تمام صفحه)
2. **جستجوی Sidebar** (Inline)

## 🎯 ویژگی‌های جستجو

### 1. جستجوی Header (تمام صفحه)
- **دکمه جستجو** در header با آیکون 🔍
- کلیک روی دکمه → باز شدن Overlay تمام صفحه
- **دکمه بستن** در بالا سمت چپ
- جستجو در **عنوان** و **تگ‌های** مقالات
- فیلتر بر اساس **دسته‌بندی**
- نمایش نتایج به صورت **Grid**
- نمایش تگ‌های هر مقاله
- ESC برای بستن
- کلیک خارج از Overlay برای بستن

### 2. جستجوی Sidebar (Inline)
- جستجو مستقیم در sidebar
- بدون نیاز به باز کردن Overlay
- فیلتر بر اساس دسته‌بندی
- نمایش نتایج به صورت لیست
- Scrollable results

## 🔍 نحوه جستجو

### جستجو در عنوان
```
مثال: "امنیت"
نتیجه: تمام مقالاتی که کلمه "امنیت" در عنوان دارند
```

### جستجو در تگ‌ها
```
مثال: "CyberSecurity"
نتیجه: تمام مقالاتی که تگ "CyberSecurity" دارند
```

### فیلتر دسته‌بندی
```
1. انتخاب دسته‌بندی از dropdown
2. جستجو فقط در آن دسته‌بندی انجام می‌شود
```

## 📁 ساختار فایل‌ها

### Frontend Files
```
layouts/
├── partials/
│   ├── search.html         # کامپوننت جستجو
│   ├── header.html         # شامل دکمه جستجو
│   └── sidebar.html        # شامل جستجوی inline
└── _default/
    └── index.json          # داده‌های JSON برای جستجو
```

### CSS Files
```
assets/css/
└── search.css              # استایل‌های جستجو
```

### JSON Output
```
public/
└── index.json              # خروجی JSON تمام مقالات
```

## 🎨 استایل‌دهی

### رنگ‌ها و تم
- **تم Cyberpunk**: سازگار با طراحی کلی
- **رنگ اصلی**: سبز نئون (#00ff41)
- **رنگ ثانویه**: آبی (#3aaddf)
- **انیمیشن‌ها**: Smooth transitions
- **Glassmorphism**: backdrop-filter blur

### کامپوننت‌های اصلی

#### دکمه جستجو (Header)
```css
.search-trigger-btn
- Gradient background
- Border نئون
- Hover effects
- Icon + Text
```

#### Overlay تمام صفحه
```css
.search-overlay
- Fixed position
- Backdrop blur
- Smooth fade-in/out
- Scrollable
```

#### Input جستجو
```css
.search-input
- Rounded pill shape
- Gradient background
- Glow effect on focus
```

#### کارت نتایج
```css
.search-result-card
- Grid layout
- Hover animations
- Category badge
- Tags display
```

## 💻 ساختار JSON

### فرمت خروجی
```json
[
  {
    "title": "عنوان مقاله",
    "category": "cyber-security",
    "tags": ["CyberSecurity", "Security"],
    "permalink": "https://example.com/article/",
    "summary": "خلاصه مقاله...",
    "date": "2026/02/08"
  }
]
```

### فیلدها
- **title**: عنوان مقاله (جستجو می‌شود)
- **category**: نام دسته‌بندی
- **tags**: آرایه تگ‌ها (جستجو می‌شود)
- **permalink**: لینک کامل مقاله
- **summary**: خلاصه مقاله (150 کاراکتر)
- **date**: تاریخ انتشار

## 🔧 JavaScript Functions

### توابع اصلی

#### `loadSearchData()`
```javascript
// بارگذاری داده‌های JSON
async function loadSearchData()
```

#### `openSearchOverlay()`
```javascript
// باز کردن Overlay تمام صفحه
function openSearchOverlay()
```

#### `closeSearchOverlay()`
```javascript
// بستن Overlay
function closeSearchOverlay()
```

#### `searchArticles(query, category, inline)`
```javascript
// جستجو در مقالات
function searchArticles(query, category = '', inline = false)
```

#### `displaySearchResults(results, inline)`
```javascript
// نمایش نتایج جستجو
function displaySearchResults(results, inline = false)
```

### Debouncing
```javascript
// جستجو با تأخیر 300ms برای بهینه‌سازی
let searchTimeout;
input.addEventListener('input', function() {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
        searchArticles(this.value);
    }, 300);
});
```

## 📱 Responsive Design

### Desktop (>768px)
- Overlay تمام صفحه
- Grid layout برای نتایج (3 ستون)
- دکمه کامل با Text

### Tablet (768px)
- Grid layout (2 ستون)
- فونت‌های کوچکتر

### Mobile (<768px)
- Grid layout (1 ستون)
- دکمه فقط آیکون
- Input کوچکتر
- Padding کمتر

## ⚙️ تنظیمات Hugo

### در `hugo.toml`
```toml
[outputs]
home = ["HTML", "RSS", "JSON"]
```

این تنظیم باعث می‌شود Hugo فایل `index.json` تولید کند.

## 🎯 نحوه استفاده

### اضافه کردن به Header
```html
<!-- در layouts/partials/header.html -->
{{ partial "search.html" (dict "inline" false) }}
```

### اضافه کردن به Sidebar
```html
<!-- در layouts/partials/sidebar.html -->
{{ partial "search.html" (dict "inline" true) }}
```

### لینک CSS
```html
<!-- در layouts/_default/baseof.html -->
<link rel="stylesheet" href="/assets/css/search.css">
```

## 🔄 Workflow جستجو

```
1. کاربر کلیک روی دکمه جستجو
   ↓
2. Overlay باز می‌شود
   ↓
3. داده‌های JSON بارگذاری می‌شوند (یک‌بار)
   ↓
4. کاربر تایپ می‌کند
   ↓
5. Debounce (300ms)
   ↓
6. جستجو در title و tags
   ↓
7. فیلتر بر اساس category (اختیاری)
   ↓
8. نمایش نتایج
   ↓
9. کلیک روی نتیجه → رفتن به مقاله
```

## 🎨 کلاس‌های CSS اضافه شده

### Header Search
- `.search-trigger-btn` - دکمه جستجو
- `.search-icon` - آیکون
- `.search-overlay` - Overlay تمام صفحه
- `.search-overlay-header` - هدر overlay
- `.search-overlay-title` - عنوان
- `.search-close-btn` - دکمه بستن
- `.search-overlay-content` - محتوای اصلی
- `.search-box-wrapper` - wrapper input
- `.search-input` - input جستجو
- `.search-filters` - فیلترها
- `.search-filter-select` - dropdown دسته‌بندی

### Search Results
- `.search-results-count` - تعداد نتایج
- `.search-results-grid` - Grid نتایج
- `.search-result-card` - کارت هر نتیجه
- `.result-header` - هدر کارت
- `.result-category` - badge دسته‌بندی
- `.result-date` - تاریخ
- `.result-title` - عنوان
- `.result-summary` - خلاصه
- `.result-tags` - container تگ‌ها
- `.result-tag` - badge تگ
- `.result-link` - لینک مشاهده
- `.search-no-results` - پیام عدم نتیجه

### Inline Search (Sidebar)
- `.search-inline-wrapper` - wrapper اصلی
- `.search-box-inline` - box جستجو
- `.search-input-inline` - input
- `.search-icon-inline` - آیکون
- `.search-filter-inline` - dropdown
- `.search-results-inline` - نتایج
- `.search-result-inline` - هر نتیجه
- `.result-title-inline` - عنوان
- `.result-category-inline` - دسته‌بندی

### Loading
- `.search-loading` - container loading
- `.loading-spinner` - چرخشی

## 🐛 عیب‌یابی

### نتایج نمایش داده نمی‌شوند
1. بررسی کنید `/index.json` در دسترس باشد
2. Console browser را برای خطاها بررسی کنید
3. Hugo را با `--cleanDestinationDir` rebuild کنید

### جستجو کار نمی‌کند
1. JavaScript را در Console بررسی کنید
2. مطمئن شوید `index.json` درست تولید شده
3. Cache مرورگر را پاک کنید

### تگ‌ها نمایش داده نمی‌شوند
1. Front matter مقالات را بررسی کنید
2. مطمئن شوید tags در JSON هستند
3. فرمت tags باید array باشد:
   ```yaml
   tags:
     - Tag1
     - Tag2
   ```

### Overlay باز نمی‌شود
1. JavaScript errors را بررسی کنید
2. مطمئن شوید `search.html` در header اضافه شده
3. بررسی کنید `search.css` لود شده

## 🚀 بهینه‌سازی‌ها

### Performance
- ✅ Lazy loading JSON (فقط هنگام نیاز)
- ✅ Debouncing برای کاهش جستجوهای غیرضروری
- ✅ Client-side search (بدون نیاز به سرور)
- ✅ Cache داده‌های JSON

### UX
- ✅ Smooth animations
- ✅ Keyboard shortcuts (ESC)
- ✅ Focus management
- ✅ Click outside to close
- ✅ Real-time results

### Accessibility
- ✅ Semantic HTML
- ✅ Keyboard navigation
- ✅ ARIA labels (قابل اضافه شدن)

## 🔮 ویژگی‌های آینده (قابل توسعه)

- [ ] Fuzzy search (جستجوی تقریبی)
- [ ] Search history (تاریخچه جستجو)
- [ ] Popular searches (جستجوهای محبوب)
- [ ] Advanced filters (فیلتر پیشرفته)
  - [ ] Filter by date range
  - [ ] Filter by author
  - [ ] Sort options
- [ ] Search suggestions (پیشنهادات)
- [ ] Highlight search terms (هایلایت)
- [ ] Voice search (جستجوی صوتی)

## 📊 ساختار کلی

```
┌─────────────────────────────────────────┐
│           Header                        │
│  [Logo]  [Menu]  [🔍 Search Button]    │
└─────────────────────────────────────────┘
         ↓ (Click)
┌─────────────────────────────────────────┐
│  Search Overlay (Full Screen)           │
│  ┌───────────────────────────────────┐  │
│  │ 🔍 جستجو در مقالات         [X]  │  │
│  └───────────────────────────────────┘  │
│  ┌───────────────────────────────────┐  │
│  │ [Search Input...................]  │  │
│  │ [Category Filter ▾]               │  │
│  └───────────────────────────────────┘  │
│  ┌───────────────────────────────────┐  │
│  │ 🎯 X نتیجه یافت شد               │  │
│  ├───────────────────────────────────┤  │
│  │ ┌────────┐ ┌────────┐ ┌────────┐ │  │
│  │ │Result 1│ │Result 2│ │Result 3│ │  │
│  │ │[Tags]  │ │[Tags]  │ │[Tags]  │ │  │
│  │ └────────┘ └────────┘ └────────┘ │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  Sidebar                                │
│  ┌───────────────────────────────────┐  │
│  │ 🔍 جستجو                         │  │
│  │ [Search Input........]            │  │
│  │ [Category Filter ▾]               │  │
│  │ ────────────────────              │  │
│  │ → Result 1 [دسته‌بندی]           │  │
│  │ → Result 2 [دسته‌بندی]           │  │
│  │ → Result 3 [دسته‌بندی]           │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## 📚 منابع

- [Hugo Output Formats](https://gohugo.io/templates/output-formats/)
- [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [Debouncing in JavaScript](https://www.freecodecamp.org/news/javascript-debounce-example/)

---

**نسخه:** 1.0.0  
**تاریخ ایجاد:** 2026-02-08  
**نویسنده:** Davood Yahya

**وضعیت:** ✅ آماده برای استفاده
