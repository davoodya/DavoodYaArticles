# ✅ HOME SLIDER - VISUAL VALIDATION CHECKLIST

**Date:** February 12, 2026  
**Purpose:** Step-by-step visual verification guide  
**Audience:** QA Engineers, Developers, Stakeholders

---

## 🎯 PRE-FLIGHT CHECK

Before starting validation:

```bash
# 1. Build production version
hugo --minify --cleanDestinationDir

# 2. Start local server
hugo server --disableFastRender

# 3. Open browser
http://localhost:1313/
```

---

## 📐 SECTION 1: LAYOUT STRUCTURE

### ✅ Full-Width Verification

**Test Steps:**
1. Open homepage in desktop browser (1920px width)
2. Open DevTools (F12) → Elements tab
3. Inspect `.home-slider` element

**Expected Results:**
- [ ] Slider stretches edge-to-edge (no white margins)
- [ ] Slider appears IMMEDIATELY below header
- [ ] 3-column layout (sidebars + content) appears AFTER slider
- [ ] No duplicate slider rendering

**Visual Reference:**
```
┌─────────────────────────────────────────────┐
│              HEADER (full-width)            │
├─────────────────────────────────────────────┤
│                                             │
│          HOME SLIDER (full-width)           │ ← Should span entire width
│              No white gaps                  │
│                                             │
├─────────────────────────────────────────────┤
│ ┌──────┬─────────────────────┬───────────┐ │
│ │ Left │   Main Content      │   Right   │ │
│ │ Side │   (Categories)      │   Side    │ │
│ └──────┴─────────────────────┴───────────┘ │
└─────────────────────────────────────────────┘
```

**How to Verify Width:**
1. Right-click slider → Inspect
2. Check computed width = `100vw` or `1920px`
3. Verify `margin-left` has negative value
4. Confirm no parent container constraining

---

## 🧭 SECTION 2: NAVIGATION DIRECTION

### ✅ Arrow Button Positions

**Test Steps:**
1. Hover over slider
2. Observe navigation arrows appear

**Expected Results:**
- [ ] **Previous arrow** on **LEFT** side
- [ ] **Next arrow** on **RIGHT** side
- [ ] Arrows appear on hover (desktop)
- [ ] Arrows have green glow effect

**Visual Layout (RTL Context):**
```
                    ┌─────────────────────────┐
                    │                         │
[← PREV]            │      SLIDE CONTENT      │            [NEXT →]
(LEFT SIDE)         │                         │         (RIGHT SIDE)
                    │                         │
                    └─────────────────────────┘
```

### ✅ Arrow Functionality

**Test Steps:**
1. Click left arrow (Previous)
2. Click right arrow (Next)
3. Use keyboard: Press Left Arrow key
4. Use keyboard: Press Right Arrow key

**Expected Results:**
- [ ] Left button → Goes to PREVIOUS slide (swaps to previous in array)
- [ ] Right button → Goes to NEXT slide (swaps to next in array)
- [ ] Left Arrow key → Previous slide
- [ ] Right Arrow key → Next slide
- [ ] Smooth fade transition (~800ms)

### ✅ Arrow Icons

**Test Steps:**
1. Inspect SVG paths in arrow buttons

**Expected Results:**
- [ ] Previous arrow (LEFT) has **right-pointing chevron** →
- [ ] Next arrow (RIGHT) has **left-pointing chevron** ←
- [ ] Icons glow green on hover
- [ ] Scale effect on hover (1.1x)

---

## 📏 SECTION 3: SIZING & PROPORTIONS

### ✅ Desktop Sizing (1920px width)

**Test Steps:**
1. Resize browser to 1920px width
2. Measure slider height using DevTools

**Expected Results:**
- [ ] Height = **750px**
- [ ] Aspect ratio appears balanced (not too tall/short)
- [ ] No vertical scrollbar on slider itself
- [ ] Content vertically centered

### ✅ Laptop Sizing (1366px width)

**Test Steps:**
1. Resize browser to 1366px
2. Check slider appearance

