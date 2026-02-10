+++
title = "مبانی و مفاهیم IP و MAC"
slug = "ip-mac-address-basic-and-concepts"
date = "2024-03-25T15:41:10+03:30"
lastmod = "2026-02-09T15:41:10+03:30"
draft = false

# Taxonomies
categories = ["Network", "Network+"]
tags = ["Network", "IP" ,"MAC", "Network+"]
series = ["Network", "Network+"]

# Badges and Filters
readingTime = 8
difficulty = "medium" # beginner | medium | intermediate | advanced
lab_required = true 
post_type_fa = "آموزشی" # "آموزشی" | "مقاله" | "اسکریپت" | "خبر" | "دستور العمل" | "معرفی" | "ابزار"

# Options
toc = true
math = false
type = "posts"
# layout = "single"

# SEO
description = "1. Binary 1. 01 2. Octa 1. 0 to 8 3. Decimal 1. 0 to 10 4. Hexadecimal 1. 0 to F 1. 0123456789 & ABCDEF 5. Convert Binary to Decimal Number 1. Whats..."
keywords = ["IP-Mac Address Basic and Concepts", "network", "ip-mac-address-basic-and-concepts"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/network/ip-mac-address-basic-and-concepts/"

featured_image = "/images/network/IP-MacAddressBasicandConcepts-1.png"
images = ["/images/network/IP-MacAddressBasicandConcepts-1.png"]

[params.opengraph]
  title = "IP-Mac Address Basic and Concepts"
  description = "1. Binary 1. 01 2. Octa 1. 0 to 8 3. Decimal 1. 0 to 10 4. Hexadecimal 1. 0 to F 1. 0123456789 & ABCDEF 5. Convert Binary to Decimal Number 1. Whats..."
  image = "/images/network/IP-MacAddressBasicandConcepts-1.png"
  url = "https://davoodya.ir/network/ip-mac-address-basic-and-concepts/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "IP-Mac Address Basic and Concepts"
  description = "1. Binary 1. 01 2. Octa 1. 0 to 8 3. Decimal 1. 0 to 10 4. Hexadecimal 1. 0 to F 1. 0123456789 & ABCDEF 5. Convert Binary to Decimal Number 1. Whats..."
  image = "/images/network/IP-MacAddressBasicandConcepts-1.png"

+++
------------
### Numbers in Computers
1. Binary
	1. 01
2. Octa
	1. 0 to 8
3. Decimal
	1. 0 to 10
4. Hexadecimal
	1. 0 to F
		1. 0123456789 & ABCDEF
5. Convert Binary to Decimal Number
### IP - Basic & Concepts
#### Definitions
1. **Whats IP? IP Usages**
	1. منظور از **IP** مخفف عبارت Internet Protocol یا به فارسی پروتکل اینترنت است. آدرس **آیپی** مجموعه‌ ای از اعداد است که به‌ عنوان شناسهٔ منحصر‌ به‌ فرد هر دستگاه، اجازه میدهند موبایل، کامپیوتر و… در شبکه از طریق اینترنت یا یک شبکه محلی به یکدیگر متصل شوند و داده‌‌ها را انتقال دهند. 
		1. ![IP-Mac Address Basic and Concepts-1](/images/network/IP-MacAddressBasicandConcepts-1.png)
	2. آیپی ها در دو ورژن 4 و ورژن 6 عرضه میشوند. وظیفه آیپی آدرس دهی و مسیریابی در شبکه میباشند.
	3. *آیپی ورژن 4 که ما بیشتر هم از آن استفاده میکنیم نوع آن `decimal` است و کلا 32 بیت است و دارای 4 بخش 8 بیتی است:*
		1. IP Parts => `0-255, 0-255, 0-255, 0-255`
#### Parts of IP
1. **IP Have 2 Part(NET IP & Broadcast IP):**
	1. Net IP: Describe network IP
		1. قسمتی از آیپی که مشخص کننده شبکه ایست که آیپی به آن اشاره میکند.
	2. Host IP: Describe Host IP
		1. قسمتی از آیپی که مشخص کننده ماشین است که در شبکه قرار دارد.
	3. Image:
		1. ![IP-Mac Address Basic and Concepts-2](/images/network/IP-MacAddressBasicandConcepts-2.png)
	4. *Note 1:* If you want machines in a same network:
		1. برای قرار دادن ماشین ها در یک شبکه:
		2. اول NET IP تمام ماشین های شبکه باید یکسان باشند.
		3. همچنین HOST IP آیپی هر ماشین باید متفاوت باشد.
	5. *Note 2:* Use Router to Connect Some Network(NET IP) together:
		1. **نکته:** از Router ها برای اتصال چندین Net IP(یا چندین شبکه) به یکدیگر استفاده میشود.
#### Subnetting
##### Basic Subnetting
1. **Subnet & IP:**
	1. ساب نت عددی است که در هنگام تعریف آیپی نوشته میشود و مشخص کننده Net ID و Host ID است. عدد 0 مشخص کننده Host ID میباشد و عدد 255 و سایرین مشخص کننده Net ID میباشند.
	2. *Subnet Pictures:*
		1. ![IP-Mac Address Basic and Concepts-3](/images/network/IP-MacAddressBasicandConcepts-3.png)
		2. ![IP-Mac Address Basic and Concepts-4](/images/network/IP-MacAddressBasicandConcepts-4.png)
##### Deep to Subnetting
1. Limit Subnet to user count  == Increase Security
2. Subnets =>
	1. Subnet /24 ==> `x.x.x.0-254/24`
	2. Subnet /25 ==> `x.x.x.0-128/25`
	3. Subnet /26 ==> `x.x.x.0-64/26`
	4. Subnet /27 ==> `x.x.x.0-32/27`
	5. Subnet /25 ==> `x.x.x.0-16/28`
3. Example of IP/Subnetting for A Corporations in Three Part: 
	1. `One Range IP for 3 network`
#### Special IPs
چندین آیپی خاص و ویژه هستند که از پیش برای یکسری از کارها رزرو شده اند. دو عدد از این ها Net IP و Broadcast IP میباشد. برای تعریف آیپی های خاص باید یک رنج آیپی داشته باشیم. برای اینکار از آیپی `192.168.10.100` استفاده میکنیم.
1. **NET IP & Broadcast IP(In the specific Network):**
	1. *Net IP:* `192.168.10.0`
		1. اولین آیپی یک شبکه میباشد که مشخص کننده رنج کلی شبکه است.
		2.  `192.168.10.0`
	2. *Broadcast IP:*  `192.168.10.255`
		1. *توضیح فرآیند Broadcast:* به فرآیند ارسال یک بسته برای تمام هاست ها(ماشین هایی) که درون یک شبکه قرار دارند Broadcasting گفته میشود.
		2. حال Broadcast IP آخرین آیپی یک شبکه است که برای فرآیند Broadcasting از آن استفاده میشود.
		3.  `192.168.10.255`
	3. *Note:* We cant use Net IP & Broadcast IP for Packet Src/Dst Addresses and Machines in the Network
		1. آیپی های مبدا و مقصد یک بسته، نباید از این دو آیپی Net IP و Broadcast IP باشند. 
		2. همچنین ماشین های شبکه نیز نمیتوانند از این دو آیپی استفاده کنند.
2. Loopback => `127.0.0.1/8`
3. **Global Broadcast => `255.255.255.255`**
	1. تفاوت این Broadcast IP با Broadcast IP یک رنج شبکه در این است که بسته ای که به این آیپی ارسال میشود برای تمام شبکه های موجود ارسال میشود. 
	2. بر خلاف مورد قبلی که بسته برای تمام هاست های یک شبکه ارسال میشد.
4. APIPA => `169.254.0.1-169.254.255.254`
5. Default Route => `0.0.0.0/0`
6. Multicast=>`224.0.0.0/4`
#### Set IP on Windows
1. **Set IP:**
	0. برای تنظیم آیپی بر روی اینترفیس های شبکه(کارت های شبکه) باید از پنجره Network and Internet Sharing Center شویم. برای وارد شدن به این پنجره روش های متفاوتی داریم:
	1. `ncpa.cpl` 
	2. `Settings => Network & Internet Sharing Center => Change Adapter Setings => Network Interfaces`
#### IP Classes
1. **IP Classes:**
	1. ![IP-Mac Address Basic and Concepts-5](/images/network/IP-MacAddressBasicandConcepts-5.png)
	2. ![IP-Mac Address Basic and Concepts-6](/images/network/IP-MacAddressBasicandConcepts-6.png)
	3. ![IP-Mac Address Basic and Concepts-7](/images/network/IP-MacAddressBasicandConcepts-7.png)
	4. ![IP-Mac Address Basic and Concepts-8](/images/network/IP-MacAddressBasicandConcepts-8.png)
#### IP Versions
1. **IP Versions:**
	1. در کل دو ورژن آیپی یعنی IPv4 و IPv6 داریم.
	2. *IPv4 Structure:*
		1. `xxx.xxx.xxx.xxx` 
		2. که هر پارت xxx میتواند بین 0 تا 255 باشد. 
		3. در کل آیپی ورژن 4 ترکیبی از اعداد Decimal میباشد.
	3. *IPv6 Structure:*
		1. `xxxx.xxxx.xxxx.xxxx.xxxx.xxxx`
		2. هر پارت xxxx میتواند بین 0 تا F باشد.
		3. یعنی آیپی ورژن 6 از نوع Hexadecimal میباشد.
	4. *Image:*
		1. ![IP-Mac Address Basic and Concepts-9](/images/network/IP-MacAddressBasicandConcepts-9.png)
2. **IPv6 vs IPv4:**
	1. IPv6 VS IPv4 Image
		1. ![IP-Mac Address Basic and Concepts-10](/images/network/IP-MacAddressBasicandConcepts-10.png)
3. **Loopbacks(Localhost) in IPv4 & IPv6**
### MAC Address
#### Definitions
1. **MAC Address:**
	1. مک آدرس (**MAC address**) یا آدرس‌‌ کنترل دسترسی رسانه (Media Access Control) شناسه‌ ای منحصر به‌ فرد محسوب می‌شود که سازنده به یک کارت شبکه (NIC) اختصاص داده است.
	2. ساختار مک آدرس `xx.xx.xx.xx.xx.xx` میباشد و در کل `48bit` میباشد.
	3. هر بخش `xx` شامل اعداد Hexadecimal میباشد:
		![IP-Mac Address Basic and Concepts-11](/images/network/IP-MacAddressBasicandConcepts-11.png)
		![IP-Mac Address Basic and Concepts-12](/images/network/IP-MacAddressBasicandConcepts-12.png)
	4. مک آدرس ها توسط سازنده دیوایس سخت افزاری به دیوایس تعلق میگیرد البته به روش هایی قابل تغییر است که جلوتر توضیح میدهیم.
#### MAC Table & See MAC
1. Mac Addr Save to Mac tables. Switches Work with Mac Tables
	1. ![IP-Mac Address Basic and Concepts-13](/images/network/IP-MacAddressBasicandConcepts-13.png)
2. See Mac Addr on windows => `getmac` & `ipconfig -all`
#### Changing MAC Address
2. مک آدرس را با روش های امنیتی و برای انجام کارهای امنیتی میتوانیم با استفاده از ابزارهایی مانند `macchanger, ifconfig, ip link, ...` تغییر دهیم.
3. مثلا برای حملاتی که از MAC Filtering وایرلس عبور میکند و آنرا دور میزند از این ابزارها استفاده میکنیم.
#### Attack Through MAC Address
3. Mac Flooding
4. Mac Spoofing

### !