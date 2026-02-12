/**
 * Article Slider - Previous & Next Articles
 * Enhanced version with loop navigation, dots navigation, and middle start
 * Version: 2.0.0
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
        }
    }
    
    // Update slider position based on current page
    function updateSliderPosition(animated = true) {
        const cardWidth = cards[0].offsetWidth;
        const gap = 24; // 1.5rem
        const offset = -(currentPage * cardsPerView * (cardWidth + gap));
        
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
        }
        
        if (nextBtn) {
            nextBtn.disabled = false;
        }
    }
    
    // Update dots
    function updateDots() {
        dots.forEach((dot, index) => {
            const isActive = index === currentPage;
            dot.classList.toggle('active', isActive);
            dot.setAttribute('aria-selected', isActive);
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
        
        updateSliderPosition(animated);
    }
    
    // Next page (with loop)
    function nextPage() {
        goToPage(currentPage + 1);
    }
    
    // Previous page (with loop)
    function prevPage() {
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
        
        track.style.cursor = 'grabbing';
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
        
        track.style.cursor = 'grab';
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
            prevBtn.addEventListener('click', prevPage);
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', nextPage);
        }
        
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => goToPage(index));
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
            updateSliderPosition(false);
        }
    }
    
    // Initialize slider
    function init() {
        updateCardsPerView();
        startFromMiddle(); // Start from middle instead of first page
        initTouchEvents();
        initButtonEvents();
        initKeyboardNav();
        
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
        
        // Log info for debugging
        console.log('Article Slider initialized:', {
            totalCards: cards.length,
            cardsPerView: cardsPerView,
            totalPages: totalPages,
            startPage: currentPage
        });
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
        
        // Optional: Resume after inactivity
        // setTimeout(() => startAutoplay(), 10000);
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
        getTotalPages: () => totalPages
    };
    
})();
