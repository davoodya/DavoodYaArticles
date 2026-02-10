# راهنمای Sidebar - وبسایت Davoodya

## 📋 توضیحات کلی

سایدبار به صفحات زیر اضافه شده است:
- صفحه اصلی (Home Page)
- صفحات دسته‌بندی (Category List Pages)
- صفحات تک مقاله (Single Article Pages)

## 🎯 ویژگی‌های Sidebar

### 1. دسته‌بندی‌های مقالات
- نمایش 5 دسته‌بندی اول به صورت مستقیم
- دسته‌بندی‌های بیشتر در منوی dropdown
- نمایش تعداد مقالات هر دسته‌بندی
- آیکون ▸ برای هر دسته‌بندی
- Badge سبز با تعداد مقالات

### 2. تگ‌های مقالات
- نمایش 8 تگ اول به صورت مستقیم
- تگ‌های بیشتر در منوی dropdown
- نمایش تعداد مقالات هر تگ
- طراحی badge آبی برای تگ‌ها
- قابلیت کلیک و رفتن به صفحه تگ

### 3. نوشته‌های تازه
- نمایش 5 مقاله آخر
- شامل عنوان و تاریخ انتشار
- آیکون 📄 برای هر مقاله
- لینک مستقیم به مقاله
- مرتب‌سازی بر اساس تاریخ (جدیدترین اول)

## 🎨 استایل‌دهی

### رنگ‌ها و طراحی
- پس‌زمینه: gradient از darker-bg به card-bg
- Border: سبز نئون با شفافیت
- عنوان‌ها: سبز نئون با text-shadow
- Hover effects: انیمیشن translateX و تغییر رنگ

### Layout
```css
.main-content-wrapper {
    display: grid;
    grid-template-columns: 1fr 350px;  /* محتوا اصلی | سایدبار */
    gap: 3rem;
}
```

### Sticky Sidebar
```css
.sidebar {
    position: sticky;
    top: 110px;
    max-height: calc(100vh - 130px);
    overflow-y: auto;
}
```

## 📱 Responsive Design

### Desktop (> 1024px)
- سایدبار در سمت چپ (یا راست در RTL)
- عرض ثابت 350px
- sticky position

### Tablet/Mobile (< 1024px)
- سایدبار به زیر محتوا منتقل می‌شود
- عرض 100%
- position: static

## 🔧 ساختار فایل‌ها

### Partial File
```
layouts/partials/sidebar.html
```

### استایل‌ها
استایل‌های sidebar در `assets/css/main.css` اضافه شده:
- Sidebar Styles (خط ~350)
- Category List in Sidebar
- Dropdown Styles
- Tags in Sidebar
- Recent Posts in Sidebar
- Sidebar Responsive

### صفحات استفاده‌کننده
1. `layouts/index.html` - صفحه اصلی
2. `layouts/_default/list.html` - لیست مقالات
3. `layouts/_default/single.html` - تک مقاله

## 💡 نحوه استفاده

### اضافه کردن Sidebar به صفحه جدید
```html
<div class="container">
  <div class="main-content-wrapper">
    <div class="main-content">
      <!-- محتوای اصلی شما -->
    </div>

    {{ partial "sidebar.html" . }}
  </div>
</div>
```

### JavaScript Dropdown
```javascript
function toggleDropdown(type) {
    const dropdown = document.getElementById(type + '-dropdown');
    if (dropdown) {
        dropdown.classList.toggle('active');
    }
}
```

## ⚙️ تنظیمات

### تغییر تعداد آیتم‌های نمایشی

#### دسته‌بندی‌ها
```html
{{ $visibleCount := 5 }}  <!-- تغییر این عدد -->
```

#### تگ‌ها
```html
{{ $visibleTagsCount := 8 }}  <!-- تغییر این عدد -->
```

#### نوشته‌های تازه
```html
{{ $recentPosts = first 5 (sort $recentPosts "Date" "desc") }}
                        <!-- ↑ تغییر این عدد -->
```

## 🐛 رفع مشکلات رایج

### Sidebar نمایش داده نمی‌شود
1. بررسی کنید partial به درستی فراخوانی شده
2. cache مرورگر را پاک کنید (Ctrl + Shift + R)
3. Hugo server را restart کنید

