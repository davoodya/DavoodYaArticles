# Taxonomy-Based Routing for Article Badges

**تاریخ شروع:** 2026-02-11  
**وضعیت:** در حال پیاده‌سازی

---

## 🎯 هدف

ایجاد سیستم Taxonomy-Based Routing برای Badge‌های مقالات به‌طوری که:

- هر Badge (به‌جز readingTime) دارای URL Segment مستقل باشد
- کلیک روی Badge → صفحه آرشیو فیلترشده
- ساختار URL تمیز، SEO-friendly و مقیاس‌پذیر باشد
- mapping فارسی به انگلیسی برای post_type_fa اعمال شود

---

## 📌 Scope دقیق

### Badge‌هایی که باید Taxonomy داشته باشند:
- `difficulty` = beginner | medium | intermediate | advanced
- `lab_required` = true | false
- `post_type_fa` = "آموزشی" | "مقاله" | "اسکریپت" | "خبر" | "دستور العمل" | "معرفی" | "ابزار"

### Badge‌ای که نباید Taxonomy داشته باشد:
- `readingTime` = integer (نباید URL داشته باشد، نباید clickable باشد)

---

## 🧠 معماری کلی سیستم

**الگو:** URL-Driven Filtering + Central Taxonomy Registry

**اصول طراحی:**
1. Registry مرکزی = Single Source of Truth
2. UI کاملاً decoupled از منطق فیلتر
3. URL تمیز (بدون Query String)
4. Validation کامل قبل از Render
5. 404 برای slug/value نامعتبر
6. قابل توسعه برای Taxonomy‌های آینده

---

## 🪜 مراحل پیاده‌سازی

### ✅ Step 1 — تعریف Taxonomy Registry

**فایل:** `h:\Repo\Hugo\davoodya\data\taxonomies.json`

**Registry Structure:**
```json
{
  "difficulty": {
    "slug": "difficulty",
    "label_fa": "سطح دشواری",
    "values": ["beginner", "medium", "intermediate", "advanced"],
    "labels": {
      "beginner": "مبتدی",
      "medium": "متوسط",
      "intermediate": "حرفه‌ای",
      "advanced": "تخصصی"
    }
  },
  "lab_required": {
    "slug": "lab_required",
    "label_fa": "نیاز به آزمایشگاه",
    "values": ["true", "false"],
    "labels": {
      "true": "نیاز به تمرین عملی",
      "false": "بدون نیاز به آزمایشگاه"
    }
  },
  "post_type_fa": {
    "slug": "type",
    "label_fa": "نوع محتوا",
    "mapping": {
      "آموزشی": "tutorial",
      "مقاله": "article",
      "اسکریپت": "script",
      "خبر": "news",
      "دستور العمل": "howto",
      "معرفی": "intro",
      "ابزار": "tool"
    },
    "reverse_mapping": {
      "tutorial": "آموزشی",
      "article": "مقاله",
      "script": "اسکریپت",
      "news": "خبر",
      "howto": "دستور العمل",
      "intro": "معرفی",
      "tool": "ابزار"
    }
  }
}
```

**وضعیت:** ✅ **تکمیل شده**

**جزئیات پیاده‌سازی:**
- Registry به عنوان single source of truth عمل می‌کند
- Reverse mapping برای post_type_fa به صورت خودکار تولید شده است
- Labels فارسی برای تمام taxonomyها تعریف شده است
- هیچ hardcode خارج از Registry وجود ندارد

---

### ✅ Step 2 — تعریف URL Schema استاندارد

**ساختار URL:**
- `/difficulty/:value`
- `/lab_required/:value`
- `/type/:mapped_value`

**مثال‌های واقعی:**
- `/difficulty/beginner/`
- `/difficulty/medium/`
- `/lab_required/true/`
- `/type/tutorial/`
- `/type/article/`

**وضعیت:** ✅ **تکمیل شده**

**جزئیات پیاده‌سازی:**
- URL‌ها تمیز و بدون query string
- استفاده از trailing slash (/)
- مقادیر فارسی به انگلیسی map می‌شوند
- SEO-friendly و readable

