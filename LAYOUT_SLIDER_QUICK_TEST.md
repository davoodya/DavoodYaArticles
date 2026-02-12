# 🚀 Quick Test Guide - Layout & Slider Fix

## ⚡ تست سریع (5 دقیقه)

### 1️⃣ Start Hugo Server
```bash
hugo server -D
```

### 2️⃣ باز کردن یک مقاله
مثال: `http://localhost:1313/linux/60-commands-hacker-should-know-it/`

### 3️⃣ چک لیست بصری

#### ✅ Layout صحیح:
```
┌─────────────────────────────────────────┐
│           HEADER (هدر سایت)             │
├─────────────────────────────────────────┤
│                                         │
│        عنوان مقاله (وسط چین) ✓         │
│                                         │
├─────────────────────────────────────────┤
│         Badges (مدت، سختی، ...)         │
├─────────────────────────────────────────┤
│        Table of Contents (TOC)          │
├─────────────────────────────────────────┤
│              بدنه مقاله                 │
│            (محتوای اصلی)                │
├─────────────────────────────────────────┤
│             تگ‌های مقاله                │
├─────────────────────────────────────────┤
│       اشتراک‌گذاری شبکه‌های اجتماعی      │
├─────────────────────────────────────────┤
│      دکمه‌های کپی لینک و لینک کوتاه     │
├─────────────────────────────────────────┤
│                                         │
│      🔹 COMMENTS SECTION 🔹             │
│   (در قسمت اصلی - نه در sidebar)       │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│      🔹 ARTICLE SLIDER 🔹               │
│   (مقالات پیشنهادی - Previous/Next)    │
│     [◀] [Card 1] [Card 2] [▶]          │
│          ● ○ ○ ○                        │
│                                         │
├─────────────────────────────────────────┤
│          FOOTER (فوتر سایت)             │
└─────────────────────────────────────────┘
```

---

## 🔍 تست دقیق‌تر

### ✅ عنوان مقاله:
- [ ] وسط‌چین است
- [ ] رنگ سبز (accent-green) دارد
- [ ] font-size مناسب دارد

### ✅ بخش Comments:
- [ ] **در پایین مقاله است (نه در sidebar)**
- [ ] عرض کامل دارد
- [ ] background سبز کمرنگ دارد
- [ ] border بالا و پایین دارد
- [ ] فرم نظرات نمایش داده می‌شود

### ✅ اسلایدر مقالات:
- [ ] **در انتهای صفحه است**
- [ ] 2 کارت نمایش داده می‌شود (Desktop)
- [ ] دکمه Previous کار می‌کند
- [ ] دکمه Next کار می‌کند
- [ ] Dots (●) کار می‌کنند
- [ ] عکس مقالات لود می‌شوند
- [ ] لینک‌ها کار می‌کنند

---

## 📱 تست Responsive

### Desktop (> 1024px):
```bash
# در مرورگر:
F12 → Responsive Design Mode → Desktop (1920x1080)
```
- [ ] 2 کارت در هر ردیف اسلایدر
- [ ] Navigation دکمه‌ها بزرگ
- [ ] عنوان مقاله بزرگ و واضح

### Tablet (768px - 1024px):
```bash
F12 → Responsive Design Mode → Tablet (768x1024)
```
- [ ] 1 کارت در هر ردیف اسلایدر
- [ ] Navigation دکمه‌ها متوسط
- [ ] فرم نظرات 1 ستونی

### Mobile (< 768px):
```bash
F12 → Responsive Design Mode → Mobile (375x667)
```
- [ ] 1 کارت در هر ردیف اسلایدر
- [ ] Touch/Swipe کار می‌کند
- [ ] دکمه‌ها کوچک اما قابل کلیک
- [ ] فرم نظرات کاملاً واکنش‌گرا

---

## 🐛 اگر مشکلی دیدید:

### مشکل 1: اسلایدر کار نمی‌کند
```bash
# 1. Check Console (F12)
console → بررسی خطا

# 2. Check Network
Network → بررسی لود شدن article-slider.js

# 3. Hard Refresh
Ctrl + Shift + R
```

### مشکل 2: Comments در sidebar است
```bash
# 1. Clear cache
Ctrl + Shift + Delete

# 2. Restart Hugo
Ctrl + C
hugo server -D --disableFastRender

# 3. Hard Refresh
Ctrl + Shift + R
```

