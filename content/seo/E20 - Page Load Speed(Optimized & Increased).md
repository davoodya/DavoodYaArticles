---
Episode: E20
Date: 2026-01-22
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 43:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E18, E19 - Start On Page SEO]]"
Next Episode: "[[E21 - robots.txt]]"
---
-------
# TOC
- [E20 - Increase Speed of Website Loading](#E20%20-%20Increase%20Speed%20of%20Website%20Loading)
	- [SEO Tools](#SEO%20Tools)
		- [Tools Until Here](#Tools%20Until%20Here)
		- [Speed Checking Tools](#Speed%20Checking%20Tools)
	- [Load Page Speed Description](#Load%20Page%20Speed%20Description)
	- [GT-Metrix Tools](#GT-Metrix%20Tools)
		- [Introduction](#Introduction)
	- [GT-Metrix Analyze Reading](#GT-Metrix%20Analyze%20Reading)
		- [Main(First Section) Details](#Main(First%20Section)%20Details)
		- [GT-Metrix UI Description](#GT-Metrix%20UI%20Description)
		- [GT-Metrix Parameters Description - Page Speed(Google)](#GT-Metrix%20Parameters%20Description%20-%20Page%20Speed(Google))
			- [1. Server Scaled Images](#1.%20Server%20Scaled%20Images)
			- [2. Enable gzip Compression](#2.%20Enable%20gzip%20Compression)
			- [3. Optimize Images](#3.%20Optimize%20Images)
			- [4. Avoid Bad Requests](#4.%20Avoid%20Bad%20Requests)
			- [5. Leverage Browser Caching](#5.%20Leverage%20Browser%20Caching)
			- [6. Specify Image Dimensions](#6.%20Specify%20Image%20Dimensions)
			- [7. Minify CSS](#7.%20Minify%20CSS)
			- [8. Minify HTML](#8.%20Minify%20HTML)
			- [9. Minify JS](#9.%20Minify%20JS)
			- [10. Defer Parsing Java Script](#10.%20Defer%20Parsing%20Java%20Script)
			- [11. Enable Keep-Alive](#11.%20Enable%20Keep-Alive)
			- [12. Avoid Inline Small CSS & JS](#12.%20Avoid%20Inline%20Small%20CSS%20&%20JS)
			- [13. Avoid Landing Page Redirects](#13.%20Avoid%20Landing%20Page%20Redirects)
			- [14. Minimize Redirects](#14.%20Minimize%20Redirects)
			- [15. Minimize Request Size](#15.%20Minimize%20Request%20Size)
			- [16. Optimize the order of Styles and Scripts](#16.%20Optimize%20the%20order%20of%20Styles%20and%20Scripts)
			- [17. Put CSS in the Document Head](#17.%20Put%20CSS%20in%20the%20Document%20Head)
			- [18. Server Resource from a Consistent URL](#18.%20Server%20Resource%20from%20a%20Consistent%20URL)
			- [19. Specify a Cache Validator](#19.%20Specify%20a%20Cache%20Validator)
			- [20. Combine Image Using CSS Sprites](#20.%20Combine%20Image%20Using%20CSS%20Sprites)
			- [21. Avoid CSS @import](#21.%20Avoid%20CSS%20@import)
			- [22. Prefer Asynchronous Resource](#22.%20Prefer%20Asynchronous%20Resource)
			- [23. Specific a Character Set Early *Check Needed*](#23.%20Specific%20a%20Character%20Set%20Early%20*Check%20Needed*)
			- [24. Remove Query String from Static Resources](#24.%20Remove%20Query%20String%20from%20Static%20Resources)
			- [25. Specific a Vary: Accept-Encoding Header](#25.%20Specific%20a%20Vary:%20Accept-Encoding%20Header)
		- [GT-Metrix Parameters Description - YSlow(Yahoo)](#GT-Metrix%20Parameters%20Description%20-%20YSlow(Yahoo))
			- [0. YSlow(Yahoo) Description](#0.%20YSlow(Yahoo)%20Description)
			- [Similar to Page Speed(Google)](#Similar%20to%20Page%20Speed(Google))
			- [1. Add Expires Headers](#1.%20Add%20Expires%20Headers)
			- [2. Use a Content Delivery Network(CDN)](#2.%20Use%20a%20Content%20Delivery%20Network(CDN))
			- [3. Use Cookie-free Domain](#3.%20Use%20Cookie-free%20Domain)
			- [4. Make Fewer HTTP Requests](#4.%20Make%20Fewer%20HTTP%20Requests)
			- [5. Avoid HTTP 404(Not Found) Error](#5.%20Avoid%20HTTP%20404(Not%20Found)%20Error)
			- [6. Make AJAX Cacheable](#6.%20Make%20AJAX%20Cacheable)
			- [7. Remove Duplicate Java Scripts and CSS](#7.%20Remove%20Duplicate%20Java%20Scripts%20and%20CSS)
			- [8. Avoid Alpha Image Loader Filter](#8.%20Avoid%20Alpha%20Image%20Loader%20Filter)
			- [9. Reduce the Number of DOM Elements](#9.%20Reduce%20the%20Number%20of%20DOM%20Elements)
			- [10. Use GET for AJAX Requests](#10.%20Use%20GET%20for%20AJAX%20Requests)
			- [11. Reduce DNS Lookup](#11.%20Reduce%20DNS%20Lookup)
			- [12. Reduce Cookie Size](#12.%20Reduce%20Cookie%20Size)
			- [13. Make Favicon Small and Cacheable](#13.%20Make%20Favicon%20Small%20and%20Cacheable)
			- [14. Configure Entity Tags(ETags)](#14.%20Configure%20Entity%20Tags(ETags))
			- [15. Avoid CSS Expression](#15.%20Avoid%20CSS%20Expression)
		- [GT-Metrix Other Tabs](#GT-Metrix%20Other%20Tabs)
			- [Waterfall](#Waterfall)
			- [Timing](#Timing)
			- [Video](#Video)
			- [History](#History)
	- [Note, Perform Speed Analysis for Each Page](#Note,%20Perform%20Speed%20Analysis%20for%20Each%20Page)
----------------
## E20 - Increase Speed of Website Loading
### SEO Tools
#### Tools Until Here
1. Google ADS
2. Webmaster Tools
3. Woorank
4. Check Page Rank
5. Alexa Firefox and Chrome Extension
#### Speed Checking Tools
برای بررسی سرعت وبسایت میتوانیم از ابزار های زیر استفاده کنیم:
1. Alexa Firefox and Chrome Extension
	1. این افزونه میتواند سرعت لود وبسایت، رتبه وبسایت در الکسا، Traffic Rank, لینک های استفاده شده، Way Back Machine، سایت های مشابه و .... را نشان دهد:
		1. ![Pasted image 20260121213241.png](/images/seo/Pasted image 20260121213241.png)
### Load Page Speed Description
اگر سرعت لود وبسایت بیش از 7 ثانیه تاخیر داشته باشد:
1. کاهش 1 درصدی آمار بازدید کنندگان
2. کاهش 16 درصدی رضایت بازدید کنندگان
3. کاهش 7 درصدی فروش
4. کاهش 50 درصدی Bonus Rate یا پرش کاربران(کاربرانی که وبسایت شما را باز کردند اما دیگر به وبسایت شما باز نمیگردند)
### GT-Metrix Tools
#### Introduction
برای بررسی سرعت لود وبسایت، یافتن کندی ها و مشکلات و همچنین یافتن روش های افزایش سرعت ابزار های زیادی وجود دارند. یکی از بهترین ابزار ها `GT-Metrix` است که امکانات زیادی را برای بررسی سرعت وبسایت و رفع مشکلات آن نیز دارد.
- https://gtmetrix.com
	- ![Pasted image 20260121213713.png](/images/seo/Pasted image 20260121213713.png)
- پس از وارد کردن URL و Analyze وبسایت نتایج اسکن را میتوانیم مشاهده کنیم:
	- ![Pasted image 20260121213748.png](/images/seo/Pasted image 20260121213748.png)
- *نکته:* آنالیز GT-Metrix را هم برای صفحه اصلی و هم برای سایر صفحات مهم وبسایت باید انجام دهیم و در واقع فقط محدود به صفحه اصلی نمیشود.
### GT-Metrix Analyze Reading
#### Main(First Section) Details
1. **Page Speed Score:**
	1. این عدد نشان دهنده سرعت لود وبسایت بر اساس معیار های گوگل است. عدد مناسب باید بالای 75 باشد.
2. **YSlow Score:**
	1. این عدد نشان دهنده سرعت لود وبسایت بر اساس معیار های یاهو است. عدد مناسب باید بالای 80 باشد.
3. **Fully Loaded Time:**
	1. زمانی که صرف لود صفحه شده است. باید زیر 3 ثانیه باشد.
4. **Total Page Size:**
	1. حجم کلی صفحه به مگابایت که باید زیر 1 مگابایت باشد.
5. **Requests:**
	1. تعداد درخواست هایی که برای باز شدن صفحه زده شده است.
6. **Pictures:**
	1. Good Speed Scan:
		1. ![Pasted image 20260121214439.png](/images/seo/Pasted image 20260121214439.png)
	2. Low Speed Scan:
		1. ![Pasted image 20260121214451.png](/images/seo/Pasted image 20260121214451.png)
#### GT-Metrix UI Description
در قسمت بدنه آنالیز معیار هایی که برای افزایش سرعت لود صفحه نیاز است بصورت ریز قابل مشاهده هستند و با دسته بندی های Grade, Type, Priority قابل مشاهده هستند:
	![Pasted image 20260121214609.png](/images/seo/Pasted image 20260121214609.png)
1. **Colors Description:**
	1. این معیار ها دارای رنگ های مختلفی میباشند که هر رنگ معنی خود را دارد.
	2. *رنگ خاکستری:* بدین معناست که معیار مورد نظر در وبسایت رعایت نشده است و در نتیجه در کل امتیاز آن قابل محاسبه نیست:
		1. ![Pasted image 20260121215524.png](/images/seo/Pasted image 20260121215524.png)
	3. *رنگ قرمز:* بدین معناست که پارامتر در وبسایت رعایت شده است اما بدرستی کار نشده است:
		1. ![Pasted image 20260121215603.png](/images/seo/Pasted image 20260121215603.png)
	4. *رنگ نارنجی:* بدین معناست که پارامتر استفاده شده درست کار شده است و امتیاز مثبت هم داشته اما قابل بهبود دارد:
		1. ![Pasted image 20260121215801.png](/images/seo/Pasted image 20260121215801.png)
	5. *رنگ سبز کم رنگ:* بدین معناست که پارامتر استفاده بدرستی کار شده و بهینه هم هست اما باز هم قابلیت بهینه تر شدن دارد:
		1. ![Pasted image 20260121215905.png](/images/seo/Pasted image 20260121215905.png)
	6. *رنگ سبز پر رنگ:* بدین معناست که پارامتر استفاده شده بصورت درست و بهینه پیاده سازی شده است:
		1. ![Pasted image 20260121215956.png](/images/seo/Pasted image 20260121215956.png)
2. **Priority Description:**
	1. پارامتر های استفاده شده در سه اولویت متفاوت دسته بندی میشوند: High, Medium, Low
		1. ![Pasted image 20260121220614.png](/images/seo/Pasted image 20260121220614.png)
	2. پارامتر هایی که اولویت High دارند حتما باید بهینه شوند.
3. **Type Description:**
	1. پارامتر ها نیز به نوع های مختلفی تقسیم میشوند که عبارتند از:
	2. Images
	3. Content
	4. Server
	5. CSS
	6. JS
	7. تصویر:
		1. ![Pasted image 20260121220708.png](/images/seo/Pasted image 20260121220708.png)
#### GT-Metrix Parameters Description - Page Speed(Google)
##### 1. Server Scaled Images
پارامتر تصاویری که باید Resize شوند را نشان میدهد.
1. **Parameter Description and Duty:**
	1. این پارامتر بهینه سازی تصاویر در سرور وبسایت را بررسی میکند. یکی از پارامتر های مهم برای افزایش سرعت لود وبسایت بهینه سازی تصاویر وبسایت است که باید بدرستی رعایت شود.
	2. پارامتر تصاویری که مناسب نیستند(یا سایز بالاتر از نیاز دارند یا حجم بیشتر) را تک به تک نشان میدهد تا بتوان مشکل آنها را رفع کرد:
		1. ![Pasted image 20260121221423.png](/images/seo/Pasted image 20260121221423.png)
	3. *نکته:* رفع کردن این مشکل تاثیر زیادی در افزایش سرعت لود وبسایت دارد.
2. **Optimizing Pictures Steps:**
	1. تصویری که مشکل دارد بود را از طریق لینکی که GT-Metrix در این پارامتر به ما داده باز و دانلود میکنیم:
		1. ![Pasted image 20260121221820.png](/images/seo/Pasted image 20260121221820.png)
	2. تصویر را به سایز مورد نیاز که GT-Metrix پیشنهاد داده Resize میکنیم:
		1. ![Pasted image 20260121221838.png](/images/seo/Pasted image 20260121221838.png)
	3. سپس تصویر را با ابزار آنلاین یا اسکریپت پایتون بصورت فشرده در می آوریم.
	4. در آخر تصویر Resized & Compressed شده را با تصویر فعلی جایگزین میکنیم.
3. **Features of Optimized Pictures for Web:**
	1. تصاویر باید در سایز مناسب باشند. یعنی تصویری که در تامبنیل استفاده شده است باید `150*150` باشد بنابراین تصویر `800*600` نیازی نیست. 
	2. تصاویر باید در دو یا چند سایز ذخیره شوند(یک سایز مناسب تامبنیل، یک سایز مناسب مقالات و یک سایز اصلی)
	3. *نکته:* تصاویری که سایز بزرگ و اشتباه باعث افزایش حجم صفحه و در نتیجه سرعت لود بیشتر میشوند.
##### 2. Enable gzip Compression
1. **What is gzip Compression and How Use This?**
	1. ابزاری است که بر روی سرور نصب میشود و در واقع میتوانیم به ارائه دهنده هاست درخواست دهیم تا Gzip Compression را برای ما نصب کند.
	2. ابزار Gzip Compression تمام کدهای HTML, CSS, JS را بصورت فشرده در می آورد.(کامنت ها و فضاهای خالی شامل Empty Line, Tab, Space, ... را حذف میکند)
		1. ![Pasted image 20260121222922.png](/images/seo/Pasted image 20260121222922.png)
	3. استفاده از Gzip Compression حجم خروجی را به شدت کاهش میدهد و استفاده از آن حتما پیشنهاد میشود.
	4. برای فعال کردن Gzip Compression باید بر اساس CMS , Webserver خودمان عمل کنیم. مثلا فعالسازی Gzip Compression در IIS Webserver متفاوت از Wordpress است.
##### 3. Optimize Images
این پارامتر تصاویری که نیاز به فشرده سازی دارند را نشان میدهد:
	![Pasted image 20260121223507.png](/images/seo/Pasted image 20260121223507.png)
- در واقع این تصاویر فقط نیاز به فشرده سازی دارند و نه Resize کردن 
- **How Compress Image?**
	- برای فشرده سازی تصاویر میتوانیم از اسکریپت و کد نویسی استفاده کنیم اما استفاده از ابزار های آنلاین مانند https://compressor.io/compress تاثیر بیشتری بر روی تصویر دارند و حجم بیشتری را در فشرده سازی کم میکنند:
		- ![Pasted image 20260121223719.png](/images/seo/Pasted image 20260121223719.png)
##### 4. Avoid Bad Requests
این گزینه Assets هایی که استفاده کردیم اما دیگر وجود ندارند یعنی `Status Code 404, 410` بر میگرداند را لیست میکند:
	![Pasted image 20260121223934.png](/images/seo/Pasted image 20260121223934.png)
وجود این نوع از فایل ها باعث کاهش سرعت لود وبسایت میشود زیرا منابع زیادی صرف لود فایلی که وجود ندارد میشود. 
در واقع چندین درخواست اضافه برای باز شدن فایلی که نیست به سرور زده میشود و موتور جستجو نیز فرض میگیرد که سرور پاسخی نداده است و نه اینکه فایل نبوده است.
- *نتیجه:* بنابراین حتما باید فایل هایی که در این قسمت نشان داده میشوند را باید درست کنیم تا تعداد این فایل ها به *صفر* برسد.
##### 5. Leverage Browser Caching 
برای افزایش سرعت لود وبسایت پیشنهاد میشود فایل هایی در وبسایت که به ندرت بروز میشوند را در سمت مرورگر کاربر به اصطلاح Cache کنیم. برای پیاده سازی اینکار روش های متفاوتی وجود دارد.
1. **Implement Leverage Browser Caching:**
	1. Wordpress, Joomla, HTML|CSS|JS Website: Cache using `.htaccess`
	2. .Net Website: Cache using `webconfig` File
2. **What files to be Cache?**
	1. در واقع تمام انواع فایل از قبیل تصاویر، اسکریپت های JS, استایل های CSS و یا کدهای HTML که بصورت ثابت هستند و نیاز به تغییر سریع ندارند را باید Cache کنیم.
	2. مثلا فایل هایی از قبیل `Fav Icon, Google Analytics JS, ...` را حتما باید Cache کنیم.
3. **Leverage Browser Caching in GT-Metrix:**
	1. در این گزینه نیز تمام فایل هایی که قابلیت Cache شدن را دارند اما در وبسایت هنوز کش نشدند را میتوانیم مشاهده کنیم:
		1. ![Pasted image 20260122144812.png](/images/seo/Pasted image 20260122144812.png)
4. *نکته:* برای دانستن روش Leverage Browser Caching در هر پلتفرم کافیست که Leverage Browser Caching را با نام پلتفرم جستجو کنید تا به روش آن برسید.
##### 6. Specify Image Dimensions
تصاویر برای اینکه برای سئو مناسب باشند باید دو ویژگی Width, Height را داشته باشند. حال در این پارامتر نیز تصاویری که عرض و ارتفاع ثابت را ندارند لیست میکند تا Width, Height را به این تصاویر اضافه کنیم:
	![Pasted image 20260122151101.png](/images/seo/Pasted image 20260122151101.png)
##### 7. Minify CSS
- **What is Minify?**
	- به حذف فضاهای حالی از قبیل New Line, Space, Tabs, ... و همچنین حذف کامنت های فایل به اصطلاح Minify گفته میشود.
	- در کل هنگامیکه عملیات Minify بر روی یک فایل انجام میشود، تمام خطوط و کد های درون فایل به یک خط پشت سرهم تبدیل میشوند.
- **Minify CSS:**
	- در این گزینه هم فایل های CSS که فشرده(gzip compression) نشده اند را مشاهده میکنیم. حال برای افزایش سرعت لود صفحه حتما و حتما باید این فایل ها نیز فشرده یا به اصطلاح Minify بشوند:
			![Pasted image 20260122151246.png](/images/seo/Pasted image 20260122151246.png)
	- علاوه بر این در این گزینه نسخه Optimized شده فایل CSS را نیز میتوانیم مشاهده کنیم:
		- ![Pasted image 20260122151636.png](/images/seo/Pasted image 20260122151636.png)
- **Minify Tools:**
	- برای پیاده سازی Minify ابزار های زیادی وجود دارد. ابزار هایی که میتوان آنها را در پروژه بصورت Bundle استفاده کرد و یا ابزار های آنلاین که میتوانیم فایل ها را بصورت جداگانه Minify کنیم.
##### 8. Minify HTML 
در این گزینه ها فایل های HTML که Minify نشده اند را لیست میکند تا آنها را بصورت Minify شده در بیاوریم و سرعت لود صفحه را افزایش دهیم.
##### 9. Minify JS
در این گزینه ها فایل های JS که Minify نشده اند را لیست میکند تا آنها را بصورت Minify شده در بیاوریم و سرعت لود صفحه را افزایش دهیم.
##### 10. Defer Parsing Java Script
1. **Importing Java Script Logic:**
	1. در کل صفحات HTML همگی از بالا به پایین لود میشوند یعنی از خط اول تا خط آخر.
	2. همچنین برای استفاده از Java Script ها درون صفحات HTML میتوانیم آنها را درون تگهای Header, Footer وارد کنیم. 
	3. نکته اینجاست که اگر آنها را در Header وارد کنیم بارگذاری کل صفحه منوط به بارگذاری Java Script ها میشود و در نتیجه تا Java Script ها لود نشود صفحه نیز لود نمیشود که باعث تاخیر در لود صفحه میشود.
	4. اما اگر Java Script درون تگ Footer لود شوند این امر باعث میشود که صفحه بدرستی لود شود و در آخر نیز Java Script ها لود شوند.
2. **What is Defer Parsing Java Script?**
	1. این گزینه نیز به الزام لود Java Script ها درون Footer اشاره میکند تا زمان زیادی که صرف لود Java Script ها میشود در لود کل صفحه تاثیر نگذارد:
		1. ![Pasted image 20260122152501.png](/images/seo/Pasted image 20260122152501.png)
	2. بنابراین این گزینه فایل هایی که Java Script ها را درون Header لود کرده اند نمایش میدهد تا بتوانیم لود Java Script ها را به تگ Footer انتقال دهیم.
- *نکته:* انتقال Import کردن فایل های Java Script به تگ Footer تاثیر زیادی در افزایش سرعت لود صفحه دار.
##### 11. Enable Keep-Alive
1. این گزینه به تعداد درخواست هایی که برای لود یک صفحه ارسال میشود اشاره میکند. 
2. در واقع یکسری از وبسایت ها کل مطلب را با یک درخواست(شامل چند ریز درخواست) لود میکنند.
3. اما یکسری از وبسایت ها که قابلیت Lazy Loading را دارند، یک صفحه را در چند قسمت و با درخواست های مختلف لود میکنند که این امر میتواند امتیاز منفی داشته باشد.
4. البته قابلیت Lazy Load نیز خود در بعضی مواقع مخصوصا برای لود مدیا های با حجم بالا مانند ویدئو، یا تصاویر با کیفیت بزرگ کاربردی است.
##### 12. Avoid Inline Small CSS & JS
1. **What is Inline CSS, JS?**
	1. در کد های HTML میتوانیم استایل ها و اسکریپت های JS را درون خود تگ HTML با پارامتر های `style, on-click, onblur, ...` بنویسیم.
	2. به اینکار به اصطلاح Inline CSS, Inline JS گفته میشود.
2. **Don't Use Inline Small CSS & JS:**
	1. حال در این گزینه اشاره میکند که برای افزایش سرعت لود صفحه به هیچ وجه از Inline Small CSS & JS استفاده نکنیم و بجای آنها از `Class, ID` و تگ `<script>` استفاده کنیم.
	2. اینکار باعث افزایش سرعت لود صفحه میشود.
	3. در این دو گزینه نیز فایل هایی که Inline Small CSS & JS دارند را مشاهده میکنیم تا بتوانیم استایل ها و اسکریپت های Inline استفاده شده را بصورت External دربیاوریم.
3. **What is External CSS, JS?**
	1. هنگامیکه از `Class, ID` و تگ `<script>` استفاده کنیم به اینکار External CSS, JS گفته میشود.
	2. استفاده از External CSS, JS باعث میشود که پس از لود یک بار استایل و اسکریپت، آنها در سمت کاربر یا CDN کش شوند و در نتیجه در دفعات بعدی سرعت لود وبسایت را به شدت کاهش میدهد.
##### 13. Avoid Landing Page Redirects
این گزینه به Redirect های کلی که در وبسایت پیاده سازی میشوند اشاره دارد که در واقع باید از آنها جلوگیری کنیم.
- مثلا کاری که در podisfahan.ir انجام دادیم و آنرا مستقیما به vapeclub3.com ریدایرکت کردیم، از نظر موتور جستجو گوگل اشتباه است و امتیاز منفی زیادی برای podisfahan.ir دارد:
	![Pasted image 20260122153117.png](/images/seo/Pasted image 20260122153117.png)
- **How Implement Redirects?**
	1. استفاده از JQuery
	2. استفاده از `htaccess.`
##### 14. Minimize Redirects
این گزینه به محدود کردن و کاستن تعداد Redirect هایی که درون وبسایت خودمان انجام دادیم اشاره میکند. 
- در واقع گاهی نیاز است که مثلا `dsecurity.com/news` را به `dsecurity.com/blog` ریدایرکت کنیم، این گزینه میگوید تعداد این Redirect ها نباید بیش از حد شود و باید در واقع Minimal باشد.
- برای پیاده سازی این Redirect ها نیز از کدهای درون صفحه و یا `htaccess` میتوان استفاده کرد که هر دو را باید Minimize کنیم.
##### 15. Minimize Request Size
1. **What is Requests?**
	- برای لود یک صفحه از وبسایت چندین درخواست یا Request به سرور ارسال میشود. هر Request نیز حجم مشخصی دارد.
	- برای افزایش سرعت لود صفحه باید از تعداد این Request ها و حجم نهایی آنها بکاهیم تا صفحه سریعتر لود شود.
2. **Which Page Using More Requests?**
	1. صفحاتی مانند صفحه فروشگاه و یا صفحاتی که دارای فیلتر هایی هستند با اعمال هر فیلتر در واقع درخواستی به سمت سرور میفرستند و طول URL را نیز طولانی تر میکنند:
		1. ![Pasted image 20260122155153.png](/images/seo/Pasted image 20260122155153.png)
		2. ![Pasted image 20260122155348.png](/images/seo/Pasted image 20260122155348.png)
	2. این فیلتر ها بصورت معمول اگر با SQL Query های ساده نوشته شده باشند مشکلی ندارند و باعث افزایش Request Size نمیشوند.
	3. اما اگر از SQL Query های پیچیده استفاده کنیم این گزینه باعث افزایش حجم Request Size و در نتیجه کاهش سرعت لود صفحه میشود.
	4. همچنین گاهی اوقات در مطلب نیز از کوئری هایی استفاده میشود مثلا برای لود محصولات با دسته بندی دوره که قیمت زیر 1000000 دارند و استاد آنها داوود یاحی است.
	5. خوب این کوئری کمی پیچیده است و باعث افزایش Request Size و همچنین کاهش سرعت لود صفحه میشود.
##### 16. Optimize the order of Styles and Scripts
این گزینه نیز به بهینه سازی استفاده از CSS, JS اشاره دارد. در واقع هم به فشرده سازی و هم به اولویت و ترتیب وارد کردن آنها اشاره میکند.
- در واقع مهمترین و اصلی ترین CSS, JS ها در ابتدا باید وارد شوند و سپس نیز سایر CSS, JS ها باید در صفحات وارد شوند.
- در واقع وقتیکه Gzip Compression, Minify را بر روی CSS, JS ها پیاده سازی کنیم این گزینه نیز 100 درصد را از GT-Metrix دریافت میکند.
##### 17. Put CSS in the Document Head
این گزینه نیز میگوید برای افزایش سرعت لود صفحه بهتر است که استایل های CSS را درون تگ Head صفحه لود کنیم. اینکار باعث افزایش سرعت بارگذاری صفحه میشود.
- در واقع اگر استایل ها در آخر صفحه باشد، ابتدا وبسایت با ظاهری بهم ریخته لود میشود تا سپس استایل ها لود شود و در واقع باعث آزار کاربران میشود.
##### 18. Server Resource from a Consistent URL
بطور کلی برای وبسایت ها میتوانیم از قابلیتی بنام CDN استفاده کنیم. حال این گزینه میگوید که برای افزایش سرعت لود صفحه بهتر است که از CDN های معتبر استفاده کنیم:
	![Pasted image 20260122162401.png](/images/seo/Pasted image 20260122162401.png)
- در واقع اگر که از CDN استفاده کنیم که معتبر باشد ممکن است که کاربر وبسایت دیگری را باز کرده باشد که از این CDN استفاده میکرده و در نتیجه فایل های وبسایت ما نیز Cache شده اند.
- بنابراین وقتی که کاربر وبسایت ما را باز میکند بسیار سریعتر صفحه برای او لود میشود.
- **Note: Manual CDN**
	- گاهی اوقات توسعه دهنده ها، Resource های وبسایت خود را در Sub Domain های خود قرار میدهند و سپس از لینک آنها درون صفحات اصلی خود استفاده میکنند.
	- حال اگر که این Sub Domain معتبر نباشد و منابع وبسایت لود نشود این گزینه به ما این خطا را نشان میدهد.
##### 19. Specify a Cache Validator
اگر فایل های استفاده شده در وبسایت بدرستی Cache نشده باشند در این گزینه فایل ها و ایراد هایی که وجود دارند را نشان میدهد.
##### 20. Combine Image Using CSS Sprites
در بسیاری از موارد از تصاویر درون استایل های CSS استفاده میکنیم. حال اگر تصاویر استفاده شده درون استایل های CSS مشکل داشته باشد(از قبلی تنظیم نبودن اندازه، وجود نداشتن تصاویر، ...) در این گزینه تصاویر ایراد دار را مشاهده میکنیم:
	![Pasted image 20260122170250.png](/images/seo/Pasted image 20260122170250.png)
##### 21. Avoid CSS @import
فایل های CSS را میتوان با استفاده از `import@` وارد صفحه HTML کنیم. در واقع در قدیم هم با استفاده از `import@` استایل ها را درون صفحه HTML وارد میکردیم:
	![Pasted image 20260122170548.png](/images/seo/Pasted image 20260122170548.png)
- اما امروزه این روش باعث کند شدن سرعت لود صفحه میشود و در نتیجه استفاده از این روش پیشنهاد نمیشود و برای افزایش سرعت لود صفحه باید از آن جلوگیری کنیم.
##### 22. Prefer Asynchronous Resource
همانطور که گفتیم کدهای HTML از بالا به پایین یعنی از خط اول به انتها اجرا میشوند. 
- این گزینه میگوید که در وسط کدهای HTML یعنی داخل سایر تگ های HTML به هیچ وجه از `<script>` استفاده نشود زیرا که باعث کاهش سرعت لود صفحه میشود:
	![Pasted image 20260122170846.png](/images/seo/Pasted image 20260122170846.png)
- در واقع بهترین جا برای لود اسکریپت ها در آخر کدهای HTML و درون تگ `<Footer>` میباشد.
##### 23. Specific a Character Set Early *Check Needed*
این گزینه میگوید که حتما `charset="utf-8"` را در تگ `meta Content Type` باید مشخص کرده باشیم که باعث افزایش سرعت لود صفحه میشود:
	![Pasted image 20260122171513.png](/images/seo/Pasted image 20260122171513.png)
- در واقع برای رعایت این موضوع کافیست تگ متا زیر را حتما در `<Head>` کدهای HTML مان بنویسیم:
```html
<meta http-equiv="Content-Type" content="text/html" charset="utf-8"/>
```
- *نکته:* برای وبسایت با زبان فارسی `charset="utf-8"` میباشد اما برای سایر زبان ها مثلا زبان ژاپنی چینی `charset="utf-16"` است.
- **Avoid a Character set in the meta tag:**
	- این گزینه نیز در زیر گزینه Specific a Character Set Early وجود دارد. 
	- به همین دلیل بهتر است بار دیگر خودمان این دو گزینه و کارکرد آنها را بصورت دقیق تر بررسی کنیم.
##### 24. Remove Query String from Static Resources
1. **What is Query String?**
	1. گاهی اوقات برای واکشی مقادیر مشخص شده ای، مانند فیلتر های فروشگاه و واکشی یک دسته خاص از کالا ها نیاز به اجرای کوئری داریم. 
	2. این متن های کوئری اصولا در URL صفحه و پس از `?` اضافه میشوند:
		1. ![Pasted image 20260122172108.png](/images/seo/Pasted image 20260122172108.png)
	3. به این متن ها به اصطلاح Query Strings گفته میشود.
2. **Remove Query String from Static Resources:**
	1. حال این گزینه به ما میگوید بهتر است بجای استفاده از Query String ها، از URL های مشخص استفاده شود. مثلا:
	2. بجای URL زیر:
		1. https://toplearn.com/courses?categories=webdesign
	3. از URL زیر استفاده شود:
		1. https://toplearn.com/courses/categories/webdesing
	4. این امر باعث افزایش سرعت لود صفحه میشود زیرا که برای لود از تعداد و حجم درخواست ها به سمت دیتابیس میکاهد.
##### 25. Specific a Vary: Accept-Encoding Header
این گزینه باید در سمت سرور وبسایت فعال باشد که باعث افزایش سرعت لود صفحه میشود.
- **Whats Accept-Encoding Header?**
	- در CDN ها برای افزایش سرعت لود صفحه، پس از کش شدن فایل ها دیگر فایل اصلی درون هاست وبسایت ما لود نمیشود. 
	- بلکه فایل کش شده با پسوند `me.` لود میشود که سرعت لود صفحه را افزایش میدهد.
	- حال اگر که این گزینه در سمت سرور فعال نباشد، در CDN بجای درخواست فایل ها با پسوند `me.` فایل اصلی لود میشود که میتواند سرعت لود صفحه را کاهش دهد.
#### GT-Metrix Parameters Description - YSlow(Yahoo)
##### 0. YSlow(Yahoo) Description
برای موتور جستجو Yahoo نیز پارامتر هایی وجود دارد که یکسری از آنها با Page Speed(Google) هم وجود دارد ولی یکسری هم مخصوص YSlow(Yahoo) است. 
همچنین یک وبسایت عالی باید برای هر دو الگوریتم جستجو یعنی Page Speed(Google) و YSlow(Yahoo) بهینه و مناسب باشد و امتیاز سبز را از هر دو اینها دریافت کند.
##### Similar to Page Speed(Google)
1. Compress Components with gzip
2. Minify Java Scripts and CSS
3. Make Java Script and CSS External
##### 1. Add Expires Headers
در این گزینه فایل هایی که قابلیت Cache شدن در سمت مرورگر کاربر را دارند اما کش نشده اند را مشاهده میکنیم:
	![Pasted image 20260122173410.png](/images/seo/Pasted image 20260122173410.png)
برای کش این فایل ها میتوانیم از `htaccess` یا `webconfig` استفاده کنیم.
##### 2. Use a Content Delivery Network(CDN)
این گزینه میگوید که شما از CDN استفاده کرده اید یا خیر
- در واقع لیست فایل هایی از وبسایت که بهتر است در CDN باشند را به ما نشان میدهد:
	- ![Pasted image 20260122173609.png](/images/seo/Pasted image 20260122173609.png)
##### 3. Use Cookie-free Domain
وقتیکه از CDN برای وبسایت استفاده کنیم مشکلات درون این گزینه نیز برطرف میشود. در واقع اگر از CDN استفاده نشود هم در این گزینه امتیاز منفی میگیریم و هم در گزینه Use a Content Delivery Network(CDN) نیز امتیاز منفی دریافت میکنیم.
##### 4. Make Fewer HTTP Requests
در این گزینه تعداد درخواست هایی که برای واکشی CSS, JS ها زده ایم را مشاهده میکنیم:
	![Pasted image 20260122173907.png](/images/seo/Pasted image 20260122173907.png)
- حال این گزینه میگوید که بهتر است تمامی این درخواست ها را به یک عدد برای JS و یک عدد برای CSS کاهش دهیم.
- **How Improve?**
	- برای پیاده سازی اینکار هم کافیست بجای استفاده از چندین فایل JS, CSS و وارد کردن آنها در کد HTML تمام CSS ها را درون یک فایل، همچنین تمام JS ها را نیز درون یک اسکریپت قرار دهیم و سپس CSS را در بالا و JS را در آخر فایل HTML وارد کنیم.
##### 5. Avoid HTTP 404(Not Found) Error
لیست فایل هایی که در سرور ما پیدا نمیشوند را نشان میدهد تا آنها را حذف یا اصلاح کنیم.
##### 6. Make AJAX Cacheable 
مشکلات یافت شده از کوئری های AJAX درون این پارامتر قابل مشاهده هستند.
##### 7. Remove Duplicate Java Scripts and CSS
اگر از فایل های CSS, JS بصورت Duplicate استفاده کرده باشیم در این گزینه مکان های استفاده شده را نشان میدهد تا مشکلات آنرا برطرف کنیم و استفاده های Duplicate را حذف کنیم.
##### 8. Avoid Alpha Image Loader Filter
1. **What is Alpha Image Loader?**
	1. وقتیکه مرورگر به فایل های PNG میرسد، تا زمانیکه PNG بصورت کامل لود نشود صفحه نیز لود نمیشود. در نتیجه از سرعت لود وبسایت میکاهد.
	2. به این نوع تصاویر Alpha Image Loader گفته میشود.
	3. البته مرورگر ها امروزه این مشکل را برطرف کرده اند و دیگر این مشکل را ندارند.
2. **What is Alpha Image Loader Filter?**
	1. حال این گزینه میگوید اگر تصاویر PNG در صفحه دارید بهتر است که آنها را در CSS با فیلتر `Loader` بارگذاری کنیم تا به این مشکل برنخوریم.
3. *نکته:* مرورگر ها امروزه این مشکل را برطرف کرده اند و دیگر این مشکل را ندارند.
##### 9. Reduce the Number of DOM Elements
- **What is DOM Elements?**
	- اگر یک صفحه HTML یا ویدئو یا تصویری را درون یک صفحه دیگر HTML با استفاده از `iframe` ها لود کنیم به این شی ها DOM Elements گفته میشود.
	- شی های DOM Elements دشمن سئو هستند و سرعت لود صفحه را به شدت کاهش میدهند.
- این گزینه به ما میگوید که استفاده از DOM Elements را به شدت کاهش دهید و حتی به صفر برسانید تا صفحه با سرعت بیشتری لود شود.
##### 10. Use GET for AJAX Requests
برخی برای ارسال درخواست های AJAX از پارامتر POST HTTP استفاده میکنند که میتواند باعث کاهش سرعت لود صفحه شود.
- این گزینه میگوید برای ارسال درخواست های AJAX از پارامتر GET HTTP استفاده کنید که باعث افزایش سرعت لود صفحه شود.
##### 11. Reduce DNS Lookup
این گزینه به کاهش درخواست های DNS اشاره دارد که باعث افزایش سرعت لود صفحه شود.
در واقع این گزینه به دامنه ما مربوط میشود.
##### 12. Reduce Cookie Size
این گزینه هم به کاهش حجم Cookie ها اشاره دارد که باعث افزایش سرعت لود صفحه شود.
##### 13. Make Favicon Small and Cacheable
این گزینه میگوید که Favicon استفاده شده در وبسایت باید سایز کوچک داشته باشد و همچنین Cache شود.
##### 14. Configure Entity Tags(ETags)
- **Whats Entity Tags(ETags)?**
	- نوعی تگ هویتی هستند که ویژگی های صفحه را از قبیل تاریخ آخرین تغییر، تاریخ انتشار، نویسنده و ... را مشخص میکند.
	- در واقع از Entity Tags(ETags) برای تغییر Cache ها استفاده میشود و بسیار برای موتور جستجو مهم است.
- حال این گزینه نیز میگوید که در صفحه حتما از Entity Tags(ETags) ها استفاده کنیم.
##### 15. Avoid CSS Expression
این گزینه هم به Minify و فشرده سازی فایل های CSS اشاره دارد.
#### GT-Metrix Other Tabs
##### Waterfall
در این گزینه یک چارت به ما نشان میدهد که موارد زیر در آن قابل مشاهده هست:
1. میزان منابع مصرف شده برای لود صفحه:
	1. ![Pasted image 20260122180033.png](/images/seo/Pasted image 20260122180033.png)
2. حجم و زمانی که برای لود Assets های صفحه استفاده شده:
	1. ![Pasted image 20260122180141.png](/images/seo/Pasted image 20260122180141.png)
- در واقع در این گزینه میتوان فهمید که کدام Asset زمان زیادی را برای لود صفحه اشغال کرده است و یا اینکه چقدر از منابع سرور برای لود صفحه مصرف شده است.
##### Timing 
در این گزینه زمان بندی دقیق اجزای لود صفحه از قبلی `TTFB, DOM int, DOM Loaded, ...` قابل مشاهده است:
	![Pasted image 20260122180336.png](/images/seo/Pasted image 20260122180336.png)
##### Video
اگر در وبسایت خود از ویدئو استفاده کرده باشیم در اینجا بهینه بودن یا نبودن آنها را میتوانیم مشاهده کنیم.
##### History
در این گزینه هم تاریخچه ای از تغییراتی که در وبسایت برای افزایش سرعت اعمال کرده ایم قابل مشاهده است:
	![Pasted image 20260122180519.png](/images/seo/Pasted image 20260122180519.png)
	![Pasted image 20260122180535.png](/images/seo/Pasted image 20260122180535.png)
### Note, Perform Speed Analysis for Each Page
یکی از نکات مهمی که در بهینه سازی سرعت لود صفحه وجود دارد، انجام اسکن و بهینه سازی سرعت لود برای صفحات مهم وبسایت مان میباشد.
در واقع یک وبسایت عالی باید تمام صفحات آن با سرعت بسیار بالا(زیر 3 ثانیه) لود شوند و نه اینکه فقط صفحه اصلی اینگونه لود شود.
### !