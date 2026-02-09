+++
title = "1-Install Burpsuite"
tags = ["Pentest", "Web_Pentest", "Bug_Bounty", "Burpsuite", "Pentest_Tool"]
categories = ["cyber-security", "pentest", "web_pentest"]
series = ["bug bounty"]
# Category = "Pentest, Web_Pentest"
draft = false
readingTime = 12
difficulty = "intermediate"
toc = true
math = false
lab_required = true
course = "Burpsuite begginer to advance"
# featured_image = "/images/tools/1-InstallBurpsuite-1.png"
images = ["/images/tools/1-InstallBurpsuite-1.png"]
image = "/images/tools/1-InstallBurpsuite-1.png"

slug = "installing-burp-suite"
+++

-------
### Install Cracked Burpsuite
Requirements => JDK v9.04 
نسخه از ابزار ممکن است با JDK 21 کار نکند همچنین با JDK زیر 9 هم نمیتواند کار کند.
![1-Install Burpsuite-1](/images/tools/1-InstallBurpsuite-1.png)
برای نصب کافیست از وبسایت soft98 ابزار Burpsuite را دانلود کنیم و سپس آنرا از loader موجود نصب کنیم.
### Work with Burpsuite
![1-Install Burpsuite-2](/images/tools/1-InstallBurpsuite-2.png)
وقتیکه که Burpsuite را باز میکنیم 2 Task بصورت پیشفرض در حال اجرا هستند که تیک آنها نیز خورده است. اگر Inspector در Proxy روشن باشد این Task ها بصورت اتوماتیک بر روی هر وبسایت که باز  میشود انجام میشود.
### Dashboard Module
##### 1. Live Passive crawl from proxy (all traffic)
این Task پیشفرض فرآیند خزش و Crawl را بصورت پیش فرض بر روی هر وبسایت که باز شود انجام میدهد.
##### 2. Live audit from proxy (all traffic)
این Task پیشفرض بصورت اتوماتیک به یافتن آسیب پذیری های وبسایتی که باز میشود میپردازد. در واقع آسیب پذیری ها را میابد و در دسته بندی های Low, Medium, High, Informational دسته بندی میکند.
### Proxy Module
#### Basic
در این ماژول میتوانیم تمام درخواست های HTTP که ارسال و دریافت میشوند را مشاهده، و سپس Action مورد نظر را بر روی آن اعمال کنیم. ابزار Burpsuite ار میتوانیم بصورت Proxy بر روی مرورگر خودمان Set کنیم و یا میتوانیم از مرورگر داخلی Burpsuite برای ارسال و دریافت درخواست ها استفاده کنیم.
![1-Install Burpsuite-3](/images/tools/1-InstallBurpsuite-3.png)
پیشنهاد میشود از Layout جفتی بصورت (مرورگر در راست و ابزار در چپ) از Burpsuite استفاده کنیم.
![1-Install Burpsuite-4](/images/tools/1-InstallBurpsuite-4.png)
داده هایی که در هر درخواست HTTP وجود دارند را در ابزار در این ماژول میتوانیم مشاهده کنیم.
![1-Install Burpsuite-5](/images/tools/1-InstallBurpsuite-5.png)
حال پس از باز کردن وبسایت در ماژول Dashboard میتوانیم آسیب پذیری هایی که Burpsuite پیدا کرده را نیز مشاهده کنیم. در همین مثال میتوانیم مشاهده کنیم که 16 Low Security پیدا شده و 25 Informational پیدا شده است.
![1-Install Burpsuite-6](/images/tools/1-InstallBurpsuite-6.png)

#### Change HTTP Data
در مثال زیر یک درخواست به sabzlearn زده ایم و دایرکتوری `/produet/flex-box/` را درخواست مشاده کرده ایم. حال میتوانیم با عوض کردن دستی مسیر این دایرکتوری درخواست را تغییر دهیم و به دایرکتوری جدید منتقل شویم:
![1-Install Burpsuite-7](/images/tools/1-InstallBurpsuite-7.png)
![1-Install Burpsuite-8](/images/tools/1-InstallBurpsuite-8.png)
حال با Forward کردن درخواست تغییر یافته مشاهده میکنیم که به دایرکتوری جدید نقل مکان کرده ایم، با اینکه URL همان آدرس قبلی است اما دایرکتوری جدید را در مرورگر مشاهده میکنیم.
![1-Install Burpsuite-9](/images/tools/1-InstallBurpsuite-9.png)

### Use Burpsuite on Firefox
پیشنهاد میشود که از مرورگر Chrome یا ... به عنوان مرورگر پیشفرض استفاده کنید و مرورگر Firefox را برای کار با Burpsuite اختصاص دهید. همچنین پیشنهاد میشود بر روی ip لوکال هاست (127.0.0.1) و پورت به غیر از 8080(except 8080) کار کنید.
##### Set Burpsuite Proxy 
ابتدا باید آدرس پراکسی که Burpsuite بر روی آن کار میکند را تنظیم کنیم. برای اینکار به ماژول Proxy رفته و سپس به تب Option میرویم. در این تب در بخش Proxy Listeners میتوانیم آدرس Proxy که Burp با آن کار میکند را تنظیم کنیم.
![1-Install Burpsuite-10](/images/tools/1-InstallBurpsuite-10.png)
با کلیک بر روی Add میتوانیم آدرس پراکسی جدید اضافه کنیم و با کلیک بر روی Edit میتوانیم این آدرس پراکسی را ویرایش کنیم. همچنین با کلیک بر روی Regenerate CA Certificate میتوانیم یک گواهینامه جدید بگیریم که به مرورگر معرفی کنیم که Burp ارور Privacy در مرورگر ندهد.
##### Add new proxy listener
![1-Install Burpsuite-11](/images/tools/1-InstallBurpsuite-11.png)


##### Config Foxyproxy for use Burpsuite
![1-Install Burpsuite-12](/images/tools/1-InstallBurpsuite-12.png)
