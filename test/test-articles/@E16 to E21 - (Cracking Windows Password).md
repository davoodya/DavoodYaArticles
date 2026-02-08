---
Episode: E16 to E21
Date: 2024-06-29
Is Finished?: true
Practice Primary: true
Practice Secondary: 
Time: 36:00
tags:
  - CyberSecurity
  - hacking
Category: Cyber Security
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[E7 to E15 - (Bypassing & Resetting Windows Password)]]"
Next Episode: "[[E22 to E27 (Cracking Compresses & Offices Files - Part1)]]"
---
-------
#CyberSecurity #hacking 
# E16 to E21 - (Cracking Windows Password)
- [Cracking Password with `Ophcrack` & `Kali` - E16](#Cracking%20Password%20with%20%60Ophcrack%60%20&%20%60Kali%60%20-%20E16)
	- [Cracking or Bypassing this is a Question?](#Cracking%20or%20Bypassing%20this%20is%20a%20Question?)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is Ophcrack?](#What%20is%20Ophcrack?)
		- [Usage Scenario](#Usage%20Scenario)
		- [Instructions Steps](#Instructions%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [Cracking Password with `Ophcrack` & `Windows` - E17](#Cracking%20Password%20with%20%60Ophcrack%60%20&%20%60Windows%60%20-%20E17)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [0.1 Usage Scenario](#0.1%20Usage%20Scenario)
		- [0.2 Obtaining(Get) Hashes Ways Description](#0.2%20Obtaining(Get)%20Hashes%20Ways%20Description)
		- [1. Download & Install Ophcrack](#1.%20Download%20&%20Install%20Ophcrack)
		- [2. Dumping Hashes](#2.%20Dumping%20Hashes)
		- [3. Cracking Hashes](#3.%20Cracking%20Hashes)
	- [Practical Demo](#Practical%20Demo)
- [Cracking Password with `john` & `Kali` - E18](#Cracking%20Password%20with%20%60john%60%20&%20%60Kali%60%20-%20E18)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is John the Ripper(JTR)?](#What%20is%20John%20the%20Ripper(JTR)?)
		- [Usage Scenario](#Usage%20Scenario)
		- [Wordlists](#Wordlists)
			- [Basic & Concetps](#Basic%20&%20Concetps)
			- [Kali Built-In Wordlists](#Kali%20Built-In%20Wordlists)
			- [Other Wordlists](#Other%20Wordlists)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [Cracking Password with `hashcat` & `Kali` - E19](#Cracking%20Password%20with%20%60hashcat%60%20&%20%60Kali%60%20-%20E19)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is Hashcat?](#What%20is%20Hashcat?)
		- [Concept of Hashcat Usage](#Concept%20of%20Hashcat%20Usage)
		- [`Hashcat` Command & Flags](#%60Hashcat%60%20Command%20&%20Flags)
			- [Hashcat Description](#Hashcat%20Description)
			- [Hashcat Flags](#Hashcat%20Flags)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [Password Extraction from RAM with `Mimikatz` - E20](#Password%20Extraction%20from%20RAM%20with%20%60Mimikatz%60%20-%20E20)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Whats Mimikatz?](#Whats%20Mimikatz?)
		- [Usage Scenario](#Usage%20Scenario)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [Review of Password Cracking, Bypassing & Recovery - E21](#Review%20of%20Password%20Cracking,%20Bypassing%20&%20Recovery%20-%20E21)
	- [Comparing Password Reset/Bypassing Tools](#Comparing%20Password%20Reset/Bypassing%20Tools)
	- [Comparing Password Cracking Tools](#Comparing%20Password%20Cracking%20Tools)
------
### Cracking Password with `Ophcrack` & `Kali` - E16 
#### Cracking or Bypassing this is a Question?
- *عملیات کرک و عملیات Bypass دو علمیات مجزا هستند که در زیر به توضیح تفاوت آنها میپردازیم >>*
1. در عملیات کرک سعی میکنیم از عبارت هش شده پسورد به مقدار واقعی پسورد برسیم که در این روش میتوانیم ناشناس بمانیم و در واقع غیر قابل رهگیری میشود. البته اگر ماشین تارگت به Logger مجهز باشد میتواند این حمله را ثبت و ضبط کند.
2. در عملیات Bypassing نیاز و احتیاج به وارد کردن پسورد توسط کاربر را دور میزنیم، در واقع سعی میکنیم مکانیزم های امنیتی را دور بزنیم. این روش قابل رهگیری است زیرا که یوزر در لاگین خود بعدی خود میتواند تغییر پسورد را مشاهده کند.
#### Definition & Instruction
##### What is Ophcrack?
ابزار `Ophcrack` یک کرکر پسورد برای سیستم عامل ویندوز و لینوکس است که بصورت پیشفرض بر روی Kali نصب است. این Cracker با جداول Rainbow Table کار میکند و همچنین به GUI هم برای کار کردن راحت تر شدن استفاده مجهز است. 
	![[Pasted image 20240627164406.png]]
- در جداول Rainbow Table، مقادیر از قبل هش شده هزاران عبارت وجود دارد(Pre-Computed Hashes) که قبلا در Dictionary Attack ها استفاده شده است و سپس در دیتابیسی جمع آوری شده است. 
- استفاده از این روش سرعت بسیار بیشتری در کرک پسورد نسبت به حملاتی همچون Dictionary Attack و یا Bruteforce دارد زیرا که با بررسی هش فعلی با داده های موجود سرعت یافتن عبارت اصلی بصورت تصاعدی افزایش میابد.
> در واقع میتوان گفت Rainbow Table دیتابیس جامع از مقادیر هش شده عبارات مختلف هستند که میتوانند برای یافتن مقدار اصلی از هش بسیار مفید باشند. هرچه این دیتابیس جامع تر باشد دقت حمله بالا میرود و سرعت آن کاهش میابد.
> جداول رنگین کمانی مخصوص Ophcrack را از وبسایت رسمی Ophcrack در بخش Tables میتوانیم دانلود و در ابزار Ophcrack نصب کنیم. 
##### Usage Scenario
فرض کنید به ماشین ویندوزی دسترسی فیزیکی داریم که `Password Locked` است، با استفاده از `Ophcrack` میتوانیم پسورد اکانت مورد نظر را `Crack` کنیم.
	![[Pasted image 20240627164729.png]]
دقت کنید در اینجا واقعا پسورد را `Crack` میکنیم یعنی از عبارت هش شده پسورد به مقدار واقعی پسورد میرسیم، بر عکس مطالب قبلی که نیاز به وارد کردن پسورد را Bypass میکردیم و در واقع کلا احراز هویت بوسیله پسورد را بر میداشتیم.
##### Instructions Steps
0. برای اینکار نیاز به Kali Live boot USB داریم. 
	1. *بیشتر بخوانید =>*  [[E0 to E6- (Introduction & Installation Kali Linux)]]
1. ماشین را Kali Live بوت میکنیم.
2. سپس به مسیر زیر میرویم و فایل های `SAM` و `SYSTEM` را به دسکتاپ کالی انتقال میدهیم.
	1. `/media/kali/WINDOWSDRIVE/Windows/System32/config`
		1. ![[Pasted image 20240627165558.png]]
3. سپس `Ophcrack` را اجرا میکنیم:
	1. `Kali Start => 05-Password Attacks => Ophcrack `
		1. ![[Pasted image 20240627165712.png]]
4. در GUI ابزار، بر روی `Load => Encrypted SAM` کلیک میکنیم و پوشه `Desktop` که فایل `SAM, System` در آن قرار دارد را انتخاب میکنیم.
	1. ![[Pasted image 20240627165848.png]]
5. ابزار تمام اکانت های درون فایل SAM را لیست میکند:
	1. ![[Pasted image 20240627170028.png]]
6. حال باید جدول Rainbow Table را دانلود و در Ophcrack نصب کنیم:
	1. جدول رنگین کمان بنام `vista free rainbow` را از وبسایت اصلی Ophcrack دانلود میکنیم.
	2. دانلود از https://ophcrack.sourceforge.io/tables.php
		1. ![[Pasted image 20240627170252.png]]
	3. سپس در GUI ابزار، بر روی Tables کلیک میکنیم تا بتوانیم جدول مربوط که دانلود کردیم را نصب کنیم.
		1. ![[Pasted image 20240627170420.png]]
	4. در صفحه باز شده جدول `Vista Free` را انتخاب میکنیم و بر روی `Install` کلیک میکنیم.
		1. ![[Pasted image 20240627170511.png]]
	5. جدول Rainbow Table با موفقیت به Ophcrack اضافه شد.
7. حال کافیست اکانتی که میخواهیم پسورد آن کرک شود را انتخاب میکنیم و سپس بر روی `Crack` کلیک کنیم تا ابزار پسورد اکانت مورد نظر را کرک کند.
	1. ![[Pasted image 20240627170845.png]]
#### Practical Demo
0. *Boot Machine with Kali Live*
	1. Create Bootable USB from Kali Live 
	2. Restart machine & Booting with Removable USB Device
	3. Start Live Kali System(686-pae)
		1. ![[Pasted image 20240627173204.png]]
1. *Copy SAM and SYSTEM Files*
	1. Navigate to => `media/kali/WINDOWSDRIVE/Windows/System32/config`
	2. Right Click on folder & Open as Root
		1. ![[Pasted image 20240627173419.png]]
	3. Copy `SAM` & `SYSTEM` files & Paste it to Desktop
		1. ![[Pasted image 20240627173608.png]]
2. *Open `Ophcrack` and Load SAM, SYSTEM*
	1. Open Tool => `Kali Start => 05-Password Attacks => Ophcrack `
	2. Click `Load => Encrypted SAM`
		1. ![[Pasted image 20240627173754.png]]
	3. Select `Desktop` Folder
		1. ![[Pasted image 20240627173826.png]]
	4. Now all accounts in SAM file listed by Ophcrack
		1. ![[Pasted image 20240627173908.png]]
3. *Download & Install Vista Free Rainbow Table*
	1. Download `Vista Free(461Mb)` Rainbow Table from https://ophcrack.sourceforge.io/tables.php
	2. Extracted ZIP Downloaded file & Navigate to this directory
		1. ![[Pasted image 20240627174320.png]]
	3. `Ophcrack => Tables => Select Vista Free => Install => Select tables_vista_free directory => Open `
		1. ![[Pasted image 20240627174526.png]]
		2. ![[Pasted image 20240627174529.png]]
	4. Now `Vista Free(461Mb)` Rainbow Table Successfully Installed
		1. ![[Pasted image 20240627174627.png]]
4. *Cracking all accounts Passwords*
	1. Now Vista Free table seen in Main Page of GUI
		1. ![[Pasted image 20240627174816.png]]
	2. Click `Crack` to Cracking all accounts password in the list using Vista Free Rainbow Table
		1. ![[Pasted image 20240627174911.png]]
	3. Now waiting to Cracking Finished and then you can see all accounts passwords
		1. ![[Pasted image 20240627175034.png]]
5. Waiting some hours(base on password characters and complexity) and then Cracking Operation Successfully Done
	1. بنابراین دفعالت اولی که میخواهیم فرآیند کرک را انجام دهیم، بسته به تعداد کارکارتر ها و یا پیچیدگی پسورد میتواند مدت زمان عملیات کرک ممکن است تا ساعت ها نیز طول بکشد.
### Cracking Password with `Ophcrack` & `Windows` - E17 
#### Definition & Instruction
##### 0.1 Usage Scenario
فرض کنید به ماشین ویندوزی دسترسی فیزیکی داریم که `Password Locked` است:
- در اینجا میتوانیم مقادیر hash شده فایل را کپی کنیم و سپس بوسیله ابزار `Ophcrack` در یک حمله آفلاین پسورد های درون آنرا را کرک کنیم.
- هنگامیکه یکبار بوسیله این روش پسورد های یک فایل هش شده را کرک میکنیم، میتوانیم از این مقادیر برای کرک یوزر های یک سیستم مشابه هم استفاده کنیم. در واقع `Reusable` است.
	- ![[Pasted image 20240627175809.png]]
- بنابراین دفعالت اولی که میخواهیم فرآیند کرک را انجام دهیم، بسته به تعداد کارکارتر ها و یا پیچیدگی پسورد میتواند مدت زمان عملیات کرک ممکن است تا ساعت ها نیز طول بکشد.
##### 0.2 Obtaining(Get) Hashes Ways Description
برای بدست آوردن مقادیر هش شده رمز های عبور ماشین روش های متفاوتی وجود دارد که میتوانیم از آنها استفاده کنیم:
1. *روش اول(پیشنهادی):* ابتدا ماشین را با دیسک Kali Live بوت میکنیم و سپس فایل های `SAM و SYSTEM` را در یک حافظه مجزا کپی میکنیم تا بتوانیم بعدا آنرا کرک کنیم.
2. *روش دوم:* میتوانیم مستقیما بوسیله `Ophcrack` مقادیر هش شده را `Dump` کنیم. البته این روش همه جا کارایی ندارد.
3. *روش سوم:* با استفاده از کامند های CMD میتوانیم از `Registry` مقادیر هش شده پسورد ها را `Dump` کنیم و در یک فایل متنی ذخیره کنیم تا پس از آن فایل را کرک کنیم.
4. *اسلاید:*
	1. ![[Pasted image 20240627180328.png]]
##### 1. Download & Install Ophcrack
1. Download Ophcrack
	1. https://ophcrack.sourceforge.io/
		1. ![[Pasted image 20240627180509.png]]
2. Download Vista Free Rainbow Table
	1. https://ophcrack.sourceforge.io/tables.php
3. Install Vista Free on Ophcrack 
	1. `Ophcrack => Tables => Select Vista Free => Install => Select tables_vista_free directory => Open => OK `
			1. ![[Pasted image 20240627180749.png]]
##### 2. Dumping Hashes
- دقت کنید روش اول ممکن است در ویندوز های 10 و 11 کار نکند. 
1. *در روش اول* با استفاده از ابزار داخلی Ophcrack بنام `samdump2` فایل SAM ماشین محلی را واکشی میکنیم.
- `Ophcrack => Local SAM with samdump2 `
	1. ![[Pasted image 20240627181151.png]]
2. *در روش دوم* با استفاده از کامند های زیر میتوانیم فایل SAM را واکشی کنیم. این روش در ویندوز های 10 و 11 هم کار میکند.
	1. ![[Pasted image 20240627181417.png]]
```powershell
C:\> reg.exe save hklm\sam c:\temp\sam
C:\> reg.exe save hklm\system c:\temp\system
```
	![[Pasted image 20240627181448.png]]
3. *در روش سوم* هم که میتوانستیم ماشین را Kali Live USB بوت کنیم، سپس به `Windows/System32/config` برویم و فایل های `SAM & SYSTEM` را از آنجا کپی و در حافظه ای مجزا پیست کنیم.
	1. ![[Pasted image 20240627181956.png]]
4. پس از واکشی فایل SAM باید آنرا در `Ophcrack` لود کنیم.
	1. ![[Pasted image 20240627181805.png]]
- `Ophcrack => Load => Encrypted SAM ` Select folder which `SAM & SYSTEM` file in there.
##### 3. Cracking Hashes
0. حال که Rainbow Table را در ابزار نصب کردیم و همچنین فایل SAM که مقادیر هش شده پسورد ها در آن میباشد را بدست آوردیم، کافیست در GUI ابزار بر روی `Crack` کلیک کنیم تا عملیات کرک با موفقیت انجام شود:
	1. ![[Pasted image 20240627182415.png]]
#### Practical Demo
0. Download & Install
	1. Download `Ophcrack Windows Portable Version`
	2. Extract Zip file, then Run Ophcrack.exe from Extracted folder
		1. ![[Pasted image 20240627182732.png]]
	3. Download `Vista Free Rainbow Table` & Extract Downloaded Folder
	4. `Ophcrack => Tables => Select Vista Free => Install => Select tables_vista_free Folder => Open => Click Ok Finish Installing `
		1. ![[Pasted image 20240627183014.png]]
1. *Dumping Hashes Way 1:* Local SAM with `Ophcrack samdump2`
	1. `Ophcrack => Load => Local SAM with samdump2`
		1. ![[Pasted image 20240627183219.png]]
	2. in Windows 10 or 11 we Got this Error
		1. ![[Pasted image 20240627183254.png]]
	3. But this function successfully working in *Windows XP, 7, 8 and older version of Windows 10*
2. *Dumping Hashes Way 2:* Command Prompt
	1. SAM & SYSTEM files save on `c:/temp` folder
	2. After running following Commands 
	3. `Ophcrack => Load => Encrypted SAM ` Select `c:/temp` folder
	4. Now yo can see all accounts in machine listed in Ophcrack GUI
		1. ![[Pasted image 20240627184141.png]]
```powershell
#Open in Escalation Privilege (Run as Administrator)
C:\> reg.exe save hklm\sam c:\temp\sam
C:\> reg.exe save hklm\system c:\temp\system
```
	![[Pasted image 20240627183816.png]]
3. *Dumping Hashes Way 3:*
	1. Plug Kali Live USB to machine and boot machine with this
	2. Navigate `/Windows/System32/config` and Open directory `as Root` 
	3. then Copy `SAM & SYSTEM` files and Paste it to another External USB Drives
		1. ![[Pasted image 20240627184455.png]]
	4. `Ophcrack => Load => Encrypted SAM ` Select `/ophcrack/x64/` folder
	5. Now yo can see all accounts in machine listed in Ophcrack GUI
		1. ![[Pasted image 20240627184551.png]]
4. *Now we can Cracking Password*
	1. After Installing Vista Free Rainbow Table & Load SAM file(which contains Accounts Password hashes) we can crack passwords
	2. `Ophcrack => Crack `
		1. ![[Pasted image 20240627184744.png]]
3. Password Successfully Cracked by Ophcrack utility
		1. ![[Pasted image 20240627184824.png]]
	4. 
### Cracking Password with `john` & `Kali` - E18
#### Definition & Instruction
##### What is John the Ripper(JTR)?
یکی از ابزار های محبوب و معروف در زمینه کرک پسورد هاست است که در انواع توزیع های لینوکسی مانند Kali, Parrot, Hawk, .... قابل دسترس است.
این ابزار دارای رابط CLI بصورت User-friendly است که بوسیله آن میتوانیم اکثر hash Types های مختلف را کرک کنیم. 
	![[Pasted image 20240628150819.png]]
در این جلسه میخواهیم بوسیله john پسورد ماشین ویندوزی را کرک کنیم.
##### Usage Scenario
*فرض کنید به ماشین ویندوزی دسترسی فیزیکی داریم که Password Locked است:*
- در اینجا میتوانیم بوسیله ابزار `John the Ripper` پسورد ماشین را کرک کنیم. 
- دقت کنید که میخواهیم پسورد را Crack کنیم و نه Bypass کنیم.
	- ![[Pasted image 20240628151152.png]]
*برای اینکار باید >>*
- ابتدا Hash ها را از فایل SAM بدست بیاوریم.
- سپس بوسیله John مقادیر پسورد ها را از مقادیر هش شده بدست بیاوریم.
	- ![[Pasted image 20240628151426.png]]
##### Wordlists
###### Basic & Concetps 
با استفاده از ابزار John متیوانیم حملات مختلفی مانند Bruteforce, Dictionary, Hybrid, ... را بر روی فایل هش بدست آمده پیاده سازی کنیم.
- در حملات Dictionary Attack باید لیستی از کلمات Wordlists را به ابزار معرفی کنیم که ابزار با استفاده از آن لیست به کرک بپردازد. برای معرفی Wordlists به ابزار از سوئیچ `w-` استفاده میشود که اگر خالی استفاده شود ابزار از Built-in Dictionary خود استفاده میکند. 
```sh
`john -w hash.txt --format=NT`
```
- `-w` => تعریف لیست کلمه، اگر خالی استفاده شود از دیکشنری داخلی ابزار استفاده میشود.
- `--format` => برای تسریع سرعت کرک بهتر است فرمت هش را مشخص کنیم.
###### Kali Built-In Wordlists
- در سیستم عامل Kali یکسری Wordlists بصورت پیشفرض در مسیر زیر وجود دارد:
```sh
ls /usr/share/wordlists/
```
- فایل `rockyou.txt` یک فایل Wordlist جامع و معروف است که در توزیع های کالی لینوکس بصورت پیشفرض وجود دارد. این فایل را بصورت فشرده شده `gz.` در مسیر زیر میتوان یافت که برای استفاده باید با دستور `gunzip` بصورت Uncompressed شود تا بتوان آنرا در ورودی ابزار john استفاده کنیم.
	- ![[Pasted image 20240628160956.png]]
```sh
locate rockyou
gunzip /usr/share/wordlists/rockyou.txt.gz
john -w="/usr/share/wordlists/rockyou.txt" ./hash.txt --format=NT
```
###### Other Wordlists
از Wordlist های معروفی که در اینترنت وجود دارند میتوانیم به نمونه های زیر اشاره کنیم:
	![[Pasted image 20240628155948.png]]
*Best Alternate Word lists Collections.*
1. https://weakass.com
2. https://github.com/danielmiessIer/SecLists/tree/master/Passwords/WiFi-WPA
3. https://labs.nettitude.com/blog/rocktastic
4. https://github.com/kennyn510/wpa2-wordIists
همچنین با ابزار هایی مانند Crunch نیز میتوانیم Wordlist های را مخصوص حملات خود ایجاد کنیم.
##### Instruction Steps
0. *Pre-Requires Step*
	1. ساخت USB دیسک bootable از Kali Live
	2. اتصال USB به ماشین و بوت کردن ماشین ویندوزی با Kali Live
1. *Obtaining Hashes*
	1. ابتدا به دایرکتوری `Windows/System32/config` میرویم و دو فایل `SAM & SYSTEM` را از آنجا کپی و در Desktop پیست میکنیم.
		1. ![[Pasted image 20240628152534.png]]
	2. حال باید ترمینال را در Desktop باز کنیم و مقادیر هش شده را بوسیله کامند زیر Dump کنیم:
	3. `samdump2 SYSTEM SAM > hash.txt`
	4. *ابزار `Samdump2`:* از این ابزار برای Dump کردن مقادیر هش شده از فایل SAM استفاده میکنیم.
	5. *فایل `hash.txt`:* مقادیر هش شده که استخراج کردیم در این فایل ذخیره میشود.
		1. ![[Pasted image 20240628152913.png]]
2. *Cracking Hashes*
	1. حال میتوانیم پسورد مورد نظر را از فایل `hash.txt` که مقادیر هش شده پسورد های ویندوز در آن وجود دارد را بوسیله `John` با استفاده از حملات مختلف کرک کنیم.
	2. *Dictionary Attack with John Built-In Dictionary:*
		1. در حمله اول میخواهیم بوسیله Built-in Dictionary که در خود John وجود دارد حمله را انجام دهیم:
		2. `john -w hash.txt --format=NT`
			1. `-w` => تعریف لیست کلمه، اگر خالی استفاده شود از دیکشنری داخلی ابزار استفاده میشود.
			2. `--format` => برای تسریع سرعت کرک بهتر است فرمت هش را مشخص کنیم.
			3. IF Target windows 11 => `--format==LM` 
			4. Image
				1. ![[Pasted image 20240628153529.png]]
	3. *Dictionary Attack with Rockyou file:*
		1. *Description:*
			1. فایل `rockyou.txt` یک فایل Wordlist جامع و معروف است که در توزیع های کالی لینوکس بصورت پیشفرض وجود دارد. این فایل را بصورت فشرده شده `gz.` در مسیر زیر میتوان یافت که برای استفاده باید با دستور `gunzip` بصورت Uncompressed شود.
				1. ![[Pasted image 20240628154049.png]]
			2. `ls /usr/share/wordlists/`
				1. در این دایرکتوری Wordlist های دیگری هم وجود دارد اما جامع ترین آنها rockyou.txt است.
			3. `gunzip /usr/share/wordlists/rockyou.txt.gz`
				1. خارج کردن فایل rockyou.txt از حالت فشرده
		2. *Attack Steps:*
			1. حال در این حمله میخواهیم از rockyou.txt به عنوان Wordlist حمله استفاده کنیم بنابراین باید به نحو زیر عمل کرد:
			2. `john -w="/usr/share/wordlists/rockyou.txt" ./hash.txt --format=NT`
				1. ![[Pasted image 20240628154513.png]]
			3. پس از اجرای کامند بالا، ابزار شروع به کرک فایل hash.txt میکند و اگر نتیجه موفقیت آمیز باشد نتیجه حمله به شکل زیر میشود:
				1. ![[Pasted image 20240628154704.png]]
			4. IF Target windows 11 => `--format==LM` 
3. Password Cracked Successfully
#### Practical Demo
0. Create bootable Kali Live Disk and booted machine with this.
1. Navigate to `C:/Windows/System32/config` and Copy `SAM & SYSTEM` to Desktop
2. Open Terminal in Desktop and Run following Command to *Cracking Passwords*
	1. `samdump2 SYSTEM SAM > hash.txt` Dumping Hashes from SYSTEM & SAM 
		1. ![[Pasted image 20240628160408.png]]
	2. `john -w hash.txt --format=NT` Built-In Dictionary Attack
		1. ![[Pasted image 20240628160613.png]]
	3. `john -w="/usr/share/wordlists/rockyou.txt" hash.txt --format=NT` Dictionary Attack with Rockyou.txt Wordlist
		1. ![[Pasted image 20240628161153.png]]
3. Password Cracking Successfully finished
```sh
samdump2 SYSTEM SAM > hash.txt
john -w hash.txt --format=NT #Built-In Dictionary Attack

#Dictionary Attack with Rockyou.txt Wordlist
locate rockyou
gunzip /usr/share/wordlists/rockyou.txt.gz
john -w="/usr/share/wordlists/rockyou.txt" hash.txt --format=NT 
```
### Cracking Password with `hashcat` & `Kali` - E19
#### Definition & Instruction
##### What is Hashcat?
- ابزار `Hashcat` یک ابزار مبتنی بر `GUI` است که در نتیجه برای اجرای آن نیازمند ماشینی هستیم که کارت گرافیک GPU مناسب و قوی به همراه تمام درایور های مورد نیاز آن را بر روی خود داشته باشد.
- ابزار Hashcat را میتوانیم بر روی ویندوز، انواع توزیع های لینوکس و حتی رایانه های ابری Cloud اجرا کنیم. 
- در این جلسه ما به استفاده از Hashcat در ویندوزی میپردازیم که مجهز به GPU Powerful است. همچنین تمام درایور های GPU نیز نصب شده اند.
	![[Pasted image 20240628162115.png]]
##### Concept of Hashcat Usage

*فرض کنید به ماشین ویندوزی دسترسی فیزیکی داریم که Password Locked است:*
- در اینجا میتوانیم بوسیله ابزار `Hashcat` پسورد ماشین را کرک کنیم. 
- همچنین میتوانیم فایل متنی بنام `hash.txt` که مقادیر هش استخراج شده از فایل های `SAM & SYSTEM` در آن ذخیره میشوند را در یک حافظه فلش USB کپی کنیم و در زمانی مناسب در مکانی دیگر در یک ماشین Kali دیگر به کرک این پسورد ها بپردازیم. به این نوع از حمله به اصطلاح `Offline Attack` هم گفته میشود. 
	- ![[Pasted image 20240628162929.png]]
*برای کرک پسورد بوسیله Hashcat باید مراحل زیر را انجام دهیم:*
1. بوت کردن ماشین با Kali Live و بدست آوردن فایل های `SAM & SYSTEM` 
2. پیاده سازی حمله Dictionary Attack بوسیله Hashcat و فایل Rockyou برای کرک کردن پسورد ها
	1. ![[Pasted image 20240628162507.png]]
##### `Hashcat` Command & Flags
###### Hashcat Description
- کامند و ابزار `Hashcat` را هم در Powershell Windows و هم در Terminal Linux میتوانیم استفاده کنیم.
- برای کرک کردن یک فایل یا عبارت hash ابتدا باید آن فایل را به پوشه ای که فایل `Hashcat.exe` وجود دارد منتقل کنیم و سپس به عملیات کرک بپردازیم.
- همچنین فایل Wordlist که میخواهیم از آن برای کرک استفاده کنیم نیز باید در پوشه فایل `Hashcat.exe` باشد.
- `hashcat.exe [OPTIONS] HASH.txt WORDLIST.txt`
```sh
.\Hashcat.exe -m 1000 -a 0 -o cracked.txt hash.txt rockyou.txt
```
###### Hashcat Flags
- `-m 1000`
	- مشخص کننده نوع فرمت هش، که هر عدد معنای خود را دارد.
	- مثلا عدد هزار نشان دهنده این است که هش وارد شده مربوط ویندوز است.
	- میتوان گفت که `m 1000-` در `Hashcat`، همان معنای `format=NT--` در `John` را میدهد.
- `-a 0`
- `-o output.txt`
	- فایل خروجی و Result Crack در این فایل ذخیره میشود.
- `-D 2` & `-d 3`
	- این دو فلگ میتوانند کانفیگ های کارت گرافیک مثلا تعداد Thread های فعال GPU که همزمان میتوانند برای کرک استفاده شوند را تنظیم میکند.
	- وارد کردن این دو فلگ اختیاری است.
```powershell
.\hashcat.exe -a 0 -m 1000 -D 2 -d 3 --status -o cracked.txt hash.txt rockyou.txt
```
##### Instruction Steps
0. *Pre-Requires*
	1. Create bootable USB Disk from Kali Live
	2. Download & Install `Hashcat` from official website https://hashcat.net/hashcat/
		1. ![[Pasted image 20240628163240.png]]
	3. Download & Extracted the `Rockyou` dictionary in hashcat folder https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
		1. ![[Pasted image 20240628163418.png]]
	4. Plug-In USB Drive to machine and booted machine from it
		1. ![[Pasted image 20240628163452.png]]
1. *Obtaining Hashes*
	1. ابتدا به دایرکتوری `Windows/System32/config` میرویم و دو فایل `SAM & SYSTEM` را از آنجا کپی و در `Desktop` پیست میکنیم.
		1. ![[Pasted image 20240628152534.png]]
	2. حال باید `Terminal` را در `Desktop` باز کنیم و مقادیر هش شده را بوسیله کامند زیر Dump کنیم:
	3. `samdump2 SYSTEM SAM > hash.txt`
		1. ![[Pasted image 20240628163628.png]]
	4. حال فایل `hash.txt` را در حافظه USB دیگری کپی میکنیم و سپس آنرا به `PC اصلی` انتقال میدهیم.
		1. ![[Pasted image 20240628163805.png]]
2. *Cracking Password by Hashcat*
	1. حال که فایل `hash.txt` را در پوشه Hashcat در ویندوز اصلی کپی کردیم، در همان پوشه `Powershell` را باز میکنیم و سپس کامند های زیر را برای کرک پسورد اجرا میکنیم:
		1. ![[Pasted image 20240628164805.png]]
	2. `.\Hashcat.exe -m 1000 -a 0 -o cracked.txt hash.txt rockyou.txt`
		1. `-m 1000` فرمت هش ویندوزی است
		2. `-a 0`
		3. `-o cracked.txt` مشخص کننده فایل خروجی نتیجه کرک
		4. Image
			1. ![[Pasted image 20240628164931.png]]
	3. حال کافیست فایل `cracked.txt` را باز کنیم تا متن کرک شده هر هش را مشاهده کنیم:
		1. ![[Pasted image 20240628165030.png]]
3. Cracking Successfully Done by Hashcat
#### Practical Demo
0. *Pre-Requires*
	1. Prepare Kali Live Bootable Disk
	2. Download hashcat https://hashcat.net/hashcat/
		1. ![[Pasted image 20240628173545.png]]
	3. Download Rockyou https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
		1. ![[Pasted image 20240628174233.png]]
	4. then Extracted Rockyou to Hashcat Folder
	5. Rebooted windows machine on Kali Live Disk
1. *Obtaining Hashes*
	1. Navigate to `C:/Windows/System32/config` and Copy `SAM & SYSTEM` to `Desktop`
	2. Open Terminal in `Desktop`
	3. Run Following Commands to extract hashes from SYSTEM & SAM files
		1. `samdump2 SYSTEM SAM > hash.txt` Dumping hashes
	4. Now copy `hash.txt` to a Removable USB Disk
2. *Cracking Hashes with Hashcat*
	1. Connect USB Removable to Windows Machine and Copy `hash.txt` to `Hashcat Folder`  on main windows
	2. Open `Powershell` in `hashcat` folder
	3. Run following Commands to Cracking `hash.txt`
		1. `.\Hashcat.exe -a 0 -m 1000 -D 2 -d 3 --status -o cracked.txt hash.txt rockyou.txt`
			1. ![[Pasted image 20240628175912.png]]
		2. وارد کردن دو فلگ `-D 2` & `-d 3` که مشخص کننده کانفیگ های GPU است، اختیاری است.
3. Password Successfully Cracked, Now We can see Cracking Result in 
	1. Powershell Terminal
		1. ![[Pasted image 20240628180121.png]]
	2. `cracked.txt` in Hashcat folder
		1. ![[Pasted image 20240628180205.png]]
```sh Kali Live
samdump2 SYSTEM SAM > hash.txt #Dumping hashes to hash.txt
```
---
```powershell Open in hashcat folder
.\hashcat.exe -a 0 -m 1000 -D 2 -d 3 --status -o cracked.txt hash.txt rockyou.txt
```
- *Image:*
	- ![[Pasted image 20240628175923.png]]
### Password Extraction from RAM with `Mimikatz` - E20
#### Definition & Instruction
##### Whats Mimikatz?
ابزار Mimikatz یک Credential Dumper است که میتواند پسورد ها و لاگین های اکانت های ویندوز را بدست بیاورد. 
- همچنین از Mimikatz در تست های امنیتی شبکه هم استفاده میشود و میتواند باعث افزایش امنیت شبکه شود.
*نقل قولی از وبسایت معروف wired.com است که میگوید::*
- ابزار Mimikatz، یکی از بهترین و قدرتمند ترین ابزار ها در زمنیه Password Stealth است.
	- ![[Pasted image 20240629191102.png]]
##### Usage Scenario
فرض کنید به ماشینی که Password Locked است و همچنین پسورد آن با استفاده از سیاست های بسیار قوی محافظت میشود دسترسی فیزیکی داریم. در واقع به ماشینی دسترسی فیزیکی داریم که با `Password Locked` شده است و به `Strong Security Policies` هم مجهز است. در اینجا برای کرک پسورد >>

> [!example] Example in Real Place
> *در مثال واقعی:* فرض  کنید ماشین تارگت در شرکتی قرار دارد و ما توانسته ایم در روز به آن شرکت وارد شویم. روز است و سیستم تمام کارمندان روشن است، برای هک و کرک سیستم کافیست یک فلش داشته باشیم که Mimikatz در آن نصب باشد. با متصل کردن فلش به ویندوز تاگت و Dump کردن مقدار هش از RAM و ذخیره مقدار hash شده در فلش، میتوانیم بعدا بوسیله یک ماشین Kali و ابزاری مانند John یا Hashcat به رک مقدار Hash شده بپردازیم تا پسورد ماشین مورد نظر را بدست بیاوریم.

*مزیت های Mimikatz >>*
1. میتوانیم مقادیر Passwords Hashes را از حافظه موقت RAM بوسیله `Mimikatz` استخراج کنیم و سپس بوسیله `John` به کرک مقادیر هش شده بپردازیم.
2. ابزار `Mimikatz` با استفاده از `Post-Exploitation Phase` مقادیر `Hash` شده از `RAM` استخراج میکند.
	![[Pasted image 20240628181420.png]]
##### Dumping local system authority process
1. همچنین میتوانیم بوسیله Mimikatz مقادیر Account Hashes را از RAM Active(رم فعال) بدست بیاوریم(Dumping)
1. برای انجام اینکار به `Task Manager` میرویم. 
2. سپس بر روی `local system authority proccess` کلیک راست میکنیم و `Create Dump` را میفشاریم.
	1. ![[Pasted image 20240629191905.png]]
3. فایل Dump شده در مسیر زیر قابل مشاهده است:
4. `C:\User\Davoodya\AppData\Local\Temp\lass.dump`
	1. ![[Pasted image 20240629191845.png]]
##### Instruction Concepts 
*برای کرک کردن پسورد بوسیله Mimikatz باید مراحل زیر را دنبال کنیم. در واقع مفاهیم حمله با استفاده از Mimikatz به شرح زیر است:*
1. ابتدا باید در ماشین ویندوزی مقادیر درون `local Security authority proccess` که در `Task Manager` قرار دارد را `Dump` کنیم.
2. سپس `Mimikatz` را اجرا میکنیم و فایل `DMP.` را با `sekurlsa::minidump` میکنیم.
3. حال میتوانیم مقادیر `hash` شده اکانتی که لاگین کرده است را بوسیله `sekurlsa::logonPasswords` بدست بیاوریم. 
4. حال مقدار `hash` اکانت مورد نظر را در فایلی متنی ذخیره میکنیم و این فایل را به `Kali` منتقل میکنیم.
5. حال در `Kali` میتوانیم مقدار hash شده را `Crack` کنیم. این کار را بوسیله ابزار هایی مانند `John` یا `Hashcat` براحتی میتوانیم انجام دهیم.
##### Instruction Steps
1. *Dumping* `local Security authority proccess`
	1. `Task Manager => Right-Click local Security authority proccess => Create Dump`
		1. ![[Pasted image 20240629192113.png]]
	2. See Dump `C:\User\Davoodya\AppData\Local\Temp\lsass.DMP`
2. *Download Mimikatz ZIP File*
	1. https://github.com/ParrotSec/mimikatz
		1. ![[Pasted image 20240629192147.png]]
	2. Download ZIP File and Extract it
3. *Extract Hashes from Dump File*
	1. حال فایل `DMP.` را به پوشه Mimikatz منتقل میکنیم و سپس CMD را در پوشه Mimikatz باز میکنیم و کامند های زیر را به ترتیب اجرا میکنیم تا مقادیر هش شده را از فایل Dump شده استخراج کنیم.
```powershell
cd C:\User\Davoodya\Download\mimikatz-master\Win32
C:\User\Davoodya\Download\mimikatz-master\Win32> mimikatz.exe
#-----#-----# Mimikatz Command #-----#-----#
privilege::debug
sekurlsa::minidump C:\Users\Davoodya\AppData\Local\Temp\lsass.DMP

standard::log .\hash-log.txt
sekurlsa::logonPasswords
```
	![[Pasted image 20240629192552.png]]
4. *See Hashes file*
	1. حال مقادیر هش شده تمام اکانت هایی که به این ماشین لاگین کردند را در فایل `hash.txt` در پوشه Mimikatz میتوانیم مشاهده کنیم. Mimikatz مقادیر هش شده اکانت ها را در فرمت های `NTLM, SHA 1` را به همراه `Username, Domain` آنها نمایش میدهد.
		1. ![[Pasted image 20240629192855.png]]
	2. حال فقط مقدار هش اکانتی که میخواهیم کرک شود را در فایل نگه میداریم و بقیه محتوا را پاک میکنیم تا مقدار هش شده آماده کرک شود:
		1. ![[Pasted image 20240630230049.png]]
5. *Cracking Passwords*
	1. حال میتوانیم فایل `hash.txt` را بوسیله ابزار هایی مانند John یا Hashcat کرک کنیم تا پسورد اکانت ها را بدست بیاوریم.
	2. برای انجام اینکار، ابتدا فایل `hash.txt` را به ماشین کالی منتقل میکنیم و سپس از کامند زیر برای کرک پسورد استفاده میکنیم.
		1. ![[Pasted image 20240629193228.png]]
```sh
john -w hash.txt --format="NT" #Use Built-In Dictionary for Attack

#Or Attack with hashcat
hashcat -a 0 -m 1000 hash.txt /usr/share/wordlists/rockyou.txt #Dictionary Attack
hashcat -a 3 -m 1000 hash.txt cbad@4321 #Bruteforce Attack
hashcat hash.txt -m 1000 --show #See Cracked Result
```
	![[Pasted image 20240629193232.png]]
6. Cracking Successfully Done
	1. در تصویر اول مقدار هش اکانت Administrator را مشاهده میکنیم که توسط John کرک شده است:
		1. ![[Pasted image 20240630230406.png]]
	2. 
#### Practical Demo 
0. *پیش نیاز ها*
	1. Download Mimikatz from https://github.com/ParrotSec/mimikatz
	2. Extract Mimikatz to a Folder
1. باز کردن CMD در پوشه Mimikatz با دسترسی Administrator و اجرای آن
```powershell
cd C:\User\Davoodya\Download\mimikatz-master\Win32
C:\User\Davoodya\Download\mimikatz-master\Win32> mimikatz.exe
mimikatz: privilege::debug
```
2. دامپ کردن `local system authority process`
	1. `Task Manager => Right-Click local system authority proccess => Create Dump` Dumping local system authority process
		1. ![[Pasted image 20240629194127.png]]
	2. See `.DMP` file =>
		1. ![[Pasted image 20240629194153.png]]
3. حال به CMD که Mimikatz در آن باز است بر میگردیم و دستورات زیر را در کنسول Mimikatz وارد میکنیم:
```powershell
C:\User\Davoodya\Download\mimikatz-master\Win32> mimikatz.exe
mimikatz: privilege::debug
mimikatz: log hash.txt
mimikatz: sekurlsa::minidump C:\Users\Davoodya\AppData\Local\Temp\lsass.DMP
mimikatz: sekurlsa::logonPasswords #when run this command all accounts in machine wich logged in, listed in terminal and also stored in hash.txt file
```
	![[Pasted image 20240629194522.png]]
	![[Pasted image 20240629194711.png]]
4. *مشاهده نتیجه Hash های بدست آمده*
	1. حال نتیجه کرک را در ترمینال و همچنین در فایل `hash.txt` درون پوشه Mimikatz که لاگ های ابزار درون آن ذخیره شده است را میتوانیم مشاهده کنیم:
		1. ![[Pasted image 20240629194859.png]]
	2. حال تمام داده های اضافی را از فایل `hash.txt` حذف میکنیم و فقط نام یوزر و مقدار hash شده NTLM آنرا در جلوی آن وارد میکنیم:
		1. ![[Pasted image 20240629195049.png]]
	3. سپس هم فایل `hash.txt` را کپی و در ماشین کالی پیست میکنیم.
5. *کرک کردن فایل Hash بدست آمده `hash.txt`*
	1. حال که فایل `hash.txt` را به ماشین کلی منتقل کردیم، Terminal را در جایی که فایل وجود دارد باز میکنیم تا بتوانیم آنرا بوسیله `John` و یا `Hashcat` کرک کنیم.
```sh Kali Machine
john -w hash.txt --format="NT"
#Or Attack with hashcat
hashcat -a 0 -m 1000 hash.txt /usr/share/wordlists/rockyou.txt #Dictionary Attack
hashcat -a 3 -m 1000 hash.txt cbad@4321 #Bruteforce Attack
hashcat hash.txt -m 1000 --show #See Cracked Result
```
- *Images:*
	- ![[Pasted image 20240629195355.png]]
	![[Pasted image 20240630224514.png]]
### Review of Password Cracking, Bypassing & Recovery - E21
#### Comparing Password Resetting/Bypassing Tools
تا اینجا ابزار هایی را برای Resetting و یا Bypassing پسورد ها بررسی کردیم که هر کدام مزایا و معایب خود خاص را دارند، همچنین از هر کدام نیز در ورژن های خاصی از ویندوز میتوان استفاده کرد. 
*در تصویر زیر میتوانید مقایسه ای کامل بین تمامی این ابزار ها را مشاهده کنید:*
	![[Pasted image 20240630191905.png]]
*دو نمونه از بهترین این ابزار ها >>*
1. یکی Kon Boot است که میتواند به سرعت برای Bypass و یا Unlock Online Account استفاده شود.
2. دومی هم ابزار و کامند Chntpw در Kali Live که برای تغییر فایل SAM ماشین ویندوزی و در واقع Bypassing مکانیزم وارد کردن پسورد برای لاگین استفاده میشود.
#### Comparing Password Cracking Tools
ابزار هایی که برای کرک کردن پسورد بررسی کردیم را نیز در تصویر زیر میتوانیم با هم مقایسه کنیم:
	![[Pasted image 20240630192334.png]]
1. `John` Easiest to Use
	- از ساده ترین ابزار ها `John` را میتوان نام برد که میتواند مقادیر هش شده را در حملاتی مانند Dictionary Attack کرک کند.
2. `Hashcat` Fast GPU Based Cracker
	- مزیت ابزار `Hashcat` استفاده از GPU در فرآیند کرک است که باعث افزایش تصادعی سرعت کرک میشود. 
	- با استفاده از این ابزار میتوانیم انواع حملات از جمله Bruteforce, Dictionary, Hybrid, .... را برای کرک مقادیر هش پیاده سازی کنیم.
3. `Ophcrack` Fast Speed Cracking with Rainbow Tables
	- ابزار `Ophcrack` میتواند با استفاده از Rainbow Table ها که مقادیر Precomputed hashes(هش های از قبل محاسبه شده) در آن قرار دارد سرع عملیات کرک را بالا ببرد.
4.  `Mimikatz` Recover Hashes from RAM
	- ابزار  `Mimikatz` یکی از پیشرفته ترین و پیچیده ترین ابزار های برای Password Stealth است. مزیت هم این است که میتواند داده های RAM را Dump کند. در واقع میتوان گفته هنگامیکه هیچ روش کار نکند،  `Mimikatz` با قدرت میتواند کرک کند.
	- چالش اینجاست که استفاده از  `Mimikatz` پیچیدگی خاص خود را دارد و برای استفاده از آن باید به اسکریپت نویسی مسلط بود.

> [!NOTE]
> در کل زمان عملیات Cracking پسورد بسته به تعداد کاراکتر های پسورد، پیچیدگی پسورد و قدرت منابع ماشین متغیر میباشد. همچنین اگر هیچ یک از روش ها بالا کار نداد  میتوان بر روی Mimikatz حساب کرد، فقط کافیست منابع بیشتری در مورد این ابزار بدانید.

### !