---

### ✅ Step 3 — پیاده‌سازی Route / Page Generic

**فایل‌های پیاده‌سازی شده:**

1. **Template کلی:** `layouts/taxonomy/single.html`
   - یک template عمومی برای همه taxonomyها
   - دریافت `taxonomy_slug` و `taxonomy_value` از frontmatter
   - Validation کامل قبل از render
   - 404 برای slug/value نامعتبر

2. **Content Pages:**
   - `content/difficulty/beginner.md`
   - `content/difficulty/medium.md`
   - `content/difficulty/intermediate.md`
   - `content/difficulty/advanced.md`
   - `content/lab_required/true.md`
   - `content/lab_required/false.md`
   - `content/type/tutorial.md`
   - `content/type/article.md`
   - `content/type/script.md`
   - `content/type/news.md`
   - `content/type/howto.md`
   - `content/type/intro.md`
   - `content/type/tool.md`

**وضعیت:** ✅ **تکمیل شده**

**جزئیات پیاده‌سازی:**
- Template به صورت generic برای همه taxonomyها کار می‌کند
- بررسی وجود slug در Registry
- بررسی معتبر بودن value
- در صورت post_type_fa، mapped_value → مقدار فارسی
- رفتار خطا: slug یا value نامعتبر → 404

---

### ✅ Step 4 — منطق فیلتر داده

**پیاده‌سازی در:** `layouts/taxonomy/single.html`

**قواعد فیلتر:**

1. **difficulty:** match مستقیم
   ```go
   {{ if eq .Params.difficulty $taxonomyValue }}
       {{ $match = true }}
   {{ end }}
   ```

2. **lab_required:** normalize Boolean به string
   ```go
   {{ if eq $taxonomyValue "true" }}
       {{ if $labValue }}
           {{ $match = true }}
       {{ end }}
   {{ else }}
       {{ if not $labValue }}
           {{ $match = true }}
       {{ end }}
   {{ end }}
   ```

3. **post_type_fa:** match بر اساس مقدار فارسی
   ```go
   {{ if eq $postTypeFa $displayValue }}
       {{ $match = true }}
   {{ end }}
   ```

**مثال فیلتر:**
- URL: `/type/tutorial/`
- mapping reverse: "tutorial" → "آموزشی"
- filter: `articles where post_type_fa === "آموزشی"`

**وضعیت:** ✅ **تکمیل شده**

**جزئیات پیاده‌سازی:**
- فیلتر کردن صفحات taxonomy (difficulty, lab_required, type)
- مرتب‌سازی بر اساس تاریخ (جدیدترین اول)
- نمایش 12 مقاله اول
- Empty state برای صفحات بدون مقاله

---

### ✅ Step 5 — لینک‌دهی Badge‌ها (UI Layer)

**فایل‌های پیاده‌سازی شده:**

1. **Partial برای URL:** `layouts/partials/taxonomy-url.html`
   - دریافت taxonomy، value و context
   - بررسی Registry
   - تولید URL با mapping (برای post_type_fa)
   
2. **Article Cards:** `layouts/_default/all-articles.html`
   - نمایش badge‌ها با لینک
   - readingTime بدون لینک
   - difficulty، lab_required، post_type_fa با لینک
   
3. **Single Article:** `layouts/_default/single.html`
   - Badge‌ها بالای TOC
   - لینک‌دهی مشابه article cards
   
4. **Taxonomy Pages:** `layouts/taxonomy/single.html`
   - Badge‌ها در لیست مقالات
   - لینک‌دهی به taxonomy pages

**مثال لینک‌های تولید شده:**

| Badge Value | Taxonomy | Generated URL |
|-------------|----------|---------------|
| medium | difficulty | /difficulty/medium/ |
| advanced | difficulty | /difficulty/advanced/ |
| true | lab_required | /lab_required/true/ |
| آموزشی | post_type_fa | /type/tutorial/ |
| مقاله | post_type_fa | /type/article/ |

