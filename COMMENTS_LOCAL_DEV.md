# 🔧 LOCAL DEVELOPMENT - COMMENTS SYSTEM

## 🎯 GOAL

Test the comment system **locally** before deploying to Netlify.

---

## ⚙️ SETUP

### 1. Install Netlify CLI

```bash
npm install -g netlify-cli
```

### 2. Install Project Dependencies

```bash
cd h:\Repo\Hugo\davoodya
npm install
```

This installs:
- `@netlify/blobs@^7.0.0`

---

## 🚀 RUN LOCALLY

### Start Development Server

```bash
netlify dev
```

This will:
1. ✅ Build Hugo site
2. ✅ Start local server (usually `http://localhost:8888`)
3. ✅ Enable Netlify Functions at `http://localhost:8888/.netlify/functions/`
4. ✅ Simulate Netlify Blobs locally

---

## 🧪 TESTING

### 1. Open Site

```
http://localhost:8888
```

### 2. Navigate to Article

Any article with comments section.

### 3. Submit Test Comment

**Form Data:**
- Name: Test User
- Email: test@example.com
- Website: (optional)
- Comment: This is a local test comment

**Expected:**
- ✅ Success message: "دیدگاه شما با موفقیت ثبت شد..."
- ✅ Form resets
- ✅ Comment NOT displayed (pending approval)

### 4. Test Admin Auto-Approval

**Form Data:**
- Email: `davoodya40@gmail.com`

**Expected:**
- ✅ Success message: "دیدگاه شما با موفقیت ثبت و منتشر شد."
- ✅ Comment displayed immediately

### 5. Test Admin Panel

```
http://localhost:8888/admin/
```

**Login:**
- Password: `admin123` (default, change in production)

**Enter Article Slug:**
- Example: Type article slug and press Enter

**Actions:**
- Approve pending comments
- View approved comments
- Delete comments

---

## 🐛 DEBUGGING

### Check Netlify Function Logs

The `netlify dev` terminal shows function logs in real-time.

**Look for:**
```
◈ Functions GET /.netlify/functions/comments 200 123ms
◈ Functions POST /.netlify/functions/comments 201 234ms
```

### Check Browser Console

Press `F12` → Console tab

**Look for:**
- Network errors
- JSON parse errors
- CORS issues

### Check Network Tab

Press `F12` → Network tab

**Filter:** XHR

**Check:**
- Request URL: Should be `/.netlify/functions/comments`
- Response: Should be valid JSON
- Status: Should be 200 or 201

---

## 📁 LOCAL STORAGE

When running `netlify dev`, Netlify Blobs data is stored in:

```
.netlify/blobs-serve/
```

This folder is git-ignored.

---

## ⚠️ IMPORTANT NOTES

### 1. PHP Files Are Ignored

Even locally, **PHP files will not run** with `netlify dev`.

Only Netlify Functions work.

### 2. Environment Variables

Create `.env` file (git-ignored):

```env
ADMIN_PASSWORD=admin123
```

Netlify CLI will load this automatically.

### 3. Hugo Build

If you modify Hugo templates/content:

```bash
# Stop netlify dev (Ctrl+C)
# Then restart:
netlify dev
```

---

## 🔄 WORKFLOW

### Development Loop

1. **Code change**
2. **Save file**
3. **Refresh browser** (Hugo auto-rebuilds)
4. **Test feature**
5. **Check console/logs**
6. **Repeat**

### Function Changes

If you modify `netlify/functions/*.js`:

```bash
# Netlify dev auto-reloads functions
# Just refresh browser
```

---

## 🚨 COMMON ISSUES

### Issue: "Port 8888 already in use"

**Solution:**
```bash
netlify dev --port 3000
```

### Issue: "@netlify/blobs not found"

**Solution:**
```bash
npm install
```

### Issue: "Failed to fetch"

**Check:**
1. Is `netlify dev` running?
2. Correct endpoint: `/.netlify/functions/comments`?
3. Any errors in terminal?

### Issue: "Admin panel not working"

**Check:**
1. Password correct? (default: `admin123`)
2. Article slug exists?
3. Check browser console

---

## ✅ READY TO DEPLOY

Once everything works locally:

```bash
netlify deploy --prod
```

Or push to Git (if Netlify auto-deploy is configured).

---

## 📝 QUICK REFERENCE

**Start server:**
```bash
netlify dev
```

**Site URL:**
```
http://localhost:8888
```

**Admin panel:**
```
http://localhost:8888/admin/
```

**Functions endpoint:**
```
http://localhost:8888/.netlify/functions/comments
```

**Logs:**
Check terminal running `netlify dev`

**Stop server:**
```
Ctrl + C
```

---

**Happy coding! 🚀**
