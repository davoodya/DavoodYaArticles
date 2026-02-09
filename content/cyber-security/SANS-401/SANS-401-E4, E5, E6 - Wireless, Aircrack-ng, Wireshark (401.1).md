+++
title = "SANS-401-Wireless, Aircrack-ng, Wireshark (401.1)"
slug = "sans-401-wireless-aircrack-ng-wireshark-4011"
date = "2026-02-09T13:50:09+03:30"
lastmod = "2026-02-09T13:50:09+03:30"
draft = false

categories = ["cyber-security", "SANS-401"]
tags = ["cyber-security", "SANS-401", "CyberSecurity", "Pentest"]
series = ["cyber-security", "SANS-401"]

description = "شبکه های وایرلسی که امروزه بسیار هم مورد استفاده واقع میشوند در استاندارد های مختلف عرضه شده اند: 1. 802.11g 1. استاندارد قدیمی که فقط بر روی باند..."
keywords = ["SANS-401-Wireless, Aircrack-ng, Wireshark (401.1)", "cyber-security", "SANS-401", "CyberSecurity", "Pentest", "sans-401-e4-e5-e6-wireless-aircrack-ng-wireshark-4011"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/cyber-security/SANS-401/sans-401-wireless-aircrack-ng-wireshark-4011/"

featured_image = "/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-1.png"
images = ["/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-1.png"]

[params.opengraph]
  title = "SANS-401-Wireless, Aircrack-ng, Wireshark (401.1)"
  description = "شبکه های وایرلسی که امروزه بسیار هم مورد استفاده واقع میشوند در استاندارد های مختلف عرضه شده اند: 1. 802.11g 1. استاندارد قدیمی که فقط بر روی باند..."
  image = "/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-1.png"
  url = "https://davoodya.ir/cyber-security/SANS-401/sans-401-wireless-aircrack-ng-wireshark-4011/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "SANS-401-Wireless, Aircrack-ng, Wireshark (401.1)"
  description = "شبکه های وایرلسی که امروزه بسیار هم مورد استفاده واقع میشوند در استاندارد های مختلف عرضه شده اند: 1. 802.11g 1. استاندارد قدیمی که فقط بر روی باند..."
  image = "/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-1.png"

readingTime = 7
difficulty = "medium"
toc = true
math = false
lab_required = true
post_type_fa = "مقاله"

# layout = "single"
type = "posts"
+++

-------
### Wireless Attacks
#### Wireless Standards
شبکه های وایرلسی که امروزه بسیار هم مورد استفاده واقع میشوند در استاندارد های مختلف عرضه شده اند:
1. 802.11g
	1. استاندارد قدیمی که فقط بر روی باند 2.4 کار میکند و پهنای باند آن میتواند تا 300Mb افزایش داشته باشد.
2. 802.11n
	1. استاندارد پر استفاده که بر هر دو باند 2.4 و 5 میتواند کار کند.
3. 802.11 ac
	1. استاندارد جدید که در 2011 عرضه شده است و در هر دو باند 2.4 و 5 میتواند کار کند. پیشرفتی که در این استاندارد داشتیم افزایش پهنای بان مجاز به 1Gb بود.
4. 802.11 ax
	1. جدیدترین استاندارد وایرلسی است که بر روی باند 5Ghz کار میکند و تا 6Gb »یتواند افزایش پهنای باند داشته باشد.
#### Wireless Encryption Algorithms
برای احرازهویت کاربران در شبکه وایرلس از الگوریتم های رمزنگاری مختلفی استفاده میشود که این الگوریتم ها عبارتند از >>
1. WEP(Wired Equivalent Privacy)
	1. این مدل از رمزنگاری Symmetric محسوب میشود از الگوریتم RC4 برای رمزنگاری استفاده میکند.
	2. این مدل امروزه استفاده نمیشود زیرا الگوریتم آن کرک شده است.
		1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-1](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-1.png)
2. WPA 1
	1. این رمزنگاری از پروتکل TKIP(Temporal Key Integrity protocol) استفاده میکند.
	2. همچنین با استفاده از MIC(Message Integrity Check) هم یک لایه  امن سازی اضافه انجام میدهد.
		1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-2](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-2.png)
3. WPA 2
	1. این مدل تقویت شده ورژن اول خود است که از الگوریتم AES(Advance Encryption Standard) برای رمزنگاری استفاده میکند.
		1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-3](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-3.png)
4. WPA 3
	1. پیشرفته ترین الگوریتمی که امروزه میتوانیم از آن برای رمزنگاری استفاده کنیم این مورد است. 
	2. این ورژن Compatibility با Wifi 6(802.11ax) دارد.
#### Rogue Access Point
0. در این مدل Attacker یک SSID فیک و مجازی را با نام SSID اصلی بالا می آورد.
1. سپس کاربر را مجبور به Disconnect از SSID اصلی میکند. 
2. حال کاربر در اتصال مجدد بدلیل اینکه نام SSID Fake با SSID اصلی یکسان است، بصورت خودکار به SSID فیک متصل میشود. 
3. سپس Attacker با ربودن بسته های Three Way Handshake بین کلاینت و SSID فیک سعی به کرک پسورد وایرلس و SSID اصلی میکند.
4. حملات *Evil Twin* و یا *Rogue AP* از نوع شایع این حملات هستند.
	1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-4](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-4.png)
#### DoS and DDoS
حملات DOS , DDOS هم به شبکه های وایرلسی بسیار صورت میگرد که میتواند خدمات دهی شبکه را از کار بیندازد.
این حملات به Channel Wifi, Signal Wifi(jamming), AP Resources, ... انجام میشود که قصد از تمام آنها از کار انداختن سرویس دهی وایرلس است:
	![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-5](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-5.png)

