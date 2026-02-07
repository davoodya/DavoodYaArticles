---
Episode: E42
Date: 2026-02-01
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 17:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E41 - Google Analytics(Conversions - Goals - Funnels)]]"
Next Episode: "[[E43 - Google Analytics(Conversion - Ecommerce - Marketing)]]"
---
-------
## TOC
- [Description](#Description)
	- [Description](#Description)
	- [Usage](#Usage)
	- [Enable Ecommerce](#Enable%20Ecommerce)
		- [1. Enable Ecommerce in Google Analytics Admin](#1.%20Enable%20Ecommerce%20in%20Google%20Analytics%20Admin)
		- [2. Add Script to Your Website](#2.%20Add%20Script%20to%20Your%20Website)
		- [3. Ecommerce Script](#3.%20Ecommerce%20Script)
- [Google Analytics => Conversion => Ecommerce](#Google%20Analytics%20=%3E%20Conversion%20=%3E%20Ecommerce)
	- [1. Overview](#1.%20Overview)
	- [2. Shopping Behavior](#2.%20Shopping%20Behavior)
	- [3. Checkout Behavior](#3.%20Checkout%20Behavior)
	- [4. Product Performance](#4.%20Product%20Performance)
	- [5. Sales Performance](#5.%20Sales%20Performance)
	- [6. Product List Performance](#6.%20Product%20List%20Performance)
----------------------
### Description
#### Description
قابلیت Ecommerce(فروشگاه) در واقع نوعی حسابداری داخلی در Google Analytics است که به ما گزارشی از مقدار فروش و درآمد وبسایت را به ما میدهد.
برای وبسایت های فروشگاهی استفاده از این قابلیت بسیار کارآمد است.
- **نکته:** همانطور که گفتیم قسمت Ecommerce دقیقا مانند یک نرم افزار حسابداری عمل میکند و آمارهایی از فروش را به ما میدهد. حال در مواردی که بر روی سئو یک فروشگاه  کار میکنیم که اجازه دسترسی به نرم افزار حسابداری آنرا نداریم در اینجا فعال کردن این گزینه و استفاده از آن بسیار مفید است.
#### Usage
1. *بدست آوردن مشکل یک محصول که به فروش نمیرود.*
	1. مهمترین کاربرد این منو است که میتوانیم مشکل یک محصول که به فروش نمیرسد را بدست بیاوریم.
	2. آیا محصول در دید کاربر نیست؟ 
	3. آیا قیمت بالاست؟
2. بدست آوردن محصولات پرفروش
3. بدست آوردن عبارت های جستجو شده که منجر به خرید شده اند.
4. مشاهده بر ترین محصولات که در Related Products نمایش داده شده اند و منجر به خرید شده اند.
5. ثابت کردن آمار فروش به کارفرما
	1. در بعضی مواقع کارفرما برای اینکه هزینه سئو را کمتر بدهد از فروش پایین شکایت میکند. 
	2. در این مواقع ما هم دسترسی به سیستم حسابداری نداریم تا آمار کلی فروش را مشاهده کنیم.
	3. در اینجا میتوانیم با فعالسازی این گزینه آمار فروش را بصورت دقیق داشته باشیم و به کارفرما نشان دهیم.
#### Enable Ecommerce
##### 1. Enable Ecommerce in Google Analytics Admin
این قابلیت بصورت پیشفرض در Google Analytics فعال نیست و باید بصورت دستی فعال شود. برای اینکار:
1. `Google Analytics => Admin => Ecommerce Settings => Enable Ecommerce`
	1. ![[Pasted image 20260201212956.png]]
2. `Google Analytics => Admin => Ecommerce Settings => Enable Enhanced Ecommerce Reporting` 
	1. پس از فعال سازی Ecommerce با فعال کردن این گزینه میتوانیم گزارش دقیق از نحوه فروش و مقدار در آمد را بدست بیاوریم:
		1. ![[Pasted image 20260201213153.png]]
3. `Google Analytics => Admin => Ecommerce Settings => Checkout Labeling` 
	1. در این گزینه نیز میتوانیم مراحلی که کاربر تا نهایی کردن خرید خود پیمایش میکند را تعریف کنیم. 
	2. مثلا کاربر ابتدا به صفحه سبد خرید، سپس به تسویه حساب و سپس به صفحه تشکر از پرداخت میرود. حال میتوانیم هر یک از این قسمت ها را به عنوان یک مرحله تعریف کنیم تا آماری از هر مرحله را بصورت دقیق داشته باشیم:
		1. ![[Pasted image 20260201213425.png]]
	3. **نکته:** مراحلی که در این قسمت تعریف میشود در واقع همان Funnel Steps تا رسیدن به هدف نهایی یعنی خرید کاربر میباشند.
##### 2. Add Script to Your Website
1. **Add Ecommerce Script to your Website:**
	1. برای اینکه Google Analytics مقادیر فروش شما را بدست بیاورد باید اسکریپت مربوط به آنرا در صفحه نهایی خود(یعنی صفحه تشکر از پرداخت که پس از نهایی شدن خرید به کاربر نمایش داده میشود) قرار دهید.
	2. برای مشاهده این اسکریپت کافیست عبارت `google analytics data layer enhaced ecommerce` را در گوگل جستجو کنیم و سپس به وبسایت مربوط به آدرس زیر برویم:
	3. https://developers.google.com/tag-manager/enhanced-ecommerce
		1. ![[Pasted image 20260201214004.png]]
2. **Select Data layer:**
	1. در مرحله بعدی باید بر رویی عملیاتی که میخواهیم رهگیری شود کلیک کنیم تا اسکریپت آن را مشاهده کنیم:
		1. ![[Pasted image 20260201214231.png]]
	2. *این عملیات ها عبارتند از:*
			1. . Product Impressions
			2. Product Clicks
			3. Product Detail Impressions
			4. Add / Remove from Cart
			5. Promotion Impressions
			6. Promotion Clicks
			7. Checkout
			8. Purchases
			9. Refunds
	3. مثلا اسکریپت Data Layer بنام Product Impression اسکریپت به شکل زیر میباشد:
		1. ![[Pasted image 20260201214251.png]]
	4. عملیات Product Impression پر استفاده ترین عملیات هاست که در وبسایت نیاز است.
3. **Dynamic Script:**
	1. پس از کپی کردن و جایگذاری اسکریپت در وبسایت باید اسکریپت را بصورت داینامیک در بیاوریم تا مقادیری از قبیل `name, id, price, brand, category, variant, position` بصورت داینامیک بر اساس مقادیر محصول تکمیل شود:
		1. ![[Pasted image 20260201214531.png]]
4. **Note:** Add Script using **Google Tag Manager**
	1. اضافه کردن اسکریپت به وبسایت را با استفاده از ابزار Google Tag Manager براحتی میتوانیم انجام دهیم که برای اینکار ابتدا نیاز داریم که در در Google Tag Manager ثبت نام و وبسایت خود را به آن معرفی کنیم.
5. **Note 2:** 
	1. تمام این اسکریپت ها را در صفحه نهایی شدن خرید(تشکر از خرید شما) میتوانیم قرار دهیم.
##### 3. Ecommerce Script
1. Product Impression Static Script
```html
<script>
// Measures product impressions and also tracks a standard
// pageview for the tag configuration.
// Product impressions are sent by pushing an impressions object
// containing one or more impressionFieldObjects.
dataLayer.push({
	'ecommerce': {
	'currencyCode': 'EUR',
	'impressions': [
	
	'name' : 'Triblend Android T-Shirt',
	'id': '12345',
	'price' : '15.25',
	'brand': ]Google',
	'category': 'Apparel',
	'variant': 'Gray',
	'list': 'Search Results',
	'position': 1
	
	// Local currency is optional.
	
	// Name or ID is required.
	
	'name': 'Donut Friday Scented T-Shirt',
	'id': '67890',
	'price': '33.75',
	'brand' : 'Google',
	'category': 'Apparel',
	'variant': 'Black',
	'list': 'Search Results',
	'position' : 2
	
	}):
</script>
```
2. Product Impression Dynamic Script
```html
<script>
/ **
* Call this function when a user clicks on a product link. This function uses the event
* callback datalayer variable to handle navigation after the ecommerce data has been sent
* to Google Analytics.
* @param {Object} productObj An object representing a product.
*/
function(productObj) {
	dataLayer.push({
	'event': 'productClick',
	'ecommerce': {
	'click': {
	'actionField': {'list': 'Search Results'},
	'products': [{
	'name' : productObj.name,
	'id': productObj.id,
	'price': productObj.price,
	'brand': product0bj.brand,
	'category': product0bj.cat,
	'variant': productObj.variant,
	'position': productObj.position
	
	// Optional list property.
	
	// Name or ID is required.
	
	'eventCallback': function() {
	document.location = productObj.url

</script>
```
### Google Analytics => Conversion => Ecommerce
#### 1. Overview
1. **Description:**
	1. در این منو آماری کلی از فروش و در آمد وبسایت را به همراه محصولات پرفروش و پر بازدید وبسایت را مشاهده میکنیم:
		1. ![[Pasted image 20260201215438.png]]
#### 2. Shopping Behavior
1. **Description:**
	1. در این قسمت آماری کلی از رفتار فروش مشاهده میشود:
		1. ![[Pasted image 20260201215604.png]]
2. **Reading Shopping Behavior:**
	1. در تصویر زیر مشاهده میکنیم که تعداد 19513 برای خرید وارد وبسایت شده اند که 15174 نفر آنها در همان مرحله اول خرید را لغو کرده اند:
		1. ![[Pasted image 20260201215718.png]]
	2. سپس تعداد 4253 نفر محصولات ما را مشاهده کرده اند که 2974 نفر آنها عملیاتی بر روی محصول انجام ندادند:
		1. ![[Pasted image 20260201215834.png]]
	3. همچنین تعداد 1178 نفر محصولی را به سبد خرید خود اضافه کرده اند که 895 نفر آنها سبد خرید خود را لغو کرده اند:
		1. ![[Pasted image 20260201215926.png]]
	4. سپس 470 نفر به صفحه تسویه حساب رفته اند که 456 نفر تسویه حساب را لغو کرده اند:
		1. ![[Pasted image 20260201220013.png]]
	5. در آخر 14 کاربر داشته ایم که خرید خود را کامل کردند و محصولی را از وبسایت ما خریداری کرده اند:
		1. ![[Pasted image 20260201220047.png]]
3. **Table in End of Page:**
	1. در جدول آخر صفحه نیز آمار خرید بر اساس New Visitors, Returning Visitors قابل مشاهده هستند که از اینجا میتوانیم مشتریان جدید وبسایت خود را بدست بیاوریم:
		1. ![[Pasted image 20260201220159.png]]
	2. در آماری که بررسی کردیم یعنی 14 نفر خرید کامل، تعداد 9 نفر New Visitor و 5 نفر Returning Visitors بوده اند:
		1. ![[Pasted image 20260201220250.png]]
#### 3. Checkout Behavior
1. **Description:**
	1. در این منو آماری از کاربران که به صفحه تسویه حساب Checkout مراجعه کردند را به صورت کامل میتوانیم مشاهده کنیم:
		1. ![[Pasted image 20260201220406.png]]
2. **Reading Checkout Behavior:**
	1. 322 نفر وارد صفحه Checkout(Billing & Shipping) شده اند.
	2. 252 نفر به صفحه Payment رفته اند.
	3. 15 نفر به صفحه نظر سنجی پس از خرید رفته اند.
	4. 14 نفر خرید را تکمیل کرده اند.
	5. *تصویر:*
		1. ![[Pasted image 20260201232416.png]]
#### 4. Product Performance
1. **Description:**
	1. در این قسمت گزارشی از فروش هر یک محصولات را مشاهده میکنیم:
		1. ![[Pasted image 20260201232615.png]]
2. **Usage:**
	1. با استفاده از این گزینه میتوانیم کل فروش یک محصول، تعداد فروش، تعداد دفعات اضافه شدن محصول به سبد خرید و .... را مشاهده کنیم:
		1. ![[Pasted image 20260201233103.png]]
	2. در نتیجه میتوانیم محصولات پرفروش و محصولات کم فروش را بدست بیاوریم.
#### 5. Sales Performance
1. **Description:**
	1. در این منو آمار فروش وبسایت را بر اساس شماره فاکتور مشاهده میکنیم.
	2. همچنین آمارهایی از مالیات، هزینه حمل و نقل، سود و تعداد فروش از هر شماره فاکتور را مشاهده میکنیم:
		1. ![[Pasted image 20260201233309.png]]
#### 6. Product List Performance
1. **Description:**
	1. در این گزینه آمار فروش را بر اساس Category, Search Results, Related Products و موارد دیگر که میتوانیم بصورت دستی مشخص کنیم مشاهده میشود:
		1. ![[Pasted image 20260201233622.png]]
	2. برای مشاهده آمار ریز هر معیار مثلا Category کافیست بر روی آن کلیک کنیم تا به صفحه آماری آن معیار منتقل شوم:
		1. ![[Pasted image 20260201233710.png]]
2. **Category Metrics:**
	1. در تصویر زیر آمار فروش بر اساس هر دسته بندی وبسایت را مشاهده میکنیم:
		1. ![[Pasted image 20260201233817.png]]
3. **Search Result Metrics:**
	1. در این قسمت آمار فروش بر اساس جستجو هایی که در وبسایت انجام شده را مشاهده میکنیم:
		1. ![[Pasted image 20260201233903.png]]
	2. در اینجا میتوانیم عبارت پر جستجو وبسایت خود را بدست بیاوریم و بر روی آن مانور بیشتری بدهیم.
4. **Related Products Metric:**
	1. در این گزینه نیز آماری از محصولات مرتبط که به کاربر نشان دادیم و خرید از طریق این قسمت انجام شده را مشاهده میکنیم.
### !