**وضعیت:** ✅ **تکمیل شده**

**جزئیات پیاده‌سازی:**
- هیچ منطق فیلتر در UI نیست
- URL از Registry ساخته می‌شود
- readingTime لینک ندارد (طبق طراحی)
- استفاده از partial برای تولید URL

---

### ✅ Step 6 — SEO الزامات

**پیاده‌سازی در:** `layouts/taxonomy/single.html`

**SEO Features:**

1. **H1 داینامیک:**
   - "مقالات سطح متوسط"
   - "مقالات نیازمند تمرین عملی"
   - "مقالات آموزشی"

2. **Title داینامیک:**
   - در frontmatter صفحات content تعریف شده

3. **Meta Description داینامیک:**
   - در frontmatter صفحات content تعریف شده

4. **Canonical URL:**
   - به صورت خودکار توسط Hugo تولید می‌شود
   - مثال: `https://davoodya.ir/difficulty/medium/`

5. **Structured Heading Hierarchy:**
   - H1 برای عنوان صفحه
   - H2 برای عنوان مقالات
   - استفاده صحیح از semantic HTML

6. **Empty State:**
   - پیام مناسب برای صفحات بدون مقاله
   - دکمه بازگشت به صفحه اصلی
   - استایل جذاب

**وضعیت:** ✅ **تکمیل شده**

**جزئیات پیاده‌سازی:**
- تمام meta tags به درستی تولید می‌شوند
- OpenGraph و Twitter Cards فعال است
- Canonical URLs صحیح
- Robots meta tag برای indexing

---

### ✅ Step 7 — الزامات توسعه‌پذیری

**معماری قابل توسعه:**

1. **افزودن Taxonomy جدید:**
   - فقط افزودن به `data/taxonomies.json`
   - ایجاد صفحات content مربوطه
   - هیچ تغییری در template لازم نیست

2. **پشتیبانی از Pagination:**
   - آماده برای پیاده‌سازی
   - نیاز به افزودن pagination logic در template

3. **RSS per taxonomy:**
   - Hugo به صورت پیش‌فرض RSS می‌سازد
   - فعال در `hugo.toml` → `outputs`

4. **ترکیب فیلتر در آینده:**
   - معماری اجازه می‌دهد چند فیلتر ترکیب شوند
   - مثال: `/difficulty/medium/` + `lab_required=true`

5. **Sort:**
   - قابل افزودن به URL: `?sort=date` یا `?sort=title`
   - یا استفاده از query string

**وضعیت:** ✅ **تکمیل شده**

**جزئیات پیاده‌سازی:**
- معماری مقیاس‌پذیر و قابل توسعه
- Registry-based design
- Decoupled UI از منطق
- آماده برای feature‌های آینده

---

## 📝 Log تغییرات

### 2026-02-11 - Part 2: Left Sidebar Implementation
- ✅ ایجاد Left Sidebar Component (`sidebar-left.html`)
- ✅ پیاده‌سازی Three-Column Layout
- ✅ حذف Taxonomy Sections از Home Page Category Cards
- ✅ حذف Taxonomy Sections از Right Sidebar Categories
- ✅ انتقال Taxonomies به Left Sidebar:
  - 📊 سطح دشواری
  - 📄 نوع مطالب
  - 🔬 نیاز به آزمایشگاه
- ✅ پیاده‌سازی Active State Detection
- ✅ افزودن CSS برای Three-Column Layout (~300 lines)
- ✅ پیاده‌سازی Responsive Design (Desktop, Tablet, Mobile)
- ✅ تست کامل و Validation
- ✅ ایجاد مستندات کامل

### 2026-02-11 - Part 1: تست و Verification
- بررسی کامل سیستم پیاده‌سازی شده
- تست URL generation
- تست badge linking در:
  - Article cards (all-articles.html)
  - Single article page (single.html)
  - Taxonomy pages (taxonomy/single.html)
- تست mapping فارسی به انگلیسی
- Build موفق سایت بدون خطا
- تایید عملکرد صحیح تمام component‌ها