**Expected Results:**
- [ ] Height = **650px**
- [ ] Still full-width (no gaps)
- [ ] Typography scales down proportionally
- [ ] All elements visible

### ✅ Tablet Sizing (768px width)

**Test Steps:**
1. Resize to 768px or use DevTools Device Toolbar (iPad)
2. Verify slider adapts

**Expected Results:**
- [ ] Height = **600px**
- [ ] Full-width maintained
- [ ] Arrows slightly smaller (55px)
- [ ] Content readable

### ✅ Mobile Sizing (375px width)

**Test Steps:**
1. Switch to iPhone SE in DevTools
2. Check mobile layout

**Expected Results:**
- [ ] Height = **450-500px**
- [ ] Arrows hidden (dots only)
- [ ] Badges stack vertically
- [ ] CTA button full-width
- [ ] Touch swipe works

---

## 📖 SECTION 4: TEXT READABILITY

### ✅ Light Background Test

**Test Steps:**
1. Navigate to slide with bright/light image
2. Read title and description

**Expected Results:**
- [ ] Title (green text) clearly visible
- [ ] Description (white text) clearly visible
- [ ] No squinting required
- [ ] Text has strong shadow outline
- [ ] Badges readable

**Contrast Test:**
- Use browser extension: "WCAG Color Contrast Checker"
- Expected ratio: **>7:1** (AAA compliance)

### ✅ Dark Background Test

**Test Steps:**
1. Navigate to slide with dark image
2. Verify text still readable

**Expected Results:**
- [ ] Title still glows (green shadow)
- [ ] Description clear against dark
- [ ] Overlay doesn't over-darken
- [ ] Natural image tones preserved

### ✅ Overlay Quality

**Test Steps:**
1. Inspect `.slide-overlay` in DevTools
2. Observe gradient effect

**Expected Results:**
- [ ] Gradient visible (lighter top, darker bottom)
- [ ] No harsh line between gradient layers
- [ ] Subtle blur effect (backdrop-filter)
- [ ] Doesn't completely block image

**Visual Effect:**
```
Image (100% bright)
     ↓
Overlay (50% dark top → 85% dark bottom)
     ↓
Text (with multi-layer shadows)
     ↓
Result: Perfect readability + visible image
```

---

## 📱 SECTION 5: RESPONSIVE BEHAVIOR

### ✅ Desktop (1920px)

**Checklist:**
- [ ] Full-width slider
- [ ] 750px height
- [ ] Both arrows visible on hover
- [ ] Dots at bottom center
- [ ] 2-column badge layout
- [ ] Title size: ~3.5rem
- [ ] Description size: ~1.35rem

### ✅ Laptop (1366px)

**Checklist:**
- [ ] Full-width maintained
- [ ] 650px height
- [ ] Arrows still visible
- [ ] Typography scales down
- [ ] All badges visible
- [ ] No horizontal scroll

### ✅ Tablet (768px - iPad)

**Checklist:**
- [ ] 600px height
- [ ] Arrows 55px size
- [ ] Badges may wrap
- [ ] Title readable
- [ ] Touch swipe functional

### ✅ Mobile (375px - iPhone)

**Checklist:**
- [ ] 450-500px height
- [ ] Arrows hidden
- [ ] Dots larger (easier to tap)
- [ ] Badges stack vertically
- [ ] Button full-width
- [ ] Swipe gestures work
- [ ] No content cut off

---

## 🎨 SECTION 6: VISUAL POLISH

### ✅ Typography

**Test Steps:**
1. Review all text elements
2. Check font rendering

**Expected Results:**
- [ ] Title uses Persian heading font
- [ ] Title has green glow effect
- [ ] Description uses Persian text font
- [ ] Tags use English font (if Latin characters)
- [ ] No font loading flash (FOUT)

### ✅ Badges & Tags

**Test Steps:**
1. Inspect meta elements (categories, tags, badges)
2. Hover over each

**Expected Results:**
- [ ] Categories: Blue gradient background
- [ ] Tags: Green border
- [ ] Badges: Dark background with colored borders
- [ ] Hover effects: Lift up 2px + glow
- [ ] Icons properly aligned
- [ ] Backdrop blur visible

