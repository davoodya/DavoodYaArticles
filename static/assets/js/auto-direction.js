/**
 * Auto Direction Detection Script (Obsidian-like behavior)
 * Author: Davood Yahya
 * Date: 2026-02-08
 * Version: 2.1 - Optimized and crash-safe
 */

(function() {
    'use strict';
    
    /**
     * Check if text starts with Persian/Arabic characters
     */
    function startsWithPersian(text) {
        if (!text || text.trim().length === 0) return false;
        const firstChar = text.trim()[0];
        const charCode = firstChar.charCodeAt(0);
        return (charCode >= 0x0600 && charCode <= 0x06FF) || 
               (charCode >= 0x0750 && charCode <= 0x077F);
    }
    
    /**
     * Check if text is predominantly English
     */
    function isEnglishText(text) {
        if (!text || text.trim().length === 0) return false;
        const englishLetters = (text.match(/[a-zA-Z]/g) || []).length;
        const persianLetters = (text.match(/[\u0600-\u06FF\u0750-\u077F]/g) || []).length;
        const totalLetters = englishLetters + persianLetters;
        if (totalLetters === 0) return false;
        return (englishLetters / totalLetters) > 0.7;
    }
    
    /**
     * Set direction for an element
     */
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
    
    /**
     * Process article content
     */
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
        
        // Process headings
        articleContent.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(setAutoDirection);
        
        // Process paragraphs
        articleContent.querySelectorAll('p').forEach(setAutoDirection);
        
        // Process list items
        articleContent.querySelectorAll('li').forEach(setAutoDirection);
        
        // Force LTR for code blocks
        articleContent.querySelectorAll('pre, code').forEach(code => {
            code.style.direction = 'ltr';
            code.style.textAlign = 'left';
            code.setAttribute('dir', 'ltr');
        });
        
        // Force LTR for TOC
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
    
    /**
     * Process article cards - Remove images from summaries
     */
    function processArticleCards() {
        document.querySelectorAll('.article-card-summary').forEach(card => {
            if (card.getAttribute('data-processed')) return;
            
            // Simply hide images with CSS (safer than removing from DOM)
            card.querySelectorAll('img').forEach(img => {
                img.style.display = 'none';
            });
            
            card.setAttribute('data-processed', 'true');
        });
    }
    
    /**
     * Initialize
     */
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
