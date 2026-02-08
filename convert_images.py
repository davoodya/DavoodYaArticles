"""
اسکریپت تبدیل و مدیریت تصاویر Obsidian به Hugo
نویسنده: Davood Yahya
تاریخ: 2026-02-08

این اسکریپت:
1. تمام فایل‌های markdown را اسکن می‌کند
2. لینک‌های تصویر Obsidian (![[image.png]]) را به فرمت استاندارد Markdown تبدیل می‌کند
3. دایرکتوری‌های مورد نیاز را ایجاد می‌کند
4. تصاویر را از پوشه Obsidian به پوشه static کپی می‌کند
5. از تکرار عملیات جلوگیری می‌کند (اگر قبلاً انجام شده باشد)
"""

import os
import re
import shutil
import json
from pathlib import Path
from datetime import datetime

# ==================== تنظیمات ====================

# مسیر پوشه تصاویر Obsidian
OBSIDIAN_IMAGES_DIR = r"H:\Files\Obsidian\Handouts\VaultData\Attachments"

# مسیر پوشه محتوا
CONTENT_DIR = "content"

# مسیر پوشه static برای تصاویر
STATIC_IMAGES_BASE = "static/images"

# فایل JSON برای ذخیره تصاویر پردازش شده
PROCESSED_IMAGES_FILE = "processed_images.json"

# فایل log
LOG_FILE = "image_conversion.log"

# Pattern برای پیدا کردن لینک‌های Obsidian
# مثال: ![[Pasted image 20260205202337.png]]
OBSIDIAN_IMAGE_PATTERN = r'!\[\[([^\]]+?\.(png|jpg|jpeg|gif|webp|svg|bmp|tiff))\]\]'

# ==================== متغیرهای Global ====================

processed_images = {}  # {image_name: category}
stats = {
    'files_scanned': 0,
    'files_modified': 0,
    'images_found': 0,
    'images_converted': 0,
    'images_copied': 0,
    'images_skipped': 0,
    'errors': 0
}

# ==================== توابع کمکی ====================

