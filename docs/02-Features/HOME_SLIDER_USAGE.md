# 🎯 Homepage Slider - Quick Usage Guide

**Last Updated**: February 11, 2026

---

## 📝 Overview

The homepage slider is a **fully data-driven carousel** that displays featured articles with premium animations and optimal performance.

---

## 🚀 Quick Start

### Step 1: Edit Slide Data

Open `/data/main_slide.json` and add your slides:

```json
[
  {
    "title": "عنوان مقاله شما",
    "description": "توضیح کوتاه مقاله (حداکثر 120 کاراکتر)",
    "image": "/images/your-category/your-image.jpg",
    "url": "/your-category/your-article/",
    "readingTime": 15,
    "difficulty": "beginner",
    "lab_required": true,
    "post_type_fa": "آموزشی",
    "tags": ["tag1", "tag2", "tag3"],
    "categories": ["category1"]
  }
]
```

### Step 2: Add Your Image

1. Place your image in `/static/images/your-category/`
2. Recommended size: **1920x1080** (16:9 ratio)
3. Format: **WebP** or **JPG** (< 300KB)

### Step 3: Done!

No code changes needed. Hugo will automatically rebuild.

---

## 🎨 Field Reference

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `title` | string | Slide title | "راهنمای نصب Kali Linux" |
| `description` | string | Slide description | "آموزش کامل نصب..." |
| `image` | string | Image path (relative to /static) | "/images/linux/kali.jpg" |
| `url` | string | Article link | "/linux/kali-guide/" |

### Optional Fields

| Field | Type | Options | Default |
|-------|------|---------|---------|
| `readingTime` | integer | Minutes | None (badge hidden) |
| `difficulty` | string | beginner, medium, intermediate, advanced | None |
| `lab_required` | boolean | true, false | false |
| `post_type_fa` | string | Persian label | None |
| `tags` | array | String array | [] |
| `categories` | array | String array | [] |

---

## 🎯 Difficulty Levels

| Value | Persian Label | Color |
|-------|---------------|-------|
| `beginner` | مبتدی | Green |
| `medium` | متوسط | Yellow |
| `intermediate` | حرفه‌ای | Orange |
| `advanced` | تخصصی | Purple |

---

## 📊 Best Practices

### Content Guidelines

✅ **DO**:
- Keep titles under 60 characters
- Keep descriptions under 120 characters
- Use high-quality images (1920x1080)
- Compress images (< 300KB)
- Use 3-5 tags per slide
- Use 1-2 categories max

❌ **DON'T**:
- Use overly long titles (breaks mobile layout)
- Use low-resolution images
- Upload huge images (slows LCP)
- Leave required fields empty

### Image Optimization

```bash
# Recommended tools:
# - TinyPNG (https://tinypng.com)
# - Squoosh (https://squoosh.app)
# - ImageOptim (https://imageoptim.com)

# Target specs:
- Dimensions: 1920x1080
- Format: WebP (fallback JPG)
- Quality: 80%
- Size: < 300KB
```

### Slide Count

- **Minimum**: 1 slide (nav hidden automatically)
- **Optimal**: 3-5 slides
- **Maximum**: 7 slides (more may hurt UX)

---

## 🔄 Update Workflow

### Adding a New Slide

1. Open `/data/main_slide.json`
2. Add new object to array
3. Save file
4. Rebuild Hugo: `hugo server`

### Removing a Slide

1. Open `/data/main_slide.json`
2. Delete object from array
3. Save file

### Reordering Slides

Simply rearrange objects in the JSON array. First object = first slide.

---

## 🎬 Examples

### Example 1: Beginner Tutorial

```json
{
  "title": "آشنایی با شبکه برای مبتدیان",
  "description": "یادگیری مفاهیم اولیه شبکه و پروتکل‌های اساسی",
  "image": "/images/network/network-basics.jpg",
  "url": "/network/network-basics/",
  "readingTime": 10,
  "difficulty": "beginner",
  "lab_required": false,
  "post_type_fa": "آموزشی",
  "tags": ["network", "beginner"],
  "categories": ["network"]
}
```

### Example 2: Advanced Lab

```json
{
  "title": "تست نفوذ شبکه با Nmap",
  "description": "تکنیک‌های پیشرفته اسکن شبکه و شناسایی آسیب‌پذیری",
  "image": "/images/tools/nmap-advanced.jpg",
  "url": "/tools/nmap-advanced/",
  "readingTime": 30,
  "difficulty": "advanced",
  "lab_required": true,
  "post_type_fa": "آموزشی",
  "tags": ["nmap", "network", "pentest"],
  "categories": ["tools", "network"]
}
```

### Example 3: News Article

```json
{
  "title": "آسیب‌پذیری جدید در OpenSSL",
  "description": "کشف باگ امنیتی حیاتی در نسخه 3.0.7",
  "image": "/images/news/openssl-vulnerability.jpg",
  "url": "/news/openssl-cve-2024/",
  "readingTime": 5,
  "difficulty": "medium",
  "lab_required": false,
  "post_type_fa": "خبر",
  "tags": ["security", "openssl", "vulnerability"],
  "categories": ["news"]
}
```

---

## 🐛 Common Issues

### Issue: Slide not appearing

**Check**:
1. JSON syntax is valid (use JSONLint)
2. All required fields present
3. Hugo rebuild completed
4. Browser cache cleared

### Issue: Image not loading

**Check**:
1. Image path correct (starts with `/`)
2. Image exists in `/static/images/`
3. File extension matches (case-sensitive)
4. Image accessible (permissions)

### Issue: Layout broken on mobile

**Check**:
1. Title length (max 60 chars)
2. Description length (max 120 chars)
3. CSS file loaded
4. Browser DevTools for errors

---

## 🎯 Performance Tips

### Image Optimization

```bash
# Before uploading:
1. Resize to 1920x1080
2. Compress to < 300KB
3. Convert to WebP if possible
4. Test on mobile devices
```

### First Slide Priority

The **first slide** in the array is automatically preloaded for optimal LCP. Put your most important/popular article first!

---

## 📱 Mobile Preview

Test your slides on various devices:

- iPhone: Safari
- Android: Chrome
- Tablet: iPad Safari
- Desktop: Chrome, Firefox, Edge

**Tip**: Use Chrome DevTools (F12) → Device Mode for quick testing.

---

## 🔒 Security Notes

### Content Safety

- Always sanitize user-provided content
- Validate JSON structure before deployment
- Use relative URLs for images/links
- Avoid external image sources (CORS issues)

### Image Sources

Only use images you own or have rights to use. Avoid:
- Copyrighted images
- Hotlinked images (bandwidth theft)
- Unoptimized stock photos

---

## 📞 Support

For issues or questions:

1. Check `/docs/02-Features/HOME_SLIDER_IMPLEMENTATION.md`
2. Review browser console for errors
3. Test JSON validity at JSONLint.com
4. Inspect Network tab for failed requests

---

## ✅ Pre-Deployment Checklist

Before going live:

- [ ] All images optimized (< 300KB)
- [ ] JSON syntax validated
- [ ] All URLs tested (404 check)
- [ ] Mobile responsive tested
- [ ] Performance tested (Lighthouse)
- [ ] Accessibility tested (keyboard nav)
- [ ] Cross-browser tested
- [ ] Schema.org validated (Google Rich Results)

---

## 🎓 Learning Resources

- [Hugo Data Files](https://gohugo.io/templates/data-templates/)
- [JSON Format](https://www.json.org/)
- [Image Optimization](https://web.dev/fast/#optimize-your-images)
- [Core Web Vitals](https://web.dev/vitals/)

---

**Happy Sliding!** 🎉
