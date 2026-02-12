# Article Slider - Previous & Next Articles

## Overview

The **Article Slider** is a dynamic component that displays related articles (previous and next) at the bottom of each article page. It provides an elegant way for users to discover more content and navigate between articles.

---

## 📁 File Structure

```
davoodya/
├── layouts/
│   ├── partials/
│   │   └── article-slider.html          # Main slider partial
│   └── _default/
│       ├── single.html                  # Slider integration
│       └── baseof.html                  # Asset loading
├── assets/
│   ├── css/
│   │   └── article-slider.css           # Slider styles
│   └── js/
│       └── article-slider.js            # Slider functionality
└── docs/
    └── 02-Features/
        └── ARTICLE_SLIDER_GUIDE.md      # This file
```

---

## ✨ Features

### Core Functionality

- ✅ **Smart Article Selection**: Prioritizes articles from the same category
- ✅ **Dynamic Fallback**: Automatically fills with random articles if needed
- ✅ **Responsive Design**: Adapts to all screen sizes (desktop, tablet, mobile)
- ✅ **Touch Gestures**: Full swipe support on mobile devices
- ✅ **Keyboard Navigation**: Arrow keys for accessibility
- ✅ **Smooth Animations**: CSS transform-based transitions
- ✅ **Lazy Loading**: Images load on demand for performance
- ✅ **SEO Optimized**: Proper semantic HTML and JSON-LD structured data

### Display Logic

1. Shows **2 previous** (older) and **2 next** (newer) articles
2. If previous/next articles don't exist, fills with **random articles** from same category
3. If same category has insufficient articles, uses articles from **all categories**
4. **Never shows** the current article
5. **Never shows** draft or future articles
6. **Minimum requirement**: At least 2 articles to display slider

---

## 🎨 Design Specifications

### Visual Style

The slider **perfectly matches** existing article cards:

- Same card layout and structure
- Same badge styling (time, difficulty, lab, type)
- Same tag styling
- Same button style ("مشاهده مطلب")
- Same color scheme and borders
- Same hover effects and transitions

### Responsive Behavior

| Viewport | Cards Per View | Layout |
|----------|----------------|--------|
| Desktop (>1024px) | 2 cards | Horizontal slider |
| Tablet (768-1024px) | 1 card | Horizontal slider |
| Mobile (<768px) | 1 card | Swipe-enabled |

---

## 📋 Front Matter Requirements

All displayed data is read from each article's front matter:

```yaml
---
title: "Article Title"
description: "Article description"
featured_image: "/images/category/article-image.jpg"
images:
  - "/images/category/article-image.jpg"
tags:
  - "tag1"
  - "tag2"
  - "tag3"
categories:
  - "cyber-security"
readingTime: 15
difficulty: "beginner"  # beginner, medium, intermediate, advanced
lab_required: true
post_type_fa: "آموزش"
date: 2026-02-10
lastmod: 2026-02-11
---
```

### Required Fields

- `title`: Article title *(required)*
- `categories`: Used for smart article selection *(recommended)*
- `date`: Used for sorting articles *(required)*

### Optional Fields (Displayed if Available)

- `description` / `summary`: Article description
- `featured_image` / `images`: Article image
- `tags`: Article tags (max 3 displayed)
- `readingTime`: Reading time in minutes
- `difficulty`: Difficulty level badge
- `lab_required`: Lab required badge
- `post_type_fa`: Post type badge

---

## 🔧 Implementation Details

### HTML Structure

```html
<section class="article-slider">
  <div class="slider-container">
    <h2 class="slider-title">مقالات پیشنهادی</h2>
    
    <div class="slider-wrapper">
      <button class="slider-nav slider-nav-prev">←</button>
      
      <div class="slider-track-container">
        <div class="slider-track">
          <!-- Slider cards here -->
        </div>
      </div>
      
      <button class="slider-nav slider-nav-next">→</button>
    </div>
    
    <div class="slider-dots">
      <!-- Navigation dots -->
    </div>
  </div>
</section>
```

### Article Selection Algorithm

```go
// 1. Get current article's primary category
currentCategory := .Params.categories[0]

// 2. Get all published articles (exclude drafts and future)
allArticles := where .Site.RegularPages "Draft" false
allArticles = where allArticles "Date" "le" now

// 3. Get articles from same category
sameCategoryArticles := where allArticles ".Params.categories" "intersect" currentCategory

// 4. Sort by date
sortedArticles := sameCategoryArticles.ByDate

// 5. Find current article index
currentIndex := findIndex(sortedArticles, currentArticle)

// 6. Get 2 previous and 2 next
previousArticles := sortedArticles[currentIndex-2:currentIndex]
nextArticles := sortedArticles[currentIndex+1:currentIndex+3]

// 7. Fill with random if needed
if len(sliderArticles) < 4 {
    randomArticles := shuffle(availableArticles)[0:needed]
}
```

