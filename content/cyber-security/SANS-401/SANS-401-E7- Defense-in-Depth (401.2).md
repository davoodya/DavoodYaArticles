+++
title = "SANS-401-Defense-in-Depth (401.2)"
slug = "sans-401-defense-in-depth-4012"
date = "2026-02-09T09:59:19+03:30"
lastmod = "2026-02-09T09:59:19+03:30"
draft = false

categories = ["SANS-401"]
tags = ["SANS-401", "CyberSecurity", "Pentest"]
series = ["SANS-401"]

description = "- Definitions - Whats Defense-in-Depth? - Key Focus of Risk - Access Controlling - Access Control Parameters - Access Control Techniques - Managing..."
keywords = ["SANS-401-Defense-in-Depth (401.2)", "SANS-401", "CyberSecurity", "Pentest", "sans-401-e7-defense-in-depth-4012"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/SANS-401/sans-401-defense-in-depth-4012/"

featured_image = "/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-1.png"
images = ["/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-1.png"]

[params.opengraph]
  title = "SANS-401-Defense-in-Depth (401.2)"
  description = "- Definitions - Whats Defense-in-Depth? - Key Focus of Risk - Access Controlling - Access Control Parameters - Access Control Techniques - Managing..."
  image = "/images/cyber-security/SANS-401-Defense-in-Depth(401.2"
  url = "https://davoodya.ir/SANS-401/sans-401-defense-in-depth-4012/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "SANS-401-Defense-in-Depth (401.2)"
  description = "- Definitions - Whats Defense-in-Depth? - Key Focus of Risk - Access Controlling - Access Control Parameters - Access Control Techniques - Managing..."
  image = "/images/cyber-security/SANS-401-Defense-in-Depth(401.2"

readingTime = 8
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
+++

-------

### Definitions
#### Whats Defense-in-Depth?
دفاع در عمق و یا Defense-in-Depth بدین معناست که برای Security Solution که میخواهیم استفاده کنیم باید >>
1. دارای چندین لایه امنتیی باشد که اگر یکی از لایه ها از کار افتاد و یا مورد حمله قرار گرفت لایه های دیگر بتوانند عملیات دفاع را انجام دهند.
2. مقابله کردن با حملات بسیار عالیست، اما شناسایی آنها بهتر است. نکته اینجاست شناسایی بدون واکنش کمترین ارزش را دارد. 
	1. بنابراین در Security Solution ما باید شناسایی بالاترین اهمیت را داشته باشد.
	2. هر شناسایی که صورت گرفت باید بلافاصله واکنشی مناسب با آن انجام شود.
	3. برنامه برای مقابله و مسدود کردن حملات بلافاصله پس از شناسایی حمله از مزیت های Solution است که میخواهد Defense-in-Depth را عرضه کند.
3. *تصویر:*
	1. ![SANS-401-Defense-in-Depth (401.2)-1](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-1.png)
#### Key Focus of Risk
در مبحث Defense-in-Depth هم رعایت مثلث *CIA(Confidentiality, Integrity, Availability)* از واجبات است و بر حسب هر پروژه میتوان ضریب هر ضلع را افزایش و کاهش داد:
	![SANS-401-Defense-in-Depth (401.2)-2](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-2.png)
- *Confidentiality*
	- محرمانه بودن اطلاعات برای جلوگیری از دسترسی های غیر مجاز
- *Integrity*
	- حفظ یکپارچگی اطلاعات برای جلوگیری از دستکاری شدن آنها
- *Availability*
	- میزان در دسترس بودن داده ها برای جلوگیری از دسترسی های غیر مجاز 
### Access Controlling
#### Access Control Parameters
برای کنترل دسترسی ها باید سه پارامتر زیر را در نظر داشته باشیم:
1. Identity
	1. شخصی که میخواهد دسترسی داشته باشد باید شناسایی شود.
2. Authentication
	1. شخصی که میخواهد دسترسی داشته باشد باید احراز هویت شود.
3. Authorization
	1. شخصی که میخواهد دسترسی داشته باشد باید سطح دسترسی و مجوز های دسترسی او او مشخص شود.
در واقع یوزرهای که میخواهند دسترسی به یک فایل یا فولدر دسترسی داشته باشند باید ابتدا شناسایی شوند و سپس نیز احراز هویت شوند. پس از آن باید سطح دسترسی که میتوانند داشته باشند را مشخص کنیم.
#### Access Control Techniques
تکنیک های کنترل و مدیریت دسترسی به شرح زیر است:
1. Discretionary(DAC)
	1. در اینجا احراز هویت را یوزر ها انجام میدهند.
2. Mandatory(MAC)
	1. نیاز به Match بودن classification دارد.
3. Role Based(RBAC)
	1. بر اساس عضویت در گروه ها و تنظیم دسترسی بر روی گروه ها
4. Ruleset- based(RSBACK)
	1. در این روش برای هر object خاص قانون مربوط مینویسیم.
5. List Based
	1. در این روش لیستی نوشته میشود که دسترسی هر Object در آن لیست مشخص میشود.
6. Token Based
	1. در این روش لیستی نوشته میشود که دسترسی هر Principle در آن لیست مشخص میشود.
7. Image
	1. ![SANS-401-Defense-in-Depth (401.2)-3](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-3.png)
#### Managing Access
پس از انتخاب تکنیک مناسب باید یوزر ها در دسته های زیر دسته بندی کنیم:
1. Account Administration
	1. بالاترین سطح دسترسی را این گروه دارد که یوزر هایی که مدیر سیستم هستند در آن قرار دارند.
2. Maintenance
	1. اکانت هایی که میخواهیم بتوانند ارور ها و مشکلات مربوط در سیستم ها و شبکه را بررسی و رفع کنند در این دسته قرار میگیرند.
	2. کاربران این دسته کمک مدیر های این سازمان هستند.
3. Monitoring
	1. این دسته که وظیفه نظارت را بر عهده دارند باید مجوز های نظارت یا Auditing، تعیین سطح دسترسی ها authorization، دیدن خطاها failures را داشته باشد.
4. Revocation
	1. برای این گروه که شامل یوزر های استفاده کننده است باید تمام دسترسی های غیر لازم را برداریم و فقط دسترسی هایی که نیاز دارند مانند read, write برای آنها در موقع نیاز صادر شود.
	2. اینکار اصولا بوسیله تیم Monitoring انجام میشود.
5. *Image:*
	1. ![SANS-401-Defense-in-Depth (401.2)-4](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-4.png)
#### Single-Sign-On (SSO)
*از این تکنیک برای احراز هویت کاربران و مدیریت آن استفاده میشود که یکی از بهترین روش ها هم محسوب میشود:*
- در این روش یوزر با یکبار لاگین میتواند به تمام سرویس های آن مجموعه دسترسی داشته باشد.
- مدیریت یوزر ها در این روش بسیار انعطاف پذیری بیشتری دارد.
- در این روش Credential وارد شده یوزر فقط یکبار اعتبار دارد و ذخیره هم نمیشود.
- این روش را میتوانیم با Multi-Factor-Authentication هم پیاده سازی کنیم.
- *تصویر:*
	- ![SANS-401-Defense-in-Depth (401.2)-5](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-5.png)
### Password Management
#### Whats Password Cracking?
با استفاده از ابزار های کرک پسورد مانند John the Ripper و یا استفاده از روش های کرک پسورد مانند Rainbow Table میتوانیم پسورد هایی که بصورت plain text و یا hash شده ذخیره شده اند را کرک کنیم. 
این کرک میتواند براساس Wordlist و یا بصورت کور Bruteforce باشد.
	![SANS-401-Defense-in-Depth (401.2)-6](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-6.png)
#### Password Cracker Methods
1. *Dictionary Attack*
	1. حمله با استفاده از یک wordlist, pass list انجام میشود.
2. *Bruteforce Attacks*
	1. حمله با یکسری کاراکتر های تصادفی انجام میشود.
3. *Hybrid-Attack*
	1. استفاده از دو روش Dictionary و Bruteforce همزمان با یکدیگر
4. *Pre-Computing Brute-Force Attacks (Rainbow Tables)*
	1. در این نوع حمله Bruteforce بر اساس الگوریتم Rainbow و دیتابیس Rainbow Table انجام میشود که میتواند سرعت کرک پسورد را بسیار کاهش دهد.
5. Image:
	1. ![SANS-401-Defense-in-Depth (401.2)-7](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-7.png)
#### Password Cracker Tools
##### John the Ripper
این ابزار که در CLI استفاده میشود، یکی از ابزار های مهمی که در Password Cracking استفاده میشود John the Ripper است. در ادامه در آزمایشگاه با این ابزار کار میکنیم.
##### Cain
یکی از ابزار های دیگر برای کرک پسورد Cain است که بصورت GUI و در ویندوز استفاده میشود. از این ابزار برای کرک پسورد های ویندوزی با هش NTLM بسیار استفاده میشود. 
	![SANS-401-Defense-in-Depth (401.2)-8](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-8.png)
در واقع میتوان دیتابیس LDAP را در ویندوز برداریم و سپس با این دستور پسورد تمام یوزر های درون اکتیو دایرکتوری را کرک کنیم.
این ابزار میتواند از هر دو روش Dictionary و Bruteforce برای حملات خود استفاده کند.
#### Protect Against Password Cracking
1. استفاده از رمزنگاری برای ذخیره سازی پسورد ها
2. استفاده از Password Policy و تعیین سیاست برای استفاده از پسور های Strong
3. استفاده از One-Time Password(OTP) به همراه Multi Factor Authentication(2FA) همزمان *Best*
	1. در این روش هر بار یوزر میخواهد لاگین کند از پسوردی متفاوت باید استفاده کند.
	2. در واقع هر پسورد برای یک Session مناسب است.
4. استفاده از Smart Card/Token یا Physical Keys
5. جلوگیری از Pre-Computing Attacks یا همان Rainbow tables attack
6. استفاده از احراز هویت Biometric برای احراز هویت کاربران *Best*
	1. این روش بالاترین سطح امنیتی را میتواند ارائه کند و همچنین میتواند پارامترهای متفاوتی داشته باشد:
	2. *Hand:* Finger Print, Hand Geometry
	3. *Eye:* Retina, iris
	4. *Face:* 3D,2D Face Scan, Photo Scan
	5. *Voice:* Voice Print, Voice Recognition 
	6. *Mannerisms:* Keystrokes, treads, handwriting
	7. *مزیت های استفاده از احراز هویت Biometric:*  
		1. افزایش سطح اطمینان Reliability
		2. راحت تر شدن کاربران برای احراز هویت
		3. کاهش هزینه های پیاده سازی و
		4. کاهش هزینه های نگهداری 
	5. *تصویر:*
			1. ![SANS-401-Defense-in-Depth (401.2)-9](/images/cyber-security/SANS-401-Defense-in-Depth(401.2)-9.png)

### !