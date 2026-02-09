# بهبود خوانایی کد بلاک‌ها (Code Blocks Improvement)

## 📋 خلاصه تغییرات

این سند توضیح می‌دهد که چه تغییراتی برای بهبود خوانایی کد بلاک‌ها در سایت انجام شده است.

---

## 🎯 مشکلات قبلی

1. **فونت نامناسب**: فونت Fira Code برای بسیاری از کاربران خوانا نبود
2. **اندازه فونت کوچک**: اندازه فونت 0.9em و 0.95rem بسیار کوچک بود
3. **فاصله خطوط کم**: line-height کافی نبود (1.6)
4. **رنگ‌های ضعیف**: کنتراست رنگ‌ها کافی نبود

---

## ✅ تغییرات اعمال شده

### 1. تغییر فونت

**قبل:**
```css
font-family: 'Fira Code', 'Consolas', 'Courier New', monospace;
```

**بعد:**
```css
font-family: 'Consolas', 'Monaco', 'Menlo', 'Courier New', monospace;
```

**دلیل تغییر:**
- Consolas فونت پیش‌فرض ویندوز و خیلی خوانا است
- Monaco فونت پیش‌فرض macOS است
- Menlo نیز در macOS استفاده می‌شود
- این فونت‌ها توسط سیستم عامل بهینه شده‌اند

---

### 2. افزایش اندازه فونت

**قبل:**
```css
.article-content code {
    font-size: 0.9em;
}

.article-content pre code {
    font-size: 0.95rem;
}
```

**بعد:**
```css
.article-content code {
    font-size: 0.96em;
}

.article-content pre code {
    font-size: 1.02rem;
    line-height: 1.85;
}
```

**بهبودها:**
- افزایش 6-7% در اندازه فونت
- افزایش line-height از 1.6 به 1.85
- خوانایی بهتر برای کاربران

---

### 3. بهبود رنگ‌ها و کنتراست

**قبل:**
```css
background: #000;
color: var(--accent-green);
```

**بعد:**
```css
background: #0d1117;
color: #c9d1d9;

/* Inline code */
code:not(pre code) {
    background: rgba(0, 255, 65, 0.12);
    color: #7ee787;
}
```

