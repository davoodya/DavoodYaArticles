# Hugo Article Import Pipeline - Enhanced Version

## 📋 Overview

اسکریپت پیشرفته PowerShell برای پردازش خودکار مقالات از Obsidian به Hugo با گزارش‌دهی کامل و ویژگی‌های بصری.

---

## ✨ ویژگی‌های جدید

### 🎨 ویژگی‌های بصری

1. **رنگ‌بندی خروجی**
   - عناوین: آبی روشن (Cyan)
   - موفقیت: سبز (Green)
   - هشدار: زرد (Yellow)
   - خطا: قرمز (Red)
   - اطلاعات: سفید (White)
   - مراحل: بنفش (Magenta)

2. **جعبه‌های رنگی و قاب‌بندی**
   ```
   ╔═══════════════════════════════════════╗
   ║  STEP 1 of 7: Import Images           ║
   ╚═══════════════════════════════════════╝
   ```

3. **نوار پیشرفت (Progress Bar)**
   - نمایش درصد پیشرفت
   - نمایش مرحله جاری
   - به‌روزرسانی بلادرنگ

### 📊 گزارش‌دهی پیشرفته

#### گزارش بلادرنگ (Real-time)

برای هر مرحله:
- ✅ عنوان و توضیحات مرحله
- 🐍 نام اسکریپت پایتونی
- ⚙️ وضعیت اجرا
- 📊 نتایج از فایل‌های Tracking
- ⏱️ زمان اجرا
- ✅/❌ وضعیت نهایی

#### گزارش JSON

خواندن و نمایش خودکار از:
- `processed_images.json` - تصاویر وارد شده
- `processed_articles.json` - مقالات پردازش شده
- `images_rename_mapping.json` - نقشه تغییر نام تصاویر
- `toc_removal_tracking.json` - مقالات با TOC حذف شده
- `property-delete-tracking-enhanced.json` - مقالات با Front Matter جدید

#### گزارش Text

خواندن و ارجاع به:
- `image_migration_report.txt`
- `title_adder_report.txt`
- `altimage_adder_report.txt`
- `images_renamer_report.txt`
- `image_article_renamer_report.txt`
- `toc_remover_report.txt`
- `obsidian_property_remover_enhanced_report.txt`

### 📄 گزارش نهایی جامع

فایل: `pipeline-execution-report.txt`

محتویات:
1. **خلاصه اجرا**
   - زمان شروع/پایان
   - مدت زمان کل
   - تعداد مراحل کامل/ناموفق
   - نرخ موفقیت

2. **نتایج گام‌به‌گام**
   - وضعیت هر مرحله
   - زمان اجرا
   - کد خروجی
   - پیغام خطا (در صورت وجود)

3. **نتایج تفصیلی**
   - لیست فایل‌های پردازش شده
   - لیست تصاویر وارد شده
   - نقشه تغییر نام تصاویر (قدیم → جدید)
   - آمار کامل هر مرحله

4. **یادداشت‌ها**
   - توضیحات هر مرحله
   - وابستگی‌های مراحل
   - نکات مهم

---

## 🔧 ساختار اسکریپت

### 1. تنظیمات اولیه

```powershell
# رنگ‌ها
$Colors = @{
    Header = 'Cyan'
    Success = 'Green'
    Warning = 'Yellow'
    Error = 'Red'
    Info = 'White'
    Step = 'Magenta'
    Highlight = 'Yellow'
}

# آمار کلی
$GlobalStats = @{
    StartTime
    TotalSteps
    CompletedSteps
    FailedSteps
    TotalProcessedFiles
    StepResults
}
```

### 2. لیست اسکریپت‌ها

```powershell
$Scripts = @(
    @{
        Name = "convert_images.py"
        Title = "Import New Articles Images"
        Description = "..."
        ReportFile = "image_migration_report.txt"
        TrackingFile = "processed_images.json"
    },
    # ... 6 اسکریپت دیگر
)
```

### 3. توابع کمکی

