+++
title = "2-Change HTTP Data & Bypass Parameters"
tags = ["Pentest", "Web_Pentest", "Bug_Bounty", "Burpsuite", "Pentest_Tool"]
Category = "Pentest, Web_Pentest"
draft = false
+++

-------
### Change Product Price in Stores
#### Describe the Scenario
https://akofamily.com/Main/
در فروشگاه های آنلاین قیمت محصولات بر اساس تعداد انتخاب آنها صورت میگیرد. مثلا 2 عدد عینک که قیمت هر کدام 7 هزار تومان میشود 14 هزار تومان. حال میتوانیم به جای انتخاب 2 عدد 0.01 محصول را انتخاب کنیم که میشود 700 تومان. 
فروشگاه های آنلاین اصولا اجازه اینکار را نمیدهند و اینکار را باید بوسیله Burpsuite انجام میدهیم. در واقع با تغییر داده ها باید عدد 2 را به 0.01 تغییر دهیم تا بتوانیم محصول را با قیمت بسیار پایین خریداری کنیم.
در مثال زیر میخواهیم این عینک را 0.1 آن را به مبلغ 16 هزار تومان خریداری کنیم.
![2-Change HTTP Data & Bypass Parameters-1](/images/tools/2-ChangeHTTPData&BypassParameters-1.png)

#### Change Product Count (Bypass Parameter Check)
1. در صفحه انتخاب محصول یک عدد عینک انتخاب میکنیم و درخواست را توسط Burp کپچر میکنیم.
![2-Change HTTP Data & Bypass Parameters-2](/images/tools/2-ChangeHTTPData&BypassParameters-2.png)
2.  در پایین درخواست میتوانیم مشاهده کنیم که پارامتری بنام count ارسال شده است که تعداد 1 دارد میتوانیم این پارامتر را تغییر دهیم.
![2-Change HTTP Data & Bypass Parameters-3](/images/tools/2-ChangeHTTPData&BypassParameters-3.png)
###### ==روش اول==
3. عدد 1 را به 0.1 تبدیل میکنیم حتی میتوانیم بصورت دستی قیمت را کمتر کنیم و سپس درخواست را Forward میکنیم و سپس Intercept را Off میکنیم.
![2-Change HTTP Data & Bypass Parameters-4](/images/tools/2-ChangeHTTPData&BypassParameters-4.png)
4. میتوانیم در سبد خرید مشاهده کنیم که تعداد محصولات به 0.1 و مبلغ 16000 تغییر کرده است.
![2-Change HTTP Data & Bypass Parameters-5](/images/tools/2-ChangeHTTPData&BypassParameters-5.png)
###### ==روش دوم==
1. در روش دوم میتوانیم پارامتر count را حذف کنیم و یک پارامتر count جدید اضافه کنیم. اینکار را برای دور زدن if در برنامه (Bypass Security Check) انجام میدهیم. اینکار را میتوانیم با نوشتن در پنجره Intercept بصورت دستی انجام دهیم و یا در Inspector در بخش Body Parameters پارامتر `count` را اضافه کنیم. همین کار را برای پارامتر Price یا Percentage نیز میتوانیم انجام دهیم.
دقت کنید که ترتیب پارامتر ها، و اسم پارامتر ها را رعایت کنید و نامشان دقیق باشد.
###### ==روش سوم==
1. استفاده از 2 متغیر price یا count نیز باعث میشود پارامتر دومی در وبسایت اعمال شود.
![2-Change HTTP Data & Bypass Parameters-6](/images/tools/2-ChangeHTTPData&BypassParameters-6.png)
