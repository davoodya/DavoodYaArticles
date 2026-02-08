---
Episode: E34
Date: 2026-01-29
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 20:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E33 - Campaign URL Builder]]"
Next Episode: "[[E35 - Google Analytics(Behavior - Site Speed)]]"
---
-------
## TOC
- [Behavior Tab](#Behavior%20Tab)
	- [0. Description](#0.%20Description)
		- [Behavior Duty](#Behavior%20Duty)
		- [Behavior Metrics Description](#Behavior%20Metrics%20Description)
	- [1. Overview](#1.%20Overview)
	- [2. Behavior Flow](#2.%20Behavior%20Flow)
	- [3. Site Content](#3.%20Site%20Content)
		- [3.1: Description](#3.1:%20Description)
		- [3.2: All Pages](#3.2:%20All%20Pages)
		- [3.3: Content Drilldown](#3.3:%20Content%20Drilldown)
		- [3.4: Landing Pages](#3.4:%20Landing%20Pages)
- [Research Topic](#Research%20Topic)
--------------------
### Behavior Tab
#### 0. Description
##### Behavior Duty 
در تب Behavior میتوانیم مشاهده کنیم که کاربرانی که وارد وبسایت ما میشوند چه رفتاری انجام میدهند و در واقع دقیقا چکاری میکنند.
##### Behavior Metrics Description
در تب Behavior هم آمار هایی وجود دارد که باید معنای هر یک را بدانیم.
1. **Page Views:**
	1. تعداد کل صفحاتی از وبسایت ما که توسط کاربر بازدید شده اند.
2. **Unique Page Views:**
	1. تعداد بازدید های منحصر بفرد که از صفحات وبسایت ما شده است.
	2. شمارش صفحات Unique به شرح زیر است:
	3. اگر کاربری وارد صفحه اصلی وبسایت شود(1)، سپس به صفحه ای دیگر مثلا مقالات برود(2)، از آنجا مقاله ای را باز کند(3) و سپس مجددا به صفحه اصلی بازگردد(3 - صفحه اصلی مجدد شمرده نمیشود)
3. **Avg. Time On Page:**
	1. مقدار زمانی که بطور متوسط هر کاربر از صفحات ما دیدن کرده است.
	2. این عدد بهتر است که از 2 - 3 دقیقه بیشتر باشد که این آماری عالی محسوب میشود.
4. **Bounce Rate:**
	1. نرخ پرش از وبسایت است که نشان دهنده درصد کاربرانی است که وارد وبسایت ما شده اند و بدون اینکه کار خاصی انجام دهند خارج شده اند. 
5. **Exit:** - Research Topic
	1. این مقدار نشان دهنده درصدی از کاربران است که پس از چرخشی در صفحات از وبسایت خارج شده اند و با Bounce Rate متفاوت میباشد.
6. **Special Metrics:**
	1. *Description:*
		1. یکسری از آمار ها نیز در زیر منو هایی مانند `Behavior => Site Content => All Pages` وجود دارد که در زیر به توضیح آنها میپردازیم.
	2. *Entrances:*
		1. نرخ ورودی های وبسایت در این آمار مشاهده میشود. در واقع کاربرانی که از طریق این وبسایت وارد وبسایت ما شده اند. 
	3. *Page Value:*
		1. ارزش کلی که صفحه برای ما داشته است در این آمار مشخص میشود.
	4. *Exit:*
		1. صفحه خروج کاربر از وبسایت است. 
	5. *Image:*
		1. ![Pasted image 20260129161517.png](/images/python/Pasted image 20260129161517.png)
#### 1. Overview
1. **Description:**
	1. در این تب خلاصه ای از مطالب Behavior را در اختیار ما قرار میدهد:
		1. ![Pasted image 20260129153312.png](/images/python/Pasted image 20260129153312.png)
	2. برای دیدن آمار دقیق در ابتدا باید بازه تاریخ و همچنین زمان بندی تاریخ را مشخص کنیم:
		1. ![Pasted image 20260129153438.png](/images/python/Pasted image 20260129153438.png)
2. **Number Metrics:**
	1. در قسمت بالایی نرخ اعدادی از Metrics های توضیح داده شده را مشاهده میکنیم:
		1. ![Pasted image 20260129153417.png](/images/python/Pasted image 20260129153417.png)
3. **Best Pages in Pageviews:**
	1. در قسمت پایین سمت راست، آماری از پر بازدید ترین صفحات وبسایت را مشاهده میکنیم:
		1. ![Pasted image 20260129153534.png](/images/python/Pasted image 20260129153534.png)
	2. مثلا در وبسایت Top Learn پر بازدید ترین صفحه، صفحه اصلی `/` است که تعداد 31377 بازدید یعنی 13.12 % از کل بازدید ها را به خود اختصاص داده است:
		1. ![Pasted image 20260129153632.png](/images/python/Pasted image 20260129153632.png)
	3. همچنین صفحه دوم، مربوط به دوره سی شارپ مقدماتی است که در واقع نشان دهنده پربازدید ترین دوره در تاپ لرن است.
4. **Change Best Pages in Pageviews Metrics:**
	1. بصورت پیشفرض پربازدید ترین صفحات وبسایت با آدرس Page نمایش داده میشوند. 
	2. اما با استفاده از قسمت پایین سمت چپ میتوانیم این نحوه نمایش را بر روی گزینه های دیگری مانند گزینه های زیر تنظیم کنیم:
		1. Page Title
		2. Search Term
		3. Event Category
		4. Image:
			1. ![Pasted image 20260129154043.png](/images/python/Pasted image 20260129154043.png)
5. **Note:**
	1. از صفحات پربازدید وبسایت میتوانیم برای معرفی و لینک دهی به سایر صفحات وبسایت خود استفاده کنیم. 
	2. مثلا در تاپ لرن در صفحه مربوط به دوره سی شارپ مقدماتی میتوانیم لینک دوره های سی شارپ 7 و همچنین سی شارپ پیشرفته و یا اینکه آموزش Net Framework. را نیز بگذاریم.
#### 2. Behavior Flow
1. **Description:**
	1. در این گزینه میتوانیم چارت تصویری از نحوه حرکت کاربران بین صفحات وبسایت مان را مشاهده کنیم:
		1. ![Pasted image 20260129154429.png](/images/python/Pasted image 20260129154429.png)
	2. برای Highlight کردن یک مسیر هم که میتوانیم بر روی مسیر اولیه کلیک کنیم و سپس `Highlight Traffic Through here` را انتخاب کنیم:
		1. ![Pasted image 20260129154535.png](/images/python/Pasted image 20260129154535.png)
2. **Read Behavior Flow:**
	1. برای خواندن نتیجه Behavior Flow از چارت تاپ لرن استفاده میکنیم:
		1. ![Pasted image 20260129154638.png](/images/python/Pasted image 20260129154638.png)
	2. در این چارت 16K از کاربران وارد صفحه اصلی شده اند و از صفحه اصلی به همان صفحه اصلی رفتند:
		1. ![Pasted image 20260129154736.png](/images/python/Pasted image 20260129154736.png)
	3. علاوه بر آن 1K که وارد شده اند از صفحه اصلی به سایر صفحات وبسایت نیز رفته اند که چون صفحه مشخص نبود و وبسایت آکادمی است More Pages را به ما نشان میدهد:
		1. ![Pasted image 20260129154905.png](/images/python/Pasted image 20260129154905.png)
	4. همچنین در قدم سوم آمار کاربران به شکل زیر میباشد:
		1. 5.5K | 7.5K from `/` to `/courses`
		2. 972 | 3.3K from `/` to `auth/sign-in` 
		3. 84 | 2.4K from `/` to `auth/sign-up` 
		4. 831 | 992 from `/` to specific course 
		5. 4.2K | 8.7K from `/` to more 100 page of website
		6. *Image:*
			1. ![Pasted image 20260129155342.png](/images/python/Pasted image 20260129155342.png)
	5. *نکته:* این آمار بصورت تقریبی است و مثلا 5.5K | 7.5K یعنی تعداد 5500 تا 7500 نفر
	6. *نکته دوم:* قسمت قرمز در Flow هم که نشان دهنده تعداد خروجی ها از وبسایت ما میباشد. این خروجی ها هر چه در قدم اول بیشتر باشد آمار بد تر و هرچه در قدم های بالاتر باشند آمار بهتر است.
3. **Change Flow Filter:**
	1. در این Flow هم میتوانیم فیلتر را از Pages به سایر فیلتر های موجود مانند Sources, Campaigns, Landing Page, ... نیز تغییر دهیم:
		1. ![Pasted image 20260129155534.png](/images/python/Pasted image 20260129155534.png)
		2. ![Pasted image 20260129155459.png](/images/python/Pasted image 20260129155459.png)
	2. این فیلتر ها در دسته بندی های متفاوتی میباشند.
#### 3. Site Content
##### 3.1: Description
1. در این تب محتوا Content وبسایت را میتوانیم بررسی کنیم. 
##### 3.2: All Pages
1. **All Pages Description:**
	1. در این قسمت آماری کلی از بازدید هایی که از صفحات وبسایت ما انجام شده اند را مشاهده میکنیم:
		1. ![Pasted image 20260129155953.png](/images/python/Pasted image 20260129155953.png)
	2. در قسمت بالایی، تعداد کلی Pageviews را مشاهده میکنیم و در قسمت پایین هر صفحه وبسایت را به تفکیک با Metrics های توضیح داده شده مشاهده میکنیم:
		1. ![Pasted image 20260129160113.png](/images/python/Pasted image 20260129160113.png)
	3. جدولی که در قسمت پایین این منو قرار دارد ارزش بررسی دارد زیرا که میتوانیم صفحات مورد دار وبسایتمان را مشاهده کنیم و اقدام به رفع خطاهای آن کنیم:
		1. ![Pasted image 20260129160238.png](/images/python/Pasted image 20260129160238.png)
	4. همچنین مهمترین آمار این قسمت نیز `Avg. Time On Page` است که اگر بیش از 2 3 دقیقه باشد بسیار در بالا رفتن رتبه بندی سئو ما اثر گذار است.
2. **New Metrics:**
	1. *Entrances:*
		1. نرخ ورودی های وبسایت در این آمار مشاهده میشود. در واقع کاربرانی که از طریق این وبسایت وارد وبسایت ما شده اند. 
		2. مثلا در تصویر زیر مشاهده میکنیم که صفحه "دوره آموزش سی شارپ مقدماتی تا پیشرفته" تعداد 3286 ورودی داشته است:
			1. ![Pasted image 20260129160652.png](/images/python/Pasted image 20260129160652.png)
		3. این آمار نشان دهنده این است که کاربرانی صفحه "دوره آموزش سی شارپ مقدماتی تا پیشرفته" را Bookmark کرده اند و مستقیما از آن وارد وبسایت ما میشوند.
	2. *Exit:*
		1. صفحه خروج کاربر از وبسایت است. 
		2. مثلا در تصویر زیر مشاهده میکنیم که 28.49 درصد کاربران از صفحه "دوره آموزش سی شارپ مقدماتی تا پیشرفته" از وبسایت ما خارج شده اند:
			1. ![Pasted image 20260129160822.png](/images/python/Pasted image 20260129160822.png)
		3. در واقع آمار نشان دهنده این است که کاربران فایل های دوره را دانلود کردند و سپس از وبسایت خارج شده اند.
	3. *Page Value:*
		1. ارزش کلی که صفحه برای ما داشته است در این آمار مشخص میشود.
3. **Example of Metric Reading:**
	1. در تصویر زیر مشاهده میکنیم که یک صفحه مقاله "دلیل اینکه شما برنامه نویس بیکار هستید" نرخ Exit آن 77.81 درصد و Bounce Rate آن 85.73 درصد است اما Avg. Time on Page آن 03:46 دقیقه هست:
	2. این آمار نشان دهنده این است که کاربر از طریق لینک اشتراک شده مقاله در شبکه اجتماعی وارد شده است، مقاله را بصورت کامل خوانده چون زمان بالایی دارد و سپس از همان صفحه نیز از وبسایت خارج شده است.
	3. در این آمار با اینکه Exit و Bounce Rate نرخ بالایی دارد اما چون Avg. Time on Page آن بالاست آمار خوبی برای سئو محسوب میشود.
	4. *نکته:* ترفند هایی برای کاهش نرخ Exit و Bounce Rate در همچین صفحه های وجود دارد که عبارتند از: لینک گذاری مطالب مرتبط، لینک به ویدئویی مرتبط و ... 
4. **Find Exit Page(Bounce Rate & Exit Sorting):**
	1. یکی از کارهای مهم برای افزایش رتبه بندی سئو وبسایت یافتن نقاط(صفحات) ایست که کاربر در آن بیشترین خروج از وبسایت را داشته است.
	2. در واقع صفحاتی که Bounce Rate , Exit بالا دارند را باید پیدا کنیم و دلیل نرخ بالای آنها را بیابیم.
	3. برای اینکار در جدول پایین صفحه All Pages، بر روی هر یک از آمار های Bounce Rate و Exit تک به تک کلیک میکنیم تا صفحاتی که بیشترین آمار در این دو نرخ را دارند در ابتدا لیست قرار گیرند:
		1. ![Pasted image 20260129164356.png](/images/python/Pasted image 20260129164356.png)
		2. ![Pasted image 20260129164424.png](/images/python/Pasted image 20260129164424.png)
	4. حال باید صفحاتی که در بالای لیست قرار دارند را یک به یک بررسی کنیم و سپس علت این نرخ های بالا را پیدا کنیم و در نتیجه به رفع خطاهای موجود بپردازیم:
		1. ![Pasted image 20260129164638.png](/images/python/Pasted image 20260129164638.png)
	5. *نکته:* یکسری از صفحات هستند که نرخ Bounce Rate یا Exit به مقدار 100 درصد دارند که این صفحات واقعا برای سئو وبسایت منفی هستند و باید حتما بررسی شوند.
##### 3.3: Content Drilldown
1. **Description:**
	1. در این قسمت دسته بندی های وبسایت ما را با Metrics های آن مشاهده میکنیم:
		1. ![Pasted image 20260129162026.png](/images/python/Pasted image 20260129162026.png)
	2. منظور از دسته بندی در واقع همان First URL Segmentation میباشد.
	3. مثلا آدرس `vapeclub3.com/categories/` را داریم، حال هر لینکی از در این پس از این باشد در دسته بندی `categories` قرار میگیرد. مثلا:
		1. `vapeclub3.com/categories/pod/oxva.php`
		2. `vapeclub3.com/categories/mod/uwell.php`
2. **Read Analysis of Content Drilldown:**
	1. با خواندن آمار این قسمت متوجه میشویم که کدام قسمت از وبسایت ما بیشترین بازدید را داشته است.
	2. مثلا تصویر زیر مربوط تاپ لرن است که آمار آنرا بررسی میکنیم:
	3. ![Pasted image 20260129162452.png](/images/python/Pasted image 20260129162452.png)
	4. بیشترین بازدید از `/courses/` ها با آمار زیر است:
		1. Pageviews: 91852
		2. Unique Pageviews: 56263
		3. Avg. Time on Page: 00:01:51
		4. Bounce Rate: 46.47%
		5. Exit: 22.65%
	5. و دومین آمار بازدید هم مربوط به صفحه اصلی `/` است.
	6. و سومین آمار بازدید هم مربوط به صفحه `/auth/` برای احراز هویت است.
	7. کم بازدید ترین هم مربوط به بخش پنل کاربری `/account/` میباشد.
3. **Go to a Level Deeper:**
	1. اگر بخواهیم از First URL Segment به Second URL Segment و همینطور به جلو برویم و آمار آنها را نیز مشاهده کنیم(یعنی مشاهده آمار زیر دسته بندی ها)
	2. برای اینکار کافیست که روی First URL Segment دسته بندی اصلی در جدول اصلی کلیک کنیم تا زیر دسته بندی ها مشاهده شود:
		1. ![Pasted image 20260129162850.png](/images/python/Pasted image 20260129162850.png)
		2. ![Pasted image 20260129162854.png](/images/python/Pasted image 20260129162854.png)
	3. همچنین این قابلیت برای رفتن به سایر URL Segment ها نیز کاربرد دارد.
##### 3.4: Landing Pages
1. **Description:**
	1. در این صفحه آماری از کل صفحات وبسایت را با Metric های استاندارد Acquisition , Behavior, Conversions مشاهده میکنیم. 
	2. *Sessions:* Sessions, New Sessions, New Users 
	3. *Behavior:* Bounce Rate, Pages / Sessions, Avg. Session Duration
	4. *Conversion:* Goal Conversion Rate, Goal Completion, Goal Value
		1. جلوتر این قسمت را بصورت کامل توضیح خواهیم داد.
	5. *Image:*
		1. ![Pasted image 20260129163355.png](/images/python/Pasted image 20260129163355.png)
2. **Filters:**
	1. بصورت پیشفرض آمار هایی که گفتیم فقط برای Landing Pages ها نشان داده میشود. 
	2. حال میتوانیم گزارش جدیدی را نیز به این قسمت اضافه کنیم که برای اینکار بر روی `Secondary Dimensions` کلیک میکنیم و آمار جدید که میخواهیم را انتخاب میکنیم:
		1. ![Pasted image 20260129163548.png](/images/python/Pasted image 20260129163548.png)
	3. مثلا اگر در این قسمت Medium را انتخاب کنیم میتوانیم نوع ورودی های هر Landing Page را نیز مشاهده کنیم:
		1. ![Pasted image 20260129163726.png](/images/python/Pasted image 20260129163726.png)
	4. با خواندن آمار های Medium مشاهده میکنیم که بیشترین ورودی صفحه اصلی وبسایت از Google Search Engine و Referral که وبسایت های دیگر Backlinks داده اند بوده است:
		1. ![Pasted image 20260129163848.png](/images/python/Pasted image 20260129163848.png)
	5. *نکته:* بهتر است که بیشترین زمان و تمرکز خود را بر روی روش های Organic, Referral و همچنین شبکه های اجتماعی مانند تلگرام بگذاریم.
### Research Topic
1. هر کدام از نرخ های **Bounce Rate** و **Exit** دقیقا به چه معنا هستند و تفاوت دو نرخ **Bounce Rate** و **Exit** در چیست؟
2. نرخ های Entrances , Page Values دقیقا به چه معنایی هستند؟
### !