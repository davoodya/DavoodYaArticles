// ===========================
// Filter System for Articles
// ===========================

(function() {
    'use strict';
    
    // Initialize filters on page load
    document.addEventListener('DOMContentLoaded', function() {
        // Check if we're on a page with articles
        const articles = document.querySelectorAll('.article-card');
        if (articles.length === 0) {
            // Hide filter elements if no articles
            hideFilterElements();
            return;
        }
        
        initializeFilters();
        setupRangeSliders();
        updateFilterResults();
    });
    
    // Hide filter elements when no articles present
    function hideFilterElements() {
        const filterWidget = document.querySelector('.sidebar-widget:has(.filter-dropdown-btn)');
        const floatingBtn = document.querySelector('.floating-filter-btn');
        
        if (filterWidget) filterWidget.style.display = 'none';
        if (floatingBtn) floatingBtn.style.display = 'none';
    }
    
    // Initialize filter system
    function initializeFilters() {
        const articles = document.querySelectorAll('.article-card');
        
        articles.forEach(article => {
            const badges = article.querySelectorAll('.article-badge, .article-card-badges .article-badge');
            let readingTime = 0;
            let difficulty = '';
            let labRequired = false;
            let postType = '';
            
            badges.forEach(badge => {
                // Reading Time
                if (badge.classList.contains('badge-time')) {
                    const timeText = badge.querySelector('.badge-text').textContent;
                    const match = timeText.match(/(\d+)/);
                    if (match) {
                        readingTime = parseInt(match[1]);
                    }
                }
                
                // Difficulty
                if (badge.classList.contains('badge-difficulty')) {
                    if (badge.classList.contains('badge-beginner')) difficulty = 'beginner';
                    else if (badge.classList.contains('badge-medium')) difficulty = 'medium';
                    else if (badge.classList.contains('badge-intermediate')) difficulty = 'intermediate';
                    else if (badge.classList.contains('badge-advanced')) difficulty = 'advanced';
                }
                
                // Lab Required
                if (badge.classList.contains('badge-lab')) {
                    labRequired = true;
                }
                
                // Post Type
                if (badge.classList.contains('badge-type')) {
                    postType = badge.querySelector('.badge-text').textContent.trim();
                }
            });
            
            // Set data attributes
            article.dataset.readingTime = readingTime;
            article.dataset.difficulty = difficulty;
            article.dataset.labRequired = labRequired;
            article.dataset.postType = postType;
        });
    }
    
    // Setup range sliders
    function setupRangeSliders() {
        // Desktop sliders
        setupSliderPair(
            'readingTimeMinRange',
            'readingTimeMaxRange',
            'readingTimeMin',
            'readingTimeMax'
        );
        
        // Mobile sliders
        setupSliderPair(
            'mobileReadingTimeMinRange',
            'mobileReadingTimeMaxRange',
            'mobileReadingTimeMin',
            'mobileReadingTimeMax'
        );
    }
    
    // Setup a pair of min/max sliders
    function setupSliderPair(minRangeId, maxRangeId, minValueId, maxValueId) {
        const minRange = document.getElementById(minRangeId);
        const maxRange = document.getElementById(maxRangeId);
        const minValue = document.getElementById(minValueId);
        const maxValue = document.getElementById(maxValueId);
        
        if (!minRange || !maxRange || !minValue || !maxValue) return;
        
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
    
    // Apply filters (Desktop)
    window.applyFilters = function() {
        const minTime = parseInt(document.getElementById('readingTimeMinRange').value);
        const maxTime = parseInt(document.getElementById('readingTimeMaxRange').value);
        
        const selectedDifficulties = Array.from(document.querySelectorAll('input[name="difficulty"]:checked'))
            .map(input => input.value);
        
        const selectedLabRequired = Array.from(document.querySelectorAll('input[name="lab_required"]:checked'))
            .map(input => input.value === 'true');
        
        const selectedPostTypes = Array.from(document.querySelectorAll('input[name="post_type"]:checked'))
            .map(input => input.value);
        
        filterArticles(minTime, maxTime, selectedDifficulties, selectedLabRequired, selectedPostTypes);
    };
    
    // Apply filters (Mobile)
    window.applyMobileFilters = function() {
        const minTime = parseInt(document.getElementById('mobileReadingTimeMinRange').value);
        const maxTime = parseInt(document.getElementById('mobileReadingTimeMaxRange').value);
        
        const selectedDifficulties = Array.from(document.querySelectorAll('input[name="mobile-difficulty"]:checked'))
            .map(input => input.value);
        
        const selectedLabRequired = Array.from(document.querySelectorAll('input[name="mobile-lab_required"]:checked'))
            .map(input => input.value === 'true');
        
        const selectedPostTypes = Array.from(document.querySelectorAll('input[name="mobile-post_type"]:checked'))
            .map(input => input.value);
        
        filterArticles(minTime, maxTime, selectedDifficulties, selectedLabRequired, selectedPostTypes);
        closeMobileFilters();
    };
    
    // Main filter function
    function filterArticles(minTime, maxTime, difficulties, labRequired, postTypes) {
        const articles = document.querySelectorAll('.article-card');
        let visibleCount = 0;
        
        articles.forEach(article => {
            let show = true;
            
            // Reading Time filter
            const articleTime = parseInt(article.dataset.readingTime) || 0;
            if (articleTime > 0 && (articleTime < minTime || articleTime > maxTime)) {
                show = false;
            }
            
            // Difficulty filter
            const articleDifficulty = article.dataset.difficulty;
            if (articleDifficulty && difficulties.length > 0) {
                if (!difficulties.includes(articleDifficulty)) {
                    show = false;
                }
            }
            
            // Lab Required filter
            const articleLabRequired = article.dataset.labRequired === 'true';
            if (labRequired.length > 0 && labRequired.length < 2) {
                if (!labRequired.includes(articleLabRequired)) {
                    show = false;
                }
            }
            
            // Post Type filter
            const articlePostType = article.dataset.postType;
            if (articlePostType && postTypes.length > 0) {
                if (!postTypes.includes(articlePostType)) {
                    show = false;
                }
            }
            
            // Show or hide article with animation
            if (show) {
                article.style.display = '';
                article.style.animation = 'fadeIn 0.4s ease';
                visibleCount++;
            } else {
                article.style.animation = 'fadeOut 0.3s ease';
                setTimeout(() => {
                    article.style.display = 'none';
                }, 300);
            }
        });
        
        updateFilterResults(visibleCount);
        
        // Show message if no results
        showNoResultsMessage(visibleCount);
        
        // Scroll to top of articles (desktop only)
        const articlesGrid = document.querySelector('.articles-grid');
        if (articlesGrid && window.innerWidth >= 768) {
            articlesGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
    
    // Show/hide no results message
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
    
    // Reset filters (Desktop)
    window.resetFilters = function() {
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
        applyFilters();
    };
    
    // Reset filters (Mobile)
    window.resetMobileFilters = function() {
        // Reset range sliders
        document.getElementById('mobileReadingTimeMinRange').value = 0;
        document.getElementById('mobileReadingTimeMaxRange').value = 60;
        document.getElementById('mobileReadingTimeMin').textContent = 0;
        document.getElementById('mobileReadingTimeMax').textContent = 60;
        
        // Check all checkboxes
        document.querySelectorAll('input[name="mobile-difficulty"]').forEach(input => input.checked = true);
        document.querySelectorAll('input[name="mobile-lab_required"]').forEach(input => input.checked = true);
        document.querySelectorAll('input[name="mobile-post_type"]').forEach(input => input.checked = true);
        
        // Apply filters (show all)
        applyMobileFilters();
    };
    
    // Update filter results count
    function updateFilterResults(count) {
        const resultsElement = document.getElementById('filterResultsCount');
        if (resultsElement) {
            if (count === undefined) {
                const articles = document.querySelectorAll('.article-card');
                count = articles.length;
            }
            resultsElement.textContent = `${count} مقاله یافت شد`;
        }
    }
    
    // Mobile filter modal functions
    window.openMobileFilters = function() {
        const modal = document.getElementById('mobileFilterModal');
        const overlay = document.getElementById('mobileFilterOverlay');
        
        if (modal && overlay) {
            modal.classList.add('active');
            overlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    };
    
    window.closeMobileFilters = function() {
        const modal = document.getElementById('mobileFilterModal');
        const overlay = document.getElementById('mobileFilterOverlay');
        
        if (modal && overlay) {
            modal.classList.remove('active');
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    };
    
    // Close mobile filters on ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const modal = document.getElementById('mobileFilterModal');
            if (modal && modal.classList.contains('active')) {
                closeMobileFilters();
            }
        }
    });
    
    // Add fade animations
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
            padding: 4rem 2rem;
            background: linear-gradient(135deg, rgba(58, 173, 223, 0.05) 0%, rgba(0, 255, 65, 0.05) 100%);
            border: 2px dashed rgba(58, 173, 223, 0.3);
            border-radius: 16px;
            margin: 2rem 0;
            animation: fadeIn 0.5s ease;
        }
        
        .filter-no-results .no-results-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
            opacity: 0.5;
        }
        
        .filter-no-results h3 {
            color: var(--accent-blue);
            font-family: var(--persian-heading);
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        
        .filter-no-results p {
            color: var(--secondary-text);
            font-size: 1rem;
            margin: 0;
        }
        
        @media (max-width: 768px) {
            .filter-no-results {
                padding: 3rem 1.5rem;
            }
            
            .filter-no-results .no-results-icon {
                font-size: 3rem;
            }
            
            .filter-no-results h3 {
                font-size: 1.3rem;
            }
            
            .filter-no-results p {
                font-size: 0.95rem;
            }
        }
    `;
    document.head.appendChild(style);
    
})();