### استایل‌ها اعمال نمی‌شوند
1. فایل CSS را از assets به static کپی کنید:
   ```bash
   copy "assets\css\main.css" "static\assets\css\main.css"
   ```
2. Hugo را rebuild کنید:
   ```bash
   hugo --cleanDestinationDir
   ```

### تگ‌ها نمایش داده نمی‌شوند
- اطمینان حاصل کنید مقالات دارای تگ هستند
- Front matter مقالات را بررسی کنید:
  ```yaml
  ---
  title: "عنوان مقاله"
  tags:
    - CyberSecurity
    - Security
  ---
  ```

## 🎯 بهینه‌سازی‌های انجام شده

### 1. Header
- کاهش ارتفاع header از 70px به حدود 60px
- کاهش padding از 15px به 10px
- کاهش font-size لوگو از 1.8rem به 1.5rem
- کاهش font-size منو از 1.1rem به 1rem

### 2. Body Margin
- افزایش padding-top از 70px به 90px
- حل مشکل overlap با header

### 3. Container
- افزایش max-width از 1200px به 1400px (برای sidebar)
- Layout grid برای main-content و sidebar

## 📊 ساختار Grid

```
┌─────────────────────────────────────────┐
│           Header (Fixed)                │
├──────────────────┬──────────────────────┤
│                  │                      │
│  Main Content    │     Sidebar          │
│  (1fr)           │     (350px)          │
│                  │                      │
│  - Home Grid     │  - دسته‌بندی‌ها      │
│  - Article List  │  - تگ‌ها             │
│  - Single Post   │  - نوشته‌های تازه    │
│                  │                      │
│                  │  [Sticky]            │
│                  │                      │
└──────────────────┴──────────────────────┘
│           Footer                        │
└─────────────────────────────────────────┘
```

## 🎨 کلاس‌های CSS اضافه شده

### Wrapper و Layout
- `.main-content-wrapper` - wrapper اصلی با grid
- `.main-content` - محتوای اصلی

### Sidebar
- `.sidebar` - container سایدبار (sticky)
- `.sidebar-widget` - هر بخش سایدبار
- `.sidebar-widget-title` - عنوان هر widget
- `.sidebar-widget-content` - محتوای widget

### دسته‌بندی‌ها
- `.category-list` - لیست دسته‌بندی‌ها
- `.category-item` - هر آیتم
- `.category-link` - لینک دسته‌بندی
- `.category-icon` - آیکون ▸
- `.category-name` - نام دسته‌بندی
- `.category-badge` - badge تعداد

### Dropdown
- `.dropdown-toggle` - container dropdown
- `.dropdown-btn` - دکمه باز/بسته کردن
- `.dropdown-content` - محتوای dropdown
- `.dropdown-content.active` - حالت باز

### تگ‌ها
- `.tags-container` - container تگ‌ها
- `.tag-badge` - badge هر تگ
- `.tag-count` - تعداد مقالات تگ
- `.tags-dropdown-btn` - دکمه dropdown تگ‌ها
- `.tags-dropdown-content` - محتوای dropdown تگ‌ها

### نوشته‌های تازه
- `.recent-posts-list` - لیست نوشته‌ها
- `.recent-post-item` - هر آیتم
- `.recent-post-link` - لینک مقاله
- `.recent-post-icon` - آیکون 📄
- `.recent-post-info` - اطلاعات مقاله
- `.recent-post-title` - عنوان مقاله
- `.recent-post-date` - تاریخ انتشار

### سایر
- `.no-items` - پیام عدم وجود آیتم

## 🔄 تغییرات آینده (اختیاری)

- [ ] افزودن Search Box به sidebar
- [ ] افزودن Popular Posts
- [ ] افزودن Archives (آرشیو ماهانه)
- [ ] افزودن Social Media Links
- [ ] افزودن Newsletter Subscription
- [ ] افزودن Dark/Light Mode Toggle

## 📚 منابع

- [Hugo Partials](https://gohugo.io/templates/partials/)
- [Hugo Taxonomies](https://gohugo.io/content-management/taxonomies/)
- [CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
- [Sticky Positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/position)

---

**نسخه:** 1.0.0  
**تاریخ ایجاد:** 2026-02-08  
**نویسنده:** Davood Yahya
