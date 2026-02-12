# 🚀 Popup Quick Reference

**Fast reference for the page-scoped popup fix**

---

## ⚡ Quick Summary

| What Changed | Before | After |
|-------------|--------|-------|
| **Scope** | Site-wide | Page-specific |
| **Storage** | Cookie (global) | sessionStorage (per page) |
| **Behavior** | 1 popup/day total | 1 popup per article visited |
| **Rate Limit** | None | 20 popups/day max |

---

## 🔑 Key Concepts

### Page-Scoped Storage
```javascript
// Each article has unique key
sessionStorage: "popup_/article-x/" → "shown"
sessionStorage: "popup_/article-y/" → "shown"
sessionStorage: "popup_/article-z/" → "shown"

// Closing popup on Article X does NOT affect Article Y
```

### Global Rate Limiter
```javascript
// Prevents spam
localStorage: "popup_global_counter" → 5
localStorage: "popup_global_timestamp" → 1739305200000

// Max 20 popups per day, then block
// Resets automatically after 24 hours
```

---

## 📝 Configuration

```javascript
const CONFIG = {
    showDelay: 15000,              // 15 seconds
    minScrollPercent: 30,          // 30% scroll
    globalCooldownHours: 24,       // 24 hours
    maxPopupsPerDay: 20,           // Max 20 per day
    storagePrefix: 'popup_',       // Key prefix
    disableBelowWidth: 0           // Mobile disable (0 = always show)
};
```

### Common Adjustments

**Show faster (10 seconds)**
```javascript
showDelay: 10000
```

**More aggressive scroll (20%)**
```javascript
minScrollPercent: 20
```

**Disable on mobile**
```javascript
disableBelowWidth: 768
```

**Allow 50 popups per day**
```javascript
maxPopupsPerDay: 50
```

---

## 🧪 Testing

### Quick Test in Browser Console

```javascript
// Check if popup shown on current page
sessionStorage.getItem('popup_' + window.location.pathname)

// Check global counter
localStorage.getItem('popup_global_counter')

// Reset current page
sessionStorage.removeItem('popup_' + window.location.pathname)

// Reset rate limit
localStorage.removeItem('popup_global_counter')
localStorage.removeItem('popup_global_timestamp')

// Clear everything
sessionStorage.clear()
localStorage.clear()
```

### Validation Test File

Open `test-popup-fix.html` in browser:
- Interactive tests
- Storage inspector
- Rate limit simulator
- Full workflow test

---

## 🐛 Quick Fixes

### Popup not showing?

```javascript
// Console check:
sessionStorage.getItem('popup_' + window.location.pathname)  // Should be null
localStorage.getItem('popup_global_counter')                  // Should be < 20

// Fix:
sessionStorage.clear()
localStorage.removeItem('popup_global_counter')
localStorage.removeItem('popup_global_timestamp')
```

### Popup showing too often?

```javascript
// Reduce limit
maxPopupsPerDay: 10  // Instead of 20
```

### Popup showing on mobile?

```javascript
// Disable below 768px
disableBelowWidth: 768
```

---

## 📊 Expected Behavior

| Scenario | Popup Shows? |
|----------|--------------|
| First visit to Article A | ✅ Yes |
| Refresh Article A (same tab) | ❌ No (session persists) |
| Visit Article B (same tab) | ✅ Yes |
| Visit Article C (same tab) | ✅ Yes |
| Visit 20 articles | ✅ Yes (all 20) |
| Visit 21st article | ❌ No (rate limit) |
| Next day | ✅ Yes (reset) |
| Open Article A in new tab | ✅ Yes (different session) |

---

## 🔧 Files Modified

| File | What Changed |
|------|--------------|
| `layouts/partials/random-suggestion.html` | Complete refactor |
| `assets/css/random-suggestion.css` | Added accessibility |

---

## ✅ Checklist

Before deployment:
- [ ] Hugo build successful
- [ ] No console errors
- [ ] Test in Chrome, Firefox, Safari
- [ ] Test on mobile
- [ ] Test multiple articles
- [ ] Test rate limiting
- [ ] Test ESC key
- [ ] Test storage APIs

---

## 📞 Need Help?

1. Check `POPUP_PAGE_SCOPED_FIX_COMPLETE.md` (full docs)
2. Open `test-popup-fix.html` (validation tool)
3. Check browser console for errors
4. Verify storage in DevTools

---

**Status**: ✅ Production Ready  
**Date**: February 12, 2026
