/**
 * Heading IDs Generator
 * تولید ID برای headings که ID ندارند
 */

(function() {
    'use strict';
    
    // تابع تبدیل متن به slug
    function slugify(text) {
        return text
            .toString()
            .toLowerCase()
            .trim()
            .replace(/\s+/g, '-')           // فاصله‌ها را با - جایگزین کن
            .replace(/[^\w\u0600-\u06FF\-]+/g, '') // حروف غیرمجاز را حذف کن
            .replace(/\-\-+/g, '-')         // -- را با - جایگزین کن
            .replace(/^-+/, '')             // - از ابتدا را حذف کن
            .replace(/-+$/, '');            // - از انتها را حذف کن
    }
    
    // تابع اضافه کردن ID به headings
    function addHeadingIds() {
        const articleContent = document.querySelector('.article-content');
        if (!articleContent) return;
        
        const headings = articleContent.querySelectorAll('h1, h2, h3, h4, h5, h6');
        const usedIds = new Set();
        
        headings.forEach((heading) => {
            // اگر قبلاً ID دارد، نگه‌دار
            if (heading.id) {
                usedIds.add(heading.id);
                return;
            }
            
            // تولید ID از متن heading
            const text = heading.textContent || heading.innerText;
            let id = slugify(text);
            
            // اگر ID خالی است، از یک ID پیش‌فرض استفاده کن
            if (!id) {
                id = 'heading-' + Math.random().toString(36).substr(2, 9);
            }
            
            // اگر ID تکراری است، شماره اضافه کن
            let finalId = id;
            let counter = 1;
            while (usedIds.has(finalId)) {
                finalId = id + '-' + counter;
                counter++;
            }
            
            heading.id = finalId;
            usedIds.add(finalId);
        });
    }
    
    // اجرای تابع بعد از load شدن صفحه
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', addHeadingIds);
    } else {
        addHeadingIds();
    }
    
})();
