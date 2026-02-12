/**
 * Article Slider - Previous & Next Articles
 * Lightweight vanilla JS implementation with touch support
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
    let currentIndex = 0;
    let cardsPerView = 2;
    let isDragging = false;
    let startPos = 0;
    let currentTranslate = 0;
    let prevTranslate = 0;
    let animationID = 0;
    
    // Calculate cards per view based on viewport width
    function updateCardsPerView() {
        const width = window.innerWidth;
        cardsPerView = width <= 1024 ? 1 : 2;
    }
    
    // Calculate maximum index
    function getMaxIndex() {
        return Math.max(0, cards.length - cardsPerView);
    }
    
    // Update slider position
    function updateSliderPosition() {
        const cardWidth = cards[0].offsetWidth;
        const gap = 24; // 1.5rem
        const offset = -(currentIndex * (cardWidth + gap));
        
        track.style.transform = `translateX(${offset}px)`;
        currentTranslate = offset;
        prevTranslate = offset;
        
        updateNavButtons();
        updateDots();
    }
    
    // Update navigation button states
    function updateNavButtons() {
        const maxIndex = getMaxIndex();
        
        if (prevBtn) {
            prevBtn.disabled = currentIndex === 0;
        }
        
        if (nextBtn) {
            nextBtn.disabled = currentIndex >= maxIndex;
        }
    }
    
    // Update dots
    function updateDots() {
        dots.forEach((dot, index) => {
            const isActive = index === currentIndex;
            dot.classList.toggle('active', isActive);
            dot.setAttribute('aria-selected', isActive);
        });
    }
    
    // Go to specific slide
    function goToSlide(index) {
        const maxIndex = getMaxIndex();
        currentIndex = Math.max(0, Math.min(index, maxIndex));
        updateSliderPosition();
    }
    
    // Next slide
    function nextSlide() {
        const maxIndex = getMaxIndex();
        if (currentIndex < maxIndex) {
            currentIndex++;
            updateSliderPosition();
        }
    }
    
    // Previous slide
    function prevSlide() {
        if (currentIndex > 0) {
            currentIndex--;
            updateSliderPosition();
        }
    }
    
    // Touch/Mouse handlers
    function getPositionX(event) {
        return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
    }
    
    function touchStart(index) {
        return function(event) {
            isDragging = true;
            startPos = getPositionX(event);
            animationID = requestAnimationFrame(animation);
            
            track.style.cursor = 'grabbing';
            track.style.transition = 'none';
        };
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
        if (movedBy < -50 && currentIndex < getMaxIndex()) {
            nextSlide();
        } else if (movedBy > 50 && currentIndex > 0) {
            prevSlide();
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
                direction === 1 ? prevSlide() : nextSlide();
            } else {
                direction === 1 ? nextSlide() : prevSlide();
            }
            
            event.preventDefault();
        }
    }
    
    // Initialize touch events
    function initTouchEvents() {
        cards.forEach((card, index) => {
            const touchStartHandler = touchStart(index);
            
            // Touch events
            card.addEventListener('touchstart', touchStartHandler, { passive: true });
            card.addEventListener('touchmove', touchMove, { passive: true });
            card.addEventListener('touchend', touchEnd);
            
            // Mouse events
            card.addEventListener('mousedown', touchStartHandler);
            card.addEventListener('mousemove', touchMove);
            card.addEventListener('mouseup', touchEnd);
            card.addEventListener('mouseleave', () => {
                if (isDragging) touchEnd();
            });
            
            // Prevent image dragging
            const images = card.querySelectorAll('img');
            images.forEach(img => {
                img.addEventListener('dragstart', (e) => e.preventDefault());
            });
        });
    }
    
    // Initialize button events
    function initButtonEvents() {
        if (prevBtn) {
            prevBtn.addEventListener('click', prevSlide);
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', nextSlide);
        }
        
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => goToSlide(index));
            dot.addEventListener('keypress', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    goToSlide(index);
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
            
            // Adjust current index if needed
            const maxIndex = getMaxIndex();
            if (currentIndex > maxIndex) {
                currentIndex = maxIndex;
            }
            
            updateSliderPosition();
        }, 250);
    }
    
    // Initialize slider
    function init() {
        updateCardsPerView();
        updateSliderPosition();
        initTouchEvents();
        initButtonEvents();
        initKeyboardNav();
        
        window.addEventListener('resize', handleResize);
        
        // Set cursor style
        track.style.cursor = 'grab';
        
        // Add loaded class for animation
        setTimeout(() => {
            slider.classList.add('slider-loaded');
        }, 100);
    }
    
    // Auto-play (optional - disabled by default)
    let autoplayInterval;
    function startAutoplay(interval = 5000) {
        stopAutoplay();
        autoplayInterval = setInterval(() => {
            const maxIndex = getMaxIndex();
            if (currentIndex >= maxIndex) {
                goToSlide(0);
            } else {
                nextSlide();
            }
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
    
})();
