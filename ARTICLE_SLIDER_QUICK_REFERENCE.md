# ⚡ Article Slider V2 - Quick Reference

## 🎯 خلاصه سریع

```
نسخه: 2.0.0
تعداد مقالات: 6
شروع: از وسط
Navigation: Loop (حلقه‌ای)
Dots: Clickable (قابل کلیک)
```

---

## ✅ ویژگی‌های اصلی

| ویژگی | توضیح |
|-------|-------|
| **تعداد مقالات** | 6 مقاله (از دسته فعلی + Random) |
| **صفحات** | Desktop: 3 صفحه، Mobile: 6 صفحه |
| **شروع** | از صفحه میانی |
| **Loop** | آخر → اول، اول → آخر |
| **Dots** | هر Dot = یک صفحه |
| **Touch** | Swipe با Loop |

---

## 🔄 Navigation

```
[صفحه 1] [صفحه 2] [صفحه 3]
    ↓         ↑         ↓
    ←────────┼────────→
    Loop     Start    Loop
```

### کلید‌ها:
- **Next (◀):** صفحه بعد (با Loop)
- **Prev (▶):** صفحه قبل (با Loop)
- **Dots (●):** کلیک برای رفتن به صفحه
- **Arrow Keys:** ← → (با Loop)
- **Touch:** Swipe چپ/راست (با Loop)

---

## 📊 Layout

### Desktop (> 1024px):
```
┌────────────────────────────┐
│  [Card 1]    [Card 2]      │  ← صفحه 1
├────────────────────────────┤
│  [Card 3]    [Card 4]      │  ← صفحه 2 ● (شروع)
├────────────────────────────┤
│  [Card 5]    [Card 6]      │  ← صفحه 3
└────────────────────────────┘
         ○ ● ○
```

### Mobile (< 1024px):
```
┌──────────────┐
│  [Card 1]    │  ← صفحه 1
│  [Card 2]    │  ← صفحه 2
│  [Card 3]    │  ← صفحه 3 ● (شروع)
│  [Card 4]    │  ← صفحه 4
│  [Card 5]    │  ← صفحه 5
│  [Card 6]    │  ← صفحه 6
└──────────────┘
  ○ ○ ● ○ ○ ○
```

---

## 🧪 تست سریع (2 دقیقه)

### 1. تعداد مقالات:
```bash
✓ باز کردن مقاله
✓ Scroll به اسلایدر
✓ شمارش Dots: Desktop=3, Mobile=6
```

### 2. شروع از وسط:
```bash
✓ Dot وسطی فعال است؟ ●
```

### 3. Loop Navigation:
```bash
✓ Next → Next → Next → صفحه 1؟
✓ Prev → Prev → Prev → صفحه آخر؟
```

### 4. Dots Click:
```bash
✓ کلیک Dot اول → صفحه اول؟
✓ کلیک Dot آخر → صفحه آخر؟
```

### 5. Touch:
```bash
✓ Swipe چپ → صفحه بعد؟
✓ Swipe راست → صفحه قبل؟
✓ از آخر Swipe → Loop به اول؟
```

---

## 🐛 Debug Commands

### Console:
```javascript
// وضعیت فعلی
articleSlider.getCurrentPage()  // → 1 (صفحه میانی)

// تعداد صفحات
articleSlider.getTotalPages()   // → 3 (Desktop)

// رفتن به صفحه
articleSlider.goToPage(0)       // صفحه اول
articleSlider.goToPage(2)       // صفحه آخر

// Navigation
articleSlider.nextPage()        // صفحه بعد (با Loop)
articleSlider.prevPage()        // صفحه قبل (با Loop)
```

---

## 🔧 Config

### تغییر تعداد مقالات:
```go
// در article-slider.html
{{ $targetCount := 6 }}  ← تغییر به 8, 10, etc.
```

### تغییر صفحه شروع:
```javascript
// در article-slider.js → startFromMiddle()
const middlePage = Math.floor(totalPages / 2);  // میانی
// یا:
const middlePage = 0;  // اول
const middlePage = totalPages - 1;  // آخر
```

### غیرفعال کردن Loop:
```javascript
// در article-slider.js → goToPage()
if (pageIndex < 0) {
    currentPage = 0;  // بجای: totalPages - 1
} else if (pageIndex >= totalPages) {
    currentPage = totalPages - 1;  // بجای: 0
}
```

---

## 📱 Responsive

| Breakpoint | Cards/Page | Total Pages | Dots |
|------------|-----------|-------------|------|
| Desktop (> 1024px) | 2 | 3 | 3 |
| Tablet (768-1024px) | 1 | 6 | 6 |
| Mobile (< 768px) | 1 | 6 | 6 |

---

## 🎨 Styling

### Dots:
```css
/* رنگ عادی */
background: rgba(58, 173, 223, 0.2);

/* رنگ فعال */
background: var(--accent-green);
box-shadow: 0 0 12px rgba(0, 255, 65, 0.6);

/* Hover */
transform: scale(1.3);
```

### Transitions:
```css
/* Navigation */
transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);

/* Dots */
transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
```

---

## 🔍 Troubleshooting

### مشکل: اسلایدر کار نمی‌کند
```bash
✓ Check Console: article-slider.js loaded?
✓ Check Network: 200 OK?
✓ Hard Refresh: Ctrl+Shift+R
```

### مشکل: Dots کار نمی‌کنند
```bash
✓ Check: data-page attribute موجود است؟
✓ Check: Event listeners اضافه شدند؟
✓ Console: articleSlider object موجود است؟
```

### مشکل: Loop کار نمی‌کند
```bash
✓ Check: goToPage() با if/else درست است؟
✓ Check: nextPage/prevPage صدا زده می‌شوند؟
✓ Console: totalPages چند است؟
```

### مشکل: شروع از وسط نیست
```bash
✓ Check: startFromMiddle() صدا زده می‌شود؟
✓ Check: currentPage بعد از init چند است؟
✓ Console: articleSlider.getCurrentPage()
```

---

## 📂 Files

```
layouts/partials/article-slider.html     ← 6 articles logic
static/assets/js/article-slider.js       ← Loop + Middle start + Dots
assets/js/article-slider.js              ← Copy of above
assets/css/article-slider.css            ← Dots styling
```

---

## 🚀 Performance

```
JavaScript: ~8KB (minified)
CSS: ~10KB (minified)
Images: Lazy loaded (except first 2)
Animations: Hardware accelerated
Touch: Passive listeners
Resize: Debounced (250ms)
```

---

## ✨ Features

```
✅ 6 مقاله (دسته فعلی + Random)
✅ شروع از وسط
✅ Loop navigation (حلقه‌ای)
✅ Dots clickable
✅ Touch/Swipe با Loop
✅ Keyboard navigation
✅ Responsive (Desktop/Tablet/Mobile)
✅ Accessibility (ARIA labels)
✅ Performance optimized
✅ Debug commands
```

---

## 📞 Quick Help

```
مشکل دارید؟
1. Check Console (F12)
2. Check ARTICLE_SLIDER_V2_COMPLETE.md
3. Use debug commands
4. Test in different browsers
```

---

## 🎯 Status

**✅ READY**

```
Version: 2.0.0
Status: Production Ready
Last Updated: 2026-02-12
```

---

**💡 Tip:** برای تست سریع، از Console commands استفاده کنید!

```javascript
// Example:
articleSlider.getCurrentPage()  // چه صفحه‌ای فعال است؟
articleSlider.nextPage()        // صفحه بعد
articleSlider.prevPage()        // صفحه قبل
```

---

🚀 **همه چیز آماده است!**
