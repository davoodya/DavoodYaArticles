---
Episode: E35
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
Pervious Episode: "[[E34 - Google Analytics(Behavior - Behavior Flow & Site Content)]]"
Next Episode: "[[E36 - Google Analytics(Behavior - Site Search)]]"
---
-------
## TOC
- [Google Analytics => Behavior => Site Speed Tab](#Google%20Analytics%20=%3E%20Behavior%20=%3E%20Site%20Speed%20Tab)
	- [0. Description](#0.%20Description)
		- [0.1: Site Speed Tab Description](#0.1:%20Site%20Speed%20Tab%20Description)
		- [0.2: Metrics Description](#0.2:%20Metrics%20Description)
	- [1. Overview](#1.%20Overview)
	- [2. Page Timing](#2.%20Page%20Timing)
		- [2.1: Explorer => Site Usage - Default View](#2.1:%20Explorer%20=%3E%20Site%20Usage%20-%20Default%20View)
		- [2.2: Other Views](#2.2:%20Other%20Views)
	- [3. Speed Suggestion](#3.%20Speed%20Suggestion)
	- [4. User Timing](#4.%20User%20Timing)
- [Research Topic](#Research%20Topic)
------------------
### Google Analytics => Behavior => Site Speed Tab
#### 0. Description
##### 0.1: Site Speed Tab Description
قسمت Site Speed برای بررسی سرعت بارگذاری وبسایت میباشد که میتوان گفت مانند GT-Metrix میباشد:
	![Pasted image 20260129174227.png](/images/python/Pasted image 20260129174227.png)
##### 0.2: Metrics Description
1. **Avg. Page Load Time(sec):**
	1. میانگین سرعت لود بارگذاری وبسایت به ثانیه
2. **Avg. Redirection Time(sec):**
	1. میانگین سرعت بارگذاری صفحات ریدایرکت شده در وبسایت
	2. مثلا اگر صفحاتی در وبسایت داریم که لینک آنها هر چند وقت یکبار عوض میشوند و برای اینکه کاربر بتواند دسترسی داشته باشد نیاز به پیاده سازی Redirect دارد، در اینجا میانگین سرعت بارگذاری آنها مشاهده میشود.
3. **Avg. Domain Lookup Time(sec):**
	1. میانگین زمانی که برای ترجمه دامنه وبسایت به آیپی وبسایت صرف شده است. این زمان دست ما نیست و بستگی به سرور و ارائه دهنده دامنه ما دارد.
4. **Avg. Server Connection Time(sec):**
	1. میانگین زمانیکه برای اتصال کاربر با سرور وبسایت ما صرف شده است.
5. **Avg. Server Response Time(sec):**
	1. میانگین زمانیکه برای برای ارسال پاسخ سرور به کاربر صرف شده است.
	2. در واقع زمانیکه وبسایتی را باز میکنیم، در کنار آن Loader دایره ای را مشاهده میکنیم که تا زمان لود شدن کامل وبسایت میچرخد.
	3. حال میانگین زمانیکه این Loader برای کاربران میچرخد در این گزینه نمایش داده میشود.
6. **Avg. Page Download Time(sec):**
	1. میانگین زمانیکه کاربر برای دانلود منابع ما(JS, CSS, Images, ...) صرف کرده است.
	2. اگر زمان این آمار زیر 1 ثانیه باشد آماری قابل قبول محسوب میشود.
7. **Image:**
	1. ![Pasted image 20260129175252.png](/images/python/Pasted image 20260129175252.png)
- **Research Topic:**
	- بهترین آمار برای Metrics های درون Page Speed چه زمانیست؟
#### 1. Overview
1. **Description:**
	1. در این قسمت آماری کلی از Metrics های سرعت وبسایت قابل مشاهده هستند.
	2. برای مشاهده آماری دقیق مثله سایر منو ها اولین کار انتخاب بازه تاریخی مشخص برای مشاهده آمار است:
		1. ![Pasted image 20260129175728.png](/images/python/Pasted image 20260129175728.png)
2. **Main Chart: Avg. Page Load Time(sec):**
	1. در بالاترین قسمت، نموداری از سرعت لود صفحه را مشاهده میکنیم که فقط برای یک Metric یعنی Avg. Page Load Time(sec) میباشد:
		1. ![Pasted image 20260129175627.png](/images/python/Pasted image 20260129175627.png)
	2. *نکته:* البته میتوانیم Metric این نمودار را تغییر دهیم کافیست روی Avg. Page Load Time(sec) کلیک کنیم و Metric که میخواهیم را انتخاب کنیم:
		1. ![Pasted image 20260129180216.png](/images/python/Pasted image 20260129180216.png)
	3. *نکته دوم:* همچنین میتوانیم دو Metric را انتخاب و در این نمودار بصورت مقایسه ای آنها را بررسی کنیم که برای اینکار کافیست روی `Select a metric` کلیک کنیم:
		1. ![Pasted image 20260129180309.png](/images/python/Pasted image 20260129180309.png)
3. **Number Metrics:**
	1. در قسمت پایین نمودار Avg. Page Load Time(sec) آماری عددی از کلیه Metric های Page Speed را مشاهده میکنیم:
		1. ![Pasted image 20260129175710.png](/images/python/Pasted image 20260129175710.png)
4. **Page Speed Based on Browsers, Country, Pages:**
	1. در قسمت پایین آمار عددی، میتوانیم سرعت بارگذاری وبسایت را بر اساس انواع مرورگر، کشور های مختلف و یا برای هر صفحه از وبسایت را مشاهده کنیم:
	2. *Browser Image:*
		1. ![Pasted image 20260129180053.png](/images/python/Pasted image 20260129180053.png)
	3. *Country Image:*
		1. ![Pasted image 20260129180437.png](/images/python/Pasted image 20260129180437.png)
	4. *Pages Image:*
		1. ![Pasted image 20260129180455.png](/images/python/Pasted image 20260129180455.png)
#### 2. Page Timing
##### 2.1: Explorer => Site Usage - Default View
1. **Description:**
	1. در این منو گزارشی از سرعت لود صفحات وبسایت را مشاهده میکنیم. بصورت پیشفرض هم گزارش ها در زیر شاخه Explorer => Site Usage نمایش داده میشود:
		1. ![Pasted image 20260129184001.png](/images/python/Pasted image 20260129184001.png)
	2. اما گزینه های دیگری هم وجود دارند که آمار های فنی و دقیق تری به ما میدهند:
		1. ![Pasted image 20260129184014.png](/images/python/Pasted image 20260129184014.png)
	3. بصورت پیشفرض بر اساس آدرس صفحه Page صفحات را نمایش میدهد اما برای خوانایی بیشتر میتوان از Title و یا حتی سایر موارد استفاده کرد:
		1. ![Pasted image 20260129180922.png](/images/python/Pasted image 20260129180922.png)
	4. *مشاهده بر اساس Page Title:*
		1. ![Pasted image 20260129181005.png](/images/python/Pasted image 20260129181005.png)
2. **Read Page Timing:**
	1. برای هر صفحه در ستون آخر(Avg. Page Load Time(sec)) یک نمودار قرمز و یک نمودار سبز وجود دارد:
		1. ![Pasted image 20260129181222.png](/images/python/Pasted image 20260129181222.png)
	2. نمودار سبز بدین معناست که سرعت این صفحه نسبت به میانگین سرعت لود صفحه Avg. Page Load Time(sec) بالاتر بوده است.
	3. نمودار قرمز بدین معناست که سرعت این صفحه نسبت به میانگین سرعت لود صفحه Avg. Page Load Time(sec) پایین بوده است.
	4. مثلا در تصویر زیر صفحه "دوره های آموزشی تاپ لرن" 75.44 درصد بالاتر از میانگین سرعت بارگذاری و "دوره آموزش بازی سازی Unity" مقدار 389.66 درصد پایین تر از میانگین سرعت بارگذاری وبسایت است:
		1. ![Pasted image 20260129181516.png](/images/python/Pasted image 20260129181516.png)
	5. *نکته:* هر دو Metric ستون اول و ستون دوم صفحه Page Timing را میتوانیم تغییر دهیم:
		1. ![Pasted image 20260129181312.png](/images/python/Pasted image 20260129181312.png)
3. **Note:** Apply GT-Metrix for Low Speed Pages
	1. صفحاتی که سرعت لود پایینی دارند را باید با GT-Metrix بررسی خاص انجام دهیم و سپس معیار هایی که وبسایت GT-Metrix به ما میدهد را روی آن صفحه اعمال کنیم.
4. **Note 2:** Use Ajax for Low Speed Pages
	1. یکسری از صفحات ما بدلیل اینکه باید داده زیادی را با صفحه اصلی بارگذاری کنند سرعت لودشان بسیار پایین می آید. 
	2. مثلا صفحاتی که نظرات کاربران در آن هست و کاربران با تصاویر نظر میدهند بار بسیار زیادی را به صفحه اضافه میکند.
	3. حال برای رفع این نوع مشکلات پیشنهاد میشود بارگذاری نظرات یا سایر المان ها را با استفاده از AJAX پس از بارگذاری کامل صفحه انجام دهیم و به صفحه لود شده تزریق کنیم.
	4. برای اینکار کافیست کد لود المان های کند کننده سرعت را در `document.ready {}` بنویسیم تا پس از لود کامل صفحه به صفحه تزریق شوند و باعث کندی سرعت نشوند.
##### 2.2: Other Views
1. **Technical:**
	1. در این گزینه آمار فنی از کدنویسی وبسایت ما که در سرعت بارگذاری وبسایت موثر است نمایش داده میشود:
		1. ![Pasted image 20260129184256.png](/images/python/Pasted image 20260129184256.png)
	2. در واقع این قسمت نشان میدهد که آیا کدنویسی وبسایت ما بهینه بوده یا خیر
2. **Distribution:**
	1. در این قسمت آمار سرعت بارگذاری وبسایت را به شکل متفاوتی مشاهده میکنیم:
		1. ![Pasted image 20260129184438.png](/images/python/Pasted image 20260129184438.png)
	2. مثلا در تصویر مشاهده میکنیم که تعداد 45 صفحه وبسایت ما بین 0 الی 1 ثانیه بارگذاری شده اند که 8.30 درصد کل صفحات ما هستند.
	3. همچنین تعداد 242 صفحه وبسایت ما بین 1 الی 3 ثانیه بارگذاری شده اند که 44.65 درصد کل صفحات ما هستند.
	4. همچنین تعداد 144 صفحه وبسایت ما بین 3 الی 7 ثانیه بارگذاری شده اند که 26.57 درصد کل صفحات ما هستند.
	5. تعداد 15 صفحه وبسایت ما +60 ثانیه بارگذاری شده اند که 2.7 درصد کل صفحات ما هستند و در واقع آمار بسیار بدی است.
	6. *تصویر:*
		1. ![Pasted image 20260129184706.png](/images/python/Pasted image 20260129184706.png)
	7. *نکته:* با کلیک بر روی `+` در کنار هر رکورد نیز میتوانیم ریز صفحات را مشاهده کنیم.
3. **Map Overlay:**
	1. سرعت بارگذاری وبسایت را بر اساس کشور ها و شهر ها میتوان مشاهده کرد که در هر کشور یا شهر سرعت بارگذاری به چه صورت بوده است:
		1. ![Pasted image 20260129184955.png](/images/python/Pasted image 20260129184955.png)
		2. ![Pasted image 20260129184810.png](/images/python/Pasted image 20260129184810.png)
4. **Dom Timings - Research Topic:**
	1. در پنجره Dom Timings در `Behavior => Site Speed => Page Timing` آمار چه چیزی از سرعت لود صفحه نمایش داده میشود؟
#### 3. Speed Suggestion
1. **Description:**
	1. در این منو پیشنهاداتی که گوگل برای افزایش سرعت صفحات به ما میدهد مشاهده میشود:
		1. ![Pasted image 20260129182117.png](/images/python/Pasted image 20260129182117.png)
2. **Speed Suggestion Metrics:**
	1. *Page Speed Suggestion:*
		1. تعداد پیشنهاداتی که گوگل برای افزایش سرعت وبسایت داده است.
	2. *Page Speed Score:*
		1. امتیازی که گوگل به سرعت بارگذاری صفحه داده است.
	3. *Image:*
		1. ![Pasted image 20260129182308.png](/images/python/Pasted image 20260129182308.png)
3. **Page Speed Insights:**
	1. پیشنهاداتی که گوگل برای افزایش سرعت بارگذاری میدهد در واقع با آنالیز که ابزار Google Page Speed Insights انجام میدهد پیاده میشود.
	2. هنگامیکه بر روی Page Speed Suggestion ها کلیک کنیم نیز بصورت خودکار به Google Page Speed Insights منتقل میشویم و آنالیز بر روی صفحه مورد نظر انجام میشود:
		1. ![Pasted image 20260129182540.png](/images/python/Pasted image 20260129182540.png)
	3. *نکته:* پیشنهادات ابزار GT-Metrix کامل تر است و بنابراین اگر پیشنهادات GT-Metrix را بصورت کامل انجام دهیم 100 درصد امتیاز بهتری دریافت میکنیم.
	4. *نتیجه اسکن Google Page Speed Insights:*
		1. ![Pasted image 20260129182734.png](/images/python/Pasted image 20260129182734.png)
		2. ![Pasted image 20260129182737.png](/images/python/Pasted image 20260129182737.png)
#### 4. User Timing
1. **Description:**
	1. در این منو فعالیت های کاربر بر اساس زمان نمایش داده میشود، مثلا اینکه کاربر چه زمانی را در یک صفحه یا دسته بندی مشخص صرف کرده است:
		1. ![Pasted image 20260129183300.png](/images/python/Pasted image 20260129183300.png)
	2. این منو بصورت پیشفرض غیر فعال میباشد و باید بصورت دستی فعال شود.
2. **Enable User Timing:**
	1. `Click on Gear(Admin Panel) => Ecommerce Settings => Enable Toggle => Save`
		1. ![Pasted image 20260129183420.png](/images/python/Pasted image 20260129183420.png)
		2. ![Pasted image 20260129183500.png](/images/python/Pasted image 20260129183500.png)
3. **Note:**
	1. فعالسازی این گزینه باید با تحقیق انجام شود.
4. **Research Topic:**
	1. گزینه User Timing دقیقا چه فعالیت هایی را گزارش میدهد؟
	2. فعال کردن User Timing چه تداخلی ایجاد میکند و چرا فعال کردن آن پیشنهاد نمیشود؟
5. 
### Research Topic
1. **Best Score for Page Speed Metrics:**
	1. بهترین آمار برای Metrics های درون Page Speed چه زمانیست؟
2. **User Timing:**
	1. گزینه User Timing دقیقا چه فعالیت هایی را گزارش میدهد؟
	2. فعال کردن User Timing چه تداخلی ایجاد میکند و چرا فعال کردن آن پیشنهاد نمیشود؟
3. **Dom Timings - Research Topic:**
	1. در پنجره Dom Timings در `Google Analytics => Behavior => Site Speed => Page Timing` دقیقا آمار چه چیزی از سرعت لود صفحه نمایش داده میشود؟
### !