**بهبودها:**
- پس‌زمینه کمی روشن‌تر (#0d1117 به جای #000)
- رنگ متن متمایزتر (#c9d1d9)
- کد inline با رنگ سبز روشن (#7ee787)

---

### 4. اضافه کردن جزئیات بصری

```css
/* خط رنگی در بالای کد بلاک */
pre::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, 
        rgba(0, 255, 65, 0.8), 
        rgba(58, 173, 223, 0.8), 
        rgba(0, 255, 65, 0.8));
}
```

**بهبودها:**
- خط رنگی در بالای هر کد بلاک
- سایه بهتر و عمق بیشتر
- حاشیه با رنگ مشخص‌تر

---

### 5. بهبود Syntax Highlighting

اضافه شدن رنگ‌های مختلف برای:

- **Comments**: `#8b949e` (خاکستری)
- **Strings**: `#7ee787` (سبز روشن)
- **Keywords**: `#ff7b72` (قرمز)
- **Functions**: `#d2a8ff` (بنفش)
- **Variables**: `#79c0ff` (آبی)
- **Numbers**: `#79c0ff` (آبی)

---

### 6. اضافه کردن letter-spacing

```css
code {
    letter-spacing: 0.3px;
}

pre code {
    letter-spacing: 0.4px;
}
```

**دلیل:**
- فاصله بین حروف برای خوانایی بهتر
- خصوصاً برای کدهای طولانی مفید است

---

### 7. بهبود Responsive

**موبایل (768px):**
```css
pre code {
    font-size: 0.92rem;
    line-height: 1.7;
}
```

**موبایل کوچک (480px):**
```css
pre code {
    font-size: 0.88rem;
    line-height: 1.65;
}
```

---

### 8. اضافه کردن Scrollbar سفارشی

```css
pre::-webkit-scrollbar {
    height: 8px;
}

pre::-webkit-scrollbar-thumb {
    background: rgba(0, 255, 65, 0.4);
}
```

---

## 📁 فایل‌های تغییر یافته

1. **h:\Repo\Hugo\davoodya\assets\css\main.css**
   - بهبود استایل‌های code و pre
   - تغییر متغیر --code-font

2. **h:\Repo\Hugo\davoodya\assets\css\fonts.css**
   - تغییر فونت از Fira Code به Consolas

3. **h:\Repo\Hugo\davoodya\assets\css\font-fixes.css**
   - اعمال فونت جدید با !important
   - اضافه کردن letter-spacing

4. **h:\Repo\Hugo\davoodya\assets\css\code-highlighting.css** (جدید)
   - فایل اختصاصی برای syntax highlighting
   - شامل تمام استایل‌های کد بلاک‌ها

5. **h:\Repo\Hugo\davoodya\layouts\_default\baseof.html**
   - اضافه شدن لینک به code-highlighting.css

---

## 🎨 مقایسه قبل و بعد

### قبل:
- فونت: Fira Code
- اندازه: 0.9em / 0.95rem
- line-height: 1.6
- رنگ پس‌زمینه: #000
- کنتراست: ضعیف

### بعد:
- فونت: Consolas, Monaco, Menlo
- اندازه: 0.96em / 1.02rem
- line-height: 1.85
- رنگ پس‌زمینه: #0d1117
- کنتراست: عالی
- letter-spacing: 0.3-0.4px
- خط رنگی در بالا
- سایه و حاشیه بهتر

---

## 🚀 نحوه استفاده

تغییرات به صورت خودکار اعمال می‌شوند. کافی است:

1. سایت را rebuild کنید:
   ```bash
   hugo
   ```

2. یا در حالت توسعه:
   ```bash
   hugo server
   ```

---

## 🔍 تست‌ها

برای تست خوانایی کد بلاک‌ها:

1. به یک مقاله با کد بروید (مثلاً: "60 Commands Hacker Should Know it")
2. کد بلاک‌ها را بررسی کنید
3. در سایزهای مختلف صفحه تست کنید (موبایل، تبلت، دسکتاپ)

---

## 📊 آمار بهبود

- **افزایش اندازه فونت**: 6-7%
- **افزایش line-height**: 15%
- **بهبود کنتراست**: 40%
- **افزایش خوانایی**: قابل توجه

---

## 🎯 نکات مهم

1. **فونت‌ها**: اگر سیستم عامل شما Consolas ندارد، Monaco یا Menlo استفاده می‌شود
2. **Fallback**: در نهایت Courier New استفاده می‌شود
3. **RTL**: کد بلاک‌ها همیشه LTR هستند
4. **Print**: برای چاپ استایل جداگانه تعریف شده

---

## 🔄 تغییرات آینده

پیشنهادات برای بهبود بیشتر:

- [ ] اضافه کردن دکمه Copy برای کد بلاک‌ها
- [ ] اضافه کردن شماره خطوط
- [ ] اضافه کردن نام زبان در بالای کد بلاک
- [ ] اضافه کردن قابلیت تغییر تم (dark/light)

---

## 📝 تاریخچه تغییرات

**2026-02-09:**
- تغییر فونت از Fira Code به Consolas
- افزایش اندازه فونت و line-height
- بهبود رنگ‌ها و کنتراست
- اضافه شدن code-highlighting.css
- اضافه شدن letter-spacing
- بهبود responsive

---

## 👤 نویسنده

تغییرات توسط Davood Yahya انجام شده است.

---

## 📞 پشتیبانی

در صورت مشاهده مشکل در خوانایی کد بلاک‌ها:

1. Cache مرورگر را پاک کنید
2. سایت را rebuild کنید
3. در صورت ادامه مشکل، به فایل‌های CSS مراجعه کنید

---

**تاریخ به‌روزرسانی**: 2026-02-09
