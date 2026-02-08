// Search System for Davoodya Website
// نظام جستجوی پیشرفته

// Global variables
let searchData = [];
let searchDataLoaded = false;

// Load search data from JSON
async function loadSearchData() {
    if (searchDataLoaded) return;
    
    try {
        // Get base URL from meta tag or current path
        const baseURL = document.querySelector('meta[name="base-url"]')?.content || '';
        const indexURL = baseURL ? `${baseURL}index.json` : '/index.json';
        
        const response = await fetch(indexURL);
        searchData = await response.json();
        searchDataLoaded = true;
        console.log('Search data loaded:', searchData.length, 'articles');
    } catch (error) {
        console.error('Error loading search data:', error);
    }
}

// Open search overlay
function openSearchOverlay() {
    const overlay = document.getElementById('searchOverlay');
    const searchInput = document.getElementById('searchInput');
    
    if (overlay && searchInput) {
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
        
        // Load data and focus input
        loadSearchData().then(() => {
            searchInput.focus();
        });
    }
}

// Close search overlay
function closeSearchOverlay() {
    const overlay = document.getElementById('searchOverlay');
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    
    if (overlay) {
        overlay.classList.remove('active');
        document.body.style.overflow = '';
        
        if (searchInput) searchInput.value = '';
        if (searchResults) searchResults.innerHTML = '';
    }
}

// Search function
function searchArticles(query, category = '', inline = false) {
    if (!query || query.length < 2) {
        const resultsEl = inline ? 
            document.getElementById('searchResultsInline') : 
            document.getElementById('searchResults');
        
        if (resultsEl) {
            resultsEl.innerHTML = inline ? '' : 
                '<p class="search-no-results">لطفاً حداقل 2 حرف وارد کنید</p>';
        }
        return;
    }
    
    const searchTerm = query.toLowerCase().trim();
    
    // Filter by category if selected
    let filteredData = searchData;
    if (category) {
        filteredData = searchData.filter(item => item.category === category);
    }
    
    // Search in title and tags
    const results = filteredData.filter(item => {
        const titleMatch = item.title.toLowerCase().includes(searchTerm);
        const tagsMatch = item.tags && item.tags.some(tag => 
            tag.toLowerCase().includes(searchTerm)
        );
        return titleMatch || tagsMatch;
    });
    
    displaySearchResults(results, inline);
}

// Display search results
function displaySearchResults(results, inline = false) {
    const resultsEl = inline ? 
        document.getElementById('searchResultsInline') : 
        document.getElementById('searchResults');
    
    if (!resultsEl) return;
    
    if (results.length === 0) {
        resultsEl.innerHTML = inline ? 
            '<p class="search-no-results-inline">نتیجه‌ای یافت نشد</p>' :
            '<p class="search-no-results">😔 متأسفانه نتیجه‌ای یافت نشد</p>';
        return;
    }
    
    const categoryMap = {
        'cyber-security': 'امنیت سایبری',
        'python': 'پایتون',
        'seo': 'سئو',
        'tools': 'ابزارها'
    };
    
    let html = inline ? '' : '<div class="search-results-grid">';
    
    results.forEach(item => {
        const categoryName = categoryMap[item.category] || item.category;
        const tagsHTML = item.tags && item.tags.length > 0 ? 
            item.tags.map(tag => `<span class="result-tag">${tag}</span>`).join('') : 
            '';
        
        if (inline) {
            html += `
                <a href="${item.permalink}" class="search-result-inline">
                    <h4 class="result-title-inline">${item.title}</h4>
                    <span class="result-category-inline">${categoryName}</span>
                </a>
            `;
        } else {
            html += `
                <article class="search-result-card">
                    <div class="result-header">
                        <span class="result-category">${categoryName}</span>
                        <span class="result-date">${item.date}</span>
                    </div>
                    <h3 class="result-title">
                        <a href="${item.permalink}">${item.title}</a>
                    </h3>
                    ${item.summary ? `<p class="result-summary">${item.summary}</p>` : ''}
                    ${tagsHTML ? `<div class="result-tags">${tagsHTML}</div>` : ''}
                    <a href="${item.permalink}" class="result-link">مشاهده مقاله →</a>
                </article>
            `;
        }
    });
    
    if (!inline) {
        html += '</div>';
        html = `<div class="search-results-count">🎯 ${results.length} نتیجه یافت شد</div>` + html;
    }
    
    resultsEl.innerHTML = html;
}

// Initialize search functionality
function initSearch() {
    // Event listeners for overlay search
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    
    if (searchInput) {
        // Debounce search
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const query = this.value;
                searchArticles(query, '', false);
            }, 300);
        });
    }
    
    // Close on ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeSearchOverlay();
        }
    });
    
    // Close on overlay click
    const overlay = document.getElementById('searchOverlay');
    if (overlay) {
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                closeSearchOverlay();
            }
        });
    }
    
    // Event listeners for inline search
    const searchInputInline = document.getElementById('searchInputInline');
    const categoryFilterInline = document.getElementById('categoryFilterInline');
    
    if (searchInputInline) {
        // Load data on first focus
        searchInputInline.addEventListener('focus', function() {
            loadSearchData();
        }, { once: true });
        
        // Debounce search
        let searchTimeoutInline;
        searchInputInline.addEventListener('input', function() {
            clearTimeout(searchTimeoutInline);
            searchTimeoutInline = setTimeout(() => {
                const query = this.value;
                searchArticles(query, '', true);
            }, 300);
        });
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSearch);
} else {
    initSearch();
}
