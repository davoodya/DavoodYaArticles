---
Episode: E36
Date: 2026-01-29
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
Pervious Episode: "[[E35 - Google Analytics(Behavior - Site Speed)]]"
Next Episode: "[[E37 - Google Analytics(Behavior - Events)]]"
---
-------
## TOC
- [Google Analytics => Behavior => Site Search Tab](#Google%20Analytics%20=%3E%20Behavior%20=%3E%20Site%20Search%20Tab)
	- [0. Description](#0.%20Description)
		- [0.1: Site Search Description](#0.1:%20Site%20Search%20Description)
		- [0.2: Enable Site Search](#0.2:%20Enable%20Site%20Search)
		- [0.3: Metrics](#0.3:%20Metrics)
	- [1. Overview](#1.%20Overview)
	- [2. Usage](#2.%20Usage)
	- [3. Search Term](#3.%20Search%20Term)
	- [4. Search Pages](#4.%20Search%20Pages)
- [Search Topics](#Search%20Topics)
--------------
### Google Analytics => Behavior => Site Search Tab
#### 0. Description
##### 0.1: Site Search Description
در این قسمت آماری از جستجو هایی که کاربران در داخل وبسایت ما انجام میدهند مشاهده میشود. 
- *نکته:* این آمار ربطی که نتایج موتور جستجو ندارد و در واقع جستجو هاییست که کاربر درون وبسایت ما با استفاده از Search Form ها انجام داده است.
- *نکته دوم:* این گزینه بصورت پیشفرض فعال نیست و باید بصورت دستی فعال شود.
##### 0.2: Enable Site Search
1. `Left Sidebar => Click on Gear(goto Settings Panel) => View Settings`
	1. ![[Pasted image 20260129190012.png]]
2. `in View Settings => Scroll Down => Turn On => Site Search Tracking => Save` 
	1. ![[Pasted image 20260129190117.png]]
3. **Now we Should Update `gtag.js` Code:**
	1. در قدم بعدی باید اسکریپت `gtag.js` را که برای رهگیری وبسایت اضافه کردیم را بروز رسانی کنیم.
	2. برای اینکار نیاز داریم که آدرس صفحه جستجو وبسایت خود را بدست بیاوریم که کافیست درون وبسایت خود یک جستجو انجام دهیم و سپس قسمتی از URL که جستجو را انجام میدهد کپی کنیم:
		1. ![[Pasted image 20260129190502.png]]
	3. حال تگ `gtag.js` را به شکل زیر بروز میکنیم و در واقع خط زیر را به تکه اسکریپت اضافه میکنیم:
		1. `ga('send', 'pageview', '/Search?srch=keyword');`
			1. ![[Pasted image 20260129190710.png]]
	4. همانطور که گفتیم پارامتر جستجو در هر وبسایت متفاوت است و مثلا برای تاپ لرن باید خط به شکل زیر اضافه شود:
		1. `ga('send', 'pageview', '/courses?search=keyword' );`
			1. ![[Pasted image 20260129191159.png]]
```html
<script>
	...
	
	// Add below line for Site Search
	ga('send', 'pageview', '/Search?srch=keyword');
	
	...
</script>
```
4. **Note:** `keyword` is static and should be add instead of query
	1. کلمه `keyword` حتما باید در در مقابل **=** وجود داشته باشد. 
5. **Note 2:** After Enable features, Metrics add within days
	1. پس از فعالسازی این گزینه آمار ها پس از چند روز نمایش داده میشود.
6. **Full Script Codes:**
```html
<!-- Global site tag (gtag.js) - Google Analytics -->

<script async src="https://www.googletagmanager.com/gtag/js?id=UA-129154796-1"></script>
	<script>
	window.dataLayer = window.dataLayer | | [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());
	
	// Add below line for Site Search
	ga('send', 'pageview', '/courses?search=keyword' );
	
	gtag('config', 'UA-129154796-1');
</script>
```
##### 0.3: Metrics
1. **Sessions with Search:**
	1. تعداد کل جستجو ها
2. **Total Unique Search:**
	1. تعداد جستجو های تک
3. **Result Pageview / Search:**
	1. میانگین تعداد جستجو و مشاهده صفحه
4. **% Search Exit:**
	1. تعداد درصد کاربرانی که پس از جستجو از وبسایت خارج شده اند.
5. **% Search Refinements:**
	1. تعداد درصد کاربرانی که به نتیجه مورد نظر خود پس از جستجو رسیده اند.
	2. مهمترین پارامتر Site Search این پارامتر است.
6. **Time After Search:**
	1. زمانیکه کاربر پس از جستجو درون وبسایت مانده است که هر چه بالاتر باشد بهتر است.
7. **Avg. Search Depth:** Research Topic
	1. میانگین عمقی که کاربر با جستجو وارد وبسایت شده است.
#### 1. Overview
1. **Description:**
	1. در این منو آماری کلی از جستجو درون وبسایتی کاربر مشاهده میشود:
		1. ![[Pasted image 20260129191750.png]]
2. **Search Chart:**
	1. در قسمت اول آماری از جستجو ها نشان داده میشود که بصورت پیشفرض بر روی Sessions with Search تنظیم است اما قابل عوض کردن و همچنین اضافه کردن رقیب برای بررسی هم وجود دارد:
		1. ![[Pasted image 20260129191936.png]]
3. **Number Metric:**
	1. در قسمت بعدی آمار های عددی Metric های Site Search قابل مشاهده است که در کنار آن نیز نمودار دایره ای از Site Search نیز قرار دارد:
		1. ![[Pasted image 20260129192034.png]]
4. **Site Search Metrics Based on Search Terms, Site Search Category, Start Page:**
	1. در قسمت Search Terms عبارت هایی که در وبسایت ما جستجو شده است را مشاهده میکنیم:
		1. ![[Pasted image 20260129192147.png]]
	2. در قسمت Site Search Category دسته بندی ها یا همان دسته بندی جستجو ها را نمایش میدهد.
	3. در قسمت Start Page هم صفحاتی که کاربر جستجو را از داخل آنها شروع کرده است نمایش داده میشود.
	4. *تصویر:*
		1. ![[Pasted image 20260129192305.png]]
#### 2. Usage
- در این گزینه تعداد کل کاربران که وارد وبسایت ما شده اند را در دو دسته بندی زیر نمایش میدهد:
	1. Visits without Search
		1. کاربرانی که وارد شده اند اما جستجو نکردند.
	2. Visits With Search
		1. کاربرانی که وارد شدند و جستجو کردند.
	3. Image:
		1. ![[Pasted image 20260129192620.png]]
1. **Usage:**
	1. از این قسمت میتوانیم متوجه شویم که آیا قسمت جستجو وبسایت موثر بوده یا نه؟
	2. آیا قسمت جستجو در جلوی چشم کاربر هست یا نه؟
#### 3. Search Term 
در این منو کلمات که کاربر آنها را در وبسایت جستجو کرده را مشاهده میکنیم:
	![[Pasted image 20260129192854.png]]
2. **Usage:**
	1. میتوانیم متوجه شویم کدام مطلب ما بیشتر مورد توجه مخاطب است. 
	2. و یا اینکه کدام مطلب را باید به جلوی چشم مخاطب بیاوریم.
#### 4. Search Pages
این منو هم نشان میدهد که جستجو های درون وبسایت ما از کدام صفحات شروع شده اند:
	![[Pasted image 20260129192947.png]]
1. **Usage:**
	1. متوجه میشویم که در کدام صفحات چه لینک دهی بهتر است انجام شود.
### Search Topics
1. **Avg. Search Depth:**
	1. مقدار **Avg. Search Depth:** که یکی از Metric های درون Google Analytics(Behavior - Site Search) میباشد دقیقا چه آماری را نشان میدهد؟
### !