# راهنمای رفع مشکل نمایش Sidebar در موبایل

## 📋 شرح مشکل

در نسخه قبلی، در حالت موبایل و تبلت (زیر 1024px):
- **Sidebar** در ابتدای صفحه نمایش داده می‌شد
- **محتوای اصلی** (مقاله یا لیست مقالات) بعد از Sidebar نمایش داده می‌شد
- این ترتیب باعث می‌شد کاربر ابتدا Sidebar را ببیند و برای دسترسی به محتوا باید اسکرول کند

## ✅ راه‌حل پیاده‌سازی شده

### تغییرات CSS

از ویژگی `order` در CSS Flexbox برای تغییر ترتیب نمایش عناصر در موبایل استفاده شده است:

#### 1. حالت دسکتاپ (بالای 1024px)
```css
.main-content-wrapper {
    display: grid;
    grid-template-columns: 350px 1fr;
    gap: 3rem;
}
```

- از Grid Layout استفاده می‌شود
- Sidebar در سمت راست (350px)
- محتوا در سمت چپ (1fr)
- ترتیب طبیعی: Sidebar → محتوا

#### 2. حالت موبایل و تبلت (زیر 1024px)
```css
@media (max-width: 1024px) {
    .main-content-wrapper {
        display: flex;
        flex-direction: column;
    }
    
    .article-wrapper,
    .main-content {
        order: 1; /* محتوا ابتدا */
    }
    
    .sidebar {
        order: 2; /* sidebar بعد از محتوا */
    }
}
```

- از Flexbox با `flex-direction: column` استفاده می‌شود
- با استفاده از `order`، ترتیب نمایش تغییر می‌کند:
  - محتوا (order: 1) → ابتدا
  - Sidebar (order: 2) → بعد

### فایل‌های تغییر یافته

#### `assets/css/main.css`

**قسمت‌های تغییر یافته:**

1. **تعریف اصلی Layout:**
   ```css
   .main-content-wrapper {
       display: grid;
       grid-template-columns: 350px 1fr;
       gap: 3rem;
       align-items: start;
       margin-top: 80px;
   }
   ```

2. **Grid Column برای دسکتاپ:**
   ```css
   @media (min-width: 1025px) {
       .sidebar {
           grid-column: 1; /* سمت راست */
       }
       
       .article-wrapper,
       .main-content {
           grid-column: 2; /* سمت چپ */
       }
   }
   ```

3. **Flexbox برای موبایل (زیر 1024px):**
   ```css
   @media (max-width: 1024px) {
       .main-content-wrapper {
           display: flex;
           flex-direction: column;
       }
       
       .article-wrapper,
       .main-content {
           order: 1;
       }
       
       .sidebar {
           order: 2;
           margin-top: 3rem;
       }
   }
   ```

4. **Sidebar Responsive:**
   ```css
   @media (max-width: 1024px) {
       .sidebar {
           position: static;
           max-height: none;
           margin-top: 3rem;
           order: 2;
       }
   }
   ```

## 📱 نتیجه

### قبل از تغییرات:
```
┌─────────────────┐
│    Sidebar      │  ← ابتدا
├─────────────────┤
│                 │
│   محتوای اصلی   │  ← بعد
│                 │
└─────────────────┘
```

### بعد از تغییرات:
```
┌─────────────────┐
│                 │
│   محتوای اصلی   │  ← ابتدا ✓
│                 │
├─────────────────┤
│    Sidebar      │  ← بعد ✓
└─────────────────┘
```

## 🎯 مزایا

1. **بهبود تجربه کاربری**: کاربر ابتدا محتوای اصلی را می‌بیند
2. **سئوی بهتر**: محتوای اصلی در بالای صفحه قرار دارد
3. **دسترسی سریع‌تر**: نیاز به اسکرول برای دسترسی به محتوا از بین می‌رود
4. **سازگار با استانداردها**: طراحی Mobile-First

## 🧪 تست

برای تست تغییرات:

1. سایت را در مرورگر باز کنید
2. به صفحه یک مقاله بروید (مثلا: `/cyber-security/cryptography/...`)
3. DevTools را باز کنید (F12)
4. به حالت موبایل (Device Toolbar) تغییر دهید
5. بررسی کنید که محتوای مقاله ابتدا و Sidebar بعد نمایش داده می‌شود

همچنین برای صفحات دسته‌بندی (مثلا: `/cyber-security/`):
- لیست مقالات ابتدا
- Pagination بعد از مقالات
- Sidebar در آخر قبل از Footer

## 📌 نکات مهم

1. **عدم تغییر در HTML**: تغییری در فایل‌های HTML نشده و فقط CSS تغییر کرده
2. **Backward Compatible**: در دسکتاپ همچنان از Grid استفاده می‌شود
3. **Performance**: هیچ تاثیر منفی بر Performance ندارد
4. **Browser Support**: تمام مرورگرهای مدرن از Flexbox Order پشتیبانی می‌کنند

## 🔄 تاریخچه

- **تاریخ**: 09 فوریه 2026
- **نسخه**: 1.0.0
- **توسط**: AI Assistant
- **وضعیت**: ✅ تکمیل شده

---

**توجه**: این تغییرات فقط بر روی `assets/css/main.css` اعمال شده‌اند.
