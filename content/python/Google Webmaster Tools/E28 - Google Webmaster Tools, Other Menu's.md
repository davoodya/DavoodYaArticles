---
Episode: E28
Date: 2026-01-26
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 22:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E27 - Google Index & Search Appearances(Structure Data)]]"
Next Episode: "[[E29 - Google Analytics]]"
---
-------
## TOC
- [Search Appearances](#Search%20Appearances)
	- [1. Structured Data](#1.%20Structured%20Data)
	- [2. Rich Cards](#2.%20Rich%20Cards)
		- [What is Rich Cards?](#What%20is%20Rich%20Cards?)
		- [Google Structured Data Testing Tool](#Google%20Structured%20Data%20Testing%20Tool)
		- [Implement Search Box using Rich Cards](#Implement%20Search%20Box%20using%20Rich%20Cards)
		- [Other Data Structured(Rich Cards)](#Other%20Data%20Structured(Rich%20Cards))
	- [3. Data Highlighter](#3.%20Data%20Highlighter)
		- [What is Data Highlighter?](#What%20is%20Data%20Highlighter?)
		- [Start Working with Data Highlighter](#Start%20Working%20with%20Data%20Highlighter)
		- [Search Appearances => Data Highlighter](#Search%20Appearances%20=%3E%20Data%20Highlighter)
	- [4. HTML Improvements](#4.%20HTML%20Improvements)
		- [HTML Improvements Duties](#HTML%20Improvements%20Duties)
		- [Common Issues in HTML Improvements](#Common%20Issues%20in%20HTML%20Improvements)
		- [Read HTML Improvements Issue's](#Read%20HTML%20Improvements%20Issue's)
		- [False Positive Duplicate title tags issue(Not Used Canonical)](#False%20Positive%20Duplicate%20title%20tags%20issue(Not%20Used%20Canonical))
	- [5. AMP(Accelerate Mobile Pages)](#5.%20AMP(Accelerate%20Mobile%20Pages))
		- [What is AMP(Accelerate Mobile Pages)?](#What%20is%20AMP(Accelerate%20Mobile%20Pages)?)
		- [Implement AMP Using `amp-custom`](#Implement%20AMP%20Using%20%60amp-custom%60)
		- [Convert HTML to AMP *Research Topic*](#Convert%20HTML%20to%20AMP%20*Research%20Topic*)
- [Crawl](#Crawl)
	- [1. Crawl Errors](#1.%20Crawl%20Errors)
		- [Description](#Description)
		- [Not Found URL](#Not%20Found%20URL)
		- [Fix Crawler Errors](#Fix%20Crawler%20Errors)
	- [2. Fetch as Google](#2.%20Fetch%20as%20Google)
	- [3. robots.txt](#3.%20robots.txt)
	- [4. Sitemaps](#4.%20Sitemaps)
	- [5. URL Parameters](#5.%20URL%20Parameters)
- [Security Issue](#Security%20Issue)
- [Web Tools](#Web%20Tools)
	- [Description](#Description)
	- [Introduction to Web Tools](#Introduction%20to%20Web%20Tools)
------------------------------
### Search Appearances
#### 1. Structured Data
داده های ساختار یافته که برای نمایش المان هایی در کنار نتیجه جستجو وبسایت ماست را در جلسه قبلی توضیح دادیم. 
در این منو میتوانیم Structured Data هایی که در وبسایت خودمان استفاده کرده ایم را مشاهده کنیم.
#### 2. Rich Cards
##### What is Rich Cards?
قابلیت Rich Card در واقع قابلیتی مانند Data Structured ها هستند با این تفاوت که پیاده سازی آنها راحت تر است و دیگر نیازی به رجوع به Schema.org و نوشتن اسکریپت های پیچیده مانند Data Structured ها ندارند. 
- برای مشاهده راهنمای پیاده سازی Rich Card ها کافیست که به آدرس زیر برویم و تمام نمونه های Rich Card که در واقع مانند Data Structured Elements ها هستند را به همراه روش پیاده سازی آنها مشاهده کنیم:
	- https://developers.google.com/search/docs/guides/search-gallery
- **نکته:** گوگل به وبسایتی هایی که Structured Data را در وبسایت خود پیاده سازی کرده اند، Rich Search میگوید.
- `Search Appearance => Rich Cards`
	- منو Rich Cards ها در کنسول قدیمی گوگل میباشد.
##### Google Structured Data Testing Tool
- ابزار گوگل Google Structured Data Testing Tool برای تست Structured Data هاست که لینک آن نیز به شرح زیر است:
	- https://search.google.com/structured-data/testing-tool
- کافیست در این ابزار اسکریپت Structured Data خود را بنویسیم و سپس بر روی Run کلیک کنیم تا نتیجه نهایی Structured Data را مشاهده کنیم:
	- ![[Pasted image 20260126190618.png]]

##### Implement Search Box using Rich Cards
1. برای پیاده سازی فرم جستجو در وبسایتمان، در لینک زیر قسمت `Sitelinks Searchbox` بر روی `Read the Guide` کلیک میکنیم.
	- https://developers.google.com/search/docs/guides/search-gallery
		- ![[Pasted image 20260126185811.png]]
2. سپس در صفحه باز شدن بر روی `SEE MARKUP` کلیک میکنیم تا کدی که برای پیاده سازی فرم جستجو نیاز است را مشاهده کنیم:
	1. ![[Pasted image 20260126185940.png]]
3. اسکریپت مورد نیاز مانند تصویر زیر است:
	1. ![[Pasted image 20260126190056.png]]
##### Other Data Structured(Rich Cards)
1. **Article Structured Data:**
	1. ![[Pasted image 20260126190436.png]]
2. **Social Networks:**
	1. ![[Pasted image 20260126190740.png]]
3. **Local Business:** 
	1. ![[Pasted image 20260126190700.png]]
4. **Course:**
	1. ![[Pasted image 20260126190838.png]]
5. **Job Posting:**
	1. ![[Pasted image 20260126190939.png]]
#### 3. Data Highlighter
##### What is Data Highlighter?
- ابزار Data Highlighter به ما در ساخت Rich Cards ها و در واقع نوشتن Structured Data ها کمک میکند. این ابزار در کنسول قدیمی Webmaster Toolkits قرار داشت اما در نسخه جدید آن وجود ندارد اما با لینک زیر میتوانیم به ابزار دسترسی داشته باشیم:
	- https://www.google.com/webmasters/data-highlighter/
##### Start Working with Data Highlighter
1. Open Data Highlighter and Click on `Start Highlighting`
	1. ![[Pasted image 20260126191947.png]]
2. Enter URL of Your Page and Select Structured Data Type then `OK`:
	1. ![[Pasted image 20260126192041.png]]
3. *After that, Data Highlighter Open a URL:*
	1. ابزار URL مورد نظر را باز میکند تا بصورت Wizard پارامتر هایی را که میخواهد مقدار دهی کند.
	2. در صفحه باز شده ابزار با بسته به نوع Type که انتخاب کردیم موارد مورد نیاز خود را از ما میخواهد. در این مثال چون Article بود از ما موارد زیر را میخواهد:
		1. ![[Pasted image 20260126192713.png]]
4. *Now we should select texts on the page, then right click on texts and select property of selected text:*
	1. در واقع متنی که انتخاب میکنیم را با راست کلیک میتوانیم به پارامتر های لازم اختصاص دهیم:
		1. ![[Pasted image 20260126192951.png]]
	2. انتخاب المان را برای تصاویر نیز میتوانیم انجام دهیم:
		1. ![[Pasted image 20260126193101.png]]
5. **Note:** `tag this pages and others like it` & `tag just this page`
	1. در اول Data Highlighter دو گزینه `tag just this page` و `tag this pages and others like it` قابل انتخاب هستند:
		1. ![[Pasted image 20260126193539.png]]
	2. اگر در اول Data Highlighter گزینه `tag just this page` را انتخاب کرده باشیم این Structured Data را فقط برای صفحه باز شده میسازد.
	3. اما اگر `tag this pages and others like it` را انتخاب کرده باشیم بر طبق الگویی که معرفی کردیم برای تمام صفحات مشابه این Structured Data را میسازد.
	4. مثلا برای صفحه محصولات میتوانیم با یک محصول که مشخص میکنیم الگو را برای تمام محصولات بنویسیم:
		1. ![[Pasted image 20260126193404.png]]
	5. همچنین با انتخاب `Custom` میتوانیم برای صفحات مشخصی نیز این الگو را تعریف کنیم:
		1. ![[Pasted image 20260126193435.png]]
6. Then, Select name and Click on `Create Page Set` to Create for specific pages:
	1. ![[Pasted image 20260126193758.png]]
7. Then, we should check other examples and if Click on `Next` & `done`
	1. ![[Pasted image 20260126194114.png]]
	2. ![[Pasted image 20260126194112.png]]
8. Finally, in Review and Publish Step you can see Created Rich Cards and if OK Click on `PUBLISH`
	1. ![[Pasted image 20260126194243.png]]
##### Search Appearances => Data Highlighter
- پس از ساخت اولین Data Highlighter خود در این منو میتوانیم تمامی نمونه ها را مشاهده کنیم:
	- ![[Pasted image 20260126194421.png]]
- علاوه بر آن نیز میتوانیم Data Highlighter جدیدی را نیز از طریق این صفحه ایجاد کنیم.
- **نکته:** در کل ساخت Rich Cards ها را بهتر است با استفاده از اسکریپت های مربوط که داینامیک شده اند و با متغیر ها بر طبق صفحه مورد نظر ما ایجاد شده اند بنویسیم زیرا که در این روش امکانات و همچنین مدل های بسیار بیشتری را میتوانیم پیاده سازی کنیم.
#### 4. HTML Improvements
##### HTML Improvements Duties
در این منو میتوانیم ایرادات HTML که در وبسایت ما وجود دارد را مشاهده کنیم تا بتوانیم آنها را برطرف کنیم.
- مثلا در تصویر زیر مشاهده میکنیم در `Meta Description` و `Title Tag` وبسایت ما ایراداتی وجود دارد:
	- ![[Pasted image 20260126194828.png]]
##### Common Issues in HTML Improvements
1. **Meta Description Issues:**
	1. Duplicate Meta Description
	2. Long Meta Description
	3. Short Meta Description
2. **Title Tag Issues:**
	1. Missing title tags
	2. Duplicate title tags
	3. Long title tags
	4. Short title tags
	5. Non-Informative title tags(تگ تایتل بی ربط به صفحه)
3. **Non-Indexable Content:**
	1. مطالبی که قابلیت ایندکس شدن را ندارند.
##### Read HTML Improvements Issue's 
- حال در تصویر زیر مشاهده میکنیم که 8 صفحه دارای ایراد Duplicate Meta Description هستند و 145 دارای ایراد Duplicate title tags میباشند:
	- ![[Pasted image 20260126195349.png]]
- حال روی هر خطا نیز کلیک کنیم Meta Description تکراری و آدرس صفحاتی که مقدار تکراری را دارند میتوانیم مشاهده کنیم:
	- ![[Pasted image 20260126195455.png]]
	- ![[Pasted image 20260126195558.png]]
- **نکته:** بدلیل اینکه دو تگ Meta Description , Title برای سئو گوگل بسیار مهم هستند حتما باید این دو مورد را برطرف کنیم تا افزایش رتبه بندی سئو را داشته باشیم.
##### False Positive Duplicate title tags issue(Not Used Canonical)
- **مورد اول:** اگر که برای هر صفحه یک لینک فارسی انگلیسی و همچنین یک لینک کوتاه داشته باشیم و تگ `Canonical` را در یکی از آنها تعریف نکنیم(بهتر است در صفحه لینک کوتاه باشد) در اینجا آن صفحه خطای `Duplicate title tags` را میدهد:
	- ![[Pasted image 20260126201220.png]]
- **مورد دوم:** اگر یک صفحه دارای صفحه بندی های متفاوت باشد مثلا یک مطلب انجمن که در آن پرسش و پاسخ مطرح شده است و دارای چندین صفحه است، و در آن صفحات تگ `Canonical` را با لینک صفحه اول(اصلی) تعریف نکرده باشیم نیز در اینجا به خطای `Duplicate title tags` برمیخوریم:
	- ![[Pasted image 20260126201206.png]]
#### 5. AMP(Accelerate Mobile Pages)
##### What is AMP(Accelerate Mobile Pages)?
ویژگی AMP یا Accelerate Mobile Pages قابلیتی است که به امکان میدهد یکسری تگ ها و المان های صفحه HTML, CSS خود را فقط در دیوایس های موبایل لود نکنیم. 
- دقت کنید AMP المان را در دیوایس های موبایل مخفی نمیکند(مانند استایل نویسی یا Bootstrap) بلکه کلا جلو لود المان در دیوایس های موبایل میگیرد.
- برای خواندن مطالب بیشتر در این مورد به [لینک](https://www.ampproject.org/docs/fundamentals/) زیر بروید:
	- https://www.ampproject.org/docs/fundamentals/
		- ![[Pasted image 20260126201831.png]]
		- ![[Pasted image 20260126201752.png]]
- **نکته:** البته برای پیاده سازی نسخه وبسایت مناسب دیوایس های موبایل میتوانیم از Responsive CSS Styles و یا فریم ورک هایی مانند Bootstrap نیز استفاده کنیم.
##### Implement AMP Using `amp-custom`
برای پیاده سازی AMP و جلوگیری از لود المانی در دیوایس موبایل از ویژگی بنام `amp-custom` در CSS, HTML استفاده میکنیم:
```html
<html>
	<head>
	
	<style amp-custom>
		h1 {color: red; font-weight: bold}
	</style>
	
	<style>
		h2 {color: red; font-weight: bold}
	</style>
	
	</head>
</html>
```
- *Picture:*
	- ![[Pasted image 20260126202318.png]]
##### Convert HTML to AMP *Research Topic*
### Crawl
#### 1. Crawl Errors
##### Description
در این منو خطاهایی که خزنده گوگل در خزش وبسایت ما به آنها برخورده است را مشاهده میکنیم:
	![[Pasted image 20260126202833.png]]
- **Crawl Error Types:**
	1. Server Errors:
		1. خطاهای سروری در این قسمت مشاهده میشوند:
			1. ![[Pasted image 20260126203036.png]]
	2. Access Denied:
		1. صفحاتی که گوگل نتوانسته به آنها دسترسی داشته باشد:
			1. ![[Pasted image 20260126203102.png]]
	3. Not Found:
		1. صفحاتی که خزنده های گوگل آنها را نیافته است:
			1. ![[Pasted image 20260126203238.png]]
	4. Other
##### Not Found URL
صفحاتی که Not Found هستند یکی از بدترین خطاها هستند و امتیاز منفی زیادی دارند که باید حتما آنها را برطرف کنیم.
1. **Avoid from Not Found URL:**
	1. وقتیکه یک URL از وبسایتمان حذف شد، به قسمت `Google Index => Remove URLs` (کنسول قدیم) | `Indexing => Removals` (کنسول جدید) میرویم.
	2. سپس URL را به عنوان حذف شده معرفی میکنیم:
		1. ![[Pasted image 20260126203854.png]]
	3. سپس نوع حذف را مشخص میکنیم که پر استفاده ترین آن `Temporarily hide pag from search results and remove from cache` میباشد:
		1. ![[Pasted image 20260126204028.png]]
	4. در آخر `Submit Request` را میفشاریم.
2. **Fix Not Found Errors:**
	1. برای ارسال گزارش رفع خطا پس از اصلاح صفحه، روی صفحه یا خطایی که میخواهیم کلیک میکنیم و سپس `Mark as Fixed` کلیک میکنیم:
	- ![[Pasted image 20260126203408.png]]
##### Fix Crawler Errors
- برای ارسال گزارش رفع خطا پس از اصلاح صفحه، روی صفحه یا خطایی که میخواهیم کلیک میکنیم و سپس `Mark as Fixed` کلیک میکنیم:
	- ![[Pasted image 20260126203408.png]]
- **نکته:** این خطا ها را باید یکی یکی بررسی کنیم و تمام ایراداتی که برای خزنده های گوگل پیش آمده را حل کنیم تا وبسایت ما بدرستی و کامل برای گوگل ایندکس شود.
- بسیاری از Server Error ها در واقع همان Not Found هستند و بدلیل اینکه سرور جواب نداده است Server Error شده است.
- در Other Errors هم صفحاتی که Response Code 400 داشته اند و خزنده های گوگل در خزش آنها به مشکل برخورده مشاهده میشود.
#### 2. Fetch as Google
اگر لینکی توسط موتور جستجو ایندکس نشده بود برای معرفی دستی این لینک به موتور جستجو گوگل از این گزینه استفاده میکنیم:
	![[Pasted image 20260126211617.png]]
- این گزینه در کنسول جدید به Inspect URL تبدیل شده است.
- *نکته:* پیشنهاد میشود برای معرفی URL های که موتور جستجو آنها را ایندکس نکرده است استفاده کنیم. همچنین برای ایندکس کردن محتویات غیر از مطلب مانند تصویر یا صدا نیز میتوانیم از این گزینه استفاده کنیم.
#### 3. robots.txt
در این قسمت هم فایل robots.txt وبسایت قابل مشاهده و همچنین قابل ویرایش است:
	![[Pasted image 20260126210828.png]]
#### 4. Sitemaps
در این قسمت وضعیت لینک های نقشه سایت را مشاهده میکنیم. لینک های ایندکس شده آبی و لینک هایی که ایندکس نشده اند به رنگ قرمز نمایش داده میشوند:
	![[Pasted image 20260126211251.png]]
#### 5. URL Parameters
در این قسمت نیز پارامتر هایی که در تعریف URL ها بیشترین استفاده را داشته اند را مشاهده میکنیم:
	![[Pasted image 20260126211422.png]]
### Security Issue
اگر وبسایت ما نکات امنیتی را رعایت نکند و یا اینکه حریم خصوصی کاربر را نقش کند در این گزینه میتوانیم علت این خطا ها را مشاهده کنیم.
- این خطاها بیشتر در وبسایت هایی که با وردپرس، جوملا توسعه داده شده اند و پلاگین های اضافه بر روی آنها نصب میشود اتفاق می افتد.
### Web Tools
#### Description
در منو Web Tools هم ابزار های دیگر Google برای وبسایت ها را میتوان مشاهده کرد:
	![[Pasted image 20260126212540.png]]
#### Introduction to Web Tools
1. Ad Experience Report
	1. Desktop
	2. Mobile
2. **Testing Tools:**
	- Structured Data Testing Tool
	- Structured Data Markup Helper
	- Email Markup Tester
	- Image:
		- ![[Pasted image 20260126212716.png]]
3. Other Resources
### !