> [!important] 
> در کل پیشنهاد میشود از شبکه های وایرلسی تنها در صورت اجبار استفاده کنیم و تا میشود از  شبکه های سیمی بجای شبکه های بدون سیم استفاده کنیم.

### Air-Crack NG
#### Basic & Concepts
یکی از جعبه ابزار های مرسوم که برای کرک کردن شبکه های وایرلس استفاده میشود، جعبه ابزار `aircrack-ng` میباشد که به وسیله آن انواع حملات وایرلسی را میتوانیم پیاده سازی کنیم. ابزار هایی که در این جعبه ابزار وجود دارند عبارتند از:
1. `aireplay-ng`
	1. حمله بوسیله بسته های Reply به فریم های Wireless
2. `airmon-ng`
	1. بردن کارت شبکه وایرلسی به حالت مانیتورینگ
3. `airodump-ng`
	1. دامپ کردن اطلاعات SSID های اطراف
4. `aircrack-ng`
	1. کرک پسورد درون Three Way Handshake
5. `airbase-ng`
	1. ساخت اکسس پوینت فیک برای راه اندازی حملات Rogue Access Point یا Evil Twin
#### Usage of Air Crack
1. `airmon-ng` Go Wireless NIC to Monitoring Mode 
	1. در اولین قدم باید کارت شبکه که میخواهیم شنود را انجام دهد به حالت مانیتورینگ ببریم. برای اینکار باید کارت شبکه وایرلسی ما `PHY` را ساپورت کند. 
	2. برای فهمیدن موجود بودن PHY در کارت شبکه، کافیست کامند `airmon-ng` را خالی اجرا کنیم تا لیستی از کارت شبکه های وایرلسی را به همراه مشخصات آنها مشاهده کنیم.
	3. در تصویر زیر مشاهده میکنید که کارت شبکه مورد نظر PHY را پشتیبانی نمیکند در نتیجه نمیتوان آنرا در حالت مانیتورینگ استفاد کرد.
		1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-6](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-6.png)
	4. کارت شبکه های برند Alpha بهترین کارت شبکه های وایرلسی برای مانیتورینگ و کرک شبکه های وایرلسی هستند.
```sh
airmon-ng 
airmon-ng start wlan0
#After wlan0 go to monitoring mode, renamed to wlan0-mon 
```
2. `airodump-ng` Check nearby SSID and dump SSID information to `.pcap` file.
	1. در قدم دوم باید SSID های اطراف را بررسی کنیم و سپس اطلاعات در و بدل شده آن را Capture کنیم.
```sh
airodump-ng wlan0
```
3. `aircrack-ng` Crack Password in `.pacap` or `.cap` file
	1. در قدم بعدی، باید با کرک کردن فایل های کپچر شده در قدم قبلی پسورد رد و بدل شده در Three Way Handshake را کرک کنیم.
	2. نکته اینجاست اگر در شبکه وایرلسی کلاینتی Three Way Handshake را انجام نداده باشد، نمیتوانیم پسورد وایرلس را کرک کنیم.
	3. در اینجا مجبوریم که حمله Rogue Access Point را پیاده سازی کنیم تا کاربر مجبور شود دوباره پسورد شبکه را وارد کند و به آن متصل شود.
	4. در آزمایشگاه SANS SEC401 در ماشین لینوکسی به مسیر `/root/labs/401.1/` میرویم تا فایل های آزمایشگاه وایرلس را مشاهده و سپس کرک کنیم:
		1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-7](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-7.png)
	5. 
```sh
cd /root/Labs/401.1 && ls
aircrack-ng SEC401_WEP.cap
```
	![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-8](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-8.png)
	![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-9](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-9.png)
4. Crack by Wordlist
	1. برای کرک رمزنگاری WEP نیازی به Word List برای کرک نیست اما در رمزنگاری های WPA برای کرک Three Way Handshake ها نیازمند Word List هستیم.
	2. برای معرفی لیست حروف از فلگ `w-` استفاده میکنیم. 
	3. برای معرفی SSID برای کرک از فلگ `e-` استفاده میکنیم.
```sh
aircrack-ng -w /usr/share/rockyou.txt SEC401_WPA2PSK.pcap -e SEC401
aircrack-ng -w all SEC401_WPA2PSK.pcap -e SEC401
```
	![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-10](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-10.png)
### Wireshark
#### Basic & Concepts
از این ابزار کبرای شنود بسته های شبکه استفاده میشود. این ابزر میتواند Live Capturing أاشته باشد و یا میتواند فایل های cap, pcap را باز کند.
#### Follow TCP/UDP Stream
اگر میخواهیم Three Way Handshake را که در یک فایل cap, pcap قرار دارد را استخراج کنیم و رمزعبور شبکه وایرلسی را دربیاوریم >>
1. فایل `pcap.` را در Wireshark باز میکنیم.
2. اولین بسته Three Way Handshake را در لیست بسته های وایرلسی پیدا میکنیم و سپس بر روی آن راست کلیک میکنیم، و بر روی `Follow => TCP Stream` کلیک میکنیم تا بتوانیم محتویات ارتباطاتی کامل Three Way Handshake را مشاهده کنیم.
	1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-11](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-11.png)
3. اینکار میتوانیم برای یافتن پسورد های ارتباطات دیگری همچون tftp, telnet, .... هم انجام دهیم. اگر پروتکلی بر بستر UDP کار میکرد باید روی `Follow => UDP Stream` کلیک کنیم.
4. در تصویر زیر UDP Stream مربوط به یک کانکشن tftp را مشاهده میکنیم.
	1. ![SANS-401: Wireless, Aircrack-ng, Wireshark (401.1)-12](/images/cyber-security/SANS-401-Wireless,Aircrack-ng,Wireshark(401.1)-12.png)
### !