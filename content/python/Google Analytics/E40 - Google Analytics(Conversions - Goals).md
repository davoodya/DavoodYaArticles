---
Episode: E40
Date: 2026-01-31
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 14:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E39 - Conversion Definitions and Concepts]]"
Next Episode: "[[E41 - Google Analytics(Conversions - Goals - Funnels)]]"
---
-------
### Demo Account Google Analytics
ابزار Google Analytics یک اکانت بنام Demo Account Google Analytics دارد که برای تست قابلیت های Google Analytics و تمرین و یادگیری آن استفاده میشود.
این اکانت بسیار برای خواندن تحلیل ها و یادگیری Google Analytics مناسب میباشد.
1. Demo Account Google Analytics(Web Traffics)
	1. https://analytics.google.com/analytics/index/demoaccount?appstate=/p213025502
2. Demo Account Google Analytics(App & Web Traffic)
	1. https://analytics.google.com/analytics/index/demoaccount?appstate=/p153293282
3. [Read More:](https://support.google.com/analytics/answer/6367342?hl=en#uses&zippy=%2Cin-this-article)
	1. https://support.google.com/analytics/answer/6367342?hl=en#uses&zippy=%2Cin-this-article
### Google Analytics => Conversion => Goals
#### 0. Add Goal
1. `Google Analytics => Conversion => Goals => Overview => Setup Goals`
	1. برای تعریف هدف ها در منو Overview بر روی Setup Goals کلیک میکنیم:
		1. ![[Pasted image 20260131161208.png]]
	2. سپس هم در صفحه باز شده بر روی New Goal کلیک میکنیم تا هدف جدید را تعریف کنیم:
		1. ![[Pasted image 20260131161526.png]]
2. `Google Analytics => Settings Gear => Goals`
	1. روش دیگر تعریف هدف ها رفتن به منو بالاست که در واقع با کلیک بر روی Setup Goals هم به این منو منتقل میشویم:
		1. ![[Pasted image 20260131161437.png]]
	2. با انتقال به این صفحه با کلیک بر روی New Goal میتوانیم هدف جدید را تعریف کنیم:
		1. ![[Pasted image 20260131161526.png]]
3. **New Goal Options:**
	1. *Description:*
		1. با کلیک بر روی New Goals باید گزینه های ساخت هدف را مقدار دهی کنیم.
	2. *Goal Setup:*
		1. *Template:*
			1. در این گزینه میتوانیم از قالب های موجود در Google Analytics که برای ساخت هدف موجود است استفاده کنیم:
				1. ![[Pasted image 20260131161838.png]]
			2. *این قالب ها بسیاری از کارها از جمله موارد زیر را پوشش میدهند:*
				1. تعداد کاربران که اکانت جدید ساختند.
				2. تعداد کاربران که بر روی صفحه مشخص کلیک کردند.
				3. تعداد کاربران که در خبرنامه ثبت نام کردند.
				4. تعداد کاربران که Live Chat کردند.
				5. تعداد کاربران که خرید کردند یا پیش سفارش ثبت کردند.
				6. تعداد کاربران که Media بخش کردند.
				7. تعداد کاربران که اشتراک گذاری در صفحات اجتماعی را انجام داده اند. 
				8. تعداد کاربران که محصولی را به لیست مورد علاقه اضافه کردند.
				9. تعداد کاربران که مقایسه محصول انجام دادند. 
				10. تعداد کاربران که نظرات وبسایت خواندند. و ....
		2. *Custom:*
			1. با کلیک بر روی این گزینه نیز میتوانیم هدفی مشخص و شخصی سازی شده را بسازیم.
			2. *Name:*
				1. انتخاب نام برای هدف
			3. *Goal Slot ID:*
				1. انتخاب آیدی و شماره برای هدف
			4. *Type:*
				1. انتخاب نوع هدف بر اساس موارد زیر:
				2. *Destination:*
					1. کاربرانی که به یک صفحه مشخص میروند. 
					2. برای این مثال این گزینه را استفاده میکنیم و آدرس صفحه "ثبت نام با موفقیت" انجام شد را میدهیم تا تعداد کاربران ثبت نام شده در وبسایت را هدف گذاری کنیم.
				3. *Duration:*
					1. مدت زمان 
				4. *Page/Screens per Sessions:*
					1. تعداد صفحات در هر Sessions
				5. *Events:*
					1. بر اساس یک رویداد خاص مثلا Play یک ویدئو
				6. *Image:*
					1. ![[Pasted image 20260131162823.png]]
			5. *Goal Details => Destination:*
				1. بر اساس Type هدف متفاوت میباشد و باید مقدار دهی شود. 
				2. در اینجا آدرس صفحه "ثبت نام" موفق بود را میدهیم. 
				3. و یا میتوان صفحه خرید موفق برای یک دوره خاص را گذاشت تا درآمد یک دوره را داشته باشیم.
				4. برای مقایسه این مقصد از Equal to, Begins With , Regular Expression میتوان استفاده کرد:
					1. ![[Pasted image 20260131163351.png]]
			6. *Value:*
				1. میتوان مقدار پول را مشخص کرد که مثلا هر کاربر که به این صفحه وارد شده 5 دلار در آمد برای من داشته که با استفاده از آن میتوان هدف مالی را بررسی کرد.
			7. *Funnel(Optional):*
				1. در اینجا آدرس صفحه ای که انتظار داریم کاربر پس از مشاهده Destination به آن برود را وارد میکنیم.
				2. این مورد در بررسی نحوه تعامل کاربر، صفحه مورد علاقه آن و یافتن Exit Page ها استفاده میشود.
			8. *Save:*
				1. ![[Pasted image 20260131163403.png]]
	3. *See Created Goals:*
		1. پس از اینکه هدف مورد نظر را ساختیم آنرا در جدول هدف ها مشاهده میکنیم و درصدی که به آن هدف نزدیک شده ایم را میتوانیم ببینیم:
			1. ![[Pasted image 20260131163545.png]]
		2. پس از پایان و رسیدن به هدف هم میتوان Recording را Off کنیم تا ردیابی هدف خاموش شود.
		3. پس از اضافه کردن هدف برای مشاهده هدف در  منو Conversions => Goals دو سه روزی باید صبر کرد.
4. **See Goal Details:**
	1. برای مشاهده نتیجه هدف میتوانیم به `Google Analytics => Settings Gear => Goals` و یا پس از چند روز به `Google Analytics => Conversion => Goals` برویم.
	2. در نتیجه هدف ها، تعداد انجام هدف در 7 روز گذشته، نوع هدف، ID و اسم هدف مشاهده میشود که ه مهمترین آنها Past 7 Days Conversions میباشد:
	3. نتیجه هدف در `Google Analytics => Settings Gear => Goals`
		1. ![[Pasted image 20260131164349.png]]
	4. نتیجه هدف در `Google Analytics => Conversion => Goals`
		1. ![[Pasted image 20260131164529.png]]
#### 1. Metrics Description
1. **Goal Completions:**
	1. تعداد افرادی که هدف را انجام داده اند.
2. **Goal Value:**
	1. ارزش(پول) که اهداف برای ما داشته است.
3. **Goal Conversions Rate:**
	1. درصد کاربرانی که اهداف ما را انجام داده اند.
4. **Total Abandonment Rate:**
	1. درصد کاربرانی که اهداف ما را دنبال کردند اما در وسط راه آنرا رها کردند.
5. **Each Goals as Metric:**
	1. هر هدف هم که تعریف کردیم به عنوان یک Metric با تعداد افرادی که آنها را انجام داده اند در آمار ها نشان داده میشود.
6. *Image:*
	1. ![[Pasted image 20260131165802.png]]
#### 2. Overview
1. **Description:**
	1. در این پنجره آمار کلی از اهداف با Metric های تعریف شده مشاهده میشود:
		1. ![[Pasted image 20260131165853.png]]
2. **Main Chart & Numeric Metrics:**
	1. در بخش بالایی این منو آمار کلی از اهداف و همچنین آمار اعدادی Metric ها را میتوان مشاهده کرد.
3. **Goal Completion Locations:**
	1. در پایین صفحه نیز صفحاتی که اهداف ما در آن صفحات انجام میشوند را مشاهده میکنیم:
		1. ![[Pasted image 20260131170034.png]]
#### 3. Goal URLs
در این گزینه آمار Goal Completion Locations بصورت کلی و دقیق با جزئیات نمایش داده میشود:
	![[Pasted image 20260131170357.png]]
1. اگر Value مشخص کرده باشیم میتوانیم در آمدی که هر هدف برای ما داشته است را نیز مشاهده کنیم.
2. همچنین میتوانیم این آمار را برای یک هدف مشخص نشان دهیم که برای اینکار میتوانیم از فیلتر بالای صفحه استفاده کنیم:
	1. ![[Pasted image 20260131170537.png]]
#### 4. Reverse Goal Path
در این گزینه مراحلی(صفحات) که کاربر طی کرده تا به هدف ما برسد و آنرا done کند را مشاهده میکنیم:
	![[Pasted image 20260131170655.png]]
مثلا کاربر از صفحه اصلی به صفحه دوره ها آمده و سپس به صفحه یکی از دوره ها و در آخر به صفحه پرداخت که هدف ما بوده رفته است.
- **نکته:** در اینجا میتوانیم متوجه شویم که کدام صفحات ما برای رساندن کاربر به هدف بیشترین استفاده را دارد. سپس میتوانیم به بهینه سازی آن صفحه از وبسایت بپردازیم.
### !