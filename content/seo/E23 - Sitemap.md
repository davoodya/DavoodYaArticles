---
Episode: E23
Date: 2026-01-23
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
Pervious Episode: "[[E22 - Meta Tags]]"
Next Episode: "[[E24 - Google Webmaster Tools(Search Console) Basics & Concepts]]"
---
-------
## TOC
- [Sitemap](#Sitemap)
	- [What is Sitemap?](#What%20is%20Sitemap?)
	- [Create Sitemap](#Create%20Sitemap)
		- [Manual Creation](#Manual%20Creation)
		- [Automatic Creation - Online Tools](#Automatic%20Creation%20-%20Online%20Tools)
		- [Create Sitemap in Wordpress](#Create%20Sitemap%20in%20Wordpress)
	- [Update Sitemap Automatically(Dynamic Sitemap)](#Update%20Sitemap%20Automatically(Dynamic%20Sitemap))
	- [Break Sitemap](#Break%20Sitemap)
------
### Sitemap
#### What is Sitemap?
1. نقشه سایت یا Sitemap راهنمایی برای موتور جستجو است که دو دو نسخه HTML , XML تولید میشود.
2. نسخه XML مربوط به موتور جستجو است و نسخه HTML نیز مربوط به کاربران وبسایت میباشد(البته وجود نسخه HTML واجب نیست اما بهتر است باشد)
3. در واقع بهترین نقشه وبسایت برای کاربر، صفحه اصلی وبسایت است که بیشترین استفاده را از آن میبرد.
4. نسخه XML نقشه وبسایت `sitemap.xml` باید در مسیر زیر قرار بگیرد:
	1. https://website.com/sitemap.xml
		1. ![Pasted image 20260123175336.png](/images/seo/Pasted image 20260123175336.png)
5. در `sitemap.xml` تمام لینک های وبسایت و بروز رسانی ها قرار میگیرند و برای موتور جستجو و همچنین Webmaster Toolkit نیز بسیار مهم است.
6. نقشه سایت هر روز توسط موتور جستجو بررسی میشود تا اگر لینک و صفحه جدیدی به وبسایت اضافه شده بود در گوگل ایندکس شود. 
#### Create Sitemap
##### Manual Creation
برای ساخت sitemap میتوانیم بصورت دستی عمل کنیم که با یکسری از پارامتر ها ساخته میشود. پارامتر های `sitemap.xml` عبارتند از:
1. `<url>` 
	1. پارامتر اصلی `sitemap.xml` میباشد که برای تعریف لینک ها استفاده میشود.
2. `<loc></loc>`
	1. این تگ درون `<url>` نوشته میشود. درون این تگ URL که میخواهیم تعریف کنیم را مینویسیم.
	2. `<loc>https://dsecurity.com</loc>`
	3. *نکته:* بهتر است که از Shortener URL در این پارامتر استفاده کنیم و سپس در صفحه اصلی که لینک فارسی و طولانی دارد تگ Canonical را استفاده کنیم و Shortener URL را به عنوان صفحه اصلی معرفی کنیم.
3. `<lastmod>`
	1. این تگ درون `<url>` نوشته میشود.
	2. درون این تگ هم تاریخ آخرین تغییر این لینک را مینویسیم.
	3. `<lastmod>2022-11-04</lastmod>`
4. `<changefreq>`
	1. این تگ درون `<url>` نوشته میشود.
	2. درون این تگ مشخص میکنیم که موتور جستجو هر چند وقت یکبار بدنبال این لینک بیاید.
	3. مقادیری که برای آن میتوانیم استفاده کنیم عبارتند از:
	4. `daily, weekly, monthly, yearly`
	5. *نکته:* البته موتور جستجو زیاد به این پارامتر توجه نمیکند اما باید در نقشه سایت تعریف شود.
5. `<priority>`
	1. این تگ درون `<url>` نوشته میشود.
	2. اولویت یا اهمیت لینک صفحه که تعریف کردیم را نیز درون این پارامتر مشخص میکنیم.
	3. مقدار اولویت باید عددی بین 0 تا 1 باشد:
		1. `0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1`
	4. این اعداد همچنین میتواند از اعداد اعشاری نیز تشکیل شود:
		1. `0.33, 1.00, 0.958, 0.56, ...`
	5. مثلا اولیت صفحه اصلی ما باید بالاترین اولویت یعنی 1 باشد.
```xml
<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">
<url>
	<loc>https://dsecurity.com</loc>
	<lastmod>2022-11-04</lastmod>
	<changefreq>daily</changefreq>
	<priority>1</priority>
</url>
```
##### Automatic Creation - Online Tools
- روش دیگر ساخت `sitemap.xml` استفاده از ابزار های آنلاین است که یکی از بهترین آنها ابزار [XML-Sitemap](https://www.xml-sitemaps.com) میباشد:
	- https://www.xml-sitemaps.com
		- ![Pasted image 20260123181427.png](/images/seo/Pasted image 20260123181427.png)
- **Create Site Map using XML-Sitemap:**
	- برای ساخت نقشه سایت کافیست URL را وارد کنیم و سپس Start را بزنیم. 
	- سپس باید چند دقیقه صبر کنیم تا نقشه سایت را بصورت کامل برای ما بسازد و سپس نیز میتوانیم نقشه سایت را دانلود کنیم:
		- ![Pasted image 20260123182621.png](/images/seo/Pasted image 20260123182621.png)
	- در آخر نیز کافیست که  `sitemap.xml` را در Root وبسایت خودمان قرار دهیم.
- **نکته:** وقتی با این روش نقشه سایت را ایجاد میکنیم صفحاتی که بر روی `noindex` تنظیم شده اند درون `sitemap.xml` قرار نمیگیرند.
- **نکته دوم:** هنگامیکه به وبسایت صفحات جدید اضافه میشود و در واقع URL جدید به وبسایت اضافه میشود باید `sitemap.xml` را بروز کنیم. اینکار را حتما باید در بازه زمانی مشخصی انجام دهیم.
##### Create Sitemap in Wordpress
برای ساخت `sitemap.xml` در وردپرس افزونه های جانبی زیادی وجود دارند و حتی افزونه های سئو مانند Rank Math, Yoasat نیز بطور خودکار نقشه سایت را ایجاد و بروز میکنند.
#### Update Sitemap Automatically(Dynamic Sitemap) 
برای بروز رسانی Sitemap میتوانیم از Dynamic Sitemap استفاده کنیم. برای پیاده سازی این مورد میتوانیم از روش های زیر استفاده کنیم:
1. میتوانیم با استفاده از برنامه نویسی و حلقه ها تولید نقشه سایت را بصورت روزانه انجام دهیم، سپس نقشه ساخته شده را برای 24 ساعت کش کنیم و دوباره همینکار را فردا نیز انجام دهیم.
2. علاوه بر آن با استفاده از Cron ها و اسکریپت پایتون و سپس اجرای آن درون Shell میتوانیم ساخت نقشه سایت جدید را با استفاده از ابزار آنلاین انجام دهیم، سپس با آنرا با نقشه سایت فعلی `sitemap.xml` جایگذاری کنیم.
#### Break Sitemap
1. **Description:**
	- نقشه سایت اصولا نباید تعداد زیادی لینک را در خود داشته باشد. در واقع اگر در وبسایت بیشتر از 50000 داریم حتما باید `sitemap.xml` را به چندین فایل کوچکتر بشکنیم.
	- البته 50000 استاندارد تعریف شده است و پیشنهاد میشود اگر بیش از 5000 صفحه هم دارید حتما لینک ها شکسته شود.
2. **How Break Sitemap?**
	- لینک های اصلی صفحه از جمله منو های اصلی، دسته بندی ها، صفحه های اصلی از جمله تماس با ما ارتباط با ما درباره ما و .... را در `sitemap.xml` اصلی قرار دهیم.
	- سپس سایر لینک ها یعنی زیر دسته بندی های هر دوره ها، لینک مقالات و ... را هر کدام را در یک `sitemap.xml` جداگانه قرار دهیم.
### !