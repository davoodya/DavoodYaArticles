# 🚀 Homepage Slider - Quick Reference Card

**Last Updated**: February 11, 2026

---

## 📝 Add/Edit Slides in 3 Steps

### Step 1: Edit Data File

```bash
File: /data/main_slide.json
```

### Step 2: Add Slide Object

```json
{
  "title": "Your Title Here",
  "description": "Short description (max 120 chars)",
  "image": "/images/category/image.jpg",
  "url": "/category/article-url/",
  "readingTime": 15,
  "difficulty": "beginner",
  "lab_required": true,
  "post_type_fa": "آموزشی",
  "tags": ["tag1", "tag2"],
  "categories": ["cat1"]
}
```

### Step 3: Rebuild

```bash
hugo server
```

---

## 🎯 Field Quick Reference

| Field | Required | Type | Example |
|-------|----------|------|---------|
| title | ✅ Yes | string | "راهنمای Kali" |
| description | ✅ Yes | string | "آموزش نصب..." |
| image | ✅ Yes | string | "/images/linux/kali.jpg" |
| url | ✅ Yes | string | "/linux/kali/" |
| readingTime | ❌ No | integer | 15 |
| difficulty | ❌ No | string | "beginner" |
| lab_required | ❌ No | boolean | true |
| post_type_fa | ❌ No | string | "آموزشی" |
| tags | ❌ No | array | ["tag1"] |
| categories | ❌ No | array | ["cat1"] |

---

## 🎨 Difficulty Values

| Value | Persian | Color |
|-------|---------|-------|
| `beginner` | مبتدی | 🟢 Green |
| `medium` | متوسط | 🟡 Yellow |
| `intermediate` | حرفه‌ای | 🟠 Orange |
| `advanced` | تخصصی | 🟣 Purple |

---

## 📸 Image Guidelines

- **Size**: 1920x1080 (16:9)
- **Format**: WebP or JPG
- **Max Size**: 300KB
- **Location**: `/static/images/category/`

---

## ⚡ Performance Tips

1. First slide = preloaded (put best article first)
2. Compress images before upload
3. Use WebP format when possible
4. Keep titles under 60 characters
5. Keep descriptions under 120 characters

---

## 🔧 Files Modified

```
✅ /data/main_slide.json          (slide data)
✅ /layouts/index.html             (includes slider)
✅ /layouts/_default/baseof.html   (CSS + JS)
✅ /layouts/partials/home-slider.html
✅ /assets/css/home-slider.css
✅ /static/assets/js/home-slider.js
```

---

## 🐛 Quick Troubleshooting

### Slide not showing?
- Check JSON syntax (JSONLint.com)
- Verify image path
- Rebuild Hugo

### Layout broken?
- Check title length (max 60 chars)
- Clear browser cache
- Test on mobile

### Image not loading?
- Image exists in `/static/images/`?
- Path starts with `/`?
- File extension correct?

---

## 📚 Full Documentation

- **Technical**: `/docs/02-Features/HOME_SLIDER_IMPLEMENTATION.md`
- **Usage**: `/docs/02-Features/HOME_SLIDER_USAGE.md`
- **Complete**: `/HOME_SLIDER_COMPLETE.md`

---

## ✅ Quick Test Checklist

- [ ] JSON valid (no syntax errors)
- [ ] Images optimized (< 300KB)
- [ ] Hugo builds without errors
- [ ] Mobile responsive (test in DevTools)
- [ ] Swipe works on mobile
- [ ] Keyboard arrows work (← →)

---

**Need Help?** Check the full documentation in `/docs/02-Features/`
