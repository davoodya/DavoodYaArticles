---
Episode: E29
Date: 2026-01-26
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 10:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E28 - Google Webmaster Tools, Other Menu's]]"
Next Episode: "[[E30 - Google Analytics Menus]]"
---
-------
## TOC
- [Google Analytics](#Google%20Analytics)
	- [What is Google Analytics?](#What%20is%20Google%20Analytics?)
	- [Start Work with Google Analytics](#Start%20Work%20with%20Google%20Analytics)
		- [Signup and Add Website](#Signup%20and%20Add%20Website)
		- [Copy `gtag.js` to all your Website Pages](#Copy%20%60gtag.js%60%20to%20all%20your%20Website%20Pages)
		- [Access Google Analytics Dashboard](#Access%20Google%20Analytics%20Dashboard)
---------------
### Google Analytics
#### What is Google Analytics?
ابزار Google Analytics یکی دیگر از ابزار های گوگل است که برای بررسی و تحلیل رفتار کاربران وبسایت بصورت Real Time بکار میرود. 
- موارد که Google Analytics بررسی میکند:
	1. کاربران وبسایت ما از کجا وارد وبسایت شده اند.
	2. کاربران وبسایت ما به کدام صفحات بیشترین مراجعه را دارند.
	3. کدام یک از صفحات وبسایت ما الان بالاترین بازدید را دارد.
	4. کدام قسمت از کدام صفحه بیشترین بازدید را به خود اختصاص میدهد.
	5. کاربران از کدام صفحات به کدام صفحات وبسایت میروند.
	6. بیشترین بازدید ما در چه ساعاتی از روز انجام شده است.
	7. کاربران از کدام صفحه از وبسایت ما خارج شده اند.
	8. مشاهده محصولات پر بازدید در یک وبسایت
- **نکته:** در مواردی که یک فروشگاه خریدار ندارد دقیقا باید از این ابزار استفاده کنیم. در واقع ممکن است یک محصول بازدید زیادی را از گوگل دریافت کند اما محصول خریداری نشود. در این مواقع با استفاده از Google Analytics باید بررسی کنیم که مشکل این محصول از کجاست.
- **نکته دوم:** این ابزار در ایران تحریم است و در نتیجه برای استفاده باید از تحریم شکن ها استفاده کنیم. همچنین اگر هاست وبسایت ما خارج از ایران باشد Google Analytics بدون مشکل روی آن کار میکند اما اگر داخل ایران باشد به خطا میخورد.
#### Start Work with Google Analytics
##### Signup and Add Website
1. goto https://analytics.google.com and Signup
2. **Add Your information:**
	1. Select Website or Mobile App
	2. Account Name
	3. Website Name
	4. Website URL
	5. *Industry Category:*
		1. در این گزینه زمینه فعالیت وبسایت مثلا Shopping را مشخص میکنیم.
	6. Reporting Time Zone
	7. Check Necessary Ticks
	8. *Image:*
		1. ![[Pasted image 20260126214543.png]]
3. Click on `Get Tracking ID`
4. Check Necessary Ticks and Click on `I Accept`
	1. ![[Pasted image 20260126214712.png]]
##### Copy `gtag.js` to all your Website Pages
1. پس از ثبت نام در Google Analytics و اضافه کردن وبسایت، ابزار Google Analytics یک تکه کد Java Script را به من میدهد که این تکه کد را باید در تمامی صفحات وبسایت خود قرار دهیم:
	1. ![[Pasted image 20260126215026.png]]
	2. ![[Pasted image 20260126215238.png]]
2. گوگل با استفاده از این تکه کد است که میتواند رفتار کاربر را در تمامی صفحات ما رهگیری کند و همچنین برای Verify کردن وبسایت ما نیز از این تکه کد استفاده میکند.
3. به این کد Tracking Code گفته میشود.
- **نکته:** در صفحات Admin و مدیریتی نیازی به قرار دادن این اسکریپت در صفحه نیست.
##### Access Google Analytics Dashboard
پس از اضافه کردن Tracking Code به صفحات پروژه خود میتوانیم به تمام امکانات درون داشبورد Google Analytics دسترسی داشته باشیم:
	![[Pasted image 20260126215422.png]]
- در صفحه Home ابزار Google Analytics میتوانیم خلاصه ای از فعالیت ها و رفتار های کاربران را مشاهده کنیم:
	- ![[Pasted image 20260126215515.png]]
### !