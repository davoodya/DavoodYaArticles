# راهنمای سریع URL Canonical Updater

## 🚀 استفاده سریع

### 1. اجرای اسکریپت
```bash
python url-canonical-updater.py
```

### 2. وارد کردن مسیر
- **برای پردازش کل content**: فقط Enter بزنید
- **برای مسیر خاص**: مسیر را وارد کنید

مثال:
```
content/cyber-security
```

### 3. تایید
وقتی پرسید "آیا می‌خواهید ادامه دهید؟" تایپ کنید: `y`

---

## 📝 چه کاری انجام می‌دهد؟

این اسکریپت تمام URLهای front matter را پیدا کرده و به آنها `/knowledge/` اضافه می‌کند:

**قبل:**
```markdown
url = "https://davoodya.ir/cyber-security/article/"
canonical = "https://davoodya.ir/cyber-security/article/"
```

**بعد:**
```markdown
url = "https://davoodya.ir/knowledge/cyber-security/article/"
canonical = "https://davoodya.ir/knowledge/cyber-security/article/"
```

---

## ✅ ویژگی‌ها

- ✅ پشتیبانی از TOML (`---`) و YAML (`+++`)
- ✅ پشتیبانی از فرمت‌های مختلف: `url = "..."` و `url: "..."`
- ✅ Handle کردن Space در مسیر
- ✅ پردازش زیردایرکتوری‌ها
- ✅ گزارش کامل و لاگ دقیق

---

## ⚠️ نکات مهم

### 1. قبل از اجرا backup بگیرید!
```bash
git add .
git commit -m "Before URL update"
```

### 2. ابتدا روی یک پوشه کوچک تست کنید
مثلا:
```
content/cyber-security/SANS-401
```

### 3. بعد از اجرا بررسی کنید
- فایل لاگ: `url_canonical_updater_YYYYMMDD_HHMMSS.log`
- فایل گزارش: `url_canonical_updater_report_YYYYMMDD_HHMMSS.txt`

---

## 📊 خروجی‌ها

بعد از اجرا دو فایل ایجاد می‌شود:

1. **Log File**: تمام جزئیات پردازش
2. **Report File**: خلاصه آمار و لیست فایل‌های پردازش شده

---

## 🔍 مثال کامل

```bash
# اجرای اسکریپت
python url-canonical-updater.py

# پاسخ به سوالات:
# مسیر دایرکتوری: [Enter برای content/]
# ادامه دهید؟: y

# نتیجه:
# ✓ تعداد 45 فایل پیدا شد
# ✓ 42 فایل پردازش شد
# ✓ 3 فایل رد شد (URLهای قدیمی نداشتند)
# ✓ 84 جایگزینی انجام شد
```

---

## 📖 راهنمای کامل

برای جزئیات بیشتر، فایل زیر را مطالعه کنید:
```
docs/URL_CANONICAL_UPDATER_GUIDE.md
```

---

## 🧪 تست

برای تست اسکریپت:
```bash
python test-url-updater.py
```

این فایل‌های تست را در `test/test-url-updater/` پردازش می‌کند.

---

## ❓ سوالات متداول

### اگر اشتباهی اجرا کردم چه کنم؟
از Git برگردانید:
```bash
git checkout -- content/
```

### آیا می‌توانم دوباره اجرا کنم؟
بله! اگر دوباره اجرا کنید، فایل‌هایی که قبلا به‌روزرسانی شده‌اند رد می‌شوند.

### چرا برخی فایل‌ها رد می‌شوند؟
دلایل احتمالی:
- بدون front matter
- URL قدیمی ندارند
- قبلا به‌روزرسانی شده‌اند

---

## 📌 چک‌لیست

قبل از اجرا:
- [ ] Backup گرفته‌اید؟
- [ ] روی تعداد کمی فایل تست کردید؟
- [ ] مسیر را چک کرده‌اید؟

بعد از اجرا:
- [ ] لاگ فایل را بررسی کردید؟
- [ ] گزارش را خواندید؟
- [ ] چند فایل را دستی چک کردید؟
- [ ] Hugo را build کردید؟

---

**تاریخ ایجاد**: 2026-02-10  
**نسخه**: 1.0.0

برای پشتیبانی به documentation مراجعه کنید.
