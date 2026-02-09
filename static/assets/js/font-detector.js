/**
 * Font Detector - Auto Apply Persian/English Fonts
 * Detects content language and applies appropriate fonts
 */

(function() {
    'use strict';

    // Persian character regex
    const persianRegex = /[\u0600-\u06FF]/;

    // Function to detect if text contains Persian characters
    function hasPersianCharacters(text) {
        if (!text || text.trim() === '') return false;
        return persianRegex.test(text);
    }

    // Function to apply font based on content
    function applyFontToElement(element) {
        // Skip code blocks
        if (element.tagName === 'CODE' || element.tagName === 'PRE') {
            return;
        }

        const text = element.textContent || '';
        
        if (hasPersianCharacters(text)) {
            // Persian content
            if (element.tagName.match(/^H[1-6]$/)) {
                // Headings use Shabnam
                element.style.fontFamily = "'Shabnam', 'Vazir', sans-serif";
            } else {
                // Body text uses Vazir
                element.style.fontFamily = "'Vazir', 'Shabnam', sans-serif";
            }
        } else if (text.trim().length > 0) {
            // English content
            element.style.fontFamily = "'Rajdhani', 'Vazir', sans-serif";
        }
    }

    // Apply fonts to article content
    function applyFontsToArticle() {
        const articleContent = document.querySelector('.article-content');
        if (!articleContent) return;

        // Process all text elements
        const textElements = articleContent.querySelectorAll('p, h1, h2, h3, h4, h5, h6, li, td, th, blockquote, span, div');
        
        textElements.forEach(element => {
            // Skip if element has code children
            if (element.querySelector('code, pre')) {
                return;
            }
            
            applyFontToElement(element);
        });
    }

    // Apply fonts to cards and other elements
    function applyFontsToCards() {
        // Category cards
        const categoryCards = document.querySelectorAll('.category-card h2, .category-description-text');
        categoryCards.forEach(element => {
            applyFontToElement(element);
        });

        // Article cards
        const articleCards = document.querySelectorAll('.article-card-title, .article-card-summary');
        articleCards.forEach(element => {
            applyFontToElement(element);
        });

        // Page titles
        const pageTitles = document.querySelectorAll('.page-title, .category-title, .category-description');
        pageTitles.forEach(element => {
            applyFontToElement(element);
        });
    }

    // Apply fonts to sidebar
    function applyFontsToSidebar() {
        const sidebarElements = document.querySelectorAll('.sidebar-widget-title, .category-name, .recent-post-title');
        sidebarElements.forEach(element => {
            applyFontToElement(element);
        });
    }

    // Main initialization
    function init() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                applyFontsToArticle();
                applyFontsToCards();
                applyFontsToSidebar();
            });
        } else {
            applyFontsToArticle();
            applyFontsToCards();
            applyFontsToSidebar();
        }
    }

    // Run initialization
    init();

    // Re-apply fonts when content changes (for dynamic content)
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                applyFontsToArticle();
                applyFontsToCards();
                applyFontsToSidebar();
            }
        });
    });

    // Observe the document for changes
    if (document.body) {
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }

})();
