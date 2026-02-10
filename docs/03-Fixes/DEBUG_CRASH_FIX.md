# 🔧 Debug: Browser Crash Fix

## مشکل اصلی

وقتی صفحات دسته‌بندی (list pages) باز می‌شدند، مرورگر crash می‌کرد.

---

## علت مشکل

### 1. **Infinite Loop در MutationObserver**

کد قبلی:
```javascript
const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.addedNodes.length) {
            processArticleContent();      // این خود DOM را تغییر می‌داد
            processArticleCards();        // این هم DOM را تغییر می‌داد
        }
    });
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});
```

**مشکل:**
- `processArticleCards()` از `innerHTML` استفاده می‌کرد
- هر بار که `innerHTML` تغییر می‌کرد، MutationObserver فعال می‌شد
- دوباره `processArticleCards()` اجرا می‌شد
- دوباره `innerHTML` تغییر می‌کرد
- → **Infinite Loop** → Browser Crash

### 2. **عدم Check برای Already Processed**

کد قبلی بدون چک می‌کرد که آیا element قبلاً پردازش شده یا نه.

---

## راه‌حل‌های اعمال شده

### ✅ راه‌حل 1: حذف کامل MutationObserver

```javascript
// قبل:
const observer = new MutationObserver(...);
observer.observe(document.body, ...);

// بعد:
// Removed completely
```

**دلیل:** برای یک وبسایت استاتیک Hugo نیازی به MutationObserver نیست.

---

### ✅ راه‌حل 2: اضافه کردن Flag برای Processed Elements

```javascript
function processArticleCards() {
    document.querySelectorAll('.article-card-summary').forEach(card => {
        // Check if already processed
        if (card.getAttribute('data-processed')) return;
        
        // Process...
        
        // Mark as processed
        card.setAttribute('data-processed', 'true');
    });
}
```

---

### ✅ راه‌حل 3: استفاده از CSS به جای DOM Manipulation

```javascript
// قبل: DOM manipulation که trigger می‌کرد MutationObserver
card.querySelectorAll('img').forEach(img => {
    img.remove();  // ❌ Triggers mutation
});

// بعد: فقط CSS
card.querySelectorAll('img').forEach(img => {
    img.style.display = 'none';  // ✅ Safe
});
```

---

### ✅ راه‌حل 4: ساده‌سازی کد

کد جدید بسیار ساده‌تر و بهینه‌تر است:

```javascript
(function() {
    'use strict';
    
    // Simple functions
    function startsWithPersian(text) { ... }
    function isEnglishText(text) { ... }
    function setAutoDirection(element) { ... }
    
    // Process article content
    function processArticleContent() {
        const articleContent = document.querySelector('.article-content');
        if (!articleContent || articleContent.getAttribute('data-processed')) return;
        
        // ... processing ...
        
        articleContent.setAttribute('data-processed', 'true');
    }
    
    // Process article cards
    function processArticleCards() {
        document.querySelectorAll('.article-card-summary').forEach(card => {
            if (card.getAttribute('data-processed')) return;
            
            // Hide images (no DOM manipulation)
            card.querySelectorAll('img').forEach(img => {
                img.style.display = 'none';
            });
            
            card.setAttribute('data-processed', 'true');
        });
    }
    
    // Initialize once
    function init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', run);
        } else {
            run();
        }
    }
    
    function run() {
        try {
            processArticleContent();
            processArticleCards();
        } catch (error) {
            console.error('Auto-direction error:', error);
        }
    }
    
    init();
})();
```

---

## مقایسه Before/After

### قبل (Crash):
```
1. صفحه load می‌شود
2. processArticleCards() اجرا می‌شود
3. innerHTML تغییر می‌کند
4. MutationObserver trigger می‌شود
5. دوباره processArticleCards() اجرا می‌شود
6. دوباره innerHTML تغییر می‌کند
7. → Infinite Loop
8. → Memory Overflow
9. → Browser Crash
```

### بعد (Fixed):
```
1. صفحه load می‌شود
2. processArticleCards() اجرا می‌شود
3. Check می‌کند: آیا processed است?
   - اگر بله → Skip
   - اگر نه → Process و Mark as processed
4. فقط CSS تغییر می‌کند (نه innerHTML)
5. تمام
6. ✅ No Crash
```

---

## تست و تأیید

### قبل از Fix:
```
✗ صفحه دسته‌بندی → Browser Crash
✗ Console پر از error
✗ Tab freezes
```

### بعد از Fix:
```
✓ صفحه دسته‌بندی → Load می‌شود
✓ تصاویر مخفی می‌شوند
✓ Direction درست تنظیم می‌شود
✓ هیچ crash نمی‌کند
```

---

## چک‌لیست نهایی

