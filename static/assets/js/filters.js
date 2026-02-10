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
        console.log('[Filter System] 🔍 Starting filter process...');
        console.log('[Filter System] 📋 Criteria:', {
            timeRange: `${minTime}-${maxTime}`,
            difficulties: difficulties,
            labRequired: labRequired,
            postTypes: postTypes
        });
        
        const articles = document.querySelectorAll('.article-card');
        let visibleCount = 0;
        
        articles.forEach((article, index) => {
            let show = true;
            const reasons = [];
            
            // Get article data
            const articleTimeStr = article.dataset.readingTime;
            const articleTime = articleTimeStr && articleTimeStr !== '' && articleTimeStr !== '0' ? parseInt(articleTimeStr) : 0;
            const articleDifficulty = article.dataset.difficulty || '';
            const articleLabRequired = article.dataset.labRequired === 'true';
            const articlePostType = article.dataset.postType || '';
            
            console.log(`[Article ${index + 1}] 📄 Data:`, {
                time: articleTime,
                difficulty: articleDifficulty,
                lab: articleLabRequired,
                type: articlePostType
            });
            
            // ===== فیلتر مدت زمان =====
            if (articleTime > 0) {
                // مقاله زمان دارد - چک کنیم در محدوده باشد
                if (articleTime < minTime || articleTime > maxTime) {
                    show = false;
                    reasons.push(`⏱️ Time ${articleTime} NOT in range [${minTime}-${maxTime}]`);
                } else {
                    console.log(`[Article ${index + 1}] ⏱️ Time ${articleTime} OK (in range)`);
                }
            } else {
                // مقاله زمان ندارد
                if (minTime > 0) {
                    // اگر کاربر محدوده‌ای بالاتر از 0 انتخاب کرده، این مقاله را رد کن
                    show = false;
                    reasons.push(`⏱️ Article has no time, but min filter is ${minTime}`);
                } else {
                    console.log(`[Article ${index + 1}] ⏱️ No time, but filter allows it`);
                }
            }
            
            // ===== فیلتر سطح دشواری =====
            if (difficulties.length === 0) {
                // هیچ سطحی انتخاب نشده - همه را رد کن
                show = false;
                reasons.push(`📊 No difficulty selected`);
            } else if (difficulties.length === 4) {
                // همه سطوح انتخاب شده - همه را نشان بده
                console.log(`[Article ${index + 1}] 📊 Difficulty: ALL selected`);
            } else {
                // فقط بعضی سطوح انتخاب شده
                if (articleDifficulty === '') {
                    // مقاله سطح دشواری ندارد - رد کن
                    show = false;
                    reasons.push(`📊 No difficulty, but filter active [${difficulties.join(', ')}]`);
                } else if (!difficulties.includes(articleDifficulty)) {
                    // سطح مقاله در لیست انتخاب شده نیست
                    show = false;
                    reasons.push(`📊 Difficulty "${articleDifficulty}" NOT in [${difficulties.join(', ')}]`);
                } else {
                    console.log(`[Article ${index + 1}] 📊 Difficulty "${articleDifficulty}" OK`);
                }
            }
            
            // ===== فیلتر Lab Required =====
            if (labRequired.length === 0) {
                // هیچکدام انتخاب نشده - همه را رد کن
                show = false;
                reasons.push(`🔬 No lab option selected`);
            } else if (labRequired.length === 2) {
                // هر دو انتخاب شده - همه را نشان بده
                console.log(`[Article ${index + 1}] 🔬 Lab: BOTH selected`);
            } else {
                // فقط یکی انتخاب شده
                const needsLab = labRequired.includes('true');
                if (articleLabRequired !== needsLab) {
                    show = false;
                    reasons.push(`🔬 Lab ${articleLabRequired} NOT match filter ${needsLab}`);
                } else {
                    console.log(`[Article ${index + 1}] 🔬 Lab ${articleLabRequired} OK`);
                }
            }
            
            // ===== فیلتر نوع پست =====
            if (postTypes.length === 0) {
                // هیچ نوعی انتخاب نشده - همه را رد کن
                show = false;
                reasons.push(`📄 No post type selected`);
            } else if (postTypes.length === 7) {
                // همه انواع انتخاب شده - همه را نشان بده
                console.log(`[Article ${index + 1}] 📄 Type: ALL selected`);
            } else {
                // فقط بعضی انواع انتخاب شده
                if (articlePostType === '') {
                    // مقاله نوع ندارد - رد کن
                    show = false;
                    reasons.push(`📄 No type, but filter active [${postTypes.join(', ')}]`);
                } else if (!postTypes.includes(articlePostType)) {
                    // نوع مقاله در لیست انتخاب شده نیست
                    show = false;
                    reasons.push(`📄 Type "${articlePostType}" NOT in [${postTypes.join(', ')}]`);
                } else {
                    console.log(`[Article ${index + 1}] 📄 Type "${articlePostType}" OK`);
                }
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
        
        console.log(`[Filter System] ✅ Filter complete. Visible: ${visibleCount}/${articles.length}`);
        
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
            let labRequired = false; // پیش‌فرض false
            let postType = null;
            
            badges.forEach((badge, badgeIndex) => {
                const badgeText = badge.querySelector('.badge-text');
                if (!badgeText) {
                    console.warn(`[Article ${index + 1}][Badge ${badgeIndex + 1}] No badge-text found`);
                    return;
                }
                
                const text = badgeText.textContent.trim();
                console.log(`[Article ${index + 1}][Badge ${badgeIndex + 1}] Text: "${text}", Classes: ${badge.className}`);
                
                // Reading Time - استخراج عدد از متن فارسی
                if (badge.classList.contains('badge-time')) {
                    // متن مثل "10 دقیقه" یا "15 دقیقه"
                    const match = text.match(/(\d+)/);
                    if (match) {
                        readingTime = parseInt(match[1]);
                        console.log(`[Article ${index + 1}] ✅ Reading Time: ${readingTime} minutes`);
                    } else {
                        console.warn(`[Article ${index + 1}] ⚠️ Could not parse reading time from: "${text}"`);
                    }
                }
                
                // Difficulty - تشخیص از class
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
                    console.log(`[Article ${index + 1}] ✅ Difficulty: ${difficulty} (${text})`);
                }
                
                // Lab Required - اگر badge وجود داشت یعنی true
                if (badge.classList.contains('badge-lab')) {
                    labRequired = true;
                    console.log(`[Article ${index + 1}] ✅ Lab Required: true`);
                }
                
                // Post Type - مقدار فارسی
                if (badge.classList.contains('badge-type')) {
                    postType = text; // مقدار فارسی مثل "آموزشی", "مقاله"
                    console.log(`[Article ${index + 1}] ✅ Post Type: "${postType}"`);
                }
            });
            
            // ذخیره در dataset
            article.dataset.readingTime = readingTime !== null ? readingTime : '0';
            article.dataset.difficulty = difficulty !== null ? difficulty : '';
            article.dataset.labRequired = labRequired ? 'true' : 'false';
            article.dataset.postType = postType !== null ? postType : '';
            
            console.log(`[Article ${index + 1}] 📊 Final data:`, {
                readingTime: article.dataset.readingTime,
                difficulty: article.dataset.difficulty,
                labRequired: article.dataset.labRequired,
                postType: article.dataset.postType
            });
        });
        
        console.log('[Filter System] ✅ Data extraction complete');
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
        
        // دریافت ترتیب مرتب‌سازی
        const sortOrderElement = document.querySelector('input[name="sort_order"]:checked');
        const sortOrder = sortOrderElement ? sortOrderElement.value : 'newest';
        
        console.log('[Filter System] Filter criteria:', {
            minTime,
            maxTime,
            selectedDifficulties,
            selectedLabRequired,
            selectedPostTypes,
            sortOrder
        });
        
        // بررسی اینکه کدام سیستم در دسترس است
        if (typeof window.applyLoadMoreFilter === 'function') {
            // استفاده از سیستم Load More (اولویت اول)
            console.log('[Filter System] Using Load More filter system');
            const count = window.applyLoadMoreFilter(function(article) {
                return matchesFilter(article, minTime, maxTime, selectedDifficulties, selectedLabRequired, selectedPostTypes);
            }, sortOrder);
            updateFilterResults(count);
            showNoResultsMessage(count);
        } else if (typeof window.applyArticlesFilter === 'function') {
            // استفاده از Articles Loader قدیمی
            console.log('[Filter System] Using Articles Loader filter system');
            const count = window.applyArticlesFilter(function(article) {
                return matchesFilter(article, minTime, maxTime, selectedDifficulties, selectedLabRequired, selectedPostTypes);
            });
            updateFilterResults(count);
            showNoResultsMessage(count);
        } else {
            // Fallback به فیلتر DOM-based
            console.log('[Filter System] Using DOM-based filter (fallback)');
            filterArticles(minTime, maxTime, selectedDifficulties, selectedLabRequired, selectedPostTypes);
        }
        
        window.closeFilterModal();
    };
    
    // Check if article matches filter criteria
    function matchesFilter(article, minTime, maxTime, difficulties, labRequired, postTypes) {
        const articleTime = article.readingTime || 0;
        const articleDifficulty = article.difficulty || '';
        const articleLabRequired = article.labRequired || false;
        const articlePostType = article.postType || '';
        
        // Reading Time
        if (articleTime > 0) {
            if (articleTime < minTime || articleTime > maxTime) {
                return false;
            }
        } else {
            if (minTime > 0) {
                return false;
            }
        }
        
        // Difficulty
        if (difficulties.length === 0) {
            return false;
        } else if (difficulties.length === 4) {
            // All selected
        } else {
            if (articleDifficulty === '') {
                return false;
            } else if (!difficulties.includes(articleDifficulty)) {
                return false;
            }
        }
        
        // Lab Required
        if (labRequired.length === 0) {
            return false;
        } else if (labRequired.length === 2) {
            // Both selected
        } else {
            const needsLab = labRequired.includes('true');
            if (articleLabRequired !== needsLab) {
                return false;
            }
        }
        
        // Post Type
        if (postTypes.length === 0) {
            return false;
        } else if (postTypes.length === 7) {
            // All selected
        } else {
            if (articlePostType === '') {
                return false;
            } else if (!postTypes.includes(articlePostType)) {
                return false;
            }
        }
        
        return true;
    }
    
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
        
        // بررسی اینکه کدام سیستم در دسترس است
        if (typeof window.resetLoadMoreFilter === 'function') {
            // استفاده از سیستم Load More (اولویت اول)
            console.log('[Filter System] Using Load More reset');
            window.resetLoadMoreFilter();
            const count = window.getTotalArticlesCount();
            updateFilterResults(count);
            showNoResultsMessage(count > 0 ? count : 1);
        } else if (typeof window.resetArticlesFilter === 'function') {
            // استفاده از Articles Loader قدیمی
            console.log('[Filter System] Using Articles Loader reset');
            window.resetArticlesFilter();
            const allArticles = window.getAllArticles();
            updateFilterResults(allArticles ? allArticles.length : 0);
            showNoResultsMessage(allArticles ? allArticles.length : 1);
        } else {
            // Fallback: Apply filters (show all)
            console.log('[Filter System] Using fallback reset');
            window.applyFilters();
        }
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
