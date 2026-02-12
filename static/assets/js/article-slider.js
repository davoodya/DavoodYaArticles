/**
 * Article Slider - Previous & Next Articles
 * Version: 3.0.0 - Complete Rewrite with Visible Cards Fix
 * Using simple transform-based sliding with guaranteed visibility
 */

(function() {
    'use strict';
    
    // Configuration
    const CONFIG = {
        CARDS_PER_VIEW_DESKTOP: 2,
        CARDS_PER_VIEW_MOBILE: 1,
        BREAKPOINT: 1024,
        GAP: 24, // pixels
        ANIMATION_DURATION: 500 // ms
    };
    
    // Check if slider exists
    const slider = document.querySelector('.article-slider');
    if (!slider) {
        console.warn('Article slider not found on page');
        return;
    }
    
    const track = slider.querySelector('.slider-track');
    const cards = slider.querySelectorAll('.slider-card');
    const prevBtn = slider.querySelector('.slider-nav-prev');
    const nextBtn = slider.querySelector('.slider-nav-next');
    const dots = slider.querySelectorAll('.slider-dot');
    
    // Validation
    if (!track || cards.length < 2) {
        console.warn('Not enough slider cards or track missing');
        return;
    }
    
    console.log('🚀 Article Slider V3.0 Initializing...');
    console.log('📊 Total cards:', cards.length);
    
    // State
    let state = {
        currentPage: 0,
        cardsPerView: CONFIG.CARDS_PER_VIEW_DESKTOP,
        totalPages: 0,
        isAnimating: false,
        isDragging: false,
        startX: 0,
        currentX: 0,
        translateX: 0
    };
    
    /**
     * Calculate cards per view based on window width
     */
    function updateCardsPerView() {
        const width = window.innerWidth;
        state.cardsPerView = width <= CONFIG.BREAKPOINT ? 
            CONFIG.CARDS_PER_VIEW_MOBILE : 
            CONFIG.CARDS_PER_VIEW_DESKTOP;
        
        state.totalPages = Math.ceil(cards.length / state.cardsPerView);
        
        console.log('📱 Screen width:', width);
        console.log('🎴 Cards per view:', state.cardsPerView);
        console.log('📄 Total pages:', state.totalPages);
    }
    
    /**
     * Get card width including gap
     */
    function getCardWidth() {
        if (cards.length === 0) return 0;
        
        // Get computed width of first card
        const card = cards[0];
        const rect = card.getBoundingClientRect();
        const width = rect.width;
        
        console.log('📏 Card width:', width, 'Gap:', CONFIG.GAP);
        
        return width + CONFIG.GAP;
    }
    
    /**
     * Calculate translate value for current page
     */
    function calculateTranslate() {
        const cardWidth = getCardWidth();
        const cardsToSkip = state.currentPage * state.cardsPerView;
        const translate = -(cardsToSkip * cardWidth);
        
        console.log('🔢 Calculate:', {
            page: state.currentPage,
            cardsPerView: state.cardsPerView,
            cardsToSkip: cardsToSkip,
            cardWidth: cardWidth,
            translate: translate
        });
        
        return translate;
    }
    
    /**
     * Update slider position
     */
    function updatePosition(animated = true) {
        if (state.isAnimating) return;
        
        const translate = calculateTranslate();
        state.translateX = translate;
        
        // Apply transform
        if (animated) {
            track.style.transition = `transform ${CONFIG.ANIMATION_DURATION}ms cubic-bezier(0.4, 0, 0.2, 1)`;
            state.isAnimating = true;
            
            setTimeout(() => {
                state.isAnimating = false;
            }, CONFIG.ANIMATION_DURATION);
        } else {
            track.style.transition = 'none';
        }
        
        track.style.transform = `translate3d(${translate}px, 0, 0)`;
        
        console.log('✅ Position updated:', {
            page: state.currentPage,
            translate: translate,
            animated: animated
        });
        
        updateDots();
        updateButtons();
    }
    
    /**
     * Update dots
     */
    function updateDots() {
        dots.forEach((dot, index) => {
            const isActive = index === state.currentPage;
            dot.classList.toggle('active', isActive);
            dot.setAttribute('aria-selected', isActive);
        });
    }
    
    /**
     * Update buttons (always enabled for loop)
     */
    function updateButtons() {
        if (prevBtn) {
            prevBtn.disabled = false;
            prevBtn.style.opacity = '1';
        }
        if (nextBtn) {
            nextBtn.disabled = false;
            nextBtn.style.opacity = '1';
        }
    }
    
    /**
     * Go to specific page
     */
    function goToPage(pageIndex, animated = true) {
        // Loop logic
        if (pageIndex < 0) {
            state.currentPage = state.totalPages - 1;
        } else if (pageIndex >= state.totalPages) {
            state.currentPage = 0;
        } else {
            state.currentPage = pageIndex;
        }
        
        console.log('📄 Going to page:', state.currentPage);
        updatePosition(animated);
    }
    
    /**
     * Next page
     */
    function nextPage() {
        console.log('➡️ Next page');
        goToPage(state.currentPage + 1);
    }
    
    /**
     * Previous page
     */
    function prevPage() {
        console.log('⬅️ Previous page');
        goToPage(state.currentPage - 1);
    }
    
    /**
     * Start from middle page
     */
    function startFromMiddle() {
        if (state.totalPages > 1) {
            const middlePage = Math.floor(state.totalPages / 2);
            state.currentPage = middlePage;
            console.log('🎯 Starting from middle page:', middlePage);
        } else {
            state.currentPage = 0;
        }
        updatePosition(false);
    }
    
    /**
     * Touch/Drag handlers
     */
    function handleTouchStart(e) {
        state.isDragging = true;
        state.startX = e.type.includes('mouse') ? e.pageX : e.touches[0].clientX;
        track.style.transition = 'none';
        track.style.cursor = 'grabbing';
    }
    
    function handleTouchMove(e) {
        if (!state.isDragging) return;
        
        state.currentX = e.type.includes('mouse') ? e.pageX : e.touches[0].clientX;
        const diff = state.currentX - state.startX;
        const newTranslate = state.translateX + diff;
        
        track.style.transform = `translate3d(${newTranslate}px, 0, 0)`;
    }
    
    function handleTouchEnd() {
        if (!state.isDragging) return;
        
        state.isDragging = false;
        track.style.cursor = 'grab';
        
        const diff = state.currentX - state.startX;
        const threshold = 50;
        
        if (Math.abs(diff) > threshold) {
            if (diff > 0) {
                prevPage();
            } else {
                nextPage();
            }
        } else {
            updatePosition(true);
        }
    }
    
    /**
     * Keyboard navigation
     */
    function handleKeyboard(e) {
        if (e.key === 'ArrowLeft') {
            prevPage();
            e.preventDefault();
        } else if (e.key === 'ArrowRight') {
            nextPage();
            e.preventDefault();
        }
    }
    
    /**
     * Initialize events
     */
    function initEvents() {
        // Button clicks
        if (prevBtn) {
            prevBtn.addEventListener('click', (e) => {
                e.preventDefault();
                prevPage();
            });
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', (e) => {
                e.preventDefault();
                nextPage();
            });
        }
        
        // Dot clicks
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                console.log('⭕ Dot clicked:', index);
                goToPage(index);
            });
        });
        
        // Touch/Mouse events
        const container = slider.querySelector('.slider-track-container');
        if (container) {
            container.addEventListener('touchstart', handleTouchStart, { passive: true });
            container.addEventListener('touchmove', handleTouchMove, { passive: true });
            container.addEventListener('touchend', handleTouchEnd);
            
            container.addEventListener('mousedown', handleTouchStart);
            container.addEventListener('mousemove', handleTouchMove);
            container.addEventListener('mouseup', handleTouchEnd);
            container.addEventListener('mouseleave', handleTouchEnd);
            
            container.style.cursor = 'grab';
        }
        
        // Keyboard
        slider.addEventListener('keydown', handleKeyboard);
        slider.setAttribute('tabindex', '0');
        
        // Prevent image drag
        cards.forEach(card => {
            const images = card.querySelectorAll('img');
            images.forEach(img => {
                img.addEventListener('dragstart', (e) => e.preventDefault());
            });
        });
        
        // Window resize
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                console.log('📐 Window resized');
                updateCardsPerView();
                updatePosition(false);
            }, 250);
        });
    }
    
    /**
     * Force card visibility
     */
    function forceCardVisibility() {
        cards.forEach((card, index) => {
            // Remove any display:none
            card.style.display = 'flex';
            card.style.visibility = 'visible';
            card.style.opacity = '1';
            
            // Ensure proper flex properties
            if (window.innerWidth > CONFIG.BREAKPOINT) {
                card.style.flex = '0 0 calc(50% - 12px)';
                card.style.minWidth = 'calc(50% - 12px)';
                card.style.maxWidth = 'calc(50% - 12px)';
            } else {
                card.style.flex = '0 0 100%';
                card.style.minWidth = '100%';
                card.style.maxWidth = '100%';
            }
            
            console.log(`🎴 Card ${index + 1} forced visible`);
        });
    }
    
    /**
     * Initialize slider
     */
    function init() {
        console.log('🔧 Initializing Article Slider V3.0...');
        
        // Calculate initial state
        updateCardsPerView();
        
        // Force all cards to be visible
        forceCardVisibility();
        
        // Start from middle
        startFromMiddle();
        
        // Initialize events
        initEvents();
        
        // Mark as loaded
        slider.classList.add('slider-loaded');
        
        console.log('✅ Article Slider initialized successfully!');
        console.log('📊 State:', state);
    }
    
    // Start initialization
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Expose API for debugging
    window.articleSlider = {
        goToPage: goToPage,
        nextPage: nextPage,
        prevPage: prevPage,
        getState: () => ({ ...state }),
        forceVisibility: forceCardVisibility,
        debug: () => {
            console.log('🐛 === Debug Info ===');
            console.log('Current page:', state.currentPage);
            console.log('Total pages:', state.totalPages);
            console.log('Cards per view:', state.cardsPerView);
            console.log('Total cards:', cards.length);
            console.log('Translate X:', state.translateX);
            console.log('Track transform:', track.style.transform);
            console.log('Track styles:', {
                display: track.style.display,
                visibility: track.style.visibility,
                opacity: track.style.opacity
            });
            cards.forEach((card, i) => {
                const rect = card.getBoundingClientRect();
                console.log(`Card ${i + 1}:`, {
                    visible: rect.width > 0 && rect.height > 0,
                    rect: rect,
                    display: card.style.display,
                    visibility: card.style.visibility
                });
            });
        }
    };
    
})();
