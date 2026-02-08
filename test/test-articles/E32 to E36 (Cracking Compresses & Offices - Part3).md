---
Episode: E32 to E36
Date: 2024-07-05
Is Finished?: true
Practice Primary: true
Practice Secondary: 
Time: 08:00
tags:
  - CyberSecurity
  - hacking
Category: Cyber Security
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[E28 to E31 (Cracking Offices & PDF Files - Part2)]]"
Next Episode: "[[E37 to E41 - (Wifi Hacking - Part 1)]]"
---
-------
#CyberSecurity #hacking 
## E32 to E36 (Cracking Compressed & Offices - Part3)
- [Cracking ZIP and RAR Passwords with `john` & `hashcat` - E32](#Cracking%20ZIP%20and%20RAR%20Passwords%20with%20%60john%60%20&%20%60hashcat%60%20-%20E32)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Cracking Concepts & Tools](#Cracking%20Concepts%20&%20Tools)
		- [Cracking ZIP Files Passwords Instructions](#Cracking%20ZIP%20Files%20Passwords%20Instructions)
		- [Cracking RAR Files Passwords Instructions](#Cracking%20RAR%20Files%20Passwords%20Instructions)
	- [Practical Demo](#Practical%20Demo)
		- [Cracking ZIP Files Passwords Demonstration](#Cracking%20ZIP%20Files%20Passwords%20Demonstration)
		- [Cracking RAR Files Passwords Demonstration](#Cracking%20RAR%20Files%20Passwords%20Demonstration)
- [RAR Password Cracking with `cRARk` - E33](#RAR%20Password%20Cracking%20with%20%60cRARk%60%20-%20E33)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Definition](#Definition)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [Free Online Password Recovery Tool https://lostmypass.com/ - E34](#Free%20Online%20Password%20Recovery%20Tool%20https://lostmypass.com/%20-%20E34)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Definitions](#Definitions)
		- [Brute Force Calculator](#Brute%20Force%20Calculator)
		- [Cracking Power Point Password](#Cracking%20Power%20Point%20Password)
	- [Practical Demo](#Practical%20Demo)
- [Excel Password Cracking with `Passfab` *Best* - E35](#Excel%20Password%20Cracking%20with%20%60Passfab%60%20*Best*%20-%20E35)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is Passfab?](#What%20is%20Passfab?)
		- [Cracking Excel Passwords](#Cracking%20Excel%20Passwords)
		- [Remove Excel Sheet Protection](#Remove%20Excel%20Sheet%20Protection)
	- [Practical Demo](#Practical%20Demo)
		- [Cracking Excel Passwords](#Cracking%20Excel%20Passwords)
		- [Remove Excel Sheet Protection](#Remove%20Excel%20Sheet%20Protection)
- [Remove Password from Old Word Documents with `Guaword` - E36](#Remove%20Password%20from%20Old%20Word%20Documents%20with%20%60Guaword%60%20-%20E36)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is Guaword?](#What%20is%20Guaword?)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
------
### Cracking ZIP and RAR Passwords with `john` & `hashcat` - E32
#### Definition & Instruction
##### Cracking Concepts & Tools
1. `zip2john` | `rar2john` => *Get the ZIP | RAR file Hashes*
	1. در این مدل حمله ابتدا باید مقدار hash فایل فشرده را بدست بیاوریم.
	2. اینکار را بوسیله ابزار `zip2john` برای فایل های ZIP و بوسیله `rar2john` برای فایل های RAR انجام میدهیم.
2. `john` | `hashcat` => *Cracking extracted hash file*
	1. در مرحله بعدی باید فایل hash بدست آمده را بوسیله ابزار هایی مانند `john` یا `hashcat` کرک کنیم.
```sh
#Get the ZIP file Hashes
zip2john crackme.zip > hash.txt

#Cracking extracted hash file with John or hashcat
john --w hash.txt
hashcat -a 0 -m 13000 --status -o cracked.txt hash.txt ./rockyou.txt
```
##### Cracking ZIP Files Passwords Instructions 
0. Pre-Requires
	1. آماده سازی فایل ZIP با پسورد بنام `crackme.zip`
	1. *Kali* `Right-Click on Files => Create Archive => Set Password "1234" `
		1. ![[Pasted image 20240703173311.png]]
1. Get hash of `crackme.zip` with `zip2john`
	1. ترمینال را در Kali باز میکنیم و با استفاده از کامند زیر Hash فایل `crackme.zip` را بدست میاوریم.
	2. `zip2john crackme.zip > hash.txt`
		1. ![[Pasted image 20240703173912.png]]
	3. `Crackme.zip` target file want to be cracking password
	4. `hash.txt` the output file contains `crackme.zip` hashes
	5. *Slide*
		2. ![[Pasted image 20240703173831.png]]
2. Cracking Extracted hash file `hash.txt` with `john` or `hashcat`
	1. حال میتوانیم بوسیله حمله Dictionary Attack با استفاده از ابزار `john` یا `hashcat`  به کرک فایل `hash.txt` بپردازیم تا بتوانیم متن پسورد را از مقدار هش بدست بیاوریم.
	2. `john --w hash.txt` Cracking with John Built-In Dictionary Attack
		1. ![[Pasted image 20240703174645.png]]
	3. *Slide*
		1. ![[Pasted image 20240703174601.png]]
3. Cracking Successfully Done.
	1. `john --show hash.txt` See Cracking Result 
##### Cracking RAR Files Passwords Instructions 
0. Pre-Requires
	1. آماده سازی فایل RAR با پسورد بنام `crackme.rar` 
		1. *Windows* `Right-Click on Files => Add to Archive => Set Password "1234" `
			1. ![[Pasted image 20240703174941.png]]
	2. انتقال `crackme.rar` به پوشه `john\run\`
		1. ![[Pasted image 20240703175106.png]]
1. Get hash of `crackme.rar` with `rar2john`
	1. `rar2john crackme.rar > hash.txt`
		1. ![[Pasted image 20240703175451.png]]
	2. `Crackme.rar` target file want to be cracking password
	3. `hash.txt` the output file contains `crackme.rar` hashes
	4. *Slide*:
		1. ![[Pasted image 20240703175436.png]]
2. *Using John* Now Cracking `hash.txt` to get `Crackme.rar` Password 
	1. `john --w=rockyou.txt hash.txt`
		1. ![[Pasted image 20240703175643.png]]
	2. `-w=rockyou.txt` Dictionary Attack using Rockyou Wordlist
	3. Cracking Result in Terminal. *Password Cracked and is "123456"*
		1. ![[Pasted image 20240703175656.png]]
3. *Using Hashcat* Now Cracking `hash.txt` to get `Crackme.rar` Password 
	1. Copy `hash.txt` to `hashcat` folder
		1. ![[Pasted image 20240703180007.png]]
	2. Open `hash.txt` and remove `file name` from `file content`
		1. ![[Pasted image 20240703180057.png]]
	3. Now Open `Powershell` in Hashcat folder and run following commands =>
		1. `./hashcat -a 0 -m 13000 --status -o cracked.txt hash.txt rockyou.txt`
			1. ![[Pasted image 20240703180250.png]]
		2. `-a 0` Attack Mode is Dictionary Attack
		3. `-m 13000` Hash Mode is rar5, See all Hash Modes in `hashcat Wiki`
			1. ![[Pasted image 20240703181913.png]]
		4. `-o Cracked.txt` Result of Cracking save in this file
		5. *Slide*:
			1. ![[Pasted image 20240703180441.png]]
	4. Hashcat Powerfully & Successfully Cracked `hash.txt`
5. See Cracking Result in `Cracked.txt`
#### Practical Demo
##### Cracking ZIP Files Passwords Demonstration
0. پیش نیاز ها
	1. آماده سازی فایل ZIP با پسورد بنام `crackme.zip`
		1. ![[Pasted image 20240703180806.png]]
1. باز کردن ترمینال در محل فایل ZIP و بدست آوردن مقدار هش پسورد فایل ZIP و ریختن خروجی در `hash.txt`
	1. `zip2john crackme.zip > hash.txt`
		1. ![[Pasted image 20240703180949.png]]
	2. `nano hash.txt`
		1. ![[Pasted image 20240703181013.png]]
2. کرک پسورد فایل ZIP
	1. `john --w hash.txt`
		1. ![[Pasted image 20240703181107.png]]
3. پسورد فایل ZIP با موفقیت کرک شد.
----
```powershell
.\zip2john.exe .\hackme22.zip > hashzip2.txt
.\john -w=".\rockyou.txt" .\hashzip2.txt

```
	![[Pasted image 20240705000151.png]]
-----
```sh
john -w="/usr/share/wordlists/rockyou.txt" hashzip2.txt

```
##### Cracking RAR Files Passwords Demonstration
0. پیش نیاز ها
	1. آماده سازی فایل RAR بنام `Crackme.rar` 
		1. ![[Pasted image 20240703181231.png]]
	2. انتقال `Crackme.rar` به پوشه `John\run`
		1. ![[Pasted image 20240703181327.png]]
1. باز کردن CMD در محل فایل RAR و بدست آوردن مقدار هش پسورد فایل RAR و ریختن خروجی در `hash.txt`
	1. `rar2john crackme.zip > hash.txt`
		1. ![[Pasted image 20240703181452.png]]
2. کرک فایل `hash.txt` بوسیله `john`
	1. `john --w hash.txt`
		1. ![[Pasted image 20240703181629.png]]
3. کرک فایل `hash.txt` بوسیله `hashcat`
	1. فایل  `hash.txt` را به پوشه `hashcat` منتقل میکنیم.
	2. فایل `hash.txt` را در ادیتور متنی باز میکنیم و *نام فایل* را از *محتویات فایل* پاک میکنم.
		1. ![[Pasted image 20240703181723.png]]
	3. سپس `Powershell` را در پوشه `hashcat` باز میکنیم  و کامند زیر را برای کرک فایل وارد میکنیم.
	4. `./hashcat -a 0 -m 13000 --status -o cracked.txt ./hash.txt ./rockyou.txt`
		1. ![[Pasted image 20240703182116.png]]
		2. ![[Pasted image 20240703182213.png]]
4. *کرک فایل RAR با موفقیت انجام شد*
	1. نتیجه کرک و پسورد فایل RAR را در ترمینال Powershell با اجرای کامند زیر میتوانیم مشاهده کنیم.
		1. `./hashcat.exe --show -m 13000 hash.txt`
			1. ![[Pasted image 20240703182213.png]]
	2. همچنین در فایل `cracked.txt` هم در پوشه `Hashcat` قابل مشاهده است.
		1. ![[Pasted image 20240703182253.png]]
```powershell
.\rar2john.exe .\hackme2.rar > hashrar2.txt
.\john -w=".\rockyou.txt" .\hashrar2.txt

.\hashcat.exe -a 0 -m 13000 --status -o crackedRAR2.txt .\hashrar2.txt .\rockyou.txt
```
	![[Pasted image 20240705000148.png]]
----
```sh
hashcat -a 0 -m 13000 --status -o CrackedRAR.txt hashr2.txt /usr/share/wordlists/rockyou.txt
john --w hashr2.txt
```
### RAR Password Cracking with `cRARk` - E33
#### Definition & Instruction
##### Definition
ابزار `cRARk` ابزاری رایگان برای کرک(ریکاوری 🤣 ) فایل های RAR است. این ابزار با رابط کاربری CLI عرضه شده است و استفاده از آن بسیار آسان میباشد.
اگر طول پسورد فایل RAR کمتر از شش 6 کاراکتر باشد، ابزار  `cRARk` با ضریب 98% میتواند پسورد فایل را کرک کند.
	![[Pasted image 20240703185222.png]]
ابزار `cRARk` را از وبسایت رسمی ابزار میتوانیم دانلود کنیم:
- https://www.crark.net/#download
	- ![[Pasted image 20240703185342.png]]
##### Instruction Steps
0. پیش نیاز ها 
	1. دانلود `cRARk` از https://www.crark.net/#download و استخراج آن
	2. ساخت یک فایل RAR با پسورد و انتقال آن به پوشه `cRARk`
		1. ![[Pasted image 20240703185514.png]]
1. ویرایش و ساخت فایل `password.def`
	1. فایلی بنام `crackme.def` در پوشه `crark55` وجود دارد که در این فایل پسورد هایی که میخواهیم در فایل RAR امتحان شوند را وارد میکنیم.
		1. ![[Pasted image 20240703195609.png]]
	2. در این فایل نوع و ترتیب کاراکتر ها را برای پیاده سازی حمله وارد میکنیم. تعریف نوع پسورد در ابزار `cRARk` قوانین و Syntax خاص خود را دارد که در تصویر زیر میتوان نمونه ای از آنها را مشاهده کرد.
		1. ![[Pasted image 20240703185746.png]]
	3. در سناریو ما که میدانیم پسورد ما از فقط کاراکتر های اعداد تشکیل شده است باید مقادیر زیر را در فایل `crackme.def` وارد کنیم:
		1. ![[Pasted image 20240703195919.png]]
	4. حال کافیست فایل را با نام `password.def` در پوشه `crark55` ذخیره میکنیم.
		1. ![[Pasted image 20240703200144.png]]
	5. *برای مشاهده تمام قواعد به لینک زیر بروید*: `cRARk Syntax` 
		1. https://www.crark.net/cRARk.html
2. باز کردن CMD در پوشه `cRARk` و اجرای کامند زیر
	1. `crack.exe crack.rar`
		1. ![[Pasted image 20240703190003.png]]
	2. با اجرای کامند پسورد فایل کرک میشود و نمایش داده میشود:
		1. ![[Pasted image 20240703190048.png]]
#### Practical Demo
0. Pre-Requires
	1. Download `cRARk` based on your OS
		1. ![[Pasted image 20240703190202.png]]
	2. Open `crark55.rar` and then Select all files except `crackme*` and Extract it. Actually `crackme*` is paid module and need password to open.
		1. ![[Pasted image 20240703190336.png]]
	3. Create Password Protected RAR file in name `crack.rar` and Copy this to `cRARk` folder
		1. ![[Pasted image 20240703190507.png]]
1. Edit `crackme.def` and Save it in name `password.def`
	1. Open `crark55` Folder and Open `crackme.def`  with a text Editor
	2. Enter Suitable syntax for Brute Forcing Attack with Numbers and Save file in named `password.def` in `crark55` folder
		1. if Password characters only *numbers* =>
			1. ![[Pasted image 20240703200409.png]]
		2. if Password characters only *Lower Case*  =>
			1. ![[Pasted image 20240705225207.png]]
		3. if Password characters only *Upper Case*  =>
			1. ![[Pasted image 20240705225229.png]]
2. Open `CMD` in `crark55` folder and Run following command to cracking `crackme.rar`
	0. `crark.exe crackme.zip`
		1. با اجرای کامند حمله Bruteforce برای کرک پسورد فایل RAR صورت میگرد، قدرت این ابزار این است که میتواند بصورت خوکار کارت گرافیک ماشین GPU را شناسایی کند و حمله را با استفاده از قدرت کارت گرافیک GPU انجام دهد.
	2. See `Crackme.rar` Password in terminal
		1. ![[Pasted image 20240703200949.png]]

```powershell
crark.exe crackme.zip
```
	![[Pasted image 20240703200911.png]]
	![[Pasted image 20240703200921.png]]
### Free Online Password Recovery Tool https://lostmypass.com/ - E34
#### Definition & Instruction
##### Definitions
سرویس های آنلاین زیادی وجود دارند که با استفاده از آنها میتوانییم به کرک پسورد ها بپردازیم. یکی از معروف ترین آنها https://www.lostmypass.com است که میتواند خدمات با کیفیت مناسبی را برای کرک پسورد ها ارائه کند.
- https://www.lostmypass.com 
	- این سرویس آنلاین با پردازنده های قدرتمند خود میتواند انواع فایل ها را در حمله `Brute Force Attack with Mask` که میتوان گفت از بهترین حملات است، تا 99 درصد شانس کرک پسورد را دارد.
- ویژگی های استفاده از از Cloud Services برای Password Recovery به شرح زیر است >>
1. برای پسورد های ضعیف رایگان است.
2. برای پسورد های پیچیده، تنها در صورتیکه رمز کرک شود نیازمند پرداخت هزینه است.
3. از این سرویس برای کرک فایل های Word, Power Point, Excel, RAR, ZIP , .... میتوان استفاده کرد.
	![[Pasted image 20240704200638.png]]
- *این ابزار یکی از بهترین و ساده ترین روش ها برای کرک پسورد فایل های مختلف میباشد. در صورتیکه بتوان اشتراک هم تهییه کرد میتوان 99 درصدر از هر پسوردی را بوسیله این وبسایت کرک کرد*.
	- ![[Pasted image 20240705231424.png]]
##### Brute Force Calculator
این سرویس قسمتی بنام `Brute Force Calculator` دارد که میتواند تعداد کاراکتر ها و GH/z مصرفی برای حملات Brute Force را با انواع Charset متفاوت حساب کند.
- https://www.lostmypass.com/tools/bruteforce-calculator/
	![[Pasted image 20240705231916.png]]

##### Cracking Power Point Password
0. Pre-Pare Password Protected Power Point file
	1. ![[Pasted image 20240704201205.png]]
1. Open  https://www.lostmypass.com  and Upload Power Point file
	1. ![[Pasted image 20240704201255.png]]
2. Now Service cracking(Recovery) password
	1. ![[Pasted image 20240704201417.png]]
3. Cracking Successfully done
	1. ![[Pasted image 20240704201443.png]]
4. If Password Strong and Not Cracking =>
	1. سرویس سوالی میپرسد و میگوید که میخواهید به کرک ادامه دهید؟ برای کرک پسورد های Strong نیازمند سرور هستیم که در نتیجه برای استفاده باید هزینه اشتراک حدود 50 دلار بپردازیم. 
		1. ![[Pasted image 20240704201819.png]]
#### Practical Demo
0. آماده سازی فایل Power Point آسیب پذیر
	1. ![[Pasted image 20240704202213.png]]
1. حال به وبسایت  https://www.lostmypass.com  میرویم:
	1. ![[Pasted image 20240704202426.png]]
2. *در وبسایت مشاهده میکنیم که شانس یافتن انواع پسورد ها به چگونه است*:
	1. حمله *Weak Password* که *رایگان* میتوانیم انجام دهیم *22* درصد شانس یافتن پسورد ها را دارد. 
	2. اما حمله *Brute force with mask* که پلن *اشتراکی* وبسایت است، شانس *100* درصدی در کرک و یافتن پسورد  *Password Strong* را دارد. 
	3. در پلن *رایگان* هم، شانس کرک و یافتن پسورد های *Password Strong* مقدار *60%* درصد است.
	4. *تصویر*:
		1. ![[Pasted image 20240705232407.png]]
3. در واقع میتوان گفت با این سرویس و سرور های قدرتمند آن، میتوان پسورد هر فایل را کرک کرد. برای شروع هم بر روی `Try it Now` کلیک میکنیم.
	1. ![[Pasted image 20240704202708.png]]
4. سپس در صفحه آپلود فایل، بر روی `Upload` کلیک میکنیم و سپس فایل مورد نظر(Power Point) را آپلود میکنیم.
5. *پس از آپلود سرویس سعی میکند پسورد فایل مورد نظر را کرک کند*:
	1. این را در پیامی در صفحه نشان میدهد
		1. 
	2. پسورد ضعیف مانند مثال ما که پسورد *123* است، بسیار سریع توسط سرویس کرک میشود. این سرویس پسورد های متوسط مانند *iloveyou* ویا *qwerty* براحتی میتواند کرک میکند. و حتی در پسوردی مانند *D21ab!* را نیز تا *70%* میتواند کرک کند.
		1. ![[Pasted image 20240704203020.png]]
	3. اما اگر فایل پسورد پیچیده داشته باشد، مثلا فرض کنید پسورد فایل Power Point را برابر *D@vood12945* قرار دادیم، در اینصورت اگر فایل را برای کرک در وبسایت مربوط آپلود کنیم، ایندفعه زمان پس مدت زمانی پیامی دریافت میکنیم که میگوید پسورد پیچیده است و برای کرک باید اشتراک ماهیانه را بپردازید.
		1. ![[Pasted image 20240704203351.png]]
6. عملیات کرک پسورد با موفقیت به اتمام رسید.
### Excel Password Cracking with `Passfab` *Best* - E35
#### Definition & Instruction
##### What is Passfab?
یکی از ابزار های غیر رایگان که برای کرک انواع فایل ها استفاده میشود، `Passfab` نام دارد. بوسیله این ابزار میتوانیم فایل های زیر را کرک کنیم >>
1. Office Files `Passfab for Office`
	1. Word, Excel, Power Point Password Cracking
2. Compressed Files `Passfab for RAR`
	1. ZIP & RAR Password Cracking
3. Windows Password Recovery `Passfab for Win2Key`
4. Smart Phones Password Recovery `Passfab for Android` & `Passfab for IOS`
5. *Slide*:
	1. ![[Pasted image 20240704204201.png]]
همچنین توسط این ابزار میتوانیم حملات زیر را برای کرک فایل پیاده سازی کنیم:
- Dictionary Attack
- Brute Force with Mask
- Brute Force
گرچه این ابزار رایگان نیست و برای استفاده از آن باید هزینه اشتراک پرداخت کرد، اما میتوان نسخه کرک شده را از وبسایت های ایرانی یافت و استفاده کرد.
	![[Pasted image 20240704204308.png]]
##### Cracking Excel Passwords
0. Pre-Pare Password Protected Excel file
	1. ![[Pasted image 20240704204406.png]]
1. Download `Passfab` and Open `PassFab for Excel`
2. Chose Option `Recover Excel Open Password`
	1. ![[Pasted image 20240704204524.png]]
3. Now Click on Import and Select Target Excel file
	1. ![[Pasted image 20240704204614.png]]
4. Now Select `Dictionary Attack` and give path of *Rockyou* by click on `Add Dictionary`
	1. ![[Pasted image 20240704204713.png]]
5. Now Click `Recover` and it will Recover Password for you
	1. ![[Pasted image 20240704204755.png]]
##### Remove Excel Sheet Protection 
0. Pre-Pare `Sheet Protected Excel` File
	1. ![[Pasted image 20240704204918.png]]
1. Download `Passfab` and Open `PassFab for Excel`
2. Chose the Option `Unlock Sheets`
	1. ![[Pasted image 20240704205014.png]]
3. Now Click on Import and Select Target Excel file
	1. ![[Pasted image 20240704204614.png]]
4. Now Click on `Remove` and it will remove Sheet Protection
	1. ![[Pasted image 20240704205052.png]]
5. Now `Sheet Protection` Removed and Generate a new Instance from Excel file `Without Sheet Protection`
	1. ![[Pasted image 20240704205235.png]]
#### Practical Demo
##### Cracking Excel Passwords
1. آماده سازی فایل اکسل به همراه پسورد 
	1. ![[Pasted image 20240704205340.png]]
2. حال ابزار `PassFab` را دانلود و سپس باز میکنیم.
	1. ![[Pasted image 20240704205432.png]]
3. *هنگامیکه ابزار را باز میکنیم دو گزینه را میتوانیم انتخاب کنیم:*
	1. *گزینه اول:* `Recover Excel Open Password`
		1. از این گزینه برای کرک پسورد فعلی فایل اکسل استفاده میشود.
		2. در این حمله هم این گزینه را استفاده میکنیم.
	2. *گزینه دوم:*`Remove Excel Restriction Password`
		1. از این گزینه برای برداشتن مکانیزم های امنیتی مانند `Sheet Protection` و یا `Workbook Protection` استفاده میشود.
		2. در حمله بعدی از این گزینه استفاده میکنیم.
	3. در اینجا گزینه `Recover Excel Open Password` را انتخاب میکنیم.
4. *در صفحه بعدی باید نوع حمله را برای یافتن پسورد انتخاب کنیم:*
	1. حمله `Dictionary Attack`
	2. حمله `Brute Force with Mask Attack`
	3. حمله `Brute Force Attack`
	4. در اینجا هم میخواهیم با استفاده از حمله `Dictionary Attack` پسورد فایل را کرک کنیم.
		1. ![[Pasted image 20240704210048.png]]
5. *برای انجام تنظیمات هر حمله، بر روی چرخ دنده کناری `Settings` در کنار حمله کلیک میکنیم:*
	1. در اینجا هم پس از انتخاب حمله Dictionary بر روی این گزینه کلیک میکنیم و سپس بر روی `Add Dictionary` کلیک میکنیم و *Rockyou* را به ابزار معرفی میکنیم.
		1. ![[Pasted image 20240704210328.png]]
	2. پس از انتخاب Word List هم بر روی `OK` کلیک میکنیم:
		1. ![[Pasted image 20240704210554.png]]
6. پس از انتخاب نوع حمله، در همان صفحه بر روی `Import Excel file` کلیک میکنیم و فایل تارگت را وارد برنامه میکنیم:
	1. ![[Pasted image 20240704210157.png]]
7. حال کافیست بر روی `Recover` کلیک کنیم تا پسورد فایل مورد نظر کرک شود.
	1. ![[Pasted image 20240704210657.png]]
8. ابزار `PassFab` فایل اکسل را با موفقیت کرک میکند و پسورد فایل را نمایش میدهد:
	1. ![[Pasted image 20240704210802.png]]
##### Remove Excel Sheet Protection
0. آماده سازی فایل اکسل که با `Protect Sheets` محافظت میشود.
	1. ![[Pasted image 20240704211105.png]]
1. حال ابزار `PassFab` را دانلود و سپس باز میکنیم.
2. در صفحه ابزار، اینبار گزینه `Remove Excel Restriction Password` را برای برداشتن Sheet Protection  انتخاب میکنیم.
	1. ![[Pasted image 20240704211302.png]]
3. در صفحه بعدی بر روی `+ Import` کلیک میکنیم و فایل اکسل را وارد ابزار میکنیم.
	1. ![[Pasted image 20240704211432.png]]
4. حال کافیست بر روی `Remove` کلیک کنیم تا Protection برداشته شود.
	1. ![[Pasted image 20240704211530.png]]
5. حال *Sheet Protection* با موفقیت از فایل برداشته شده و یک نمونه جدید از فایل اکسل محافظت شده ساخته میشود که هیچ Protection ندارد. کافیست بر روی `Open Folder` کلیک کنیم تا وارد پشوه فایل کرک شده بشویم:
	1. ![[Pasted image 20240704211653.png]]
6. حال میتوانیم فایل اکسل جدید را باز کنیم و میبینیم که بدون نیاز به پسورد میتوانیم به ایجاد Sheet جدید و یا اعمال تغییرات در Sheet بپردازیم:
	1. ![[Pasted image 20240704211834.png]]
### Remove Password from Old Word Documents with `Guaword` - E36
#### Definition & Instruction
##### What is Guaword?
- گاهی اوقات ممکن است با فایل های Document روبرو شویم که بسیار قدیمی و با پسورد هم محافظت میشوند. این امر بیشتر برای Forensic کار ها رخ میدهد. در این جلسه میخواهیم به کرک فایل های Document قدیمی بپردازیم. 
- فایل های قدیمی Word پسوند `doc.` دارند و فایل های جدید Word پسوند `docx.` دارند و این ابزار هم مخصوص کرک فایل های `doc.` است.
- در واقع میخواهیم با استفاده از ابزاری بنام `Guaword` به کرک فایل های Old Microsoft Word Documents بپردازیم. این روش و ابزار فقط در ویندوز های XP تا 8 کار میکند و در ویندوز های 10 و 11 نمیتوان از آن استفاده کرد. بهترین سیستم عامل برای این ابزار Windows XP on VMو یا Windows 7 است.
	![[Pasted image 20240705152546.png]]
##### Instruction Steps
برای دانلود ویندوز XP و یا سایر نرم افزار های قدیمی میتوانیم از وبسایت https://internetarchives.org استفاده کنیم که آرشیو کامل و جامعی از تمامی نرم افزار ها در تمامی ورژن ها را نگهداری میکند.
0. *پیش نیاز ها*
	1. بالا آوردن Windows XP یا Windows 7 در VM
	2. دانلود ابزار از وبسایت رسمی
		1. http://www.password-crackers.com/crack/guaword.html
			1. ![[Pasted image 20240705153212.png]]
		2. https://download.cnet.com/guaranteed-word-decrypter/3000-2079_4-10044717.html
	3. پوشه دانلود شده را در ویندوز XP استخراج میکنیم.
		1. ![[Pasted image 20240705153341.png]]
	4. ساخت فایل Word قدیمی (`doc.`) با Password to Open 
1. *کرک فایل Word*
	1. حال `CMD` را در پوشه `Guaword` در ویندوز `XP` باز میکنیم و کامند زیر را برای کرک فایل اجرا میکنیم:
		1. ![[Pasted image 20240705153806.png]]
	2. `guaword.exe test.doc`
	3. با اجرای کامند بالا ابزار پسورد فایل را بر میدارد.
		1. ![[Pasted image 20240705154251.png]]
2. حال کافیست فایل را از ویندوز XP به ویندوز اصلی منتقل کنیم تا بتوانیم بدون نیاز به پسورد از آن استفاده کنیم. 
	1. ![[Pasted image 20240705154517.png]]
#### Practical Demo
0. *Pre-Requires*
	1. Power On Windows XP on VM
	2. Download free version of Guaword http://www.password-crackers.com/crack/guaword.html
		1. ![[Pasted image 20240705154857.png]]
	3. Extract Guaword and Copy the Guaword folder to windows XP
		1. ![[Pasted image 20240705155027.png]]
1. *Cracking `test.doc`*
	1. Open CMD and Navigate to `Desktop/guawrd09`
		1. `cd desktop\guawrd09\`
	2. Now cracking word file
		1. `guaword.exe test.doc`
		2. Guaword Asked for decrypting file? Press `Y`
			1. ![[Pasted image 20240705155440.png]]
	3. Password Removed Successfully
2. Move `test.doc` from windows XP to Windows 11 and `Replace` it with original `test.doc`
	1. ![[Pasted image 20240705155646.png]]
3. Now we can open `test.doc` without needing password

```powershell
cd desktop\guawrd09\
guaword.exe test.doc
#Guaword Asked for decrypting file? Press `Y`
```
	![[Pasted image 20240705155545.png]]
### !