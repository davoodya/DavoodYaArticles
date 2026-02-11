# Left Sidebar Implementation - Three Column Layout

**تاریخ:** 2026-02-11  
**وضعیت:** ✅ تکمیل شده و تست شده

---

## 🎯 هدف

ایجاد سیستم Three-Column Layout با:
- **Left Sidebar:** نمایش Taxonomy Filters (Difficulty, Content Types, Lab Required)
- **Main Content:** محتوای اصلی
- **Right Sidebar:** ابزارهای جستجو، دسته‌بندی‌ها، تگ‌ها و ...

---

## 📋 تغییرات اعمال شده

### 1. حذف Category Cards از Home Page

**قبل:**
- Taxonomy sections (difficulty, lab_required, type) به صورت Category Card نمایش داده می‌شدند

**بعد:**
- فقط Content Sections واقعی (cyber-security, linux, network, ...) نمایش داده می‌شوند
- Taxonomy sections به Left Sidebar منتقل شدند

**فایل‌های تغییر یافته:**
- `layouts/index.html`
- `layouts/partials/sidebar.html`

---

## 🏗️ معماری سیستم

### Component Structure

```
layouts/
├── partials/
│   ├── sidebar-left.html    (جدید - Left Sidebar)
│   └── sidebar.html          (موجود - Right Sidebar)
├── index.html                (به‌روز شده)
├── _default/
│   ├── list.html             (به‌روز شده)
│   └── all-articles.html     (به‌روز شده)
└── taxonomy/
    └── single.html           (به‌روز شده)

assets/css/
└── main.css                  (CSS جدید برای Three-Column Layout)
```

---

## 📄 فایل‌های پیاده‌سازی شده

### 1. Left Sidebar Component

**فایل:** `layouts/partials/sidebar-left.html`

**ویژگی‌ها:**
- ✅ خواندن داده از Registry (`data/taxonomies.json`)
- ✅ سه Widget مجزا:
  - 📊 سطح دشواری (Difficulty)
  - 📄 نوع مطالب (Content Types)
  - 🔬 نیاز به آزمایشگاه (Lab Required)
- ✅ Active State Detection (بر اساس URL فعلی)
- ✅ ترتیب دقیق Options طبق راهنما
- ✅ Mapping فارسی به انگلیسی برای post_type_fa

**ساختار کلی:**
```html
<aside class="sidebar sidebar-left">
  <div class="sidebar-widget">
    <h3 class="sidebar-widget-title">📊 سطح دشواری</h3>
    <div class="sidebar-widget-content">
      <ul class="widget-list">
        <li class="widget-item [active]">
          <a href="/difficulty/beginner/" class="widget-link">
            <span class="widget-icon">▸</span>
            <span class="widget-text">سطح دشواری مبتدی</span>
          </a>
        </li>
        <!-- ... -->
      </ul>
    </div>
  </div>
  <!-- Widget 2: نوع مطالب -->
  <!-- Widget 3: نیاز به آزمایشگاه -->
</aside>
```

### 2. Widget Options

#### Widget 1: سطح دشواری

**ترتیب:**
1. سطح دشواری مبتدی → `/difficulty/beginner/`
2. سطح دشواری متوسط → `/difficulty/medium/`
3. سطح دشواری حرفه‌ای → `/difficulty/intermediate/`
4. سطح دشواری تخصصی → `/difficulty/advanced/`

**پیاده‌سازی:**
```go
{{ $values := slice "beginner" "medium" "intermediate" "advanced" }}
{{ range $values }}
  {{ $label := index $labels . }}
  {{ $url := printf "/%s/%s/" $slug . }}
  <!-- ... -->
{{ end }}
```

#### Widget 2: نوع مطالب

**ترتیب:**
1. مطالب مقاله → `/type/article/`
2. مطالب آموزشی → `/type/tutorial/`
3. مطالب دستور العمل → `/type/howto/`
4. مطالب ابزار → `/type/tool/`
5. مطالب اسکریپت → `/type/script/`
6. مطالب خبر → `/type/news/`
7. مطالب معرفی → `/type/intro/`

**پیاده‌سازی:**
```go
{{ $orderedTypes := slice "مقاله" "آموزشی" "دستور العمل" "ابزار" "اسکریپت" "خبر" "معرفی" }}
{{ range $orderedTypes }}
  {{ $enValue := index $mapping . }}
  {{ $url := printf "/%s/%s/" $slug $enValue }}
  <!-- ... -->
{{ end }}
```

#### Widget 3: نیاز به آزمایشگاه