- [x] حذف MutationObserver
- [x] اضافه کردن `data-processed` flag
- [x] استفاده از CSS به جای DOM manipulation
- [x] ساده‌سازی کد
- [x] اضافه کردن try-catch
- [x] تست در Chrome
- [x] تست در Firefox
- [x] تست در Edge

---

## نکات مهم برای آینده

### 1. **هرگز از MutationObserver در صفحات استاتیک استفاده نکنید**

```javascript
// ❌ Bad for static sites
const observer = new MutationObserver(...);

// ✅ Good for static sites
document.addEventListener('DOMContentLoaded', () => {
    // Run once
});
```

### 2. **همیشه Check کنید که element پردازش شده یا نه**

```javascript
// ✅ Always check
if (element.getAttribute('data-processed')) return;
// ... process ...
element.setAttribute('data-processed', 'true');
```

### 3. **ترجیح دهید CSS به DOM Manipulation**

```javascript
// ❌ DOM manipulation
element.remove();
element.innerHTML = '...';

// ✅ CSS
element.style.display = 'none';
element.classList.add('hidden');
```

---

## کد نهایی

فایل: `static/assets/js/auto-direction.js`

```javascript
/**
 * Auto Direction Detection Script
 * Version: 2.1 - Crash-safe
 */

(function() {
    'use strict';
    
    function startsWithPersian(text) {
        if (!text || text.trim().length === 0) return false;
        const firstChar = text.trim()[0];
        const charCode = firstChar.charCodeAt(0);
        return (charCode >= 0x0600 && charCode <= 0x06FF) || 
               (charCode >= 0x0750 && charCode <= 0x077F);
    }
    
    function isEnglishText(text) {
        if (!text || text.trim().length === 0) return false;
        const englishLetters = (text.match(/[a-zA-Z]/g) || []).length;
        const persianLetters = (text.match(/[\u0600-\u06FF\u0750-\u077F]/g) || []).length;
        const totalLetters = englishLetters + persianLetters;
        if (totalLetters === 0) return false;
        return (englishLetters / totalLetters) > 0.7;
    }
    
    function setAutoDirection(element) {
        if (!element || element.getAttribute('data-dir-set')) return;
        
        const text = element.textContent || element.innerText || '';
        
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
    
    function processArticleContent() {
        const articleContent = document.querySelector('.article-content');
        if (!articleContent || articleContent.getAttribute('data-processed')) return;
        
        const articleText = articleContent.textContent || '';
        
        if (isEnglishText(articleText)) {
            articleContent.style.direction = 'ltr';
            articleContent.style.textAlign = 'left';
            articleContent.setAttribute('dir', 'ltr');
            articleContent.setAttribute('lang', 'en');
        }
        
        articleContent.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(setAutoDirection);
        articleContent.querySelectorAll('p').forEach(setAutoDirection);
        articleContent.querySelectorAll('li').forEach(setAutoDirection);
        
        articleContent.querySelectorAll('pre, code').forEach(code => {
            code.style.direction = 'ltr';
            code.style.textAlign = 'left';
            code.setAttribute('dir', 'ltr');
        });
        
        const toc = document.querySelector('#TableOfContents');
        if (toc) {
            toc.style.direction = 'ltr';
            toc.style.textAlign = 'left';
            toc.setAttribute('dir', 'ltr');
            toc.querySelectorAll('ul, ol').forEach(list => {
                list.style.paddingLeft = '1.5rem';
                list.style.paddingRight = '0';
                list.style.direction = 'ltr';
            });
        }
        
        articleContent.setAttribute('data-processed', 'true');
    }
    
    function processArticleCards() {
        document.querySelectorAll('.article-card-summary').forEach(card => {
            if (card.getAttribute('data-processed')) return;
            
            card.querySelectorAll('img').forEach(img => {
                img.style.display = 'none';
            });
            
            card.setAttribute('data-processed', 'true');
        });
    }
    
    function init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', run);
        } else {
            run();
        }
    }
    
    function run() {
        try {
            processArticleContent();
            processArticleCards();
        } catch (error) {
            console.error('Auto-direction error:', error);
        }
    }
    
    init();
})();
```

---

## نتیجه‌گیری

✅ **مشکل حل شد**
- Browser دیگر crash نمی‌کند
- صفحات دسته‌بندی به درستی load می‌شوند
- تصاویر از summary مخفی می‌شوند
- Direction به درستی تنظیم می‌شود

✅ **بهینه‌سازی‌های انجام شده**
- حذف MutationObserver (غیرضروری)
- اضافه کردن flag های processed
- استفاده از CSS به جای DOM manipulation
- ساده‌سازی و خوانایی کد

✅ **تست شده در**
- Chrome ✓
- Firefox ✓
- Edge ✓
- Mobile browsers ✓

---

**تاریخ Fix**: 2026-02-08  
**وضعیت**: ✅ حل شده  
**نسخه**: 2.1

---
