# ✅ Popup Validation Checklist

**Use this checklist to verify the popup fix is working correctly**

---

## 🧪 PRE-DEPLOYMENT TESTS

### 1. Build Verification
- [ ] `hugo --cleanDestinationDir` runs without errors
- [ ] No warnings in build output
- [ ] All 267+ pages generated successfully
- [ ] `hugo server` runs correctly

### 2. Code Quality
- [ ] No console errors in browser
- [ ] No JavaScript warnings
- [ ] No CSS rendering issues
- [ ] No lint errors

---

## 🎯 FUNCTIONAL TESTS

### Test 1: Basic Popup Display
**Scenario**: First visit to article

**Steps**:
1. Clear browser storage (F12 → Application → Storage → Clear)
2. Open any article page
3. Wait 15 seconds OR scroll to 30%

**Expected**:
- [ ] Popup appears at bottom left
- [ ] Smooth slide-in animation
- [ ] All content renders correctly
- [ ] Images load properly
- [ ] Badges display correctly

---

### Test 2: Page-Scoped Behavior
**Scenario**: Multiple article visits

**Steps**:
1. Visit Article A
2. Wait for popup → Close it
3. Visit Article B
4. Wait for popup

**Expected**:
- [ ] Popup shows on Article A
- [ ] Popup closes when dismissed
- [ ] Popup shows AGAIN on Article B
- [ ] Popup shows on Article C, D, E...
- [ ] Each article independent

**Critical**: ✅ Popup must show on EVERY new article

---

### Test 3: Session Persistence
**Scenario**: Refresh same page

**Steps**:
1. Visit Article A
2. Wait for popup → Close it
3. Refresh the page (F5)

**Expected**:
- [ ] Popup does NOT show after refresh
- [ ] sessionStorage key persists
- [ ] Same behavior on multiple refreshes

---

### Test 4: Rate Limiting
**Scenario**: Visit many articles

**Steps**:
1. Visit 20 different articles
2. Close popup on each
3. Visit 21st article

**Expected**:
- [ ] Popups show on articles 1-20
- [ ] Popup blocked on article 21
- [ ] localStorage counter = 20
- [ ] No popup until 24 hours pass

**Check in console**:
```javascript
localStorage.getItem('popup_global_counter')  // Should be 20
```

---

### Test 5: Cross-Tab Behavior
**Scenario**: Multiple browser tabs

**Steps**:
1. Tab 1: Open Article A → popup shows
2. Tab 2: Open Article A → popup shows
3. Tab 1: Close popup
4. Tab 2: Verify popup still visible

**Expected**:
- [ ] Each tab has independent session
- [ ] Closing in Tab 1 doesn't affect Tab 2
- [ ] Global counter still increments

---

### Test 6: Trigger Logic
**Scenario**: Time vs Scroll triggers

**Steps**:

**Test 6a: Time Trigger**
1. Open article
2. Don't scroll, just wait 15 seconds

**Expected**:
- [ ] Popup shows after 15 seconds

**Test 6b: Scroll Trigger**
1. Open article
2. Immediately scroll to 30% of page

**Expected**:
- [ ] Popup shows when reaching 30%
- [ ] Popup shows before 15 seconds elapsed

**Test 6c: First Trigger Wins**
1. Open article
2. Scroll to 20% (below threshold)
3. Wait 15 seconds

**Expected**:
- [ ] Popup shows at 15 seconds (time trigger wins)

---

### Test 7: User Interactions

**Test 7a: Close Button**
1. Wait for popup
2. Click × button

**Expected**:
- [ ] Popup closes smoothly
- [ ] Fade-out animation plays

**Test 7b: Next Article Button**
1. Wait for popup
2. Click "مقاله بعدی"

**Expected**:
- [ ] New article loads in popup
- [ ] Badges update correctly
- [ ] Image changes
- [ ] Can cycle through all articles

**Test 7c: Read Article Button**
1. Wait for popup
2. Click "مطالعه مقاله"

**Expected**:
- [ ] Navigates to article
- [ ] Correct URL

**Test 7d: ESC Key**
1. Wait for popup
2. Press ESC key

**Expected**:
- [ ] Popup closes
- [ ] Same as clicking close button

---

## 📱 RESPONSIVE TESTS

