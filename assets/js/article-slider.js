/**
 * Article Slider - Previous & Next Articles
 * Version: 4.0.0 - Slide-based Structure with 2 Cards Per Slide
 * Fixed: Empty slides bug by restructuring HTML to use slide containers
 */

(function() {
    'use strict';
    
    // Configuration
    const CONFIG = {
        BREAKPOINT: 1024,
        ANIMATION_DURATION: 500, // ms
        SWIPE_THRESHOLD: 50 // pixels
    };
    
    // Check if slider exists
    const slider = document.querySelector('.article-slider');
    if (!slider) {
        console.warn('Article slider not found on page');
        return;
    }
    
    const track = slider.querySelector('.slider-track');
    const slides = slider.querySelectorAll('.slider-slide');
    const prevBtn = slider.querySelector('.slider-nav-prev');
    const nextBtn = slider.querySelector('.slider-nav-next');
    const dots = slider.querySelectorAll('.slider-dot');
    
    // Validation
    if (!track || slides.length === 0) {
        console.warn('No slider slides found');
        return;
    }
    
    console.log('🚀 Article Slider V4.0 Initializing...');
    console.log('📊 Total slides:', slides.length);
    
    // State
    let state = {
        currentSlide: 0,
        totalSlides: slides.length,
        isAnimating: false,
        isDragging: false,
        startX: 0,
        currentX: 0,
        translateX: 0
    };
    
    /**
     * Get slide width including gap
     */
    function getSlideWidth() {
        if (slides.length === 0) return 0;
        
        const slide = slides[0];
        const rect = slide.getBoundingClientRect();
        const width = rect.width;
        
        // Get gap from CSS (1.5rem = 24px typically)
        const trackStyles = window.getComputedStyle(track);
        const gap = parseFloat(trackStyles.gap) || 24;
        
        console.log('📏 Slide width:', width, 'Gap:', gap);
        
        return width + gap;
    }
    
    /**
     * Calculate translate value for current slide
     */
    function calculateTranslate() {
        const slideWidth = getSlideWidth();
        const translate = -(state.currentSlide * slideWidth);
        
        console.log('🔢 Calculate:', {
            currentSlide: state.currentSlide,
            slideWidth: slideWidth,
            translate: translate
        });
        
        return translate;
    }
    
    /**
     * Update slider position
     */
    function updatePosition(animated = true) {
        if (state.isAnimating && animated) return;
        
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
            slide: state.currentSlide,
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
            const isActive = index === state.currentSlide;
            dot.classList.toggle('active', isActive);
            dot.setAttribute('aria-selected', isActive);
        });
    }
    
    /**
     * Update buttons (always enabled for loop)
     */
    function updateButtons() {
        // Always enable buttons for infinite loop
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
     * Go to specific slide
     */
    function goToSlide(slideIndex, animated = true) {
        // Loop logic
        if (slideIndex < 0) {
            state.currentSlide = state.totalSlides - 1;
        } else if (slideIndex >= state.totalSlides) {
            state.currentSlide = 0;
        } else {
            state.currentSlide = slideIndex;
        }
        
        console.log('📄 Going to slide:', state.currentSlide);
        updatePosition(animated);
    }
    
    /**
     * Next slide - Fixed direction
     */
    function nextSlide() {
        console.log('➡️ Next slide (Right arrow)');
        goToSlide(state.currentSlide + 1);
    }
    
    /**
     * Previous slide - Fixed direction
     */
    function prevSlide() {
        console.log('⬅️ Previous slide (Left arrow)');
        goToSlide(state.currentSlide - 1);
    }
    
    /**
     * Start from middle slide
     */
    function startFromMiddle() {
        if (state.totalSlides > 1) {
            const middleSlide = Math.floor(state.totalSlides / 2);
            state.currentSlide = middleSlide;
            console.log('🎯 Starting from middle slide:', middleSlide, 'of', state.totalSlides);
        } else {
            state.currentSlide = 0;
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
        
        if (Math.abs(diff) > CONFIG.SWIPE_THRESHOLD) {
            // Swipe right = previous, Swipe left = next
            if (diff > 0) {
                prevSlide();
            } else {
                nextSlide();
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
            // In RTL context, left might mean next, but for standard behavior:
            prevSlide();
            e.preventDefault();
        } else if (e.key === 'ArrowRight') {
            nextSlide();
            e.preventDefault();
        }
    }
    
    /**
     * Initialize events
     */
    function initEvents() {
        // Button clicks - Fixed direction mapping
        if (prevBtn) {
            prevBtn.addEventListener('click', (e) => {
                e.preventDefault();
                prevSlide();
            });
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', (e) => {
                e.preventDefault();
                nextSlide();
            });
        }
        
        // Dot clicks
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                console.log('⭕ Dot clicked:', index);
                goToSlide(index);
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
        const images = slider.querySelectorAll('img');
        images.forEach(img => {
            img.addEventListener('dragstart', (e) => e.preventDefault());
        });
        
        // Window resize
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                console.log('📐 Window resized');
                updatePosition(false);
            }, 250);
        });
    }
    
    /**
     * Verify slide structure
     */
    function verifySlideStructure() {
        let isValid = true;
        
        slides.forEach((slide, index) => {
            const cards = slide.querySelectorAll('.slider-card');
            console.log(`🎴 Slide ${index + 1}: ${cards.length} card(s)`);
            
            if (cards.length === 0) {
                console.error(`❌ Slide ${index + 1} has NO cards!`);
                isValid = false;
            }
            
            // Force visibility
            slide.style.display = 'flex';
            cards.forEach(card => {
                card.style.display = 'flex';
            });
        });
        
        if (!isValid) {
            console.error('❌ Slider structure validation FAILED');
        } else {
            console.log('✅ Slider structure validated successfully');
        }
        
        return isValid;
    }
    
    /**
     * Initialize slider
     */
    function init() {
        console.log('🔧 Initializing Article Slider V4.0...');
        
        // Verify structure
        if (!verifySlideStructure()) {
            console.error('❌ Cannot initialize slider - structure invalid');
            return;
        }
        
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
        goToSlide: goToSlide,
        nextSlide: nextSlide,
        prevSlide: prevSlide,
        getState: () => ({ ...state }),
        verify: verifySlideStructure,
        debug: () => {
            console.log('🐛 === Debug Info ===');
            console.log('Current slide:', state.currentSlide);
            console.log('Total slides:', state.totalSlides);
            console.log('Translate X:', state.translateX);
            console.log('Track transform:', track.style.transform);
            
            slides.forEach((slide, i) => {
                const rect = slide.getBoundingClientRect();
                const cards = slide.querySelectorAll('.slider-card');
                console.log(`Slide ${i + 1}:`, {
                    visible: rect.width > 0 && rect.height > 0,
                    width: rect.width,
                    cards: cards.length,
                    display: slide.style.display
                });
            });
        }
    };
    
})();
