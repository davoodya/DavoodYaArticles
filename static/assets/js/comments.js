/**
 * ===========================
 * Comments System
 * ===========================
 * سیستم کامنت برای Hugo Static Site
 * با استفاده از PHP Backend
 */

(function() {
    'use strict';

    // ===========================
    // Configuration
    // ===========================
    
    const CONFIG = {
        // Use PHP Backend (for local development and PHP hosting)
        // When deploying to Netlify, change to: '/.netlify/functions/comments'
        API_ENDPOINT: '/api/comments.php',
        MAX_RETRIES: 3,
        RETRY_DELAY: 1000,
        RATE_LIMIT_WINDOW: 60000, // 1 minute
        MAX_COMMENTS_PER_WINDOW: 3,
        CACHE_DURATION: 300000, // 5 minutes
    };

    // ===========================
    // State Management
    // ===========================
    
    const state = {
        articleSlug: null,
        articleTitle: null,
        articleUrl: null,
        comments: [],
        isLoading: false,
        isSubmitting: false,
        lastSubmitTime: 0,
        submitCount: 0,
        cache: new Map(),
    };

    // ===========================
    // DOM Elements
    // ===========================
    
    const elements = {
        form: null,
        commentsList: null,
        loadingIndicator: null,
        emptyState: null,
        commentsCount: null,
        submitBtn: null,
        formMessage: null,
    };

    // ===========================
    // Utility Functions
    // ===========================
    
    function sanitizeHTML(str) {
        const temp = document.createElement('div');
        temp.textContent = str;
        return temp.innerHTML;
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    function validateURL(url) {
        if (!url) return true; // Optional field
        try {
            const urlObj = new URL(url);
            return urlObj.protocol === 'http:' || urlObj.protocol === 'https:';
        } catch {
            return false;
        }
    }

    function getInitials(name) {
        const parts = name.trim().split(/\s+/);
        if (parts.length === 1) {
            return parts[0].substring(0, 2).toUpperCase();
        }
        return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    }

    function formatDate(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const diffMs = now - date;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'همین الان';
        if (diffMins < 60) return `${diffMins} دقیقه پیش`;
        if (diffHours < 24) return `${diffHours} ساعت پیش`;
        if (diffDays < 7) return `${diffDays} روز پیش`;

        const options = { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric'
        };
        
        try {
            return new Intl.DateTimeFormat('fa-IR', options).format(date);
        } catch {
            return date.toLocaleDateString('fa-IR');
        }
    }

    function showFormMessage(message, type = 'success') {
        if (!elements.formMessage) return;
        
        elements.formMessage.textContent = message;
        elements.formMessage.className = `form-message ${type} show`;
        
        setTimeout(() => {
            elements.formMessage.classList.remove('show');
        }, 5000);
    }

    function showFieldError(fieldId, message) {
        const input = document.getElementById(fieldId);
        const errorElement = document.getElementById(`${fieldId.replace('comment', '').toLowerCase()}Error`);
        
        if (input) {
            input.classList.add('error');
            input.setAttribute('aria-invalid', 'true');
        }
        
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.classList.add('show');
        }
    }

    function clearFieldError(fieldId) {
        const input = document.getElementById(fieldId);
        const errorElement = document.getElementById(`${fieldId.replace('comment', '').toLowerCase()}Error`);
        
        if (input) {
            input.classList.remove('error');
            input.removeAttribute('aria-invalid');
        }
        
        if (errorElement) {
            errorElement.textContent = '';
            errorElement.classList.remove('show');
        }
    }

    function clearAllErrors() {
        ['commentName', 'commentEmail', 'commentWebsite', 'commentText'].forEach(clearFieldError);
    }

    // ===========================
    // Rate Limiting
    // ===========================
    
    function checkRateLimit() {
        const now = Date.now();
        
        // Reset counter if window has passed
        if (now - state.lastSubmitTime > CONFIG.RATE_LIMIT_WINDOW) {
            state.submitCount = 0;
        }
        
        if (state.submitCount >= CONFIG.MAX_COMMENTS_PER_WINDOW) {
            const remainingTime = Math.ceil((CONFIG.RATE_LIMIT_WINDOW - (now - state.lastSubmitTime)) / 1000);
            return {
                allowed: false,
                message: `لطفاً ${remainingTime} ثانیه صبر کنید.`
            };
        }
        
        return { allowed: true };
    }

    // ===========================
    // API Functions
    // ===========================
    
    async function fetchWithRetry(url, options = {}, retries = CONFIG.MAX_RETRIES) {
        try {
            const response = await fetch(url, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers,
                },
            });
            
            // Read response text first
            const text = await response.text();
            
            // Try to parse as JSON
            let data;
            try {
                data = JSON.parse(text);
            } catch (parseError) {
                console.error('JSON Parse Error:', parseError);
                console.error('Response text:', text);
                throw new Error('سرور پاسخ نامعتبری ارسال کرد. لطفاً دوباره تلاش کنید.');
            }
            
            if (!response.ok) {
                throw new Error(data.error || data.message || `خطای سرور: ${response.status}`);
            }
            
            return data;
        } catch (error) {
            if (retries > 0 && !error.message.includes('نامعتبر')) {
                await new Promise(resolve => setTimeout(resolve, CONFIG.RETRY_DELAY));
                return fetchWithRetry(url, options, retries - 1);
            }
            throw error;
        }
    }

    async function loadComments(slug) {
        // Check cache first
        const cached = state.cache.get(slug);
        if (cached && (Date.now() - cached.timestamp < CONFIG.CACHE_DURATION)) {
            return cached.data;
        }

        const data = await fetchWithRetry(`${CONFIG.API_ENDPOINT}?article=${encodeURIComponent(slug)}`);
        
        // Update cache
        state.cache.set(slug, {
            data: data,
            timestamp: Date.now()
        });
        
        return data;
    }

    async function submitComment(commentData) {
        return await fetchWithRetry(CONFIG.API_ENDPOINT, {
            method: 'POST',
            body: JSON.stringify(commentData),
        });
    }

    // ===========================
    // Render Functions
    // ===========================
    
    function renderComment(comment) {
        const card = document.createElement('article');
        card.className = 'comment-card';
        card.setAttribute('role', 'article');
        card.setAttribute('data-comment-id', comment.id);
        
        const initials = getInitials(comment.name);
        const formattedDate = formatDate(comment.datetime);
        const sanitizedComment = sanitizeHTML(comment.comment);
        
        let authorHTML;
        if (comment.website && validateURL(comment.website)) {
            authorHTML = `<a href="${sanitizeHTML(comment.website)}" class="comment-author" target="_blank" rel="nofollow noopener noreferrer">${sanitizeHTML(comment.name)}</a>`;
        } else {
            authorHTML = `<span class="comment-author no-link">${sanitizeHTML(comment.name)}</span>`;
        }
        
        card.innerHTML = `
            <div class="comment-header">
                <div class="comment-avatar" aria-hidden="true">${initials}</div>
                <div class="comment-meta">
                    <div class="comment-author-row">
                        ${authorHTML}
                    </div>
                    <time class="comment-date" datetime="${comment.datetime}">${formattedDate}</time>
                </div>
            </div>
            <div class="comment-body">${sanitizedComment}</div>
        `;
        
        return card;
    }

    function renderComments(comments) {
        if (!elements.commentsList) return;
        
        elements.commentsList.innerHTML = '';
        
        if (comments.length === 0) {
            elements.emptyState.style.display = 'flex';
            elements.commentsList.style.display = 'none';
        } else {
            elements.emptyState.style.display = 'none';
            elements.commentsList.style.display = 'flex';
            
            comments.forEach((comment, index) => {
                const card = renderComment(comment);
                card.style.animationDelay = `${index * 0.1}s`;
                elements.commentsList.appendChild(card);
            });
        }
        
        updateCommentsCount(comments.length);
    }

    function updateCommentsCount(count) {
        if (elements.commentsCount) {
            elements.commentsCount.textContent = `(${count})`;
            elements.commentsCount.setAttribute('data-count', count);
        }
        
        const listTitle = document.getElementById('commentsListTitle');
        if (listTitle) {
            listTitle.textContent = count > 0 ? `${count} دیدگاه` : 'همه دیدگاه‌ها';
        }
    }

    // ===========================
    // Form Validation
    // ===========================
    
    function validateForm(formData) {
        clearAllErrors();
        const errors = [];
        
        // Name validation
        if (!formData.name || formData.name.trim().length === 0) {
            showFieldError('commentName', 'لطفاً نام خود را وارد کنید');
            errors.push('name');
        } else if (formData.name.trim().length > 100) {
            showFieldError('commentName', 'نام شما بیش از حد طولانی است (حداکثر ۱۰۰ کاراکتر)');
            errors.push('name');
        }
        
        // Email validation
        if (!formData.email || !validateEmail(formData.email)) {
            showFieldError('commentEmail', 'لطفاً یک ایمیل معتبر وارد کنید');
            errors.push('email');
        }
        
        // Website validation (optional)
        if (formData.website && !validateURL(formData.website)) {
            showFieldError('commentWebsite', 'لطفاً یک آدرس وبسایت معتبر وارد کنید (مثال: https://example.com)');
            errors.push('website');
        }
        
        // Comment validation
        if (!formData.comment || formData.comment.trim().length === 0) {
            showFieldError('commentText', 'لطفاً دیدگاه خود را وارد کنید');
            errors.push('comment');
        }
        
        if (formData.comment && formData.comment.length > 2000) {
            showFieldError('commentText', 'دیدگاه شما خیلی طولانی است (حداکثر ۲۰۰۰ حرف)');
            errors.push('comment');
        }
        
        return errors.length === 0;
    }

    // ===========================
    // Form Submission
    // ===========================
    
    async function handleFormSubmit(event) {
        event.preventDefault();
        
        if (state.isSubmitting) return;
        
        // Rate limit check
        const rateLimitCheck = checkRateLimit();
        if (!rateLimitCheck.allowed) {
            showFormMessage(rateLimitCheck.message, 'error');
            return;
        }
        
        const formData = new FormData(elements.form);
        const data = {
            article_slug: state.articleSlug,
            article_title: state.articleTitle,
            article_url: state.articleUrl,
            name: formData.get('name')?.trim(),
            email: formData.get('email')?.trim(),
            website: formData.get('website')?.trim(),
            comment: formData.get('comment')?.trim(),
        };
        
        // Honeypot check
        const honeypot = formData.get('honeypot');
        if (honeypot) {
            console.warn('Spam detected via honeypot');
            showFormMessage('دیدگاه شما ثبت شد.', 'success');
            elements.form.reset();
            return;
        }
        
        // Validate
        if (!validateForm(data)) {
            return;
        }
        
        // Update UI
        state.isSubmitting = true;
        elements.submitBtn.disabled = true;
        elements.submitBtn.classList.add('loading');
        
        try {
            const response = await submitComment(data);
            
            // Update rate limit
            state.lastSubmitTime = Date.now();
            state.submitCount++;
            
            // Clear cache
            state.cache.delete(state.articleSlug);
            
            // Show success message
            showFormMessage(
                response.message || 'دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد.',
                'success'
            );
            
            // Reset form
            elements.form.reset();
            clearAllErrors();
            
            // Reload comments after a short delay
            setTimeout(() => {
                loadAndRenderComments();
            }, 1000);
            
        } catch (error) {
            console.error('Comment submission error:', error);
            showFormMessage(
                error.message || 'خطا در ارسال دیدگاه. لطفاً دوباره تلاش کنید.',
                'error'
            );
        } finally {
            state.isSubmitting = false;
            elements.submitBtn.disabled = false;
            elements.submitBtn.classList.remove('loading');
        }
    }

    // ===========================
    // Load and Render Comments
    // ===========================
    
    async function loadAndRenderComments() {
        if (!state.articleSlug || state.isLoading) return;
        
        state.isLoading = true;
        elements.loadingIndicator.style.display = 'flex';
        elements.commentsList.style.display = 'none';
        elements.emptyState.style.display = 'none';
        
        try {
            const data = await loadComments(state.articleSlug);
            state.comments = data.comments || [];
            renderComments(state.comments);
        } catch (error) {
            console.error('Failed to load comments:', error);
            elements.emptyState.style.display = 'flex';
            elements.commentsList.style.display = 'none';
        } finally {
            state.isLoading = false;
            elements.loadingIndicator.style.display = 'none';
        }
    }

    // ===========================
    // Real-time Validation
    // ===========================
    
    function setupRealtimeValidation() {
        const nameInput = document.getElementById('commentName');
        const emailInput = document.getElementById('commentEmail');
        const websiteInput = document.getElementById('commentWebsite');
        const commentInput = document.getElementById('commentText');
        
        if (nameInput) {
            nameInput.addEventListener('blur', () => {
                const length = nameInput.value.trim().length;
                if (length > 100) {
                    showFieldError('commentName', 'نام شما بیش از حد طولانی است (حداکثر ۱۰۰ کاراکتر)');
                } else {
                    clearFieldError('commentName');
                }
            });
            
            nameInput.addEventListener('input', () => {
                if (nameInput.classList.contains('error') && nameInput.value.trim().length <= 100) {
                    clearFieldError('commentName');
                }
            });
        }
        
        if (emailInput) {
            emailInput.addEventListener('blur', () => {
                if (emailInput.value.trim().length > 0 && !validateEmail(emailInput.value)) {
                    showFieldError('commentEmail', 'فرمت ایمیل معتبر نیست');
                } else {
                    clearFieldError('commentEmail');
                }
            });
            
            emailInput.addEventListener('input', () => {
                if (emailInput.classList.contains('error') && validateEmail(emailInput.value)) {
                    clearFieldError('commentEmail');
                }
            });
        }
        
        if (websiteInput) {
            websiteInput.addEventListener('blur', () => {
                if (websiteInput.value.trim().length > 0 && !validateURL(websiteInput.value)) {
                    showFieldError('commentWebsite', 'آدرس وبسایت معتبر نیست');
                } else {
                    clearFieldError('commentWebsite');
                }
            });
            
            websiteInput.addEventListener('input', () => {
                if (websiteInput.classList.contains('error') && validateURL(websiteInput.value)) {
                    clearFieldError('commentWebsite');
                }
            });
        }
        
        if (commentInput) {
            commentInput.addEventListener('blur', () => {
                const length = commentInput.value.trim().length;
                if (length > 2000) {
                    showFieldError('commentText', 'دیدگاه خیلی طولانی است (حداکثر ۲۰۰۰ حرف)');
                } else {
                    clearFieldError('commentText');
                }
            });
            
            commentInput.addEventListener('input', () => {
                const length = commentInput.value.trim().length;
                if (commentInput.classList.contains('error')) {
                    if (length <= 2000) {
                        clearFieldError('commentText');
                    }
                }
            });
        }
    }

    // ===========================
    // Initialization
    // ===========================
    
    function init() {
        // Check if we're on a comments-enabled page
        const commentsSection = document.querySelector('.comments-section');
        if (!commentsSection) return;
        
        // Get article slug
        state.articleSlug = commentsSection.getAttribute('data-article-slug');
        state.articleTitle = commentsSection.getAttribute('data-article-title');
        state.articleUrl = commentsSection.getAttribute('data-article-url');
        if (!state.articleSlug) {
            console.error('Article slug not found');
            return;
        }
        
        // Get DOM elements
        elements.form = document.getElementById('commentForm');
        elements.commentsList = document.getElementById('commentsList');
        elements.loadingIndicator = document.getElementById('commentsLoading');
        elements.emptyState = document.getElementById('commentsEmpty');
        elements.commentsCount = document.getElementById('commentsCount');
        elements.submitBtn = document.getElementById('submitCommentBtn');
        elements.formMessage = document.getElementById('formMessage');
        
        if (!elements.form || !elements.commentsList) {
            console.error('Required elements not found');
            return;
        }
        
        // Setup event listeners
        elements.form.addEventListener('submit', handleFormSubmit);
        setupRealtimeValidation();
        
        // Load comments
        loadAndRenderComments();
    }

    // ===========================
    // Start when DOM is ready
    // ===========================
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
