---
Episode: E43
Date: 2026-02-01
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 08:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E42 - Google Analytics(Conversion - Ecommerce)]]"
Next Episode: "[[E44, E45 - Google Analytics(Conversion - Multi-Channel Funnels & Attribution)]]"
---
-------
## TOC
- [Marketing Description](#Marketing%20Description)
	- [Description](#Description)
	- [Create Promotion Link](#Create%20Promotion%20Link)
		- [Promotion Link](#Promotion%20Link)
		- [Parameters Description](#Parameters%20Description)
	- [Usage Suggestion](#Usage%20Suggestion)
- [Google Analytics => Conversion => Ecommerce => Marketing](#Google%20Analytics%20=%3E%20Conversion%20=%3E%20Ecommerce%20=%3E%20Marketing)
	- [1. Internal Promotion](#1.%20Internal%20Promotion)
	- [2. Order Coupons](#2.%20Order%20Coupons)
	- [3. Product Coupons](#3.%20Product%20Coupons)
	- [4. Affiliate Code](#4.%20Affiliate%20Code)
----------
### Marketing Description
#### Description
گاهی اوقات در وبسایت خود تبلیغاتی را قرار میدهیم که محصول یا نوشته از وبسایت خود را تبلیغ میکنیم. به این تبلیغات از وبسایت خود Promotion گفته میشود.(Internal Marketing)
- مثلا در وبسایت برنامه نویسان تبلیغاتی از دوره های تاپ لرن قرار دارد که همان Promotion ها هستند:
	![[Pasted image 20260201235754.png]]
- نکته اینجاست که برای تبدیل یک تبلیغ معمولی به Promotion باید از لینک خاص Promotion استفاده کنیم که توانایی رهگیری توسط Google Analytics را داشته باشد.
#### Create Promotion Link
##### Promotion Link
1. **Syntax of Promotion Link:**
	- https://example.com/product?promotion_name=NAME&promotion_id=ID&promotion_creative=VERSION&promotion_position=POSITION
```txt
https://example.com/product?promotion_name=NAME&promotion_id=ID&promotion_creative=VERSION&promotion_position=POSITION
```
2. **Example of Promotion Link:**
```txt
https://vapeclub3.com/oxva-xlim-sq-pro2?promotion_name=oxva-xlim&promotion_id=123&promotion_creative=v1&promotion_position=sidebar
```
##### Parameters Description
1. `promotion_name`
	1. نام Promotion که بهتر است با نام محصول یکی باشد.
2. `promotion_id`
	1. آیدی Promotion که بهتر است با آیدی محصول یا Slug ID در وردپرس برابر باشد.
3. `promotion_creative`
	1. ورژن Promotion که میتواند انتخابی باشد و برای هر Position تغییر کند.
4. `promotion_position`
	1. مکانی که Promotion در آن قرار دارد که میتواند Footer, Sidebar, Related Product, Header, Banner , ... باشد.
	2. در واقع انتخابی است و Syntax واجب ندارد.
#### Usage Suggestion
پیشنهاد میشود که از Internal Promotion برای موارد زیر استفاده کنیم تا آماری دقیق از وبسایت داشته باشیم:
1. Products in Related Products
2. Products in Banners(Header or Hero Section)
3. *Products in Special Sale Section:*
	1. محصولاتی که در محصولات ویژه گذاشته ایم.
4. *Products in Other Websites:*
	1. محصولاتی که برای تبلیغ به وبسایت های دیگر داده ایم.
5. *Products in Landing Pages(with Discounts Coupons):*
	1. محصولاتی را که در Landing page ها معرفی کردیم و یا کد تخفیفی به آنها داده ایم.
### Google Analytics => Conversion => Ecommerce => Marketing
#### 1. Internal Promotion
1. **Description:**
	1. در این منو آماری کلی از تمامی Promotion هایی که در وبسایت خود استفاده کرده ایم مشاهده میشود:
		1. ![[Pasted image 20260202001136.png]]
2. **Metrics:**
	1. آمار هایی که در این منو مشاهده میشوند عبارتند از:
	2. *Internal Promotion Views:*
		1. تعداد بازدید ها از Promotion
	3. *Internal Promotion Clicks:*
		1. تعداد کلیک ها بر روی Promotion
	4. *Internal Promotion CTR:*
		1. نرخ CTR هر Promotion
	5. *Transaction:*
		1. تعداد خرید که از Promotion انجام شده است.
	6. *Revenue:*
		1. مقدار سود حاصل از یک Promotion
	7. *Image:*
		1. ![[Pasted image 20260202001629.png]]
3. **Notes:**
	1. اگر آمار بازدید یک Promotion بالا بود اما آمار کلیک بر روی آن پایین بود، بدین معناست که مکان Promotion خوب نیست.
	2. اگر آمار کلیک و بازدید یک Promotion بالا بود به معنای خوب بودن مکان Promotion است.
	3. در واقع هر چه CTR یک Promotion بالا باشد به معنای بهتر بودن آن Promotion است.
#### 2. Order Coupons 
1. **Description:**
	1. در این منو آمار بازدید، کلیک و فروش محصولات با کد تخفیف بر روی فاکتور را مشخص میکنیم:
		1. ![[Pasted image 20260202002045.png]]
	2. در واقع در Promotion Link که میسازیم میتوانیم یک Order Coupon هم تعریف کنیم که مثلا برای هر فاکتور بصورت کلی 15 درصد تخفیف در نظر بگیریم.
	3. اگر این Order Coupon را تعریف کنیم در این منو میتوانیم آمار آنها را مشاهده کنیم.
2. **Usage:**
	1. مثلا تبلیغی را در وبسایت خاصی انجام داده ایم و گفتیم اگر از اینجا وارد وبسایت ما شوید و خرید کنید به فاکتور شما 15 درصد تخفیف تعلق میگیرد.
	2. در اینجا میتوانیم از Order Coupons ها استفاده کنیم و لینکی که در آن وبسایت استفاده میکنیم را با تعریف Order Coupons انجام دهیم.
#### 3. Product Coupons
1. **Description:**
	1. در این منو آمار بازدید، کلیک و فروش محصولات با کد تخفیف بر روی هر محصول را مشخص میکنیم:
		1. ![[Pasted image 20260202002153.png]]
	2. در واقع در Promotion Link که میسازیم میتوانیم یک Product Coupon هم تعریف کنیم که مثلا برای یک محصول 10 درصد تخفیف در نظر بگیریم.
	3. اگر این Order Coupon را تعریف کنیم در این منو میتوانیم آمار آنها را مشاهده کنیم.
2. **Usage:**
	1. مثلا تبلیغی را در وبسایت خاصی انجام داده ایم و گفتیم اگر از اینجا وارد وبسایت ما شوید و خرید کنید به محصول خریداری شده 20 درصد تخفیف تعلق میگیرد.
	2. در اینجا میتوانیم از Product Coupons ها استفاده کنیم و لینکی که در آن وبسایت استفاده میکنیم را با تعریف Product Coupons انجام دهیم.
#### 4. Affiliate Code
1. **Description:**
	1. اگر وبسایت ما بازاریاب دارد و در واقع بازاریاب ها تبلیغات ما را انجام میدهند و ورودی از طریق آنها انجام شده باشد در اینجا میتوانیم آمار بازدید، کلیک و فروش هر یک را مشاهده کنیم.
	2. برای تعریف Affiliate Code کد هم در زمان ساخت Promotion Link باید کد بازاریاب را تعریف کنیم.
2. **Usage:**
	1. مثلا میخواهیم بصورت درصدی با یکسری از وبسایت ها کار کنیم و میگویم اگر که فروش محصول از طریق ورودی وبسایت شما داشتیم از هر خرید 10 درصد به شما تعلق میگیرد.
	2. در واقع میگویم هر کسی مثلا دوره سئو ما را بفروشد 20 درصد از آن را به او میدهیم.
	3. در اینجا میتوانیم برای هر وبسایت(بازاریاب) یک کد در نظر بگیریم و در زمان تبلیغ با ساختن Promotion Link با Affiliate Code مقدار ورودی، کلیک و فروش هر بازاریاب را بدست بیاوریم.
### !