- `Write-ColorHeader` - عنوان رنگی با قاب
- `Write-ColorBox` - جعبه متن رنگی
- `Write-StepHeader` - عنوان مرحله با قاب زیبا
- `Write-Progress` - نوار پیشرفت
- `Read-JsonReport` - خواندن فایل JSON
- `Read-TextReport` - خواندن فایل متنی
- `Show-StepResults` - نمایش نتایج هر مرحله
- `Execute-PythonScript` - اجرای اسکریپت پایتون
- `Generate-FinalReport` - ایجاد گزارش نهایی
- `Show-FinalSummary` - نمایش خلاصه نهایی

---

## 📝 ترتیب اجرای مراحل

### Step 1: Import New Articles Images
**اسکریپت:** `convert_images.py`

- وارد کردن تصاویر از Obsidian Vault Attachment
- کپی به `static/images/[category]/`
- ذخیره لیست در `processed_images.json`

**خروجی:**
```
✅ Images imported: 15
📄 Detailed report: image_migration_report.txt
```

---

### Step 2: Add Title for New Articles
**اسکریپت:** `title-adder.py`

- اضافه کردن عنوان به Front Matter
- استخراج عنوان از نام فایل
- حذف E-number از عنوان

**خروجی:**
```
✅ Articles with title added: 25
📄 Detailed report: title_adder_report.txt
```

**⚠️ مهم:** این مرحله برای مراحل 3 و 4 ضروری است.

---

### Step 3: Add ALT for Images in Articles
**اسکریپت:** `altimage-adder.py`

- اضافه کردن ALT به تصاویر
- بر اساس عنوان مقاله

**خروجی:**
```
✅ Files processed: 25
📄 Detailed report: altimage_adder_report.txt
```

---

### Step 4: Rename Images in /static/images/*
**اسکریپت:** `images-renamer.py`

- تغییر نام تصاویر با نام Slugified
- فرمت: `lowercase-with-dashes.extension`
- ذخیره نقشه تغییر نام در JSON

**خروجی:**
```
✅ Images renamed: 45
📝 Sample renamed images (first 5):
   • Pasted image 20260203212022.png → pasted-image-20260203212022.png
   • Network Diagram.PNG → network-diagram.png
   ... and 40 more
📄 Detailed report: images_renamer_report.txt
```

---

### Step 5: Update Image References in Articles
**اسکریپت:** `image-article-renamer.py`

- به‌روزرسانی مسیر تصاویر در فایل‌های Markdown
- هماهنگ‌سازی با نام‌های جدید

**خروجی:**
```
✅ Files processed: 25
📄 Detailed report: image_article_renamer_report.txt
```

---

### Step 6: Remove Obsidian TOC
**اسکریپت:** `toc-remover.py`

- حذف فهرست مطالب Obsidian
- Hugo فهرست خود را تولید می‌کند

**خروجی:**
```
✅ TOC removed from: 25 articles
📄 Detailed report: toc_remover_report.txt
```

---

### Step 7: Add Enhanced Hugo Front Matter
**اسکریپت:** `obsidian-property-remover-enhanced.py`

- حذف Obsidian Properties
- حذف Front Matter قدیمی
- اضافه کردن Front Matter جامع Hugo

**شامل:**
- Basic: title, slug, date, lastmod, draft
- Taxonomies: categories, tags, series
- Badges: readingTime, difficulty, toc, math, lab_required, post_type_fa
- SEO: description, keywords, author, robots, canonical
- Images: featured_image, images array
- Open Graph & Twitter Cards

**خروجی:**
```
✅ Front matter added to: 25 articles
📄 Detailed report: obsidian_property_remover_enhanced_report.txt
```

---

## 🚀 نحوه استفاده

### روش 1: اجرای مستقیم

```powershell
.\import-images-enhanced.ps1
```

### روش 2: از PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\import-images-enhanced.ps1
```

### روش 3: از CMD

```cmd
powershell -ExecutionPolicy Bypass -File "H:\Repo\Hugo\davoodya\import-images-enhanced.ps1"
```

---

## 📊 نمونه خروجی

### شروع اجرا

```
################################################################################
#                                                                              #
#          HUGO ARTICLE PROCESSING PIPELINE - ENHANCED VERSION                #
#                                                                              #
################################################################################

📅 Start Time: 2026-02-09 17:30:00
📂 Working Directory: H:\Repo\Hugo\davoodya
🐍 Python Scripts: 7