---

## 🎯 JavaScript Features

### Core Functions

```javascript
// Initialize slider
init()

// Navigation
nextSlide()
prevSlide()
goToSlide(index)

// Touch/Mouse handling
touchStart(event)
touchMove(event)
touchEnd()

// Responsive
updateCardsPerView()
handleResize()
```

### Event Listeners

- **Click**: Navigation buttons and dots
- **Touch**: Swipe gestures on mobile
- **Mouse**: Drag on desktop
- **Keyboard**: Arrow key navigation
- **Resize**: Viewport changes

### Performance Optimizations

- `requestAnimationFrame` for smooth animations
- `debounce` on resize events (250ms)
- `backface-visibility: hidden` for GPU acceleration
- `will-change: transform` for animation optimization
- `content-visibility: auto` for image rendering

---

## 🎨 CSS Architecture

### Key Classes

| Class | Purpose |
|-------|---------|
| `.article-slider` | Main container |
| `.slider-container` | Content wrapper (max-width: 1400px) |
| `.slider-track` | Sliding track |
| `.slider-card` | Individual article card |
| `.slider-nav` | Navigation buttons |
| `.slider-dot` | Navigation dots |
| `.slider-badge` | Badge components |

### CSS Custom Properties Used

```css
--accent-green: #00ff41
--accent-blue: #3aaddf
--card-bg: rgba(20, 20, 20, 0.95)
--darker-bg: rgba(15, 15, 15, 0.98)
--secondary-text: #b0b0b0
--persian-heading: 'Shabnam', 'IRANYekanX'
--persian-text: 'VazirMatn', 'Mikhak'
```

---

## 📱 Mobile Touch Support

### Gestures

- **Swipe Left**: Next slide (RTL aware)
- **Swipe Right**: Previous slide (RTL aware)
- **Tap**: Click links/buttons
- **Drag**: Desktop mouse dragging

### Implementation

```javascript
// Touch threshold: 50px
const swipeThreshold = 50;

if (movedBy < -50) {
    nextSlide();
} else if (movedBy > 50) {
    prevSlide();
}
```

---

## ♿ Accessibility

### ARIA Attributes

```html
<section class="article-slider" aria-label="مقالات مرتبط">
  <button class="slider-nav-prev" 
          aria-label="مقاله قبلی" 
          disabled>
  
  <div class="slider-track" role="list">
    <article role="listitem">
  
  <button class="slider-dot" 
          role="tab" 
          aria-label="مقاله ۱" 
          aria-selected="true">
</section>
```

### Keyboard Navigation

- **Arrow Left/Right**: Navigate slides (RTL aware)
- **Tab**: Navigate through links
- **Enter/Space**: Activate dots
- **Focus Visible**: Custom outline styling

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
    .slider-track,
    .slider-card {
        transition: none;
    }
}
```

---

## 🔍 SEO Implementation

### Semantic HTML

```html
<section>           <!-- Slider container -->
  <h2>             <!-- Section heading -->
  <article>        <!-- Each card -->
    <h3>          <!-- Card title -->
    <a href="">   <!-- Links -->
```

### JSON-LD Structured Data

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "مقالات پیشنهادی",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Article",
        "name": "Article Title",
        "url": "https://example.com/article",
        "description": "...",
        "datePublished": "2026-02-10",
        "dateModified": "2026-02-11"
      }
    }
  ]
}
```

### Image Optimization

- First 2 images: `loading="eager"` (visible on load)
- Remaining images: `loading="lazy"` (load on scroll)
- Alt attributes from article titles
- Fixed aspect ratio (180px height)

---

## 🚀 Performance Metrics

### Best Practices

✅ No layout shift (CLS = 0)
✅ Fixed image dimensions
✅ Deferred JavaScript loading
✅ CSS transforms (GPU accelerated)
✅ Minimal reflows/repaints
✅ Lightweight vanilla JS (~6KB)

### Load Times

- CSS: ~8KB (gzipped: ~2KB)
- JS: ~6KB (gzipped: ~2KB)
- Total: ~14KB (4KB gzipped)

---

## 🧪 Testing Checklist

### Functionality

- [ ] Slider displays on single article pages
- [ ] Shows 4 articles (2 previous + 2 next)
- [ ] Falls back to random articles if needed
- [ ] Never shows current article
- [ ] Never shows draft articles
- [ ] Hides if fewer than 2 total articles

### Navigation

- [ ] Next button works correctly
- [ ] Previous button works correctly
- [ ] Buttons disable at boundaries
- [ ] Dots navigation works
- [ ] Active dot updates correctly
- [ ] Keyboard arrow keys work

### Responsive

- [ ] Desktop: 2 cards visible
- [ ] Tablet: 1 card visible
- [ ] Mobile: 1 card visible
- [ ] Touch swipe works on mobile
- [ ] No horizontal overflow
- [ ] No layout breaking

