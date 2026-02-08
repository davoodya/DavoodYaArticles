# 🔧 اصلاح Summary و Direction Detection

> **تاریخ**: 2026-02-08  
> **نسخه**: 2.3

---

## 📋 تغییرات اعمال شده

### 1. برگشت به نمایش TOC در توضیحات کوتاه
### 2. اصلاح تشخیص LTR/RTL در لیست‌های تو در تو

---

## 1. 📝 نمایش TOC در توضیحات کوتاه

### مشکل قبلی:
در نسخه قبل، TOC و همه متن‌های لیست حذف می‌شدند و فقط اولین پاراگراف واقعی نمایش داده می‌شد.

### راه‌حل جدید:
- **TOC نمایش داده می‌شود** (برای قابلیت کلیک در آینده)
- **تصاویر مخفی می‌شوند** (با CSS)
- **متن اصلی حفظ می‌شود**

### کد قبلی (حذف شد):

```javascript
function processArticleCards() {
    // Extract first paragraph
    const firstPara = extractFirstParagraph(originalText);
    if (firstPara && firstPara.length > 50) {
        card.textContent = firstPara;  // ❌ جایگزین می‌کرد
    }
}
```

### کد جدید:

```javascript
function processArticleCards() {
    document.querySelectorAll('.article-card-summary').forEach(card => {
        if (card.getAttribute('data-processed')) return;
        
        // Hide images with CSS (but keep TOC and text)
        card.querySelectorAll('img').forEach(img => {
            img.style.display = 'none';  // ✅ فقط مخفی می‌کند
        });
        
        card.setAttribute('data-processed', 'true');
    });
}
```

### نتیجه:

**قبل:**
```
توضیحات کوتاه:
امنیت شبکه مجموعه‌ای از تکنولوژی‌ها...
```

**بعد:**
```
توضیحات کوتاه:
## E6 to E9 - (Find Keywords, Website Structure...)
- [Find Keywords](#Find%20Keywords)
  - [Google Ads](#Google%20Ads)
  - [Competitor's](#Competitor's)
- [Website Structure](#Website%20Structure)
...
```

### مزایا:
- ✅ TOC قابل کلیک (در آینده)
- ✅ ساختار محتوا نمایش داده می‌شود
- ✅ تصاویر همچنان مخفی هستند
- ✅ کاربر می‌تواند ساختار مقاله را ببیند

---

## 2. 🔄 اصلاح تشخیص Direction در لیست‌های تو در تو

### مشکل:

لیست‌های تو در تو با محتوای مخلوط (انگلیسی و فارسی) direction اشتباه داشتند:

```markdown
2. Patching                         ← ✅ LTR (درست)
3. Logical Isolation                ← ✅ LTR (درست)
4. Guest & Host OS                  ← ❌ RTL (اشتباه - باید LTR بود)
    1. موارد امن سازی را...        ← ✅ RTL (درست)
5. Physical Isolation               ← ❌ RTL (اشتباه - باید LTR بود)
    1. استفاده از سخت افزار...     ← ✅ RTL (درست)
```

### علت:

تابع `setAutoDirection` تمام متن element را چک می‌کرد (شامل nested lists):

```javascript
// ❌ کد قبلی
function setAutoDirection(element) {
    const text = element.textContent;  // شامل متن nested lists
    
    if (startsWithPersian(text)) {
        // آیتم 4 و 5 به اشتباه RTL می‌شدند
        // چون nested list فارسی دارند
    }
}
```

### راه‌حل:

فقط **متن سطح اول** element را چک کنید (بدون nested elements):

```javascript
/**
 * Get first meaningful text from element (skip child elements)
 */
function getFirstLevelText(element) {
    let text = '';
    for (let node of element.childNodes) {
        if (node.nodeType === Node.TEXT_NODE) {
            text += node.textContent;
        }
    }
    return text.trim();
}

/**
 * Set direction for an element
 */
function setAutoDirection(element) {
    if (!element || element.getAttribute('data-dir-set')) return;
    
    // For list items, only check the first level text (not nested lists)
    let text;
    if (element.tagName === 'LI') {
        text = getFirstLevelText(element);  // ✅ فقط سطح اول
        // If no first-level text, fallback to full text
        if (!text || text.length < 5) {
            text = element.textContent || element.innerText || '';
        }
    } else {
        text = element.textContent || element.innerText || '';
    }
    
    if (startsWithPersian(text)) {
        element.style.direction = 'rtl';
        element.style.textAlign = 'right';
        element.setAttribute('dir', 'rtl');
    } else if (isEnglishText(text)) {
        element.style.direction = 'ltr';
        element.style.textAlign = 'left';
        element.setAttribute('dir', 'ltr');
        element.setAttribute('lang', 'en');
    }
    
    element.setAttribute('data-dir-set', 'true');
}
```

### نتیجه:

```markdown
2. Patching                         ← ✅ LTR (درست)
3. Logical Isolation                ← ✅ LTR (درست)
4. Guest & Host OS                  ← ✅ LTR (حل شد!)
    1. موارد امن سازی را...        ← ✅ RTL (درست)
5. Physical Isolation               ← ✅ LTR (حل شد!)
    1. استفاده از سخت افزار...     ← ✅ RTL (درست)
```

### نحوه کار:

#### ساختار HTML:

```html
<ol>
  <li>
    "Guest & Host OS"          ← متن سطح اول (انگلیسی)
    <ol>
      <li>موارد امن سازی...</li>  ← nested list (فارسی)
    </ol>
  </li>
</ol>
```

#### چک شدن Direction:

```javascript
// برای <li> با "Guest & Host OS"
const firstLevelText = getFirstLevelText(li);  // "Guest & Host OS"
// Nested list ("موارد امن سازی...") نادیده گرفته می‌شود

if (isEnglishText("Guest & Host OS")) {
    li.style.direction = 'ltr';  // ✅ LTR
}

// برای nested <li> با "موارد امن سازی..."
const nestedText = getFirstLevelText(nestedLi);  // "موارد امن سازی..."

if (startsWithPersian("موارد امن سازی...")) {
    nestedLi.style.direction = 'rtl';  // ✅ RTL
}
```

---

## 📊 مقایسه Before/After

### Before:

```javascript
// ❌ مشکلات:
1. TOC حذف می‌شد از summary
2. لیست‌های تو در تو direction اشتباه داشتند
3. فقط اولین پاراگراف نمایش داده می‌شد
```

### After:

```javascript
// ✅ حل شده:
1. TOC نمایش داده می‌شود (قابل کلیک در آینده)
2. لیست‌های تو در تو direction صحیح دارند
3. تمام محتوا نمایش داده می‌شود (بدون تصویر)
```

---

## 🧪 تست

### تست 1: TOC در Summary

```bash
# باز کردن صفحه دسته‌بندی
http://localhost:1313/articles/seo/

# انتظار:
✓ TOC نمایش داده شود
✓ تصاویر مخفی باشند
✓ ساختار مقاله قابل مشاهده باشد
```

---

### تست 2: لیست‌های تو در تو

```bash
# باز کردن مقاله‌ای با لیست تو در تو
http://localhost:1313/articles/cyber-security/...

# انتظار:
✓ آیتم‌های انگلیسی: LTR
✓ آیتم‌های فارسی: RTL
✓ nested lists مستقل از parent
```

---

## 🔍 تست دستی

### HTML تست:

```html
<ol>
  <li>Patching</li>
  <li>Logical Isolation</li>
  <li>Guest & Host OS
    <ol>
      <li>موارد امن سازی را در سیستم عامل Guest & Host انجام دهید.</li>
    </ol>
  </li>
  <li>Physical Isolation
    <ol>
      <li>استفاده از سخت افزار های مجزا...</li>
    </ol>
  </li>
</ol>
```

### انتظار:

```
✓ "Patching" → LTR
✓ "Logical Isolation" → LTR
✓ "Guest & Host OS" → LTR (parent)
  ✓ "موارد امن سازی..." → RTL (nested)
✓ "Physical Isolation" → LTR (parent)
  ✓ "استفاده از..." → RTL (nested)
```

---

## 📝 نکات مهم

### 1. Node Types در JavaScript:

```javascript
Node.TEXT_NODE === 3     // متن معمولی
Node.ELEMENT_NODE === 1  // المان HTML (مثل <ol>, <li>)
```

### 2. تفاوت `textContent` و `getFirstLevelText()`:

```javascript
// <li>Text <ol><li>Nested</li></ol></li>

element.textContent  // "Text Nested" (همه)
getFirstLevelText(element)  // "Text" (فقط سطح اول)
```

### 3. Fallback:

اگر متن سطح اول کمتر از 5 کاراکتر باشد، از تمام متن استفاده می‌شود:

```javascript
if (!text || text.length < 5) {
    text = element.textContent;  // fallback
}
```

---

## ✅ چک‌لیست

- [x] TOC در summary نمایش داده می‌شود
- [x] تصاویر در summary مخفی هستند
- [x] لیست‌های parent انگلیسی: LTR
- [x] لیست‌های nested فارسی: RTL
- [x] بدون re-processing (با data-dir-set)
- [x] کد تمیز و documented
- [x] تست شده در مرورگرها مختلف

---

## 🚀 ویژگی‌های آینده

### 1. کلیک روی TOC در Summary:

```javascript
// در آینده اضافه می‌شود
document.querySelectorAll('.article-card-summary a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        // Navigate to article + scroll to section
    });
});
```

### 2. Highlight کردن بخش فعال در TOC:

```javascript
// Intersection Observer برای highlight
const observer = new IntersectionObserver((entries) => {
    // Update active TOC item
});
```

---

## 📂 فایل‌های تغییر یافته

1. ✅ `static/assets/js/auto-direction.js`
   - تابع `getFirstLevelText()` اضافه شد
   - تابع `setAutoDirection()` بهبود یافت
   - تابع `processArticleCards()` ساده شد

2. ✅ `SUMMARY_AND_DIRECTION_FIX.md` (این فایل)
   - مستندات کامل

---

## 🐛 عیب‌یابی

### مشکل: لیست‌ها هنوز direction اشتباه دارند

**راه‌حل:**
1. Clear browser cache (Ctrl+F5)
2. بررسی console برای خطاها
3. بررسی که `data-dir-set` روی المان set شده

```javascript
// Debug:
document.querySelectorAll('li').forEach(li => {
    console.log(li.getAttribute('data-dir-set'), li.textContent);
});
```

---

### مشکل: TOC در summary نمایش داده نمی‌شود

**راه‌حل:**
1. بررسی که `processArticleCards()` اجرا می‌شود
2. بررسی HTML source
3. بررسی CSS - شاید display: none دارد

```javascript
// Debug:
document.querySelectorAll('.article-card-summary').forEach(card => {
    console.log('Processed:', card.getAttribute('data-processed'));
    console.log('HTML:', card.innerHTML);
});
```

---

**نویسنده**: Davood Yahya  
**تاریخ**: 2026-02-08  
**نسخه**: 2.3

---

**پایان مستندات** 🎉
