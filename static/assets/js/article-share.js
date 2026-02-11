/**
 * Article Share & Link Management
 * Handles social sharing, copy link, and short link generation
 */

(function() {
    'use strict';
    
    // ===========================
    // Utility Functions
    // ===========================
    
    /**
     * Generate unique short slug based on article slug
     * @param {string} articleSlug - Original article slug
     * @returns {string} - Short slug (8 characters)
     */
    function generateShortSlug(articleSlug) {
        // Simple hash function for consistency
        let hash = 0;
        for (let i = 0; i < articleSlug.length; i++) {
            const char = articleSlug.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash; // Convert to 32bit integer
        }
        
        // Convert to base36 and take first 8 characters
        const shortSlug = Math.abs(hash).toString(36).substring(0, 8);
        return shortSlug;
    }
    
    /**
     * Get short link data from localStorage or generate new
     * @returns {object} - { shortSlug, fullUrl, shortUrl }
     */
    function getOrCreateShortLink() {
        const currentUrl = window.location.href;
        const pathname = window.location.pathname;
        const articleSlug = pathname.split('/').filter(Boolean).pop();
        
        // Check if short link already exists
        const storageKey = `shortlink_${articleSlug}`;
        let shortLinkData = localStorage.getItem(storageKey);
        
        if (shortLinkData) {
            return JSON.parse(shortLinkData);
        }
        
        // Generate new short link
        const shortSlug = generateShortSlug(articleSlug);
        const baseUrl = window.location.origin;
        const shortUrl = `${baseUrl}/s/${shortSlug}`;
        
        const data = {
            shortSlug: shortSlug,
            fullUrl: currentUrl,
            shortUrl: shortUrl,
            articleSlug: articleSlug,
            created: new Date().toISOString()
        };
        
        // Save to localStorage
        localStorage.setItem(storageKey, JSON.stringify(data));
        
        // Save mapping for redirect
        saveShortLinkMapping(shortSlug, currentUrl);
        
        return data;
    }
    
    /**
     * Save short link mapping for redirect handler
     * @param {string} shortSlug - Short slug
     * @param {string} fullUrl - Full article URL
     */
    function saveShortLinkMapping(shortSlug, fullUrl) {
        const mappings = JSON.parse(localStorage.getItem('shortlink_mappings') || '{}');
        mappings[shortSlug] = fullUrl;
        localStorage.setItem('shortlink_mappings', JSON.stringify(mappings));
    }
    
    /**
     * Copy text to clipboard with fallback
     * @param {string} text - Text to copy
     * @returns {Promise<boolean>} - Success status
     */
    async function copyToClipboard(text) {
        // Modern Clipboard API
        if (navigator.clipboard && navigator.clipboard.writeText) {
            try {
                await navigator.clipboard.writeText(text);
                return true;
            } catch (err) {
                console.warn('Clipboard API failed, using fallback');
            }
        }
        
        // Fallback method
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        textArea.style.top = '-999999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        
        try {
            const successful = document.execCommand('copy');
            document.body.removeChild(textArea);
            return successful;
        } catch (err) {
            document.body.removeChild(textArea);
            return false;
        }
    }
    
    /**
     * Show success notification
     * @param {HTMLElement} button - Button element
     * @param {string} message - Success message
     */
    function showSuccessState(button, message) {
        const originalText = button.querySelector('.btn-text').textContent;
        const textSpan = button.querySelector('.btn-text');
        
        textSpan.textContent = message;
        button.classList.add('success');
        
        setTimeout(() => {
            textSpan.textContent = originalText;
            button.classList.remove('success');
        }, 2000);
    }
    
    // ===========================
    // Social Share Functions
    // ===========================
    
    /**
     * Get share URL for different platforms
     * @param {string} platform - Social media platform
     * @param {string} url - Article URL
     * @param {string} title - Article title
     * @returns {string} - Share URL
     */
    function getShareUrl(platform, url, title) {
        const encodedUrl = encodeURIComponent(url);
        const encodedTitle = encodeURIComponent(title);
        
        const shareUrls = {
            telegram: `https://t.me/share/url?url=${encodedUrl}&text=${encodedTitle}`,
            whatsapp: `https://wa.me/?text=${encodedTitle}%20${encodedUrl}`,
            twitter: `https://twitter.com/intent/tweet?url=${encodedUrl}&text=${encodedTitle}`,
            linkedin: `https://www.linkedin.com/sharing/share-offsite/?url=${encodedUrl}`,
            facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}`,
            instagram: `https://www.instagram.com/create/story/?text=${encodedTitle}%20${encodedUrl}`,
            youtube: `https://www.youtube.com/create?url=${encodedUrl}&text=${encodedTitle}`
        };
        
        return shareUrls[platform] || '';
    }
    
    /**
     * Initialize social share buttons
     */
    function initializeSocialShare() {
        const shareButtons = document.querySelectorAll('.share-btn[data-platform]');
        const articleTitle = document.querySelector('.article-title')?.textContent || document.title;
        const articleUrl = window.location.href;
        
        shareButtons.forEach(button => {
            const platform = button.dataset.platform;
            
            // Skip email (already has href)
            if (platform === 'email') return;
            
            const shareUrl = getShareUrl(platform, articleUrl, articleTitle);
            button.href = shareUrl;
        });
    }
    
    // ===========================
    // Copy Link Function
    // ===========================
    
    /**
     * Initialize copy link button
     */
    function initializeCopyLink() {
        const copyBtn = document.getElementById('copyLinkBtn');
        if (!copyBtn) return;
        
        copyBtn.addEventListener('click', async () => {
            const currentUrl = window.location.href;
            const success = await copyToClipboard(currentUrl);
            
            if (success) {
                showSuccessState(copyBtn, 'کپی شد ✓');
            } else {
                showSuccessState(copyBtn, 'خطا در کپی');
            }
        });
    }
    
    // ===========================
    // Short Link Functions
    // ===========================
    
    /**
     * Initialize short link button
     */
    function initializeShortLink() {
        const shortLinkBtn = document.getElementById('shortLinkBtn');
        const shortLinkDisplay = document.getElementById('shortLinkDisplay');
        const shortLinkInput = document.getElementById('shortLinkInput');
        const copyShortLinkBtn = document.getElementById('copyShortLinkBtn');
        
        if (!shortLinkBtn || !shortLinkDisplay || !shortLinkInput) return;
        
        // Generate/Show short link
        shortLinkBtn.addEventListener('click', () => {
            const linkData = getOrCreateShortLink();
            shortLinkInput.value = linkData.shortUrl;
            shortLinkDisplay.style.display = 'block';
            
            // Animate display
            setTimeout(() => {
                shortLinkDisplay.classList.add('active');
            }, 10);
        });
        
        // Copy short link
        if (copyShortLinkBtn) {
            copyShortLinkBtn.addEventListener('click', async () => {
                const shortUrl = shortLinkInput.value;
                const success = await copyToClipboard(shortUrl);
                
                if (success) {
                    const originalText = copyShortLinkBtn.textContent;
                    copyShortLinkBtn.innerHTML = `
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                        </svg>
                        کپی شد
                    `;
                    copyShortLinkBtn.classList.add('success');
                    
                    setTimeout(() => {
                        copyShortLinkBtn.innerHTML = `
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                            </svg>
                            کپی
                        `;
                        copyShortLinkBtn.classList.remove('success');
                    }, 2000);
                }
            });
        }
    }
    
    // ===========================
    // Short Link Redirect Handler
    // ===========================
    
    /**
     * Handle short link redirects (for /s/:slug pages)
     */
    function handleShortLinkRedirect() {
        const pathname = window.location.pathname;
        
        // Check if we're on a short link page
        if (pathname.startsWith('/s/')) {
            const shortSlug = pathname.split('/').pop();
            const mappings = JSON.parse(localStorage.getItem('shortlink_mappings') || '{}');
            
            if (mappings[shortSlug]) {
                // Redirect to full article URL
                window.location.replace(mappings[shortSlug]);
            } else {
                // Show 404 if mapping not found
                console.error('Short link not found:', shortSlug);
                // Could redirect to custom 404 page
                if (document.body) {
                    document.body.innerHTML = `
                        <div style="
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                            justify-content: center;
                            height: 100vh;
                            background: #0a0a0a;
                            color: #00ff41;
                            font-family: 'Vazir', sans-serif;
                            text-align: center;
                            padding: 2rem;
                        ">
                            <h1 style="font-size: 4rem; margin-bottom: 1rem;">404</h1>
                            <p style="font-size: 1.5rem; margin-bottom: 2rem;">لینک کوتاه یافت نشد</p>
                            <a href="/" style="
                                color: #00ff41;
                                text-decoration: none;
                                padding: 1rem 2rem;
                                border: 2px solid #00ff41;
                                border-radius: 8px;
                                transition: all 0.3s ease;
                            ">بازگشت به صفحه اصلی</a>
                        </div>
                    `;
                }
            }
        }
    }
    
    // ===========================
    // Initialize All Features
    // ===========================
    
    function init() {
        // Handle short link redirect first
        handleShortLinkRedirect();
        
        // Initialize features on single article pages
        if (document.querySelector('.article-wrapper')) {
            initializeSocialShare();
            initializeCopyLink();
            initializeShortLink();
        }
    }
    
    // Run on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
})();
