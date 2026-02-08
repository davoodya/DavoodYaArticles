/**
 * Auto Direction Detection Script (Obsidian-like behavior)
 * Author: Davood Yahya
 * Date: 2026-02-08
 * Version: 2.2 - Improved summary extraction
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
            text = getFirstLevelText(element);
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
    
    /**
     * Extract first real paragraph from text (skip headings, TOC, lists)
     */
    function extractFirstParagraph(text) {
        if (!text) return '';
        
        // Split into lines
        const lines = text.split('\n');
        let paragraph = '';
        let inParagraph = false;
        
        for (let line of lines) {
            line = line.trim();
            
            // Skip empty lines
            if (line.length === 0) {
                if (inParagraph && paragraph.length > 50) {
                    break; // End of paragraph
                }
                continue;
            }
            
            // Skip headings (starts with # or ####, etc.)
            if (line.match(/^#+\s+/)) {
                continue;
            }
            
            // Skip TOC lines (starts with - [link] or just - text)
            if (line.match(/^-\s*\[/) || line.match(/^-\s+[#A-Za-z]/)) {
                continue;
            }
            
            // Skip bullet points
            if (line.match(/^[\*\-]\s+/)) {
                continue;
            }
            
            // Skip numbered lists
            if (line.match(/^\d+\.\s+/)) {
                continue;
            }
            
            // Skip lines that are just links or references
            if (line.match(/^\[.*?\]\(.*?\)$/)) {
                continue;
            }
            
            // Skip lines with mostly special characters
            if (line.match(/^[#\-\*\d\[\]\(\):\s]{5,}$/)) {
                continue;
            }
            
            // Skip "TOC" keyword
            if (line.match(/^TOC$/i) || line.match(/^Table of Contents$/i)) {
                continue;
            }
            
            // Skip horizontal rules
            if (line.match(/^[-=]{3,}$/)) {
                continue;
            }
            
            // This looks like actual paragraph text
            // Must have at least some real content
            const hasRealContent = line.match(/[\u0600-\u06FF\u0750-\u077Fa-zA-Z]{5,}/);
            
            if (hasRealContent && line.length > 20) {
                if (!inParagraph) {
                    inParagraph = true;
                }
                paragraph += line + ' ';
                
                // If we have enough text, stop
                if (paragraph.length > 200) {
                    break;
                }
            }
        }
        
        // Clean up the paragraph
        paragraph = paragraph.trim();
        
        // If we found a good paragraph, return it
        if (paragraph.length > 50) {
            return paragraph.length > 250 ? paragraph.substring(0, 250) + '...' : paragraph;
        }
        
        // Fallback: just take first 200 chars of actual text
        const cleaned = text.replace(/^#+\s+.*$/gm, '')
                           .replace(/^-\s+.*$/gm, '')
                           .replace(/^\d+\.\s+.*$/gm, '')
                           .trim();
        return cleaned.substring(0, 200);
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
     * Process article cards - Hide images, remove ALL headers, limit height
     */
    function processArticleCards() {
        document.querySelectorAll('.article-card-summary').forEach(card => {
            if (card.getAttribute('data-processed')) return;
            
            // Hide images with CSS (but keep TOC and text)
            card.querySelectorAll('img').forEach(img => {
                img.style.display = 'none';
            });
            
            // Remove ALL headings completely
            const headings = card.querySelectorAll('h1, h2, h3, h4, h5, h6');
            headings.forEach(heading => {
                heading.remove();
            });
            
            // Remove HR (horizontal rules) as well
            card.querySelectorAll('hr').forEach(hr => {
                hr.remove();
            });
            
            // Limit list depth to prevent too much nesting
            const lists = card.querySelectorAll('ul, ol');
            lists.forEach(list => {
                // If list is nested more than 3 levels deep, remove it
                let depth = 0;
                let parent = list.parentElement;
                while (parent && parent !== card) {
                    if (parent.tagName === 'UL' || parent.tagName === 'OL' || parent.tagName === 'LI') {
                        depth++;
                    }
                    parent = parent.parentElement;
                }
                
                if (depth > 3) {
                    list.remove();
                }
            });
            
            // Make sure TOC links are styled properly
            card.querySelectorAll('a').forEach(link => {
                link.style.pointerEvents = 'auto';
                link.style.cursor = 'pointer';
            });
            
            card.setAttribute('data-processed', 'true');
        });
    }
    
    /**
     * Make article cards clickable
     */
    function makeCardsClickable() {
        document.querySelectorAll('.article-card').forEach(card => {
            const url = card.getAttribute('data-article-url');
            if (!url) return;
            
            card.addEventListener('click', function(e) {
                // Don't trigger if clicking on a link inside the card
                if (e.target.tagName === 'A' || e.target.closest('a')) {
                    return;
                }
                
                // Navigate to article
                window.location.href = url;
            });
            
            // Add hover effect hint
            card.style.cursor = 'pointer';
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
            makeCardsClickable();
        } catch (error) {
            console.error('Auto-direction error:', error);
        }
    }
    
    init();
    
})();