**ترتیب:**
1. مطالب نیازمند تمرین عملی → `/lab_required/true/`
2. مطالب بدون نیاز به آزمایشگاه → `/lab_required/false/`

**پیاده‌سازی:**
```go
{{ $orderedValues := slice "true" "false" }}
{{ range $orderedValues }}
  {{ $label := index $labels . }}
  {{ $url := printf "/%s/%s/" $slug . }}
  <!-- ... -->
{{ end }}
```

---

## 🎨 طراحی و استایل

### CSS Classes

**Left Sidebar:**
- `.sidebar-left` - Container اصلی
- `.sidebar-widget` - هر Widget
- `.sidebar-widget-title` - عنوان Widget
- `.widget-list` - لیست لینک‌ها
- `.widget-item` - هر Item
- `.widget-link` - لینک
- `.widget-icon` - آیکون
- `.widget-text` - متن لینک
- `.widget-item.active` - Active State

### استایل مشابه Right Sidebar

**ویژگی‌های مشترک:**
- Border Radius: `12px`
- Background: `rgba(15, 15, 15, 0.95)`
- Border: `1px solid rgba(0, 255, 65, 0.2)`
- Padding: `1.5rem`
- Box Shadow: `0 4px 20px rgba(0, 0, 0, 0.5)`
- Backdrop Filter: `blur(10px)`

### Hover Effects

```css
.sidebar-left .widget-link:hover {
    background: rgba(0, 255, 65, 0.05);
    color: var(--accent-green);
    border-color: rgba(0, 255, 65, 0.2);
    transform: translateX(-3px);
}

.sidebar-left .widget-link:hover .widget-icon {
    transform: translateX(3px);
}
```

### Active State

```css
.sidebar-left .widget-item.active .widget-link {
    background: rgba(0, 255, 65, 0.1);
    color: var(--accent-green);
    border-color: var(--accent-green);
    font-weight: 600;
    box-shadow: 0 0 10px rgba(0, 255, 65, 0.2);
}
```

---

## 📐 Three-Column Layout

### Desktop Layout (> 1024px)

```
┌───────────────────────────────────────────────────────┐
│                       Header                          │
├──────────────┬──────────────────┬─────────────────────┤
│              │                  │                     │
│  Left        │   Main Content   │   Right Sidebar    │
│  Sidebar     │                  │                     │
│  (280px)     │   (Flexible)     │   (350px)          │
│              │                  │                     │
│  - Difficulty│   - Articles     │   - Search         │
│  - Types     │   - Categories   │   - Categories     │
│  - Lab Req   │   - Content      │   - Tags           │
│              │                  │   - Recent Posts   │
│              │                  │                     │
└──────────────┴──────────────────┴─────────────────────┘
```

**Grid Template:**
```css
grid-template-columns: 280px 1fr 350px;
gap: 2rem;
```

### Tablet Layout (768px - 1024px)

```
┌───────────────────────────────────────────┐
│              Header                       │
├───────────────────────────────────────────┤
│                                           │
│          Main Content                     │
│                                           │
├───────────────────────────────────────────┤
│                                           │
│          Right Sidebar                    │
│                                           │
├───────────────────────────────────────────┤
│                                           │
│          Left Sidebar                     │
│                                           │
└───────────────────────────────────────────┘
```

**Order:**
1. Main Content
2. Right Sidebar
3. Left Sidebar

### Mobile Layout (< 768px)

```
┌─────────────────────────┐
│        Header           │
├─────────────────────────┤
│                         │
│     Main Content        │
│                         │
├─────────────────────────┤
│                         │
│    Right Sidebar        │
│                         │
├─────────────────────────┤
│                         │
│    Left Sidebar         │
│                         │
└─────────────────────────┘
```

**Flex Direction:** Column

---

## 🔄 Active State Logic

### نحوه عملکرد

```go
{{ $currentPath := .RelPermalink }}
{{ $url := printf "/%s/%s/" $slug $value }}
{{ $isActive := eq $currentPath $url }}

<li class="widget-item{{ if $isActive }} active{{ end }}">
```

### مثال‌ها

**صفحه فعلی:** `/difficulty/medium/`

**نتیجه:**
- ✅ "سطح دشواری متوسط" → `class="widget-item active"`
- ❌ سایر موارد → `class="widget-item"`

---

## 📱 Responsive Behavior

### Desktop (> 1024px)
- ✅ Three columns visible
- ✅ Left Sidebar sticky
- ✅ Grid layout

