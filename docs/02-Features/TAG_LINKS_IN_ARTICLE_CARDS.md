# پیاده‌سازی لینک‌سازی برای تگ‌ها در Article Cards و Single Articles

**تاریخ:** 2026-02-09  
**وضعیت:** ✅ تکمیل شده

## مشکل

تگ‌های نمایش داده شده در Article Cards و Single Articles قابل کلیک نبودند و کاربران نمی‌توانستند با کلیک بر روی هر تگ، به صفحه لیست مقالات آن تگ دسترسی پیدا کنند.

## راه‌حل

### 1. تغییر در `layouts/_default/list.html` (Article Cards)

تگ‌ها را از `<span>` به `<a>` (لینک) تبدیل کردیم:

```html
<!-- قبل -->
<span class="article-tag">{{ . }}</span>

<!-- بعد -->
<a href="{{ "/tags/" | relLangURL }}{{ . | urlize }}" class="article-tag" title="مشاهده همه مقالات با تگ {{ . }}">{{ . }}</a>
```

### 2. تغییر در `layouts/_default/single.html` (Single Articles)

تگ‌های انتهای مقاله را هم از `<span>` به `<a>` تبدیل کردیم:

```html
<!-- قبل -->
<span class="article-tag-item">{{ . }}</span>

<!-- بعد -->
<a href="{{ "/tags/" | relLangURL }}{{ . | urlize }}" class="article-tag-item" title="مشاهده همه مقالات با تگ {{ . }}">{{ . }}</a>
```

**توضیحات:**
- `{{ "/tags/" | relLangURL }}`: مسیر پایه صفحات تگ را می‌سازد
- `{{ . | urlize }}`: نام تگ را به فرمت URL-friendly تبدیل می‌کند
- `title`: برای بهبود UX یک tooltip اضافه شده است

### 3. تغییرات CSS در `assets/css/main.css`

استایل‌های لینک را برای هر دو نوع تگ بهبود دادیم:

#### الف) استایل‌های تگ در Article Cards (`.article-tag`):

```css
.article-tag {
    /* ... استایل‌های قبلی ... */
    text-decoration: none;
    cursor: pointer;
}

.article-tag:hover {
    /* ... استایل‌های قبلی ... */
    box-shadow: 0 2px 8px rgba(58, 173, 223, 0.2);
}

/* استایل‌های جدید برای لینک‌ها */
a.article-tag {
    color: var(--accent-blue);
    text-decoration: none;
}

a.article-tag:visited {
    color: var(--accent-blue);
}

a.article-tag:active {
    transform: translateY(0);
}
```

#### ب) استایل‌های تگ در Single Articles (`.article-tag-item`):

```css
.article-tag-item {
    /* ... استایل‌های قبلی ... */
    text-decoration: none;
    cursor: pointer;
}

.article-tag-item:hover {
    /* ... استایل‌های قبلی ... */
    box-shadow: 0 3px 10px rgba(58, 173, 223, 0.3);
}

/* استایل‌های جدید برای لینک‌های تگ در Single Article */
a.article-tag-item {
    color: var(--accent-blue);
    text-decoration: none;
}

a.article-tag-item:visited {
    color: var(--accent-blue);
}

a.article-tag-item:active {
    transform: translateY(0);
}
```

## نتیجه

### قبل از تغییرات:
- ❌ تگ‌ها در Article Cards غیرقابل کلیک بودند
- ❌ تگ‌ها در Single Articles (انتهای مقاله) غیرقابل کلیک بودند
- ❌ کاربران نمی‌توانستند به راحتی مقالات مرتبط با یک تگ را پیدا کنند

### بعد از تغییرات:
- ✅ تمام تگ‌ها در Article Cards قابل کلیک هستند
- ✅ تمام تگ‌ها در Single Articles (انتهای مقاله) قابل کلیک هستند
- ✅ کلیک بر روی هر تگ کاربر را به صفحه لیست مقالات آن تگ می‌برد
- ✅ استایل‌های hover و active برای بهبود UX اضافه شدند
- ✅ لینک‌ها به صورت SEO-friendly با `urlize` تولید می‌شوند

## مثال‌های لینک تولید شده:

```
تگ: "cyber-security"    → /tags/cyber-security/
تگ: "network"           → /tags/network/
تگ: "web_developing"    → /tags/web_developing/
تگ: "0-seo-theories"    → /tags/0-seo-theories/
```

## تست

برای تست این ویژگی:

### تست 1: تگ‌های Article Cards

1. سرور Hugo را اجرا کنید:
   ```bash
   hugo server --port 1314
   ```

2. به صفحه لیست هر دسته‌بندی بروید (مثلاً `http://localhost:1314/network/`)

3. در هر Article Card، بر روی یکی از تگ‌ها کلیک کنید

4. باید به صفحه لیست مقالات آن تگ منتقل شوید

### تست 2: تگ‌های Single Articles

1. به یک مقاله وارد شوید (مثلاً `http://localhost:1314/network/network-basics-terminology-topology/`)

2. به انتهای مقاله بروید

3. در بخش "تگ‌ها"، بر روی یکی از تگ‌ها کلیک کنید

4. باید به صفحه لیست مقالات آن تگ منتقل شوید

## فایل‌های تغییر یافته:

1. ✅ `layouts/_default/list.html` - افزودن لینک به تگ‌ها در Article Cards
2. ✅ `layouts/_default/single.html` - افزودن لینک به تگ‌ها در Single Articles
3. ✅ `assets/css/main.css` - بهبود استایل‌های لینک‌های تگ (هر دو نوع)

## یادداشت‌های فنی:

- از تابع `urlize` Hugo استفاده شده تا نام تگ‌ها به فرمت URL-safe تبدیل شوند
- استایل‌های CSS به گونه‌ای طراحی شده‌اند که با theme کلی سایت هماهنگ باشند
- از `relLangURL` استفاده شده تا در صورت چندزبانه بودن سایت، لینک‌ها به درستی کار کنند
- در Article Cards: فقط 4 تگ اول نمایش داده می‌شوند (`first 4`) برای جلوگیری از شلوغی
- در Single Articles: تمام تگ‌ها نمایش داده می‌شوند
- کلاس‌های CSS متفاوت: `.article-tag` برای Cards و `.article-tag-item` برای Single Articles

## مزایای این تغییرات:

1. **بهبود تجربه کاربری (UX)**: کاربران می‌توانند از هر جای سایت به راحتی مقالات مرتبط را پیدا کنند
2. **افزایش Engagement**: تشویق کاربران به کاوش بیشتر در مقالات
3. **بهبود ناوبری سایت**: دسترسی سریع‌تر به محتوای مرتبط از دو نقطه مختلف (Cards و Single)
4. **سازگار با SEO**: استفاده از لینک‌های داخلی برای بهبود SEO و Internal Linking
5. **یکنواختی**: رفتار مشابه با تگ‌های Sidebar در سراسر سایت
6. **Accessibility**: افزودن tooltip برای راهنمایی بهتر کاربران

## تکمیل شده توسط:

Assistant AI - 2026-02-09

---

**وضعیت نهایی:** ✅ آماده برای Production
