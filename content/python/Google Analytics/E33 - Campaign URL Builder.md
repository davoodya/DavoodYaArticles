---
Episode: E33
Date: 2026-01-28
Is Finished?:
Practice Primary:
Practice Secondary:
Time: 07:00
tags:
  - CyberSecurity
  - Security
Category:
  - SEO
  - Web Developing
banner:
Home: "[[Handouts Board]]"
Pervious Episode: "[[E32 - Google Analytics(Acquisition Tab)]]"
Next Episode: "[[E34 - Google Analytics(Behavior - Behavior Flow & Site Content)]]"
---
-------
## TOC
- [Campaign URL Builder](#Campaign%20URL%20Builder)
	- [What is Campaign URL Builder?](#What%20is%20Campaign%20URL%20Builder?)
	- [Create URL Builder](#Create%20URL%20Builder)
	- [Manually Create URL Builder](#Manually%20Create%20URL%20Builder)
- [Acquisition => Campaigns: See Campaigns Acquisition](#Acquisition%20=%3E%20Campaigns:%20See%20Campaigns%20Acquisition)
--------------
### Campaign URL Builder
#### What is Campaign URL Builder?
با استفاده از URL Builder میتوانیم لینک های قابل رهگیری ایجاد کنیم که در مبحث تبلیغات بسیار کار آمد هستند.
- **Usage Example:**
	- فرض کنید میخواهیم یکی از محصولات وبسایت خود مثلا "آموزش CEH++" را در چندین وبسایت و همچنین چندین کانال شبکه اجتماعی تبلیغ کنیم. 
	- حال با استفاده از URL Builder و ساخت لینک رهگیری برای این دوره میتوانیم آمار دقیق از ورودی های این لینک را از هر منبع مشخص مشاهده کنیم.
#### Create URL Builder
1. goto https://ga-dev-tools.google/campaign-url-builder/
	1. ![Pasted image 20260129145816.png](/images/python/Pasted image 20260129145816.png)
2. **Enter Campaign URL Builder Information:**
	1. *Website URL:*
		1. آدرس URL که میخواهیم URL Builder را برای آن بسازیم با HTTP, HTTPS
		2. https://toplearn.com/seocourse
	2. *Campaign Source:*
		1. نام کانال یا وبسایتی که میخواهیم تبلیغ را به آنجا بدهیم:
		2. `BarnamehNevisanChannel`
	3. *Campaign Medium:*
		1. پلتفرم که محل تبلیغ در آنجا قرار دارد:
		2. `Telegram, Google, Facebook, Website, ...`
	4. *Campaign Name:*
		1. نام کمپین که هر نامی میتواند باشد:
		2. SEO Course Campaign(ADS Telegram)
	5. *Campaign Term(Optional):*
		1. تعریف کردن Keywords برای Campaign - اختیاری
	6. *Campaign Content(Optional):*
		1. تعریف کردن محتوا Content برای Campaign برای داشتن تبلیغ متفاوت - اختیاری
3. **Copy the Created URL from `Share the Generated Campaign URL`**
	1. پس از وارد کردن اطلاعات Campaign مقدار URL برای ما ساخته میشود که میتوانیم آنرا کپی و استفاده کنیم:
		1. ![Pasted image 20260129150551.png](/images/python/Pasted image 20260129150551.png)
4. **Shorter URL:**
	1. پیشنهاد میشود URL که به ما میدهد را بصورت کوتاه شده در بیاوریم تا Share کردن آن راحت تر باشد. 
	2. برای اینکار از ابزار گوگل و یا ابزار های شخصی میتوانیم استفاده کنیم:
		1. ![Pasted image 20260129150708.png](/images/python/Pasted image 20260129150708.png)
	3. با کلیک بر روی `Convert URL to Short Link` به وبسایت bit.ly برای کوتاه کردن URL منتقل میشویم.
5. **Create Another URL Builder for Another Source:**
	1. اگر که میخواهیم چندین تبلیغ را در چند کانال یا وبسایت متفاوت بگذاریم باید برای هر یک از این منبع ها یک URL Builder بسازیم تا بتوانیم مقدار دقیق ورودی های هر کدام را اندازه گیری کنیم.
	2. برای اینکار کافیست مقدار Campaign Source را به نام کانال مرتبط تغییر دهیم تا URL را داشته باشیم:
		1. ![Pasted image 20260129151047.png](/images/python/Pasted image 20260129151047.png)
#### Manually Create URL Builder
1. بصورت دستی هم میتوانیم URL های قابل رهگیری را بسازیم که برای اینکار باید از Syntax خاص URL Builder استفاده کنیم:
	1. ![Pasted image 20260129151207.png](/images/python/Pasted image 20260129151207.png)
### Acquisition => Campaigns: See Campaigns Acquisition
1. **Share the Campaign URLs:**
	1. حال برای دادن تبلیغ از پست، محصول یا دوره مورد نظرمان کافیست که Campaign URL را به منبع تبلیغاتی خود بدهیم.
	2. به محض اینکه تعدادی ورودی از Campaign URL ها دریافت شود آمار آنها در تب زیر قابل مشاهده هستند.
2. `Google Analytics => Acquisition => Campaigns => All Campaigns`
	1. در این منو میتوانیم تمامی Campaign URLs های خود را به همراه آمار دقیق ورودی های آنها مشاهده کنیم:
		1. ![Pasted image 20260129151915.png](/images/python/Pasted image 20260129151915.png)
3. `Google Analytics => Acquisition => All Traffic => Referral`
	1. همچنین در تب Referral هم Campaign URLs را به عنوان یک Source مشاهده میکنیم که میتوان آمار دقیق ورودی های آنرا مشاهده کنیم:
		1. ![Pasted image 20260129151843.png](/images/python/Pasted image 20260129151843.png)
### !
