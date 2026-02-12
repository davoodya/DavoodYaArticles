/**
 * Premium Home Slider with IntersectionObserver
 * Features: Autoplay, Pause on Hover, Swipe Support, Keyboard Navigation
 */

(function() {
  'use strict';
  
  // Configuration
  const CONFIG = {
    autoplayInterval: 6000,
    transitionDuration: 800,
    swipeThreshold: 50,
    observerThreshold: 0.3
  };
  
  class HomeSlider {
    constructor(element) {
      this.slider = element;
      this.slides = Array.from(this.slider.querySelectorAll('.slider-slide'));
      this.dots = Array.from(this.slider.querySelectorAll('.slider-dot'));
      this.prevBtn = this.slider.querySelector('[data-slider-prev]');
      this.nextBtn = this.slider.querySelector('[data-slider-next]');
      
      this.currentIndex = 0;
      this.isTransitioning = false;
      this.autoplayTimer = null;
      this.isAutoplayPaused = false;
      this.isInView = false;
      
      // Touch/Swipe
      this.touchStartX = 0;
      this.touchEndX = 0;
      
      this.init();
    }
    
    init() {
      if (this.slides.length <= 1) return;
      
      this.setupIntersectionObserver();
      this.bindEvents();
      this.preloadNextImage();
    }
    
    setupIntersectionObserver() {
      // Only start autoplay when slider enters viewport
      const options = {
        threshold: CONFIG.observerThreshold,
        rootMargin: '0px'
      };
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && !this.isInView) {
            this.isInView = true;
            this.startAutoplay();
            // Disconnect observer after first activation (performance optimization)
            observer.disconnect();
          }
        });
      }, options);
      
      observer.observe(this.slider);
    }
    
    bindEvents() {
      // Navigation buttons
      if (this.prevBtn) {
        this.prevBtn.addEventListener('click', () => this.prev());
      }
      if (this.nextBtn) {
        this.nextBtn.addEventListener('click', () => this.next());
      }
      
      // Pagination dots
      this.dots.forEach((dot, index) => {
        dot.addEventListener('click', () => this.goToSlide(index));
      });
      
      // Pause on hover
      this.slider.addEventListener('mouseenter', () => this.pauseAutoplay());
      this.slider.addEventListener('mouseleave', () => this.resumeAutoplay());
      
      // Keyboard navigation
      document.addEventListener('keydown', (e) => this.handleKeyboard(e));
      
      // Touch/Swipe support
      this.slider.addEventListener('touchstart', (e) => this.handleTouchStart(e), { passive: true });
      this.slider.addEventListener('touchend', (e) => this.handleTouchEnd(e), { passive: true });
      
      // Pause autoplay when page is hidden
      document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
          this.pauseAutoplay();
        } else if (this.isInView) {
          this.resumeAutoplay();
        }
      });
    }
    
    goToSlide(index, direction = 'next') {
      if (this.isTransitioning || index === this.currentIndex) return;
      
      this.isTransitioning = true;
      
      const currentSlide = this.slides[this.currentIndex];
      const nextSlide = this.slides[index];
      
      // Remove active class from current
      currentSlide.classList.remove('active');
      currentSlide.setAttribute('aria-hidden', 'true');
      
      // Add active class to next
      nextSlide.classList.add('active');
      nextSlide.setAttribute('aria-hidden', 'false');
      
      // Update dots
      this.updateDots(index);
      
      // Update current index
      this.currentIndex = index;
      
      // Preload next image
      this.preloadNextImage();
      
      // Allow next transition after duration
      setTimeout(() => {
        this.isTransitioning = false;
      }, CONFIG.transitionDuration);
    }
    
    next() {
      const nextIndex = (this.currentIndex + 1) % this.slides.length;
      this.goToSlide(nextIndex, 'next');
    }
    
    prev() {
      const prevIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
      this.goToSlide(prevIndex, 'prev');
    }
    
    updateDots(index) {
      this.dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
      });
    }
    
    startAutoplay() {
      if (this.autoplayTimer) return;
      
      this.autoplayTimer = setInterval(() => {
        if (!this.isAutoplayPaused) {
          this.next();
        }
      }, CONFIG.autoplayInterval);
    }
    
    pauseAutoplay() {
      this.isAutoplayPaused = true;
    }
    
    resumeAutoplay() {
      this.isAutoplayPaused = false;
    }
    
    stopAutoplay() {
      if (this.autoplayTimer) {
        clearInterval(this.autoplayTimer);
        this.autoplayTimer = null;
      }
    }
    
    handleKeyboard(e) {
      if (!this.isInView) return;
      
      // In RTL: Left arrow goes to previous slide (visual right)
      if (e.key === 'ArrowLeft') {
        this.prev();
      }
      // In RTL: Right arrow goes to next slide (visual left)
      else if (e.key === 'ArrowRight') {
        this.next();
      }
    }
    
    handleTouchStart(e) {
      this.touchStartX = e.changedTouches[0].screenX;
    }
    
    handleTouchEnd(e) {
      this.touchEndX = e.changedTouches[0].screenX;
      this.handleSwipe();
    }
    
    handleSwipe() {
      const diff = this.touchStartX - this.touchEndX;
      
      // Swipe right to left (next slide in RTL)
      if (diff > CONFIG.swipeThreshold) {
        this.next();
      }
      // Swipe left to right (previous slide in RTL)
      else if (diff < -CONFIG.swipeThreshold) {
        this.prev();
      }
    }
    
    preloadNextImage() {
      // Preload next slide's image for smooth transition
      const nextIndex = (this.currentIndex + 1) % this.slides.length;
      const nextSlide = this.slides[nextIndex];
      const img = nextSlide.querySelector('.slide-bg img');
      
      if (img && img.loading === 'lazy') {
        // Force load the image
        img.loading = 'eager';
      }
    }
    
    destroy() {
      this.stopAutoplay();
      // Remove event listeners if needed
    }
  }
  
  // Initialize slider when DOM is ready
  function initSlider() {
    const sliderElement = document.querySelector('[data-slider]');
    
    if (!sliderElement) return;
    
    // Check if IntersectionObserver is supported
    if ('IntersectionObserver' in window) {
      new HomeSlider(sliderElement);
    } else {
      // Fallback: start immediately without observer
      const slider = new HomeSlider(sliderElement);
      slider.isInView = true;
      slider.startAutoplay();
    }
  }
  
  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSlider);
  } else {
    initSlider();
  }
  
})();
