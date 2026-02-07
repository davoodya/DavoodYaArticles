---
Episode: E21
Date: 2026-01-22
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
Pervious Episode: "[[E20 - Page Load Speed(Optimized & Increased)]]"
Next Episode: "[[E22 - Meta Tags]]"
---
-------
## TOC
- [robots.txt File](#robots.txt%20File)
	- [Whats `robots.txt`?](#Whats%20%60robots.txt%60?)
	- [robots.txt Parameters](#robots.txt%20Parameters)
- [Control robots.txt Using Meta Tags](#Control%20robots.txt%20Using%20Meta%20Tags)
	- [Description](#Description)
	- [Index, Follow](#Index,%20Follow)
	- [Meta Tags for robots.txt Management](#Meta%20Tags%20for%20robots.txt%20Management)
- [Create robots.txt](#Create%20robots.txt)
- [Writing  robots.txt for All Situations](#Writing%20%20robots.txt%20for%20All%20Situations)
---------
### robots.txt File
#### Whats `robots.txt`?
1. وقتیکه خزنده های موتور جستجو به یک وبسایت میرسند در اولین قدم به سراغ فایلی بنام `robots.txt` میگردد:
	1. ![[Pasted image 20260122212030.png]]
2. در واقع `robots.txt` دستور العمل وبسایت برای موتور جستجو است که چگونه با این وبسایت برخورد کند.
3. در واقع در `robots.txt` مشخص میکنیم کدام صفحات ایندکس شوند و کدام صفحات ایندکس نشوند.
4. در واقع اگر میخواهیم تمام وبسایت ما توسط گوگل ایندکس شود وجود این فایل ضروری نیست(مثلا صفحات که برای مدیر هستند و بهتر است برای جلوگیری از نفوذ توسط گوگل ایندکس نشوند) 
5. اما در بعضی مواقع نمیخواهیم قسمتی از وبسایت ایندکس شود که در اینصورت باید که وجود داشته باشد.
#### robots.txt Parameters
1. `user-agent`
	1. در این قسمت نام ربات جستجو گر را مینویسیم تا بتوانیم رفتار مشخصی را برای هر ربات جستجو گر در نظر بگیریم:
		1. `user-agent: googlebot` Google Search Engine Bot
		2. `user-agent: Googlebot-Image` Google Image Search Engine Bot
	2. اگر هم از `*` استفاده کنیم به معنای تمام ربات هاست:
		1. `user-agent: *` All Bots
	3. در URL زیر میتوانیم نام ربات های جستجوگر را مشاهده کنیم که بیش از 300 ربات هستند که هر کدام نیز رفتار مشخصی دارند:
		1. https://robotstxt.org/db.html
			1. ![[Pasted image 20260122212638.png]]
2. `allow:`
	1. آدرس هایی که خزنده گوگل اجازه ایندکس آنها را دارد در این پارامتر مشخص میشود.
	2. `allow: /` Mean All Pages in domain 
3. `disallow:`
	1. آدرس هایی که خزنده گوگل اجازه ایندکس آنها را ندارد در این پارامتر مشخص میشود. مانند صفحات کاربری مدیر یا `wp-admin` که نیازی نیست توسط گوگل ایندکس شوند.
4. `sitemap:`
	1. در این پارامتر نیز آدرس URL نقشه سایت Site Map قرار میگیرد.
	2. `sitemap: https://site.com/sitemap.xml`
### Control robots.txt Using Meta Tags
#### Description
روش دیگری که برای مدیریت پارامتر های `robots.txt` وجود دارد استفاده از Meta Tags های مربوط به `robots.txt` است که میتوانیم در هر صفحه از آنها استفاده کنیم:
	![[Pasted image 20260122213042.png]]
#### Index, Follow 
1. Follow, No Follow
	1. اگر Follow مقدار برای Meta Tags در نظر گرفته شود یعنی لینک های درون صفحه را دنبال کن(Internal, External)
	2. اگر No Follow برای Meta Tags در نظر گرفته شود یعنی لینک های درون صفحه را دنبال نکن(Internal, External)
2. Index, No Index
	1. اگر Index برای Meta Tags در نظر گرفته شود یعنی صفحه مورد نظر را ایندکس کن.
	2. اگر No Index برای Meta Tags در نظر گرفته شود یعنی صفحه مورد نظر را ایندکس نکن.
#### Meta Tags for robots.txt Management
بطور کلی Syntax نوشتن Meta Tags های مدیریت robots.txt به صورت زیر است:
```html
<META NAME="ROBOT-NAME" CONTENT="FOLLOW, INDEX">
```
بنابراین تگ های مدیریتی به شکل زیر میشوند:
```html
<META NAME="ROBOTS" CONTENT="INDEX, FOLLOW">
<META NAME="ROBOTS" CONTENT="NOINDEX, FOLLOW">
<META NAME="ROBOTS" CONTENT="INDEX, NOFOLLOW">
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">

<META NAME="googlebot" CONTENT="INDEX, FOLLOW">
```
- *تصویر:*
	- ![[Pasted image 20260122213723.png]]
- *نکته:* نام ربات Google Images ها متفاوت از ربات اصلی گوگل است و نام آن `Googlebot-Image` است، بنابراین میتوان تصاویر یک صفحه را ایندکس نکرد اما محتوای آنرا ایندکس کرد.
### Create robots.txt
- فایل `robots.txt` حتما باید در Root پروژه ایجاد شود.
1. Disallow Path in Website
```txt
User-Agent: *
disallow: */wp-admin/ #OR disallow: /wp-admin/
```
2. Disallow a Picture Indexing for `Googlebot-Image`
```txt
User-Agent: Googlebot-Image
disallow: /Images/Logo.png
disallow: /Images/Admin/*
```
3. Disallow Type of Pictures(gif) for all bots
```txt
User-Agent: *
disallow: /*.gif$
```
- *Picture:*
	- ![[Pasted image 20260122214325.png]]
### Writing  robots.txt for All Situations 
نوشتن `robots.txt` برای تمام حالت های ممکن یک امتیاز مثبت برای گوگل و سایر موتور جستجو ها محسوب میشود و باعث میشود موتور جستجو بصورت ریزبینانه به وبسایت ما بنگرد.
- همچنین برای افزایش امنیت وبسایت و جلوگیری از نفوذ به داشبورد ادمین هم استفاده از `robots.txt` بسیار کاربردی است زیرا که میتوانیم URL هایی که قرار نیست در دسترس عموم باشد را از نتایج موتور جستجو حذف کنیم.
### robots.txt Sample
در زیر نمونه یک فایل استاندارد `robots.txt` را مشاهده میکنید:
```robot
User-agent: *
Allow: /
Sitemap: https://davoodya.com/sitemap.xml

# Allow all web crawlers to access all content
User-agent: *
Disallow:

# Specific rules for major search engines
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: Yandexbot
Allow: /

# Prevent crawling of certain file types
User-agent: *
Disallow: /*.pdf$
Disallow: /*.doc$
Disallow: /*.docx$
Disallow: /*.xls$
Disallow: /*.xlsx$
Disallow: /*.zip$
Disallow: /*.rar$

# Prevent crawling of admin or private areas
User-agent: *
Disallow: /admin/
Disallow: /private/
Disallow: /temp/

# Crawl delay to prevent server overload
User-agent: *
Crawl-delay: 10

```