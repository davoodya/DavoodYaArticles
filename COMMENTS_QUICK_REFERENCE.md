# 🚀 COMMENTS SYSTEM - QUICK REFERENCE

## ⚡ ONE-LINER COMMANDS

### Local Development
```bash
start-dev.bat
```
**Opens:** `http://localhost:8888`

### Production Deploy
```bash
netlify deploy --prod
```

---

## 🔧 KEY FILES

| File | Purpose |
|------|---------|
| `static/assets/js/comments.js` | Frontend logic |
| `netlify/functions/comments.js` | Backend API |
| `netlify/functions/admin-comments.js` | Admin API |
| `static/admin/index.html` | Admin panel |
| `layouts/partials/comments.html` | HTML template |

---

## 🌐 ENDPOINTS

### Public
- Submit: `POST /.netlify/functions/comments`
- Get: `GET /.netlify/functions/comments?article=SLUG`

### Admin
- Manage: `POST /.netlify/functions/admin-comments`
- Panel: `/admin/`

---

## 🔑 CONFIGURATION

### Admin Email (Auto-Approve)
**File:** `netlify/functions/comments.js`
```javascript
ADMIN_EMAIL: 'davoodya40@gmail.com'
```

### Admin Password
**Netlify Env Var:** `ADMIN_PASSWORD`

---

## ✅ CRITICAL CHECKS

Before deploy:
- [ ] `npm install` completed
- [ ] Endpoint: `/.netlify/functions/comments` ✅
- [ ] NOT: `/api/comments.php` ❌
- [ ] Env var `ADMIN_PASSWORD` set

---

## 🐛 QUICK DEBUG

### Error: "Unexpected token '<'"
**Fix:** Clear cache + verify endpoint URL

### Error: "Failed to fetch"
**Fix:** Check Netlify Functions logs

### Comments not saving
**Fix:** Check function response + Netlify Blobs

---

## 📚 FULL DOCS

- **Complete Guide:** `COMMENTS_SYSTEM_COMPLETE.md`
- **Fix Summary:** `COMMENTS_SYSTEM_FIXED.md`
- **Local Dev:** `COMMENTS_LOCAL_DEV.md`
- **Validation:** `COMMENTS_VALIDATION_CHECKLIST.md`

---

**Ready? Run:** `start-dev.bat` 🚀