### ✅ CTA Button

**Test Steps:**
1. Hover over "مشاهده مقاله" button
2. Click button

**Expected Results:**
- [ ] Green gradient background
- [ ] Black text (high contrast)
- [ ] Ripple effect on hover
- [ ] Scale + lift animation
- [ ] Arrow icon animates left (-5px)
- [ ] Clicks navigate to article

### ✅ Pagination Dots

**Test Steps:**
1. Observe dots at bottom
2. Click different dots

**Expected Results:**
- [ ] Inactive dots: Small circles (12px)
- [ ] Active dot: Wide pill (35px)
- [ ] Active dot glows green
- [ ] Smooth transition between states
- [ ] Dots centered horizontally

---

## ⚡ SECTION 7: INTERACTIONS

### ✅ Autoplay

**Test Steps:**
1. Load homepage and wait
2. Do NOT interact with slider

**Expected Results:**
- [ ] Slides automatically advance every **6 seconds**
- [ ] Smooth fade transition between slides
- [ ] Autoplay pauses on hover
- [ ] Autoplay resumes after mouse leaves
- [ ] Autoplay stops when tab hidden

### ✅ Manual Navigation

**Test Steps:**
1. Click Previous/Next arrows
2. Click pagination dots
3. Use keyboard arrows
4. Swipe on mobile

**Expected Results:**
- [ ] All methods change slides
- [ ] Transitions are smooth (800ms)
- [ ] No double-triggering
- [ ] Current slide dot updates
- [ ] Autoplay resets timer

### ✅ Hover Effects

**Test Items to Hover:**
1. Slider itself → Arrows appear
2. Arrow buttons → Scale + glow
3. Category badges → Lift + border glow
4. Tags → Lift + shadow
5. CTA button → Ripple effect
6. Info badges → Lift + border glow
7. Pagination dots → Scale up

**Expected Results:**
- [ ] All hover states smooth (300ms)
- [ ] No janky animations
- [ ] GPU-accelerated (smooth 60fps)

---

## ♿ SECTION 8: ACCESSIBILITY

### ✅ Keyboard Navigation

**Test Steps:**
1. Tab to slider area
2. Press Left Arrow
3. Press Right Arrow
4. Tab to dots

**Expected Results:**
- [ ] Keyboard focus visible (outline)
- [ ] Left/Right arrows navigate slides
- [ ] Tab reaches navigation buttons
- [ ] Enter key activates focused button
- [ ] No keyboard trap

### ✅ ARIA Attributes

**Test Steps:**
1. Inspect slider HTML in DevTools
2. Check ARIA attributes

**Expected Results:**
- [ ] Slider has `role="region"`
- [ ] Slider has `aria-label="مقالات ویژه"`
- [ ] Buttons have `aria-label` (prev/next)
- [ ] Active slide: `aria-hidden="false"`
- [ ] Inactive slides: `aria-hidden="true"`

### ✅ Screen Reader Test

**Test Steps:**
1. Enable screen reader (NVDA/JAWS/VoiceOver)
2. Navigate to slider

**Expected Results:**
- [ ] Announces "مقالات ویژه region"
- [ ] Reads slide title
- [ ] Reads slide description
- [ ] Announces button labels
- [ ] Announces current slide number

### ✅ Reduced Motion

**Test Steps:**
1. Enable "Reduce Motion" in OS settings
2. Reload page

**Expected Results:**
- [ ] No fade transitions
- [ ] No zoom animation on images
- [ ] Instant slide changes
- [ ] No content stagger animations

---

## 🔍 SECTION 9: PERFORMANCE

### ✅ Lighthouse Audit

**Test Steps:**
1. Open DevTools → Lighthouse tab
2. Run audit (Desktop mode)

**Expected Scores:**
- [ ] Performance: **90+**
- [ ] Accessibility: **95+**
- [ ] Best Practices: **95+**
- [ ] SEO: **100**

### ✅ Network Performance

**Test Steps:**
1. Open Network tab in DevTools
2. Reload page
3. Check slider resources