### Tablet (768px - 1024px)
- ✅ Single column
- ✅ Order: Content → Right Sidebar → Left Sidebar
- ✅ Sidebars full width

### Mobile (< 768px)
- ✅ Flex column
- ✅ Reduced padding
- ✅ Smaller fonts
- ✅ Order: Content → Right Sidebar → Left Sidebar

---

## 📋 فایل‌های تغییر یافته

### 1. Templates

| فایل | تغییرات | وضعیت |
|------|---------|--------|
| `layouts/partials/sidebar-left.html` | ایجاد جدید | ✅ |
| `layouts/index.html` | اضافه کردن left sidebar + فیلتر sections | ✅ |
| `layouts/_default/list.html` | اضافه کردن left sidebar | ✅ |
| `layouts/_default/all-articles.html` | اضافه کردن left sidebar | ✅ |
| `layouts/taxonomy/single.html` | اضافه کردن left sidebar | ✅ |
| `layouts/partials/sidebar.html` | فیلتر sections در categories | ✅ |

### 2. Styles

| فایل | تغییرات | وضعیت |
|------|---------|--------|
| `assets/css/main.css` | افزودن CSS برای three-column layout | ✅ |

**تعداد خطوط اضافه شده:** ~300 خط CSS

---

## ✅ معیارهای پذیرش

### Checklist کامل

- [x] **Category Card از Home حذف شده**
  - ✅ difficulty, lab_required, type از index.html حذف شدند
  - ✅ فقط content sections نمایش داده می‌شوند

- [x] **Left Sidebar اضافه شده**
  - ✅ Component مستقل ایجاد شده
  - ✅ در صفحات مشخص شده نمایش داده می‌شود

- [x] **ترتیب Options دقیق رعایت شده**
  - ✅ Difficulty: beginner → medium → intermediate → advanced
  - ✅ Types: مقاله → آموزشی → دستور العمل → ابزار → اسکریپت → خبر → معرفی
  - ✅ Lab Required: true → false

- [x] **لینک‌ها درست کار می‌کنند**
  - ✅ تمام لینک‌ها به صفحات taxonomy صحیح منتقل می‌شوند
  - ✅ URL‌ها تمیز و SEO-friendly

- [x] **Active state فعال است**
  - ✅ در صفحات taxonomy مربوطه active class اضافه می‌شود
  - ✅ استایل active state به درستی اعمال می‌شود

- [x] **Responsive behavior صحیح است**
  - ✅ Desktop: Three columns
  - ✅ Tablet: Single column با order صحیح
  - ✅ Mobile: Flex column

- [x] **طراحی هماهنگ با Right Sidebar**
  - ✅ Border radius یکسان
  - ✅ Colors مشابه
  - ✅ Hover effects یکسان
  - ✅ Typography هماهنگ

- [x] **فقط در صفحات موردنظر نمایش داده می‌شود**
  - ✅ Home page
  - ✅ List pages (content sections)
  - ✅ All articles page
  - ✅ Taxonomy pages
  - ❌ Single article pages (به درستی مخفی است)

---

## 🧪 تست‌های انجام شده

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
- ✅ Left sidebar render شده
- ✅ Right sidebar render شده
- ✅ Three-column layout اعمال شده
- ✅ Taxonomy sections از category cards حذف شدند

**Taxonomy Page (/difficulty/medium/):**
- ✅ Left sidebar با active state
- ✅ "سطح دشواری متوسط" دارای class="widget-item active"

### 3. CSS Validation

- ✅ استایل‌های Left Sidebar اعمال شده
- ✅ Responsive breakpoints کار می‌کنند
- ✅ Hover effects اعمال شده
- ✅ Active state styling صحیح است

---

## 🚀 نتیجه‌گیری

سیستم Three-Column Layout با موفقیت پیاده‌سازی شده و تمام معیارهای پذیرش برآورده شده‌اند.

### نکات مهم:

1. **Reusable Component:** Left sidebar یک component مستقل است
2. **Registry-Based:** همه داده‌ها از `data/taxonomies.json` خوانده می‌شوند
3. **SEO-Friendly:** تمام لینک‌ها واقعی و follow هستند
4. **Accessible:** ساختار semantic HTML
5. **Responsive:** طراحی کاملاً responsive
6. **Maintainable:** کد تمیز و قابل نگهداری

### آماده برای Production ✅

---

**پیاده‌سازی شده توسط:** AI Assistant  
**تاریخ:** 2026-02-11  
**وضعیت نهایی:** ✅ **تکمیل شده و تست شده**
