+++
tags:
  - CyberSecurity
  - Pentest
Category: Cyber Security
date = '2024-06-20T12:38:14+03:30'
draft = true
title = 'SANS-401.5 Password Cracking'
+++

-------
## E8, E9 - Password Cracking (401.2)
### John The Ripper
#### Basic & Concepts
برای توضیح این ابزار از آزمایشگاه SANS SEC401.2 استفاده میکنیم:
```sh
cd /eoot/Labs/401.2
ls 
```
	![[Pasted image 20240624195037.png]]
برای استفاده از ابزار کافیست کامند `john` را استفاده کنید:
```sh
john --help
john | grep mode
```
	![[Pasted image 20240624195151.png]]
#### John Modes & Modes Flags 🚩
0. `john | grep mode `
1. *Single => Single Crack Mode* `john --single`
	1. روش ساده برای کرک پسورد های استفاده شده در زمان لاگین
	2. در واقع بصورت خودکار میتواند فایل `etc/shadow/` و `etc/passwd/` را بخواند و آنرا کرک کند.
2. *Word List* `john --wordlist[=FILE] --stdin` , `john --stdin`
	1. استفاده از فایل لیست کلمات و یا از Std In برای کرک پسورد و پیاده سازی حمله Dictionary Attack
		1. ![[Pasted image 20240624195533.png]]
3. *Prince* `john --prince[=FILE]` 
	1. استفاده از فایل لیست کلمات برای کرک پسورد
4. *Rules* `john --rules[=SECTION]` 
	1. اعمال قوانینی برای Dictionary Attack و استفاده از Wordlist وارد شده
5. *Incremental* `john --incremental[=MODE]` 
	1. این مود همان bruteforce است که John آنرا مود افزایشی یا Incremental مینامد.
6. *Mask* `john --mask[=MASK]` 
	1. استفاده از Mask یا فرمت مشخص برای کرک پسورد، مثلا تمام حروف 7 حرفی که با D بزرگ شروع و با a تمام میشوند.
7. *Markov* `john --markov[=OPTIONS]` 
	1. یک مود مخصوص است که میتواند توضیحات آنرا در داکیومنت رسمی john مشاهده کنید.
8. *External* `john --external=MODE` 
	1. استفاده از Word filter برای کرک پسورد
#### Users Password Files in Linux
در لینوکس دو فایل مهم که پسورد تمام اکانت ها در آن ذخیره میشوند عبارتند از >>
```sh
cat /etc/passwd
cat /etc/shadow
```
1. در فایل `passwd` یوزر ها بصورت معمولی و پسورد آنها بصورت هش شده مشاهده میشود.
2. در فایل `shadow` هم پسورد یوزرها بصورت هش شده ذخیره میشوند.
> فرمت هش استفاده شده برای ذخیره پسورد ها `Md5` میباشد.
#### Shadow Password Cracking
اگر بخواهیم پسوردهای درون فایلهای `shadow` و `passwd` را توسط John کرک کنیم >> 
1. در ابتدا باید دو فایل `shadow` و `passwd`را بوسیله ابزار `unshadow` آنرا hashing crack کنیم تا بتوانیم سپس آنرا در ابزار `john` وارد کنیم. برای اینکار به نحو زیر عمل میکنیم:
```sh
unshadow passwd shadow > ./unshadow.txt
```
2. حال کافیست این فایل را به ابزار `john` معرفی نیم تا فایل کرک شود و پسورد  تمام اکانت های درون فایل `passwd` و `shadow` بدست بیاید:
```sh
john ./unshadow.txt
```
	![[Pasted image 20240624204001.png]]
#### John Logs
1. تمام پسورد هایی که `john` آنها را کرک میکند، در لاگ فایل `john` ذخیره میشود و این فایل را میتوانیم در مسیر زیر مشاهده کنیم:
```sh
cd /root/.john/john.log
```
2. با استفاده از یک `grep` میتوانیم فقط پسورد های استفاده شده را واکشی کنیم:
```sh
grep "cracked" /root/.john/john.log
#OR 
grep cracked /root/.john/john.log
```
### Security Policies
#### Reasons of Security Policies Usage
1. محافظت از سازمان، کارمندان و اطلاعات
2. محافظت از اطلاعات درون ماشین های درون سازمان
3. مشخص کردن مرز و محدوه برای کارمندان و سازمان که میتواند باعث نظارت بهتر و افزایش امنیت شود.
4. *تصویر*
	2. ![[Pasted image 20240624205403.png]]
