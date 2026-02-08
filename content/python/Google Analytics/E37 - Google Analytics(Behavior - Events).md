---
Episode: E37
Date: 2026-01-31
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
Pervious Episode: "[[E36 - Google Analytics(Behavior - Site Search)]]"
Next Episode: "[[E38 - Google Analytics(Behavior - Published)]]"
---
-------
## TOC
- [Google Analytics => Behavior => Event Tab](#Google%20Analytics%20=%3E%20Behavior%20=%3E%20Event%20Tab)
	- [What is Events?](#What%20is%20Events?)
		- [Event Description](#Event%20Description)
		- [Event Usages in Online Shops](#Event%20Usages%20in%20Online%20Shops)
	- [Event Tracking](#Event%20Tracking)
	- [Dynamic Event Tracking Script](#Dynamic%20Event%20Tracking%20Script)
		- [Script](#Script)
		- [Script Description](#Script%20Description)
	- [Outbound Link Tracking](#Outbound%20Link%20Tracking)
	- [Non Interactive Events](#Non%20Interactive%20Events)
- [Google Analytics => Behavior => Events](#Google%20Analytics%20=%3E%20Behavior%20=%3E%20Events)
-------------------
### Google Analytics => Behavior => Event Tab
#### What is Events?
##### Event Description
با استفاده از قابلیت Events ها در Google Analytics میتوانیم عملیات هایی که کاربر در وبسایت ما انجام داده است را مشاهده کنیم. مثلا:
1. ویدئو درون صفحه محصول X چندبار توسط کاربر مشاهده شده است(چند بار روی Play کلیک شده است)؟
2. رزومه کاری من در وبسایت چند بار توسط کاربران دیده شده اند؟
3. چند نفر در مقاله X را در صفحات اجتماعی به اشتراک گذاشته اند؟
4. چند نفر از فیلتر های وبسایت ما استفاده کرده اند؟
- **نکته:** در واقع با استفاده از Events ها میتوانیم تعداد دفعاتی که بر روی یک لینک یا دکمه کلیک شده است را مشاهده کنیم. میتوان گفت Events کلیک شمار میباشد.
- [Read Help](https://developers.google.com/analytics/devguides/collection/analyticsjs/events) *of Google Analytics Events:*
	- https://developers.google.com/analytics/devguides/collection/analyticsjs/events
##### Event Usages in Online Shops
در فروشگاه های اینترنتی استفاده از Events ها بسیار پر کاربرد است. از کارایی های آن عبارتند از:
1. چند نفر محصولات را به سبد خرید اضافه کردند.
2. چند نفر سبد خرید خود را لغو کردند.
3. چند نفر خرید خود را نهایی کردند.
4. چه محصولی بیشترین لغو را داشته است.
5. چه محصولی بهترین محصول فروشگاه بوده است.
#### Event Tracking
- برای فعالسازی Events ها و رهگیری Events ها نیاز داریم که این قابلیت را در وبسایت خودمان فعال کنیم که برای اینکار باید از اسکریپت Event Tracking را به وبسایت خود اضافه کنیم:
	- ![Pasted image 20260131144829.png](/images/python/Pasted image 20260131144829.png)
- **نکته:** اسکریپت Event Tracking باید زیر اسکریپت اصلی `gtag.js` قرار بگیرد:
	- ![Pasted image 20260131144955.png](/images/python/Pasted image 20260131144955.png)
- همچنین برای اضافه کردن این اسکریپت میتوانیم از فانکشن کلی و سپس فراخوانی آن استفاده کنیم.
- **Event Tracking Script:**
```js
function handleOutboundLinkClicks(event) {
	ga('send', 'event', {
	eventCategory: 'Outbound Link',
	eventAction: 'click',
	eventLabel: event.target.href
});
```
#### Dynamic Event Tracking Script
##### Script
روش بهینه استفاده از اسکریپت Event Tracking داینامیک کردن آن اسکریپت، و سپس فراخوانی آن در `onclick` هر پارامتری است که میخواهیم برای Google Analytics ارسال شود.
1. Dynamic Event Tracking Script
```js
function handleOutboundLinkClicks(event, eventCategory, eventAction) {
	ga('send', 'event', {
	eventCategory: eventCategory,
	eventAction: eventAction',
	eventLabel: event.target.href
});
```
2. **Now we can call it from any element in HTML Code:**
```html
<a 
	href="https://link.url" 
	onclick="handleOutboundLinkClicks(this, 'Video', 'Play')"</a>
```
##### Script Description
1. **Event Field's Description:**
	1. `eventCategory` - text - required
		1. نوع شی که با کاربر با آن تعامل کرده است را مشاهده میکنیم.
		2. مقداری که در این قسمت استفاده میکنیم در قسمت Event Categories مشاهده میشود:
			1. ![Pasted image 20260131150110.png](/images/python/Pasted image 20260131150110.png)
	2. `eventAction` - text - required
		1. نوع تعامل Interaction کاربر را مشخص میکند.
	3. `eventLabel` - text - optional
		1. برای دسته بندی Events ها استفاده میشود.
	4. `eventValue` - integer - optional
		1. نمره عددی است که ارزش Event را مشخص میکند.
	5. ***All Values supported in Google Analytics:***
		1. `send, event, Videos, play, Fall Campaign`
			1. ![Pasted image 20260131145535.png](/images/python/Pasted image 20260131145535.png)
	6. *Image:*
		1. ![Pasted image 20260131150724.png](/images/python/Pasted image 20260131150724.png)
2. **Other Notes:**
	1. `eventLabel = event.target.href`
		1. ارسال آدرس URL المان به عنوان مقدار `eventLabel`
	2. `this` in `handleOutboundLinkClicks(this, 'Video', 'Play')`
	3. به معنای خود المان است که در مثال بالا `<a>` است.
#### Outbound Link Tracking
اگر که بخواهیم Event را که وظیفه انتقال کاربر از یک صفحه به صفحه دیگری در وبسایت مان را بر عهده دارد رهگیری کنیم باید در `eventCategory` نوع را برابر `Outbound Link` قرار دهیم. در غیر این صورت رهگیری Event انجام نمیشود:
	![Pasted image 20260131151635.png](/images/python/Pasted image 20260131151635.png)
	![Pasted image 20260131152118.png](/images/python/Pasted image 20260131152118.png)
```js
function handleOutboundLinkClicks(event) {
	ga('send', 'event', {
	eventCategory: 'Outbound Link',
	eventAction: 'click',
	eventLabel: event.target.href
});
```
- **نکته:** برخی از مرورگر ها و افزونه های آن از اجرای Javascript در مرورگر جلوگیری میکند که باعث میشود Event Tracking انجام نشود. در این صورت برای اینکه رهگیری انجام شود باید خط زیر را به اسکریپت اضافه کنیم:
	- `transport: 'beacon'`
```js
function handleOutboundLinkClicks(event) {
	ga('send', 'event', {
	eventCategory: 'Outbound Link',
	eventAction: 'click',
	eventLabel: event.target.href
	transport: 'beacon'
});
```
#### Non Interactive Events
گاهی اوقات هم نیاز داریم که Event هایی را برای Google Analytics ارسال کنیم که Events های بدون تعامل یا Non Interactive نام دارند. برای ارسال این Events ها باید از تکه اسکریپت زیر استفاده کنیم:
	![Pasted image 20260131152048.png](/images/python/Pasted image 20260131152048.png)
```js
ga('send', 'event', 'Videos', 'play', 'Fall Campaign', {
	nonInteraction: true
}):
```
### Google Analytics => Behavior => Events
1. **Overview:**
	1. در این تب هم آمار های کلی از Events ها را مشاهده میکنیم:
		![Pasted image 20260131151825.png](/images/python/Pasted image 20260131151825.png)
2. **Top Events:**
	1. رویداد های برتر را نشان ما میدهد:
		1. ![Pasted image 20260131152409.png](/images/python/Pasted image 20260131152409.png)
3. **Pages:**
	1. در این منو رویداد ها بر اساس صفحات نمایش داده میشود:
		1. ![Pasted image 20260131152703.png](/images/python/Pasted image 20260131152703.png)
4. **Events Flow:**
	1. در این منو هم نمودار Flow رویداد ها را مشاهده میکنیم:
		1. ![Pasted image 20260131152741.png](/images/python/Pasted image 20260131152741.png)
### !