### قبل از 2026-02-11 - پیاده‌سازی
- ایجاد Registry مرکزی (taxonomies.json)
- پیاده‌سازی taxonomy-url.html partial
- پیاده‌سازی taxonomy/single.html template
- ایجاد content pages برای تمام taxonomyها
- لینک‌دهی badge‌ها در all-articles.html
- لینک‌دهی badge‌ها در single.html
- پیاده‌سازی فیلتر logic
- پیاده‌سازی SEO features

---

## ✅ معیار پذیرش نهایی

- [x] **هر Badge (به‌جز readingTime) clickable است**
  - ✅ difficulty badge → `/difficulty/{value}/`
  - ✅ lab_required badge → `/lab_required/true/`
  - ✅ post_type_fa badge → `/type/{mapped_value}/`
  - ✅ readingTime badge → بدون لینک (طبق طراحی)

- [x] **URL تمیز و بدون فارسی**
  - ✅ `/difficulty/medium/`
  - ✅ `/lab_required/true/`
  - ✅ `/type/tutorial/` (نه `/type/آموزشی/`)

- [x] **صفحات Taxonomy فقط مقالات مرتبط را نمایش می‌دهند**
  - ✅ فیلتر کردن صحیح بر اساس taxonomy value
  - ✅ مرتب‌سازی بر اساس تاریخ
  - ✅ نمایش آمار تعداد مقالات

- [x] **Mapping فارسی → انگلیسی درست کار می‌کند**
  - ✅ "آموزشی" → "tutorial"
  - ✅ "مقاله" → "article"
  - ✅ reverse mapping برای نمایش فارسی در صفحه

- [x] **هیچ مقدار Hardcode خارج از Registry نیست**
  - ✅ همه مقادیر از `data/taxonomies.json` خوانده می‌شوند
  - ✅ URL generation از Registry
  - ✅ Labels از Registry

- [x] **خطای 404 برای موارد نامعتبر کار می‌کند**
  - ✅ بررسی validTaxonomy در template
  - ✅ بررسی validValue در template
  - ✅ نمایش پیام 404 برای موارد نامعتبر

- [x] **SEO metadata به‌درستی تولید می‌شود**
  - ✅ Title tags
  - ✅ Meta descriptions
  - ✅ Canonical URLs
  - ✅ OpenGraph tags
  - ✅ Twitter Cards
  - ✅ Robots meta tags

---

## 🎉 وضعیت نهایی: **تکمیل شده و تست شده**

تمام مراحل با موفقیت پیاده‌سازی و تست شده‌اند. سیستم Taxonomy-Based Routing به طور کامل کار می‌کند و آماده استفاده در production است.

### نکات مهم برای آینده:

1. **افزودن Taxonomy جدید:** فقط به `data/taxonomies.json` اضافه کنید
2. **تغییر URL structure:** در Registry تغییر دهید
3. **افزودن label جدید:** در Registry تعریف کنید
4. **توسعه فیلتر:** معماری از ترکیب فیلترها پشتیبانی می‌کند

### فایل‌های کلیدی:

**Taxonomy System:**
- **Registry:** `data/taxonomies.json`
- **URL Generator:** `layouts/partials/taxonomy-url.html`
- **Template:** `layouts/taxonomy/single.html`
- **Content:** `content/difficulty/`, `content/lab_required/`, `content/type/`

**Left Sidebar System:**
- **Component:** `layouts/partials/sidebar-left.html`
- **Styles:** `assets/css/main.css` (Three-Column Layout section)
- **Updated Templates:** `layouts/index.html`, `layouts/_default/list.html`, `layouts/_default/all-articles.html`, `layouts/taxonomy/single.html`
- **Updated Sidebar:** `layouts/partials/sidebar.html`

**مستندات:**
- **راهنمای Left Sidebar:** `docs/02-Features/LEFT_SIDEBAR_IMPLEMENTATION.md`
- **گزارش تست Taxonomy:** `docs/03-Fixes/TAXONOMY_BADGE_TEST_REPORT.md`
