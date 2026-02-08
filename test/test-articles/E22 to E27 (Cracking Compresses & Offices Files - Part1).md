---
Episode: E22 to E27
Date: 2024-07-01
Is Finished?: true
Practice Primary: true
Practice Secondary: 
Time: 40:00
tags:
  - CyberSecurity
  - hacking
Category: Cyber Security
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[@E16 to E21 - (Cracking Windows Password)]]"
Next Episode: "[[E28 to E31 (Cracking Offices & PDF Files - Part2)]]"
---
-------
## E22 to E28 (Cracking Compressed, Offices and PDF Files)
- [Cracking Old ZIP(ZipCrypto) Files with `Bkcrack` - E22](#Cracking%20Old%20ZIP(ZipCrypto)%20Files%20with%20%60Bkcrack%60%20-%20E22)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Old Zip File Encrypt Functionality](#Old%20Zip%20File%20Encrypt%20Functionality)
		- [Create Vulnerable Archive](#Create%20Vulnerable%20Archive)
		- [Cracking/Breaking ZIPCrypto Instruction](#Cracking/Breaking%20ZIPCrypto%20Instruction)
	- [Practical Demo](#Practical%20Demo)
- [Cracking Office Word Files with `John` on `Kali` - E23](#Cracking%20Office%20Word%20Files%20with%20%60John%60%20on%20%60Kali%60%20-%20E23)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Basic & Concetps](#Basic%20&%20Concetps)
		- [Usage Concepts](#Usage%20Concepts)
		- [Prepare a Password Protected Office File](#Prepare%20a%20Password%20Protected%20Office%20File)
		- [Instruction Steps](#Instruction%20Steps)
		- [John Additional Attacks](#John%20Additional%20Attacks)
		- [Remove Saved Password in John](#Remove%20Saved%20Password%20in%20John)
	- [Practical Demo](#Practical%20Demo)
- [Install Hashcat & John on Windows](#Install%20Hashcat%20&%20John%20on%20Windows)
	- [Install Hashcat on Windows - E24](#Install%20Hashcat%20on%20Windows%20-%20E24)
	- [Install John on Windows - E26](#Install%20John%20on%20Windows%20-%20E26)
- [Cracking Office Excel Password with `Hashcat` - E25](#Cracking%20Office%20Excel%20Password%20with%20%60Hashcat%60%20-%20E25)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Usage Concept](#Usage%20Concept)
		- [Instruction Steps](#Instruction%20Steps)
		- [Hashcat Additional](#Hashcat%20Additional)
			- [Hashcat Wiki](#Hashcat%20Wiki)
			- [Specify GPU Device for Hashcat](#Specify%20GPU%20Device%20for%20Hashcat)
	- [Practical Demo](#Practical%20Demo)
- [Cracking Office PowerPoint Files with `John` on `Windows` - E27](#Cracking%20Office%20PowerPoint%20Files%20with%20%60John%60%20on%20%60Windows%60%20-%20E27)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Definitions](#Definitions)
		- [Usage Concept](#Usage%20Concept)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)

### Cracking Old ZIP(ZipCrypto) Files with `Bkcrack` - E22
#### Definition & Instruction
##### Old Zip File Encrypt Functionality 
- در رمزنگاری فایل های Zip قدیمی Encrypt بر روی داده صورت نمیگرفت و در واقع از متدی بنام `Store` برای ذخیره سازی فایل درون فایل Zip استفاده میشد.
- نرم افزار های مدرن مانند `Winzip` و یا `Winrar` از روش های مدرن برای رمزنگاری استفاده میکنند که در این روش باید نمونه از این Archive Type را بصورت دستی ایجاد کنیم.
- حمله ای که برای کرک فایل های ZIP که از متد قدیمی Store برای رمز نگاری استفاده میکنند انجام میشود، به عنوان حمله *Plain Text Attack* شناخته میشود که در این نوع حمله باید دست کم اطلاعاتی از نوع و محتوای فایلی که میخواهیم درون آرشیو کرک شود را داشته باشیم، در واقع قسمتی از *Type & Content* فایل تارگت درون آرشیو ZIP را باید داشته باشیم.
	![[Pasted image 20240630194241.png]]
- *Known Plain Text Attack Schema*
	- ![[Pasted image 20240630194406.png]]
##### Create Vulnerable Archive
برای تست این روش نیاز داریم که یک آرشیو ZIP آسیب پذیر ایجاد کنیم. برای ایجاد این فایل از نرم افزار `7z` استفاده میکنیم.
برای ساخت آرشیو ZIP آسیب پذیر، در هنگام ساخت ZIP تنظیمات آرشیو را ماننند تصویر زیر تنظیم میکنیم:
	![[Pasted image 20240630194718.png]]
- *Archive format:* `ZIP`
- *Compression Level:* `0 - Store`
- *Encryption:* Set Password `123`
- *Encryption method:* `ZipCrypto`
	- ![[Pasted image 20240630194838.png]]
##### Cracking/Breaking ZIPCrypto Instruction
0. دانلود `Bkcrack` از گیت هاب
	1. https://github.com/kimci86/bkcrack/releases
1. *بدست آوردن محتویات* `test.zip`
	1. فایل `test.zip` آسیب پذیر که ساختیم را به پوشه `Bkcrack` انتقال میدهیم و `CMD` را در آن پوشه باز میکنیم، سپس کامند زیر را برای کرک فایل `test.zip` اجرا میکنیم:
	2. `bkcrack -L test.zip`
		1. ![[Pasted image 20240630195402.png]]
	3. با اجرای کامند بالا، ابزار محتویات درون `test.zip` را لیست میکند.
2. *حال یک فایل متنی جدید میسازیم که شامل Content هایی که میدانیم در فایل های درون `test.zip` موجود است.*
	1. مثلا درون فایل `test.zip` یک فایل متنی `test.txt` وجود دارد، که میدانیم در آن فایل کدهای اجرای کانتینر Docker است. 
	2. بنابراین فایل متنی بنام `pl.txt` ایجاد میکنیم که باید شامل محتویات زیر باشد:
		1. ![[Pasted image 20240630195824.png]]
	3. در واقع از این فایل به عنوان Cipher text  برای ورودی کرک استفاده میشود که در مکانیزم Bkcrack میتوانیم محل Cipher Text را مشاهده کنیم:
		1. ![[Pasted image 20240630194406.png]]
3. *حال برای بدست آوردن Recovery Key کامند زیر را اجرا میکنیم:*
	1. برای بدست آوردن Recovery Key نیازمند فایلی هستیم که محتویاتی داشته باشد که حدس میزنیم در فایل تارگت که میخواهیم کرک شود هم وجود دارد. این فایل با فلگ `p-` به عنوان *Plain Text* به ابزار *Bkcrack* معرفی میشود، 
	2. `bkcrack -C test.zip -c Test/test.txt -p pl.txt`
		1. ![[Pasted image 20240630200609.png]]
	3. `bkcrack -C VulnZip -c VulnZip/request.py -p pl.txt`
		1. ![[Pasted image 20240702224123.png]]
	4. `test.zip` => `-C`
		1. همان فایل آرشیو Zip ماست.
		2. از فلگ `-C` برای معرفی فایل آرشیو اصلی استفاده میشود.
	5. `test.txt` => `-c`
		1. فایلی درون آرشیو که هدف ماست و میخواهیم کرک شود.
		2. از فلگ `-c` برای معرفی فایل تارگت همان Cipher که میخواهیم کرک شود استفاده میکنیم.
	6. `pl.txt` => `-p`
		1. یک فایل متنی که شامل محتویاتی است که درون فایل تارگت هم وجود دارد.
		2. از فلگ `-p` برای معرفی فایل Plain Text که شامل مقداری از Content فایل تارگت است استفاده میشود.
	7. *تصویر*
		1. ![[Pasted image 20240630200500.png]]
4. *حال میتوانیم با استفاده از Recover Key فایل تارگت را Decrypt شده تحویل بگیریم:*
	1. `bkcrack -C test.zip -c test.txt -k f04945f4 3018d661 edc704a6 -d decrypt.txt`
		1. ![[Pasted image 20240630201027.png]]
	2. `decrypt.txt`
		1. فایل خروجی که حاوی فایل کرک شده است.
	3. `-k`
		1. برای وارد کردن Recovery Key در جلوی کامند از ای فلگ استفاده میشود.
	4. `-d`
		1. از این فلگ برای مشخص کردن فایل Decrypt شده که همان نتیجه کرک است استفاده میکنیم.
	5. *تصویر*
		1. ![[Pasted image 20240630200940.png]]
5. *با استفاده از Recovery Key میتوانیم فایل آرشیو جدیدی با پسوردی جدید از فایل `test.zip` ایجاد کنیم:*
	1. با استفاده از Recovery Key میتوانیم یک فایل آرشیو جدید از فایل `test.zip` با پسورد جدید بسازیم.
	2. `bkcrack -C test.zip -k f04945f4 3018d661 edc704a6 -U Unlocked.zip NewPassword`
		1. ![[Pasted image 20240630201341.png]]
	3. با اجرای کامند بالا از فایل `test.zip` یک نمونه جدید بنام `Unlocked.zip` ایجاد کردیم که پسورد آن `NewPassword` است و تمام فایل هایی که درون آرشیو `test.zip` وجود دارند درون آرشیو جدید  `Unlocked.zip` هم وجود دارند.
	4. 
6. *همچنین با استفاده از Recovery Key میتوانیم فایل آرشیو جدید بدون رمز از فایل `test.zip` بسازیم:*
	1. `.\bkcrack.exe -C .\VulnZip.zip -k 348e6771 cecf3c76 51a09805 -D decrypt.zip `
		1. ![[Pasted image 20240702225312.png]]
	2. با این کامند یک فایل آرشیو ZIP جدید بنام `decrypt.zip` ساخته میشود که حاوی تمام محتویات فایل `VulnZip.zip` میشود.
#### Practical Demo
0. *Scenario Description* 
	1. در این سناریو 2 فایل متنی بنام `test, test2` داریم که فایل های کانفیگ Docker یک ایمیج هستند. 
	2. فایل `test1.txt` دارای محتویات زیر است:
		1. ![[Pasted image 20240630201807.png]]
	3. حال Attacker باید سعی کند حداقل محتویات درون این فایل را بفهمد، یعنی حداقل 2 یا سه خط اول فایل را بدست بیاورد و سپس درون فایل متنی جدیدی بریزد تا بتواند به عنوان ورودی Plain Text در جلوی فلگ `p-` آنرا وارد کرد.
		1. ![[Pasted image 20240630202021.png]]
	4. در بسیاری از سناریو ها مشخص است درون فایل تارگت ما چه جیزی وجود دارد.
	5. فایل `test2.txt` حاوی یکسری متن معمولی است که درون آرشیو وجود دارد. در این سناریو فرض میکنیم Attacker هیچ اطلاعاتی از محتویات درون این فایل ندارد.
		1. ![[Pasted image 20240630202141.png]]
1. *Pre-Requires*
	1. *Create Archive*
		1. Install 7-Zip
		2. `Select test1, test2 => Right-Click => 7-Zip => Add to Archive...`
			1. ![[Pasted image 20240630202355.png]]
		3. *Archive Options*
			1. *Compression Level:* Store
			2. *Encryption Method:* ZipCrypto
			3. *Encryption:* Set Password `123`
			4. Image
				1. ![[Pasted image 20240630202542.png]]
			5. Now we have zip file in desktop in name `test.zip`
				1. ![[Pasted image 20240630202627.png]]
	2. Download & Extracted`Bkcrack` https://github.com/kimci86/bkcrack/releases Base on Windows or Linux OS
		1. ![[Pasted image 20240630202805.png]]
	3. Copy `test.zip` to `bkcrack.exe` Folder
		1. ![[Pasted image 20240630202848.png]]
2. *Create Requires file*
	1. Create `pl.txt` in `bkcrack.exe` folder and enter this content in this file
		1. ![[Pasted image 20240630203049.png]]
	2. Now we have all files we need for cracking zip file
		1. ![[Pasted image 20240630203145.png]]
3. *Get Recovery Key*
	1. Open CMD and navigate to `bkcrack.exe` folder
		1. `cd C:\Downloads\Compressed\bkcrack-1.5.1-win64`
			1. ![[Pasted image 20240630203436.png]]
	2. List all content in `test.zip` and Encryption methods
		1. `bkcrack.exe -L test.zip`
			1. ![[Pasted image 20240630203613.png]]
	3. Get Recovery Key of `test.txt`
		1. `bkcrack -C test.zip -c test.txt -p pl.txt`
			1. ![[Pasted image 20240630204038.png]]
		2. پس از اجرای این کامند ابزار حمله ای Bruteforce را پیاده سازی میکند و پس از چند دقیقه Recovery Key فایل تارگت بدست می آید.
4. *Cracking `test.txt`* with plain text defined `-d`
	1. Cracking `test.txt` and save Decrypted file using Recovery key
		1. `bkcrack -C test.zip -c test.txt -k f04945f4 3018d661 edc704a6 -d decrypt.txt`
			1. ![[Pasted image 20240630204525.png]]
		2. Now Decrypted(Cracked) file save in `bkcrack.exe` folder
			1. مشاهده فایل `decrypt.txt`
				1. ![[Pasted image 20240630204756.png]]
		3. فایل `decrypt.txt` در واقع فایل کرک شده همان `test.txt` است و تمام محتویات آنرا شامل میشود:
				1. ![[Pasted image 20240630204709.png]]
5. *Cracking* `test.zip` with created new Instance of Archive `-D`
	1. در این حمله از فایل آرشیو یک نمونه جدید بدون پسورد میسازیم.
	2. `bkcrack -C test.zip -k f04945f4 3018d661 edc704a6 -D Decrypt.zip`
6. *Cracking* `test.zip` with created new Instance of Archive *with Password* `-U`
	1. در این حمله از فایل آرشیو یک نمونه جدید با پسورد دلخواه میسازیم.
	2. `bkcrack -C test.zip -k f04945f4 3018d661 edc704a6 -U Unlocked.zip d@vood129`
		1. ![[Pasted image 20240630205714.png]]
	3. فایل آرشیو جدید ما بنام `Unlocked.zip` از نمونه رمز نگاری خود `test.zip` در پوشه `bkcrack` ایجاد شده و با پسورد `d@vood129` میتوانیم آنرا *Extract* کنیم. در این فولدر هر دو فایل متنی `test1, test2` را میتوانیم مشاهده کنیم:
		1. ![[Pasted image 20240630205923.png]]
----
```powershell
cd C:\Downloads\Compressed\bkcrack-1.5.1-win64
bkcrack.exe -L test.zip #List all files in Archive
bkcrack -C test.zip -c test.txt -p pl.txt #Get Recovery Key
#Decrypt test1.txt to decrypt.txt
bkcrack -C test.zip -c test.txt -k f04945f4 3018d661 edc704a6 -d decrypt.txt
#Create new Archive without password
bkcrack -C test.zip -k f04945f4 3018d661 edc704a6 -D Unlocked.zip
#Create new Archive with password 
bkcrack -C test.zip -k f04945f4 3018d661 edc704a6 -U Unlocked-Password.zip d@vood129
```
- Images:
	- ![[Pasted image 20240630203613.png]]
	- ![[Pasted image 20240630205703.png]]
### Cracking Office Word Files with `John` on `Kali` - E23
#### Definition & Instruction
##### Basic & Concetps 
در این جلسه میخواهیم به کرک فایل های آفیس از جمله Word, PowerPoint, Excel , .... که پسورد دارند بپردازیم. این کار را با ابزار `John` انجام میدهیم.
- ابزار `John` از بهترین ابزار ها در زمینه کرک پسورد میباشد که در اکثر توزیع های لینوکسی مانند Kali, Parrot بصورت پیشفرض یافت میشود. این ابزار یک CLI User-Friendly دارد و همچنین توانایی شناسایی اکثر انواع Hash Type ها را دارد.
- در این جلسه به عمق کاری `John` میرویم تا درک کنیم `John` چگونه کار میکند و چرا استفاده از `John` در تست های امنیتی  Security Testing مهم است.
	- ![[Pasted image 20240701160204.png]]
##### Usage Concepts
*برای کرک فایل های آفیس باید مراحل زیر را دنبال کنیم >>*
1. `office2john`
	1. ابتدا باید مقادیر Hash را از فایل Office با استفاده از `office2john` بدست بیاوریم.
2. `john` | `hashcat`
	1. سپس مقدار Hash را بوسیله `John` و یا `hashcat` کرک میکنیم.
		1. ![[Pasted image 20240701160414.png]]
##### Prepare a Password Protected Office File
*برای آماده کردن فایل Office که Password Protected باشد، در نرم افزار مورد نظر  >>* 
	![[Pasted image 20240701160745.png]]
1. `File => Save as => Tools => General Options => `
	- کافیست یک فایل Office را Save کنیم، سپس در هنگام فرآیند Save به `General Options` میرویم و پسوردی برای فایل انتخاب میکنیم.
		- ![[Pasted image 20240703202144.png]]
2. Now Select Password for Open or Modify File
	- پسورد را میتوانیم برای باز کردن `Password to Open` و یا برای ویرایش فایل `Password to Modify` برای فایل های آفیس مشخص کنیم.
		- ![[Pasted image 20240703202200.png]]
3. Now Copy file to `john\run` folder in windows or Move file to Kali Linux
##### Instruction Steps
0. *Pre-Requires*
	1. یک فایل Office مثلا Word بنام `crackme2.docx` ایجاد میکنیم که پسورد هم داشته باشد. 
	2. سپس فایل را از ماشین ویندوزی به ماشین Kali منتقل میکنیم.
1. *Get the hash from Document(.docx)*
	1. `office2john`
		1. ابزار درونی آفیس است که برای استخراج Hash فایل های آفیس برای کرک توسط John استفاده میشود.
	2. برای بدست آوردن Hash پسورد از فایل Office کافیست کامند زیر را اجرا کنیم:
		1. ![[Pasted image 20240701161603.png]]
	3. `office2john crackme2.docx > hash2.txt`
		1. ![[Pasted image 20240701161644.png]]
	4. `crackme2.docx` Password Protected file
	5. `hash2.txt` this file contains the hash that's requires to cracking
		1. هش پسورد درون این فایل ذخیره میشود که برای کرک پسورد هم باید این فایل را در ورودی `John` وارد کنیم.
2. *Cracking Hash file*
	1. حال با کرک فایل `hash2.txt` میتوانیم به مقدار واقعی پسورد برسیم. برای اینکار کامند زیر را اجرا میکنیم:
	2. `john hash2.txt`
		1. ![[Pasted image 20240701162322.png]]
	3. `hash2.txt` 
		1. فایلی که مقادیر هش شده `crackme2.docx` در آن ذخیره میشود.
	4. با اجرای کامند بالا بصورت پیشفرض، در *حمله اول* یک حمله `Single Core Attack` برای کرک فایل صورت میگیرد که از ترکیب نام فایل برای یافتن و کرک پسورد استفاده میکند.
	5. سپس در *حمله دوم* اگر پسورد یافت نشدن، John حمله ای `Bruteforce` برای کرک پسورد انجام میدهد.
	6. میتوانیم از `Dictionary Attack` هم برای کرک پسورد استفاده کنیم:
	7. `john --w hash2.txt`
	8. *تصویر*
		1. ![[Pasted image 20240701162237.png]]
3. *See Cracking Result*
	1. برای مشاهده مقادیر کرک شده در یک فایل هم از کامند زیر استفاده میکنیم:
	2. `john hash2.txt --show`
		1. ![[Pasted image 20240701162427.png]]
##### John Additional Attacks
- استفاده از حملات `Single Core Attack`  و یا `Brute Force` برای کرک پسورد فایل های آفیس مناسب نیست زیرا زمان و منابع بسیار بیشتری را نسبت به سایر حملات مصرف میکند. 
- بنابراین پیاده سازی حملات `Dictionary Attack` برای این نوع کرک بیشتر استفاده میشود زیرا که میتواند با سرعت بیشتری پسورد عبارت هش شده را پیدا کند.
- همچنین برای افزایش سرعت حمله میتوانیم `Dictionary Attack` را با حمله `Multi-Process Attack` ترکیب کنیم تا حمله ای بهینه داشته باشیم.
1. *Normal Attacks*
	1. تا اینجا فقط از حمله Normal و پیشفرض John استفاده کردیم که در این حمله نیازی به تعریف هیچ فلگی نیست.
	2. `john hash2.txt`
2. *Multi-Process Attack* `-fork=3`
	1. برای افزایش سرعت حمله میتوانیم از این روش استفاده کنیم که در این روش از چند CPU بصورت همزمان در حمله استفاده میشود.
	2. در این حمله میتوانیم از تعداد هسته های CPU بیشتری استفاده کنیم که برای مشخص کردن این تعداد از فلگ `fork=12-` استفاده میشود.
	3. مثلا با استفاده از `fork=3-` مشخص میکنیم که تعداد 3 هسته CPU برای کرک این پسورد استفاده شود.
	4. *اسلاید:*
		1. ![[Pasted image 20240701163154.png]]
3. *Dictionary Attack* `--w` , `--w=""`
	1. *Use Built-In Dictionary Attack* `-w`
		1. با استفاده از فلگ `w-` برای حمله Dictionary از Wordlist داخلی ابزار بنام `john.lst` استفاده میشود.
		2. `john -w hash2.txt`
		3. *اسلاید:*
			1. ![[Pasted image 20240701163438.png]]
	2. *Use a Wordlist for Dictionary Attack* `-w=""`
		1. میتوانیم در مقابل فلگ `w-` یک Wordlist را وارد کنیم تا حمله با استفاده از آن لیست انجام شود.
		2. اگر میخواهیم از Rockyou استفاده کنیم باید ابتا آنرا با استفاده از `gunzip` حالت فشرده خارج کنیم.
		3. `john -w=/usr/share/wordlists/rockyou.txt hash2.txt`
		4. *اسلاید:*
			1. ![[Pasted image 20240701163817.png]]
4. *Mask Attack* `--mask='?d'`
	1. اگر میدانیم که نوع پسورد چیست و یا اطلاعی از اعداد درون پسورد داریم میتوانیم از Mask Attack استفاده کنیم که در این حمله میتوانیم *Pattern* برای یافتن پسورد مشخص کنیم.
	2. در واقع میتوان گفت Mask Attack نوعی از حملات Brute Force است که کاراکترهای مشخصی یا رعایت الگوی مشخصی در آن برای کرک پسورد امتحان میشوند.
	3. `john --mask='?d?d?d' hash2.txt`
		1. ![[Pasted image 20240701164742.png]]
	4. `--mask='?d'`
		1. این ماسک نشان دهنده یک عدد است. در واقع `d?` نشان دهنده کاراکتر عدد است.
		2. در مثال بالا این عبارت `'mask='?d?d?d--`  میگوید که پسورد 3 کاراکتر عدد است. 
		3. میتوانیم مشخص کنیم که پسورد یک کاراکتر عدد و یک حرف بزرگ است.
	5. `--mask='?l'`
		1. مشخص کننده یک کاراکتر Lowercase است.
	6.  `--mask='?u'`
		1. مشخص کننده یک کاراکتر Uppercase است.
	7. `--mask='?u?l?l?l?l?l?d?d?d?d?d'`
		1. مثلا عبارت mask بالا نشان دهنده عبارت `Davood12945` میباشد.
		2. در واقع اگر میدانیم در پسورد از چه کاراکتر هایی استفاده شده است، با Mask Attack میتوانیم حمله را با سرعت بیشتری انجام دهیم.
	8. *اسلاید:*
		1. ![[Pasted image 20240701164657.png]]
```sh
john hash2.txt #Normal Attack
john hash2.txt -fork=3 #Multi-Process Attack
john -w hash2.txt #Built-In Dictionary Attack
john -w=/usr/share/wordlists/rockyou.txt hash2.txt #a Wordlist for Dictionary Attack
john --mask='?d?d?d' hash2.txt #Mask Attack

```
##### Remove Saved Password in John
- *Clear john cache to remove Saved Password* `john.pot`
	- مقادیر هش شده را که John کرک میکند در فایلی بنام `john.pot` ذخیره میکند و در صورتیکه مقدار هش مشابه را در حمله ای دیگر مشاهده کند دیگر آنرا کرک نمیکند و جواب را از دیتابیس واکشی میکند. 
	- اگر این فایل را خذف کنیم، تمام پسورد های کرک شده نیز از حافظه کش john پاک میشوند. 
	- برای حذف کردن مقادیر کرک شده توسط John میتوانیم از کامند های زیر استفاده کنیم.
- *Slide*
	- ![[Pasted image 20240701165150.png]]
```sh
find --name "john.pot"
rm /home/davoodya/.john/john.pot
rm ~/.john/john.pot
```
#### Practical Demo
0. *Pre-Requires*
	1. Create Office Word file and save this.
	2. in *Save Windows* Click on `Tools => General Options`
		1. ![[Pasted image 20240701165346.png]]
	3. Enter Password for `crackme.docx`
		2. ![[Pasted image 20240701165455.png]]
	4. No Create another Office Word file in named `crackme2.docx` and save this with *123* Password
	5. Copy `crackme.docx` and `crackme2.docx` from windows and Paste it to `Kali Home Directory => cd ~`
		1. ![[Pasted image 20240701165854.png]]
	6. `cd ~ && ls`
		1. ![[Pasted image 20240701165955.png]]
1. *Get `crackme.docx` & `crackme2.docx` Hashes using `office2john`*
```sh
cd ~
office2john crackme.docx > hash.txt
office2john crackme2.docx > hash2.txt
```
	![[Pasted image 20240701170252.png]]
2. *Single Core Attack*
	1. `john hash2.txt` Cracking hashes
		1. ![[Pasted image 20240701170433.png]]
		2. ![[Pasted image 20240701170437.png]]
	2. `john hash2.txt --show` See Cracking result
		1. ![[Pasted image 20240701170544.png]]
```sh
john hash2.txt
john hash2.txt --show
```
3. *Multi-Process Attack*
	1. `john hash2.txt --fork=3`
		1. چون قبلا این فایل را کرک کردیم پیامی درایفت میکنیم که پسورد های درون این فایل کرک شده اند.
			1. ![[Pasted image 20240701170751.png]]
		2. پسورد های کرک شده درون فایل `john.pot` قرار دارد در نتیجه اگر این فایل را حذف کنیم پسورد های کرک شده هش ها هم حذف میشوند و دیگر پیام بالا را مشاهده نمیکنیم.
			1. `find --name "john.pot"`
			2. `rm ./.john/john.pot`
				1. ![[Pasted image 20240701171001.png]]
		3. حال اگر دوباره کامند `john hash2.txt --fork=3` را اجرا کنیم ایندفعه حمله انجام میشود.
			1. ![[Pasted image 20240701171055.png]]
		4. 
```sh
john hash2.txt --fork=3
find --name "john.pot"
rm ./.john/john.pot
```
	![[Pasted image 20240701170701.png]]
	![[Pasted image 20240701171010.png]]
4. *Dictionary Attack*
	1. *Built-In Dictionary Attack*
		1. همانطور که گفتیم استفاده از حملات Dictionary برای کرک پسورد فایل های آفیس بهتر کار میدهد. در حمله اول میخواهیم با استفاده از دیکشنری داخلی John حمله را انجام دهیم.
		2. `john -w hash2.txt` Crack Password 
			1. ![[Pasted image 20240701173603.png]]
		3. `john --show hash2.txt` See Cracking Result
			1. ![[Pasted image 20240701173635.png]]
	2. *Dictionary Attack Using Rockyou*
		1. بهترین روش و روش پیشنهادی برای کرک مقادیر هش فایل های آفیس، پیاده سازی حمله Dictionary Attack با استفاده از  Wordlist جامع Rockyou است.
		2. البته هنگامیکه از Wordlist برای کرک استفاده میکنیم زمان حمله افزایش و سرعت حمله کاهش میابد.
		3. `john -w="/usr/share/wordlists/rockyou.txt" hash.txt`
			1. ![[Pasted image 20240701174055.png]]
```sh
john --w hash2.txt #Built-In Dictionary Attack
locate rockyou
gunzip /usr/share/wordlists/rockyou.txt.gz
john -w="/usr/share/wordlists/rockyou.txt" hash.txt #Dictionary Attack using Rockyou wordlist
john -w="/usr/share/wordlists/rockyou.txt" hash.txt --fork=4
```
	![[Pasted image 20240701173536.png]]
	![[Pasted image 20240701174129.png]]
5. *Mask Attack*
	1. در اینجا که میدانیم پسورد فایل `hash2.txt` عبارت `123` است و پسورد فایل `hash.txt` هم `123abC` است، در اینجا با استفاده از Mask Attack هم میتوانیم حملات را پیاده سازی کنیم و هش مورد نظر را کرک کنیم تا پسورد فایل بدست آید.
	2. `john --mask="?d?d?d" hash2.txt` => Mask for Cracking *123* Password
		1. ![[Pasted image 20240701175154.png]]
	3. `john --mask="?d?d?d?l?l?u" hash.txt` => Mask for Cracking *123abC* Password
	4. `john --show hash2.txt hash.txt-` See Cracking Results
		1. ![[Pasted image 20240701175209.png]]

```sh
john --mask="?d?d?d" hash2.txt #Mask Attack for "123" Password
john --mask="?d?d?d?l?l?u" hash.txt #Mask Attack for "123abC" Password
```
	![[Pasted image 20240701174947.png]]
### Install Hashcat & John on Windows 
#### Install Hashcat on Windows - E24
- همانطور که گفتیم Hashcat ابزاری GPU Based است که نیازمند کارت گرافیک قوی به همراه تمام درایور های آن است. از این ابزار میتوانیم در ماشین ویندوزی، توزیع های لینوکس مانند ubuntu, Kali و یا حتی در فضای ابری Cloud استفاده کنیم.
	- ![[Pasted image 20240701180222.png]]
1. Download `hashcat binaries` from official website and Extract it. *9Mb*
	1. https://hashcat.net/hashcat/
		1. ![[Pasted image 20240701180349.png]]
2. Download Rockyou wordlist and Extract it to `Hashcat folder` *139Mb*
	1. https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
		1. ![[Pasted image 20240701180623.png]]
3. Hashcat Folder Files
	1. ![[Pasted image 20240701180954.png]]
4. Installing Finished 
#### Install John on Windows - E26
0. Download `john Windows Binary` 7z or Zip from official website
	1. https://www.openwall.com/john/
		1. ![[Pasted image 20240701181210.png]]
	2. *7z is 20Mb* and *ZIP is 63Mb*
		1. ![[Pasted image 20240701181513.png]]
	3. Extracted Compressed file
1.  Download Rockyou wordlist and Extract it to `John folder` *139Mb*
	1. https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
		1. ![[Pasted image 20240701180623.png]]
	2. Copy Rockyou to `\john-win32\run` folder, Actually in `run` folder in `john` folder
		1. ![[Pasted image 20240701181723.png]]
2. Download and Install `Python 2.7.10`
	1. is important to Download `python 2.7.10` version
		1. ![[Pasted image 20240701181836.png]]
	2. https://www.python.org/download/releases/2.7/
		1. ![[Pasted image 20240701181311.png]]
	3. Download x86 or x64 MSI Installer version
		1. ![[Pasted image 20240701181913.png]]
	4. Install `python2.7.10` sdk for all users
### Cracking Office Excel Password with `Hashcat` - E25
#### Definition & Instruction
##### Usage Concept
*در این روش و حمله نیازمند یک ماشین Kali و همچنین یک ماشین ویندوزی هستیم.*
برای پیاده سازی این Cracking باید فایل Office مورد نظر را به ماشین Kali انتقال دهیم و سپس >>
1. ابتدا باید Hash پسورد را از فایل آفیس بوسیله John استخراج کنیم.
2. سپس با استفاده از ابزار Hashcat و حمله Dictionary Attack به کرک مقدار hash میپردازیم.
*مرحله دوم را در هر دو ماشین ویندوزی و یا لینوکسی میتوانیم انجام دهیم.*
	![[Pasted image 20240701183403.png]]
##### Instruction Steps
0. فایل Office که با پسورد محافظت میشود(Password Protected) را به ماشین Kali منتقل میکنیم.
	1. ![[Pasted image 20240701183521.png]]
1. حال با استفاده از کامند زیر مقدار hash را از فایل Office استخراج میکنیم.
	1. `office2john crackme.xlsx > hash.txt`
		1. ![[Pasted image 20240701183805.png]]
2. پس از بدست آوردن مقادیر hash، فایل `hash.txt` را برای کرک به ماشین ویندوزی و پوشه `Hashcat` منتقل میکنیم.
	1. ![[Pasted image 20240701184021.png]]
3. حال فایل `hash.txt` را باز میکنیم و *نام فایل* را از *محتویات فایل* *حذف* میکنیم.
	1. اینکار را برای اینکه میخواهیم مقدار هش را با Hashcat کرک کنیم انجام میدهیم، در حالیکه در ابزار John نیازی به این کار نیست:
		1. ![[Pasted image 20240701184121.png]]
4. *کرک فایل `hash.txt`*
	1. دقت کنید که فایل `Rockyou` در پوشه `Hashcat` وجود داشته باشد، سپس `Powershell` را در پوشه `Hashcat` باز میکنیم و کامند زیر را برای کرک فایل hash.txt وارد میکنیم.
	2. `.\hashcat -a 0 -m 9600 --status -o cracked.txt hash.txt rockyou.txt`
		1. ![[Pasted image 20240701185021.png]]
	3. `-a 0` Attack Mode is Wordlist
	4. `-m 9600` tell hashcat target is a *Office 13 file*
		1. `-m 9500` for *Office 10* files
		2. `-m 9600` for *Office 13* files
		3. `-m 25300` for *Office 16* files
	5. `-o cracked.txt` Specify Output file
	6. `hash.txt` Target hash file
	7. `rockyou.txt` Target Wordlist for Attack
5. کرک فایل Excel با موفقیت انجام شد.
```sh Get Hashes from document
office2john crackme.xlsx > hash.txt #get hashes from excel document
```
	![[Pasted image 20240701183923.png]]
----
```powershell Cracking hashes
.\hashcat -a 0 -m 9600 --status -o cracked.txt hash.txt rockyou.txt
```
##### Hashcat Additional  
###### Hashcat Wiki
- https://hashcat.net/wiki/
در هنگام کرک با `hashcat` در مقابل فلگ `m-` باید نوع فرمت hash را مشخص کنید. هر فرمت از هش ها عدد مخصوص خود را دارد مثلا >>
1. `100` *SHA1*
2. `1000` *NTLM*
3. `9500` *Office 10 file*
4. `9600` *Office 13 file*
5. `-m 2530` *Office 16* 
6. etc ....
> حال لیست کامل این اعداد را برای انواع فرمت های hash را میتوان از صفحه `Hashcat Wiki` از قسمت `Example Hashes` بصورت کامل مطالعه کرد.
> https://hashcat.net/wiki/
> لینک قسمت `Example Hashes` که لیست کاملی از فرمت ها و اعداد آنها برای استفاده از مقابل `m-` وجود دارد:
> https://hashcat.net/wiki/doku.php?id=example_hashes
###### Specify GPU Device for Hashcat 
برای انتخاب دیوایس کارت گرافیکی که میخواهیم در کرک Hashcat استفاده شود از فلگ `D-` و `d-` که مخفف `Device` است، استفاده میکنیم. در واقع ابتدا باید دیوایس هایی که Hashcat میتواند از آنها استفاده کند را لیست کنیم و پس از انتخاب دیوایس مورد نظر آنرا بوسیله این فلگ ها انتخاب کنیم.
```powershell
./hashcat -a 0 -m 9600 --status -D2 -d3 -o cracked hash.txt rockyou.txt
```
#### Practical Demo
0. *Pre-Requires*
	1. Create Password Protected Excel file.
		1. Create Excel file in name `crackme.xlsx`
		2. Save As `Excel Workbook` Type
		3. in Save Windows `Tools => Generel Options => `
		4. Set Password for file *123456*
			1. ![[Pasted image 20240701193513.png]]
	2. Copy Excel file `crackme.xlsx` and Paste it to Kali Machine `/home/kali` Home Directory
		1. ![[Pasted image 20240701193648.png]]
1. *Get Hashes from* `crackme.xlsx`
	1. Open Terminal and get hashes from `crackme.xlsx`
	2. `office2john crackme.xlsx > hash.txt`
		1. ![[Pasted image 20240701194004.png]]
	3. Now Copy `hash.txt` and paste it to Windows Machine in `Hashcat Folder`
		1. ![[Pasted image 20240701194132.png]]
2. *Crack Hash file* `hash.txt
	1. Open `hash.txt` and remove *File Name* from *File Content*
		1. در واقع فقط وقتی بنام فایل نیاز داریم که بخواهیم پسورد فایل را Modify کنیم. 
			1. ![[Pasted image 20240701194420.png]]
		2. در غیر اینصورت نام را از محتویات فایل حذف میکنیم:
			1. ![[Pasted image 20240701194503.png]]
	2. `Shift + Right-Click => Open Powershell here ...` in Hashcat Folder
	3. Run Following Command to Crack `hash.txt` and save result to `cracked.txt`
		1. `./hashcat -a 0 -m 9600 --status -o cracked.txt hash.txt rockyou.txt`
			1. ![[Pasted image 20240701195421.png]]
4. *Cracking Result* `cracked.txt`
	1. in Powershell
		1. ![[Pasted image 20240701195549.png]]
	2. `\Hashcat\cracked.txt`
		1. ![[Pasted image 20240701195752.png]]
----
```powershell
./hashcat -a 0 -m 9600 --status -o cracked.txt hash.txt rockyou.txt
```
	![[Pasted image 20240701195337.png]]
	![[Pasted image 20240701195549.png]]
### Cracking Office PowerPoint Files with `John` on `Windows` - E27
#### Definition & Instruction
##### Definitions
- در این روش میخواهیم به کرک فایل PowerPoint بپردازیم، اما از این روش برای کرک فایل های Word, Excel, و سایر فایل های آفیس هم میتوانیم استفاده کنیم.
- ابزار `John` یک ابزار پایتونی است که اکثر ماژول های آن به زبان پایتون نوشته شده اند. 
- استفاده از `John` در لینوکس بصورت پیشفرض میسر است و نیازی هم به نصب پکیج های اضافه ندارد اما استفاده از `John` در ویندوز نیازمند نصب پیکیج `Python 2.7.10` بصورت مجزا در کنار اوست.
- همچنین یکسری از ماژول های ابزار John با زبان `perl` توسعه داده شده اند مانند `rar2john` 
##### Usage Concept
1. بدست آوردن مقدار Hash پسورد از فایل Office بوسیله `office2john`
2. کرک مقدار Hash بوسیله `John`
3. *اسلاید*
	1. ![[Pasted image 20240701201219.png]]
##### Instruction Steps
0. *Pre-Requires*
	1. ساخت یک فایل Power Point بنام `crackme.pptx` با پسورد *1234*
		1. ![[Pasted image 20240701201344.png]]
	2. کپی فایل `crackme.pptx` به پوشه `\john\run\` در ویندوز
		1. ![[Pasted image 20240701201500.png]]
1. *Get Hashes from* `crackme.pptx`
	1. حال کافیست Powershell را در پوشه `\john\run\` باز کنیم و کامند زیر را برای بدست آوردن هش ها اجرا کنیم.
	2. `C:\python27\python office2john.py crackme.pptx > hash.txt`
		1. در واقع بدلیل اینکه ابزار `office2john.py` ابزاری پایتونی است باید انرا با فایل اجرایی Python 2.7 اجرا کنیم.
			1. ![[Pasted image 20240701202020.png]]
		2. `C:\python27\python` لینک به فایل اجرایی پایتون 2.7 برای اجرای ابزار
		3. `Crackme.pptx` فایل هدف که میخواهیم هش پسورد آنرا بدست بیاوریم
		4. `hash.txt` هش فایل در این فایل ذخیره میشود که برای کرک باید از این فایل استفاده کنیم
2. *Cracking Password from* `hash.txt`
	1. دقت کنید فایل Rockyou در پوشه `\john\run\` وجود داشته باشد. سپس در Powershell کامند زیر را برای کرک فایل هش `hash.txt` اجرا میکنیم.
	2. `.\john -w="rockyou.txt" hash.txt`
		1. با اجرای کامند John شروع به Dictionary Attack برای کرک مقدار هش پسورد میکند.
			1. ![[Pasted image 20240701202543.png]]
3. *See Cracking Results*
	1. `.\john --show hash.txt`
		1. ![[Pasted image 20240701202715.png]]
----
```powershell Open in /john/run 📂 
#Get hash from hackme.pptx
C:\python27\python office2john.py crackme.pptx > hash.txt 
#Cracking Hash from hash.txt 
.\john -w="rockyou.txt" hash.txt
#See Cracking Result
.\john --show hash.txt
```
	![[Pasted image 20240701202235.png]]
	![[Pasted image 20240701202611.png]]
#### Practical Demo
0. *Pre-Requires*
	1. Create Power Point file
	2. Save With Password
		1. ![[Pasted image 20240701202912.png]]
		2. ![[Pasted image 20240701202934.png]]
	3. Copy `hackme.pptx` and Paste it to `john\run` folder
		1. ![[Pasted image 20240701203129.png]]
1. *Get hashes from `hackme.pptx`*
	1. Open CMD in `john\run` 
		1. ![[Pasted image 20240701203217.png]]
	2. Use `python27` and `office2john` to obtaining Office File Password Hashes
		1. `C:\python27\python office2john.py crackme.pptx > hash.txt`
		2. مسیر فایل پایتون را باید به دقت بر طبق نصب پایتون بر روی ماشین خود انتخاب کنیم.
			1. ![[Pasted image 20240701203414.png]]
	3. Open `hash.txt` and remove *file name* from *file content*  `Optional`
		1. ![[Pasted image 20240701203636.png]]
2. *Crack `hash.txt` by Dictionary Attack*
	1. Now we can Crack `hash.txt` using `john` in Dictionary Attack
	2. `john -w="rockyou.txt" hash.txt`
		1. ![[Pasted image 20240701203832.png]]
3. *Cracking Successfully Done*
	1. See Password in Terminal, Or get all Cracked password by run following command
	2. `john --show hash.txt`
----
```powershell
#Get hash from hackme.pptx
C:\python27\python office2john.py crackme.pptx > hash.txt 
#Cracking Hash from hash.txt 
john --w="rockyou.txt" hash.txt
#See Cracking Result
john.py --show hash.txt
```
	![[Pasted image 20240701204050.png]]
4. Cracking `crackme.pptp` in Kali
	1. Move `crackme.pptp` to Kali machine
	2. Open Terminal and run following commands 
```sh
office2john crackme.pptp > hashp.txt
john -w="/usr/share/wordlists/rockyou.txt" hashp.txt
```
	![[Pasted image 20240703222548.png]]
### !