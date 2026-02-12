# 💬 Comments System - Quick Reference Card

## 🚀 Quick Commands

```bash
# Install dependencies
npm install

# Test locally (with functions)
netlify dev

# Build site
hugo --gc --minify

# Deploy to production
git push origin main

# View function logs
netlify functions:log comments
```

---

## 📁 Key Files

```
Frontend:
  layouts/partials/comments.html
  assets/css/comments.css
  static/assets/js/comments.js

Backend:
  netlify/functions/comments.js

Config:
  netlify.toml
  package.json

Docs:
  docs/08-Comments/
```

---

## 🔧 Configuration Quick Access

### API Endpoint
```javascript
/api/comments
```

### Rate Limits
```
Client:  3 comments/minute
Server: 10 requests/minute
```

### Comment Limits
```
Min: 10 characters
Max: 2000 characters
```

---

## 🎨 Customization Quick Guide

### Change Colors
**File:** `assets/css/comments.css`
```css
:root {
    --accent-green: #00ff41;
    --accent-blue: #3aaddf;
    --accent-orange: #e06c11;
}
```

### Change Comment Limits
**File:** `netlify/functions/comments.js`
```javascript
const CONFIG = {
    MAX_COMMENT_LENGTH: 2000,
    MIN_COMMENT_LENGTH: 10,
};
```

### Require Approval
**File:** `netlify/functions/comments.js` (line ~230)
```javascript
status: 'pending'  // Change from 'approved'
```

---

## 🐛 Quick Troubleshooting

### Comments not showing?
```
1. Check browser console
2. Verify API endpoint
3. Check function logs
4. Ensure article slug correct
```

### Form not submitting?
```
1. Check JavaScript console
2. Verify validation
3. Check network tab
4. Review rate limiting
```

### Rate limit error?
```
1. Wait 60 seconds
2. Check spam protection
3. Review submit frequency
```

---

## 📊 Quick Test

### Local Test
```
1. netlify dev
2. Navigate to article
3. Submit comment
4. Verify success
5. Refresh page
6. Confirm displays
```

### Security Test
```
Submit: <script>alert('xss')</script>
Expected: Sanitized text display
```

---

## 📚 Documentation Quick Links

| Document | Purpose |
|----------|---------|
| `COMMENTS_README.md` | Quick overview |
| `INTEGRATION_STEPS.md` | Getting started |
| `COMMENTS_SYSTEM_GUIDE.md` | Full technical guide |
| `DEPLOYMENT_GUIDE.md` | Production deployment |
| `VALIDATION_CHECKLIST.md` | Testing checklist |

---

## 🔒 Security Checklist

```
✅ XSS Prevention
✅ Honeypot Field
✅ Rate Limiting
✅ Email Protection
✅ CORS Configured
✅ HTTPS Enforced
✅ Input Validation
```

---

## 📈 Performance Targets

```
Page Load:       +50KB
API Response:    <500ms
Render Time:     <100ms
Cache Duration:  5 minutes
```

---

## ✅ Pre-Deployment Checklist

```
[ ] npm install completed
[ ] netlify dev runs
[ ] Test comment submitted
[ ] Comment displays
[ ] Validation tested
[ ] Security tested
[ ] Mobile tested
[ ] No console errors
```

---

## 🎯 Support Quick Access

**Local Testing:**
```bash
netlify dev
```

**Check Logs:**
```bash
netlify functions:log comments
```

**Browser Console:**
```
F12 → Console tab
```

**Network Tab:**
```
F12 → Network tab → Filter: comments
```

---

## 📞 Need Help?

1. **Documentation:** `docs/08-Comments/README.md`
2. **Full Guide:** `COMMENTS_SYSTEM_GUIDE.md`
3. **Code Comments:** Check inline documentation
4. **Test Locally:** Use `netlify dev`

---

## 🎉 Status

```
✅ IMPLEMENTATION COMPLETE
✅ PRODUCTION READY
🚀 READY TO DEPLOY
```

---

**Keep this card handy for quick reference!**