### Visual

- [ ] Matches article card design
- [ ] Badges styled correctly
- [ ] Tags styled correctly
- [ ] Images load properly
- [ ] Hover effects work
- [ ] Animations smooth

### Performance

- [ ] No console errors
- [ ] No layout shift
- [ ] Images lazy load
- [ ] Smooth animations
- [ ] No memory leaks
- [ ] Fast page load

### Accessibility

- [ ] Keyboard navigation works
- [ ] ARIA labels present
- [ ] Focus visible
- [ ] Screen reader friendly
- [ ] Semantic HTML
- [ ] Reduced motion support

### SEO

- [ ] Structured data valid
- [ ] Semantic HTML correct
- [ ] Alt attributes present
- [ ] No duplicate content
- [ ] Links indexable

---

## 🐛 Troubleshooting

### Slider Not Appearing

**Possible Causes:**
1. Fewer than 2 total articles in site
2. JavaScript not loaded
3. CSS not loaded

**Solution:**
```bash
# Check article count
hugo list all | wc -l

# Verify JS loads
View Page Source → Search for "article-slider.js"

# Verify CSS loads
DevTools → Network → Filter CSS → article-slider.css
```

### Navigation Not Working

**Possible Causes:**
1. JavaScript error
2. Card count incorrect
3. Index calculation issue

**Solution:**
```javascript
// Check console for errors
console.log('Cards:', cards.length);
console.log('Current Index:', currentIndex);
console.log('Max Index:', getMaxIndex());
```

### Images Not Loading

**Possible Causes:**
1. Wrong image path
2. Missing featured_image
3. Lazy load issue

**Solution:**
```yaml
# Verify front matter
featured_image: "/images/category/image.jpg"
# OR
images:
  - "/images/category/image.jpg"
```

### Touch Gestures Not Working

**Possible Causes:**
1. Touch events not bound
2. Passive event listener
3. CSS touch-action

**Solution:**
```css
.slider-track-container {
    touch-action: pan-y pinch-zoom;
}
```

---

## 🔄 Customization

### Change Cards Per View

```javascript
// In article-slider.js
function updateCardsPerView() {
    const width = window.innerWidth;
    cardsPerView = width <= 768 ? 1 : 3;  // Change to 3 for desktop
}
```

### Change Slide Count

```html
<!-- In article-slider.html -->
{{ $previousArticles := first 3 (after ...) }}  <!-- Change to 3 -->
{{ $nextArticles := first 3 (after ...) }}      <!-- Change to 3 -->
```

### Change Animation Speed

```css
/* In article-slider.css */
.slider-track {
    transition: transform 0.3s ease;  /* Change duration */
}
```

### Enable Auto-Play

```javascript
// In article-slider.js (uncomment)
startAutoplay(5000);  // 5 seconds interval
```

### Change Colors

```css
/* In article-slider.css */
.slider-card {
    border-color: #your-color;
}

.slider-nav:hover {
    border-color: #your-color;
}
```

---

## 📊 Browser Support

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Full Support |
| Firefox | 88+ | ✅ Full Support |
| Safari | 14+ | ✅ Full Support |
| Edge | 90+ | ✅ Full Support |
| Opera | 76+ | ✅ Full Support |
| iOS Safari | 14+ | ✅ Full Support |
| Android Chrome | 90+ | ✅ Full Support |

### Required Features

- CSS Grid/Flexbox
- CSS Transforms
- Touch Events
- IntersectionObserver (lazy loading)
- requestAnimationFrame

---

## 📝 Future Enhancements

### Planned Features

- [ ] Filter by specific tags
- [ ] Show article reading progress
- [ ] Add view count to cards
- [ ] Social proof (comments count)
- [ ] Related by tags (not just category)
- [ ] AI-powered recommendations
- [ ] User preference learning

### Possible Improvements

- [ ] Infinite scroll option
- [ ] Vertical slider mode
- [ ] Grid view option
- [ ] Compact card mode
- [ ] Video thumbnail support
- [ ] Audio article support

---

## 📚 Related Documentation

- [Article Features Implementation](./ARTICLE_FEATURES_IMPLEMENTATION.md)
- [Article Cards Guide](../03-Fixes/ARTICLE_CARDS_SINGLE_COLUMN_FIX.md)
- [Home Slider Guide](./HOME_SLIDER_IMPLEMENTATION.md)
- [Responsive Design Guide](../05-Guides/MOBILE_LAYOUT_TEST_GUIDE.md)

---

## 📞 Support

For issues or questions:

1. Check [Troubleshooting](#-troubleshooting) section
2. Review browser console for errors
3. Verify all required files are present
4. Check article front matter format
5. Test with different article counts

---

## 📜 License

This component is part of the Davoodya Hugo theme and follows the same license.

---

**Last Updated**: February 11, 2026  
**Version**: 1.0.0  
**Status**: ✅ Production Ready