def log_message(message, level="INFO"):
    """لاگ پیام‌ها"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}"
    print(log_entry)
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')

def load_processed_images():
    """بارگذاری لیست تصاویر پردازش شده"""
    global processed_images
    
    if os.path.exists(PROCESSED_IMAGES_FILE):
        try:
            with open(PROCESSED_IMAGES_FILE, 'r', encoding='utf-8') as f:
                processed_images = json.load(f)
            log_message(f"تعداد {len(processed_images)} تصویر پردازش شده قبلی بارگذاری شد")
        except Exception as e:
            log_message(f"خطا در بارگذاری فایل JSON: {e}", "ERROR")
            processed_images = {}
    else:
        processed_images = {}
        log_message("فایل JSON پردازش شده وجود ندارد - شروع از ابتدا")

def save_processed_images():
    """ذخیره لیست تصاویر پردازش شده"""
    try:
        with open(PROCESSED_IMAGES_FILE, 'w', encoding='utf-8') as f:
            json.dump(processed_images, f, ensure_ascii=False, indent=2)
        log_message(f"تعداد {len(processed_images)} تصویر در JSON ذخیره شد")
    except Exception as e:
        log_message(f"خطا در ذخیره فایل JSON: {e}", "ERROR")

def is_image_processed(image_name, category):
    """بررسی اینکه آیا تصویر قبلاً پردازش شده است"""
    return image_name in processed_images and processed_images[image_name] == category

def mark_image_as_processed(image_name, category):
    """علامت‌گذاری تصویر به عنوان پردازش شده"""
    processed_images[image_name] = category

def create_category_directory(category):
    """ایجاد دایرکتوری برای دسته‌بندی"""
    category_path = os.path.join(STATIC_IMAGES_BASE, category)
    
    if not os.path.exists(category_path):
        os.makedirs(category_path, exist_ok=True)
        log_message(f"دایرکتوری ایجاد شد: {category_path}")
    
    return category_path

def get_category_from_path(file_path):
    """استخراج نام دسته‌بندی از مسیر فایل"""
    # مثال: content/cyber-security/article.md -> cyber-security
    # با پشتیبانی از فاصله در نام فایل/پوشه
    parts = Path(file_path).parts
    
    if len(parts) >= 2 and parts[0] == 'content':
        return parts[1]
    
    return None

def copy_image_from_obsidian(image_name, category):
    """کپی تصویر از پوشه Obsidian به static"""
    source_path = os.path.join(OBSIDIAN_IMAGES_DIR, image_name)
    dest_dir = os.path.join(STATIC_IMAGES_BASE, category)
    dest_path = os.path.join(dest_dir, image_name)
    
    # بررسی وجود فایل در Obsidian
    if not os.path.exists(source_path):
        log_message(f"❌ تصویر در Obsidian پیدا نشد: {image_name}", "WARNING")
        stats['errors'] += 1
        return False
    
    # بررسی اینکه آیا قبلاً کپی شده
    if os.path.exists(dest_path):
        # بررسی اندازه فایل‌ها برای اطمینان از یکسان بودن
        if os.path.getsize(source_path) == os.path.getsize(dest_path):
            log_message(f"⏩ تصویر از قبل موجود است: {image_name}")
            stats['images_skipped'] += 1
            return True
    
    # ایجاد دایرکتوری مقصد
    create_category_directory(category)
    
    # کپی فایل
    try:
        shutil.copy2(source_path, dest_path)
        log_message(f"✓ کپی شد: {image_name} → {category}/")
        stats['images_copied'] += 1
        return True
    except Exception as e:
        log_message(f"❌ خطا در کپی {image_name}: {e}", "ERROR")
        stats['errors'] += 1
        return False

def convert_markdown_file(file_path):
    """تبدیل لینک‌های تصویر در یک فایل markdown"""
    category = get_category_from_path(file_path)
    
    if not category:
        log_message(f"⚠️  دسته‌بندی برای {file_path} پیدا نشد", "WARNING")
        return
    
    stats['files_scanned'] += 1
    
    # خواندن محتوا
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        log_message(f"❌ خطا در خواندن {file_path}: {e}", "ERROR")
        stats['errors'] += 1
        return
    
    # پیدا کردن تمام تصاویر
    images = re.findall(OBSIDIAN_IMAGE_PATTERN, content, re.IGNORECASE)
    
    if not images:
        return  # فایل بدون تصویر
    
    log_message(f"\n📄 {file_path}")
    log_message(f"   دسته‌بندی: {category}")
    log_message(f"   تعداد تصاویر: {len(images)}")
    
    modified = False
    
    # پردازش هر تصویر
    for image_name, ext in images:
        stats['images_found'] += 1
        
        # بررسی اینکه آیا قبلاً پردازش شده
        if is_image_processed(image_name, category):
            log_message(f"   ⏩ از قبل پردازش شده: {image_name}")
            continue
        
        # مسیر جدید برای Hugo - فرمت استاندارد Markdown
        # static/images/category_name/image.png
        hugo_path = f"static/images/{category}/{image_name}"
        
        # الگوی قدیمی و جدید
        old_pattern = f"![[{image_name}]]"
        new_pattern = f"![{image_name}]({hugo_path})"
        
        # جایگزینی در محتوا
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            modified = True
            
            log_message(f"   ✓ تبدیل شد: {image_name}")
            log_message(f"      از: {old_pattern}")
            log_message(f"      به: {new_pattern}")
            stats['images_converted'] += 1
            
            # ایجاد دایرکتوری برای دسته‌بندی
            create_category_directory(category)
            
            # ذخیره اطلاعات تصویر برای کپی بعدی
            mark_image_as_processed(image_name, category)
    
    # ذخیره فایل اگر تغییر کرده
    if modified:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            log_message(f"   💾 فایل ذخیره شد")
            stats['files_modified'] += 1
        except Exception as e:
            log_message(f"   ❌ خطا در ذخیره {file_path}: {e}", "ERROR")
            stats['errors'] += 1

def scan_content_directory():
    """اسکن تمام فایل‌های markdown در content"""
    log_message("\n" + "="*60)
    log_message("🔍 مرحله 1: اسکن فایل‌های markdown و تبدیل فرمت...")
    log_message("="*60)
    
    if not os.path.exists(CONTENT_DIR):
        log_message(f"❌ پوشه {CONTENT_DIR} وجود ندارد!", "ERROR")
        return
    
    # پیمایش تمام فایل‌های .md
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = os.path.join(root, file)
                convert_markdown_file(file_path)

def copy_all_processed_images():
    """کپی تمام تصاویر پردازش شده از Obsidian"""
    log_message("\n" + "="*60)
    log_message("🔍 مرحله 2: کپی تصاویر از Obsidian...")
    log_message("="*60)
    
    if not processed_images:
        log_message("هیچ تصویری برای کپی وجود ندارد")
        return
    
    log_message(f"تعداد {len(processed_images)} تصویر برای کپی")
    
    # پیمایش تمام تصاویر پردازش شده
    for image_name, category in processed_images.items():
        copy_image_from_obsidian(image_name, category)

def verify_obsidian_directory():
    """بررسی وجود دایرکتوری Obsidian"""
    if not os.path.exists(OBSIDIAN_IMAGES_DIR):
        log_message(f"❌ دایرکتوری Obsidian پیدا نشد: {OBSIDIAN_IMAGES_DIR}", "ERROR")
        log_message("لطفاً مسیر را در اسکریپت بررسی کنید", "ERROR")
        return False
    
    log_message(f"✓ دایرکتوری Obsidian پیدا شد: {OBSIDIAN_IMAGES_DIR}")
    
    # شمارش تصاویر موجود
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.bmp', '.tiff')
    try:
        image_count = len([f for f in os.listdir(OBSIDIAN_IMAGES_DIR) 
                           if f.lower().endswith(image_extensions)])
        log_message(f"✓ تعداد تصاویر موجود در Obsidian: {image_count}")
    except Exception as e:
        log_message(f"⚠️  خطا در خواندن تصاویر Obsidian: {e}", "WARNING")
    
    return True

def create_base_directories():
    """ایجاد دایرکتوری پایه برای تصاویر"""
    if not os.path.exists(STATIC_IMAGES_BASE):
        os.makedirs(STATIC_IMAGES_BASE, exist_ok=True)
        log_message(f"✓ دایرکتوری پایه ایجاد شد: {STATIC_IMAGES_BASE}")

def print_statistics():
    """نمایش آمار نهایی"""
    log_message("\n" + "="*60)
    log_message("📊 آمار نهایی:")
    log_message("="*60)
    log_message(f"📁 فایل‌های اسکن شده: {stats['files_scanned']}")
    log_message(f"📝 فایل‌های ویرایش شده: {stats['files_modified']}")
    log_message(f"🖼️  تصاویر پیدا شده: {stats['images_found']}")
    log_message(f"🔄 تصاویر تبدیل شده: {stats['images_converted']}")
    log_message(f"📦 تصاویر کپی شده: {stats['images_copied']}")
    log_message(f"⏩ تصاویر رد شده (از قبل موجود): {stats['images_skipped']}")
    log_message(f"❌ خطاها: {stats['errors']}")
    log_message(f"📋 تعداد کل تصاویر در JSON: {len(processed_images)}")
    log_message("="*60)
    
    if stats['images_converted'] > 0 or stats['images_copied'] > 0:
        log_message("\n✅ تبدیل موفقیت‌آمیز بود!")
        log_message(f"📋 تصاویر پردازش شده در: {PROCESSED_IMAGES_FILE}")
        log_message(f"📋 لاگ کامل در: {LOG_FILE}")
    else:
        log_message("\nℹ️  هیچ تصویر جدیدی برای تبدیل پیدا نشد")

def create_summary_report():
    """ایجاد گزارش خلاصه"""
    report_file = "image_conversion_report.txt"
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("گزارش تبدیل تصاویر Obsidian به Hugo\n")
        f.write("="*60 + "\n")
        f.write(f"تاریخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*60 + "\n\n")
        
        f.write("آمار:\n")
        f.write(f"- فایل‌های اسکن شده: {stats['files_scanned']}\n")
        f.write(f"- فایل‌های ویرایش شده: {stats['files_modified']}\n")
        f.write(f"- تصاویر پیدا شده: {stats['images_found']}\n")
        f.write(f"- تصاویر تبدیل شده: {stats['images_converted']}\n")
        f.write(f"- تصاویر کپی شده: {stats['images_copied']}\n")
        f.write(f"- تصاویر رد شده: {stats['images_skipped']}\n")
        f.write(f"- خطاها: {stats['errors']}\n")
        f.write(f"- تعداد کل تصاویر در JSON: {len(processed_images)}\n\n")
        
        f.write("تصاویر پردازش شده بر اساس دسته‌بندی:\n")
        f.write("-"*60 + "\n")
        
        # گروه‌بندی بر اساس دسته‌بندی
        categories = {}
        for img, cat in processed_images.items():
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(img)
        
        for cat, imgs in sorted(categories.items()):
            f.write(f"\n{cat.upper()} ({len(imgs)} تصویر):\n")
            for img in sorted(imgs):
                f.write(f"  - {img}\n")
        
        # اطلاعات مسیر تصاویر
        f.write("\n" + "="*60 + "\n")
        f.write("مسیرها:\n")
        f.write(f"- Obsidian: {OBSIDIAN_IMAGES_DIR}\n")
        f.write(f"- Static: {STATIC_IMAGES_BASE}\n")
        f.write(f"- JSON: {PROCESSED_IMAGES_FILE}\n")
        f.write(f"- Log: {LOG_FILE}\n")
    
    log_message(f"\n📄 گزارش خلاصه ایجاد شد: {report_file}")

def verify_paths():
    """بررسی و نمایش اطلاعات مسیرها"""
    log_message("\n" + "="*60)
    log_message("📂 بررسی مسیرها:")
    log_message("="*60)
    
    # مسیر فعلی
    current_dir = os.getcwd()
    log_message(f"📍 دایرکتوری فعلی: {current_dir}")
    
    # بررسی content
    content_path = os.path.join(current_dir, CONTENT_DIR)
    if os.path.exists(content_path):
        log_message(f"✓ دایرکتوری content: {content_path}")
    else:
        log_message(f"❌ دایرکتوری content پیدا نشد: {content_path}", "ERROR")
    
    # بررسی static
    static_path = os.path.join(current_dir, STATIC_IMAGES_BASE)
    log_message(f"📁 دایرکتوری static: {static_path}")
    
    # بررسی Obsidian
    if os.path.exists(OBSIDIAN_IMAGES_DIR):
        log_message(f"✓ دایرکتوری Obsidian: {OBSIDIAN_IMAGES_DIR}")
    else:
        log_message(f"❌ دایرکتوری Obsidian پیدا نشد: {OBSIDIAN_IMAGES_DIR}", "ERROR")
    
    log_message("="*60)

# ==================== تابع اصلی ====================

def main():
    """تابع اصلی"""
    print("\n" + "="*60)
    print("🖼️  ابزار تبدیل تصاویر Obsidian به Hugo")
    print("="*60)
    print(f"نویسنده: Davood Yahya")
    print(f"تاریخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")
    
    # شروع لاگ
    log_message("="*60)
    log_message("شروع فرآیند تبدیل تصاویر")
    log_message("="*60)
    
    # بررسی مسیرها
    verify_paths()
    
    # بررسی دایرکتوری Obsidian
    if not verify_obsidian_directory():
        log_message("\n❌ فرآیند متوقف شد به دلیل عدم وجود دایرکتوری Obsidian", "ERROR")
        return
    
    # ایجاد دایرکتوری‌های پایه
    create_base_directories()
    
    # بارگذاری تصاویر پردازش شده قبلی
    load_processed_images()
    
    # مرحله 1: اسکن و تبدیل فایل‌های markdown
    scan_content_directory()
    
    # ذخیره تصاویر پردازش شده بعد از تبدیل
    save_processed_images()
    
    # مرحله 2: کپی تصاویر از Obsidian
    copy_all_processed_images()
    
    # نمایش آمار
    print_statistics()
    
    # ایجاد گزارش خلاصه
    if stats['images_converted'] > 0 or len(processed_images) > 0:
        create_summary_report()
    
    log_message("\n✅ فرآیند به پایان رسید")
    log_message("="*60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  فرآیند توسط کاربر متوقف شد")
        log_message("فرآیند توسط کاربر متوقف شد", "WARNING")
    except Exception as e:
        print(f"\n\n❌ خطای غیرمنتظره: {e}")
        log_message(f"خطای غیرمنتظره: {e}", "ERROR")
        import traceback
        log_message(traceback.format_exc(), "ERROR")
