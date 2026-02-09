# تاریخچه تغییرات - وبسایت Davoodya

## نسخه 1.2.0 (2026-02-08)

### ✨ ویژگی‌های جدید

#### 1. جابجایی Sidebar به سمت راست
- ✅ Sidebar از سمت چپ به سمت **راست** منتقل شد (مناسب برای زبان فارسی)
- ✅ تغییر Grid Layout از `1fr 350px` به `350px 1fr`
- ✅ جابجایی ترتیب در HTML (sidebar ابتدا، سپس main-content)

#### 2. Pattern Animated برای عناوین صفحات
- ✅ اضافه شدن **Grid Pattern Animated** با تم هکری
- ✅ افکت Binary Code در پس‌زمینه
- ✅ انیمیشن‌های مینیمال و جذاب
- ✅ رنگ‌های سبز و آبی نئون
- ✅ پیاده‌سازی برای:
  - `.page-title` (صفحه اصلی)
  - `.category-title` (صفحات دسته‌بندی)

#### 3. افزایش فاصله بین Header و Body
- ✅ افزایش `padding-top` body از 90px به 80px
- ✅ افزایش `padding` container از 2rem به 3rem
- ✅ فاصله بهتر بین header و محتوا

#### 4. تغییر عنوان صفحه اصلی
- ✅ عنوان از "دسته‌بندی‌ها" به **"دسته‌بندی مقالات"** تغییر کرد

#### 5. بهبود RTL (Right-to-Left)
- ✅ تصحیح جهت انیمیشن‌ها برای RTL
- ✅ تغییر `translateX(-5px)` به `translateX(5px)` در hover effects
- ✅ تغییر `border-left` به `border-right` برای recent-posts
- ✅ تصحیح جهت hover در:
  - دکمه "ادامه مطلب"
  - لینک‌های sidebar
  - نتایج جستجو
  - لینک‌های footer

### 🎨 تغییرات استایل

#### Pattern Animated
```css
/* Grid Pattern با انیمیشن */
background-image: 
    linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px),
    linear-gradient(0deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px),
    linear-gradient(45deg, rgba(58, 173, 223, 0.02) 1px, transparent 1px);
animation: grid-move 20s linear infinite;
```

#### Binary Code Effect
```css
/* کد باینری در پس‌زمینه */
content: '01001000 01100001 01100011 01101011 01100101 01110010...';
animation: binary-fade 8s ease-in-out infinite;
```

### 📁 فایل‌های تغییر یافته

#### CSS Files
- ✅ `assets/css/main.css`
  - Grid layout برای sidebar
  - Pattern animated برای عناوین
  - افزایش padding container
  - تصحیح RTL animations
  
- ✅ `assets/css/search.css`
  - تصحیح RTL برای result hover
  
- ✅ `assets/css/header-footer.css`
  - تصحیح RTL برای footer links

#### HTML Files
- ✅ `layouts/index.html`
  - جابجایی sidebar و main-content
  - تغییر عنوان صفحه
  
- ✅ `layouts/_default/list.html`
  - جابجایی sidebar و main-content
  
- ✅ `layouts/_default/single.html`
  - جابجایی sidebar و main-content

### 🐛 رفع مشکلات

- ✅ مشکل جهت انیمیشن‌ها در RTL
- ✅ مشکل چسبیدگی محتوا به header
- ✅ مشکل قرارگیری sidebar در سمت چپ

### 🎯 بهبودها

- ✅ UX بهتر با sidebar در سمت راست
- ✅ جذابیت بیشتر با pattern animated
- ✅ فضای بهتر بین اجزا
- ✅ RTL کامل و درست

---

## نسخه 1.1.0 (2026-02-08)

### ✨ ویژگی‌های جدید

#### سیستم جستجوی پیشرفته
- ✅ جستجوی AJAX در عنوان و تگ‌ها
- ✅ Overlay تمام صفحه برای header
- ✅ جستجوی inline در sidebar
- ✅ فیلتر دسته‌بندی
- ✅ نمایش تگ‌ها در نتایج
- ✅ Debouncing و بهینه‌سازی

#### Sidebar
- ✅ دسته‌بندی‌های مقالات با dropdown
- ✅ تگ‌های مقالات با dropdown
- ✅ نوشته‌های تازه (5 مقاله آخر)
- ✅ جستجو در sidebar

---

## نسخه 1.0.0 (2026-02-08)

### ✨ ویژگی‌های اولیه

- ✅ طراحی Cyberpunk با تم نئون
- ✅ Header و Footer سفارشی
- ✅ صفحه اصلی با کارت‌های دسته‌بندی
- ✅ صفحات لیست مقالات
- ✅ صفحه تک مقاله با تم Things Obsidian
- ✅ Responsive design
- ✅ RTL support
- ✅ فونت‌های فارسی و لاتین

---

**نویسنده:** Davood Yahya  
**آخرین بروزرسانی:** 2026-02-08
