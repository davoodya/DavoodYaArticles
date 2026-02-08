---
Episode: E28 to E31
Date: 2024-07-03
Is Finished?: true
Practice Primary: true
Practice Secondary: 
Time: 32:00
tags:
  - CyberSecurity
  - hacking
Category: Cyber Security
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[E22 to E27 (Cracking Compresses & Offices Files - Part1)]]"
Next Episode: "[[E32 to E36 (Cracking Compresses & Offices - Part3)]]"
---
-------
#CyberSecurity #hacking 
## E28 to E31 (Cracking Offices & PDF Files - Part2)
- [Unlock Read-Only Excel Files - E28](#Unlock%20Read-Only%20Excel%20Files%20-%20E28)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Concept of Usage](#Concept%20of%20Usage)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [Remove Sheet & Workbook Protection from Excel Files - E29](#Remove%20Sheet%20&%20Workbook%20Protection%20from%20Excel%20Files%20-%20E29)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Concept of Usage](#Concept%20of%20Usage)
		- [Protect Sheet & Workbook in Excel](#Protect%20Sheet%20&%20Workbook%20in%20Excel)
		- [1. Remove Sheet Protection Instruction](#1.%20Remove%20Sheet%20Protection%20Instruction)
		- [2. Remove Workbook Protection Instruction](#2.%20Remove%20Workbook%20Protection%20Instruction)
	- [Practical Demo](#Practical%20Demo)
		- [Remove Sheet Protection](#Remove%20Sheet%20Protection)
		- [Remove Workbook Protection](#Remove%20Workbook%20Protection)
- [Unlock Read-Only Word & Power Point Files - E30](#Unlock%20Read-Only%20Word%20&%20Power%20Point%20Files%20-%20E30)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Unlock Power Point File Instruction](#Unlock%20Power%20Point%20File%20Instruction)
		- [Unlock Word File Instruction](#Unlock%20Word%20File%20Instruction)
	- [Practical Demo](#Practical%20Demo)
		- [Unlock Power Point Demonstrates](#Unlock%20Power%20Point%20Demonstrates)
		- [Unlock Word File Demonstrates](#Unlock%20Word%20File%20Demonstrates)
- [Cracking PDF Passwords with `Pdfrip` & `John` - E31](#Cracking%20PDF%20Passwords%20with%20%60Pdfrip%60%20&%20%60John%60%20-%20E31)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [Concept of Usage](#Concept%20of%20Usage)
		- [Different Usage in Different Versions](#Different%20Usage%20in%20Different%20Versions)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
-----
### Unlock Read-Only Excel Files - E28
#### Definition & Instruction
##### Concept of Usage
برخی فایل های آفیس بصورت فقط خواندنی عرضه و ارائه میشوند. حال میتوانیم این نوع فایل ها را نیز کرک کنیم تا بتوانیم به محتویات آن فایل دسترسی Full یعنی هم Read و هم Write داشته باشیم.
##### Instruction Steps
0. Pre-Pare Password Protected Excel file
	1. ![[Pasted image 20240702193737.png]]
1. Change Excel file Extension to `.zip` and Open it
	1. ![[Pasted image 20240702193922.png]]
	2. ![[Pasted image 20240702194051.png]]
2. in ZIP folder Navigate to `\xl\` folder and Cut `workbook.xml` to other path, Then Open `workbook.xml` file in Text Editor.
	1. در این مرحله در پوشه ZIP فایل Excel، به پوشه `xl` میرویم و فایل  `workbook.xml` در ادیتور متنی باز میکنیم. در اینجام نام فایل ما `Workbook.xml` است:
		1. ![[Pasted image 20240702194516.png]]
3. Search for *"filesharing"* tag and Remove this tag and all content in this`<filesharing ... />` 
	1. حال کافیست در این فایل، تگ "filesharing" و محتویات درون `<filesharing ... />` آنرا کاملا پاک کنیم.
		1. ![[Pasted image 20240702194737.png]]
4. Save edited file in same name `Workbook.xml` , and then Drag it to Archive `xl` folder and Replace it with Original `Workbook.xml`
	1. حال کافیس فایل را در محلی دیگر در ماشین با نام مشابه نام اصلی فایل ذخیره کنیم و سپس فایل را به آرشیو فایل اکسل پوشه `xl` منتقل میکنیم و آنرا Replace فایل اصلی میکنیم.
		1. ![[Pasted image 20240702195049.png]]
5. Excel file now is Full Access 
#### Practical Demo
0. ساخت فایل اکسل جدید و ذخیره آن با پسورد `Password to Modify` 
	1. دقت داشته باشید این حمله فقط برای یافتن `Password to Modify`  استفاده میشود.
		1. ![[Pasted image 20240702195357.png]]
	2. برای کرک پسورد `Password to Open` باید از روش های قبلی که توضیح دادیم(Cracking Password) استفاده کنیم.
	3. حال اگر فایل اکسل را باز کنیم برای تغییر باید پسورد را وارد کنیم و یا فقط میتوانیم فایل را بصورت `Read-Only` باز و مشاهده کنیم:
		1. ![[Pasted image 20240702195614.png]]
1. حال پسوند فایل اکسل را به `ZIP.` تغییر میدهیم.
	1. ![[Pasted image 20240702195812.png]]
2. سپس فایل `Book1.zip` را با `Explorer` و یا `Winrar` باز میکنیم و به پوشه `\xl\` درون آن میرویم و فایل `workbook.xml` که حاوی کدهای اصلی Work Sheet ماست  را به پوشه ای دیگر منتقل میکنیم و آنرا با ادیتوری متنی باز میکنیم :
	1. ![[Pasted image 20240702195936.png]]
3. در کدهای فایل `workbook.xml` بدنبال تگ `<filesharing>` میگردیم و این تگ و تمام محتویات درون این تگ را پاک میکنیم:
	1. ![[Pasted image 20240702200235.png]]
4. فایل را با همان نام `workbook.xml`  ذخیره میکنیم، و سپس آنرا به پوشه `xl` منتقل میکنیم و در واقع آنرا با فایل `workbook.xml` اصلی *Replace* میکنیم.
	1. ![[Pasted image 20240702200415.png]]
5. حال کافیست پسوند فایل zip را مجددا به `xlsx.` تغییر دهیم:
	1. ![[Pasted image 20240702200511.png]]
6.  حال فایل اکسل را که باز کنیم میتوانیم بدون نیاز به وارد پسورد آنرا ویرایش کنیم.
	1. ![[Pasted image 20240702200549.png]]
### Remove Sheet & Workbook Protection from Excel Files - E29
#### Definition & Instruction
##### Concept of Usage
*تا اینجا یاد گرفتیم که >>*
- پسورد `Password to Open` فایل های آفیس را حذف کنیم که همان Password Cracking است.
- محدودیت های` Read-Only` و `Password to Modify` را از فایل های آفیس برداریم.
*در این جلسه میخواهیم یاد بگیریم که >>*
- حذف مکانیزم `Excel Sheet Protection` از فایل های آفیس
- حذف مکانیزم `Excel Workbook Protection` از فایل های آفیس
*اسلاید >>*
	![[Pasted image 20240702200954.png]]
##### Protect Sheet & Workbook in Excel 
- `Excel file => Review Tab => Protect Workbook`
	- ![[Pasted image 20240703225008.png]]
- `Excel file => Review Tab => Protect Sheet`
	- ![[Pasted image 20240703224813.png]]
- در فایل های اکسل میتوانیم یک سپر محافظتی را بر روی کل Workbook و یا بر روی یک Sheet بگذاریم. برای اینکار فایل اکسل را باز میکنیم و سپس به تب `Review` در فایل اکسل میرویم، حال بر روی `Protect Sheet` و یا `Protect Workbook` کلیک میکنیم و نوع سپر محافظتی را مشخص میکنیم، همچنین یک پسورد هم میتوانیم برای این محافظت در نظربگیریم:
	![[Pasted image 20240702201247.png]]
	![[Pasted image 20240702204044.png]]
- بوسیله مکانیزم Protect Sheet میتوانیم انواع محدودیت هایی را برای دسترسی و کار با این Sheet های فایل اکسل تعریف کنیم و در نظر بگیریم. 
	- ![[Pasted image 20240702202500.png]]
- بوسیله مکانیزم Protect Workbook میتوانیم انواع محدودیت هایی را برای دسترسی و کار با این کل فایل اکسل Workbook تعریف کنیم و در نظر بگیریم.
- در واقع این محدودیت ها را بر روی Workbook و یا Sheet ها میتوانیم اعمال کنیم که روش برداشتن هر کدام متفاوت میباشد. محدودیتهایی که بر روی Workbook صورت میگیرد بر روی کل Structure فایل اعمال میشود و محدودیت هایی که بر روی Sheet قرار میگرند میتوانند به محدود کردن فرآیند های اضافه کردن Sheet جدید و یا Remove کردن یک Sheet و ... کلا مسائل مدیریتی Sheet ها بپردازند.
##### 1. Remove Sheet Protection Instruction
0. Pre-Requires
	1. ساخت یک فایل اکسل که Password Protected است و سپر محافظتی `Protect Sheet` هم دارد.
	2. سپس فایل را ذخیره میکنیم، و پسوند فایل را به `ZIP` تغیر میدهیم.
		1. ![[Pasted image 20240702201421.png]]
3. Navigate to `zip\xl\worksheet\` and Cut `sheet2.xml` to other location, Then Open `sheet2.xml` with Text Editor
	1. سپس فایل `ZIP` را باز میکنیم و به پوشه `xl` میرویم.
			1. ![[Pasted image 20240702201522.png]]
	2. سپس به پوشه `\xl\worksheet` میرویم، فایل را به مکانی دیگر منتقل میکنیم و فایل `sheet2.xml` را در ادیتور متنی باز میکنیم:
		1. ![[Pasted image 20240702201621.png]]
4. Search and Remove *"sheetProtection"* Tag and all content in this `<sheetProtection />`
	1. در فایل باز شده بدنبال تگ `<sheetProtection />` میگردیم و خود تگ و محتویات آنرا پاک میکنیم.
		1. ![[Pasted image 20240702201911.png]]
	2. حال فایل را با همان نام `sheet2.xml` ذخیره میکنیم و سپس آنرا به پوشه `zip\xl\worksheet\` درگ میکنیم و با فایل اصلی `Replace` میکنیم.
		1. ![[Pasted image 20240702202020.png]]
5. Change back `zip` extension to `xlsx` 
	1. حال کافیست پسوند فایل `ZIP` را به `xlsx` تغییر دهیم.
		1. ![[Pasted image 20240702202135.png]]
6. *Open Excel file without any Sheet Protection*
##### 2. Remove Workbook Protection Instruction
0. Pre-Requires
	1. Create `Protected Workbook Excel` file and save it.
	2. Change Excel file extension to `ZIP`
		1. ![[Pasted image 20240702202607.png]]
1. Open `ZIP` file with `Explorer` or `WinRAR(Recommended)` 
	1. Open ZIP Folder with WinRAR  Recommended
		2. ![[Pasted image 20240702202707.png]]
	1. Navigate to `zip\xl\` and copy `workbook.xml` to other location and open it with a Text Editor
		1. ![[Pasted image 20240702202836.png]]
	2. Search for `<workbookProtection />` tag and remove tag and all contents in tag
		1. ![[Pasted image 20240702203041.png]]
	3. Save file with same name `workbook.xml` , and then Drag it to `zip\xl\` folder and `Replace` this with original `workbook.xml`.
		1. ![[Pasted image 20240702203207.png]]
2. Now Change back `.zip` to `.xlsx`
	1. ![[Pasted image 20240702203322.png]]
3. *Now Open Excel file without Workbook Protection*
#### Practical Demo
##### Remove Sheet Protection
0. Pre-Requires
	1. Create Excel file, Open it and goto `Review tab => Protect Sheet` and Select password for protecting sheet
		1. ![[Pasted image 20240702204143.png]]
	2. Save file with `.xlsx` extension in name `test1.xlsx`
		1. ![[Pasted image 20240702204248.png]]
	3. Now Open file, When you add new content in columns, We see this Error
		1. ![[Pasted image 20240702204336.png]]
	4. Change file extension from `test1.xlsx` to `test1.zip`
1. Open `test1.zip` and Navigate to `test1.zip\xl\worksheets`
	1. Drag `sheet2.xml` on Desktop and Open `sheet2.xml` with *Text Editor*
	2. in `sheet2.xml` Find `sheetProtection` and *Remove* `<sheetProtection />` Tag and Tag Contents
		1. ![[Pasted image 20240702204835.png]]
	3. Now Save file, and Drag it to `test1.zip\xl\worksheets` and *Replace* it with Original `sheet2.xml`
		1. ![[Pasted image 20240702205020.png]]
2. Change back `test1.zip` to `test1.xlsx`
3. *Open `test1.xlsx` without any Sheet Protection*
##### Remove Workbook Protection
0. Pre-Requires
	1. Create Excel file, Open it and goto `Review tab => Protect Workbook` and Select password for protecting Workbook
		1. ![[Pasted image 20240702205347.png]]
	2. Save file, Open again and you cant add or hide sheets without password.
	3. Change file extension from `test1.xlsx` to `test1.zip`
1. Open `test1.zip` and Navigate to `test1.zip\xl`
	1. Drag `workbook.xml` on Desktop and Open `workbook.xml` with *Text Editor*
	2. in `workbook.xml` Find `workbookProtection` and *Remove* `<workbookProtection />` Tag and Tag Contents
		1. ![[Pasted image 20240702205719.png]]
	3. Now Save file, and Drag it to `test1.zip\xl` and *Replace* it with Original `workbook.xml`
		1. ![[Pasted image 20240702205835.png]]
2. Change back `test1.zip` to `test1.xlsx`
	1. ![[Pasted image 20240702205914.png]]
3. *Open `test1.xlsx` without any Workbook Protection. Actually we can add new sheet or hide sheets*
### Unlock Read-Only Word & Power Point Files - E30
#### Definition & Instruction
##### Unlock Power Point File Instruction 
0. Pre-Requires
	1. Prepare Password Protected Power Point file with `Password to Modify`
		1. ![[Pasted image 20240703160723.png]]
	2. Change `.pptx` extension to `.zip`
		1. ![[Pasted image 20240703160818.png]]
1. Open `Crackme.zip` in *Windows Explorer*
	1. Navigate to `\Crackme.zip\ppt` and open `presentation.xml` in Text Editor
		1. ![[Pasted image 20240703161029.png]]
	2. Search for `<modifyVerifier>` and Remove this tag and all contents in this tag.
		1. ![[Pasted image 20240703161153.png]]
	3. Save file in same name `presentation.xml` in Desktop folder.
	4. Copy `presentation.xml` in `\Crackme.zip\ppt` and Replace with Original file
		1. ![[Pasted image 20240703161539.png]]
2. Change back extension from `.zip` to `.pptx`
3. Now we can Open Power Point file without any password
##### Unlock Word File Instruction 
0. Pre-Requires
	1. Prepare Password Protected Word file with `Password to Modify` 
		1. ![[Pasted image 20240703161856.png]]
	2. Change `.docx` extension to `.zip`
1. Open `Crackme.zip` in *Windows Explorer*
	1. Navigate to `\Crackme.zip\word` and open `settings.xml` in Text Editor
		1. ![[Pasted image 20240703162004.png]]
	2. Search for `<writeprotection>` and Remove this tag and all contents in this tag.
		1. ![[Pasted image 20240703162043.png]]
	3. Copy `settings.xml` in `\Crackme.zip\word` and Replace with Original file
2. Change back extension from `.zip` to `.docx`
3. Now we can Open Word file without any password
#### Practical Demo
##### Unlock Power Point Demonstrates 
1. *پیش نیاز ها*
	1. ساخت فایل پاور پوینت آسیب و ذخیره آن با پسورد `Password to Modify`
		1. ![[Pasted image 20240703162344.png]]
		2. `Save As => Tools => General Option => Enter Password to Modify `
	2. تغییر پسوند فایل از `pptp` به `zip`
2. *باز کردن `Crackme.zip` در اکسپلورر ویندوز*
	1. رفته به پوشه `Crackme.zip\ppt` و کپی فایل `presentation.xml` به دسکتاپ
	2. باز کردن فایل `presentation.xml` در ادیتور و متنی
	3. یافتن تگ `<modifyVerifier>` و حذف کرن تگ و محتویات این تگ
		1. ![[Pasted image 20240703162728.png]]
	4. ذخیره فایل و انتقال مجدد فایل به ` Crackme.zip\ppt` و جایگزین کردن آن با `presentation.xml` اصلی
3. تغییر پسوند فایل از `zip` به `pptp`
4. پسورد با موفقیت از فایل `Crackme.pptp` حذف شده و بدون نیاز به پسورد میتوان فایل را باز و ادیت کرد.
##### Unlock Word File Demonstrates 


1. *پیش نیاز ها*
	1. ساخت فایل Word آسیب و ذخیره آن با پسورد `Password to Modify`
		2. `Save As => Tools => General Option => Enter Password to Modify `
			1. ![[Pasted image 20240703163034.png]]
	2. تغییر پسوند فایل از `docx` به `zip`
2. *باز کردن `Crackme.zip` در اکسپلورر ویندوز*
	1. رفته به پوشه `Crackme.zip\word` و کپی فایل `settings.xml` به دسکتاپ
	2. باز کردن فایل `settings.xml` در ادیتور و متنی
	3. یافتن تگ `<writeProtection>` و حذف کرن تگ و محتویات این تگ
		1. ![[Pasted image 20240703163317.png]]
	4. ذخیره فایل و انتقال مجدد فایل به ` Crackme.zip\word` و جایگزین کردن آن با `settings.xml` اصلی
3. تغییر پسوند فایل از `zip` به `docx`
4. پسورد با موفقیت از فایل `Crackme.docx` حذف شده و بدون نیاز به پسورد میتوان فایل را باز و ادیت کرد.
### Cracking PDF Passwords with `Pdfrip` & `John` - E31
#### Definition & Instruction
##### Concept of Usage
- برخی از پلاگین و ماژول های ابزار John با استفاده از زبان Perl توسعه داده شده است. بنابراین اگر میخواهیم در ویندوز از ماژول های John، مثلا ماژول کرک PDF استفاده کنیم باید ابتدا `Perl Language` را بر روی ماشین ویندوزی نصب کنیم.
 - در حالیکه `Perl Language` بصورت پیشفرض بر روی Kali و سایر توزیع های لینوکسی نصب است بنابراین بدون نیاز به نصب `Perl Language` میتوانیم ماژول کرک PDF ابزار john را استفاده کنیم.
 - حال ابزار دیگری بنام `Pdfrip` وجود دارد که بوسیله آن در ویندوز میتوانیم به کرک فایل های PDF بپردازیم.
 - *اسلاید*
	 - ![[Pasted image 20240703165023.png]]
> در نتیجه برای کرک فایل های PDF در ویندوز از *Pdfrip* استفاده میکنیم و در لینوکس از *John The Ripper* و *Perl Module* استفاده میکنیم.
##### Different Usage in Different Versions
- **نکته**: این ابزار بر روی ورژن های جدید رمزنگاری Acrobat یعنی `Adobe Acrobat X` که از الگوریتم `AES 256` استفاده میکند کار نمیکند و نمیتواند این نوع رمزنگاری را کرک کند، اما ابزار میتواند سایر ورژن های یعنی `Adobe 7 & Adobe 8` را که از الگوریتم `AES 128bit` استفاده میکنند را کرک کند:
	- ![[Pasted image 20240704231535.png]]
**نکته دوم**: همچنین Syntax استفاده از `Pdfrip` در ورژن های قدیمی و جددی متفاوت میباشد. در زیر میتوانید این تفاوت را مشاهده کنید:
```powershell
#In Old Versions
.\pdfrip.exe TARGETFILE.pdf -w WORDLIST.txt
.\pdfrip.exe Crackme.pdf -w Rockyou.txt 

#In New Versions
.\pdfrip.exe -f TARGETFILE.pdf wordlist WORDLIST.txt
.\pdfrip.exe -f Crackme.pdf wordlist .\rockyou.txt 
```
##### Instruction Steps
0. Pre-Requires
	1. ساخت فایل PDF با پسورد
		1. در نرم افزار Adobe Acrobat reader برای ساخت فایل PDF محافظت شده کافیست به `Properties => Security tab` برویم و در آن قسمت میتوانیم برای فایل پسوردی را انتخاب کنیم. پس از انتخاب پسورد هم فایل را Save میکنیم:
			1. ![[Pasted image 20240703165339.png]]
	2. دانلود `Pdfrip` از https://github.com/mufeedvh/pdfrip/releases
		1. ![[Pasted image 20240703165459.png]]
	3. دانلود `Rockyou` و کپی آن به پوشه `Pdfrip` از https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
			1. ![[Pasted image 20240703165607.png]]
	4. کپی کردن فایل تارگت به پوشه `Pdfrip`
1. Open Terminal in `Pdfrip` Folder and Run following command to Cracking target file
	1. Dictionary Attack
		1. *in Old Versions* `.\pdfrip.exe Crackme.pdf -w Rockyou.txt`
		2. *in New Versions* `.\pdfrip.exe -f Crackme.pdf wordlist .\rockyou.txt`
		3. `Crackme.pdf` Target file want to be Cracking
		4. `-w Rockyou.txt`  Wordlist for Dictionary Attack
			1. ![[Pasted image 20240703170044.png]]
		5. See Cracking Result in Terminal
			1. ![[Pasted image 20240703170111.png]]
----
```powershell
.\pdfrip.exe Crackme.pdf -w Rockyou.txt #In Old Versions
.\pdfrip.exe -f Crackme.pdf wordlist .\rockyou.txt #In New Versions
```
#### Practical Demo
0. Pre-Requires
	1. Open Adobe Acrobat Reader, Create PDF file and Save it with password
		1. `File => Properties(CTRL+D) => Security tab => Select Password Security `
			1. ![[Pasted image 20240703170437.png]]
		2. in next windows Enter Password for PDF file and click `OK`
			1. ![[Pasted image 20240703170524.png]]
		3. Close file and Save it, Now open again and yo see password field
			1. ![[Pasted image 20240703170624.png]]
	2. Download `Pdfrip`
		1. https://github.com/mufeedvh/pdfrip/releases
	3. Download `Rockyou`
		1. https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
	4. Copy Rockyou and Target PDF File to `Pdfrip` folder
		1. ![[Pasted image 20240703170841.png]]
1. Open `CMD` in `Pdfrip` folder and Run following Command to be Cracking `crackme.pdf` file
	1. در ورژن های قدیمی از کامند اول برای کرک استفاده میکنیم و در ورژن های جدید از کامند دوم برای کرک پسورد فایل استفاده میکنیم.
	2. `pdfrip crackme.pdf -w rockyou.txt`
		1. ![[Pasted image 20240703171134.png]]
	3. `.\pdfrip.exe -f .\Crackme.pdf wordlist .\rockyou.txt`
		1. ![[Pasted image 20240704231926.png]]
2. `crackme.pdf` Successfully Cracked.

```powershell
.\pdfrip.exe crackme.pdf -w rockyou.txt #Old Versions
.\pdfrip.exe -f .\Untitled.pdf wordlist .\rockyou.txt #New Versions
```
	![[Pasted image 20240703171116.png]]
	![[Pasted image 20240704231800.png]]


