---
Episode: E41
Date: 2026-02-01
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 15:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E42 - Google Analytics(Conversion - Ecommerce)]]"
Next Episode: "[[E40 - Google Analytics(Conversions - Goals)]]"
---
-------
## TOC
- [Funnel Description](#Funnel%20Description)
	- [Funnel Meaning](#Funnel%20Meaning)
	- [Funnel Description with Example](#Funnel%20Description%20with%20Example)
	- [Funnel Usages](#Funnel%20Usages)
- [Google Analytics => Conversion => Goals => Funnels](#Google%20Analytics%20=%3E%20Conversion%20=%3E%20Goals%20=%3E%20Funnels)
	- [0. Define Goal with Funnel](#0.%20Define%20Goal%20with%20Funnel)
	- [1. Conversion => Goals => Funnel Visualization](#1.%20Conversion%20=%3E%20Goals%20=%3E%20Funnel%20Visualization)
	- [2. Conversion => Goals => Goal Flow](#2.%20Conversion%20=%3E%20Goals%20=%3E%20Goal%20Flow)
---------------------
### Funnel Description
#### Funnel Meaning 
عبارت Funnel به معنای قیف میباشد. در Google Analytics قیف Funnel به چهار موضوع زیر میپردازد که مراحلی است که برای رسیدن به یک هدف انجام میشود:
1. Awareness - ورودی ها
2. Interest - علاقه مندی
3. Decision - تصمیم
4. Action - اقدام
5. Image:
	1. ![Pasted image 20260201202830.png](/images/python/Pasted image 20260201202830.png)
#### Funnel Description with Example
برای توضیح Funnel نیاز به یک مثال داریم، فرض کنید هدف ما "فروش 1000 عدد دوره سئو" میباشد که برای رسیدن به این هدف تبلیغاتی را درون شبکه های اجتماعی یا سطح وب انجام میدهیم. از هر تبلیغی که انجام میدهیم کاربرانی به شکل زیر جذب میشوند:
1. **Awareness - ورودی ها:**
	1. ورودی هایی که از طریق این تبلیغ بدست می آوریم که تعداد آنها نسبت به مراحل بعدی بیشتر است.
	2. در واقع View هایی که هر یک از مطالب ما دارد Awareness یا ورودی مطلب ما محسوب میشود که میتوانیم در برنامه نویسی وبسایت نمایش این مطلب را پیاده سازی کنیم:
		1. ![Pasted image 20260201203816.png](/images/python/Pasted image 20260201203816.png)
	3. تعدادی از افراد در همین مرحله از Funnel خارج میشوند.
2. **Interest - علاقه مندی:**
	1. تعدادی از کاربران ورودی از طریق تبلیغ به موضوع ما یعنی "دوره سئو" علاقه نشان میدهند و آنرا به لیست علاقه مندی خود اضافه میکنند.
	2. برای اینکه تعداد بیشتر افرادی که Awareness داشتند به مرحله Decision بروند باید در مطلب علاقه مندی Interest ایجاد کنیم که اینکار را با شرح جذاب سر فصل ها، گذاشتن ویدئو معرفی، قیمت مناسب، نظرات مناسب کاربران و ... پیاده سازی میکنیم.
	3. تعدادی از افراد در همین مرحله از Funnel خارج میشوند.
3. **Decision - تصمیم:**
	1. سپس تعدادی از افرادی که علاقه مندی نشان دادند وارد مرحله تصمیم گیری برای خریدن یا نخریدن این "دوره سئو" میشوند. 
	2. تعدادی از افراد در همین مرحله از Funnel خارج میشوند.
4. **Action - اقدام:**
	1. اما مرحله آخر تعداد کاربرانی که "دوره سئو" را خریداری میکنند و دانشجوی این دوره میشوند را به ما نشان میدهد که ما را برای رسیدن به هدف نهایی یعنی فروش "1000 دوره سئو" نزدیک میکند.
	2. در واقع Funnel میگوید تعداد افرادی که ورودی یک تبلیغ هستند هر چه به مرحله بعدی میروند تعدادشان کمتر میشود و تعدادی از آنها اقدام به خرید Action میکنند.
#### Funnel Usages
1. بررسی اینکه تبلیغاتی که انجام دادیم چقدر بازدهی داشته است.
2. بررسی اینکه ضعف اینکه هدف ما نهایی نمیشود چیست.
3. بررسی اینکه آیا تبلیغات ما با هدف ما سازگاری داشته است یا خیر
### Google Analytics => Conversion => Goals => Funnels

#### 0. Define Goal with Funnel
1. `Google Analytics => Admin => Goals => +New Goal `
	1. Name: Product Sale
	2. Type: Destination
	3. Destination: equals to: https://website.com/sale-complete
		1. آدرس صفحه تبریک خرید شما با موفقیت انجام شد را در این قسمت میگذاریم.
	4. Value: 1$
	5. Funnel: ON
2. **Enter Funnel Details(Steps):**
	1. *Description:*
		1. با روشن کردن گزینه Funnel میتوانیم مراحلی که برای رسیدن به هدف باید طی شود را مشخص کنیم. 
		2. در واقع میتوانیم آدرس صفحاتی را معرفی کنیم که مقادیر هر کدام از Awareness, Interest, Decisions, Action را بدست بیاوریم.
	2. **Step 1:**
		1. Name: Card(سبد خرید)
		2. Screen/Page: https://example.com/cart - آدرس سبد خرید
		3. Required: Yes
	3. **Step 2:**
		1. Name: Vault(کیف پول)
		2. Screen/Page: https://example.com/vault - آدرس صفحه کیف پول
	4. **Step 3:**
		1. Name: Checkout(تسویه حساب)
		2. Screen/Page: https://example.com/checkout - آدرس صفحه تسویه حساب
	5. Click on `Save`
	6. *Image:*
		1. ![Pasted image 20260201205812.png](/images/python/Pasted image 20260201205812.png)
#### 1. Conversion => Goals => Funnel Visualization
0. **Description:**
	1. در این منو نمودار و آمار هایی از نحوه رسیدن به هدف و مقادیری که هدف ما را تمام کرده اند را مشاهده میکنیم:
	![Pasted image 20260201204411.png](/images/python/Pasted image 20260201204411.png)
1. **First Chart:**
	1. در نمودار اولیه و بالای وبسایت آماری از رسیدن به اهداف با بازه زمانی نشان میدهد.
	2. مثلا در چه روزی چه تعدادی از هدف ما done شده است. همچنین آماری مسیری که برای رسیدن به کل هدف ما طی شده است نیز نمایش داده میشود که در تصویر زیر 11% کل هدف طی شده است:
		1. ![Pasted image 20260201204703.png](/images/python/Pasted image 20260201204703.png)
2. **Goal Funnels Steps | Description:**
	1. در قسمت پایینی هر Funnel Step را با آمار ورودی و خروجی آن مشاهده میکنیم:
		1. ![Pasted image 20260201204958.png](/images/python/Pasted image 20260201204958.png)
	2. در هر مرحله ورودی آن به همراه خروجی آن قابل مشاهده است که در واقع با استفاده از آن میتوانیم مشاهده کنیم که مثلا چند نفر از Awareness به Interest و سپس به Decision و در آخر به Action رفتند و خروجی در هر مرحله چقدر بوده است.
	3. با استفاده از این آمار میتوانیم مشکلی که در هر مرحله برای رسیدن به Goal وجود دارد را شناسایی کنیم و به رفع آن بپردازیم.
3. **Goal Funnels Steps | Reading:**
	1. *Step 1 Reading:*
		1. در تصویر زیر مشاهده میکنیم که 2296 نفر به صفحه Cart ورود کردند که 1782 نفر آنها در این مرحله خارج شده اند.
		2. همچنین صفحاتی که افراد از آنجا به Cart وارد شده اند به همراه صفحاتی که پس از خروج از Cart به آنجا رفتند نیز قابل مشاهده هستند. عبارت exit هم به معنای خروجی کلی از وبسایت پس از مشاهده Cart است:
			1. ![Pasted image 20260201210625.png](/images/python/Pasted image 20260201210625.png)
		3. در اینجا مشاهده میکنیم که 601 نفر از این مرحله وبسایت ما را ترک کرده اند و بقیه به صفحات `signin, home, store, basket` رفتند بنابراین اگر امکانی را برای ورود/ثبت نام و مشاهده سبد خرید در اینجا قرار میدادیم آمار خروج از این مرحله کاهش پیدا میکرد.
	2. *Step 2 Reading:*
		1. سپس 514 نفر یعنی 22.39 درصد کاربران از Cart به صفحه Billing and Shipping که قدم دوم Funnel ما(Interest) است رفته اند که 228 نفر آنها از اینجا از وبسایت خارج شده اند:
			1. ![Pasted image 20260201210849.png](/images/python/Pasted image 20260201210849.png)
		2. در اینجا مشاهده میکنیم که 107 نفر از این مرحله وبسایت ما را ترک کرده اند و بقیه به صفحات `yourinfo, home, basket, myaccount` رفتند بنابراین اگر امکانی را برای مشاهده اطلاعات کاربر، دسترسی به داشبورد کاربری و مشاهده سبد خرید در اینجا قرار میدادیم آمار خروج از این مرحله کاهش پیدا میکرد.
	3. *Step 3 Reading:*
		1. سپس 286 نفر یعنی 55.64 درصد کاربران از Billing and Shipping به صفحه Payment که قدم سوم Funnel ما(Decision) است رفته اند که 242 نفر آنها از اینجا از وبسایت خارج شده اند:
			1. ![Pasted image 20260201211046.png](/images/python/Pasted image 20260201211046.png)
	4. *Step 4 Reading:*
		1. سپس 44 نفر یعنی 15.38 درصد کاربران از Payment به صفحه Review که قدم چهارم Funnel ما(Action) است رفته اند که 23 نفر آنها از اینجا از وبسایت خارج شده اند و 21 نفر آنها هدف ما را Done کردند(Purchase Completed)
			1. ![Pasted image 20260201211246.png](/images/python/Pasted image 20260201211246.png)
	5. *Note:*
		1. در این نمودار مشاهده میکنیم که از 2296 نفر که ورودی Awareness داشتیم تعدد 21 نفر آنها Action کردند.
		2. این آمار نشان دهنده نقطه ضعفی در قسمتی از Funnel ماست که با برطرف کردن آن میتوانیم تعداد افرادی که Action کردند را افزایش دهیم.
#### 2. Conversion => Goals => Goal Flow
1. **Description:**
	1. در این منو Flow Chart از اهداف خود با مسیر ورودی آنها(direct, organic, campaign, ...) را مشاهده میکنیم:
		1. ![Pasted image 20260201212048.png](/images/python/Pasted image 20260201212048.png)
	2. در اینجا هم میتوانیم ابتدا گزارش ورودی را از یک قسمت Highlight کنیم و سپس به مشاهده Step های بعدی آن بپردازیم.
### !