#### Security Policies Must Have ...
1. *Purpose *
	1. اهداف مشخص
2. *Related Documents & Reference *
	1. داکیومنت و منابع سیاست ها باید کامل باشد.
3. *Cancellation or Expiration*
	1. سیاست ها باید قابلیت کنسل و منقضی شدن را داشته باشند.
4. *Background*
	1. سیاست ها باید پس زیمنه مشخص داشته باشند.
5. *Scope*
	1. حوزه کاری سیاست ها باید مشخص باشد.
6. *Policy statement*
	1. سیاست ها باید در سطح و لول مشخص خود کار کنند.
7. *Responsibility*
	1. سیاست ها باید نیاز امنیتی مورد نظر را بصورت کامل برطرف کنند.
8. *Action*
	1. سیاست باید واکنش مناسب در زمان خود نشان دهد.
9. *Image*
	1. ![[Pasted image 20240624205939.png]]
#### NDA(Non-Disclosure Agreements)
این سیاست که باید بصورت Enforce تدوین و بین طرفین قرار داد اجرا شود میگوید هیچ یک از طرفین قرار داد نمیتوانند اطلاعات محرمانه که مخصوص شرکت هستند را منتشر کنند و یا استفاده های شخصی از این اطلاعات کنند.
> در واقع این قرارداد محرمانه بودن اطلاعات را بین دو طرف قرار داد مشخص میکند و عدم افشای اطلاعات شرکت توسط طرفین و محرمانه بودن اطاعات هدف اصلی این قرار داد است.
### CAIN
#### Basic & Concepts
یکی از قدیمی ترین، معروف ترین و بهترین ابزار های کرک پسورد و شنود که در ویندوز بصورت GUI قابل استفاده است. 
یکی از استفاده های مرسوم این ابزار کرک فایل های پسورد ویندوز با فرمت هش NTLM است که هنوز هم Cain به خوبی این فایل ها را کرک میکند.
#### Cain Features
 از امکاناتی که این ابزار دارد میتوان به موارد زیر اشاره کرد:
1. *Password Cracker*
	1. Cracker tab
		1. ![[Pasted image 20240624211241.png]]
	2. 
2. Sniffer
	1. Start/Stop Sniffer
		1. ![[Pasted image 20240624210842.png]]
	2. Cisco Devices Passwords Decoder
		1. ![[Pasted image 20240624211100.png]]
	3. 
3. Decoder
	1. Base64 Decoder
		1. ![[Pasted image 20240624211034.png]]
	2. 
4. Network Tools
	1. Start/Stop ARP Cache Pois
		1. ![[Pasted image 20240624210955.png]]
	2. 
5. Wireless Tools
6. etc ...
	1. RSA SecureID Calculator
		1. ![[Pasted image 20240624211139.png]]
	2. 
7. Image
	1. ![[Pasted image 20240624210729.png]]
#### Crack NTLM Hashing
برای کرک کردن فایل پسورد ویندوز بوسیله Cain میتوانیم از یک فایل استخراج شده استفاده میکنیم و یا میتوانیم از Local System فایل را ابتدا بخوانیم و سپس کرک کنیم. همچنین میتوانیم مستقیما فایل دیتابیس SAM را به ابزار معرفی کنیم.
> برای اینکار بر روی `+` کلیک میکنیم: 
	![[Pasted image 20240624211736.png]]
1. *Use Local System Accounts*
	1. با انتخاب این گزینه تمام اکانت های که بر روی این ماشین ویندوزی فعال هستند را میتوان مشاهده کرد:
		1. ![[Pasted image 20240624212005.png]]
	2. سپس بر روی هر اکانتی که میخواهیم پسورد آنرا کرک کنیم راست کلیک میکنیم و سپس نوع حمله را انتخاب میکنیم:
		1. ![[Pasted image 20240624212124.png]]
	3. همچنین در منو راست کلیک با استفاده از گزینه `Test Password` میتوانیم عملیات کرک پسورد را بصورت Password Guessing یا حدس زدن انجام دهیم.
		1. ![[Pasted image 20240624212250.png]]
