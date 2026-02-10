// ===========================
// Filter System for Articles
// ===========================

(function() {
    'use strict';
    
    // Update filter results count - تابع قابل دسترسی در scope module
    function updateFilterResults(count) {
        const resultsElement = document.getElementById('filterResultsCount');
        if (resultsElement) {
            if (count === undefined) {
                const articles = document.querySelectorAll('.article-card');
                count = articles.length;
            }
            resultsElement.textContent = `${count} مقاله یافت شد`;
            console.log(`[Filter System] Results updated: ${count} articles`);
        }
    }
    
    // Show/hide no results message - تابع قابل دسترسی در scope module
    function showNoResultsMessage(count) {
        let messageEl = document.querySelector('.filter-no-results');
        const articlesGrid = document.querySelector('.articles-grid');
        
        if (count === 0) {
            if (!messageEl) {
                messageEl = document.createElement('div');
                messageEl.className = 'filter-no-results';
                messageEl.innerHTML = `
                    <div class="no-results-icon">🔍</div>
                    <h3>هیچ مقاله‌ای یافت نشد</h3>
                    <p>لطفاً فیلترهای خود را تغییر دهید یا بازنشانی کنید</p>
                `;
                if (articlesGrid) {
                    articlesGrid.after(messageEl);
                }
            }
            if (messageEl) {
                messageEl.style.display = 'block';
            }
        } else {
            if (messageEl) {
                messageEl.style.display = 'none';
            }
        }
    }
    
    // Main filter function - تابع قابل دسترسی در scope module
    function filterArticles(minTime, maxTime, difficulties, labRequired, postTypes) {
        console.log('[Filter System] Starting filter process...');
        
        const articles = document.querySelectorAll('.article-card');
        let visibleCount = 0;
        
        articles.forEach((article, index) => {
            let show = true;
            const reasons = [];
            
            // Get article data
            const articleTimeStr = article.dataset.readingTime;
            const articleTime = articleTimeStr !== '' ? parseInt(articleTimeStr) : null;
            const articleDifficulty = article.dataset.difficulty || null;
            const articleLabRequired = article.dataset.labRequired === 'true';
            const articlePostType = article.dataset.postType || null;
            
            console.log(`[Article ${index + 1}] Checking:`, {
                articleTime,
                articleDifficulty,
                articleLabRequired,
                articlePostType
            });
            
            // Reading Time filter
            if (articleTime !== null && articleTime > 0) {
                if (articleTime < minTime || articleTime > maxTime) {
                    show = false;
                    reasons.push(`Time ${articleTime} not in range [${minTime}, ${maxTime}]`);
                }
            } else {
                if (minTime > 0) {
                    show = false;
                    reasons.push(`Article has no reading time, but minimum filter is ${minTime}`);
                }
            }
            
            // Difficulty filter
            if (articleDifficulty && difficulties.length > 0) {
                if (!difficulties.includes(articleDifficulty)) {
                    show = false;
                    reasons.push(`Difficulty "${articleDifficulty}" not in [${difficulties.join(', ')}]`);
                }
            } else if (!articleDifficulty && difficulties.length > 0 && difficulties.length < 4) {
                show = false;
                reasons.push(`Article has no difficulty, but filter is active`);
            }
            
            // Lab Required filter
            const labFilterValues = labRequired.map(val => val === 'true');
            
            if (labFilterValues.length > 0 && labFilterValues.length < 2) {
                const requiredValue = labFilterValues[0];
                if (articleLabRequired !== requiredValue) {
                    show = false;
                    reasons.push(`Lab required "${articleLabRequired}" does not match filter "${requiredValue}"`);
                }
            }
            
            // Post Type filter
            if (articlePostType && postTypes.length > 0) {
                if (!postTypes.includes(articlePostType)) {
                    show = false;
                    reasons.push(`Post type "${articlePostType}" not in [${postTypes.join(', ')}]`);
                }
            } else if (!articlePostType && postTypes.length > 0 && postTypes.length < 7) {
                show = false;
                reasons.push(`Article has no post type, but filter is active`);
            }
            
            // Show or hide article with animation
            if (show) {
                console.log(`[Article ${index + 1}] ✅ VISIBLE`);
                article.style.display = '';
                article.style.animation = 'fadeIn 0.4s ease';
                visibleCount++;
            } else {
                console.log(`[Article ${index + 1}] ❌ HIDDEN - Reasons:`, reasons);
                article.style.animation = 'fadeOut 0.3s ease';
                setTimeout(() => {
                    article.style.display = 'none';
                }, 300);
            }
        });
        
        console.log(`[Filter System] Filter complete. Visible: ${visibleCount}/${articles.length}`);
        
        updateFilterResults(visibleCount);
        showNoResultsMessage(visibleCount);
        
        // Scroll to top of articles
        const articlesGrid = document.querySelector('.articles-grid');
        if (articlesGrid && window.innerWidth >= 768) {
            articlesGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
    
    // Initialize filters on page load
    document.addEventListener('DOMContentLoaded', function() {
        console.log('[Filter System] Initializing...');
        
        // Check if we're on a page with articles
        const articles = document.querySelectorAll('.article-card');
        console.log('[Filter System] Found articles:', articles.length);
        
        if (articles.length === 0) {
            console.log('[Filter System] No articles found, hiding filter elements');
            const floatingBtn = document.querySelector('.floating-filter-btn');
            if (floatingBtn) floatingBtn.style.display = 'none';
            return;
        }
        
        initializeFilters();
        setupRangeSliders();
        updateFilterResults();
        
        console.log('[Filter System] Initialization complete');
    });
    
    // Initialize filter system
    function initializeFilters() {
        const articles = document.querySelectorAll('.article-card');
        console.log('[Filter System] Extracting article data from', articles.length, 'articles');
        
        articles.forEach((article, index) => {
            const badges = article.querySelectorAll('.article-badge');
            console.log(`[Article ${index + 1}] Found ${badges.length} badges`);
            
            let readingTime = null;
            let difficulty = null;
            let labRequired = null;
            let postType = null;
            
            badges.forEach((badge, badgeIndex) => {
                const badgeText = badge.querySelector('.badge-text');
                if (!badgeText) {
                    console.warn(`[Article ${index + 1}][Badge ${badgeIndex + 1}] No badge-text found`);
                    return;
                }
                
                const text = badgeText.textContent.trim();
                console.log(`[Article ${index + 1}][Badge ${badgeIndex + 1}] Text: "${text}"`);
                
                // Reading Time
                if (badge.classList.contains('badge-time')) {
                    const match = text.match(/(\d+)/);
                    if (match) {
                        readingTime = parseInt(match[1]);
                        console.log(`[Article ${index + 1}] Reading Time: ${readingTime} minutes`);
                    }
                }
                
                // Difficulty
                if (badge.classList.contains('badge-difficulty')) {
                    if (badge.classList.contains('badge-beginner')) {
                        difficulty = 'beginner';
                    } else if (badge.classList.contains('badge-medium')) {
                        difficulty = 'medium';
                    } else if (badge.classList.contains('badge-intermediate')) {
                        difficulty = 'intermediate';
                    } else if (badge.classList.contains('badge-advanced')) {
                        difficulty = 'advanced';
                    }
                    console.log(`[Article ${index + 1}] Difficulty: ${difficulty}`);
                }
                
                // Lab Required
                if (badge.classList.contains('badge-lab')) {
                    labRequired = true;
                    console.log(`[Article ${index + 1}] Lab Required: true`);
                }
                
                // Post Type
                if (badge.classList.contains('badge-type')) {
                    postType = text;
                    console.log(`[Article ${index + 1}] Post Type: ${postType}`);
                }
            });
            
            if (labRequired === null) {
                labRequired = false;
            }
            
            article.dataset.readingTime = readingTime !== null ? readingTime : '';
            article.dataset.difficulty = difficulty !== null ? difficulty : '';
            article.dataset.labRequired = labRequired;
            article.dataset.postType = postType !== null ? postType : '';
            
            console.log(`[Article ${index + 1}] Final data:`, {
                readingTime,
                difficulty,
                labRequired,
                postType
            });
        });
        
        console.log('[Filter System] Data extraction complete');
    }
    
    // Setup range sliders
    function setupRangeSliders() {
        console.log('[Filter System] Setting up range sliders');
        
        setupSliderPair(
            'readingTimeMinRange',
            'readingTimeMaxRange',
            'readingTimeMin',
            'readingTimeMax'
        );
    }
    
    // Setup a pair of min/max sliders
    function setupSliderPair(minRangeId, maxRangeId, minValueId, maxValueId) {
        const minRange = document.getElementById(minRangeId);
        const maxRange = document.getElementById(maxRangeId);
        const minValue = document.getElementById(minValueId);
        const maxValue = document.getElementById(maxValueId);
        
        if (!minRange || !maxRange || !minValue || !maxValue) {
            console.warn(`[Filter System] Slider pair not found: ${minRangeId}`);
            return;
        }
        
        console.log(`[Filter System] Setting up slider pair: ${minRangeId}`);
        
        minRange.addEventListener('input', function() {
            let min = parseInt(this.value);
            let max = parseInt(maxRange.value);
            
            if (min > max - 5) {
                min = max - 5;
                this.value = min;
            }
            
            minValue.textContent = min;
        });
        
        maxRange.addEventListener('input', function() {
            let max = parseInt(this.value);
            let min = parseInt(minRange.value);
            
            if (max < min + 5) {
                max = min + 5;
                this.value = max;
            }
            
            maxValue.textContent = max;
        });
    }
    
    // ===========================
    // Global Functions (accessible from HTML onclick)
    // ===========================
    
    // Apply filters
    window.applyFilters = function() {
        console.log('[Filter System] Applying filters...');
        
        const minTime = parseInt(document.getElementById('readingTimeMinRange').value);
        const maxTime = parseInt(document.getElementById('readingTimeMaxRange').value);
        
        const selectedDifficulties = Array.from(document.querySelectorAll('input[name="difficulty"]:checked'))
            .map(input => input.value);
        
        const selectedLabRequired = Array.from(document.querySelectorAll('input[name="lab_required"]:checked'))
            .map(input => input.value);
        
        const selectedPostTypes = Array.from(document.querySelectorAll('input[name="post_type"]:checked'))
            .map(input => input.value);
        
        console.log('[Filter System] Filter criteria:', {
            minTime,
            maxTime,
            selectedDifficulties,
            selectedLabRequired,
            selectedPostTypes
        });
        
        filterArticles(minTime, maxTime, selectedDifficulties, selectedLabRequired, selectedPostTypes);
        window.closeFilterModal();
    };
    
    // Reset filters
    window.resetFilters = function() {
        console.log('[Filter System] Resetting filters...');
        
        // Reset range sliders
        document.getElementById('readingTimeMinRange').value = 0;
        document.getElementById('readingTimeMaxRange').value = 60;
        document.getElementById('readingTimeMin').textContent = 0;
        document.getElementById('readingTimeMax').textContent = 60;
        
        // Check all checkboxes
        document.querySelectorAll('input[name="difficulty"]').forEach(input => input.checked = true);
        document.querySelectorAll('input[name="lab_required"]').forEach(input => input.checked = true);
        document.querySelectorAll('input[name="post_type"]').forEach(input => input.checked = true);
        
        // Apply filters (show all)
        window.applyFilters();
    };
    
    // Open filter modal
    window.openFilterModal = function() {
        console.log('[Filter System] Opening filter modal...');
        const modal = document.getElementById('filterModal');
        const overlay = document.getElementById('filterModalOverlay');
        
        if (modal && overlay) {
            modal.classList.add('active');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
            
            // Update results count when modal opens
            updateFilterResults();
        } else {
            console.error('[Filter System] Modal or overlay not found!');
        }
    };
    
    // Close filter modal
    window.closeFilterModal = function() {
        console.log('[Filter System] Closing filter modal...');
        const modal = document.getElementById('filterModal');
        const overlay = document.getElementById('filterModalOverlay');
        
        if (modal && overlay) {
            modal.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    };
    
    // Close filter modal on ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const modal = document.getElementById('filterModal');
            if (modal && modal.classList.contains('active')) {
                window.closeFilterModal();
            }
        }
    });
    
    // Add fade animations and styles
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes fadeOut {
            from { opacity: 1; transform: translateY(0); }
            to { opacity: 0; transform: translateY(-20px); }
        }
        
        .filter-no-results {
            text-align: center;
            padding: 60px 20px;
            background: rgba(255, 255, 255, 0.05);
            border: 2px dashed rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            margin: 40px 0;
        }
        
        .filter-no-results .no-results-icon {
            font-size: 64px;
            margin-bottom: 20px;
            opacity: 0.5;
        }
        
        .filter-no-results h3 {
            color: #00ff41;
            margin-bottom: 10px;
            font-size: 24px;
        }
        
        .filter-no-results p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 16px;
        }
    `;
    document.head.appendChild(style);
    
    console.log('[Filter System] Loaded successfully');
    
})();