### Test 8: Desktop (> 1024px)
- [ ] Popup width: 380px
- [ ] Position: Bottom left
- [ ] All features visible
- [ ] Smooth animations
- [ ] No layout shift

### Test 9: Tablet (768px - 1024px)
- [ ] Popup width: 360px
- [ ] Position: Bottom left
- [ ] All features visible
- [ ] Touch interactions work

### Test 10: Mobile (< 768px)
- [ ] Popup width: Full width minus margins
- [ ] Footer buttons stack vertically
- [ ] Smaller image height
- [ ] Touch scrolling works
- [ ] No horizontal overflow

### Test 11: Small Mobile (< 480px)
- [ ] Popup fits screen
- [ ] Text readable
- [ ] Buttons accessible
- [ ] No layout breaking

---

## ♿ ACCESSIBILITY TESTS

### Test 12: Screen Reader
- [ ] Popup announced as dialog
- [ ] Title read correctly
- [ ] ARIA labels present
- [ ] Focus management works

### Test 13: Keyboard Navigation
- [ ] Tab through interactive elements
- [ ] ESC closes popup
- [ ] Enter activates buttons
- [ ] Focus visible

### Test 14: Reduced Motion
**Steps**:
1. Enable "Reduce motion" in OS settings
2. Trigger popup

**Expected**:
- [ ] Popup appears without animation
- [ ] Still functional
- [ ] No jarring transitions

---

## 🔧 TECHNICAL VALIDATION

### Test 15: Storage API
**Check in Console**:

```javascript
// sessionStorage test
sessionStorage.setItem('test', 'test')
sessionStorage.getItem('test')  // Should return 'test'
sessionStorage.removeItem('test')

// localStorage test
localStorage.setItem('test', 'test')
localStorage.getItem('test')  // Should return 'test'
localStorage.removeItem('test')
```

**Expected**:
- [ ] sessionStorage available
- [ ] localStorage available
- [ ] No errors or warnings

---

### Test 16: Storage Keys
**After triggering popup on article, check console**:

```javascript
// Check page-specific key
sessionStorage.getItem('popup_' + window.location.pathname)
// Should return: "shown"

// Check global counter
localStorage.getItem('popup_global_counter')
// Should return: "1" (or higher)

// Check timestamp
localStorage.getItem('popup_global_timestamp')
// Should return: timestamp number
```

**Expected**:
- [ ] Page key exists in sessionStorage
- [ ] Counter increments properly
- [ ] Timestamp is valid

---

### Test 17: Memory Leaks
**Steps**:
1. Open DevTools → Performance
2. Start recording
3. Visit 10 articles with popups
4. Stop recording
5. Check memory graph

**Expected**:
- [ ] No continuous memory growth
- [ ] Event listeners cleaned up
- [ ] No detached DOM nodes

---

### Test 18: XSS Protection
**Steps**:
1. Inspect popup HTML in DevTools
2. Check article title, description, image URL

**Expected**:
- [ ] All text properly escaped
- [ ] No raw HTML injection possible
- [ ] Special characters handled correctly

---

## 🌐 BROWSER COMPATIBILITY

### Test 19: Chrome/Edge
- [ ] All features work
- [ ] No console errors
- [ ] Smooth animations
- [ ] Storage APIs work

### Test 20: Firefox
- [ ] All features work
- [ ] No console errors
- [ ] Smooth animations
- [ ] Storage APIs work

### Test 21: Safari (Desktop)
- [ ] All features work
- [ ] No console errors
- [ ] Animations work
- [ ] Storage APIs work

### Test 22: Safari (iOS)
- [ ] Touch interactions work
- [ ] Layout responsive
- [ ] Storage works
- [ ] No scrolling issues

### Test 23: Chrome Mobile (Android)
- [ ] Touch interactions work
- [ ] Layout responsive
- [ ] Storage works
- [ ] No scrolling issues

---

## 🐛 EDGE CASES

### Test 24: No Related Articles
**Steps**:
1. Visit article with no related content

**Expected**:
- [ ] Popup does NOT render
- [ ] No JavaScript errors
- [ ] Page works normally

---

### Test 25: Storage Disabled
**Steps**:
1. Disable cookies/storage in browser
2. Visit article

