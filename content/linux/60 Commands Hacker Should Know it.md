+++
title = "60 Commands Hacker Should Know it"
tags = ["Linux", "Command_Line"]
Category = "Linux"
draft = false
+++

-------
## TOC
### Strategy
در این آموزش میخواهم Location یک اکانت واتساپ را بدون نفوذ به موبایل تارگت بدست بیاوریم. برای اینکار مراحل زیر پیمایش میکنیم:
1. WhatsApp Phone Call to Target
	1. برقراری تماس تلفنی واتساپ با حساب کاربری تارگت
2. Get Target IP Address by WA Phone Call
	1. بدست آوردن آیپی آدرس از تماس تلفنی
3. Use IP to Find Country and City of Target
	1. پیدا کردن شهر و کشور با آیپی
4. After we Find ID Card of target(Full Name, Date of Birth, ...)
	1. بدست آوردن نام کامل، تاریخ تولد و اطلاعات کامل شخص، ...
	2. حتی در بعضی کشور ها مانند آلمان در این مرحله به آدرس کامل هم دسترسی خواهیم داشت.
5. Continue Info Gathering and Fine Target Email & LinkedIn Accounts
6. After that we find Exact Location of target on Map & Physical Address
7. in the End we Find Password of Target Accounts
### Tracking Target
#### 1. Get IP of Target & City + Country of IP
1. **Requires:**
	1. WhatsApp Call to Target, Wait for them to Answer
	2. Analyze and Filter the Network using `Wireshark` to get more info(Email, Phone, ....)
	3. So we need Install Perquisites 
		1. WhatsApp Desktop
		2. Wireshark
2. **Wireshark Filtering:**
	1. پس از اینکه WhatsApp Desktop را آماده کردیم و آماده تماس بودیم باید ابتدا آیپی لوکال خود را از `ipconfig, ifconfig` بدست بیاوریم. 
	2. سپس Wireshark را باز میکنیم و فیلتر Wireshark زیر را برای فیلتر بسته های که از ماشین ما خارج میشوند و مربوط به تماس تلفنی واتساپ هستند را اعمال میکنیم.
	3. Wireshark Filter: `ip.addr == 10.0.2.15 && stun`
		1. ![Alt text](/images/linux/Pastedimage20251201181732.png)
	4. حال کافیست تماس واتساپ را با شخص مقابل برقرار کنیم و منتظر باشیم تا پاسخ بدهد.
3. **Suitable Packet we Need:**
	1. حال اگر به Wireshark باز گردم بسته هایی که Capture شده را مشاهده میکنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201181847.png)
	2. بسته ای که ما به دنبال آن هستیم با `INFO: Binding Request` است که در آن اطلاعات آیپی و ایمیل تارگت مشاهده میشود:
		1. ![Alt text](/images/linux/Pastedimage20251201182046.png)
	3. بنابراین کافیست آیپی آدرس جلوی این بسته را برداشته با اطلاعات محلی آیپی را بدست بیاوریم:
		1. ![Alt text](/images/linux/Pastedimage20251201182137.png)
4. **Find Location(City & Country) of IP Address:**
	1. حال کافیست به وبسایت زیر برویم و اطلاعات محلی آیپی را بدست بیاوریم:
		1. https://whatismyipaddress.com
		2. https://whatismyipaddress.com/ip/ENTER_IP_ADDRESS
			1. ![Alt text](/images/linux/Pastedimage20251201182336.png)
	2. در پایین صفحه میتوانیم اطلاعات زیادی از آیپی شامل کشور، شهر و مختصات جغرافیای آیپی را مشاهده کنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201182425.png)
	3. مانند این وبسایت زیاد است و حتی برنامه ای که خودم نوشتم هم هست.
5. **Write Information of target in a Note:**
	1. اطلاعات *شهر* و *شماره تلفن* تارگت را یک نوشته مینویسیم تا بعدا بر روی آن کار کنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201182611.png)
#### 2. Get More Information about WhatsApp Number 
1. https://whatsapp.checkleaked.cc
	1. در مرحله بعدی به وبسایت بالا میرویم تا اطلاعات بیشتری را در مورد شماره تلفن واتساپ که بدست آوردیم جمع آوری کنیم. اطلاعاتی مانند بیوگرافی، تصویر پروفایل، نام، یوزر نیم و ....
	2. بنابراین شماره تلفن تارگت را وارد میکنیم، بر روی Search کلیک میکنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201182934.png)
	3. در اینجا اطلاعاتی از تارگت را مشاهده میکنیم ما فقط *Profile Picture* تارگت را برمیداریم.
2. **Google Reverse Image Search(For Finding Name of Person):**
	1. در این مرحله تصویر پروفایل تارگت را بصورت برعکس در گوگل جستجو میکنیم تا ببینیم اطلاعات بیشتری در مورد شخص یافت میشود یا خیر.
	2. اگر شخص پروفایل دیگری با همین تصویر داشته باشد با اینکار میتوانیم آنرا پیدا کنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201183204.png)
	3. در این مرحله نام شخص را که بدست آوردیم به نوشته حاوی شهر و شماره تارگت اضافه میکنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201183318.png)