**Expected Results:**
- [ ] First slide image preloaded
- [ ] Other slides lazy loaded
- [ ] CSS fingerprinted and cached
- [ ] JS deferred
- [ ] No render-blocking resources

### ✅ Layout Shift (CLS)

**Test Steps:**
1. Reload page
2. Watch slider load

**Expected Results:**
- [ ] No layout jump when slider appears
- [ ] Reserved space maintained
- [ ] Images don't shift content down
- [ ] CLS score = **0.00**

### ✅ Console Errors

**Test Steps:**
1. Open Console tab
2. Check for errors

**Expected Results:**
- [ ] **Zero** JavaScript errors
- [ ] **Zero** CSS errors
- [ ] **Zero** 404 errors (missing images)
- [ ] No CORS warnings

---

## 🌐 SECTION 10: CROSS-BROWSER

### ✅ Chrome (Latest)
- [ ] Slider renders correctly
- [ ] Animations smooth
- [ ] Full functionality works

### ✅ Firefox (Latest)
- [ ] Layout consistent with Chrome
- [ ] Backdrop blur supported
- [ ] Navigation functional

### ✅ Safari (Latest)
- [ ] WebKit rendering correct
- [ ] Backdrop blur working
- [ ] Touch events work

### ✅ Edge (Latest)
- [ ] Chromium engine consistent
- [ ] All features functional

### ✅ Mobile Safari (iOS 14+)
- [ ] Touch swipe gestures
- [ ] Height appropriate
- [ ] No zoom issues

### ✅ Mobile Chrome (Android)
- [ ] Swipe functional
- [ ] Layout correct
- [ ] Performance good

---

## 📋 FINAL VERIFICATION

### Critical Path Check
- [ ] Homepage loads
- [ ] Slider visible immediately after header
- [ ] At least 1 slide renders
- [ ] Navigation buttons work
- [ ] Text is readable
- [ ] Autoplay functions
- [ ] No console errors

### Deployment Readiness
- [ ] All tests passed
- [ ] Cross-browser verified
- [ ] Performance targets met
- [ ] Accessibility compliant
- [ ] Documentation reviewed

---

## 🐛 COMMON ISSUES & FIXES

### Issue: Slider Not Full Width
**Diagnostic:**
```css
/* Check computed styles */
.home-slider {
  width: 100vw ✅
  margin-left: calc(-50vw + 50%) ✅
  margin-right: calc(-50vw + 50%) ✅
}
```
**Fix:** Remove max-width from parent container

### Issue: Arrows Reversed
**Diagnostic:**
```css
.slider-arrow-prev { left: 3rem ✅ }
.slider-arrow-next { right: 3rem ✅ }
```
**Fix:** Swap left/right values if reversed

### Issue: Text Unreadable
**Diagnostic:**
- Check overlay opacity values
- Verify text-shadow applied
- Test contrast ratio

**Fix:** Increase overlay darkness:
```css
rgba(0, 0, 0, 0.85) → rgba(0, 0, 0, 0.95)
```

### Issue: Mobile Swipe Not Working
**Diagnostic:**
- Check touch event listeners
- Verify `passive: true` option

**Fix:** Ensure JavaScript loaded without errors

---

## ✅ SIGN-OFF

### QA Engineer Sign-Off
- Date: __________
- Name: __________
- Status: [ ] PASS [ ] FAIL
- Notes: ___________________________

### Developer Sign-Off
- Date: __________
- Name: __________
- Status: [ ] Ready for Production
- Notes: ___________________________

### Stakeholder Approval
- Date: __________
- Name: __________
- Status: [ ] Approved [ ] Changes Needed
- Feedback: ___________________________

---

**Validation Completed:** __________  
**Production Deploy Date:** __________  
**Next Review:** __________

---

## 📞 SUPPORT CONTACTS

**Technical Issues:** Check `HOME_SLIDER_REFACTOR_COMPLETE.md`  
**Quick Reference:** Check `HOME_SLIDER_QUICK_REFERENCE.md`  
**Implementation Details:** Check code comments in files

---

**Document Version:** 1.0  
**Last Updated:** February 12, 2026  
**Maintained By:** QA & Development Team