### مشکل 3: عنوان وسط‌چین نیست
```bash
# 1. Check Inspector (F12)
Elements → Find <h1 class="article-title">
بررسی کنید style="text-align: center;" وجود دارد

# 2. اگر نبود، در CSS اضافه کنید:
.article-title {
    text-align: center;
}
```

---

## 🎯 تست Navigation اسلایدر

### Test Case 1: کلیک روی Next
```
1. باز کردن مقاله
2. Scroll به پایین (اسلایدر)
3. کلیک روی دکمه Next (▶)
4. باید کارت بعدی نمایش داده شود
```
**Result:** ✅ Pass / ❌ Fail

### Test Case 2: کلیک روی Dots
```
1. کلیک روی Dot دوم (○)
2. باید به کارت دوم برود
3. Dot فعال تغییر می‌کند (● → ○)
```
**Result:** ✅ Pass / ❌ Fail

### Test Case 3: Touch/Swipe (Mobile)
```
1. Resize به Mobile
2. Swipe چپ روی اسلایدر
3. باید کارت بعدی نمایش داده شود
```
**Result:** ✅ Pass / ❌ Fail

### Test Case 4: Keyboard Navigation
```
1. Focus روی اسلایدر
2. فشار دادن Arrow Keys
3. باید navigation کند
```
**Result:** ✅ Pass / ❌ Fail

---

## 🎨 تست بصری CSS

### Comments Section:
```css
/* باید این استایل‌ها را ببینید: */
background: rgba(0, 255, 65, 0.02);
border-top: 2px solid rgba(0, 255, 65, 0.15);
border-bottom: 2px solid rgba(0, 255, 65, 0.15);
max-width: 1200px;
padding: 2rem;
```

### Article Slider:
```css
/* باید این استایل‌ها را ببینید: */
background: linear-gradient(135deg, rgba(0, 255, 65, 0.02) 0%, rgba(58, 173, 223, 0.02) 100%);
border-top: 2px solid rgba(58, 173, 223, 0.15);
border-bottom: 2px solid rgba(58, 173, 223, 0.15);
max-width: 1200px;
padding: 3rem 2rem;
```

---

## 🚦 نتیجه تست

### مثال گزارش:
```
✅ عنوان مقاله - وسط‌چین است
✅ Comments - در قسمت اصلی است
✅ Slider - کار می‌کند
✅ Navigation - دکمه‌ها فعال هستند
✅ Dots - کار می‌کنند
✅ Touch - Swipe کار می‌کند
✅ Responsive - همه سایزها OK
```

---

## 📊 Performance Check

### Lighthouse Test:
```bash
# 1. باز کردن DevTools (F12)
# 2. Lighthouse tab
# 3. Generate Report
# 4. بررسی:
   - Performance > 90
   - Accessibility > 90
   - Best Practices > 90
   - SEO > 90
```

### بررسی Load Time:
```bash
# Network tab → Reload page
# بررسی:
   - article-slider.js loaded? ✅
   - article-slider.css loaded? ✅
   - comments.css loaded? ✅
   - Total Load Time < 3s? ✅
```

---

## ✨ Extra Tests

### Test 1: عکس‌های اسلایدر
- [ ] عکس‌ها لود می‌شوند
- [ ] Alt text دارند
- [ ] Lazy loading کار می‌کند
- [ ] Hover effect کار می‌کند

### Test 2: لینک‌های اسلایدر
- [ ] کلیک روی عنوان کارت
- [ ] کلیک روی عکس
- [ ] کلیک روی "مشاهده مطلب"
- [ ] همه به صفحه صحیح می‌روند

### Test 3: فرم نظرات
- [ ] فیلدها قابل کلیک هستند
- [ ] Validation کار می‌کند
- [ ] دکمه Submit فعال است
- [ ] پیام خطا/موفقیت نمایش داده می‌شود

---

## 🔗 لینک‌های مفید

- [مستندات کامل](LAYOUT_AND_SLIDER_FIX_COMPLETE.md)
- [فایل تست HTML](test-slider-fix.html)
- [Article Slider CSS](assets/css/article-slider.css)
- [Comments CSS](assets/css/comments.css)

---

## ⏱️ زمان تست: 5 دقیقه

**Date:** 2026-02-12  
**Status:** Ready for Testing ✅

---

💡 **نکته:** اگر همه تست‌ها Pass شد، یعنی همه چیز کامل کار می‌کند! 🎉
