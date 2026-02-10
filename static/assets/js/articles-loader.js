// ===========================
// Articles Loader - Client-Side Pagination & Filtering
// ===========================

(function() {
    'use strict';
    
    // Global state
    let allArticles = [];
    let filteredArticles = [];
    let currentPage = 1;
    const articlesPerPage = 10;
    
    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        console.log('[Articles Loader] Initializing...');
        
        // Check if we're on a list page
        const articlesGrid = document.querySelector('.articles-grid');
        if (!articlesGrid) {
            console.log('[Articles Loader] Not a list page, skipping');
            return;
        }
        
        // Load articles from JSON
        loadArticlesFromJSON();
    });
    
    // Load articles from JSON endpoint
    async function loadArticlesFromJSON() {
        try {
            console.log('[Articles Loader] Loading articles from JSON...');
            
            // Get current page URL to construct JSON URL
            const currentPath = window.location.pathname;
            const jsonUrl = currentPath.endsWith('/') 
                ? `${currentPath}index.json` 
                : `${currentPath}/index.json`;
            
            console.log('[Articles Loader] Fetching:', jsonUrl);
            
            const response = await fetch(jsonUrl);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            allArticles = await response.json();
            console.log(`[Articles Loader] ✅ Loaded ${allArticles.length} articles`);
            
            // Initially, filtered = all
            filteredArticles = [...allArticles];
            
            // Render first page
            renderArticles();
            
            // Setup pagination
            setupPagination();
            
        } catch (error) {
            console.error('[Articles Loader] ❌ Error loading articles:', error);
            // Fallback: use existing HTML articles
            console.log('[Articles Loader] Falling back to existing HTML');
        }
    }
    
    // Render articles for current page
    function renderArticles() {
        const articlesGrid = document.querySelector('.articles-grid');
        if (!articlesGrid) return;
        
        console.log(`[Articles Loader] Rendering page ${currentPage} of ${Math.ceil(filteredArticles.length / articlesPerPage)}`);
        
        // Calculate pagination
        const startIndex = (currentPage - 1) * articlesPerPage;
        const endIndex = startIndex + articlesPerPage;
        const pageArticles = filteredArticles.slice(startIndex, endIndex);
        
        console.log(`[Articles Loader] Showing articles ${startIndex + 1}-${Math.min(endIndex, filteredArticles.length)} of ${filteredArticles.length}`);
        
        // Clear existing articles
        articlesGrid.innerHTML = '';
        
        // Render each article
        pageArticles.forEach(article => {
            const articleEl = createArticleElement(article);
            articlesGrid.appendChild(articleEl);
        });
        
        // Update pagination UI
        updatePaginationUI();
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    // Create article HTML element
    function createArticleElement(article) {
        const articleEl = document.createElement('article');
        articleEl.className = 'article-card';
        
        // Set data attributes for filtering
        articleEl.dataset.readingTime = article.readingTime || '0';
        articleEl.dataset.difficulty = article.difficulty || '';
        articleEl.dataset.labRequired = article.labRequired ? 'true' : 'false';
        articleEl.dataset.postType = article.postType || '';
        
        let html = `
            <h2 class="article-card-title">
                <a href="${article.url}">${article.title}</a>
            </h2>
        `;
        
        // Featured image
        if (article.featuredImage) {
            html += `
                <div class="article-card-image">
                    <a href="${article.url}">
                        <img src="${article.featuredImage}" alt="${article.title}" loading="lazy">
                    </a>
                </div>
            `;
        }
        
        // Summary
        if (article.summary) {
            html += `
                <div class="article-card-summary">
                    ${article.summary}
                </div>
            `;
        }
        
        // Tags
        if (article.tags && article.tags.length > 0) {
            html += `
                <div class="article-card-tags">
                    <div class="tags-label">
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M21.41 11.58l-9-9C12.05 2.22 11.55 2 11 2H4c-1.1 0-2 .9-2 2v7c0 .55.22 1.05.59 1.42l9 9c.36.36.86.58 1.41.58.55 0 1.05-.22 1.41-.59l7-7c.37-.36.59-.86.59-1.41 0-.55-.23-1.06-.59-1.42zM5.5 7C4.67 7 4 6.33 4 5.5S4.67 4 5.5 4 7 4.67 7 5.5 6.33 7 5.5 7z"/>
                        </svg>
                        <span>تگ‌ها:</span>
                    </div>
            `;
            article.tags.slice(0, 4).forEach(tag => {
                html += `<a href="/tags/${encodeURIComponent(tag).toLowerCase()}/" class="article-tag">${tag}</a>`;
            });
            html += `</div>`;
        }
        
        // Footer with badges and read more
        html += `<div class="article-card-footer">
            <a href="${article.url}" class="read-more-btn">ادامه مطلب ←</a>`;
        
        // Badges
        const hasBadges = article.readingTime || article.difficulty || article.labRequired || article.postType;
        if (hasBadges) {
            html += `<div class="article-card-badges">`;
            
            // Reading time
            if (article.readingTime) {
                html += `
                    <span class="article-badge badge-time">
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm.5-13H11v6l5.2 3.2.8-1.3-4.5-2.7V7z"/>
                        </svg>
                        <span class="badge-text">${article.readingTime} دقیقه</span>
                    </span>
                `;
            }
            
            // Difficulty
            if (article.difficulty) {
                const difficultyMap = {
                    'beginner': { text: 'مبتدی', class: 'badge-beginner' },
                    'medium': { text: 'متوسط', class: 'badge-medium' },
                    'intermediate': { text: 'حرفه‌ای', class: 'badge-intermediate' },
                    'advanced': { text: 'تخصصی', class: 'badge-advanced' }
                };
                const diff = difficultyMap[article.difficulty] || { text: article.difficulty, class: '' };
                html += `
                    <span class="article-badge badge-difficulty ${diff.class}">
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                        </svg>
                        <span class="badge-text">${diff.text}</span>
                    </span>
                `;
            }
            
            // Lab required
            if (article.labRequired) {
                html += `
                    <span class="article-badge badge-lab">
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M7 2v11h3v9l7-12h-4l4-8z"/>
                        </svg>
                        <span class="badge-text">تمرین عملی</span>
                    </span>
                `;
            }
            
            // Post type
            if (article.postType) {
                html += `
                    <span class="article-badge badge-type">
                        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/>
                        </svg>
                        <span class="badge-text">${article.postType}</span>
                    </span>
                `;
            }
            
            html += `</div>`;
        }
        
        html += `</div>`;
        
        articleEl.innerHTML = html;
        return articleEl;
    }
    
    // Setup pagination controls
    function setupPagination() {
        // Find or create pagination container
        let paginationEl = document.querySelector('.pagination');
        if (!paginationEl) {
            paginationEl = document.createElement('nav');
            paginationEl.className = 'pagination';
            const articlesGrid = document.querySelector('.articles-grid');
            if (articlesGrid && articlesGrid.parentNode) {
                articlesGrid.parentNode.insertBefore(paginationEl, articlesGrid.nextSibling);
            }
        }
        
        updatePaginationUI();
    }
    
    // Update pagination UI
    function updatePaginationUI() {
        const paginationEl = document.querySelector('.pagination');
        if (!paginationEl) return;
        
        const totalPages = Math.ceil(filteredArticles.length / articlesPerPage);
        
        if (totalPages <= 1) {
            paginationEl.style.display = 'none';
            return;
        }
        
        paginationEl.style.display = 'flex';
        
        let html = '<ul>';
        
        // Previous button
        if (currentPage > 1) {
            html += `<li><a href="#" data-page="${currentPage - 1}" class="prev">← قبلی</a></li>`;
        }
        
        // Page numbers
        for (let i = 1; i <= totalPages; i++) {
            if (i === currentPage) {
                html += `<li><span class="active">${i}</span></li>`;
            } else if (i === 1 || i === totalPages || Math.abs(i - currentPage) <= 2) {
                html += `<li><a href="#" data-page="${i}">${i}</a></li>`;
            } else if (i === currentPage - 3 || i === currentPage + 3) {
                html += `<li><span>...</span></li>`;
            }
        }
        
        // Next button
        if (currentPage < totalPages) {
            html += `<li><a href="#" data-page="${currentPage + 1}" class="next">بعدی →</a></li>`;
        }
        
        html += '</ul>';
        paginationEl.innerHTML = html;
        
        // Add event listeners
        paginationEl.querySelectorAll('a[data-page]').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const page = parseInt(this.dataset.page);
                goToPage(page);
            });
        });
    }
    
    // Go to specific page
    function goToPage(page) {
        currentPage = page;
        renderArticles();
    }
    
    // Apply filters (called from filters.js)
    window.applyArticlesFilter = function(filterFn) {
        console.log('[Articles Loader] Applying filter to all articles');
        
        filteredArticles = allArticles.filter(filterFn);
        currentPage = 1; // Reset to first page
        
        console.log(`[Articles Loader] Filtered: ${filteredArticles.length} / ${allArticles.length} articles`);
        
        renderArticles();
        
        return filteredArticles.length;
    };
    
    // Reset filter (show all)
    window.resetArticlesFilter = function() {
        console.log('[Articles Loader] Resetting filter');
        filteredArticles = [...allArticles];
        currentPage = 1;
        renderArticles();
    };
    
    // Get all articles (for filter initialization)
    window.getAllArticles = function() {
        return allArticles;
    };
    
    console.log('[Articles Loader] Loaded successfully');
    
})();
