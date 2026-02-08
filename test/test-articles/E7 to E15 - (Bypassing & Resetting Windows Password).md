---
Episode: E7 to E15
Date: 2024-06-27
Is Finished?: true
Practice Primary: true
Practice Secondary: 
Time: 52:00
tags:
  - CyberSecurity
  - hacking
Category: Cyber Security
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[E0 to E6- (Introduction & Installation Kali Linux)]]"
Next Episode: "[[@E16 to E21 - (Cracking Windows Password)]]"
---
-------
#CyberSecurity #hacking 
## E7 to E15 - (Bypassing & Resetting Windows Password)
- [Password Storing on Windows Functionality](#Password%20Storing%20on%20Windows%20Functionality)
	- [How Windows Stored Password?](#How%20Windows%20Stored%20Password?)
	- [Get Windows Password Ways](#Get%20Windows%20Password%20Ways)
	- [Tools Need for Bypassing Windows Password](#Tools%20Need%20for%20Bypassing%20Windows%20Password)
	- [Tools Need for Cracking Windows Password](#Tools%20Need%20for%20Cracking%20Windows%20Password)
- [Bypassing Windows Password](#Bypassing%20Windows%20Password)
	- [Bypassing with `chntpw` Utility - E9](#Bypassing%20with%20%60chntpw%60%20Utility%20-%20E9)
		- [Instruction & Definitions](#Instruction%20&%20Definitions)
			- [What is chntpw?](#What%20is%20chntpw?)
			- [Attacks by this Utility](#Attacks%20by%20this%20Utility)
			- [Windows Passwords Save Path](#Windows%20Passwords%20Save%20Path)
			- [Download & Install `chntpw`](#Download%20&%20Install%20%60chntpw%60)
			- [Booting Windows on `chntpw` & Cracking Password](#Booting%20Windows%20on%20%60chntpw%60%20&%20Cracking%20Password)
		- [Practical Demo](#Practical%20Demo)
	- [Bypassing Online Authentication by Active Local Administrator using `chntpw` - E11](#Bypassing%20Online%20Authentication%20by%20Active%20Local%20Administrator%20using%20%60chntpw%60%20-%20E11)
		- [Instruction](#Instruction)
			- [Scenario Scheme](#Scenario%20Scheme)
			- [Instruction Steps](#Instruction%20Steps)
		- [Practical Demo](#Practical%20Demo)
	- [Bypassing Windows Password using `KonBoot` - E12](#Bypassing%20Windows%20Password%20using%20%60KonBoot%60%20-%20E12)
		- [Definitions & Instructions](#Definitions%20&%20Instructions)
			- [What is KonBoot?](#What%20is%20KonBoot?)
			- [Instructions Steps](#Instructions%20Steps)
		- [Practical Demo](#Practical%20Demo)
	- [Bypassing Windows Password using `HIREN'S Boot CD` - E13](#Bypassing%20Windows%20Password%20using%20%60HIREN'S%20Boot%20CD%60%20-%20E13)
		- [Definitions & Instructions](#Definitions%20&%20Instructions)
			- [What is Hiren Boot CD?](#What%20is%20Hiren%20Boot%20CD?)
			- [Scenario Schema](#Scenario%20Schema)
			- [Instructions Steps](#Instructions%20Steps)
		- [Practical Demo](#Practical%20Demo)
	- [Bypassing Windows Password using `Windows Boot Disk` - E14](#Bypassing%20Windows%20Password%20using%20%60Windows%20Boot%20Disk%60%20-%20E14)
		- [Definitions & Instructions](#Definitions%20&%20Instructions)
			- [Definitions](#Definitions)
			- [Scenario Schema](#Scenario%20Schema)
			- [Instructions Steps](#Instructions%20Steps)
		- [Practical Demo](#Practical%20Demo)
- [Resetting Windows Password](#Resetting%20Windows%20Password)
	- [Reset Windows Password by Kali & `chntpw` - E10](#Reset%20Windows%20Password%20by%20Kali%20&%20%60chntpw%60%20-%20E10)
		- [Instruction & Definition](#Instruction%20&%20Definition)
			- [Usage Scenario](#Usage%20Scenario)
			- [`chntpw` Command Flags](#%60chntpw%60%20Command%20Flags)
			- [Instructions Steps](#Instructions%20Steps)
		- [Demo](#Demo)
	- [Reset Windows Password with `Lazesoft` - E15](#Reset%20Windows%20Password%20with%20%60Lazesoft%60%20-%20E15)
		- [Definitions & Instructions](#Definitions%20&%20Instructions)
			- [Definitions](#Definitions)
			- [Usage Scenario](#Usage%20Scenario)
			- [Instruction Steps](#Instruction%20Steps)
		- [Practical Demo](#Practical%20Demo)
- [!](#!)

### Password Storing on Windows Functionality 
#### How Windows Stored Password?
1. هنگامیکه مقدار رمز عبور کاربری را تغییر میدهیم و یا پسورد کاربر جدید را انتخاب میکنیم، ویندوز hash این رمز عبور را با فرمت هش NTLM ذخیره میکند. 
2. ویندوز از فرمت Hash بنام `LM Hash` یا `NT Hash` و یا جدیدا `NTLM Hash` استفاده میکند.
3. ویندوز مقادیر Hash شده پسورد ها را در فایلی در دیتابیسی بنام `SAM(Security Account Manager)` ذخیره میکند که اصولا در ماشین یوزر Administrator قابل مشاهده و دسترس است.
4. میدانیم که Hash ها یکطرفه هستند بدین معنا که از عبارت Hash شده نمیتوان مستقیما به مقدار واقعی پسورد رسید.
5. بنابراین هنگامیکه کاربر در Login Screen پسورد اکانت خود را وارد میکند، ویندوز این عبارت را Hash میکند و سپس با Hash درون دیتایس SAM مقایسه میکند و اگر دو مقدار  برابر بود اجازه دسترسی را به یوزر میدهد.
	1. ![[Pasted image 20240625204101.png]]
#### Get Windows Password Ways 
- دو روش مرسوم که میتوان برای دور زدن و کرک پسور های ویندوزی از آن استفاده کنیم Bypassing و Cracking نام دارند. در روش Cracking با استفاده از هش موجود پسورد ها سعی در بدست آوردن پسورد میکنیم و در روش Bypassing سعی میکنیم پسورد فعلی را برداشته تا بتوانیم پسورد جدید را خودمان تعیین کنیم.
*اصولا از این دو روش بصورت ترکیبی و با دستور العمل خاص استفاده میشوند که مثال هایی از آن عبارتند از >>*
1. راه اندازی Kali و گرفتن دسترسی به ویندوز و سپس Bypassing پسورد لاگین 
2. کرک کردن پسورد ویندوز با استفاده از استخراج Hash پسورد از دیتابیس SAM
3. استخراج پسورد از حافظه کوتاه مدت RAM
4. استخراج پسورد از دیتابیس SAM در هنگام بوت ماشین
5. *تصویر*
	1. ![[Pasted image 20240625203057.png]]
#### Tools Need for Bypassing Windows Password
1. Kali Linux Machine
2. `CHNTPW`
3. KON-Boot
	1. ![[Pasted image 20240625203312.png]]
4. Windows Install Disk
5. HIREN'S PE X64 2020
	1. ![[Pasted image 20240625203307.png]]
#### Tools Need for Cracking Windows Password
1. John the Ripper
	1. ![[Pasted image 20240625203543.png]]
2. Hashcat
	1. ![[Pasted image 20240625203547.png]]
3. OPCrack(OS Crack)
	1. ![[Pasted image 20240625203538.png]]
### Bypassing Windows Password
#### Bypassing with `chntpw` Utility - E9
##### Instruction & Definitions
###### What is chntpw?
از ابزار `chntpw` برای ریست کردن پسورد Local Users های درون یک ویندوز استفاده میشود، همچنین بوسیله این ابزار میتوانیم تمام کلید های رجیستری ماشین را نیز تغییر دهیم. مزیت این ابزار این است که تمامی نسخه های ویندوز از `XP` تا `11` این ابزار را پشتیبانی میکنند.
در واقع میتوان گفت ازاین ابزار برای ریست کردن پسورد یوزر های محلی در ویندوز استفاده میشود و بهترین ابزار در زمینه کاری خود هم محسوب میشود:
	![[Pasted image 20240625204616.png]]
**این ابزار فقط در Bios کار میکند و در ماشین های که با UEFI بوت میشوند نمیتواند کار کند. قابلیت Secure Boot هم باید خاموش باشد.**
###### Attacks Scenarios Using `chntpw`
این ابزار در دو سناریو متفاوت قابل استفاده است:
1. *Attack 1:* Machine Locked with Password
	1. در این حالت دسترسی فیزیکی به ماشین هدف که توسط پسورد قفل شده `Password Locked` است داریم.
	2. این ابزار در اینجا برای حذف سریع پسورد فعلی استفاده میشود تا بتوانیم پسورد جدید بر روی اکانت مورد نظر تنظیم کنیم.
2. *Attack 2:* Machine Protect by Online Account
	1. در این حالت دسترسی فیزیکی به ماشین ویندوزی داریم که از `Online Account` مانند ایمیل برای لاگین و احراز هویت استفاده میکند.
	2. در اینجا از این ابزار برای فعال سازی `Local Administrator` در این ماشین ویندوزی استفاده میکنیم که پس از آن میتوانیم با دسترسی Full به این ماشین ویندوزی تارگت دسترسی داشته باشیم.
3. *Attack 3:* Registry Edit
	1. با ایجاد تغییرات در کلید های رجیستری هم کار های بسیار زیاد را میتوانیم بر روی ماشین مقصد انجام دهیم. 
	2. *مثلا:* میتوانیم سرویس های SSH یا FTP را در ماشین تارگت فعال کنیم تا بتوانیم دسترسی شل را نیز به ماشین تارگت بگیریم.
###### Windows Passwords Save Path
گفتیم که ویندوز اطلاعات تمامی یوزر ها از جمله پسورد هر اکانت بصورت Encrypt شده را درون فایلی بنام `SAM` ذخیره میکند که این فایل را میتوانیم در مسیر `c:\\windows\system32\config` پیدا کنیم:
```powershell
cd c:\\windows\system32\config
```
- حال ابزار `CHNTPW` با  دستکاری manipulate کردن این فایل سعی میکند پسورد های ذخیره شده را بصورت Clean استخراج کند و سپس پسورد را با عبارت که ما وارد میکنیم عوض کند. این ابزار فرآیند manipulate را بصورت Interactive با کمک کاربر انجام میدهد.
###### Download & Install `chntpw`
1. Download `USB Version of chntpw` from official website
	- https://pogostick.net/~pnh/ntpasswd/
		- ![[Pasted image 20240625210046.png]]
2. Extract Downloaded file and Copy all files into a USB Drive
	1. دقت کنید حافظه USB فرمت شده باشد و داده مهمی در آن وجود نداشته باشد:
		1. ![[Pasted image 20240625210207.png]]
3. Open CMD as Administrator in `utility Folder` and then run below commands
	1. دقت داشته باشید حرف `f` حرف درایو USB است که میخواهیم ابزار بر روی آن بصورت Bootable نصب شود. 
	2. بنابراین دقت کنید که Drive Letter را بدرستی وارد کنید.
	3. به محض اجرای کامند، حافظه USB ما با ابزار نصب شده `chntpw` بصورت bootable در می آید.
	4. *تصویر*
		1. ![[Pasted image 20240625210611.png]]
```powershell
#f is drive letter, so enter based on your USB Disk Drive Letter
f:syslinux.exe -ma f:
```
4. Now Restart PC and Boot Machine with USB Disk
	1. ![[Pasted image 20240625210910.png]]
###### Booting Windows on `chntpw` & Cracking Password
هنگامیکه ماشین را با حافظه USB که `chntpw` را بر روی آن نصب کردیم بوت میکنیم، ابزار `chntpw` بصورت خودکار بدنبال نسخه ویندوز نصب شده و درایوی که ویندوز بر روی آن نصب است میگردد و لیست درایو هایی که ویندوز بر روی آن نصب است را نشان میدهد. حال کافیست >>
1. *Select Type(Drive) and Press Enter*
	1. در این مرحله باید انتخاب کنیم درایو هایی که ویندوز بر روی آن نصب شده است بصورت خودکار پیدا شوند و یا بصورت دستی مشخص شوند. همچنین میتوان مشخص کرد درایو های نصب ویندوز از حافظه مجزا Floppy, CD, DVD خوانده شود.
		1. ![[Pasted image 20240625211258.png]]
2. *Now Select File you want Manipulate that*
	0. در این قسمت باید عملیاتی که میخواهیم بر روی درایو و ویندوز مشخص شده انجام گیرد را مشخص میکنیم که عبارتند از >>
	1. Password Reset(SAM)
	2. Recovery Console Parameters
	3. Load Almost all of it
	4. در اینجا ما میخواهیم پسورد ماشین را ریست کنیم بنابراین `1` را انتخاب میکنیم.
		1. ![[Pasted image 20240625211758.png]]
3. *Now Select Options*
	0. در این قسمت گزینه های کرک پسورد را انتخاب میکنیم:
	1. `Edit User data and password`
		1. برای کرک پسورد این گزینه را انتخاب میکنیم که در این سناریو هم اینگونه است.
	2. List Groups
	3. Registry Editor with Full Write Support
	4. `Type 1 & Press Enter`
		1. ![[Pasted image 20240625212059.png]]
4. *Now Select User to Cracking Password*
	1. در این مرحله ابزار تمام یوزر های محلی که در این ماشین وجود دارند را برای ما لیست میکند که میتوانیم یکی از آنها را انتخاب کنیم تا پسورد آن کرک شود.
	2. برای انتخاب یوزر از شماره `RID` یوزر استفاده میکنیم:
	3. در اینجا RID یوزر مورد نظر `03eb` را وارد میکنیم و Enter را میزنیم:
		2. ![[Pasted image 20240625212318.png]]
5. *Now Select options to Clear Password*
	0. در این مرحله گزینه های Clear کردن password را انتخاب میکنیم.
	1. *Clear (blank) User Password*
		1. ریست کردن و خالی پسورد یوزر که در اینجا هم میخواهیم همین کار را انجام دهیم.
	2. *Unlock and Enable User Account*
		1. اگر یوزر فعلی قفل شده است این گزینه میتواند قفل را بشکند.
	3. *Promote User*
		1. این گزینه یوزر انتخاب شده را Administrator میسازد.
	4. *Add user to a group*
		1. این گزینه یوزر مورد نظر را به گروهی دلخواه اضافه میکند.
	5. *Remove user from group*
		1. این گزینه یوزر مورد نظر را از گروهی دلخواه حذف میکند.
	6. `Type 1 and Press Enter`
		1. ![[Pasted image 20240625212846.png]]
6. *Now press `quit` and Save Changes by Pressing `Y`*
	1. پس از انتخاب عملیاتی که بر روی پسورد انجام دادیم، از ابزار quit میکنیم و در سوالی که پرسیده میشود با فشردن Y تغییرات یا به اصطلاح Hives ها را ذخیره میکنیم.
		1. ![[Pasted image 20240625213152.png]]
7. Reboot Your System and your password will removed
	1. پس از ریبوت ماشین در بالا آمدن مجدد میتوانیم مشاهده کنیم که پسورد اکانت مورد نظر برداشته شده است.
##### Practical Demo
1. Download `CHNTPW` 
	1. Goto https://pogostick.net/~pnh/ntpasswd/
	2. Download `USB` Version
		1. ![[Pasted image 20240625214011.png]]
2. Booted USB Disk
	1. Extracted downloaded files
	2. Format USB Disk
	3. Copy extracted files to USB Disk
	4. Copy Drive Letter to Use in Next Step
	5. in `readme.txt` read about tool usage
		1. ![[Pasted image 20240625214251.png]]
3. Open Command Prompt as Administrator & Run below command to booted flash with chntpw
	1. حرف درایو را باید بر اساس درایو USB که فایل های ابزار را در مرحله قبل در آن کپی کردیم وارد میکنیم.
```powershell
C:\Windows\System32>f:\syslinux.exe -ma f:
#F is Drive Letter which chntpw files in there
```
	![[Pasted image 20240625214646.png]]
4. Reboot machine and boot on USB Disk
	1. ![[Pasted image 20240625214805.png]]
5. Now Setup `chntpw` for Cracking a User
	0. با فشردن `Enter` در پنجره خوش آمد گویی ابزار، وارد محیط کاری ابزار شوید.
		1. ![[Pasted image 20240625214916.png]]
	1. در مرحله اول تمام درایور های لود میشوند:
		1. ![[Pasted image 20240625214950.png]]
	2. جستجو خودکار پارتیشن هایی که ویندوز دارند را انتخاب میکنیم => `1`
		1. ![[Pasted image 20240625215303.png]]
	3. فایل `SAM` را برای کرک شدن انتخاب میکنیم => `1`
		1. ![[Pasted image 20240625215410.png]]
	4. عملیاتی `Edit User data and passwords` را که میخواهیم بر روی SAM انجام شود، انتخاب میکنیم => `1`
		1. ![[Pasted image 20240625215602.png]]
	5. یوزر `Administrator` یا هر یوزر که میخواهیم را با وارد کردن `RID` آن انتخاب میکنیم => `01f4`
		1. ![[Pasted image 20240625215723.png]]
	6. حال عملیات `Clear(Blank) User Password` که میخواهیم بر روی یوزر Administrator انجام شود را انتخاب میکنیم => `1`
		1. ![[Pasted image 20240625215907.png]]
	7. *"پسورد با موفقیت پاک شد"*
		1. ![[Pasted image 20240625220016.png]]
	8. *حال با فشردن `q` از ابزار خارج میشویم و تغییرات را نیز ذخیره میکنیم >>*
		1. در سوال اول ابزار میپرسد فایل را دوباره بنویسم؟ با فشردن `Y` جواب بله میدهیم.
		2. در سوال دوم ابزار میپرسد که میخواهید تغییرات را ذخیره کنید؟ با فشردن `Y` جواب بله میدهیم.
		3. در سوالی دیگر هم میپرسد که اگر در عملیات با Failure مواجه شدید میخواهید مجددا از نو ادامه دهید که با فشردن `N` جواب خیر میدهیم.
			1. ![[Pasted image 20240625220429.png]]
9. Now Reboot machine and you can login with Administrator Account without needed to Password
	1. ماشین را ریست کنید و میبینید که در لاگین برای یوزر Administrator آز شما پسورد نمیخواهد.
#### Bypassing Online Authentication by Active Local Administrator using `chntpw` - E11
##### Instruction
###### Scenario Scheme
در این جلسه میخواهیم با فعالسازی اکانت administrator محلی در ویندوز، احراز هویت اکانت آنلاین مانند ایمیل را دور بزنیم و دسترسی به آن ماشین ویندوزی بگیریم.
- فرض کنید به ماشین ویندوزی که با `Online Email Password` محافظت میشود و قفل شده است دسترسی فیزیکی داریم. در این جا میتوانیم ماشین را با استفاده از Kali Live USB بوت کنیم و سپس اکانت `Local Administrator` را در این ماشین فعال کنیم.
	- ![[Pasted image 20240626155739.png]]
###### Instruction Steps
0. Boot windows machine from Kali Linux Live USB
1. When Kali is UP, goto `/media/kali/[WINDOWS-DRIVE]/Windows/System32/config` 
	1. Open Directory as Root
		1. ![[Pasted image 20240626160051.png]]
	2. Open Terminal in this directory when open it as root
2. Now Run following command, Open SAM by `chntpw`
	1. `chntpw -i SAM`
3. `chntpw` Options
	1. Edit user data and passwords => `Type 1`
	2. Type Administrator Account RID => `01f4`
		1. ![[Pasted image 20240626160436.png]]
	3. Unlock and enable user accounts (Probably locked now)=> `Type 2`
		1. ![[Pasted image 20240626160553.png]]
	4. Quit & Save Hives(Chan) => `Type q` then `Type Y`
		1. ![[Pasted image 20240626160629.png]]
	5. Reboot System & boot to windows
4. Now we can see *Administrator* Account with Blank Password Appears on the Lock Screen 
	1. ![[Pasted image 20240626160730.png]]
##### Practical Demo 
1. . ماشین ویندوزی را با Live Kali USB بوت میکنیم.
2. به درایوی که ویندوز در آن نصب است میرویم و سپس به پوشه `Windows/System32/config` میرویم:
	1. ابتدا در فضای خالی کلیک راست و `Open as root` را میفشاریم.
	2. سپس دوباره در فضای خالی کلیک راست و `Open Terminal here` را میفشاریم.
		1. ![[Pasted image 20240626161122.png]]
	3. *اگر دسترسی به Kali Live نداریم:*
		1. میتوانیم از دیسک نصب معمولی Ubuntu استفاده کنیم که Live Ubuntu بصورت پیشفرض همیشه در آن وجد دارد.
		2. پس از بالا آوردن Ubuntu به پوشه  `Windows/System32/config` میرویم و فایل های `SAm & SYSTEM` را در یک فلش دیسک دیگر کپی میکنیم.
		3. فلش دیسک را به لپ تاپ که کالی نصب است متصل میکنیم، به دایرکتوری فلش میرویم و `Terminal` را با دسترسی `Root` در آن دایرکتوری باز میکنیم.
		4. حال ابزار `chntpw` را باز میکنیم و مراحلی زیر را ادامه میدهیم:
		5. *نکته:* پس از کرک دو فایل SAM & SYSTEM ، باید مجددا فلش را به Ubuntu Live متصل کنیم و فایل های کرک شده را با فایل های اصلی عوض کنیم تا عملیات کرک ما با موفقیت تمام شود.
3. حال `chntpw` را بصورت Interactive بر روی فایل SAM اجرا میکنیم. شرح کانفیگ های ابزار عبارتند از:
	1. `chntpw -i SAM`
	2. loaded Hives *Type* `1` => Edit user data and passwords
	3. Edit Users Info & Password *Type User RID* `01f4` => Select Administrator Account
	4.  User Edit Menu*Type* `2` => Unlock and Enable user account(probably locked now)
		1. ![[Pasted image 20240626161535.png]]
	5. *Type* `q` => Quit Editing User `THEN` *Type* `y` => Save Hive Changes
	6. Restart Machine and booted to Windows 
4. حال میتوانیم با اکانت Administrator بدون نیاز به وارد کردن پسورد لاگین کنیم. همچنین بدلیل اینکه ویندوز تا بحال از اکانت آنلاین استفاده میکرده است و اکانت Administrator Local اولین بار است که فعال میشود صفحه Welcome Screen ویندوز برای اعمال تنظیمات اولیه باز میشود.
	1. ![[Pasted image 20240626161727.png]]
#### Bypassing Windows Password using `KonBoot` - E12
##### Definitions & Instructions
###### What is KonBoot?
ابزار KonBoot یکی از بهترین و ساده ترین ابزار ها برای دور زدن پسورد های ویندوز و همچنین پسورد های مک است.
بر خلاف سایر ابزار ها که تابحال توضیح دادیم،  KonBoot پسورد اکانت های فعلی را تغییر و یا ریست  نمیکند، و در واقع پس از راه اندازی مجدد سیستم به حالت قبلی خود باز میگردد و اینکار فرآیند Attack و کرک اکانت را غیر قابل تشخیص و پیگیری میکند.
ابزار  KonBoot یک ابزار غیر رایگان است و نسخه رایگان آن(ورژن 1.1) ویندوز های 10 و 11 را پشتیبانی نمیکند:
	![[Pasted image 20240626162442.png]]
> ابزار  KonBoot، ابزاری بسیار حرفه ایست که در سطح نظامی، سازمان های دادگستری و قضایی، متخصصان IT & Security و همچنین متخصصان جرم شناسی Forensic Experts استفاده میشود.
> از مزیت های KonBoot این است میتوان پسورد اکانت های ماشین های Mac را نیز بوسیله این ابزار Bypass کنیم.

**این ابزار برای در دو نسخه Bios و UEFI میتواند کار کند، اما در UEFI در ویندوز های 10 یا 11 بدرستی کار نمیکند.**
###### Instructions Steps
برای نصب KonBoot بر روی USB بصورت Bootable ابتدا باید تمام حافظه های USB که اضافه به ماشین متصل هستند را از ماشین جدا کنیم و فقط USB Drive که میخواهیم KonBoot بر روی آن نصب شود را به ماشین متصل میکنیم:
0. Download or Purchase tool from official website
	1. https://kon-boot.com/
		1. ![[Pasted image 20240626162937.png]]
1. Navigate to `konboot/USB` folder and run the following file as Administrator
	1. `usb_install_RUNASADMIN.bat`
		1. ![[Pasted image 20240626163209.png]]
2. Detach all Unnecessary USB Drives except the Target USB for install KonBoot
	1. ![[Pasted image 20240626163414.png]]
3. `Restart` machine and `Boot` from `KonBoot`
4. *KonBoot Automatically Bypass the Password*
	1. به محض بوت شدن ماشین با KonBoot، ابزار بصورت خودکار پسورد اکانت ها را Bypass میکند و دیگر نیازی به انجام کار دیگری نداریم.
##### Practical Demo
1. دانلود و یا خرید ابزار KonBoot از وبسایت رسمی
	1. ![[Pasted image 20240626164137.png]]
2. حافظه USB که میخواهیم KonBoot بر روی آن نصب شود را Format میکنیم(Fat32 on 8192)
	1. ![[Pasted image 20240626164246.png]]
3. به پوشه دانلود شده ابزار `KonBootv/Kon_Bootv2.4` میرویم و سپس به پوشه `kon-bootUSB` میرویم:
	1. ![[Pasted image 20240626164434.png]]
4. حال فایل `usb_install_RUNASADMIN.bat` را با دسترسی Administrator اجرا میکنیم.
	1. ![[Pasted image 20240626164541.png]]
5. حال KonBoot میگوید تمامی حافظه های USB را از ماشین Detach کنید به غیر از حافظه ای که میخواهید KonBoot بر روی آن نصب شود.
	1. ![[Pasted image 20240626164650.png]]
6. حال اطلاعات دیسک را که KonBoot میخواهد در آن نصب شود را در پیام نمایش داده شده تایید میکنیم:
	1. ![[Pasted image 20240626164749.png]]
7. ابزار KonBoot با موفقیت بر روی حافظه USB نصب شده است و فایل های زیر هم درون فلش دیده میشود:
	1. ![[Pasted image 20240626164856.png]]
8. حال ماشین را خاموش میکنیم تا ماشین را با KonBoot بوت کنیم، نکته اینجاست قبل از اینکار باید `Secure Boot` را در تنظیمات بایوس `Turn Off` کنیم.
	1. ![[Pasted image 20240626165102.png]]
9. به محض بوت شدن ماشین با KonBoot، ابزار بصورت خودکار و سایلنت شروع به bypassing پسورد ماشین میکند و نیازی به هیچگونه Interaction از طرف ما نیست
	1. ![[Pasted image 20240626165257.png]]
10. حال میتوانیم به تمام اکانت های ماشین با پسورد خالی Blank لاگین کنیم:
	1. ![[Pasted image 20240626165354.png]]
#### Bypassing Windows Password using `HIREN'S Boot CD` - E13
##### Definitions & Instructions
###### What is Hiren Boot CD?
ابزار Hiren Boot یک جایگزین کاملا رایگان برای KonBoot بشمار میرود که میتواند پسورد ویندوز را Bypassing کند. این ابزار در قالب فایل ISO عرضه میشود که این فایل بر اساس Windows 10 PE x64 کار میکند که علاوه بر bypassing پسورد ویندوز، ابزار های دیگری دارد که برای رفع مشکلات Troubleshooting ویندوز میتوان از آنها استفاده کرد.
	![[Pasted image 20240626172628.png]]
> در واقع میتوان گفت *Hiren Boot CD* یک `Bypassing Password` است که ابزار هایی برای رفع مشکلات ویندوز `Repair Windows Problems`  هم دارد.

- از ورژن های جدید Hiren Boot میتوانیم در نسخه های UEFI ویندوز استفاده کنیم و برای نسخه های قدیمی BIOS باید از ورژن های قدیمی ابزار استفاده کنیم.
###### Scenario Schema
فرض کنید به ماشینی ویندوزی که `Password Locked` است دسترسی داریم، در اینجا با استفاده از  Hiren Boot  میتوانیم بصورت سریع پسورد اکانت را Bypass کنیم.
	![[Pasted image 20240626172737.png]]
###### Instructions Steps
0. Download Hiren Boot & Rufus from official websites
	1. https://www.hirensbootcd.org/
		1. ![[Pasted image 20240626172911.png]]
	2. https://rufus.ie/en/ *Download Portable Version*
		1. ![[Pasted image 20240626173008.png]]
1. Run Rufus, Select Hiren Boot CD ISO file and Select USB Drive to make the USB Disk Bootable
	1. ![[Pasted image 20240626173311.png]]
2. Boot machine with Hiren Boot USB, you may need to `Turn off Secure Boot` from `BIOS` Settings
	1. ![[Pasted image 20240626173447.png]]
3. Now machine booted with Hiren Boot
	1. در واقع هنگامیکه ماشین را با Hiren Boot بالا میاوریم مانند این است که یک *Windows 10 PE x64* را بصورت *Live* بالا آوردیم
	2. در این ویندوز لایو ابزار های زیادی برای استفاده وجود دارند که برای کرک پسورد ما از `NT Password Edit` استفاده میکنیم.
		1. ![[Pasted image 20240626173727.png]]
4. `Hiren Boot => Search & Open => NT Password Edit`
	0. ابزار Hiren Boot برای Bypassing پسورد از ابزار `NT Password Edit` استفاده میکند که هسته آن `chntpw` است که یک `GUI` برای راحت تر شدن استفاده از آن بر روی آن سوار شده است.
	2. `Open` First Open SAM Files
	3. `Select User` to be unlock or changes password
		1. ![[Pasted image 20240626173941.png]]
	4. حال برای تغییر پسورد اکانت بر روی `Change Password` کلیک میکنیم.
	5. برای آنلاک کردن اکانت هم بر روی `Unlock` کلیک میکنیم.
6. `NT Password Edit => Change Password`
	0. پس از انتخاب یوزر و کلیک بر روی Change Password پنجره جدید باز میشود که پسورد جدید را میخواهد. میتوانیم با خالی گذاشتن این دو فیلد پسورد اکانت را blank کنیم.
	1. بنابراین در پنجره باز شده در هر دو فیلد مقداری وارد نمیکنیم و بر روی OK کلیک میکنیم:
		1. ![[Pasted image 20240626174533.png]]
	2. همچنین اگر اکانت Administrator قفل باشد در این جا با انتخاب آن و سپس کلیک بر روی unlock میتوانیم اکانت را باز کنیم.
		1. ![[Pasted image 20240628194451.png]]
7. Restart machine and login windows with account without password
	1. کافیست ماشین را ریستارت کنیم تا بدون نیاز به وارد کردن پسورد بتوانیم با اکانت مورد نظر به ویندوز لاگین کنیم.
##### Practical Demo
0. ساخت USB Bootable از Hiren Boot CD و بوت کردن ماشین با آن
	1. ابتدا فایل ISO ابزار Hiren Boot CD را از وبسایت رسمی با حجم 2.4Gb دانلود میکنیم. 
		1. ![[Pasted image 20240626175048.png]]
	2. سپس نرم افزار Rufus Portable را نیز دانلود میکنیم.
		1. ![[Pasted image 20240626175305.png]]
	3. حال یک حافظه USB را با فایل Hiren Boot CD ISO با استفاده از نرم افزار Rufus بصورت Bootable در میاوریم. 
		1. طرح Scheme پارتیشن باید `MBR` باشد.
		2. از فایل سیستم `NTFS in 4096bytes Cluster` استفاده شود.
			1. ![[Pasted image 20240626175459.png]]
		3. پس از Bootable شدن فلش فایل های زیر باید در فلش موجود باشند:
			1. ![[Pasted image 20240626175607.png]]
	4. کافیست حافظه USB را به ماشین متصل کنیم، ماشین را خاموش کنیم و سپس آنرا با Hiren Boot CD بالا بیاوریم.
		1. ![[Pasted image 20240626175710.png]]
1. کارهایی که باید در ویندوز Hiren Boot انجام دهیم به شرح زیر است:
	1. در ابتدا ابزار `NT Password Edit` را جستجو و سپس باز میکنیم.
		1. ![[Pasted image 20240626175854.png]]
	2. در ابزار باز شده ابتدا بر روی `Open` کلیک میکنیم تا محتویات فایل SAM بصورت خودکار واکشی شود:
		1. ![[Pasted image 20240626175959.png]]
	3. یوزر `Administrator` را انتخاب کرده و بر روی `Change Passwords` کلیک میکنیم:
		1. ![[Pasted image 20240626180055.png]]
	4. در پنجره باز شده، دو فیلد `Password, Verify Password` را خالی میگذاریم تا پسورد اکانت Empty شود.
		1. ![[Pasted image 20240626180353.png]]
	5. در آخر برای ذخیره تغییرات بر روی `Save Changes` کلیک میکنیم و سپس از ابزار خارج میشویم. 
	6. *نکته:* اگر ویندوز از اکانت آنلاین مانند ایمیل برای لاگین استفاده میکند، برای bypassing آن میتوانیم ابتدا اکانت Local Administrator را انتخاب کنیم و سپس بر روی `Unlock` کلیک کنیم.
2. خاموش کردن Hiren Boot Windows و بالا آوردن ماشین با ویندوز اصلی
	1. سپس هم Windows Hiren Boot را خاموش میکنیم و ماشین را با ویندوز اصلی بالا میاوریم.
	2. میتوانیم بدون نیاز به وارد کردن پسورد با اکانت `Administrator` به ویندوز لاگین کنیم.
#### Bypassing Windows Password using `Windows Boot Disk` - E14
##### Definitions & Instructions
###### Definitions
- دیسک Windows Boot Disk یک روش ساده برای دور زدن پسورد اکانت و گرفتن دسترسی به ماشین ارائه میدهد. در این روش برای حمله میتوانیم از تمامی دیسک های ISO نصب ویندوز (Win 10/11) استفاده کنیم.
- در واقع با این روش پسورد اکانت در ویندوز های 10 یا 11 را میتوانیم ریست کنیم.
	![[Pasted image 20240626181515.png]]
###### Scenario Schema
فرض کنید به ماشینی ویندوزی که `Password Locked` است دسترسی داریم، در اینجا با استفاده از  Windows Boot Disk میتوانیم بصورت سریع پسورد اکانت را Bypass کنیم.
	![[Pasted image 20240626172737.png]]
###### Instructions Steps
1. Download 
	1. Windows 10 or 11 Install Disk - ISO File
	2. Rufus Portable
2. Make Bootable USB from ISO file
	1. ![[Pasted image 20240626181848.png]]
3. Plug USB and Reboot machine with this
	1. ![[Pasted image 20240626181929.png]]
4. Once windows setup start, Click on `Repair Your Computer`
	1. ![[Pasted image 20240626182010.png]]
5. `Repair Your Computer => Troublshoot => Advanced Options => Command Prompt`
	1. ![[Pasted image 20240626182057.png]]
	2. ![[Pasted image 20240626182137.png]]
6. Now we need Windows Drive available for be Manipulation, So Use `Diskpart` to assign letter to windows drive
	1. در این مرحله نیاز داریم که به درایو که ویندوز در آن نصب است برویم، برای اینکار ابتدا باید حرف درایو را مشخص کنیم که برای اینکار از کامند `Diskpart` استفاده میکنیم. 
	2. در واقع در ابتدا باید درایو های ماشین را لیست کنیم، سپس درایو که ویندوز بر روی آن نصب است را انتخاب کنیم و در آخر حرف مشخص مثلا `C` را به آن درایو اختصاص دهیم.
	3. برای اینجام اینکار اید دستورات را به ترتیبی که در تصویر مشاهده میکنید اجرا کنیم.
		1. ![[Pasted image 20240626182450.png]]
```powershell
DISKPART #Start Disk Part Utility
LIST VOLUME #List all available disk drives
SELECT VOLUME 1 #Choose Windows Drive(Choose based on your Windows Drive)
ASSIGN LETTER C #Assign Letter C to Windows Drive
exit
```
	![[Pasted image 20240626182729.png]]
7. Now Rename `C:/Windows/System32/utilman.exe`(Accessibility Tools) to some other name and then Copy `cmd.exe` as `utilman.exe`
	1. اگر مشاهده کرده باشید در صفحه Lock Screen ویندوز ، آیکون Accessibility Tools را مشاهده میکنید که در واقع فایل `utilman.exe` را اجرا میکند.
	2. حال با این ترفند فایل `cmd.exe` را با این فایل جابجا میکنیم تا در Lock Screen ویندوز، با کلیک بر روی  آیکون `Accessibility Tools` در واقع `CMD` باز شود.
	3. برای اینکار ابتدا باید فایل `utilman.exe` را به نام دیگری تغییر دهیم، سپس فایل `cmd.exe` را به نام `utilman.exe` تغییر دهیم و یا آنرا بجای `utilman.exe` کپی کنیم. برای اینکار دستورات زیر را باید اجرا کنیم:
		1. ![[Pasted image 20240626183553.png]]
```powershell
X:\> cd C:\Windows\System32
C:\Windows\System32> ren utilman.exe utilman1.exe
C:\Windows\System32> copy cmd.exe utilman.exe

#if cd command not working rename and copy files directly
ren C:\Windows\System32\utilman.exe utilman2.exe
copy C:\Windows\System32\cmd.exe C:\Windows\System32\utilman.exe
```
	![[Pasted image 20240626183616.png]]
	![[Pasted image 20240627201058.png]]
8. Now Remove USB & Reboot System on Main Windows. in Lock Screen Click on `accessibility icon` in the right corner of screen and then `Command Prompt` will be Appear
	1. حال کافیست ویندوز اصلی را بالا بیاوریم و در صفحه Lock Screen بر روی `accessibility icon` کلیک کنیم تا CMD باز شود.
		1. ![[Pasted image 20240626183906.png]]
2. Now run the following commands to reset the password of a user account
	1. برای حذف پسورد یوزر ها کافیست کامند های زیر را به ترتیب اجرا کنیم:
		1. ![[Pasted image 20240626184046.png]]
	2. از کامند `net user` برای لیست کردن یوزر ها و از کامند `* net user administrator ` برای حذف پسورد اکانت استفاده میکنیم.
	3. در واقع با اجرای کامند `* net user administrator ` پسورد جدید اکانت پرسیده میشود که میتوانیم آنرا خالی بگذاریم.
```powershell 
net user
net user administrator *
```
	![[Pasted image 20240626184244.png]]
10. `If` Windows `have Online Account` for Authentication, we can also `Add New User` by run the following Commands
	1. اگر ویندوز با اکانت آنلاین احراز هویت شود میتوانیم یک یوزر محلی جدید اضافه کنیم تا با استفاده از آن بتوانیم به ویندوز مورد نظر بدون داشتن پسورد لاگین کنیم.
	2. با استفاده از کامند `net user USERNAME PASSWORD -add` یک یوزر جدید اضافه میکنیم.
	3. سپس برای بالا بردن دسترسی یوزر با استفاده از کامند `net localgroup administrators USERNAME -add` آنرا به گروه `Administrators` اضافه میکنیم.
	4. برای اینکار باید دستورات زیر را به ترتیبی که در تصویر میبینید اجرا کنیم:
		1. ![[Pasted image 20240626184636.png]]
10. Step 10 Commands =>
```powershell
net user USERNAME PASSWORD /add #Add new User
net localgroup administrators USERNAME /add #Add new User to Administrators Group

net user davoodya 12945 /add
net localgroup administrators davoodya /add
```
	![[Pasted image 20240626185708.png]]
##### Practical Demo
0. ساخت فلش Bootable از فایل ISO نصب ویندوز
	1. دانلود فایل ISO نصب ویندوز 10 یا ویندوز 11
	2. دانلود Rufus Portable و اجرای آن
	3. تنظیمات Rufus برای ساخت فلش بوتیبل
		1. اگر ماشین هدف سخت افزار نسل جدید است میتوانیم پارتیشن را `GPT` انتخاب کنیم:
			1. ![[Pasted image 20240626195404.png]]
	4. بر روی OK کلیک میکنیم تا فرآیند شروع شود.
1. بوت کردن ویندوز با Windows Installation USB Disk
	1. ماشین را ریستارت میکنیم و سپس آنرا با USB Disk که فایل نصب ویندوز در آن است بوت میکنیم.
	2. سپس در صفحه نصب ویندوز `Repair your Computer` را انتخاب میکنیم و به مسیر زیر میرویم:
		1. ![[Pasted image 20240626195636.png]]
	3. `Troubleshoot => Advanced Options => Command Prompt`
2. ابتدا باید در CMD بوسیله کامند `DISKPART` به درایو که ویندوز بر روی آن نصب است حرفی را اختصاص دهیم.
```powershell
DISKPART
DISKPART> LIST VOLUME
DISKPART> SELECT VOLUME 0
DISKPART> ASSIGN LETTER C
DISKPART> EXIT
x:\Sources>c:
C:\>
```
	![[Pasted image 20240626200208.png]]
3. حال به پوشه `C:/Windows/System32/` میرویم تا عملیات جابجای CMD با utilman را انجام دهیم:
```powershell
X:\Sources>c:
C:\> cd windows\system32
C:\Windows\System32> ren utilman.exe utilmanold.exe
C:\Windows\System32> copy cmd.exe utilman.exe
```
	![[Pasted image 20240626200649.png]]
4. اگر کامند CD بطور مستقیم کار نکرد میتوانیم عملیات Rename و Copy را بطور مستقیم استفاده کنیم:
```powershell
#if cd command not working rename and copy files directly
ren C:\Windows\System32\utilman.exe utilman2.exe
copy C:\Windows\System32\cmd.exe C:\Windows\System32\utilman.exe
```
5. حال کافیست CMD را ببندیم و ماشین را Shutdown کنیم و سپس ماشین را با ویندوز اصلی بالا بیاوریم.
	1. ![[Pasted image 20240626200751.png]]
2. حال در پنجره Lock Screen بر روی آیکون Accessibility کلیک میکنیم تا CMD باز شود:
	1. ![[Pasted image 20240626200857.png]]
3. پس از باز شدن CMD کامند های زیر را برای برداشتن پسورد و یا عوض کرن پسورد اکانت وارد میکنیم:
```powershell
net user 
net user Administrator *
Type Password for user: 12945
Retype Password for user: 12945
```
	![[Pasted image 20240626201050.png]]
7. حال میتوانیم با یوزر Administrator و پسورد 12945 به ویندوز لاگین کنیم.
8. اگر در ویندوز اکانت آنلاین فعال بود و میخواستیم آنرا دور بزنیم باید یوزر جدید اضافه کنیم و سپس نیز آنرا به گروه Administrators اضافه کنیم. برای اینکار کامندهای زیر را به ترتیب وارد کنیم:
```powershell
net user davoodya 12945 /add
net localgroup administrators davoodya /add
```
9. با اینکار یوزر Local جدید بنام `davoodya` ایجاد کردیم که در گروه `Administrators` محلی هم قرار دارد و میتوانیم با پسورد `12945` به این اکانت لاگین کنیم.
### Resetting Windows Password
#### Reset Windows Password by Kali & `chntpw` - E10
##### Instruction & Definition
###### Usage Scenario
این روش در سناریو زیر کاربرد دارد:
- فرض کنید به ماشین ویندوزی به Password Locked است دسترسی فیزیکی داریم. در این روش میخواهیم با استفاده از Kali Live boot پسورد اکانت ویندوز را حذف کنیم تا بتوانیم دسترسی را به ماشین ویندوزی بگیریم:
	- ![[Pasted image 20240626150927.png]]
- بنابراین در این سناریو به Kali Live boot USB نیاز داریم.
###### `chntpw` Command Flags
این ابزار را در قالب کامند هم در کالی لینوکس میتوانیم اجرا کنیم. سوئیچ هایی که این کامند میتواند داشته باشد را در تصویر زیر میتوان مشاهده کرد:
	![[Pasted image 20240627235237.png]]
از مهمترین آنها `l-` برای لیست کردن یوزر ها و `u-` که برای ادیت یک یوزر بصورت Interactive استفاده میشود:
```sh
cd kali/media/WINDOWSDRIVE/Windows/System32/config
chntpw -h
chntpw -l SAM
chntpw -u Administrator SAM
```
###### Instructions Steps
1. Plug Kali Live USB to machine and boot from this.
	1. ![[Pasted image 20240626151233.png]]
2. After Live Kali is UP, Open drive contains windows installation files and Open it as root
	1. پس از بالا آمدن ماشین کالی لایو، به درایو که فایل های نصب ویندوز قرار دارد میرویم و سپس به محل ذخیره سازی فایل SAM(Security Account Manager) میرویم:
	2. `cd /media/kali/[WINDOWS-DRIVE]/Windows/System32/config`
	3. سپس در این دایرکتوری، کلیک راست میکنیم و `Open as Root` را میفشاریم:
		1. ![[Pasted image 20240626151803.png]]
3. Now Open Terminal in `/Windows/System32/config` directory and run following commands
	1. میدانیم فایل دیتایس SAM حاوی تمام اکانت های ماشین ویندوزی به همراه متن هش شده پسورد آنهاست.
	2. `chntpw -i SAM`
	3. `-i` => Open utility in Interactive mode
		1. ![[Pasted image 20240626152154.png]]
4. *Now select option to edit users accounts*
	1. حال منو اصلی `chntpw` که در سناریو قبل هم با آن کار کردیم باز میشود و باید عملیاتی که میخواهیم بر روی یوزر های درون SAM انجام شود را انتخاب کنیم.
	2. در اینجا ما `Edit user data and passwords` را انتخاب میکنیم:
		1. ![[Pasted image 20240626152519.png]]
5. *The utility list all accounts on the SAM file*
	1. ابزار *chntpw* تمام اکانت های درون فایل SAM را لیست میکند و برای انتخاب اکانت کافیست `RID(Respective ID)` اکانت را وارد کنیم:
		1. ![[Pasted image 20240626152801.png]]
6. *Select Options to clear passwords*
	1. حال عملیاتی که میخواهیم بر روی یوزر صورت گیرد را انتخاب میکنیم، که چون ما میخواهیم پسورد را حذف کنیم `Clear(Blank) User Password` را انتخاب میکنیم:
		1. ![[Pasted image 20240626153024.png]]
	2. همچنین میتوانیم اکانت Administrator را انتخاب کنیم و سپس Unlock Account را بر روی آن انجام دهیم.
7. Now Quit, Save Changes, Remove USB and Restart PC
	1. حال با فشردن `q` از ابزار خارج میشویم و با فشردن `y` تغییرات انجام شده را ذخیره میکنیم.
	2. پس از آن هم حافظه را از ماشین در میاوریم و یکبار ماشین را ریبوت میکنیم.
		1. ![[Pasted image 20240626153325.png]]
8. Now in Next Login we can see Ammar Accounts Password will be Removed.
##### Demo
0. ماشین ویندوزی را با Live Kali USB بوت میکنیم.
1. به درایوی که ویندوز در آن نصب است میرویم:
	1. ![[Pasted image 20240626153638.png]]
2. سپس به پوشه `Windows/System32/config` میرویم، در فضای خالی کلیک راست و `Open as Root` را میفشاریم.
	1. ![[Pasted image 20240626153836.png]]
3. در همان فولدر راست کلیک و `Open Terminal here` را میفشاریم.
	1. ![[Pasted image 20240626153951.png]]
4. حال باید `chntpw` را بصورت Interactive بر روی فایل SAM اجرا کنیم. گزینه ها را به شرح زیر تنظیم میکنیم:
	1. `chntpw -i SAM`
	2. *Type* `1` => Edit user data and passwords
		1. ![[Pasted image 20240626154304.png]]
	3. *Type User RID* `01f4` => Select Administrator Account
		1. ![[Pasted image 20240626154414.png]]
	4. *Type*  `1` => Clear(Blank) user passwords
		1. ![[Pasted image 20240626154514.png]]
	5. پسورد در این مرحله ریست میشود اما نوتیفیکیشن نمایش داده نمیشود.
		1. ![[Pasted image 20240626154610.png]]
	6. *Type* `q` => Quit Editing User
	7. *Type* `y` => Save Hive Changes
		1. ![[Pasted image 20240626154744.png]]
5. حال Kali را `Shutdown` میکنیم و ماشین Windows را بالا میاوریم و مشاهده میکنیم *Administrator* بدون نیاز به وارد کردن پسورد میتواند به ویندوز لاگین کند.
#### Reset Windows Password with `Lazesoft` - E15
##### Definitions & Instructions
###### Definitions
اگر پسورد ویندوز را فراموش و یا گم کردیم با استفاده از این ابزار براحتی میتوانیم پسورد ویندوز را بازگردانیم. این ابزار همچنین میتوانیم Key کلید CD Windows را نیز بدست بیاوریم.
	![[Pasted image 20240627155949.png]]
- نسخه های قدیمی این ابزار بر روی Bios یعنی ویندوز های 7 الی 10 کار میدهد، اما نسخه های جدید ابزار را میتوان در UEFI یعنی ویندوز های 10 الی 11 هم اجرا کرد.
- همچنین این ابزار در مجموعه Hire Boot CD 2024 ورژن جدید UEFI موجود است  که میتوان از آن استفاده کرد.
###### Usage Scenario 
فرض کنید به ماشینی ویندوزی که `Password Locked` است دسترسی داریم، در اینجا با استفاده از Lazesoft میتوانیم بصورت سریع پسورد اکانت را Bypass کنیم و یا اکانتی را مثلا Local Administrator را `Unlock` کنیم.
	![[Pasted image 20240626172737.png]]
###### Instruction Steps
0. Download Lazesoft
	1. https://www.lazesoft.com/
		1. ![[Pasted image 20240627160143.png]]
1. Install Lazesoft & Run it.
	1. Choose Your Target OS
		1. ![[Pasted image 20240627160244.png]]
2. Select `USB Flash` Drive & Click `Start` to make it bootable with Lazesoft
	1. ![[Pasted image 20240627160401.png]]
3. Reset machine & Booting machine with USB Flash
	1. ![[Pasted image 20240627160446.png]]
4. *Now Machine booted with `Lazesoft` =>*
	1. First choose `Reset Windows Password` 
		1. ![[Pasted image 20240627160552.png]]
	2. Then `Select Windows Drive` and Choose `Reset Local Password` 
		1. ![[Pasted image 20240627160722.png]]
	3. Lazesoft listed all accounts on machine, `Choose Target Account` and click `Next`
		1. ![[Pasted image 20240627160830.png]]
	4. Now click on `RESET/UNLOCK` to reset password, then click `Finish`
		1. ![[Pasted image 20240627161023.png]]
5. *Get Windows Product Key*
	1. با استفاده از Lazesoft میتوانیم Key ثبت شده ویندوز را بدست بیاوریم.
	2. در واقع میتوانیم یک ویندوز Original پیدا کنیم و آنرا با Lazesoft بوت کنیم، سپس ابزار Lazesoft `Password Recovery` را باز کنیم. این بار بجای انتخاب Reset Password گزینه `Find Windows Product key` را انتخاب میکنیم:
		1. ![[Pasted image 20240628200503.png]]
	3. کافیست بر روی `Next` کلیک کنیم تا Key Windows را مشاهده کنیم:
		1. ![[Pasted image 20240628200701.png]]
##### Practical Demo
1. *دانلود و نصب نسخه Password Recovery از مجموعه Lazesoft*
	1. https://www.lazesoft.com/download.html
	2. Download Lazesoft Recover My Password Home Edition
		1. ![[Pasted image 20240627161437.png]]
	3. Install Lazesoft & Launch it
		1. ![[Pasted image 20240627161600.png]]
2. *ساخت دیسک Bootable از Lazesoft Password Recovery*
	1. نرم افزار را اجرا میکنیم و بر روی `Burn Bootable CD/USB Disk Now` کلیک میکنیم:
		1. ![[Pasted image 20240627161722.png]]
	2. در پنجره بعدی سیستم عامل تارگت را انتخاب میکنیم و بر روی `Next` کلیک میکنیم.
		1. ![[Pasted image 20240627161829.png]]
	3. در پنجره بعدی، در فیلد `USB Flash` هم حافظه USB که میخواهیم Bootable شود را انتخاب میکنیم. متیوانیم بر روی Virtual ISO و یا CD/DVD هم نرم افزار را نصب کنیم.
		1. ![[Pasted image 20240627161952.png]]
	4. هنگامیکه بر روی `Start` کلیک میکنیم، ابزار بصورت خودکار یکسری از فایل هایی که نیاز دارد را دانلود میکند و سپس فلش دیسک را نرم افزار Lazesoft بصورت Bootable در می آورد.
		1. ![[Pasted image 20240627162124.png]]
	5. بر روی `Finish` کلیک کنید و خارج شوید.
3. *بوت کردن ماشین با Lazesoft*
	1. ماشین را ریستارت میکنیم.
	2. دقت کنید Secure boot غیر فعال باشد.
	3. کافیست ماشین را با Removable Media حافظه USB بوت کنیم.
	4. حال ابزار Lazesoft با موفقیت بالا آمد:
		1. ![[Pasted image 20240627162423.png]]
4. *بازگردانی پسورد با Lazesoft*
	1. هنگامیکه Lazesoft بالا آمد، در پنجره `Lazesoft Recover My Password Home` گزینه `Reset Windows Password` را انتخاب میکنیم و بر روی `Next` کلیک میکنیم.
		1. ![[Pasted image 20240627162614.png]]
	2. در پنجره بعدی، درایو که ویندوز بر روی آن نصب شده است را انتخاب میکنیم و سپس بر روی `Reset Local Password` کلیک کرده و `Next` را میفشاریم :
		1. ![[Pasted image 20240627162723.png]]
	3. در پنجره بعدی هم یوزری که میخواهیم پسورد آنرا بازیابی کنیم انتخاب میکنیم و بر روی `Next` کلیک میکنیم.
		1. ![[Pasted image 20240627162842.png]]
	4. در پنجره آخر هم بر روی `RESET/UNLOCK` کلیک میکنیم تا پسورد اکانت ریست شود و سپس عملیات را `Finish` میکنیم.
		1. ![[Pasted image 20240627162951.png]]
	5. حال کافیست Lazesoft را Shutdown کنیم و ماشین را با ویندوز اصلی بالا بیاوریم:
		1. ![[Pasted image 20240627163057.png]]
5. هنگامیکه ماشین را با ویندوز اصلی خود بالا می آوریم، میتوانیم با یوزر `Administrator` بدون نیاز به وارد کردن پسورد لاگین کنیم.
### !