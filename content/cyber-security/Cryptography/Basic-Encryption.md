+++
title = "Basic-Encryption"
slug = "basic-encryption"
date = "2024-06-20T09:59:19+03:30"
lastmod = "2026-02-09T09:59:19+03:30"
draft = false

categories = ["Cryptography"]
tags = ["Cryptography", "CyberSecurity", "Encryption"]
series = ["Cryptography"]

description = "- E2: Introduction - What  is Network Security? - Why do we need Security? - Security Concerns - That's Why Need Security? - OSI Security..."
keywords = ["Basic-Encryption", "Cryptography", "CyberSecurity", "Encryption", "basic-encryption"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/Cryptography/basic-encryption/"

featured_image = "/images/cyber-security/Basic-Encryption-1.png"
images = ["/images/cyber-security/Basic-Encryption-1.png"]

[params.opengraph]
  title = "Basic-Encryption"
  description = "- E2: Introduction - What  is Network Security? - Why do we need Security? - Security Concerns - That's Why Need Security? - OSI Security..."
  image = "/images/cyber-security/Basic-Encryption-1.png"
  url = "https://davoodya.ir/Cryptography/basic-encryption/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Basic-Encryption"
  description = "- E2: Introduction - What  is Network Security? - Why do we need Security? - Security Concerns - That's Why Need Security? - OSI Security..."
  image = "/images/cyber-security/Basic-Encryption-1.png"

readingTime = 23
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
+++
-------
- [E2: Introduction](#E2:%20Introduction)
	- [What  is Network Security?](#What%20%20is%20Network%20Security?)
	- [Why do we need Security?](#Why%20do%20we%20need%20Security?)
	- [Security Concerns](#Security%20Concerns)
	- [That's Why Need Security?](#That's%20Why%20Need%20Security?)
	- [OSI Security Architecture](#OSI%20Security%20Architecture)
	- [Security Attacks, Mechanisms & Services](#Security%20Attacks,%20Mechanisms%20&%20Services)
	- [Episode Summary](#Episode%20Summary)
- [E3: Network Attacks](#E3:%20Network%20Attacks)
	- [What is Network Security Attacks?](#What%20is%20Network%20Security%20Attacks?)
	- [Five Forms of Network Attacks](#Five%20Forms%20of%20Network%20Attacks)
	- [Security Attacks Types](#Security%20Attacks%20Types)
		- [Passive Attacks Types](#Passive%20Attacks%20Types)
		- [Active Attacks Types](#Active%20Attacks%20Types)
		- [Attack Types Slide](#Attack%20Types%20Slide)
	- [Active & Passive Attack Types](#Active%20&%20Passive%20Attack%20Types)
		- [Deep to Passive Attacks](#Deep%20to%20Passive%20Attacks)
			- [Release of Message Contents](#Release%20of%20Message%20Contents)
			- [Traffic Analysis](#Traffic%20Analysis)
		- [Deep to Active Attacks](#Deep%20to%20Active%20Attacks)
			- [Masquerade](#Masquerade)
			- [Replay](#Replay)
		- [All Attacks Slides](#All%20Attacks%20Slides)
	- [Episode Summary](#Episode%20Summary)
- [E4: Network Services](#E4:%20Network%20Services)
	- [What is Network Security Services(NSS)?](#What%20is%20Network%20Security%20Services(NSS)?)
	- [Network Security Services(NSS) Types](#Network%20Security%20Services(NSS)%20Types)
	- [NSS Types Description](#NSS%20Types%20Description)
		- [Authentication](#Authentication)
		- [Access Control](#Access%20Control)
		- [Confidentiality](#Confidentiality)
		- [Integrity](#Integrity)
		- [Non-Repudiation](#Non-Repudiation)
		- [Availability](#Availability)
		- [Summary & Slide](#Summary%20&%20Slide)
	- [Cryptography Mechanism](#Cryptography%20Mechanism)
	- [OSI Network Security Model](#OSI%20Network%20Security%20Model)
		- [Open in OSI(Open System Interconnection)](#Open%20in%20OSI(Open%20System%20Interconnection))
		- [OSI First Blocks(Encryption in Source)](#OSI%20First%20Blocks(Encryption%20in%20Source))
		- [Key for Plain Text to Cipher Text](#Key%20for%20Plain%20Text%20to%20Cipher%20Text)
		- [OSI Last Block(Decryption in Destination)](#OSI%20Last%20Block(Decryption%20in%20Destination))
		- [Summary of OSI Model](#Summary%20of%20OSI%20Model)
	- [Tasks of OSI Network Security Model](#Tasks%20of%20OSI%20Network%20Security%20Model)
	- [Episode Summary](#Episode%20Summary)
-------
### E2: Introduction
#### What  is Network Security?
امنیت شبکه مجموعه ای از تکنولوژی ها و فناوری هاست که از قابلیت Usability(استفاده) و Integrity(تجمیع) شبکه و زیر ساخت یک شرکت محافظت میکند.
از امنیت شبکه برای جلوگیری از ورود یا تکثیر بد افزارها و تهدیدات بالقوه درون شبکه استفاده میشود.
#### Why do we need Security?
ما به امنیت در تمام جنبه های زندگی نیازمندیم: از امنیت زندگی، امنیت شغلی، امنیت وسایل خود و ...
علاوه بر آن ما به امنیت برای ارسال پیام های خود در سطح اینترنت نیز نیازمندیم.
1. در سالهای قبل که از ماشین های Stand Alone استفاده میشد به امنیت شبکه نیاز بسیار کمتری داشتیم اما با ظهور شبکه های کامپیوتری حملات در سطح شبکه بطور چشمگیری افزایش داشته است.
2. هکرها آسیب پذیری های درون  سیستم ما را پیدا میکنند و سعی به نفوذ از طریق آن میکنند.
3. امروزه با وجود و ظهور شبکه اینترنت حتی اگر شبکه هم نداشته باشیم در سطح زیادی به امنیت وابسته شده ایم. در واقع امروزه اکثر کارهای روزمره مانند امور بانکی، کارهای دولتی، ارسال پیام ها و ایمیل، پر کردن فرم های مختلف، انجام معاملات سهام، رزرو بلیط هواپیما و ... همگی از طریق اینترنت  انجام میشوند و در نتیجه باید به امنیت آنها توجه زیادی داشته باشیم:
	1. ![Basic-Encryption-1](/images/cyber-security/Basic-Encryption-1.png)
4. تمام این فناوری ها که ذکر کردیم در قالب سیستم هایی عرضه میشوند که با این سیستم ها قابلیت های نفوذ بسیار بیشتری نسبت به ماشین های Stand Alone را دارند.
#### Security Concerns
مشکلات و گپ هایی که در برقراری ارتباط بین این سیستم ها پیش می آید را در زیر توضیح میدهیم:
1. چگونه بفهمم طرفی که در طرف مقابل شبکه است همان طرفیست که من میخواهم با او صحبت کنم؟
2. چگونه مطمئن شوم اطلاعاتی که در شبکه ارسال میکنم شنود نمیشود و به دست شخصی که باید میرسد؟
3. آیا هکری در شبکه من وارد شده است یا خیر؟
4. وبسایتی که اطلاعات را از آن دانلود کرده ام وبسایتی قانونیست یا جعلی؟
5. اگر با شخصی معامله مالی برقرار میکنم چگونه تضمین کنم که او در مدتی بعد معامله را جعل نکند؟
6. من میخواهم جنسی را از اینترنت بخرم اما نمیخواهم تا قبل رسیدن بسته دست من پول از کارت من کم شود.
#### That's Why Need Security?
ما به امنیت اطلاعات به دلایل زیر نیازمندیم:
1. CIA Triangles - (Confidentiality, Integrity, Availability)
	1. از محرمانه بودن(Confidentiality) ، یکپارچگی و جامع بودن(Integrity) و در دسترس بودن(Availability) داده اطمینان حاصل کنیم.
2. Insecure Networks: Internet, Internal Networks
	1. امروزه اینترنت تنها شبکه نا امن نیست و بلکه شبکه های داخلی ارگان ها و سازمان ها هم نیاز به امنیت دارند.
3. Insider Attacks
	1. همچنین احتمال حملات از درون سازمان Insider Attacks نیز بسیار بالاست.
#### OSI Security Architecture
یک معماری امنیتی است که برای نوع شبکه از مدل OSI عرضه شده است. بطور کامل به این معماری در جلسات آینده میپردازیم:
	![Basic-Encryption-2](/images/cyber-security/Basic-Encryption-2.png)
#### Security Attacks, Mechanisms & Services
در مبحث امنیت شبکه بطور کلی سه نکته وجود دارد که باید عمیقا درک شود:
1. **Attacks**:
	1. هر اقدامی که امنیت اطلاعات شبکه را به خطر بیندازد را حمله امنیتی می نامند. 
	2. این نوع از حملات میتوانند در دو مدل انجام شوند: 1. *Active* و 2. *Passive* که هدف این دو حمله با یکدیگر متفاوت میباشد:
		1. ![Basic-Encryption-3](/images/cyber-security/Basic-Encryption-3.png)
	3. در حملات *Passive* انگیزه اصلی *سرقت اطلاعات* است در حالیکه در حملات *Active* انگیزه اصلی *ایجاد پارازیت و اختلال(مانند Jamming)* در برقراری ارتباطات شبکه میباشد.
2. **Security Mechanism**:
	1. **Security Mechanism Description:**
		1. *مکانیزمی که برای شناسایی، پیشگیری و یا بازیابی از یک حمله امنیتی طراحی شده است:*
			1. Detect 
			2. Prevent
			3. Recover
		2. در واقع هنگامیکه  سیستم مورد حمله قرار میگیرد باید مکانیزمی وجود  داشته باشد تا بتواند جلوی حمله را بگیرد و یا حمله را از سیستم دفع کند.
		3. مکانیزم های امنیتی زیادی وجود دارند که در جلسات بعدی به آنها میپردازیم و از مهمترین آنها میتوان به Cryptography اشاره کرد.
	2. **Cryptography:**
		1. کلمه Cryptography از کلمه یونانی **Cryptos** به معنی *مخفی* و **Writing** به معنی *نوشتن* تشکیل شده است و در کل به معنی Hidden Writing میباشد.
		2. در واقع در این فرآیند میگوییم که مثلا اگر بخواهیم متنی را در شبکه برای طرف مقابل ارسال کنیم بجای اینکه آنرا بصورت Plain Text ارسال کنیم در آن تغییراتی را ایجاد میکنیم که اگر در بین راه  شنود شد قابل خواندن نباشد.
		3. مثلا اگر بخواهیم *abc* را برای طرف مقابل بفرستیم *def* را میفرستیم و قانون کلمات را نیز تعریف میکنیم. این مکانیزم باعث میشود که اگر هکر در بین راه داده را سرقت کرد نتواند به داده اصلی دست یابد و بلکه به داده ای دیگر دست پیدا میکند:
			1. ![Basic-Encryption-4](/images/cyber-security/Basic-Encryption-4.png)
		4. در فرایند پیچیده تر متن Plain Text را به متن Cipher Text تبدیل میکنیم که اینکار با یک کلید عمومی انجام میشود.
		5. به این کار به اصطلاح Cryptography گفته میشود.
	3. **Steganography:**
		1. یکی دیگر از مکانیزم های امنیتی است که در این مکانیزم مهاجم متوجه رد و بدل شدن داده در بین فرستند و گیرنده نمیشود.
		2. در قدیم متنی را با آب لیمو خشک شده بر روی کاغذ مینوشتند و در نتیجه اگر بین راه کسی میدید با کاغذی خالی متوجه میشد اما شخص گیرنده میدانست که با گرفتن اتش میتواند متن را از تصویر بخواند.
		3. امروزه میتوان متنی را درون یک عکس نوشت و سپس عکس را به سمت گیرنده ارسال کرد. در اینجا اگر هکر در بین راه به تصویر دسترسی پیدا کند به محتوای اصلی که درون تصویر است دسترسی ندارد در حالیکه گیرنده میداند چگونه متن را از عکس استخراج کند.
		4. فرآیند Steganography را میتوان بر روی تصاویر، موسیقی، فایل های PDF و ... اعمال کرد.
	4. **Different Between Cryptography and Steganography:**
		1. در Cryptography مهاجم میداند متنی داده ای در حال عبور است و بنابراین به تجزیه و تحلیل ترافیک ادامه میدهد تا بتواند به داده اصلی دست پیدا کند و رمز گشایی را انجام دهد اما در Steganography مهاجم اطلاعی از عبور داده ندارد و در نتیجه تجزیه تحلیل را هم متوقف میکند.
	5. Slide:
		1. ![Basic-Encryption-5](/images/cyber-security/Basic-Encryption-5.png)
3. **Security Services**:
	1. سرویسی است که میتواند امنیت پردازش داده و انتقال داده را برقرار کند. 
	2. سرویس های امنیتی اصولا از چندین مکانیزم امنیتی برای برقراری امنیت و غلبه بر حملات استفاده میکنند.
#### Episode Summary
بطور خلاصه در این جلسه موارد زیر را یاد گرفتیم:
1. Why need Security
2. Dependence on IT with or without Networks
3. Security Concerns
4. Glimpse OSI Network Security Architecture
	1. Glimpse(نگاهی اجمالی)
5. Security Attacks, Mechanisms & Services
6. Slide:
	1. ![Basic-Encryption-6](/images/cyber-security/Basic-Encryption-6.png)
### E3: Network Attacks
#### What is Network Security Attacks?
به حملات امنیتی که برای گرفتن دسترسی غیر مجاز به شبکه یک سازمان انجام میشود و هدف اصلی آن سرقت اطلاعات یا انجام سایر امور مخرب است انجام میشود حملات امنیتی شبکه گفته میشود.
#### Five Forms of Network Attacks
1. **Normal Flow:**
	- در این جریان اطلاعات از مبدا به مقصد توسط کانالی امن منتقل میشود. در این جریان نشت اطلاعاتی وجود ندارد و نهایت امنیت اطلاعات حفظ میشود:
		- ![Basic-Encryption-7](/images/cyber-security/Basic-Encryption-7.png)
2. **Interruption(Attack on Availability):**
	- در این جریان مبدا ارسال کننده مشاهده میکند که اطلاعات به سمت مقصد ارسال شده در حالیکه اطلاعاتی به مقصد نرسیده است:
		- ![Basic-Encryption-8](/images/cyber-security/Basic-Encryption-8.png)
	- در این حالت مهاجم مکانیزمی را برای متوقف کردن جریان ارسال داده ارائه میدهد که به آن حمله به دسترسی میگویند.
	- در این مدل دسترسی به داده Availability مورد حمله قرار میگیرد.
3. **Interception(Attack on Confidentiality):**
	- در این مدل اطلاعات مانند Normal Flow از مبدا به سمت مقصد ارسال میشوند با این تفاوت که مهاجم در بین راه اطلاعات را شنود و سرقت میکند:
		- ![Basic-Encryption-9](/images/cyber-security/Basic-Encryption-9.png)
	- در این مدل محرمانگی اطلاعات Confidentiality مورد حمله قرار میگیرد.
4. **Modification(Attack on Integrity):**
	- در این مدل بر خلاف Normal Flow اطلاعات بصورت کامل از مبدا به مقصد نمیرسند بلکه در بین راه توسط مهاجم شنود و دستکاری میشوند و سپس اطلاعات دستکاری شده به سمت مقصد ارسال میشوند.:
		- ![Basic-Encryption-10](/images/cyber-security/Basic-Encryption-10.png)
	- در واقع در این مدل مهاجم در بین راه مبدا و مقصد به دستکاری اطلاعات رد و بدل شده میپردازد.
	- در این مدل یکپارچگی اطلاعات مورد حمله قرار میگیرد.
5. **Fabrication(Attack on Authenticity):**
	- در این مدل اطلاعات از مبدا به مقصد صادر نمیشوند و بلکه اطلاعات از ماشین مهاجم به سمت مقصد ارسال میشوند:
		1. ![Basic-Encryption-11](/images/cyber-security/Basic-Encryption-11.png)
	- در واقع در این مدل مهاجم جوری وانمود میکند که اطلاعاتی که برای مقصد ارسال کرده از مبدا ارسال شده است و در واقع خود(مهاجم) مبدا است.
	- در این مدل به اصالت داده(Authenticity) حمله میشود.
- All Flows Slide:
	- ![Basic-Encryption-12](/images/cyber-security/Basic-Encryption-12.png)
#### Security Attacks Types
##### Passive Attacks Types
هدف کلی این نوع حملات سرقت و شنود اطلاعات است.
1. No modification or fabrication
	1. در این مدل از حملات مهاجم اطلاعاتی را که بدست می آورد در بین راه تغییر نمیدهد و یا جعل نمیکند. 
	2. در واقع در این نوع حملات هدف مشاهده و مانیتورینگ اطلاعاتی است که بین مبدا و مقصد رد و بدل میشود.
2. Eavesdropping to learn contents
	1. در این مدل مهاجم به شنود اطلاعات  میپردازد و اطلاعات را در واقع سرقت میکند .
##### Active Attacks Types
هدف کلی این نوع حملات متوقف کردن برقراری ارتباط و انتقال داده هاست.
1. Modification of Content
	1. در این مدل مهاجم اطلاعات را تغییر میدهد.
2. Impersonate legitimate parties
	1. در این مدل مهاجم جعل را انجام میدهد.
3. Modify Content in Transmit
	1. در این مدل اطلاعات در بین راه توسط مهاجم تغییر پیدا میکند.
4. Launch DOS
	1. در این مدل حمله از کار دهنده سرویس به تارگت انجام میشود.
	2. در این مدل مهاجم ارتباط بین مبدا و مقصد را با ارسال پیام های Jam Message محدود میکند و در نتیجه Jamming بین مبدا و مقصد انجام میشود.
##### Attack Types Slide
![Basic-Encryption-13](/images/cyber-security/Basic-Encryption-13.png)
#### Active & Passive Attack Types
##### Deep to Passive Attacks
###### Release of Message Contents
1. **Release of Message Contents:**
	- در تصویر زیر شخصی در مبدا بنام Bob میخواهد اطلاعات را بر بستر اینترنت برای شخصی در مقصد بنام Alice ارسال کند، در اینجا مهاجم در میان راه بصورت سایلنت به شنود و برداشت داده ها میپردازد:
		![Basic-Encryption-14](/images/cyber-security/Basic-Encryption-14.png)
###### Traffic Analysis
1. **Traffic Analysis:**
	1. در این مدل هم در تصویر زیر شخصی در مبدا بنام Bob میخواهد اطلاعات را بر بستر اینترنت برای شخصی در مقصد بنام Alice ارسال کند:
	2. در این مدل مهاجم علاوه بر شنود پیام رد و بدل شده، سعی میکند با شنود تمام پیام  ها الگویی که برای Cipher شدن متن معمولی پیام استفاده میشود و در واقع کلید رمزنگاری را نیز بدست بیاورد.
		1. ![Basic-Encryption-15](/images/cyber-security/Basic-Encryption-15.png)
##### Deep to Active Attacks 
###### Masquerade
در این سناریو مبدا Bob، مقصد Alice و مهاجم Darth نام دارد:
1. حال در حمله Masquerade یا ماسک مهاجم Darth جوری وانمود میکند که مثلا مبدا Bob است و میخواهد برای مقصد Alice داده بفرستد. 
2. در واقع در این نوع حمله مهاجم خود را بجای مبدا جا میزند.
3. در اینجا مقصد Alice ممکن است متوجه شود که پیام هایی که به او میرسد به اندازه پیام هایی که از مبدا اصلی Bob میرسیدند نیستند و بنابراین اینترنت و ارتباط خود را قطع میکند.
4. در این نوع از حمله هدف مهاجم Darth قطع ارتباط مبدا و مقصد است که به خوبی انجام میشود.
5. *Slide:*
	1. ![Basic-Encryption-16](/images/cyber-security/Basic-Encryption-16.png)
###### Replay
در این سناریو مبدا Bob، مقصد Alice و مهاجم Darth نام دارد:
1. در این نوع حمله مبدا Bob داده ها را به سمت مقصد Alice ارسال میکند. همچنین در همان زمان مهاجم Darth داده ها را در بین راه شنود میکند و مجددا همان داده ها را برای مبدا Bob میفرستد.
2. حال وقتی مقصد Alice دو پیام مشابه را از دو مکان مختلف دریافت میکند، ارتباطات خود را قطع میکند و در نتیجه مهاجم Darth به هدف خود یعنی قطع ارتباط میرسد.
3. Slide:
	1. ![Basic-Encryption-17](/images/cyber-security/Basic-Encryption-17.png)
##### All Attacks Slides
![Basic-Encryption-18](/images/cyber-security/Basic-Encryption-18.png)
#### Episode Summary
1. **Five Forms of Security Attacks:**
	1. Normal Flow
	2. Interruption
	3. Interception
	4. Modification
	5. Fabrication 
2. **Passive Attack and Active Attacks:**
	1. *Passive Attacks:*
		1. Release of Message Contents
		2. Traffic Analysis 
	2. *Active Attacks:*
		1. Masquerade
		2. Replay
		3. Modification of Message Contents
3. **Slide:**
	1. ![Basic-Encryption-19](/images/cyber-security/Basic-Encryption-19.png)
### E4: Network Services
#### What is Network Security Services(NSS)?
سرویس های امنیت شبکه یا Network Security Services(NSS) مجموعه ای از کتابخانه ها هستند که برای توسعه به سبک Cross Platform برنامه های کاربردی کلاینت/سرور با قابلیت های امنیتی طراحی شده  اند.
در این قسمت به شش دسته از این ابزارها که برای ارائه  خدمات امنیتی استفاده میشوند میپردازیم و از آنها استفاده میکنیم.(مانند Cryptography, Steganography و ...)
#### Network Security Services(NSS) Types
همانطور که گفتیم بطور کلی 6 دسته خدمات امنیتی که برای امن سازی سیستم ها ارائه میشوند را در این جلسه بررسی میکنیم:
1. Authentication احراز هویت
2. Access Control کنترل دسترسی
3. Data Confidentiality محرمانه بودن اطلاعات
4. Data Integrity صحت اطلاعات(جامعیت)
5. Non-Repudiation عدم انکار ارسال یا دریافت
6. Availability در دسترس بودن کانال ارتباطی - Preventation against DOS
7. *Slide:*
	1. ![Basic-Encryption-20](/images/cyber-security/Basic-Encryption-20.png)
#### NSS Types Description
##### Authentication
به معنای احراز هویت مبدا است که داده را ارسال کرده است. در واقع بدین وسیله از صحت ارسال داده اطمینان حاصل میکنیم.
در واقع در این مفهوم باید از صحت وجودی Node هایی که به ارسال داده میپردازند اطمینان حاصل کنیم تا مطمئن شویم تا از سمت دیگر یعنی مهاجم ارسال نشده باشد.
- بطور خلاصه در این مفهوم مبدا و مقصد باید احراز هویت شوند تا Node غیر مجاز نتواند داده ای در این بین رد و بدل کند.
##### Access Control
پس از اینکه Node(یا Entity) احراز هویت شد، باید دسترسی هایی که میتواند به منابع داشته باشد را کنترل کنیم. در واقع یک Node باید به اندازه خود نه بیشتر و نه کمتر به داده های لازم دسترسی داشته باشد.
- این مورد میتواند از دسترسی غیر مجاز به منابع شبکه جلوگیری کند.
##### Confidentiality
در این مفهوم باید محرمانه بودن اطلاعات را مدیریت کنیم، یعنی اطلاعات درون شبکه نباید به افراد غیر مجاز برسد و باید از دسترسی افراد غیر مجاز جلوگیری شود.
- در واقع محرمانگی اطلاعات در حین انتقال آنها باید به خوبی حفظ شوند تا اطلاعات بدست Entity های غیر مجاز مانند هکر ها نیفتد.
##### Integrity
این مفهوم میگوید که داده که میخواهیم ارسال کنیم باید بصورت کاملا دست نخورده به سمت طرف مقصد برسد. 
- در واقع داده نباید در بین راه تغییر کند و افشا شود و مقصد باید همان داده ای را دریافت کند که از مبدا ارسال شده است.
- در این مدل مبدا باید اطمینان حاصل کند که داده ای که برای مقصد میفرستد بدون دستکاری به او میرسد و همچنین مقصد نیز باید اطمینان حاصل کند که داده ای که دریافت کرده است بدون هیچ تغییری در بین راه به او رسیده است. بصورت خلاصه این مفهوم صداقت داده را نشان میدهد.
##### Non-Repudiation
در این مفهوم باید قابلیت انکار کردن را از بین ببریم. یعنی مثلا اگر من ایمیل را به سمت مقصد ارسال کردم نباید بعدا بتوانم این ارسال را انکار کنم حتی اگر این ایمیل را از روی اکانت خود حذف کرده باشم.
- در واقع در این مفهوم ارسال کننده هیچ گزینه ای را برای انکار  ارسال نباید داشته باشد و همچنین دریافت کننده نیز هیچ گزینه ای را برای انکار دریافت نباید داشته  باشد.
##### Availability 
همانطور که توضیح دادیم بسیاری از مهاجمان در نزدیکی شبه تلاش به مسدود کردن شبکه Jamming آن دارند تا بتوانند  کانال های ارتباطی را مسدود کنند و در واقع Availability را از بین ببرند.
حال در مفهوم Availability ما باید این مدل از حملات را یعنی حملات DOS را جلوگیری کنیم تا مهاجمان نتوانند ارتباطات شبکه را مختل و قطع کنند.
- در واقع در مفهوم Availability باید از کانال ارتباطی بصورتی محافظت کنیم تا همیشه برای اهداف سازمان در دسترس باشند و بتوانیم از آنها برای ارسال اطلاعات و برقراری ارتباط استفاده کنیم.
##### Summary & Slide
بنابراین این 6 دسته از خدماتی هستند که Network Security Services ها NSS برای افزایش امنیت شبکه ارائه میدهند که در تصویر زیر نیز میتواند آنها را مشاهده کنید:
	![Basic-Encryption-21](/images/cyber-security/Basic-Encryption-21.png)
#### Cryptography Mechanism
یکی از مهمترین و بهترین مکانیزم های امنیتی که برای افزایش امنیت سیستم ها ارائه میشود Cryptography(رمزنگاری) نام دارد.
برای بررسی مفهوم Cryptography نیاز داریم که ابتدا مدل OSI شبکه را با یکدیگر بررسی کنیم. مدل OSI(Open System Interconnection) یکی از مدل هاییست که برای فهم و درک بهتر از شبکه های کامپیوتری عرضه و ارائه شده است.
#### OSI Network Security Model
##### Open in OSI(Open System Interconnection)
- کلمه Open در این مدل بدین معناست که میتوانیم ماژول ها و مکانیزم هایی را که میخواهیم برای افزایش امنیت به شبکه اضافه کنیم. در واقع Open میگوید که هر کس بخواهد میتواند ماژول های مورد نیاز خود را به این سیستم شبکه اضافه کند.
##### OSI First Blocks(Encryption in Source)
- مدل OSI اساسا از سه بلوک اصلی تشکیل شده است:
	![Basic-Encryption-22](/images/cyber-security/Basic-Encryption-22.png)
- بلوک اول در از سمت چپ مربوط به امنیت مدل است و Security Related Transformation نامیده میشود. همانطور که در تصویر زیر هم مشاهده میکنید Message به حالت نرمال بدون رمز وارد این چرخه میشود و سپس به عبارتی شامل کاراکتر های بی ربط تبدیل میشود تا اگر در بین راه بدست مهاجم افتاد نتواند داده اصلی را  بخواند. در واقع در اولین بلاک Plain Text به Cipher Text تبدیل میشود:
	![Basic-Encryption-23](/images/cyber-security/Basic-Encryption-23.png)
##### Key for Plain Text to Cipher Text
- عبارت Cipher Text توسط کلید Key میتواند مجدد به Plain Text تبدیل شود که این کلید از طریق راه ارتباطی Information Channel به سمت گیرنده داده ارسال میشود:
	![Basic-Encryption-24](/images/cyber-security/Basic-Encryption-24.png)
- همچنین این کلید میتواند توسط یک طرف سوم مورد اعتماد که Trusted Third Party نیز خوانده میشود تولید شود و سپس برای گیرنده ارسال شود:
	![Basic-Encryption-25](/images/cyber-security/Basic-Encryption-25.png)
- هکر در بین راه برای شنود و یا تغییر اطلاعات قرار میگیرد و اگر بتواند کلید را  بدست بیاور میتواند به اهداف خود برسد.
- بنابراین کلید استفاده شده باید بسیار طولانی باشد و همچنین با استفاده از الگوریتم های امنیتی به قدری پیچیده شود که قابل شکستن نباشد.
##### OSI Last Block(Decryption in Destination)
- حال که داده Cipher Text به مقصد میرسد باید در اولین قدم رمزگشایی شود. به همین دلیل در سمت مقصد نیز باید بلاکی وجود داشته باشد تا بتواند متن Cipher Text شده را به Plain Text باز گرداند.
- این بلاک هم Security Related Transformation نام دارد:
	- ![Basic-Encryption-26](/images/cyber-security/Basic-Encryption-26.png)
- کلید این رمز گشایی باید از سمت کانال ارتباطی Information Channel و یا شخص سوم مورد اعتماد Trusted Third Party برای مقصد ارسال شود
##### Summary of OSI Model
1. بنابراین مشاهده کردیم که در مدل OSI بلاک اول به رمزنگاری داده میپردازد و Plain Text را به Cipher Text تبدیل میکند. اینکار توسط بلاک Security Related Transformation انجام میشود:
	1. ![Basic-Encryption-27](/images/cyber-security/Basic-Encryption-27.png)
2. برای این رمزنگاری کلیدی استفاده میشود که این کلید از طریق کانال ارتباطی Information Channel و یا شخص سوم مورد اعتماد Trusted Third Party در مبدا ایجاد و برای مقصد ارسال میشود:
	1. ![Basic-Encryption-28](/images/cyber-security/Basic-Encryption-28.png)
3. در بلاک آخر مدل، داده Cipher Text دریافت شده مجددا باید به حالت اولیه Plain Text تبدیل شود که اینکار توسط بلاک آخر مدل که آنهم Security Related Transformation نام دارد انجام میشود:
	1. ![Basic-Encryption-29](/images/cyber-security/Basic-Encryption-29.png)
#### Tasks of OSI Network Security Model
1. اولین وظیفه این مدل طراحی و ساخت الگوریتم پیچیده برای Cryptography است که این نوع الگوریتم باید بسیار پیچیده باشد تا توسط مهاجم شکسته نشود:
	1. ![Basic-Encryption-30](/images/cyber-security/Basic-Encryption-30.png)
2. *وظیفه بعدی ایجاد اطلاعات محرمانه است که این اطلاعات باید بین فرستنده و گیرنده ارسال شود:*
	1. این اطلاعات باید بصورت رمزنگاری Cryptography شده باشد.
	2. اگر کلید توسط خود فرستنده تولید شود باید به توسط فرستنده به گیرنده ارسال شود.
	3. اگر توسط شخص سوم مورد اعتماد Trusted Third Party تولید شود باید توسط شخص سوم به مبدا و مقصد ارسال شود.
3. وظیفه بعدی توسعه روش هایی برای ارسال و اشتراک گذاری کلید Cryptography بین مبدا و مقصد داده است که این روش باید به نحوی باشد که توسط مهاجم شنود و یا کرک نشود. برای اینکار میتواند از ترکیب چندین الگوریتم با یکدیگر استفاده کرد.
4. در آخر باید پروتکلی را تعریف کنیم که مبدا و مقصد هر دو از آن استفاده کنند.
5. **Slide:**
	1. ![Basic-Encryption-31](/images/cyber-security/Basic-Encryption-31.png)
#### Episode Summary
1. **Six Category of Network Security Services**
	1. Authentication
	2. Access Control
	3. Data Confidentiality
	4. Data Integrity
	5. Non-Repudiation 
	6. Availability
2. OSI Network Model 
3. Tasks of OSI Network Model
4. *Slide:*
	1. ![Basic-Encryption-32](/images/cyber-security/Basic-Encryption-32.png)
### !