#### 3. More Information about Target
1. **More Information from LinkedIn:**
	1. در صفحه لینکدین تارگت اطلاعات زیادی را میتوانیم بدست بیاوریم. مثلا دانشگاهی که تارگت درس خوانده یا محل کار تارگت
	2. این اطلاعات در جمع آوری اطلاعات بسیار مفید هستند. در این مثال ما از دانشگاه تارگت خود که در LinkedIn قرار داده است استفاده میکنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201183534.png)
2. **Google Search:**
	1. در این مرحله که دانشگاه و نام تارگت را داریم در گوگل جستجویی انجام میدهیم تا اطلاعات بیشتری را در مورد تارگت بدست بیاوریم. این جستجو را `""` انجام میدهیم تا نتایج دقیق تر باشد. پس عبارت زیر را در گوگل جستجو میکنیم:
		1. `"FULL-NAME" "UNIVERSITY"`
		2. `"Thomas pfeffer" "eppendorf"`
			1. ![Alt text](/images/linux/Pastedimage20251201183918.png)
	2. حال کافیست در لینک های که گوگل نشان میدهد کمی جستجو کنیم تا اطلاعات مفید و بیشتری را نیز بدست بیاوریم. مثلا در اینجا با جستجو تاریخ تولد تارگت را بدست میاوریم که در آخر نوشته یادداشت میکنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201184053.png)
3. **Full Address:**
	1. در بسیاری از کشور های دنیا مانند آلمان اگر نام کامل، نام شهر و تاریخ تولد یک فرد را داشته باشیم براحتی میتوانیم از پلیس درخواست آدرس کامل او را داشته باشیم.
	2. اگر اطلاعات دیگری مانند ایمیل و وبسایت شخص را هم پیدا کردید آنرا در نوشته خود یادداشت میکنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201184400.png)
#### 4. Email & Website Info Gathering
1. **https://intelx.io - Get Passwords of Target Email**
	1. در مرحله بعد به این وبسایت مراجعه میکنیم تا اطلاعات بیشتری را در مورد وبسایت و ایمیل تارگت خود بدست بیاوریم.
	2. بنابراین اولین جستجو را بر اساس ایمیل تارگت خود انجام میدهیم:
		1. ![Alt text](/images/linux/Pastedimage20251201184619.png)
	3. در این وبسایت اگر پسورد هایی که برای این ایمیل بوده اند و Leak شده باشند را میتوانیم بیابیم.
	4. مثلا یک دیتابیس `Collection 1/Collection` هست که میتوانیم با کلیک بر روی آن و سپس جستجو ایمیل تارگت پسورد که برای آن ثبت شده است را مشاهده کنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201184843.png)
	5. بنابراین پسورد که بدست آوردیم را نیز به آخر نوشته اضافه میکنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201184925.png)
2. **Have I Been Pwned**
	1. یکی دیگر از وبسایت ها که میتوانیم پسورد های Leak شده ایمیل ها را مشاهده کنیم، وبسایت بالاست که اگر پسورد دیگر برای آن ثبت شده باشد میتوانیم مشاهده کنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201185105.png)
	2. در نتایج این وبسایت فیلد هایی که از ایمیل مورد نظر Leak شده است را مشاهده میکنیم. مثلا در یک نتیجه فقط Username و Password است و در نتیجه ای دیگر Physical Address, Phone Numbers, IP Address و ... هم وجود دارد:
		1. ![Alt text](/images/linux/Pastedimage20251201185334.png)
		2. ![Alt text](/images/linux/Pastedimage20251201185312.png)
	3. بنابراین دیتابیس مورد نظر که Leak شده است و اطلاعات تارگت در آن وجود دارد بنام `LEAD Hunter` را دانلود میکنیم.
3. **Search In Database using `Agent Ransack`:**
	1. دیتابیس یک فایل بسیار بزرگ است که خواندن آن نیز دشوار است و نیاز به ابزار خود را دارد.
	2. ابزار `Agent Ransack` را دانلود و نصب میکنیم و سپس در محلی که فایل دیتابیس قرار دارد کلیک راست میکنیم و بر روی Agent Ransack کلیک میکنیم.
	3. سپس فیلدها را با موارد زیر پر میکنیم:
		1. File Name:
		2. `Containing Text: EMAIL OF TARGET`
		3. `Look In: PATH OF WHERE DATABASE HERE`
			1. ![Alt text](/images/linux/Pastedimage20251201185841.png)
	4. سپس بر روی `Search` کلیک میکنیم و سپس اطلاعاتی که فیلد `Containing Text` درون آن است را میتوانیم مشاهده کنیم:
		1. ![Alt text](/images/linux/Pastedimage20251201190027.png)
		2. ![Alt text](/images/linux/Pastedimage20251201185958.png)
		3. ![Alt text](/images/linux/Pastedimage20251201190000.png)
## !