**Expected**:
- [ ] Popup still shows (no storage = no blocking)
- [ ] May show on every page load (acceptable)
- [ ] No JavaScript errors

---

### Test 26: Ad Blockers
**Steps**:
1. Enable ad blocker
2. Visit article

**Expected**:
- [ ] Popup still shows (not blocked as ad)
- [ ] All features work

---

### Test 27: Slow Connection
**Steps**:
1. Enable network throttling (DevTools)
2. Visit article

**Expected**:
- [ ] Popup renders when JS loads
- [ ] No race conditions
- [ ] Graceful degradation

---

### Test 28: Very Long Article
**Steps**:
1. Visit long article (10,000+ words)
2. Test scroll trigger

**Expected**:
- [ ] 30% calculation correct
- [ ] Popup triggers at right position
- [ ] No performance issues

---

### Test 29: Very Short Article
**Steps**:
1. Visit short article (< 500 words)
2. Test scroll trigger

**Expected**:
- [ ] 30% calculation correct
- [ ] Popup still triggers
- [ ] No division by zero

---

## 📊 ANALYTICS VALIDATION

### Test 30: Event Tracking
**If analytics enabled, check**:

```javascript
// Should fire when popup shown
gtag('event', 'suggestion_shown', ...)

// Should fire when article clicked
gtag('event', 'suggestion_click', ...)
```

**Expected**:
- [ ] Events fire correctly
- [ ] Data captured properly

---

## 🚀 PRODUCTION CHECKS

### Test 31: Build Output
**Check `public/` directory**:

```bash
# Check if partial is included
grep -r "random-suggestion" public/cyber-security/*/index.html

# Check CSS is loaded
grep -r "random-suggestion.css" public/cyber-security/*/index.html
```

**Expected**:
- [ ] Popup HTML in single.html pages
- [ ] CSS file exists and linked
- [ ] JavaScript embedded correctly

---

### Test 32: Performance
**Run Lighthouse audit**:

**Expected**:
- [ ] No performance regression
- [ ] No CLS (Cumulative Layout Shift)
- [ ] No blocking JavaScript
- [ ] LCP not affected

---

### Test 33: SEO Impact
**Check with SEO tools**:

**Expected**:
- [ ] No duplicate content
- [ ] No hidden text
- [ ] No cloaking
- [ ] Popup doesn't affect crawling

---

## ✅ FINAL SIGN-OFF

### Critical Requirements
- [ ] ✅ Popup shows on every new article
- [ ] ✅ Dismissal is page-scoped
- [ ] ✅ Rate limiting works (max 20/day)
- [ ] ✅ No global blocking
- [ ] ✅ Triggers work (15s + 30% scroll)
- [ ] ✅ One trigger per page load
- [ ] ✅ ESC key closes popup
- [ ] ✅ Responsive design works
- [ ] ✅ No console errors
- [ ] ✅ Hugo build successful
- [ ] ✅ All browsers tested
- [ ] ✅ Accessibility verified

### Documentation
- [ ] ✅ POPUP_PAGE_SCOPED_FIX_COMPLETE.md
- [ ] ✅ POPUP_QUICK_REFERENCE.md
- [ ] ✅ POPUP_FIX_SUMMARY.md
- [ ] ✅ POPUP_VALIDATION_CHECKLIST.md
- [ ] ✅ test-popup-fix.html

### Code Quality
- [ ] ✅ Production-grade implementation
- [ ] ✅ XSS protection
- [ ] ✅ Memory leak prevention
- [ ] ✅ Event cleanup
- [ ] ✅ Error handling

---

## 🎉 COMPLETION CERTIFICATE

**Test Date**: _____________

**Tester Name**: _____________

**Results**:
- [ ] All tests passed
- [ ] Minor issues (documented below)
- [ ] Major issues (fix required)

**Notes**:
```
_________________________________________________
_________________________________________________
_________________________________________________
```

**Approval**:
- [ ] ✅ Ready for production deployment

**Signature**: _____________

---

## 📞 SUPPORT

**If any test fails**:

1. Check `POPUP_QUICK_REFERENCE.md` for quick fixes
2. Review `POPUP_PAGE_SCOPED_FIX_COMPLETE.md` for details
3. Use `test-popup-fix.html` for interactive debugging
4. Clear storage and try again
5. Check browser console for errors

---

**End of Checklist**
