---
Episode: E24
Date: 2026-01-24
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
Pervious Episode: "[[E23 - Sitemap]]"
Next Episode: "[[E25 - Search Traffic Tab(Search Analytics)]]"
---
-------
## TOC
- [Search Console(Google Webmaster Tools) - Add Website](#Search%20Console(Google%20Webmaster%20Tools)%20-%20Add%20Website)
	- [What is Search Console(Google Webmaster Tools)?](#What%20is%20Search%20Console(Google%20Webmaster%20Tools)?)
	- [Start Working With Search Console(Google Webmaster Tools)](#Start%20Working%20With%20Search%20Console(Google%20Webmaster%20Tools))
- [Start Working - Initial Jobs & UI Description](#Start%20Working%20-%20Initial%20Jobs%20&%20UI%20Description)
	- [Initial Jobs](#Initial%20Jobs)
		- [Add Sitemap](#Add%20Sitemap)
		- [Redirect All Addresses of Website](#Redirect%20All%20Addresses%20of%20Website)
	- [UI Description](#UI%20Description)
		- [Dashboard](#Dashboard)
		- [Messages - Website Issues](#Messages%20-%20Website%20Issues)
		- [Search Appearance](#Search%20Appearance)
		- [Search Traffic](#Search%20Traffic)
		- [Google Index](#Google%20Index)
		- [Crawl](#Crawl)
		- [Security Issues](#Security%20Issues)
----------------
### Search Console(Google Webmaster Tools) - Add Website
#### What is Search Console(Google Webmaster Tools)?
ابزار Search Console یا Google Webmaster Tools که متعلق به گوگل است، یکی از حیاتی ترین ابزار های سئو مخصوصا برای موتور جستجو گوگل میباشد.
- **Google Webmaster Tools Duties:**
	1. اعلام گزارش عملکرد وبسایت 
	2. اعلام خطاهایی که برای خزنده های گوگل در وبسایت ما پیش آمده است.
	3. گزارش ورودی های وبسایت ما 
	4. گزارش از کلمات کلیدی وبسایت و برترین کلمات کلیدی وبسایت
	5. امکان معرفی تمام صفحات وبسایت و همینطور نقشه سایت `sitemap.xml` به آن
	6. امکان معرفی لینک های جدید
	7. مشاهده Broken Links ها و درخواست حذف آنها از گوگل
	8. اعلام تغییرات که در وبسایت اعمال شده 
	9. مشاهده پیشرفت سئو وبسایت ما
	10. و ....
#### Start Working With Search Console(Google Webmaster Tools)
1. Login to Your Google Account
2. Search [Search Console or Google Webmaster](Open https://www.google.com/webmasters/) Tools or Open Link 
	1. Open https://www.google.com/webmasters/
3. After Open, Click on Search Console
	1. ![Pasted image 20260124144526.png](/images/python/Pasted image 20260124144526.png)
4. Then Enter the URL in `Site URL` and Click on `Add Property`
5. Now we Should Verify Our Website
	1. برای تایید وبسایت روش های متفاوتی وجود دارد که راحت ترین آنها دانلود فایل html که خود Webmaster به ما داده و جایگذاری آن درون Root پروژه است:
		1. ![Pasted image 20260124145142.png](/images/python/Pasted image 20260124145142.png)
	2. روش های دیگری از جمله قرار دادن Meta Tag, DNS TXT Record, Google Analytics, Google Tag Manager میباشد:
		1. ![Pasted image 20260124145046.png](/images/python/Pasted image 20260124145046.png)
	3. *نکته:* بجای دانلود فایل مرحله اول میتوانیم یک فایل جدید با همان نامی که گوگل پیشنهاد داده نیز ایجاد کنیم.
6. After Verified you can see new property(your site) in Webmaster Tools plus Main Webmaster Tool Page
	1. Empty Panel: ![Pasted image 20260124145728.png](/images/python/Pasted image 20260124145728.png)
	2. Toplearn Panel: ![Pasted image 20260124145637.png](/images/python/Pasted image 20260124145637.png)
### Start Working - Initial Jobs & UI Description
#### Initial Jobs
##### Add Sitemap
در اولین قدم کار با Google Webmaster Tools باید نقشه سایت را برای آن تعریف کنیم.
1. `Webmaster Tools => Current Status => Click on Sitemaps`
	1. ![Pasted image 20260124145939.png](/images/python/Pasted image 20260124145939.png)
2. Then Click on Add Sitemap
	1. ![Pasted image 20260124150057.png](/images/python/Pasted image 20260124150057.png)
3. Enter URL of Sitemap(sitemap.xml) and Click on Submit
	1. ![Pasted image 20260124150216.png](/images/python/Pasted image 20260124150216.png)
4. *In Current Status Panel:*
	1. در قسمت Sitemaps یک Chart مشاهده میشود.
	2. اگر Chart به رنگ آبی باشد، یعنی لینک ها Submit ثبت شده اند.
	3. اگر به رنگ قرمز در آمدند به معنای این است که لینک ها توسط گوگل ایندکس شده است.
	4. *تصویر:*
		1. ![Pasted image 20260124154039.png](/images/python/Pasted image 20260124154039.png)
##### Redirect All Addresses of Website
در قدم دوم باید تمام آدرس های وبسایت یعنی شامل www یا http را به آدرس اصلی یعنی https://website.com ریدایرکت کنیم. برای اینکار:
1. `Right Gear => Site Settings`
	1. ![Pasted image 20260124152136.png](/images/python/Pasted image 20260124152136.png)
2. `Preferred Domain => Select => Display URLs as website.com`
	1. ![Pasted image 20260124152308.png](/images/python/Pasted image 20260124152308.png)
#### UI Description
##### Dashboard
در قسمت پیشخوان یا داشبورد Google Webmaster Tools گزارشی کلی از قسمت های مهم وبسایت دیده میشود. این گزینه ها عبارتند از:
1. New and Important
	1. مشکلات مهم در اینجا مشاهده میشوند.
2. Crawl Errors
	1. نمایش خطاهای خزنده ها:
		1. ![Pasted image 20260124154053.png](/images/python/Pasted image 20260124154053.png)
3. Search Analytics 
	1. نمایش آماری کلی تعداد کلیک ها یا همان ورودی هایی که از گوگل وارد وبسایت ما شده اند:
		1. ![Pasted image 20260124154104.png](/images/python/Pasted image 20260124154104.png)
4. Sitemaps
	1. نمایش وضعیت نقشه سایت و لینک های درون آن:
		1. ![Pasted image 20260124154111.png](/images/python/Pasted image 20260124154111.png)
5. Image:
	1. ![Pasted image 20260124153908.png](/images/python/Pasted image 20260124153908.png)
##### Messages - Website Issues
اگر وبسایت ما به مشکل جدی بر بخورد، Google Webmaster Tools به ایمیل میدهد که باید به این مشکلات و رفع آنها اهمیت دهیم.
- علاوه بر آن در `Dashboard => Messages` نیز میتوانیم این پیام های مهم را مشاهده کنیم:
	![Pasted image 20260124152502.png](/images/python/Pasted image 20260124152502.png)
- *نکته:* پیام هایی که در این قسمت مشاهده میشود را حتما باید جدی گرفت زیرا مشکل اساسی بوده کهGoogle Webmaster Tools پیام برای ما داده است.
##### Search Appearance 
در این گزینه ظاهر وبسایت ما تحلیل و بررسی میشود. در واقع قسمت های زیر در این منو مشاهده میشوند: 
1. Structed Data
2. Rich Cards
3. Data Highlighter
4. HTML Improvements
5. Accelerated Mobile Pages
6. Image:
	1. ![Pasted image 20260124153624.png](/images/python/Pasted image 20260124153624.png)
##### Search Traffic
یکی از قسمت های Google Webmaster Tools است که گزارش هایی از جستجو وبسایت ما را ارائه میدهد. در این منو گزینه های زیر مشاهده میشود:
1. Search Analytics
2. Link to Your Site
3. Internal Links
4. Manual Actions
5. International Targeting
6. Mobile Usability
7. Image:
	1. ![Pasted image 20260124153603.png](/images/python/Pasted image 20260124153603.png)
##### Google Index
در این منو وضعیت لینک های وبسایت نمایش داده میشوند. در واقع چه لینک هایی ایندکس شده اند، چه لینک هایی بلاک شده اند و یا چه لینک های حذف شده اند.
1. Index Status
2. Blocked Resource
3. Remove URLs
4. Image:
	1. ![Pasted image 20260124153223.png](/images/python/Pasted image 20260124153223.png)
##### Crawl 
در این قسمت گزارشاتی از خزنده های گوگل را مشاهده میکنیم. مثلا خطاهایی که خزنده ها در خزش وبسایت ما به آنها برخوردند و یا بررسی `robots.txt` و یا بررسی `sitemap.xml`. در این منو گزینه های زیر مشاهده میشوند:
1. Crawl Errors
2. Crawl Stats
3. Fetch as Google
4. `robots.txt` Tester
5. Sitemaps
6. URL Parameters
7. Image:
	1. ![Pasted image 20260124153448.png](/images/python/Pasted image 20260124153448.png)
##### Security Issues
در این تب هم مشکلات امنیتی وبسایت در صورت وجود نمایش داده میشوند:
	![Pasted image 20260124153530.png](/images/python/Pasted image 20260124153530.png)
### !
