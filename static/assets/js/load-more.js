// ===========================
// Load More System for Articles
// با قابلیت فیلتر کردن تمام مقالات
// ===========================

(function() {
    'use strict';
    
    // تنظیمات
    const ARTICLES_PER_LOAD = 4; // تعداد مقالات در هر بار بارگذاری
    
    // State Management
    let allArticlesData = []; // تمام مقالات از JSON
    let filteredArticlesData = []; // مقالات فیلتر شده
    let displayedCount = 0; // تعداد مقالات نمایش داده شده
    let isFilterActive = false; // آیا فیلتر فعال است؟
    let currentSortOrder = 'newest'; // ترتیب مرتب‌سازی: 'newest' یا 'oldest'
    
    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        console.log('[Load More] 🚀 Initializing Load More System...');
        
        // بررسی اینکه در صفحه لیست هستیم
        const articlesGrid = document.querySelector('.articles-grid');
        if (!articlesGrid) {
            console.log('[Load More] ❌ Not a list page, skipping');
            return;
        }
        
        // بارگذاری مقالات از JSON
        loadArticlesFromJSON();
    });
    
    // بارگذاری تمام مقالات از JSON
    async function loadArticlesFromJSON() {
        try {
            console.log('[Load More] 📥 Loading articles from JSON...');
            
            // ساخت URL برای JSON
            const currentPath = window.location.pathname;
            const jsonUrl = currentPath.endsWith('/') 
                ? `${currentPath}index.json` 
                : `${currentPath}/index.json`;
            
            console.log('[Load More] 🌐 Fetching:', jsonUrl);
            
            const response = await fetch(jsonUrl);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            // بررسی اینکه آیا داده معتبر است
            if (!data || (Array.isArray(data) && data.length === 0)) {
                throw new Error('Empty JSON data');
            }
            
            allArticlesData = parseArticlesFromJSON(data);
            
            // مرتب‌سازی پیش‌فرض: جدیدترین اول
            allArticlesData = sortArticles(allArticlesData, currentSortOrder);
            filteredArticlesData = [...allArticlesData];
            
            console.log(`[Load More] ✅ Loaded ${allArticlesData.length} articles from JSON (sorted: ${currentSortOrder})`);
            
            // اگر هیچ مقاله‌ای نیست، به HTML fallback کن
            if (allArticlesData.length === 0) {
                throw new Error('No articles in JSON');
            }
            
            // پاک کردن مقالات HTML موجود
            const articlesGrid = document.querySelector('.articles-grid');
            articlesGrid.innerHTML = '';
            
            // نمایش اولین دسته از مقالات
            displayedCount = 0;
            loadMoreArticles();
            
            // حذف pagination قدیمی Hugo
            const oldPagination = document.querySelector('.pagination');
            if (oldPagination) {
                oldPagination.remove();
            }
            
            // ایجاد دکمه بارگذاری بیشتر (فقط اگر بیشتر از 4 مقاله باشد)
            if (allArticlesData.length > ARTICLES_PER_LOAD) {
                createLoadMoreButton();
            }
            
        } catch (error) {
            console.error('[Load More] ❌ Error loading articles:', error);
            console.log('[Load More] 📌 Falling back to existing HTML');
            fallbackToHTML();
        }
    }
    
    // تبدیل داده‌های JSON به فرمت قابل استفاده
    function parseArticlesFromJSON(data) {
        console.log('[Load More] 🔄 Parsing JSON data...');
        
        // بررسی ساختار JSON
        if (Array.isArray(data)) {
            return data.map(parseArticle);
        } else if (data.articles) {
            return data.articles.map(parseArticle);
        } else {
            console.error('[Load More] ❌ Unexpected JSON structure:', data);
            return [];
        }
    }
    
    // پردازش یک مقاله از JSON
    function parseArticle(item) {
        return {
            title: item.title || '',
            url: item.url || item.permalink || '',
            summary: item.summary || item.description || '',
            featuredImage: item.featuredImage || item.featured_image || item.image || '',
            tags: item.tags || [],
            readingTime: item.readingTime || item.reading_time || 0,
            difficulty: item.difficulty || '',
            labRequired: item.labRequired || item.lab_required || false,
            postType: item.postType || item.post_type_fa || '',
            categoryTitle: item.categoryTitle || '',
            categoryUrl: item.categoryUrl || '',
            date: item.date || '',
            dateUnix: item.dateUnix || 0
        };
    }
    
    // Fallback به HTML موجود (اگر JSON کار نکرد)
    function fallbackToHTML() {
        console.log('[Load More] 🔄 Using HTML articles as fallback');
        
        const articles = document.querySelectorAll('.article-card');
        
        if (articles.length === 0) {
            console.log('[Load More] ❌ No articles found in HTML either');
            return;
        }
        
        allArticlesData = Array.from(articles).map(extractArticleFromHTML);
        filteredArticlesData = [...allArticlesData];
        
        // پنهان کردن مقالات بعد از 4 تای اول
        articles.forEach((article, index) => {
            if (index >= ARTICLES_PER_LOAD) {
                article.style.display = 'none';
            }
        });
        
        displayedCount = Math.min(ARTICLES_PER_LOAD, articles.length);
        
        console.log(`[Load More] 📊 Fallback: ${displayedCount} articles displayed, ${allArticlesData.length} total`);
        
        // حذف pagination قدیمی
        const oldPagination = document.querySelector('.pagination');
        if (oldPagination) {
            oldPagination.remove();
        }
        
        // فقط اگر بیشتر از 4 مقاله وجود داشته باشد دکمه را نمایش بده
        if (allArticlesData.length > ARTICLES_PER_LOAD) {
            createLoadMoreButton();
        }
    }
    
    // استخراج اطلاعات مقاله از HTML موجود
    function extractArticleFromHTML(articleEl) {
        const titleLink = articleEl.querySelector('.article-card-title a');
        const summaryEl = articleEl.querySelector('.article-card-summary');
        const imageEl = articleEl.querySelector('.article-card-image img');
        const tags = Array.from(articleEl.querySelectorAll('.article-tag')).map(tag => tag.textContent.trim());
        
        // استخراج اطلاعات از data attributes
        const readingTime = parseInt(articleEl.getAttribute('data-reading-time') || articleEl.dataset.readingTime || '0');
        const difficulty = articleEl.getAttribute('data-difficulty') || articleEl.dataset.difficulty || '';
        const labRequired = (articleEl.getAttribute('data-lab-required') || articleEl.dataset.labRequired || 'false') === 'true';
        const postType = articleEl.getAttribute('data-post-type') || articleEl.dataset.postType || '';
        
        // استخراج اطلاعات دسته‌بندی (برای all-articles)
        const categoryLink = articleEl.querySelector('.article-card-category .category-link');
        const categoryTitle = categoryLink ? categoryLink.textContent.trim() : '';
        const categoryUrl = categoryLink ? categoryLink.getAttribute('href') : '';
        
        console.log(`[Load More] 📄 Extracted article: "${titleLink ? titleLink.textContent.trim() : 'Unknown'}"`, {
            readingTime,
            difficulty,
            labRequired,
            postType,
            category: categoryTitle
        });
        
        return {
            title: titleLink ? titleLink.textContent.trim() : '',
            url: titleLink ? titleLink.getAttribute('href') : '',
            summary: summaryEl ? summaryEl.innerHTML : '',
            featuredImage: imageEl ? imageEl.getAttribute('src') : '',
            tags: tags,
            readingTime: readingTime,
            difficulty: difficulty,
            labRequired: labRequired,
            postType: postType,
            categoryTitle: categoryTitle,
            categoryUrl: categoryUrl,
            htmlElement: articleEl // ذخیره المنت HTML برای استفاده بعدی
        };
    }
    
    // بارگذاری مقالات بیشتر
    function loadMoreArticles() {
        console.log('[Load More] 📤 Loading more articles...');
        
        const articlesGrid = document.querySelector('.articles-grid');
        if (!articlesGrid) {
            console.error('[Load More] ❌ Articles grid not found!');
            return;
        }
        
        const articlesToLoad = filteredArticlesData.slice(displayedCount, displayedCount + ARTICLES_PER_LOAD);
        
        if (articlesToLoad.length === 0) {
            console.log('[Load More] ℹ️ No more articles to load');
            return;
        }
        
        console.log(`[Load More] 📊 Loading ${articlesToLoad.length} articles (${displayedCount + 1}-${displayedCount + articlesToLoad.length} of ${filteredArticlesData.length})`);
        
        articlesToLoad.forEach(article => {
            let articleEl;
            
            // اگر المنت HTML از قبل وجود دارد از آن استفاده کن
            if (article.htmlElement) {
                articleEl = article.htmlElement;
                articleEl.style.display = '';
            } else {
                // در غیر این صورت المنت جدید بساز
                articleEl = createArticleElement(article);
            }
            
            // انیمیشن فقط برای مقالات جدید (نه اولین بار)
            if (displayedCount > 0) {
                articleEl.style.animation = 'fadeInUp 0.5s ease';
            }
            
            articlesGrid.appendChild(articleEl);
        });
        
        displayedCount += articlesToLoad.length;
        
        // به‌روزرسانی دکمه بارگذاری بیشتر
        updateLoadMoreButton();
        
        console.log(`[Load More] ✅ Now showing ${displayedCount} of ${filteredArticlesData.length} articles`);
    }
    
    // ایجاد المنت HTML مقاله
    function createArticleElement(article) {
        const articleEl = document.createElement('article');
        articleEl.className = 'article-card';
        
        // تنظیم dataset برای فیلترها
        articleEl.dataset.readingTime = article.readingTime || '0';
        articleEl.dataset.difficulty = article.difficulty || '';
        articleEl.dataset.labRequired = article.labRequired ? 'true' : 'false';
        articleEl.dataset.postType = article.postType || '';
        
        let html = `
            <h2 class="article-card-title">
                <a href="${article.url}">${article.title}</a>
            </h2>
        `;
        
        // تصویر شاخص
        if (article.featuredImage) {
            html += `
                <div class="article-card-image">
                    <a href="${article.url}">
                        <img src="${article.featuredImage}" alt="${article.title}" loading="lazy">
                    </a>
                </div>
            `;
        }
        
        // دسته‌بندی (فقط برای all-articles)
        if (article.categoryTitle && article.categoryUrl) {
            html += `
                <div class="article-card-category">
                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/>
                    </svg>
                    <a href="${article.categoryUrl}" class="category-link">
                        ${article.categoryTitle}
                    </a>
                </div>
            `;
        }
        
        // خلاصه
        if (article.summary) {
            html += `
                <div class="article-card-summary">
                    ${article.summary}
                </div>
            `;
        }
        
        // تگ‌ها
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
                html += `<a href="/tags/${encodeURIComponent(tag).toLowerCase()}/" class="article-tag" title="مشاهده همه مقالات با تگ ${tag}">${tag}</a>`;
            });
            html += `</div>`;
        }
        
        // Footer با badges و دکمه ادامه مطلب
        html += `<div class="article-card-footer">
            <a href="${article.url}" class="read-more-btn">ادامه مطلب ←</a>`;
        
        // Badges
        const hasBadges = article.readingTime || article.difficulty || article.labRequired || article.postType;
        if (hasBadges) {
            html += `<div class="article-card-badges">`;
            
            // مدت زمان مطالعه
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
            
            // سطح دشواری
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
            
            // نیاز به تمرین عملی
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
            
            // نوع پست
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
    
    // ایجاد دکمه بارگذاری بیشتر
    function createLoadMoreButton() {
        const articlesGrid = document.querySelector('.articles-grid');
        if (!articlesGrid) return;
        
        // ایجاد container برای دکمه
        const loadMoreContainer = document.createElement('div');
        loadMoreContainer.className = 'load-more-container';
        loadMoreContainer.id = 'loadMoreContainer';
        
        // ایجاد دکمه
        const loadMoreBtn = document.createElement('button');
        loadMoreBtn.className = 'load-more-btn';
        loadMoreBtn.id = 'loadMoreBtn';
        loadMoreBtn.innerHTML = `
            <svg class="load-more-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
            </svg>
            <span class="load-more-text">بارگذاری بیشتر</span>
            <span class="load-more-count">(${filteredArticlesData.length - displayedCount} مقاله باقی‌مانده)</span>
        `;
        
        loadMoreBtn.addEventListener('click', function() {
            loadMoreArticles();
        });
        
        loadMoreContainer.appendChild(loadMoreBtn);
        
        // اضافه کردن بعد از articles grid
        articlesGrid.parentNode.insertBefore(loadMoreContainer, articlesGrid.nextSibling);
        
        updateLoadMoreButton();
    }
    
    // به‌روزرسانی دکمه بارگذاری بیشتر
    function updateLoadMoreButton() {
        const loadMoreBtn = document.getElementById('loadMoreBtn');
        const loadMoreContainer = document.getElementById('loadMoreContainer');
        
        if (!loadMoreBtn || !loadMoreContainer) return;
        
        const remaining = filteredArticlesData.length - displayedCount;
        
        if (remaining <= 0) {
            // همه مقالات نمایش داده شده
            loadMoreContainer.style.display = 'none';
        } else {
            loadMoreContainer.style.display = 'flex';
            
            // به‌روزرسانی متن دکمه
            const countSpan = loadMoreBtn.querySelector('.load-more-count');
            if (countSpan) {
                countSpan.textContent = `(${remaining} مقاله باقی‌مانده)`;
            }
        }
    }
    
    // ===========================
    // API برای فیلترها
    // ===========================
    
    // تابع مرتب‌سازی مقالات
    function sortArticles(articles, order = 'newest') {
        console.log(`[Load More] 📊 Sorting articles by: ${order}`);
        
        const sorted = [...articles].sort((a, b) => {
            if (order === 'newest') {
                // جدیدترین اول
                return (b.dateUnix || 0) - (a.dateUnix || 0);
            } else {
                // قدیمی‌ترین اول
                return (a.dateUnix || 0) - (b.dateUnix || 0);
            }
        });
        
        console.log(`[Load More] ✅ Sorted ${sorted.length} articles`);
        return sorted;
    }
    
    // اعمال فیلتر روی تمام مقالات
    window.applyLoadMoreFilter = function(filterFunction, sortOrder = null) {
        console.log('[Load More] 🔍 Applying filter to all articles...');
        
        isFilterActive = true;
        
        // اگر ترتیب مرتب‌سازی داده شده، ذخیره کن
        if (sortOrder) {
            currentSortOrder = sortOrder;
            console.log(`[Load More] 📊 Sort order set to: ${currentSortOrder}`);
        }
        
        // فیلتر کردن تمام مقالات
        filteredArticlesData = allArticlesData.filter(article => {
            return filterFunction({
                readingTime: article.readingTime,
                difficulty: article.difficulty,
                labRequired: article.labRequired,
                postType: article.postType
            });
        });
        
        // مرتب‌سازی مقالات فیلتر شده
        filteredArticlesData = sortArticles(filteredArticlesData, currentSortOrder);
        
        console.log(`[Load More] ✅ Filtered: ${filteredArticlesData.length} of ${allArticlesData.length} articles`);
        
        // پاک کردن مقالات فعلی و شروع مجدد
        const articlesGrid = document.querySelector('.articles-grid');
        if (articlesGrid) {
            articlesGrid.innerHTML = '';
        }
        
        displayedCount = 0;
        loadMoreArticles();
        updateLoadMoreButton();
        
        // اسکرول به بالای grid مقالات
        if (articlesGrid && window.innerWidth >= 768) {
            setTimeout(() => {
                articlesGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
        
        return filteredArticlesData.length;
    };
    
    // حذف فیلتر و نمایش همه مقالات
    window.resetLoadMoreFilter = function() {
        console.log('[Load More] 🔄 Resetting filter...');
        
        isFilterActive = false;
        filteredArticlesData = [...allArticlesData];
        
        const articlesGrid = document.querySelector('.articles-grid');
        if (articlesGrid) {
            articlesGrid.innerHTML = '';
        }
        
        displayedCount = 0;
        loadMoreArticles();
        updateLoadMoreButton();
        
        console.log(`[Load More] ✅ Reset complete. Showing ${filteredArticlesData.length} articles`);
    };
    
    // دریافت تعداد کل مقالات
    window.getTotalArticlesCount = function() {
        return filteredArticlesData.length;
    };
    
    // دریافت تعداد مقالات نمایش داده شده
    window.getDisplayedArticlesCount = function() {
        return displayedCount;
    };
    
    console.log('[Load More] ✅ Load More System loaded successfully');
    
})();
