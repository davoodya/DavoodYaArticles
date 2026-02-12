/**
 * Article Slider - Previous & Next Articles
 * Enhanced version with loop navigation, dots navigation, and middle start
 * Version: 2.1.0 - Fixed card display issue
 */

(function() {
    'use strict';
    
    // Check if slider exists on the page
    const slider = document.querySelector('.article-slider');
    if (!slider) return;
    
    const track = slider.querySelector('.slider-track');
    const cards = slider.querySelectorAll('.slider-card');
    const prevBtn = slider.querySelector('.slider-nav-prev');
    const nextBtn = slider.querySelector('.slider-nav-next');
    const dots = slider.querySelectorAll('.slider-dot');
    
    // Exit if not enough cards
    if (!track || cards.length < 2) return;
    
    // State
    let currentPage = 0;
    let cardsPerView = 2;
    let totalPages = Math.ceil(cards.length / cardsPerView);
    let isDragging = false;
    let startPos = 0;
    let currentTranslate = 0;
    let prevTranslate = 0;
    let animationID = 0;
    
    console.log('Initial state:', {
        totalCards: cards.length,
        cardsPerView: cardsPerView,
        totalPages: totalPages
    });
    
    // Calculate cards per view based on viewport width
    function updateCardsPerView() {
        const width = window.innerWidth;
        const oldCardsPerView = cardsPerView;
        cardsPerView = width <= 1024 ? 1 : 2;
        
        // Recalculate total pages if cards per view changed
        if (oldCardsPerView !== cardsPerView) {
            totalPages = Math.ceil(cards.length / cardsPerView);
            // Adjust current page if needed
            if (currentPage >= totalPages) {
                currentPage = totalPages - 1;
            }
            
            console.log('Cards per view updated:', {
                cardsPerView: cardsPerView,
                totalPages: totalPages,
                currentPage: currentPage
            });
        }
    }
    
    // Get card width including gap
    function getCardWidthWithGap() {
        if (cards.length === 0) return 0;
        
        const cardWidth = cards[0].offsetWidth;
        const gap = 24; // 1.5rem = 24px
        
        return cardWidth + gap;
    }
    
    // Update slider position based on current page
    function updateSliderPosition(animated = true) {
        const cardWidthWithGap = getCardWidthWithGap();
        
        // Calculate offset: number of cards to skip * card width
        const cardsToSkip = currentPage * cardsPerView;
        const offset = -(cardsToSkip * cardWidthWithGap);
        
        console.log('Updating position:', {
            currentPage: currentPage,
            cardsPerView: cardsPerView,
            cardsToSkip: cardsToSkip,
            cardWidthWithGap: cardWidthWithGap,
            offset: offset
        });
        
        if (animated) {
            track.style.transition = 'transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        } else {
            track.style.transition = 'none';
        }
        
        track.style.transform = `translateX(${offset}px)`;
        currentTranslate = offset;
        prevTranslate = offset;
        
        updateNavButtons();
        updateDots();
    }
    
    // Update navigation button states (no disable for loop)
    function updateNavButtons() {
        // In loop mode, buttons are always enabled
        if (prevBtn) {
            prevBtn.disabled = false;
            prevBtn.style.opacity = '1';
            prevBtn.style.cursor = 'pointer';
        }
        
        if (nextBtn) {
            nextBtn.disabled = false;
            nextBtn.style.opacity = '1';
            nextBtn.style.cursor = 'pointer';
        }
    }
    
    // Update dots
    function updateDots() {
        dots.forEach((dot, index) => {
            const isActive = index === currentPage;
            dot.classList.toggle('active', isActive);
            dot.setAttribute('aria-selected', isActive);
        });
        
        console.log('Dots updated:', {
            totalDots: dots.length,
            activeDot: currentPage
        });
    }
    
    // Go to specific page
    function goToPage(pageIndex, animated = true) {
        // Loop around if out of bounds
        if (pageIndex < 0) {
            currentPage = totalPages - 1;
        } else if (pageIndex >= totalPages) {
            currentPage = 0;
        } else {
            currentPage = pageIndex;
        }
        
        console.log('Going to page:', {
            requestedPage: pageIndex,
            actualPage: currentPage,
            totalPages: totalPages
        });
        
        updateSliderPosition(animated);
    }
    
    // Next page (with loop)
    function nextPage() {
        console.log('Next page clicked');
        goToPage(currentPage + 1);
    }
    
    // Previous page (with loop)
    function prevPage() {
        console.log('Previous page clicked');
        goToPage(currentPage - 1);
    }
    
    // Touch/Mouse handlers
    function getPositionX(event) {
        return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
    }
    
    function touchStart(event) {
        isDragging = true;
        startPos = getPositionX(event);
        animationID = requestAnimationFrame(animation);
        
        const trackContainer = slider.querySelector('.slider-track-container');
        if (trackContainer) {
            trackContainer.style.cursor = 'grabbing';
        }
        track.style.transition = 'none';
    }
    
    function touchMove(event) {
        if (isDragging) {
            const currentPosition = getPositionX(event);
            currentTranslate = prevTranslate + currentPosition - startPos;
        }
    }
    
    function touchEnd() {
        isDragging = false;
        cancelAnimationFrame(animationID);
        
        const movedBy = currentTranslate - prevTranslate;
        
        // Swipe threshold: 50px
        if (movedBy < -50) {
            nextPage();
        } else if (movedBy > 50) {
            prevPage();
        } else {
            updateSliderPosition();
        }
        
        const trackContainer = slider.querySelector('.slider-track-container');
        if (trackContainer) {
            trackContainer.style.cursor = 'grab';
        }
        track.style.transition = 'transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
    }
    
    function animation() {
        if (isDragging) {
            track.style.transform = `translateX(${currentTranslate}px)`;
            requestAnimationFrame(animation);
        }
    }
    
    // Keyboard navigation
    function handleKeyboard(event) {
        if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
            const direction = document.dir === 'rtl' ? -1 : 1;
            
            if (event.key === 'ArrowLeft') {
                direction === 1 ? prevPage() : nextPage();
            } else {
                direction === 1 ? nextPage() : prevPage();
            }
            
            event.preventDefault();
        }
    }
    
    // Initialize touch events
    function initTouchEvents() {
        // Touch events on track container
        const trackContainer = slider.querySelector('.slider-track-container');
        
        if (trackContainer) {
            // Touch events
            trackContainer.addEventListener('touchstart', touchStart, { passive: true });
            trackContainer.addEventListener('touchmove', touchMove, { passive: true });
            trackContainer.addEventListener('touchend', touchEnd);
            
            // Mouse events
            trackContainer.addEventListener('mousedown', touchStart);
            trackContainer.addEventListener('mousemove', touchMove);
            trackContainer.addEventListener('mouseup', touchEnd);
            trackContainer.addEventListener('mouseleave', () => {
                if (isDragging) touchEnd();
            });
        }
        
        // Prevent image dragging
        cards.forEach(card => {
            const images = card.querySelectorAll('img');
            images.forEach(img => {
                img.addEventListener('dragstart', (e) => e.preventDefault());
            });
        });
    }
    
    // Initialize button events
    function initButtonEvents() {
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
        
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                console.log('Dot clicked:', index);
                goToPage(index);
            });
            dot.addEventListener('keypress', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    goToPage(index);
                    e.preventDefault();
                }
            });
        });
    }
    
    // Initialize keyboard navigation
    function initKeyboardNav() {
        slider.addEventListener('keydown', handleKeyboard);
        
        // Focus management
        slider.setAttribute('tabindex', '0');
    }
    
    // Handle window resize
    let resizeTimer;
    function handleResize() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            console.log('Window resized');
            updateCardsPerView();
            updateSliderPosition(false);
        }, 250);
    }
    
    // Start from middle page
    function startFromMiddle() {
        if (totalPages > 1) {
            // Calculate middle page (rounded down)
            const middlePage = Math.floor(totalPages / 2);
            currentPage = middlePage;
            
            console.log('Starting from middle:', {
                totalPages: totalPages,
                middlePage: middlePage
            });
            
            updateSliderPosition(false);
        } else {
            // If only 1 page, start from 0
            currentPage = 0;
            updateSliderPosition(false);
        }
    }
    
    // Initialize slider
    function init() {
        console.log('=== Article Slider Initializing ===');
        console.log('Total cards found:', cards.length);
        
        // Set initial cards per view
        updateCardsPerView();
        
        // Calculate and log initial state
        console.log('Initial calculation:', {
            totalCards: cards.length,
            cardsPerView: cardsPerView,
            totalPages: totalPages,
            cardWidth: cards[0]?.offsetWidth,
            gap: 24
        });
        
        // Start from middle
        startFromMiddle();
        
        // Initialize events
        initTouchEvents();
        initButtonEvents();
        initKeyboardNav();
        
        // Add resize listener
        window.addEventListener('resize', handleResize);
        
        // Set cursor style
        const trackContainer = slider.querySelector('.slider-track-container');
        if (trackContainer) {
            trackContainer.style.cursor = 'grab';
        }
        
        // Add loaded class for animation
        setTimeout(() => {
            slider.classList.add('slider-loaded');
        }, 100);
        
        console.log('=== Article Slider Initialized ===');
        console.log('Starting page:', currentPage);
        console.log('Total pages:', totalPages);
    }
    
    // Auto-play (optional - disabled by default)
    let autoplayInterval;
    function startAutoplay(interval = 5000) {
        stopAutoplay();
        autoplayInterval = setInterval(() => {
            nextPage();
        }, interval);
    }
    
    function stopAutoplay() {
        if (autoplayInterval) {
            clearInterval(autoplayInterval);
            autoplayInterval = null;
        }
    }
    
    // Pause autoplay on interaction
    function pauseOnInteraction() {
        stopAutoplay();
    }
    
    slider.addEventListener('mouseenter', pauseOnInteraction);
    slider.addEventListener('touchstart', pauseOnInteraction, { passive: true });
    
    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Cleanup on page unload
    window.addEventListener('beforeunload', () => {
        stopAutoplay();
        window.removeEventListener('resize', handleResize);
    });
    
    // Expose public methods for debugging (optional)
    window.articleSlider = {
        goToPage: goToPage,
        nextPage: nextPage,
        prevPage: prevPage,
        getCurrentPage: () => currentPage,
        getTotalPages: () => totalPages,
        getCardsPerView: () => cardsPerView,
        getTotalCards: () => cards.length,
        debug: () => {
            console.log('=== Debug Info ===');
            console.log('Current page:', currentPage);
            console.log('Total pages:', totalPages);
            console.log('Cards per view:', cardsPerView);
            console.log('Total cards:', cards.length);
            console.log('Card width:', cards[0]?.offsetWidth);
            console.log('Current translate:', currentTranslate);
            console.log('Track transform:', track.style.transform);
        }
    };
    
})();