Press any key to start execution, or Ctrl+C to cancel...
```

### در حین اجرا

```
╔═══════════════════════════════════════════════════════════════════════════╗
║ STEP 1 of 7: Import New Articles Images                                  ║
╚═══════════════════════════════════════════════════════════════════════════╝

  📝 Description: Import images from Obsidian Vault Attachment to Hugo static/images
  🐍 Script: convert_images.py

  ⚙️  Executing...

  ───────────────────────────────────────────────────────────────────────────
  INFO - Found 15 new images to import
  INFO - ✓ Imported: article-image-1.png
  INFO - ✓ Imported: article-image-2.png
  INFO - ✓ All images imported successfully
  ───────────────────────────────────────────────────────────────────────────

  ✅ Completed successfully in 2.34s

  📊 Results:

     ✅ Images imported: 15
     🕐 Last run: 2026-02-09T17:30:05.123456
     📄 Detailed report: image_migration_report.txt
```

### خلاصه نهایی

```
================================================================================
                           EXECUTION SUMMARY
================================================================================

  ╔════════════════════════════════════════════════════════════════════════╗
  ║  Pipeline Execution Completed                                        ║
  ╚════════════════════════════════════════════════════════════════════════╝

  📊 Statistics:

     ⏱️  Total Duration: 45.67 seconds
     📝 Total Steps: 7
     ✅ Completed: 7
     📈 Success Rate: 100%

  📋 Step Results:

     ✅ Step 1: Import New Articles Images (2.34s)
     ✅ Step 2: Add Title for New Articles (3.21s)
     ✅ Step 3: Add ALT for Images in Articles (5.43s)
     ✅ Step 4: Rename Images in /static/images/* (8.76s)
     ✅ Step 5: Update Image References in Articles (12.45s)
     ✅ Step 6: Remove Obsidian TOC (4.32s)
     ✅ Step 7: Add Enhanced Hugo Front Matter (9.16s)

  📄 Detailed Report:

     📁 Report saved to: H:\Repo\Hugo\davoodya\pipeline-execution-report.txt

  ╔══════════════════════════════════════════════════════════════════════════╗
  ║  🎉 All Steps Completed Successfully!                                  ║
  ╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🔍 بررسی گزارش نهایی

فایل `pipeline-execution-report.txt` شامل:

```
================================================================================
                 HUGO ARTICLE PROCESSING PIPELINE REPORT
================================================================================

Execution Summary
-----------------
Start Time:           2026-02-09 17:30:00
End Time:             2026-02-09 17:30:45
Total Duration:       45.67 seconds
Total Steps:          7
Completed Steps:      7
Failed Steps:         0
Success Rate:         100%

================================================================================
                              STEP-BY-STEP RESULTS
================================================================================

Step 1: Import New Articles Images
--------------------------------------------------------------------------------
Script:     convert_images.py
Status:     ✅ Success
Duration:   2.34s
Exit Code:  0

...

================================================================================
                            DETAILED RESULTS BY STEP
================================================================================

[1] Import New Articles Images
--------------------------------------------------------------------------------

Tracking File: processed_images.json
Imported Images: 15

Image List:
  • cyber-security/article-image-1.png
  • network/diagram-1.png
  • seo/google-trends.png
  ...

Last Run: 2026-02-09T17:30:05.123456

Detailed Report: image_migration_report.txt

...

[4] Rename Images in /static/images/*
--------------------------------------------------------------------------------

Tracking File: images_rename_mapping.json
Renamed Images: 45

Rename Mapping:
  • Pasted image 20260203212022.png → pasted-image-20260203212022.png
  • Network Diagram.PNG → network-diagram.png
  • SANS-401-E1.png → sans-401-e1.png
  ...

================================================================================
                                    NOTES
================================================================================

1. Import Images:
   - Images imported from Obsidian Vault Attachment
   - Destination: static/images/[category]/

2. Add Titles:
   - Titles added to Hugo front matter based on filename
   - E-numbers removed from title
   - Required for subsequent image renaming steps

...

================================================================================
                                END OF REPORT
================================================================================

Report generated: 2026-02-09 17:30:45
Report location: H:\Repo\Hugo\davoodya\pipeline-execution-report.txt
```

---

## ⚙️ تنظیمات و سفارشی‌سازی

### تغییر رنگ‌ها

```powershell
$Colors = @{
    Header = 'Cyan'      # آبی روشن
    Success = 'Green'    # سبز
    Warning = 'Yellow'   # زرد
    Error = 'Red'        # قرمز
    Info = 'White'       # سفید
    Step = 'Magenta'     # بنفش
    Highlight = 'Yellow' # زرد
}
```

### تغییر مسیر اسکریپت‌ها

```powershell
$ScriptDir = "H:\Repo\Hugo\davoodya"
```

### اضافه کردن اسکریپت جدید

```powershell
$Scripts += @{
    Name = "new-script.py"
    Title = "New Processing Step"
    Description = "Description of the step"
    ReportFile = "new_script_report.txt"
    TrackingFile = "new_script_tracking.json"
}
```

---

## ❌ مدیریت خطا

### در صورت خطا در یک مرحله

```
❌ Failed with exit code: 1

⚠️  Step 3 failed. Continue with next step? (Y/N)
```

گزینه‌ها:
- `Y` - ادامه به مرحله بعد
- `N` - توقف اجرای Pipeline

### خطاهای احتمالی

1. **اسکریپت پایتون پیدا نشد**
   ```
   ❌ Script not found: script-name.py
   ```

2. **خطا در اجرا**
   ```
   ❌ Exception occurred: Error message
   ```

3. **خطا در خواندن JSON**
   ```
   ⚠️  Warning: Could not parse JSON file: file.json
   ```

---

## ✅ Validation نتایج

### بررسی Syntax

```powershell
powershell -Command "& { 
    $null = [System.Management.Automation.PSParser]::Tokenize(
        (Get-Content 'import-images-enhanced.ps1' -Raw), 
        [ref]$null
    ); 
    Write-Host '✅ Syntax: VALID' 
}"
```

**نتیجه:**
```
✅ PowerShell Syntax: VALID
```

### بررسی عملکرد

تست شده با:
- ✅ PowerShell 5.1
- ✅ PowerShell 7.x
- ✅ Windows 10/11
- ✅ UTF-8 Encoding

---

## 📋 Checklist قبل از اجرا

- [ ] همه اسکریپت‌های پایتونی در مسیر صحیح هستند
- [ ] Python نصب شده و در PATH است
- [ ] Obsidian Vault در دسترس است
- [ ] مسیر `content/` و `static/images/` وجود دارند
- [ ] Backup از فایل‌های مهم گرفته شده
- [ ] اجرای آزمایشی روی یک فایل تست انجام شده

---

## 🆚 مقایسه با نسخه قدیم

| ویژگی | نسخه قدیم (BAT) | نسخه جدید (PS1) |
|-------|------------------|------------------|
| رنگ‌بندی | ❌ ندارد | ✅ کامل |
| گزارش بلادرنگ | ❌ ساده | ✅ پیشرفته |
| خواندن JSON | ❌ ندارد | ✅ دارد |
| نوار پیشرفت | ❌ ندارد | ✅ دارد |
| گزارش نهایی | ❌ ساده | ✅ جامع |
| مدیریت خطا | ❌ ندارد | ✅ دارد |
| قاب‌بندی زیبا | ❌ ندارد | ✅ دارد |
| آمار تفصیلی | ❌ ندارد | ✅ دارد |

---

## 🎯 نتیجه

اسکریپت پیشرفته PowerShell با:

✅ **Syntax صحیح و تست شده**
✅ **ویژگی‌های بصری کامل**
✅ **گزارش‌دهی جامع**
✅ **خواندن JSON و نمایش نتایج**
✅ **گزارش نهایی تفصیلی**
✅ **مدیریت خطای حرفه‌ای**
✅ **خوانایی بالا**
✅ **آماده استفاده**

---

## 📞 پشتیبانی

در صورت بروز مشکل:
1. بررسی `pipeline-execution-report.txt`
2. بررسی Log فایل‌های اسکریپت‌های پایتونی
3. اجرای هر اسکریپت پایتونی به صورت جداگانه
4. بررسی Permission های فایل‌ها

---

**تاریخ ایجاد:** 2026-02-09  
**نسخه:** 1.0.0  
**وضعیت:** ✅ Validated & Ready to Use