#### Cain Attack Types
*حملات مرسوم و پراستفاده در Cain عبارتند از:*
1.  `Dictionay Attack => NTLM Hashes` Normal NTLM Cracking
	1. ساده ترین مدل حمله  است، در این حمله ابتدا باید Wordlist جامع را به ابزار معرفی کنیم تا با جستجو عبارت های درون آن فایل و امتحان آنها بر روی فایل هش شده بتوان پسور مورد نظر را کرک کرد.
		1. ![[Pasted image 20240624212751.png]]
	2. ابزار Cain خود یک Wordlist نسبتا جامع دارد که در فولدر محل نصب ابزار قابل مشاهده است. اما پیشنهاد میشود ابتدا توسط ابزاری مانند Crunch لیست  مورد نظر خود را بسازید و سپس آنرا در این محل انتخاب کنید.
		1. ![[Pasted image 20240624212900.png]]
	3. پس از انتخاب فایل باید Option های حمله از جمله Lower, Upper Case و .... را مشخص کنیم:
		1. ![[Pasted image 20240624213056.png]]
	4. با کلیک بر روی `Start` هم برنامه شروع به کرک پسورد میکند:
		1. ![[Pasted image 20240624213224.png]]
	5. میتوانیم چندین اکانت را با هم انتخاب کنیم و سپس حمله را بر روی تمامی این اکانت ها انجام دهیم.
2. `Cracker => Cisco Typer-7 Password Decoder Hashes => +` Cisco Typer-7 Password Decoder
	1. از این ویژگی میتوانیم برای Decode کردن پسورد روتر ها و سوئیچ های سیسکو استفاده کنیم که اینکار را با استفاده از فایل `router config` آن دیوایس انجام میدهیم: 
		1. ![[Pasted image 20240624213704.png]]
	2. برای اینکار فایل `router_config` دیوایس را باز میکنیم و سپس مقدار متغیر `password 7` که بصورت هش شده است را کپی میکنیم و سپس در فیلد مربوط در ابزار Paste میکنیم:
		1. ![[Pasted image 20240624213812.png]]
	3. به محض Paste کردن عبارت در ابزار میتوانیم مقدار دقیق پسورد را مشاهده کنیم:
		1. ![[Pasted image 20240624213852.png]]
3. `Cracker => Cisco IOS-Md5 Hashes => +` Cisco IOS-Md5 Hashes 
	1. در بعضی از فایل های `router_config` ممکن است پسورد بصورت هش شده با فرمت Md5 هم موجود است. این مقدار را در متغیر `enable secret 5` میتوان مشاهده کرد:
		1. ![[Pasted image 20240624214101.png]]
	2. برای کرک کردن این نوع از پسورد ها، کافیست به تب `Cracker => Cisco IOS-Md5 Hashes ` برویم و سپس بر روی `+` کلیک کنیم:
		1. ![[Pasted image 20240624214347.png]]
	3. حال میتوانیم عبارت کپی شده از فایل `router_config` را در فیلد اول پیست کنیم و یا میتوانیم فایل `router_config` را مستقیما `Import`  کنیم.
		1. *Manual Hashing*
			1. ![[Pasted image 20240624214522.png]]
		2. *From Configuration File*
			1. ![[Pasted image 20240624214603.png]]
	4. حال که عبارات هش شده در ابزار وارد شده کافیست بر روی یکی از آنها کلیک راست کنیم و سپس نوع حمله `Dictionary | Bruteforce` را انتخاب کنیم:
		1. ![[Pasted image 20240624214731.png]]
	5. سپس هم در پنجره حمله Option های حمله  و یا Wordlist مورد استفاده در حمله را انتخاب میکنیم.
		1. ![[Pasted image 20240624214923.png]]
4. *Cryptanalysis Attacks*
	1. در این حملات میتوانیم از هر دو نوع حمله `Dictionary | Bruteforce` بصورت همزمان استفاده کنیم تا عملیات کرک را بصورت هدفمند و با دقت بیشتری انجام شود.
	2. در واقع میتوان گفت نوعی از `Hybrid Attack` میباشد.
> استفاده از حملات Dictionary با Wordlist جامع از بهترین نوع حملات است.
### !
