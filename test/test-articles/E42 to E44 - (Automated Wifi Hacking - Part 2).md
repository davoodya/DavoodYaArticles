---
Episode: E41 to E44
Date: 2024-07-09
Is Finished?: true
Practice Primary: true
Practice Secondary: 
Time: 42:00
tags:
  - CyberSecurity
  - hacking
Category: Cyber Security
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[E37 to E41 - (Wifi Hacking - Part 1)]]"
Next Episode: "[[E45 to E49 - (Pentesting Module Concepts - Part 1)]]"
---
-------
## E41 to E44 - (Wifi Hacking - Part 2)
- [Hacking Wifi Purely on Windows with `CommView Wifi` - E42](#Hacking%20Wifi%20Purely%20on%20Windows%20with%20%60CommView%20Wifi%60%20-%20E42)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is CommView for Wifi?](#What%20is%20CommView%20for%20Wifi?)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
		- [What is Name of this Anti Virus?](#What%20is%20Name%20of%20this%20Anti%20Virus?)
- [Automatic Wifi Cracking with `Wifite` - E43](#Automatic%20Wifi%20Cracking%20with%20%60Wifite%60%20-%20E43)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is Wifite?](#What%20is%20Wifite?)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
- [GUI Based Automated Wifi Cracking with `FERN` - E44](#GUI%20Based%20Automated%20Wifi%20Cracking%20with%20%60FERN%60%20-%20E44)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is FERN?](#What%20is%20FERN?)
		- [Wifite vs FERN](#Wifite%20vs%20FERN)
		- [Instruction Steps](#Instruction%20Steps)
	- [Practical Demo](#Practical%20Demo)
****
### Hacking Wifi Purely on Windows with `CommView Wifi` - E42
#### Definition & Instruction
##### What is CommView for Wifi?
- ابزار CommView for Wifi ابزاری غیر رایگان برای مانیتورینگ شبکه های وایرلسی(802.11) در استاندارد های `a/b/g/n/ac/ax` در ویندوز است.
- نسخه Trial این ابزار را میتوان بصورت رایگان به مدت زمان 30 روز استفاده کرد، همچنین میتوانیم از نسخه کرک شده هم استفاده کنیم. نسخه کرک شده را در سافت 98 پیدا کنید:
	- https://soft98.ir/internet/network/561-commview-wifi.html
- برای استفاده از این ابزار و در واقع اسکن شبکه های اطراف، باید کارت شبکه وایرلس داشته باشیم که `Monitor Mode` را پشتیبانی کنند. 
- همچنین اگر میخواهیم بوسیله این ابزار Attack هایی مانند `Disassotiation Attack` را برای Capture زودتر Handshake پیاده سازی کنیم، کارت شبکه وایرلسی ما باید `Injection Mode` را نیز پشتیبانی کند.
- برای استفاده از این ابزار و برنامه باید کارت شبکه قوی و مناسبی مانند Alpha Wireless Card داشته باشیم و با کارت شبکه های معمولی اینکار را نمیتوان بدرستی انجام داد.
- *اسلاید*:
	- ![[Pasted image 20240708172938.png]]
##### Instruction Steps
0. *پیش نیاز ها*
	1. دانلود ابزار از لینک رسمی
		1. https://www.tamos.com/download/main/ca.php
			1. ![[Pasted image 20240708173259.png]]
	2. فایل دانلود شده را Extract میکنیم و سپس آنرا نصب میکنیم.
		1. ![[Pasted image 20240708173337.png]]
1. *نصب ابزار `CommView for Wifi`*
	1. پس از اینکه نصب ابزار تمام شد، صفحه کانفیگ کرا تشبکه وایرلسی باز میشود که اگر کارت شبکه ما مناسب و Compatible و متصل به ویندوز باشد، میتوانیم آنرا در لیست کارت شبکه ها مشاهده کنیم:
		1. ![[Pasted image 20240708173627.png]]
	2. این ابزار بدلیل اینکه ویندوزی است، با کارت شبکه های شرکت `Realtek` سازگاری بهتری دارد، این درحلیست که ماشین های لینوکسی با مدل های `Railink` بهتر کار میکنند.
	3. بنابراین در Drive Configuration Page، کارت شبکه مناسب را انتخاب میکنیم، سپس درایور مربوط را با انتخاب یکی از گزینه ها نصب میکنیم و سپس بر روی `Configure` کلیک میکنیم:
		1. ![[Pasted image 20240708173904.png]]
2. *کار با ابزار `CommView`*
	1. پس از اجرای ابزار، بر روی `play` کلیک میکنیم تا اسکن شبکه های اطراف شروع شود:
		1. ![[Pasted image 20240708174035.png]]
	2. *نکته*: برای اسکن دقیق بهتر است کانال SSID تارگت را بدست بیاوریم و اسکن را فقط بر روی این کانال انجام دهیم. برای اینکار کپچر را `Stop` میکنیم و سپس در *Right Sidebar* از منو `Single Channel Mode` کانال وایرلسی مورد نظر را انتخاب میکنیم و سپس اسکن را مجددا `Start` میکنیم:
		1. ![[Pasted image 20240708174248.png]]
3. *پیاده سازی حمله `Node reassociation attack` و Capturing Handshake ها*
	1. برای این حمله، کارت شبکه وایرلسی باید `Injection Mode` را پشتیبانی کند. برای پیاده سازی این حمله به آدرس زیر میرویم:
	2. `CommView Wifi => Tools menu => Perform Node reassociation attack`
		1. ![[Pasted image 20240708174709.png]]
	3. این حمله تمام دیوایس هایی که به SSID تارگت متصل هستند را مجبور به Disconnect و سپس Connect مجدد میکند تا بتواند در این بین `Handshake` ها را کپچر کند. در واقع این حمله نوعی از `Deauthentication Attack` میباشد.
		1. ![[Pasted image 20240708174644.png]]
	4. اجازه دهید چند دقیقه فرآیند *Capturing* انجام شود، سپس کپچر را `Stop` میکنیم و فایل کپچر شده را با فرمت `cap.` ذخیره میکنیم.
		1. ![[Pasted image 20240708174829.png]]
4. *تبدیل فایل کپچر شده `hash.cap` به فرمت `hc22000.`*
	1. حال باید فایل کپچر شده را با استفاده از وبسایت زیر به فرمت `hc22000.` تبدیل کنیم.
	2. https://hashcat.net/cap2hashcat/
		1. ![[Pasted image 20240708175121.png]]
	3. فایل تبدیل شده را به پوشه Hashcat منتقل میکنیم تا بتوانیم آنرا با hashcat کرک کنیم.
5. *کرک فایل `hash.hc22000` بوسیله `Hashcat`*
	1. دانلود Hashcat و Rockyou و انتقال Rockyou به پوشه Hashcat
		1. ![[Pasted image 20240708175329.png]]
	2. حال Powershell را در پوشه Hashcat باز میکنیم و با استفاده از کامند زیر به کرک فایل میپردازیم:
		1. ![[Pasted image 20240708175459.png]]
	3. `.\Hashcat.exe -m 22000 -a 0 -o cracked.txt hash.hc22000 rockyou.txt`
		1. ![[Pasted image 20240708175558.png]]
6. پسورد شبکه وایرلسی با موفقیت کرک شد.
	1. نتیجه کرک مقدار هش پسورد را در فایل `cracked.txt` میتوان مشاهده کرد.
		1. ![[Pasted image 20240708175654.png]]
#### Practical Demo
0. *Pre-Requires*
	1. Download CommView for Wifi from *99Mb*  https://www.tamos.com/download/main/ca.php
		1. ![[Pasted image 20240708175941.png]]
	2. Download Cracked versions from https://soft98.ir/internet/network/561-commview-wifi.html
	3. Click on Setup.exe file to install CommView Wifi on Windows
		1. ![[Pasted image 20240708180226.png]]
	4. Download Rockyou.txt and copy to Hashcat folder
		1. ![[Pasted image 20240708183340.png]]
1. *Configure Wifi Compatible Drivers*
	1. When click on `Finish`, CommView Automatically start and `Driver Configuration Page` Will be appear automatically 
		1. ![[Pasted image 20240708180345.png]]
	2. Select `i want to test my untested adapter that may be compatible` and then Click on `Next`
		1. ![[Pasted image 20240708180447.png]]
	3. In next page, Select `Adapter`, `Adapter 802.11 Support Status` and `Adapter Provider` base on your Adapter and then Click on `Confgiure`
		1. ![[Pasted image 20240708180643.png]]
	4. in next page, Click on `Close` then `Restart Program & Machine`, Wait a minute or two then CommView Installed Wireless Capturing Drivers. 
		1. ![[Pasted image 20240708180733.png]]
2. *Open CommView and Scan Nearby & Target SSID*
	1. `CommView => Click Play` Start Wifi Scan to detect nearby ssid
		1. ![[Pasted image 20240708180944.png]]
	2. در نسخه رایگان، فقط به مدت 5 دقیقه میتوانیم اسکن شبکه های وایرلسی را انجام دهیم.
		1. ![[Pasted image 20240708181035.png]]
	3. Now Capturing Start and we can see Scan Results
		1. ![[Pasted image 20240708181152.png]]
	4. Copy Channel of Target SSID(*6*) then Play Scan only on this Channel(*6*)
		1. ![[Pasted image 20240708181309.png]]
	5. حال که اسکن را در کانال خاص محدود کردیم، لیست SSID ها و کلاینت هایی که به آن متصل هستند را میتوانیم مشاهده کنیم:
		1. ![[Pasted image 20240708181503.png]]
3. *Established Node Reassociation Attack*
	1. اگر کارت شبکه ما `Injection Mode` را پشتیبانی میکند میتوانیم با پیاده سازی حمله      `Node Reassociation` کلاینت ها را مجبور به Disconnect و سپس Connect مجدد به SSID تارگت کنیم تا بتوانیم سریعتر Handshake های SSID تارگت را Capture کنیم.
	2. در غیر اینصورت و اگر کارت شبکه ما این قابلیت را پشتیبانی نمیکند، باید منتظر شویم تا کلاینتی به SSID متصل شود تا بتوانیم Handshake  آنرا Capture کنیم.
	3. `CommView Wifi => Tools => Node Reassociation `
		1. ![[Pasted image 20240708181637.png]]
	4. پس از گذشت 5 دقیقه زمان اسکن نسخه Trial، اسکن را متوقف میکنیم.
		1. ![[Pasted image 20240708182553.png]]
	5. سپس بر روی `Save` کلیک میکنیم و فایل را با پسوند `cap.` بنام `hash.cap` ذخیره میکنیم:
		1. ![[Pasted image 20240708182723.png]]
4. *Converting `hash.cap` to `hash.hc22000`*
	1. Goto https://hashcat.net/cap2hashcat/ Or Search *Cap 2 Hashcat* in google.
	2. Click on `choose` and select `hash.cap`, then click on `Convert` to convert file to `hash.hc22000`
		1. ![[Pasted image 20240708183127.png]]
	3. After file converted, `Download` it and renamed to `hash.hc22000`
		1. ![[Pasted image 20240708183251.png]]
	4. Now Copy `hash.hc22000` and `rockyou` to Hashcat folder
5. *Cracking `hash.hc22000`*
	1. Open Powershell in Hashcat folder, Run following command to start cracking.
	2. `.\Hashcat.exe -m 22000 -a 0 -o cracked.txt hash.hc22000 rockyou.txt`
		1. ![[Pasted image 20240708183817.png]]
	3. You can see `Status..........Cracked` in terminal which mean cracked successfully done
		1. ![[Pasted image 20240708183916.png]]
6. Cracking Done, now see cracking results
	1. Result Stored in `cracked.txt` in Hashcat folder
		1. ![[Pasted image 20240708184045.png]]
	2. `notepad C:\Downloads\Hashcat\cracked.txt`
----
```powershell
#Cracking Captured Converted file(captured: hash.cap => converted: hash.hc22000)
cd C:\Downloads\Hashcat\
.\Hashcat.exe -m 22000 -a 0 -o cracked.txt hash.hc22000 rockyou.txt
notepad C:\Downloads\Hashcat\cracked.txt #See result
```
##### What is Name of this Anti Virus?
![[Pasted image 20240708183503.png]]

### Automatic Wifi Cracking with `Wifite` - E43
#### Definition & Instruction
##### What is Wifite?
- ابزار Wifite، ابزاری است که برای Capturing و Auditing فایل های رمزنگاری شده WEP, WPA استفاده میشود. این ابزار میتواند از سایر ابزار های Wifi Hacking مانند `aircrack-ng, pyrit, reaver, tshark` برای کرک شبکه وایرلسی بصورت اتوماتیک استفاده کند.
- از ویژگی های این ابزار، Customize کردن بسیار راحت آن بوسیله مقدار دهی چندین پارامتر و Arguments است که میتواند بوسیله انها تمام فرآیند Wifi Hacking را از Capturing تا Cracking را بصورت خودکار انجام دهد.
- همچنین این ابزار میتواند بعضی از حمله ها را بدون نظارت Supervision انجام دهد. 
در واقع هدف ارائه Wifite، کنار گذاشتن سایر ابزار های Wifi Hacking و تجمیع آنها در یک محل است. در واقع Wifite میتواند تمام مراحل wifi Hacking را که توضیح دادیم بصورت خودکار انجام دهد.
- *اسلاید*:
	- ![[Pasted image 20240708193608.png]]
> در این جلسه میخواهیم با استفاده از Automated Tools ها، در واقع Wifite و دیکشنری Rockyou در حمله Dictionary Attack به کرک WPA Encryption بپردازیم.

##### Instruction Steps
0. *پیش نیاز ها*
	1. آماده سازی Rockyou
		1. ![[Pasted image 20240708193941.png]]
1. *اسکن SSID های اطراف*
	1. برای کرک رمزنگاری WPA کامند زیر را اجرا میکنیم.
	2. `wifite --wpa --kill --dict /usr/share/wordlists/rockyou.txt`
		1. ![[Pasted image 20240708194630.png]]
	3. `--wpa` informs we are looking for WPA networks
	4. `--kill` Kill all process may hide with cracking process
	5. `--dict rockyou.txt` Specify Dictionary for using in attack
	6. *Slide* :
		1. ![[Pasted image 20240708194546.png]]
	7. با اجرای کامند، ابزار شروع به اسکن تمام شبکه های وایرلس SSID های اطراف میکند و سپس نیز را لیست میکند. 
	8. حال ما باید اسکن را با `CTRL+C` متوقف کنیم و سپس باید SSID تارگت را با وارد کردن شماره آن انتخاب کنیم:
		1. ![[Pasted image 20240708194942.png]]
	9. همچنین برای انتخاب تمام SSID های اطراف، کاراکتر dash `-` را وارد میکنیم.
2. *کپچر و کرک Handshake شبکه های وایرلسی*
	1. حال ابزار حملاتی را بصورت خودکار برای Capturing Handshake های اطراف پیاده سازی میکند. کافیست `CTRL+C` و سپس `C` را بفشاریم تا این حملات متوقف شوند و Capturing Handshake شروع شود.
		1. ![[Pasted image 20240708195419.png]]
	2. بسته به پلاگین هایی که بای Wifite نصب کردیم، ممکن است نیاز باشد قدم اول را سه الی پنج مرتبه انجام دهیم اما بصورت پیشفرض یکبار و برای رد کردن حمله PMKID Find استفاده میکنیم.
	3. در واقع برای بدست آوردن پسورد شبکه وایرلسی فقط حمله `WPA Handshake Captured` را نیاز داریم:
		1. ![[Pasted image 20240709230131.png]]
	4. حال هنگامیکه Wifite بتواند Handshake را Capture کند، پیامی در ترمینال نشان میدهد که گوینده این است که میخواهد بصورت اتوماتیک به مرحله کرک Handshake با استفاده از Rockyou برود:
		1. ![[Pasted image 20240708195650.png]]
3. شبکه وایرلسی SSID تارگت که با رمزنگاری WPA محافظت میشد، *با موفقیت کرک شد* =>
	1. هنگامیکه ابزار بتواند فایل Handshake را که بصورت اتوماتیک کپچر کرده است را کرک کند، نتیجه کرک را در ترمینال در مقابل فیلد `PSK(Password)` میتوان مشاهده کرد:
		1. ![[Pasted image 20240708195932.png]]
---
```sh
wifite -- wpa --kill --dict /usr/share/wordlists/rockyou.txt
"Select target ssid by enter ssid number"
"CTRL+C" & "C" #Cancel attack to start capturing
"Now wifite automatically Captured target SSID Handshake"
"Then Automatically Start Cracking operation with rockyou.txt in dictionary attack"
```
	![[Pasted image 20240708195247.png]]
#### Practical Demo
0. *Pre-Requires*
	1. Pre-Pare `rockyou.txt`
		1. ![[Pasted image 20240708200943.png]]
	2. also we can use `/usr/share/wordlists/wifite.txt` which is default Wifite Wordlist.
1. *Start Wifite Scan*
	1. wifite list all nearby ssid,s by run following command
	2. `wifite --wpa --kill --dict /usr/share/wordlist/rockyou.txt`
	3. Now Press `CTRL+C` One time and then select `target ssid` by enter `ssid number`
		1. ![[Pasted image 20240708201342.png]]
	4. wifite perform many attacks to Target SSID, but we need only `WPA Handshake Capturing` Attack. so Press `CTRL+C` to Cancel Unnecessary attacks then `C` to continue Other attacks.
		1. ![[Pasted image 20240708201648.png]]
	5. Maybe need `repeat` above step for 3 or 4 times, until  `WPA Handshake Capturing` attack
		1. ![[Pasted image 20240708201755.png]]
2. *Capturing & Cracking Handshake*
	1. after skipping attacks, wifite Start to Capturing handshake and store it in `hs/handshake_ssid....`
		1. ![[Pasted image 20240708202050.png]]
	2. After then, wifite Automatically start Cracking the Captured Handshake using `rockyou.txt` performing in dictionary attack
		1. ![[Pasted image 20240708202143.png]]
	3. When Cracking done, see result of cracked password hashes in `Terminal` in `PSK(password)` field.
		1. ![[Pasted image 20240708202417.png]]
3. Cracking Successfully done with `wifite`
-----
```sh
locate rockyou && gunzip /usr/share/wordlists/rockyou.txt.gz
sudo wifite --wpa --kill --dict /usr/share/wordlists/rockyou.txt
"Now Press CTRL+C some times, then select target ssid by enter ssid number"
```
	![[Pasted image 20240708201131.png]]
### GUI Based Automated Wifi Cracking with `FERN` - E44
#### Definition & Instruction
##### What is FERN?
- ابزار FERN، ابزاری است که برای افزایش امنیت شبکه های وایرلسی و در واقع برای نفوذ به آنها استفاده میشود. این ابزار بوسیله زبان Python توسعه داده شده است، که از Python QT GUI هم برای رابط کاربری خود استفاده میکند.
- این ابزار توانایی شکستن،کرک و بازیابی شبکه های وایرلسی که از رمزنگاری های WEP/WPA/WPS را دارد.
- *اسلاید*:
	- ![[Pasted image 20240709193701.png]]
##### Wifite vs FERN
- Wifite
	- CLI 
	- Support More Attacks
	- More Stable
- FERN
	- GUI
	- Easy to Use
##### Instruction Steps
0. *پیش نیاز ها*
	1. آماده سازی Rockyou.txt 
		1. ![[Pasted image 20240709194117.png]]
		2. ![[Pasted image 20240709194257.png]]
	2. باز کردن FERN در مسیر `Kali Start => Wireless Attacks => FERN`
		1. ![[Pasted image 20240709194431.png]]
1. *کار کردن با FERN و آماده سازی آن برای حمله*
	1. ابتدا باید کارت شبکه ای که میخواهیم شبکه های اطراف را با آن اسکن کنیم را انتخاب میکنیم تا FERN آنرا بصورت خودکار به حالت Monitoring ببرد.
		1. ![[Pasted image 20240709194622.png]]
	2. حال با کلیک بر روی `آیکون Scan` اسکن شبکه های اطراف شروع میشود، ابزار FERN تمام شبکه های WEP و WPA های اطراف را شناسایی میکند و تعداد هر یک را در کنار آن نشان میدهد.
		1. ![[Pasted image 20240709195005.png]]
	3. کافیست `WPA Network` را انتخاب کنیم تا ابزار تمام SSID های اطراف که از رمزنگاری WEP/WPA2 استفاده میکند را لیست میکند.
		1. ![[Pasted image 20240709195220.png]]
	4. حال باید دیکشنری را به ابزار معرفی کنیم. برای اینکار به `Dictionary Tab` میرویم و سپس بر روی `Browse` کلیک میکنیم و سپس هم `Rockyou.txt` را انتخاب میکنیم.
		1. ![[Pasted image 20240709195340.png]]
2. *انجام حمله با FERN*
	1. حال کافیست در پنجره باز شده `SSID Traget` را انتخاب کنیم و سپس تیک گزینه `Automated` را بزنیم و در آخر بر روی `Attack` کلیک کنیم.
		1. ![[Pasted image 20240709195622.png]]
	2. با کلیک بر روی Attack ابزار FERN بصورت خودکار >>
		1. ابتدا حمله `Disassosiation Attack` را انجام میدهد تا کلاینت ها Disconnect و Connect شوند.
		2. حال میتواند Handshake شبکه SSID تارگت را Capture کند.
		3. سپس هم به کرک مقدار Hash پسورد درون فایل کپچر شده میپردازد.
		4. *اسلاید*:
			1. ![[Pasted image 20240709195910.png]]
3. کرک شبکه وایرلسی تارگت با موفقیت انجام شد و نتیجه کرک را در صفحه اصلی ابزار در Key Database میتوانیم مشاهده کنیم.
	1. ![[Pasted image 20240709235757.png]]
##### FERN Toolbox
ابزار FERN، جعبه ابزاری درون خود دارد که شامل ابزار های زیر است >>
1. Geolocators Tracker
2. Cookie Hijacker
3. Ray Fusion(HTTP, Telnet and FTP Bruteforcer) *Recommended*
	1. ![[Pasted image 20240710000312.png]]
4. Font Settings
5. Wifi attack options
6. Screenshot
	1. ![[Pasted image 20240710000127.png]]
> یکی از بهترین این ابزار ها Ray Fusion است که میتوانیم از آن برای پیاده سازی حملات Bruteforce بر روی  پروتکل های FTP, Telnet, HTTP, HTTPS میباشد.
#### Practical Demo
0. *Pre-Requires*
	1. Prepare Rockyou
		1. ![[Pasted image 20240709200137.png]]
	2. Open FERN from `Kali Start => Wireless Attacks => FERN`
		1. ![[Pasted image 20240709200225.png]]
1. *Scan Nearby SSID and Start Attack with FERN*
	1. First `Select Wireless Adapter`, FERN Set it Automatically on Monitor Mode
		1. ![[Pasted image 20240709200356.png]]
	2. Second `Click on Scan` Icon, To start Scan
		1. ![[Pasted image 20240709200516.png]]
	3. Now *FERN List all WPA and WEP Networks* in nearby and we can see network counts in front of WPA or WEP Icons
		1. ![[Pasted image 20240709200645.png]]
	4. Third `Click on WPA` Icon, To open WPA Attacks Page.
	5. Fourth `Click on Browse` and select `Rockyou.txt` for using in Attack.
		1. ![[Pasted image 20240709200842.png]]
	6. Sixth `Select Target SSID` and then `Checked Automate` and then `Click on WPA Attack` 
		1. ![[Pasted image 20240709201011.png]]
2. *Now Fern Start Attack and Automatically do above steps*
	1. First Established a `Disassociation Attack`
	2. Then `Capture Handshakes`
	3. Then `Crack hashes` in Handshake in Dictionary Attack using Rockyou
	4. *Slide*:
		1. ![[Pasted image 20240709201313.png]]
	5. When FERN Crack handshake show password on screen
		1. ![[Pasted image 20240709201349.png]]
	6. Also store cracked hashes in `Key Database` in Main page of software
		1. ![[Pasted image 20240710001016.png]]
3. Cracking Done
### !