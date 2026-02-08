---
Episode: E32
Date: 2026-01-28
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 16:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E30, E31 - Google Analytics(Audience Tab)]]"
Next Episode: "[[E33 - Campaign URL Builder]]"
---
-------
## TOC
- [Google Analytics => Acquisition](#Google%20Analytics%20=%3E%20Acquisition)
	- [Description](#Description)
	- [Website Acquisition Methods](#Website%20Acquisition%20Methods)
	- [1. Overview](#1.%20Overview)
	- [2. All Traffic](#2.%20All%20Traffic)
		- [2.1: Channels](#2.1:%20Channels)
		- [2.2: Referrals](#2.2:%20Referrals)
	- [3. Google Ads](#3.%20Google%20Ads)
	- [4. Search Console](#4.%20Search%20Console)
	- [5. Social](#5.%20Social)
	- [5. Campaigns](#5.%20Campaigns)
---------------
### Google Analytics => Acquisition
#### Description
به عنوان یک Webmaster برای  ما باید مهم باشد که کاربران وبسایت به چه نحوی جذب و وارد وبسایت ما میشوند. 
برای مشاهده روش های ورود و جذب کاربر به وبسایت ما بصورت ریز و جزئی از تب `Acquisition` درون `Google Analytics` استفاده میکنیم.
#### Website Acquisition Methods
بطور کلی کاربران از چهار روش کلی وارد یک وبسایت میشوند:
1. **Organic Search:**
	1. ورودی هایی که از نتایج گوگل وبسایت ما را یافتند و وارد وبسایت شده اند.
2. **Direct:**
	1. کاربرانی که آدرس وبسایت ما را در مرورگر وارد کرده اند و وارد وبسایت ما شده اند.
	2. *نکته:* کاربرانی که از تلگرام نیز وارد وبسایت میشوند در واقع نوع Direct محسوب میشوند زیرا که تلگرام لینک وبسایت را در مرورگر اجرا میکند.
3. **Referral:**
	1. کاربرانی که از وبسایت هایی که ما را معرفی کرده اند(Backlinks داده اند) وارد وبسایت ما شده اند.
4. **Social:**
	1. کاربرانی که از طریق شبکه های اجتماعی وارد وبسایت ما شده اند.
	2. در این قسمت شبکه های اجتماعی معروف مانند Facebook, Twitter, Pinterest, .... ردیابی میشوند.
- **Note:** Other Social Networks Acquisition Tracking
	- برای بدست آوردن آمار ورودی از هر شبکه اجتماعی روش خاصی وجود دارد که در جلسه بعدی به آن میپردازیم.
#### 1. Overview
در این پنجره میتوانیم یک گزارش کلی از نحوه ورودی های کاربر به وبسایت خود را مشاهده کنیم. برای مشاهده آماری دقیق ابتدا بازه تاریخی که میخواهیم را مشخص میکنیم.
1. **Circle Chart:**
	1. در این گزینه آماری کلی از نحوه ورودی های وبسایت را مشاهده میکنیم:
		1. ![Pasted image 20260128154608.png](/images/python/Pasted image 20260128154608.png)
		2. ![Pasted image 20260128155002.png](/images/python/Pasted image 20260128155002.png)
2. **User Acquisition:**
	1. در کنار نمودار دایره ای آماری از کل تعداد یوزر هایی که وارد وبسایت ما شده اند را نیز مشاهده میکنیم:
		1. ![Pasted image 20260128155801.png](/images/python/Pasted image 20260128155801.png)
3. **Numbers Acquisition:**
	1. در قسمت پایین نمودار دایره ای آماری از تعداد ورودی های وبسایت را نیز مشاهده میکنیم که ورودی ها را به عدد نشان میدهد:
		1. ![Pasted image 20260128155102.png](/images/python/Pasted image 20260128155102.png)
	2. همچنین کل ورودی های وبسایت نیز در این گزینه قابل مشاهده است:
		1. ![Pasted image 20260128155158.png](/images/python/Pasted image 20260128155158.png)
	3. همچنین آمار های رفتار کاربران مانند Bounce Rate, Sessions, Page / Sessions, Avg. Session Duration, New Users ,... را در کنار هر نوع ورودی میتوانیم مشاهده کنیم:
		1. ![Pasted image 20260128155343.png](/images/python/Pasted image 20260128155343.png)
4. **Note:** Off Page SEO God or Not?
	1. در این قسمت از آمار ها میتوانیم متوجه شویم که آیا سئو OFF Page مناسبی را داشته ایم یا نه؟
	2. در واقع اگر آمار ورودی های `Referral` ما بالا باشد یعنی Off Page ما خوب بوده اگر کم باشد یعنی Off Page ما خوب نبوده است.
5. **Note 2:** Improve Social Acquisition
	1. همچنین باید بر روی افزایش ورودی های خود از شبکه هایی مانند فیسبوک، توئیتر کار کنیم زیرا که بسیار مستعد هستند و میتوانند ورودی ها را به نحو چشمگیری افزایش دهند.
6. **Note 3:** Click on Each Acquisition
	1. برای مشاهده آماری دقیق از هر نوع ورودی یعنی Organic, Direct, Referral, Social کافیست بر روی آنها در قسمت آمار عددی کلیک کنیم تا آمار دقیق آنها را مشاهده کنیم:
		1. ![Pasted image 20260128160220.png](/images/python/Pasted image 20260128160220.png)
	2. مثلا در تصویر زیر آمار دقیق Referral را مشاهده میکنیم:
		1. ![Pasted image 20260128160250.png](/images/python/Pasted image 20260128160250.png)
#### 2. All Traffic
##### 2.1: Channels
در این منو ورودی های وبسایت از شبکه های اجتماعی را بصورت کامل و به تفکیک هر شبکه میتوانیم مشاهده کنیم:
	![Pasted image 20260128155924.png](/images/python/Pasted image 20260128155924.png)
##### 2.2: Referrals
گفتیم برای مشاهده آمار های دقیق کافیست در Overview بر روی آنها کلیک کنیم و یا اینکه میتوانیم به منو Referrals درون All Traffics برویم:
	![Pasted image 20260128161423.png](/images/python/Pasted image 20260128161423.png)
	![Pasted image 20260128160250.png](/images/python/Pasted image 20260128160250.png)
1. **Analysis Referrals:**
	1. برای بررسی اینکه کدام یک از ورودی های Referrals ما بیشترین سود را برای ما داشته اند باید هم تعداد ورودی و هم Bounce Rate آنها را بررسی کنیم و اگر نرخ ورودی ها زیاد و درصد Bounce Rate آنها کم بود به معنای سود بیشتر است.
2. **Comparison:**
	1. برای بررسی بهتر مقادیر میتوانیم از روش مقایسه استفاده کنیم، مثلا در وبسایت تبلیغ داده ایم و حالا میخواهیم مشاهده کنیم که ورودی هایی که از این وبسایت گرفتیم خوب بوده یا نه.
	2. برای اینکار گزینه `Compression` را در قسمت بالای جدول آمار انتخاب میکنیم:
		1. ![Pasted image 20260128160904.png](/images/python/Pasted image 20260128160904.png)
	3. سپس پارامتر هایی که میخواهیم با هم مقایسه شوند را انتخاب میکنیم. مثلا نرخ ورودی و Bounce Rate یکی از بهترین مقایسه ها برای بررسی موثر بودن یک تبلیغ است:
		1. ![Pasted image 20260128161012.png](/images/python/Pasted image 20260128161012.png)
	4. در آمار زیر مشاهده میکنیم که ورودی از وبسایت Barnamehnevisan تعداد 2557 بوده و 5 درصد آمار پرش داشته است که به معنای آمار عالیست:
		1. ![Pasted image 20260128161204.png](/images/python/Pasted image 20260128161204.png)
	5. و یا Google API تعداد 291 ورودی داشته با 115 درصد آمار پرش که به معنای افتضاح است:
		1. ![Pasted image 20260128161220.png](/images/python/Pasted image 20260128161220.png)
#### 3. Google Ads
در این گزینه آماری از بازدهی تبلیغات گوگل را مشاهده میکنیم:
	![Pasted image 20260128161548.png](/images/python/Pasted image 20260128161548.png)
یکسری از نتایج گوگل هستند که در کنار آنها کلمه `ads` نوشته میشوند اینها همان نتایجی هستند که توسط Google Ads انجام شده اند.
خرید تبلیغات گوگل بازدهی بالایی دارند اما قیمت بالایی نیز دارند.
#### 4. Search Console
در این گزینه آمار هایی از کشور های کاربران، دیوایس ها، صفحات لندینگ و ... مشاهده میشود:
	![Pasted image 20260128161900.png](/images/python/Pasted image 20260128161900.png)
	![Pasted image 20260128161910.png](/images/python/Pasted image 20260128161910.png)
#### 5. Social
در این گزینه آماری از شبکه های اجتماعی را بصورت کامل مشاهده میکنیم:
	![Pasted image 20260128162009.png](/images/python/Pasted image 20260128162009.png)
	![Pasted image 20260128162137.png](/images/python/Pasted image 20260128162137.png)
- **نکته:** در ایران شبکه های اجتماعی که گوگل از آنها پشتیبانی میکنند مانند Facebook, Linkedin, .... زیاد استفاده نمیشوند اما راه اندازی این شبکه های اجتماعی برای بالا بردن آمار ورودی وبسایت بسیار بازده است و این آمار ورودی را به شدت افزایش میدهد.
#### 5. Campaigns
قابلیتی بنام URL Builder وجود دارد که با استفاده از آن میتوانیم URL های قابل رهگیری را بسازیم. در جلسه بعدی به توضیح این قابلیت میپردازیم زیرا که برای بررسی این منو Campaigns ابتدا باید URL Builder را پیاده سازی کنیم.
### !