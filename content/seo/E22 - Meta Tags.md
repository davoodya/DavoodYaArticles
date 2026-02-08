---
Episode: E22
Date: 2026-01-23
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 30:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E21 - robots.txt]]"
Next Episode: "[[E23 - Sitemap]]"
---
-------
## TOC
- [Meta Tags Definition](#Meta%20Tags%20Definition)
- [Meta Tags](#Meta%20Tags)
	- [0. Introduction](#0.%20Introduction)
	- [1. Title](#1.%20Title)
	- [2. Description](#2.%20Description)
	- [3. Keywords](#3.%20Keywords)
	- [4. Canonical](#4.%20Canonical)
	- [5. ALT Images/Links](#5.%20ALT%20Images/Links)
	- [6. Robots](#6.%20Robots)
	- [7. Social Network Tags(Open Graphs)](#7.%20Social%20Network%20Tags(Open%20Graphs))
		- [7.1: Main Social Networks](#7.1:%20Main%20Social%20Networks)
		- [7.2: Twitter(X) Tags:](#7.2:%20Twitter(X)%20Tags:)
		- [7.3: Other Special Tags for Social Networks](#7.3:%20Other%20Special%20Tags%20for%20Social%20Networks)
	- [8. Copyright Tags](#8.%20Copyright%20Tags)
	- [9. Responsive Meta Tags](#9.%20Responsive%20Meta%20Tags)
	- [10. Other Meta Tags](#10.%20Other%20Meta%20Tags)
		- [Necessary Tags](#Necessary%20Tags)
		- [Priority 2](#Priority%202)
- [Research Topics](#Research%20Topics)
----------------
### Meta Tags Definition
متا تگ ها، تگ هایی هستند که در قسمت بالای کد HTML و درون تگ `<head>` قرار میگیرند و میتوان گفت راهنمایی برای معرفی وبسایت ما به موتور جستجو و شبکه های اجتماعی است.
- متا تگ ها امروزه تاثیر زیادی در سئو ندارند اما در رونق گیری کسب و کار و شبکه های اجتماعی بسیار کارآمد هستند و بودن Meta Tags ها در صفحات ما الزامی است.
### Meta Tags
#### 0. Introduction
در کل Meta Tags ها به 8 دسته متفاوت تقسیم میشوند که در این جلسه به توضیح این 9 دسته میپردازیم. این 9 دسته عبارتند از:
1. Title
2. Description
3. Canonical
4. ALT(Alternative Text)
5. Robots Tag
6. Social Media Tags(Title, Image, Description, ...)
7. Header Tags(H1 to H6)
8. Copyright Tags
9. Responsive Design Meta Tags
- **Notes:**
	- تمامی Meta Tags ها با تگ `<meta>` شروع نمیشوند و بسیاری از Meta Tags ها فقط درون تگ `<head>` قرار میگیرند.
	- برای بروز رسانی مطالب وبسایت که در افزایش رتبه بندی سئو موثر است میتوانیم از Meta Tags ها نیز استفاده کنیم.
#### 1. Title
1. **`<title>` Description:**
	- تگ `<title>` یکی از مهمترین تگ های صفحه است و در واقع عنوان تب صفحه را مشخص میکند. 
	- از این تگ برای بروز رسانی محتوای وبسایت نیز استفاده میشود زیرا که سریعا توسط گوگل ایندکس میشود.
- **`<title>` Notes:**
	- مقدار `<title>` برای صفحات وبسایت باید متفاوت باشد و در واقع دو صفحه نباید `<title>` آنها یکی باشد.
	- تعداد کاراکتر های این تگ باید بین 50 تا 60 کاراکتر باشد(تا 64 مجاز است اما بهتر است که زیر 60 باشد)
	- محتوای `<title>` باید عنوان صفحه که درون `<h1>` استفاده میشود باید متفاوت اما مترادف باشند، مثلا:
		- `<title>` آموزش جامع سئو
		- `<h1>` دوره آموزش SEO بهینه سازی وبسایت
```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>آکادمی DSecurity</title>
    
</head>
<body>
	<h1> آموزشگاه امنیت سایبری DSecurity </h1>
</body>
</html>
```
#### 2. Description
1. **`<meta name="description" content="">` Description:**
	1. در Meta Tags نیز توضیح مختصر صفحه را مینویسیم. محتویات این تگ باید با محتویات صفحه خودمان یکسان باشد.
	2. وجود این Meta Tags برای موتور جستجو و معرفی توضیح مختصر وبسایت واجب است.
	3. اگر این تگ نباشد موتور جستجو فکر میکند وبسایت بصورت اتوماتیک ایجاد شده است و یک ربات آنرا ساخته است.
	4. اگر که این مقدار این تگ با محتوای صفحه یکسان باشد موتور جستجو این توضیحات را به عنوان توضیح مختصر در گوگل نمایش میدهد:
		1. ![Pasted image 20260123153817.png](/images/seo/Pasted image 20260123153817.png)
2. **`<meta name="description" content="">` Rules:**
	1. تعداد کاراکتر بین 160 تا 300 - البته در Rank Math پیشنهاد میکند تا 160 کاراکتر باشد.
```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="آموزش امنیت سایبری، شبکه، لینوکس، برنامه نویسی ابزار های امنیتی، تست نفوذ، امن سازی و موضوعات مرتبط توسط مدرسان و اساتید مجرب این حوزه">
    <title>آکادمی امنیت سایبری DSecurity</title>
    
</head>
<body>
</body>
</html>
```
#### 3. Keywords
1. `<meta name="keywords" content="">`
#### 4. Canonical
1. **`<link rel="canonical" href="main-url">` Description:**
	1. فرض کنید که در وبسایت چندین صفحه داریم که همگی مربوط به یک صفحه اصلی میشوند، و یا یک صفحه داریم که یک URL کامل با کلمات فارسی دارد و یک URL کوتاه شده نیز دارد.
	2. در این نوع صفحات باید مشخص کنیم که این نوع صفحات مرتبط به یک صفحه اصلی هستند و در واقع خودشان قسمتی از آن صفحه هستند.
	3. برای پیاده سازی این مورد از Meta Tags بنام Canonical(`rel="canonical"`) استفاده میکنیم که روش استفاده از آن بصورت زیر میباشد:
		1. `<link rel="canonical" href="https://website.com/main_url">`
2. **`<link rel="canonical" href="main-url">` Notes:**
	1. اگر صفحه مرتبط به یک صفحه دیگر باشد و با استفاده از `rel="canonical"` لینک اصلی آنرا مشخص نکنیم، موتور جستجو مطلب را Duplicate فرض میکند و باعث کاهش رتبه بندی سئو ما میشود.
	2. همچنین اگر تعداد این صفحات Duplicate زیاد نباشد میتوانیم از `robots.txt` نیز استفاده کنیم اما اگر این تعداد زیاد باشد بهترین کار استفاده از `rel="canonical"` میباشد.
3. **`<link rel="canonical" href="main-url">` Usages:**
	1. اگر دو URL بلند و کوتاه شده داریم در صفحه ای که URL بلند قرار دارد URL کوتاه شده را به عنوان URL اصلی معرفی میکنیم.
	2. اگر برای نمایش یک صفحه در موبایل از یک URL و برای نمایش یک صفحه در دسکتاپ از یک URL دیگر استفاده میکنیم، در صفحه موبایل باید صفحه اصلی وب را به عنوان مرجع معرفی کنیم.
```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>آکادمی امنیت سایبری DSecurity</title>
    <meta name="description" content="آموزش امنیت سایبری، شبکه، لینوکس، برنامه نویسی ابزار های امنیتی، تست نفوذ، امن سازی و موضوعات مرتبط توسط مدرسان و اساتید مجرب این حوزه">
    <link rel="canonical" href="https://website.com/long-url-لینک-بلند">
</head>
<body>
</body>
</html>
```

#### 5. ALT Images/Links
1. **`<img src="" alt="">` Description:**
	1. بصورت کلی اگر کاربر در Google Images جستجو انجام دهد گوگل از ALT تصاویر برای نمایش نتایج جستجو استفاده میکند و در واقع خود تصاویر را ایندکس نمیکند.
	2. بنابراین در نظر گرفتن ALT برای تصاویر امری الزامی است که حتما برای افزایش رتبه بندی سئو باید رعایت شود.
2. **`<img src="" alt="">` Rules:**
	1. تعداد کاراکتر 16 کلمه بیشتر نباشد و حداقل نیز 50 کلمه باشد.
	2. مقدار ALT تصویر با موضوع صفحه و مطلب یکسان باشد.
#### 6. Robots
1. **`<meta name="robots" content="follow,index">` Description:**
	1. این تگ را نیز که جلسه قبلی توضیح دادیم. در بیشتر مواقع و بصورت استاندارد `follow, index` باید باشد.
2. **Usage of `nofollow, noindex`:**
	1. اما در بعضی مواقع مانند زیر نیاز است که صفحه `nofollow, noindex` باشد:
	2. در صفحات نظرات و بحث های کاربران بهتر است که صفحه `nofollow` باشد زیرا که ممکن است لینک های بی مربوطی در صفحه استفاده شود.
	3. و یا صفحات مدیریتی وبسایت نیاز به ایندکس توسط گوگل ندارند بنابراین باید `noindex` شوند.
	4. اگر در یک صفحه تعداد زیادی لینک استفاده شده، باید `nofollow` باشد.
```html
<meta name="robots" content="noodp,noydir"/>
<meta name="googlebot" content="index,follow"/>
<meta name="googlebot-Image" content="noindex,nofollow"/>
```
- **تحقیق:** مقادیر `noodp,noydir` در تگ `robots` به چه معناست؟
#### 7. Social Network Tags(Open Graphs)
##### 7.1: Main Social Networks
1. **`<og>` Open Graph Tags Description:**
	1. برای یکپارچه سازی وبسایت ها با شبکه های اجتماعی ابتدا فیسبوک Meta Tag اختصاصی را بنام Open Graph معرفی کرد. این تگ ها بعدا توسط لینکدین، توئیتر، تلگرام و سایر شبکه های اجتماعی نیز شناخته شد. 
		1. البته شبکه های اجتماعی دیگر مانند توئیتر تگ های مخصوص خود را نیز دارند.
	2. در این نوع از Meta Tags ها مشخص میکنیم که اگر مطلب ما در صفحات اجتماعی به اشتراک گذاشته شد، از چه *عنوان، تصویر، توضیح کوتاه و لینکی* استفاده شود.
	3. در تصویر زیر میتوانید این قسمت ها که همگی در Open Graph مشخص شده اند را مشاهده کنید:
		1. ![Pasted image 20260123161202.png](/images/seo/Pasted image 20260123161202.png)
	4. بنابراین با استفاده از Open Graph ها میتوانیم مشخص کنیم مطلب ما در صورت به اشتراک گذاری چگونه در شبکه های اجتماعی دیده شود.
2. **Open Graph Tags:**
```html
# Priority 1
<meta property="og:type" content="article"/>
<meta property="og:title" content="Title of Article"/>
<meta property="og:description" content="Article Description"/>
<meta property="og:image" content="https://website.com/article-image-url"/>
<meta property="og:url" content="https://website.com/articles/article-url"/>
<meta property="og:site_name" content="DSecurity(Name of Website)"/>
<meta name="og:page_id" content="2115"/>

# Priority 2
<meta property="og:region" content="Tehran"/>
<meta property="og:country-name" content="Iran"/>
```
- **نکته:** تگ هایی که در Priority 2 نوشتیم واجب به استفاده نیست و در واقع اگر از Google Webmaster استفاده کنیم این تگ ها بصورت خودکار به صفحه اضافه میشوند.
##### 7.2: Twitter(X) Tags:
همانطور که گفتیم توئیتر نیز تگ های مربوط و مخصوص خود را دارد:
```html
<meta name="twitter:title" content="Article Title"/>
<meta name="twitter:description" content="Article Description"/>
<meta name="twitter:image" content="https://website.com/article-image-url"/>

<!-- twitter:site === یوزرنیم خودمان در توئیتر -->
<meta name="twitter:site" content="@twitter-username"/>

TWO BELOW CHECK NEEDED
<!-- twitter:owner === سازنده مقاله -->
<meta name="twitter:owner" content="@twitter-username"/>

<!-- twitter:author === نویسنده مقاله --> 
<meta name="twitter:author" content="@twitter-username"/>

مقدار دو تگ بالا میتواند نام یا یوزرنیم توئیتر باشد
```
##### 7.3: Other Special Tags for Social Networks
برای تمام شبکه های اجتماعی از جمله Facebook, Instagram, Telegram, .... نیز تگ های مخصوصی وجود دارند که میتوانیم از آنها استفاده کنیم. مثلا:
```html
مشخص کردن آیدی فیسبوک
<meta name="fb:page_id" content=31562/>
```
- **تحقیق:** در مورد سایر تگ های شبکه های اجتماعی نیز تحقیق کنید.
#### 8. Copyright Tags
دو تگ دیگر نیز برای مشخص کردن حق کپی رایت صفحه وبسایت وجود دارد که بهتر است از آن استفاده شود اما الزامی نیستند.
```html
<meta name="author" content="داوود یاحی Davood Yahay"/>
<meta name="owner" content="داوود یاحی Davood Yahay"/>
```
- **Note:** Google Plus Username
	- شبکه اجتماعی Google Plus قابلیتی دارد که اگر Username Google Plus را بجای نام در دو تگ کپی رایت استفاده کنیم تصویر کاربری Google Plus را در کنار نام نویسنده و سازنده مقاله نشان میدهد.
	- البته این قابلیت در قدیم بوده و باید تست شود.
#### 9. Responsive Meta Tags
یکسری از Meta Tags ها نیز برای ریسپانسیو کردن صفحه و سازگاری صفحه با تمامی دیوایس ها استفاده میشود:
```html
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="X-UA-Compatible" content="yes"/>
```
- `<meta name="viewport" content="width=device-width, initial-scale=1"/>`
	- این تگ مهمترین تگ قسمت Responsive Meta Tags ها میباشد و به موتور جستجو میگوید که وبسایت ما Responsive میباشد.
#### 10. Other Meta Tags
##### Necessary Tags
```html
<meta http-equiv="Content-Type" content="text/html" charset="utf-8"/>
<meta name=language content=fa/>
```
##### Priority 2
تعداد Meta Tags ها زیاد است. یکسری از آنها توسط Google Webmaster به صفحه اضافه میشوند و یکسری نیز توسط سایر افزونه های سئو. اما اضافه کردن آنها نیز عالیست. مثلا: 
```html
<meta name=distribution content=global/>
<meta name=rating content=general/>
<meta name="coverage" content="worldwide"/>
```
### All Meta Tags
```html
<html lang="en">

<head>
    <title>آکادمی DSecurity</title>
    <meta charset="UTF-8">
    <meta name="description" content="آموزش امنیت سایبری، شبکه، لینوکس، برنامه نویسی ابزار های امنیتی، تست نفوذ، امن سازی و موضوعات مرتبط توسط مدرسان و اساتید مجرب این حوزه">
    <link rel="canonical" href="https://website.com/long-url-لینک-بلند">
    <meta name="keywords" content="">

    <!-- Robots Tags -->
    <meta name="robots" content="index,follow">
    <meta name="googlebot" content="index,follow"/>
    <meta name="googlebot-Image" content="index,follow"/>


    <!-- Responsive Tags -->
    <meta name="apple-mobile-web-app-capable" content="yes"/>
    <meta name="X-UA-Compatible" content="yes"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Social Network Open Graph Tags -->
    <meta property="og:type" content="article"/>
    <meta property="og:title" content="Title of Article"/>
    <meta property="og:description" content="Article Description"/>
    <meta property="og:image" content="https://website.com/article-image-url"/>
    <meta property="og:url" content="https://website.com/articles/article-url"/>
    <meta property="og:site_name" content="DSecurity(Name of Website)"/>
	
	<!-- Facebook Tags -->
    <meta name="fb:page_id" content=31562/>
    
    <!-- Twitter Tags -->
    <meta name="twitter:title" content="Article Title"/>
    <meta name="twitter:description" content="Article Description"/>
    <meta name="twitter:image" content="https://website.com/article-image-url"/>
    <meta name="twitter:site" content="@twitter-username"/>
    <meta name="twitter:owner" content="@twitter-username"/>
    <meta name="twitter:author" content="@twitter-username"/>

    <!-- Copyright Tags -->
    <meta name="author" content="داوود یاحی Davood Yahay"/>
    <meta name="owner" content="داوود یاحی Davood Yahay"/>

    <!-- Other Tags -->
    <meta name=language content=fa/>    
    <meta name=distribution content=global/>
    <meta name=rating content=general/>
    <meta name="coverage" content="worldwide"/>
</head>

<body>
    <h1> آموزشگاه امنیت سایبری DSecurity </h1>
    <img src="" alt="">
</body>
</html>
```
### Research Topics
1. **تحقیق:** مقادیر `noodp,noydir` در تگ `robots` به چه معناست؟
2. **تحقیق:** در مورد سایر تگ های شبکه های اجتماعی نیز تحقیق کنید.
### !