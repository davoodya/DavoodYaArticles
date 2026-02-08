---
Episode: E58 to E61
Date: 2024-07-19
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
Pervious Episode: "[[E55 to E57 - (Setup Try Hack Me & SMB, Telnet, FTP Exploitation)]]"
Next Episode: "[[E62 to E63 - (Host & Subdomain Enumeration)]]"
---
-------
## E58 to E61 - (Setup Hack The Box & Hack Some Machines)
- [Setup HTB & Hacking Meow Machine - E58](#Setup%20HTB%20&%20Hacking%20Meow%20Machine%20-%20E58)
	- [Definition & Instruction](#Definition%20&%20Instruction)
		- [What is Hack the Box?](#What%20is%20Hack%20the%20Box?)
		- [Setup HTB Instruction](#Setup%20HTB%20Instruction)
	- [Practical Demo(Hack Meow Machine)](#Practical%20Demo(Hack%20Meow%20Machine))
		- [Start Meow](#Start%20Meow)
		- [Established Connection Between Kali-VM & Meow using OVPN](#Established%20Connection%20Between%20Kali-VM%20&%20Meow%20using%20OVPN)
		- [Gathering Info from Meow](#Gathering%20Info%20from%20Meow)
		- [Meow Q & A](#Meow%20Q%20&%20A)
- [Practical Pentesting Hacking(Fawn Machine) - E59](#Practical%20Pentesting%20Hacking(Fawn%20Machine)%20-%20E59)
	- [Connect to Fawn Playground](#Connect%20to%20Fawn%20Playground)
	- [Hack Fawn Machine](#Hack%20Fawn%20Machine)
- [Practical Pentesting Hacking(Dancing Machine) - E60](#Practical%20Pentesting%20Hacking(Dancing%20Machine)%20-%20E60)
	- [Connect to Dancing Machine](#Connect%20to%20Dancing%20Machine)
	- [Hack Dancing Machine](#Hack%20Dancing%20Machine)
- [Practical Pentesting Hacking(Redeemer Machine) - E61](#Practical%20Pentesting%20Hacking(Redeemer%20Machine)%20-%20E61)
	- [Connect to Redeemer Machine](#Connect%20to%20Redeemer%20Machine)
	- [Hack Redeemer Machine](#Hack%20Redeemer%20Machine)
*****
### Setup HTB & Hacking Meow Machine - E58
#### Definition & Instruction
##### What is Hack the Box?
- پلتفرم Hack the Box، پلتفرمی بزرگ برای انجام تمارین سایبری، امنیتی و هک است. 
- سرویس HTB مناسب کارمندان ارگان ها، کمپانی ها و دانشگاه ها و در کل هر شخصی که میخواهد مهارت های امنیتی خود را افزایش دهد مناسب است.
- پلتفرم HTB یکی از بزرگترین پلتفرم های انجام تمارین سایبری میباشد.
- *اسلاید*:
	![[Pasted image 20240718150041.png]]
##### Setup HTB Instruction
1. goto https://www.hackthebox.com/ and Sign Up
2. Pre-Pare Kali machine
3. Download VPN, Connect to Playground for hacking
	1. ![[Pasted image 20240718150636.png]]
4. Now goto Practical Demo section to hack some machines.
#### Practical Demo(Hack Meow Machine)
##### Start Meow 
1. goto https://app.hackthebox.com/home, then click `Starting Point`
	1. ![[Pasted image 20240718150817.png]]
2. Now Select Zero Tier Machine in Named `Meow` and Click on `Starting Point`
	1. ![[Pasted image 20240718151112.png]]
##### Established Connection Between Kali-VM & Meow using OVPN
3. in Split Windows `Download VPN` (OVPN Profile)
	1. ![[Pasted image 20240718151241.png]]
	2. ![[Pasted image 20240718151243.png]]
4. Now in Kali Linux open terminal in downloaded folder and Connect to VPN Server by run following commands
	1. `sudo openvpn DOWNLOADED-OVPN-PATH.ovpn`
		1. ![[Pasted image 20240718151534.png]]
	2. After Connect to Server, go back to Meow HTB Page, and click on `Starting Point` to see Online Client Status
	3. در واقع پس از اینکه به سرور OVPN متصل شدیم با بازگشت به این صفحه و مشاهده وضعیت آنلاینت کلاینت میتوانیم از این اتصال اطمینان حاصل کنیم.
		1. ![[Pasted image 20240718151754.png]]
	4. همچنین برای حاصل کردن اطمینان از صحت اتصال به سرور OVPN، در ماشین Kali میتوانیم از کامند ifconfig استفاده کنیم. در واقع باید اینترفیس tun0 با آیپی از رنج 10.10.x.x را دریافت کرده باشد.
	5. `ifconfig`
		1. ![[Pasted image 20240718152120.png]]
5. Back to Meow page and Click on `Spawn Machine`
	1. ![[Pasted image 20240718151902.png]]
6. Now Machine Started, Copy machine IP and ping it from kali linux to Check Connection status.
	1. ![[Pasted image 20240718152224.png]]
##### Gathering Info from Meow
1. *Scanning Meow machine*
	1. *Port, OS-Services Scanning* `nmap -T5 -A -p- -v --min-rate=500 10.129.187.71`
		1. ![[Pasted image 20240718155356.png]]
	2. در اسکن مشاهده کردیم که پورت 23 Telnet باز است، در نتیجه در مرحله بعدی باید سعی کنیم که بوسیله Telnet به ماشین تارگت متصل شویم.
2. *Connect to Meow using `telnet`*
	1. `telnet 10.129.187.71 ` login with `root` and `Blank Password`
		1. ![[Pasted image 20240718155938.png]]
	2. باید امتحان کنیم که یوزر root با چه پسوردی میتواند به ماشین Meow متصل شود. در ابتدا پسورد را خالی میگذاریم و امتحان میکنیم و مشاهده میکنیم که میتوانیم به ماشین تارگت لاگین کنیم.
	3. البته اگر پسورد را بدرستی حدس نزدیم، میتوانیم از ابزار های Telnet Bruteforce استفاده کنیم. 
	4. مثلا Ophcrack ابزاری درونی بنام `Ray Fusion` دارد که برای پیاده سازی حملات Bruteforce بر روی پروتکل های ftp و telnet است.
3. *Find Meow Flags*
	1. پس از متصل شدن به ماشین Meow بر بستر telnet میتوانیم انواع کامند ها را در ماشین تارگت اجرا کنیم. کافیست لیست فایل ها را بگیریم تا `flag.txt` را مشاهده کنیم:
	2. `ls`
		1. ![[Pasted image 20240718160115.png]]
	3. `cat flag.txt`
		1. ![[Pasted image 20240718160202.png]]
	4. مقدار فلگ را کپی میکنیم تا در جواب سوال آخر آزمایشگاه وارد کنیم.
##### Meow Q & A
1. what does the acronym *VM* stand for? `virtual machine`
2. what too to interact with operation system? its also known as shell or console? `terminal`
3. What Service we used for connect to HTB labs? `openvpn`
4. Whats name for a Tunnel Interface use for connection between kali and meow? `tun0`
5. Whats tool use test our connection? `ping`
6. Whats name of most common tool for finding Open Ports? `nmap`
7. Whats services do we identify on port 23/tcp during scan? `telnet`
8. What Username is able to log into target over telnet with Blank Password? `root`
9. Enter Flag Content, in `flag.txt` in Meow machine.
### Practical Pentesting Hacking(Fawn Machine) - E59
#### Connect to Fawn Playground
در این جلسه میخواهیم یک عملیات FTP Exploitation را در آزمایشگاه بنام Fawn در HTB انجام دهیم. ابتدا باید به Machine در HTB متصل شویم.
1. Connect to Fawn Machine
	1. Click on `Connect to HTB`
		1. ![[Pasted image 20240718202154.png]]
	2. Download OVPN Configuration file
		1. ![[Pasted image 20240718202253.png]]
	3. Open terminal in ovpn path and run following command to connect to HTB Playground
	4. `sudo openvpn OVPNNAME.ovpn`
		1. ![[Pasted image 20240718202533.png]]
	5. Run `ifconfig` and `tun0` should be added
2. Now go back to Fawn Machine Page and `Spawn Machine`
	1. ![[Pasted image 20240718202840.png]]
3. After Machine turned on, Copy `Target Machine IP` and back to Kali linux to check connection between kali and Fawn by `ping FAWNIP` in Kali machine.
	1. `ping 20.129.187.71`
		1. ![[Pasted image 20240718203103.png]]
		2. ![[Pasted image 20240718203751.png]]
#### Hack Fawn Machine
0. *Scanning Target machine*
	1. a Quick OS/Services & Port Scanning on verbose mode =>
	2. `sudo nmap -T5 -A -p- -v --min-rate=500 10.129.187.71`
		1. ![[Pasted image 20240718203327.png]]
	3. در نتیجه اسکن متوجه میشویم که پورت `21/tcp` که مربوط به سرویس `FTP` است، در ماشین تارگت باز است.
	4. همچنین متوجه شدیم که سرویس `vsftpd 3.0.3` بر روی ماشین تارگت فعال است و در حال خدمت رسانی است.
		1. ![[Pasted image 20240718204051.png]]
	5. همچنین نوع سیستم عامل ماشین تارگت `Unix` است.
1. *Connect to Target on FTP*
	1. حال باید سعی کنیم که بر بستر FTP به ماشین تارگت متصل شویم. در اولین اتصال سعی میکنیم با `anonymous` به سرویس متصل شویم >>
	2. `ftp 10.129.187.71` => Username: `anonymous`, Password Blank
		1. ![[Pasted image 20240718204556.png]]
	3. *نکته*: کد Status Code لاگین موفق به سرویس FTP مقدار `230` و Status Code پیام وارد کردن Password هم `331` میباشد:
		1. ![[Pasted image 20240720223510.png]]
	4. حال با موفقیت به ماشین تارگت با پروتکل FTP متصل شدیم و میتوانیم تمام کامند های سرویس FTP را بر روی ماشین تارگت اجرا کنیم.
	1. `ls` , `dir` 
		1. ![[Pasted image 20240718204731.png]]
	5. با اجرای `ls` متوجه میشویم که فایل `flag.txt` در ماشین تارگت را یافتیم. حال کافیست فایل را باز کنیم تا مقدار فلگ را بدست بیاوریم، بنابراین فلگ را دانلود میکنیم تا آنرا باز کنیم:
	6. `ftp> get flag.txt`
		1. ![[Pasted image 20240718205358.png]]
2. *Fawn Machine Q & A*
	1. What does the 3-letter acronym FTP Stand for? `File Transfer Protocol`
	2. FTP Port? `21`
	3. Whats Acronym of Secure version of ftp? `sftp`
	4. Whats command we use to send ICMP echo request to test connection? `ping`
	5. From your scan, what FTP version running on target machine? `vsftp 3.0.3`
	6. From your scan, What OS Type is running on target machine? `Unix`
		1. ![[Pasted image 20240718204147.png]]
	7. What command we need to run ftp command Help? `ftp -h`
	8. What Username we used over ftp to Logged in without account? `anonymous`
	9. What is Response Code we get for FTP Message Login Successful? `230`
	10. Couple Commands to list files on the FTP Server? `ls`
	11. What is the command used to download file we found on FTP Server? `get`
	12. Submit root flag 🚩 
3. Fawn has been `Pwned`
	1. ![[Pasted image 20240718205613.png]]
----
```sh
sudo nmap -T5 -A -p- -v --min-rate=500 10.129.187.71
ftp 10.129.187.71
"Login with anonymous & Blank password"
ftp> dir
ftp> ls
ftp> get flag.txt
ftp> exit
ls ; cat flag.txt #Copy flag value
```
### Practical Pentesting Hacking(Dancing Machine) - E60
#### Connect to Dancing Machine
0. Download OpenVPN Configuration
	1. ![[Pasted image 20240719162447.png]]
1. Open Terminal in downloaded folder and run following command to connect to Open VPN Server
	1. `sudo openvpn starting_point_davoodya.ovpn`
	2. `ifconfig` Now *tun0* added to interfaces list in Kali machine
2. Back to Dancing Machine page and `Spawn Machine`
	1. `ping DANCING-IP` from Kali => `ping 10.129.83.231` 
	2. ICMP echo replay should be received from Dancing Machine
#### Hack Dancing Machine
0. *Scanning Dancing Machine*
	1. `sudo nmap -T5 -A -p- -v 10.129.83.231`
	2. *Scanning Results*
		1. سرویس microsoft-ds بر روی `tcp/445 , tcp/135 , tcp/139` فعال است که پورت `tcp/445` مربوط به پروتکل `SMB` در ماشین تارگت باز و قابل دسترسی است، در نتیجه میتوانیم بوسیله `smbclient` به ماشین تارگت متصل شویم.
			1. ![[Pasted image 20240719164618.png]]
1. *Connect to Dancing Machine via SMB*
	1. `smbclient -L 10.129.83.231` leave Password Blank
		1. ![[Pasted image 20240719164828.png]]
	2. با این کامند تمام محتویات Share شده در شبکه لیست میشوند و پس از آن میتوانیم به هر Share که میخواهیم متصل شویم.
	3. `smbclient //10.129.83.231/WorkShares` leave Password Blank
		1. ![[Pasted image 20240719165130.png]]
	4. با اجرای کامند بالا به `WorkShares` دسترسی پیدا میکنیم و میتوانیم کامندهای smb را بر روی ماشین تارگت اجرا کنیم.
		1. `smb: \> ls`
			1. ![[Pasted image 20240719165410.png]]
2. *Find Dancing Machine Flags*
	1. حال که به Dancing Machine دسترسی گرفته ایم و میتوانیم کامند های SMB را در ماشین تارگت اجرا کنیم باید فلگ های این ماشین را پیدا کنیم. با اجرای `ls` دیدیم که دو دایرکتوری در ماشین تارگت وجود دارد بنابراین باید به تک انها برویم تا فلگ را پیدا کنیم.
	2. `smb: \> cd James.P` & `smb: \> ls`
		1. ![[Pasted image 20240719165800.png]]
	3. فایل فلگ در دایرکتوری `James.P` یافت شد و حال میتوانیم آنرا دانلود کنیم.
	4. `get flag.txt`
		1. ![[Pasted image 20240719165930.png]]
	5. حال به ماشین Kali باز میگردیم و فایل فلگ را با کامند `cat flag.txt` باز میکنیم و سپس مقدار فلگ را کپی میکنیم تا در جواب سوال وارد کنیم.
		1. ![[Pasted image 20240719170024.png]]
3. *Dancing Machine Q & A*
	1. SMB stand for? `server message block`
	2. What Port SMB use it? `445`
	3. Whats service name running on port 445 base on your nmap scan? `microsoft-ds`
	4. Whats the flag we can use with SMB tool to list the Share contents? `-L`
	5. How many share on dancing? `4`
	6. Whats the name of share we are access in the end with blank password? `WorkSahres`
	7. Whats Command we can use to download file from SMB Server? `get`
	8. Submit Flag 1 value in flag1.txt 
		1. ![[Pasted image 20240719170128.png]]
*****
```sh
sudo nmap -T5 -A -p- -v --min-rate=500 10.129.83.231
smbclient -L 10.129.83.231
smbclient //10.129.83.231/WorkShares
smb: \> ls

```
### Practical Pentesting Hacking(Redeemer Machine) - E61
#### Connect to Redeemer Machine
0. goto https://apphackthebox.com/starting-point and Redeemer Section. then Click `Connect to HTB`
	1. ![[Pasted image 20240719170555.png]]
1. Choose OpenVPN and Download OpenVPN Configuration
	1. ![[Pasted image 20240719170716.png]]
2. Open Terminal in downloaded folder and run following command to connect to Open VPN Server
	1. `sudo openvpn starting_point_davoodya.ovpn`
	2. `ifconfig` Now *tun0* added to interfaces list in Kali machine
3. Back to Redeemer Machine page and `Spawn Machine`
	1. `ping REDEEMER-IP` from Kali => `ping 10.129.236.86` 
	2. ICMP echo replay should be received from Redeemer Machine 
#### Hack Redeemer Machine
0. *Scanning Redeemer Machine*
	1. `sudo nmap -T5 -A -p- -v --min-rate=500 10.129.236.86`
	2. *Scanning Results*
		1. در نتیجه اسکن میبینیم که پورت `6379/tcp` که مربوط به سرویس `Redis 5.0.7` بر روی ماشین تارگت فعال است.
			1. ![[Pasted image 20240719171602.png]]
		2. سرویس Redis یک دیتابیس In-Memory Database است که پردازش داده در این مدل از دیتابیس با مدل معمول متفاوت است. 
1. *Work with Redis*
	1. برای کارکردن با Redis Server از ابزار `redis-cli` استفاده میکنیم که در ابتدا باید بر روی ماشین نصب شود. برای نصب باید پکیج `redis-tools` را بر روی ماشین نصب کنیم.
	2. `sudo apt update ; sudo apt install redis-tools`
	3. `redis-cli -h` Check installation and utility FLAGS
		1. ![[Pasted image 20240719172636.png]]
2. *Connect to Redis Server on Redeemer Machine*
	1. حال که باید متصل شدن به دیتابیس موجود در ماشین تارگت را امتحان کنیم. 
	2. `redis-cli -h 10.129.236.86`
	3. حال با اتصال به دیتابیس Redis میتوانیم کامندهای داخلی Redis را اجرا کنیم >>
	1. `10.129.236.86:6379> INFO` Obtain all information and statistics about Redis Server
	2. `10.129.236.86:6379> select 0` Select Record 0 in Database
		1. ![[Pasted image 20240719181650.png]]
	3. حال که رکورد خاصی را Select کردیم میتوانیم با استفاده از کامند `keys` کلید های Index 0 انتخاب شده را مشاهده کنیم.
	4. `10.129.236.86:6379> keys *` List all keys in *INDEX 0*
		1. ![[Pasted image 20240719182117.png]]
	5. در کل از کامند `* keys` برای لیست کردن تمامی کلید های درون دیتابیس استفاده میشود اما اگر قبل از آن ایندکس مشخصی را انتخاب کرده باشیم تمام کلید های ایندکس انتخاب شده را نشان میدهد.
3. *Get Redeemer Machine Flag*
	1. هنگامیکه کلید های *Index 0* را لیست کردیم، کلیدی بنام `flag` مشاهده کردیم که برای بدست آوردن فلگ مرحله کافیست رکورد بنام `flag` را در دیتابیس Redis که به آن دسترسی گرفته ایم را با استفاده از کامند زیر واکشی کنیم.
		1. ![[Pasted image 20240721000208.png]]
	2. `10.129.236.86:6379> get flag`
		1. ![[Pasted image 20240719182833.png]]
	3. حال کافیست مقدار فلگ را کپی کنیم تا در جواب آخرین سوال Redeemer Machine وارد کنیم.
4. *Redeemer Machine Q & A*
	1. What TCP port open in target machine? `6379`
	2. What service running on this port ? `redis`
	3. What type of Database is Redis? `In-Memory Database`
	4. Which command line utility to interact with Redis Server? `redis-cli`
	5. Which flag used in redis command to specify the host name? `-h`
	6. Once connect to redis server, which Command we use to obtaining information and Statistics about the Redis server? `info`
	7. Whats Version of Redis Server used in target machine? `5.0.7`
	8. Which command we use to select desire database in Redis? `select`
	9. How many key are present inside the database with index 0? `4`
	10. Which command used to list All Keys in Database? `keys *`
	11. Get Flag of Redeemer machine
		1. ![[Pasted image 20240719183123.png]]
*****
```sh
sudo nmap -T5 -A -p- -v --min-rate=500 10.129.236.86
sudo apt update ; sudo apt install redis-tools
redis-cli -h
redis-cli -h 10.129.236.86

10.129.236.86:6379> INFO
10.129.236.86:6379> select 0
10.129.236.86:6379> keys *
10.129.236.86:6379> get flag
```
### !