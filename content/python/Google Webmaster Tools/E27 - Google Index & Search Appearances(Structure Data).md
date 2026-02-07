---
Episode: E27
Date: 2026-01-24
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 18:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E26 - Search Traffic Tab(Other Tabs)]]"
Next Episode: "[[E28 - Google Webmaster Tools, Other Menu's]]"
---
-------
## TOC
- [Google Index](#Google%20Index)
	- [How Google Index Links?](#How%20Google%20Index%20Links?)
	- [1. Google Index => Index Status](#1.%20Google%20Index%20=%3E%20Index%20Status)
	- [2. Google Index => Blocked Resources](#2.%20Google%20Index%20=%3E%20Blocked%20Resources)
	- [3. Google Index => Remove URLs](#3.%20Google%20Index%20=%3E%20Remove%20URLs)
- [Search Appearance Implementation(Structure Data)](#Search%20Appearance%20Implementation(Structure%20Data))
	- [Description](#Description)
	- [Elements Can Use for Showing Website in Search Results](#Elements%20Can%20Use%20for%20Showing%20Website%20in%20Search%20Results)
	- [Google Structure Data](#Google%20Structure%20Data)
		- [Description](#Description)
		- [Ways to Implement](#Ways%20to%20Implement)
	- [http://schema.org - Schema Archive](#http://schema.org%20-%20Schema%20Archive)
	- [Structure Data Writing - JSON LD](#Structure%20Data%20Writing%20-%20JSON%20LD)
		- [All Type of Structure Data](#All%20Type%20of%20Structure%20Data)
		- [1. Company Info in Right Side](#1.%20Company%20Info%20in%20Right%20Side)
		- [2. Product Rich Snippets](#2.%20Product%20Rich%20Snippets)
		- [Note for Other](#Note%20for%20Other)
		- [Best Structure Data](#Best%20Structure%20Data)
	- [Testing Structure Data](#Testing%20Structure%20Data)
- [Search Appearance Menu Description](#Search%20Appearance%20Menu%20Description)
	- [Search Appearance => Structured Data](#Search%20Appearance%20=%3E%20Structured%20Data)
- [Research](#Research)
-------------------
### Google Index
#### How Google Index Links?
1. گوگل تمام لینک های یک وبسایت را با بررسی `sitemap.xml` و همچنین خزنده هایش Crawlers بدست می آورد و پردازش میکند.
2. سپس لینک ها را درون دیتابیس موتور جستجو خود ثبت میکند.
3. هنگامیکه لینک وبسایت درون دیتابیس ثبت شد، به معنای Index شدن لینک توسط گوگل است.
#### 1. Google Index => Index Status
در این گزینه تعداد لینک هایی که از وبسایت ما درون دیتابیس گوگل ایندکس شده اند را میتوانیم مشاهده کنیم:
	![[Pasted image 20260124180915.png]]
- **با بررسی این گزینه میتوانیم متوجه موارد زیر شویم:**
	1. تعداد کل لینک های ایندکس شده(Total Indexed):
		1. ![[Pasted image 20260124181344.png]]
	2. روند تغییرات اعمال شده برای سئو خوب بوده یا نه
		1. مثلا اگر نمودار که در این قسمت مشاهده میکنیم بصورت صعودی باشد همینطور که در تصویر زیر مشاهده میکنید به معنی این است که روند رشد سئو عالی است:
			1. ![[Pasted image 20260124181437.png]]
		2. این رشد نتیجه استفاده از مطالب خوب از قبیل مقاله، نوشته، دوره و ... میباشد.
		3. یا مثلا در تصویر زیر میتوان مشاهده کرد که آمار رشد خطی بوده یعنی رشد زیادی نداشتیم:
			1. ![[Pasted image 20260124181545.png]]
	3. تغییر الگوریتم های موتور جستجو:
		1. مثلا در تصویر زیر مشاهده میکنیم که در تاریخ 09/09/2018 تعداد 3946 لینک ایندکس شده اند:
			1. ![[Pasted image 20260124181139.png]]
		2. اما در تاریخ 16/09/2018 این تعداد به 2331 لینک رسیده است:
			1. ![[Pasted image 20260124181251.png]]
		3. این آماد نشان دهنده تغییر الگوریتم گوگل و کاهش رتبه بندی سئو وبسایت ما میباشد که باید بر روی آن کار شود.
#### 2. Google Index => Blocked Resources
در این قسمت صفحاتی از وبسایت ما که دارای مشکل Error هستند و موتور جستجو آنها را بلاک کرده است را مشاهده میکنیم:
	![[Pasted image 20260124181648.png]]
- صفحات مشکل دار(بلاک شده) را که در این قسمت مشاهده میکنیم حتما باید مشکل آنها را برطرف کنیم تا تعداد این لینک ها و صفحات به صفر برسد.
#### 3. Google Index => Remove URLs
1. **Description:**
	- یکی از قسمت های مهم Google Index میباشد که در آن URL هایی که از وبسایت ما حذف شده اند اما بصورت دستی معرفی نشدند و گوگل آنها را به کاربر نمایش داده و کاربر با باز کردن آن خطای 404 دریافت کرده است را مشاهده میکنیم.
2. **How Add Removed URLs:**
	1. اگر که یه مطلب، صفحه یا پستی را از وبسایت خود حذف کردیم، گوگل بصورت خودکار متوجه حذف آن URL نمیشود و در نتیجه هنوز در نتایج جستجو آنرا به کاربر نمایش میدهد.
	2. حال اگر کاربری بر روی آن URL حذف شده کلیک کند و با خطای 404 روبرو شود با امتیاز منفی سئو روبرو میشویم که بسیار برای وبسایت بد است.
	3. برای جلوگیری از این کار و معرفی URL حذف شده باید از کلید زیر استفاده کنیم:
	4. `Google Index => Remove URLs => Temporarily Hide => Enter URL => Click on Continue`
		1. ![[Pasted image 20260124182300.png]]
- *نکته:* اینکار برای گوگل از ارزش بسیار بالایی برخوردار است و امتیاز مثبت برای سئو وبسایت ما دارد.
### Search Appearance Implementation(Structure Data)
#### Description
در این گزینه از Google Webmaster Tools نحوه نمایش وبسایت ما در موتور جستجو گوگل را مشخص میکنیم. 
- بصورت پیشفرض در نتیجه گوگل Website Title، URL، Short Description وبسایت در نتایج نشان داده میشود:
	- ![[Pasted image 20260124182651.png]]
- اما میتوان این نحوه نمایش را شخصی سازی کرد و مثلا مشخص کنیم که دسته بندی های وبسایت و یا امتیاز محصولات و یا قیمت محصولات جستجو شده نیز در نتیجه جستجو نمایش داده شوند:
	- ![[Pasted image 20260124182837.png]]
	- ![[Pasted image 20260124182833.png]]
#### Elements Can Use for Showing Website in Search Results
- برای مشاهده تمام المان هایی که میتوانیم برای نمایش وبسایتمان در گوگل از آنها استفاده کنیم، کافیست بر روی Question Mark ? در کنار Search Appearance کلیک کنیم:
	- ![[Pasted image 20260124183055.png]]
- **Search Appearance Elements:**
	1. Title - عنوان
	2. Snippet(Short Description) - توضیح کوتاه
	3. *Siteliks:*
		1. تعریف لینک هایی از وبسایت(مانند دسته بندی)
			1. ![[Pasted image 20260124183450.png]]
		2. در نتیجه کاربر با کلیک بر روی آنها مستقیما به صفحه مورد نظر میرود و نه صفحه اصلی وبسایت
	4. *Search Within a site:*
		1. فرم جستجو داخلی در وبسایت
			1. ![[Pasted image 20260124183634.png]]
	5. URL - آدرس کامل صفحه
	6. *Event - Rich Snippet:*
		1. نمایش رویداد های وبسایت با تاریخ
		2. مثلا میتوان نویسنده و بروز کننده مطلب را در نتیجه جستجو نشان دهیم:
			1. ![[Pasted image 20260124183557.png]]
	7. *Breadcrumbs*
		1. نمایش منو ناوبری در نتایج جستجو بجای URL کامل
			1. ![[Pasted image 20260124183904.png]]
	8. *Product Rich Snippet:*
		1. نمایش ویژگی های محصولات در نتایج جستجو(امتیاز بندی، نظرات و قیمت و ...)
	9. *Company Show:*
		1. یکی از ویژگی های زیبای Search Appearance نمایش اطلاعات کمپانی از قبیل توضیحات، لوگو، سازنده، توسعه دهنده و .... در سمت راست نتایج جستجو است:
			1. ![[Pasted image 20260124184049.png]]
- *نکته:* برای پیاده سازی این المان ها در نتایج جستجو گوگل باید از ویژگی بنام Structure Data استفاده کنیم.
#### Google Structure Data
##### Description
- برای نوشتن Structure Data که در واقع نوعی اسکریپت JSON است، قاعده مشخصی وجود دارد که در لینک زیر میتوان راهنمای آن را خواند:
	- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
		- ![[Pasted image 20260124185531.png]]
- همچنین ابزار های آنلاین هم هستند که به ساخت و یا تست Structure Data میپردازند.
- کدهای Structure Data باید درون کدهای صفحه مورد نظر ما قرار گیرند. مثلا در صفحه Index باید Structure Data ها را بنویسیم.
##### Ways to Implement
برای پیاده سازی Structure Data از روش های زیر استفاده میشود:
	![[Pasted image 20260124193310.png]]
1. JSON LD Script
	1. ![[Pasted image 20260124193417.png]]
2. Microdata
3. RDFa(HTML Tag Attributes)
	1. ![[Pasted image 20260124193253.png]]
- برای پیاده سازی Structure Data بیشتر از روش اسکریپت نویسی JSON LD Script استفاده میشود.
#### http://schema.org - Schema Archive
در تمامی اسکریپت های Structure Data که مینویسیم از این لینک استفاده میکنیم که در واقع آرشیو از تمام شماتیک های موجود است.
1. **Schema Type and Properties:**
	1. در واقع تمام انواع Schema ها را به همراه مشخصات تک تک آنها که در Structure Data از آنها استفاده میکنیم را در این وبسایت میتوانیم مشاهده کنیم:
		- ![[Pasted image 20260124190556.png]]
	2. مثلا انواع مختلف `type@` داریم، مانند `Organization, Health, Person, Place, Product, ...` که هر کدام مشخصات Property های خود را دارند:
		- مثلا نوع Organization مشخصات Property های خاص خود را دارد، مانند `contactType, telephone, name, altername, ...`
2. **See Each Type Property's:**
	1. برای مشاهده مشخصه های هر Type کافیست در وبسایت http://schema.org به منو Schemas رفته و سپس بر روی Type مورد نظرمان کلیک کنیم:
		1. ![[Pasted image 20260124191056.png]]
	2. با کلیک میتوانیم جدولی از مشخصه های موجود را مشاهده کنیم:
		1. ![[Pasted image 20260124191129.png]]
	3. با کلیک بر روی هر مشخصه نیز میتوانم نحوه مقدار دهی آن را مشاهده کنیم:
		1. ![[Pasted image 20260124191206.png]]
	4. همچنین در صفحه هر مشخص نیز میتوانیم مثال هایی از نحوه پیاده سازی آن Type مورد نظر را در هر سه فرمت پیاده سازی RDFa, Microdata, JSON LD مشاهده کنیم:
		1. ![[Pasted image 20260124193549.png]]
		2. ![[Pasted image 20260124193546.png]]
#### Structure Data Writing - JSON LD
##### All Type of Structure Data
1. در لینک زیر اسکریپت تمامی انواع Structure Data ها قابل مشاهده هستند:
	1. https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
##### 1. Company Info in Right Side
- Company(Organization) in Right Side of Search Results
```html , php
<script type="application/ld+json">
{
	"@context": "http://schema.org",
	"@type": "Organization",
	"url": "http://www.example.com",
	"name": "Unlimited Ball Bearings Corp.",
	"contactPoint": {
	"@type": "ContactPoint",
	"telephone": "+1-401-555-1212",
	"contactType": "Customer service"
	}
}
</script>
```
- **Description:**
	- این اسکریپت بالا یک توضیح از کمپانی دقیقا مانند دیجی کالا را در سمت راست محتوای جستجو شده برای کمپانی ما قرار میدهد:
		- ![[Pasted image 20260124190159.png]]
- Image:
	- ![[Pasted image 20260124185754.png]]
##### 2. Product Rich Snippets
```html , php
<script type="application/ld+json">
{
	"@context": "http://schema.org/",
	"@type": "Recipe",
	"name": "Grandma's Holiday Apple Pie",
	"author": "Elaine Smith",
	"image": "http://example.com/image"
	"description": "A classic apple pie.",
	"aggregateRating": {
		"@type": "AggregateRating",
		"ratingValue": "4",
		"reviewCount": "276",
		"bestRating": "5",
		"worstRating": "1"
	},
	
	"prepTime": "PT30M",
	"totalTime": "PT1H",
	"recipeYield": "8",
	"nutrition": {
		"@type": "NutritionInformation",
		"servingSize": "1 medium slice",
		"calories": "230 calories",
		"fatContent": "1 g",
		"carbohydrateContent": "43 g",
	},

	"recipeIngredient": [
	"1 box refrigerated pie crusts, softened as directed on box",
	"6 cups thinly sliced, peeled apples (6 medium)",
	"..."
	],
	
	"recipeInstructions": [
	"1 ...",
	"2 ..."
	]
}
</script>
```
- *Image:*
	- ![[Pasted image 20260124191952.png]]
- برای مشاهده تمام المان های کافیست در http://schema.org منو Schemas بر روی نوع Product کلیک کنیم تا تمام مشخصه ها م مقادیر آنها را مشاهده کنیم.
- همچنین در http://schema.org بخش مشخصه مربوطه مثال هایی از نحوه پیاده سازی این مدل از Structure Data که میخواهیم را نیز مشاهده میکنیم، در زیر مثال های پیاده سازی `aggregateRating` را مشاهده میکنید:
	- ![[Pasted image 20260124192240.png]]
	- ![[Pasted image 20260124192252.png]]
	- JSON-LD ![[Pasted image 20260124192305.png]]
##### Note for Other
تعداد Schema ها بسیار زیاد هستند بنابراین باید بر اساس نوع پست یا محصول یا هدفی که داریم Structure Data مناسب آنرا از وبسایت http://schema.org یا [Google Developer Structured Data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) بدست بیاوریم.
##### Best Structure Data
1. نمایش لوکیشن کمپانی در سمت راست
2. نمایش اطلاعات کمپانی
3. نمایش لینک های وبسایت به عنوان دسته بندی
4. نمایش فرم جستجو داخلی
5. نمایش امتیاز و تعداد نظرات برای محصولات که باعث افزایش فروش وبسایت میشود
#### Testing Structure Data
پس از اینکه Structure Data مورد نظر خود را نوشتیم، قبل از اینکه آنرا در وبسایت خود پابلیش کنیم برای اینکه خطایی نداشته باشد بهتر است که ابتدا آنرا تست کنیم. برای تست از [ابزار تست Structure Data گوگل](https://search.google.com/structured-data/testing-tool) با آدرس زیر استفاده میکنیم:
1. https://search.google.com/structured-data/testing-tool
	1. ![[Pasted image 20260124192748.png]]
در این ابزار میتوانیم لینک صفحه که  Structure Data در آن استفاده شده و یا خود اسکریپت Structure Data را بگذاریم تا آنرا تست کنیم.
نتیجه تست به شکل زیر میباشد که دارای سه هشدار بوده است:
	![[Pasted image 20260124192904.png]]
### Search Appearance Menu Description
#### Search Appearance => Structured Data
در این قسمت میتوانیم مشاهده کنیم که در کدام صفحات وبسایت از Structure Data استفاده شده و همچنین اگر خطایی نیز Structure Data ها دارند را به ما میگوید:
	![[Pasted image 20260124185932.png]]
### Research
1. Best Structure Data for website to increase SEO scores 