+++
# Basic
title = "Virtualization Concepts"
slug = "virtualization-concepts"
date = "2024-08-28T09:26:00+03:30"
lastmod = "2026-02-10T09:26:00+03:30"
draft = false

# Taxonomies
categories = ["network"]
tags = ["network"]
series = ["network"]

# Badges and Filters
readingTime = 9 # integer number
difficulty = "medium" # beginner | medium | intermediate | advanced
lab_required = true
post_type_fa = "مقاله" 
# post_type_fa = "آموزشی" | "مقاله" | "اسکریپت" | "خبر" | "دستور العمل" | "معرفی" | "ابزار"

# Images
featured_image = "/images/network/VirtualizationConcepts-1.png"
images = ["/images/network/VirtualizationConcepts-1.png"]

# Options
toc = true
math = false
type = "posts"
# layout = "single"

# SEO
description = "قبل از ارئه Virtualization مجبور بودیم تمام نرم افزار های مورد نیازمان را بر روی سیستم عامل اصلی نصب کنیم و در واقع تمام برنامه های نیازمند سیستم..."
keywords = ["Virtualization Concepts", "network", "virtualization-concepts"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/network/virtualization-concepts/"

# Open Graph and Twitter
[params.opengraph]
  title = "Virtualization Concepts"
  description = "قبل از ارئه Virtualization مجبور بودیم تمام نرم افزار های مورد نیازمان را بر روی سیستم عامل اصلی نصب کنیم و در واقع تمام برنامه های نیازمند سیستم..."
  image = "/images/network/VirtualizationConcepts-1.png"
  url = "https://davoodya.ir/network/virtualization-concepts/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Virtualization Concepts"
  description = "قبل از ارئه Virtualization مجبور بودیم تمام نرم افزار های مورد نیازمان را بر روی سیستم عامل اصلی نصب کنیم و در واقع تمام برنامه های نیازمند سیستم..."
  image = "/images/network/VirtualizationConcepts-1.png"

+++
------
### Virtualization
#### Basic & Concepts
قبل از ارئه Virtualization مجبور بودیم تمام نرم افزار های مورد نیازمان را بر روی سیستم عامل اصلی نصب کنیم و در واقع تمام برنامه های نیازمند سیستم عامل اصلی بودند و در صورت Down شدن OS نمیتوانستیم از برنامه ها استفاده کنیم.
با عرضه قابلیت Virtualization میتوانیم بر روی سیستم عامل اصلی چندین سیستم عامل با سخت افزار های مشخص و مجازی داشته باشیم و سپس نرم افزار ها را در این سیستم عامل های مجازی ‍نصب کنیم تا در صورتیکه یکی از این سیستم عامل های مجازی از کار افتاد، کل سیستم دچار مشکل نشود و بتواند به سرویس دهی خود ادامه دهد.
میتوان گفت ماشین مجازی میتواند سخت افزار اصلی ماشین را به بصورت اشتراکی در بیاورد و سپس آنرا برای چندین سیستم عامل به اشتراک بگذارد.
	![Virtualization Concepts-1](/images/network/VirtualizationConcepts-1.png)
#### Hypervisor & Virtual Machines
این سیستم عامل های مجازی را به اصطلاح ماشین مجازی یا Virtual Machine گفته میشود و به Solution هایی که میتوانیم VM ها را در آنها نصب و اجرا کنیم Virtualization Software گفته میشود که از معروف ترین آنها میتوان به VMWare(ESXI), Microsoft Hyper-V, Critix(Xen Server), Oracle(Virtual Box) اشاره کرد.
هر ماشین مجازی میتواند V-Ram, V-CPU, V-, Disk, V-NIC , ... خود را داشته باشد:
مثلا کارت شبکه مجازی VNIC هر ماشین مجازی به یک سوئیچ مجازی که توسط Hypervisor ساخته شده است متصل میشود و سپس آن سوئیچ مجازی به کارت شبکه اصلی سرو متصل میشود.
#### Virtual Center(V-Center)
قابلیتی که توسط شرکت هایی مانند VMWare عرضه میشوند و برای مدیریت چندین ESXI در مکان های مختلف استفاده میشود.
مثلا میتوانیم دو سرور در دو مکان مختلف داشته باشیم و سپس بر روی هر سرور یک ESXI نصب داشته باشیم. حال میتوانیم با استفاده از یک سرور که بر روی آن V-Center نصب است به این دو ESXI متصل شویم و این دو ESXI و چند VM که بر روی آن نصب هستند را از یک سرور کنترل کنیم.
	![Virtualization Concepts-2](/images/network/VirtualizationConcepts-2.png)
امروزه بدلیل گسترش شعب شرکت ها و افزایش کامندان آنها در بسیاری از شرکت ها و ارگان ها از سرویس  V-Center استفاده میشود تا VM هایی که بر روی سرور های متفاوت در مکان های متفاوت نصب است را کنترل و مدیریت کنند.
در واقع ارسال و دریافت داده از طریق سرور ها انجام میشود اما کنترل سرور ها و مجازی سازی آنها از V-Center انجام میشود.
#### Virtualization Types
1. Server Virtualization
	1. در این مدل مجازی سازی بر روی سرور های ما انجام میشود و در واقع ESXI بر روی سرور های ما نصب میشود. همچنین میتوانیم در این مدل لایه Control Plane را به V-Center انتقال دهیم.
		1. ![Virtualization Concepts-3](/images/network/VirtualizationConcepts-3.png)
	2. برای افزایش امنیت این مدل باید از SDN ها دکه در قدم 3  توضیح میدهیم استفاده کنیم.
2. Desktop Virtualization (VDI)
	1. در این مدل مجازی سازی در حد Desktop صورت میگیرد و چندین دسکتاپ مجازی ساخته میشود.
3. Network Virtualization(NSX)(SDN{Software Design Network})
	1. در این مدل سرور به سه بخش تقسیم میشود. در قسمت پایین اول ESXI راه اندازی میشود. کارت شبکه های اصلی سرور در این لایه قرار میگرند و برای ارتباط سرور با شبکه بیرونی از کارت شبکه های اصلی سرور استفاده میشود.
	2. در لایه دوم نیز NFV(Network Foundation Virtualization) راه اندازی میشود که شامل سوئیچ ها، روتر ها، فایروال ها و سایر دیوایس های مجازی شبکه میباشد. لایه NFV در واقع لایه Data Plan است و از آن برای ارسال داده ها در سرور استفاده میشود. دیوایس های این لایه میتوانند داده ها را برای لایه ESXI بفرستند تا سپس لایه ESXI بتواند با کارت شبکه های اصلی سرور داده ها را به شبکه خارجی بفرستد.
	3. در قسمت سوم SDN Control قرار میگرد که وظیفه کنترل دیوایس های مجازی شبکه در لایه دوم NFV را بر عهده دارند. حال میتوانیم بوسیله اتصال به API به لایه SDN بصورت Remote این لایه و در کل سرور را کنترل کنیم.
	4. به لایه دوم NFV که دیوایس های مجازی شبکه قرار دارد Network Virtualization گفته میشود و به لایه اول که ESXI نصب میشود Server Virtualization گفته میشود. 
		1. ![Virtualization Concepts-4](/images/network/VirtualizationConcepts-4.png)
	5. حال اگر بخواهیم Desktop Virtualization را نیز در این مثال توضیح دهیم، در واقع یک لایه جدید بر روی لایه Control SDN است که Virtual Machine های ما در آن نصب میشوند.
		1. ![Virtualization Concepts-5](/images/network/VirtualizationConcepts-5.png)
	6. 
4. Cloud 
	1. Public
	2. Private
5. Example
	1. فرض کنید شبکه ای با توپولوژی زیر در اختیار ماست:
		1. ![Virtualization Concepts-6](/images/network/VirtualizationConcepts-6.png)
	2. در این توپولوژی اگر بخواهیم از Virtualization استفاده کنیم، ابتدا باید در Main Office که Sensor Office هم نامیده میشود، ESXI و سپس SDN را راه اندازی کنیم و در این SDN نیز یک VPN Server برای متصل شدن کلاینت ها راه اندازی میکنیم.
	3. سپس در شعب دیگر VDI را راه اندازی کنیم و با استفاده از کانکشن VPN کلاینت را به شبکه SDN متصل کنیم تا کلاینت ما بتواند از شبکه SDN استفاده کنند.
	4. در اینجا فقط کافیست هزینه اصلی در Sensor Office صورت بگیرد و در سایر شعب نیازی به هزینه برای تجهیزات شبکه و سرور ها نداریم.
	5. همچنین بدلیل اینکه سرور حساس ما در یک محل قرار دارد، Maintenance و Security آن بسیار بالا میرود.
#### Virtualization Hardening
##### Host & Guest Hardening
1. Update & Patch Virtualization Software
2. Configure Security Settings on `HOST`
3. Update & Patch Guest OS and Softwares on Guest OS on Host.
4. Image
	1. ![Virtualization Concepts-7](/images/network/VirtualizationConcepts-7.png)
##### Virtual Network Security
1. Disable Unnecessary Network Sharing Between Host & Guest VM
2. Disable Unnecessary Connection Bridging between Host & Guest VM
3. Using V-Lan in Vm Network
4. Image
	1. ![Virtualization Concepts-8](/images/network/VirtualizationConcepts-8.png)
##### Disable Unnecessary Hardware
1. Disable Optical Drive
2. Disable USB Port on Guest VMs
3. in Guest VMs Virtual Bios Boot Priority Select Hard Drive as First Boot Option.
4. Monitor & Protected The VM
	1. Limit VM Resources
		1. مثلا در ماشین مجازی نیازی به Printer یا Floppy نداریم بنابراین میتوانیم این سخت افزار ها را پاک کنیم.
		2. همچنین باید از CPU, RAM به اندازه ای که ماشین مجازی ما نیاز دارد، استفاده کنیم و نباید مقادیر بیشتر و مقادیر کمتر استفاده کنیم.

#### a Strategy for Initialize VM
در این استراتژی کار هایمان را به چندین OS تقسیم میکنیم تا بتوانیم با مینیاتوریزه کردن سیستم عامل ها مدیریت و انعطاف بیشتری در استفاده از ماشین مان داشته باشیم.
در این استراتژی ماشین اصلی فقط نیاز به یک Virtual machine و همچنین برنامه های اصلی مانند مرورگر، IDM, ... میباشد و سایر امور و برنامه ها را به سیستم عامل های زیر منتقل میکنیم:
1. Install Clean Windows - Special Purpose 
	1. در این سیستم عامل هیچ نرم افزاری نصب نمیکنیم و فقط از یک مرورگر، آنتی ویروس در آن استفاده میکنیم.
	2. این ماشین مجازی را مختص امور حساس مانند امور مالی میگذاریم.
2. Install a Ubuntu Linux OS
	1. یک سیستم عامل لینوکسی همیشه کارایی دارد. بنابرای یک سیستم عامل لینوکسی اصلی برای کارهایمان نصب میکنیم.
3. Install a Kali Linux
	1. همچنین یک سیستم عامل Kali مختص امور هک و امنیت نصب میکنیم.
4. Install a Windows
	1. یک ویندوز دیگر هم نصب میکنیم و از آن برای نصب و استفاده برنامه های ویندوزی مان استفاده میکنیم.
5. Install Windows Sandbox - First Testing
	1. برای تست اولیه برنامه های که میخواهیم آنها را بر روی سیستم عامل نصب کنیم میتوانیم از یک Sandbox Windows استفاده کنیم.
	2. استفاده از Sandbox در مواقعی که میخواهیم یک Malware را نیز بررسی کنیم بسیار کاربرد دارد.
6. Install Some RouterOS
	1. برای راه اندازی NDS هم چندین روتر بر روی ماشین مجازی نصب میکنیم تا بتوانیم در شبکه های VM از آنها استفاده کنیم.
7.  Install Network Laboratory

#### VMWare Networking
1. VM-Ware Networking
	1. NAT Network
	2. Bridge Network
	3. Lan Segments
	4. Host Only
	5. Custom
		1. vmnet0 to vmnet20
	6. VM
2. Networking Windows on VM
	7. Connect two windows together using Lan segments
		1. Set Computer Name & WORKGROUP
		2. Set IP
		3. Create User for sharing
	8. Networking PC1-VM to main PC and share folder from PC to PC1-VM using Host only network or custom bridged
#### Vagrant & Docker
##### Vagrant
سرویس Vagrant یک ابزار مدیریت ماشین‌های مجازی است که به شما امکان می‌دهد تا به‌سرعت محیط‌های توسعه‌ای قابل حمل و تکرارپذیر را ایجاد کنید. Vagrant بر روی پلتفرم‌های مختلفی مانند VirtualBox، VMware و دیگر ماشین‌های مجازی کار می‌کند. با استفاده از Vagrant، می‌توانید فایل‌های تنظیمات را به‌صورت کد (Vagrantfile) تعریف کنید، که به شما اجازه می‌دهد تا محیط‌های توسعه‌ای یکسان را روی سیستم‌های مختلف به‌راحتی ایجاد و بازتولید کنید. این ویژگی برای تیم‌های توسعه‌ای که نیاز به همگام‌سازی محیط‌های کاری دارند بسیار مفید است
##### Docker
داکر Docker یک پلتفرم برای ساخت، حمل و اجرای نرم‌افزارها در کانتینرها است. کانتینرها واحدهای سبک‌وزن و جداشده‌ای هستند که شامل همه چیزهایی هستند که یک نرم‌افزار برای اجرا نیاز دارد (از جمله کتابخانه‌ها و وابستگی‌ها). برخلاف Vagrant که ماشین‌های مجازی را مدیریت می‌کند، Docker بر روی کانتینرهای نرم‌افزاری متمرکز است که نسبت به ماشین‌های مجازی کم‌حجم‌تر و کارآمدتر هستند. Docker به شما این امکان را می‌دهد که نرم‌افزارها را به همراه محیط اجرایی‌شان به‌سادگی بسته‌بندی و روی سیستم‌های مختلف بدون نگرانی از تفاوت‌ های زیرساختی اجرا کنید.

## !