+++
tags:
  - CyberSecurity
  - Pentest
Category: Cyber Security
date = '2024-06-20T12:38:14+03:30'
draft = true
title = 'SANS-401.1 Networking and Protocols'
+++

-------
#CyberSecurity #Security
## E2 - Analyze Network Protocols 
- [tcpdump](#tcpdump)
	- [Definitions & Installation](#Definitions%20&%20Installation)
	- [Basic Usages](#Basic%20Usages)
		- [0. tcpdump Flags & Conditions](#0.%20tcpdump%20Flags%20&%20Conditions)
			- [0.1 Flags](#0.1%20Flags)
			- [0.2 Conditions](#0.2%20Conditions)
		- [1. Sniffing Interfaces Traffics `-i`](#1.%20Sniffing%20Interfaces%20Traffics%20%60-i%60)
		- [2. Sniffing FTP Connectivity](#2.%20Sniffing%20FTP%20Connectivity)
		- [3. Sniffing Anonymous FTP by Src](#3.%20Sniffing%20Anonymous%20FTP%20by%20Src)
		- [4. Sniffing Custom Port](#4.%20Sniffing%20Custom%20Port)
----
### Basic & Concepts
- از پروتکل هایی که بیشترین استفاده در شبکه را دارند میتوان به IP , ICMP در لایه سوم و TCP, UDP در لایه چهارم اشاره کرد. 
- اگر بخواهیم این پروتکل ها را بصورت تخصصی آنالیز کنیم و یا داده هایی که در این پروتکل های جابجا میشوند را مشاهده و بررسی کنیم باید از ابزار های خاص بررسی مانند، `tcpdump` در ترمینال و یا `Wireshark` که نسخه GUI دارد استفاده کنیم.
	- ![[Pasted image 20240620165523.png]]
- در واقع بوسیله ابزار هایی مانند `Wireshark` یا `tcpdump` میتوانیم به Sniffing داده های رد و بدل شده بپردازیم.
### tcpdump
#### Definitions & Installation 
یکی از بهترین ابزار هایی که برای شنود داده های شبکه در خط فرمان استفاده میشود `tcpdump` نام دارد. بصورت پیشفرض این ابزار بر روی kali نصب است اما بر روی سایر نسخه ها باید بصورت دستی نصب شود:
```sh
sudo apt update -y && sudo apt upgrade -y
sudo apt install tcpdump
tcpdump --help
```
	![[Pasted image 20240620165923.png]]
#### Basic Usages
##### 0. tcpdump Flags & Conditions
###### 0.1 Flags
0. `tcpdump -h`
	1. ![[Pasted image 20240620170018.png]]
1. `tcpdump -i eth0`
	1. مشخص کردن اینترفیس برای کپچر اطلاعات آن اینترفیس
2. `tcpdump port 23`
	1. مشخص کردن پورت برای کپچر
3. `tcpdump -c 3`
	1. مشخص کردن تعداد پکت هایی که میخواهیم کپچر شود.
4. `tcpdump -X`
	1. جواب Capturing را بصورت ASCI Code(Binary) نشان میدهد:
		1. ![[Pasted image 20240620175636.png]]
5. `tcpdump -a`
	1. با این فلگ Capturing بصورت Anonymous صورت میگرد.
6. 
###### 0.2 Conditions
0. *and, src* `tcpdump port 21 and src 10.10.10.10`  
	1. با استفاده از `and` میتوانیم شرط جدید به دستور اضافه کنیم و با استفاده از `src` میتوانیم مبدا برای Capturing مشخص کنیم.
	2. در مثال بالا، Capturing از بسته های پورت FTP 21 که مبدا آنها 10.10.10.20(ماشین لینوکس) است، صورت میگیرد.
##### 1. Sniffing Interfaces Traffics `-i`
1. میتوانیم یک اینترفیس را به tcpdump معرفی کنیم تا تمام پکت ها و بسته هایی که از آن اینترفیس عبور میکنند توسط این ابزار Capture شود.
2. در هنگام معرفی اینترفیس میتوانیم از اینترفیس مشخص(Ethernet، Wireless، vpn adapters, ...) استفاده کنیم.
3. همچنین با معرفی اینترفیس *loopback* میتوانیم تمام پکت های عبوری از ماشین لینوکسی را Capture کنیم.
```sh
#loopback interface go Listening mode
tcpdump -i lo
```
	![[Pasted image 20240620170629.png]]
حال اگر ترافیکی از این ماشین عبور کند و یا ترافیکی به این ماشین وارد شود، پکت های ترافیک توسط tcpdump بصورت Capture میشوند، ساده ترین روش تولید ترافیک هم پینگ گرفتن یک مقصد خاص است. در واقع اگر در ترمینال جدیدی در ماشین لینوکسی `ping 127.0.0.1 -c 1` را بگیریم میتوانیم مشاهده کنیم که بسته پینگ توسط `tcpdump` کپچر شده است:
	![[Pasted image 20240620171105.png]]
حال اگر بخواهیم بسته کپچر شده را آنالیز کنیم >> 
1. ابتدا بسته Echo Request از ماشین لینوکسی برای 127.0.0.1 ارسال شده است.
2. سپس 127.0.0.1 جواب Echo Replay را با موفقیت برای ماشین لینوکسی میفرستد.
3. اینکاری که آنالیز کردیم یکی از رایج ترین کارهای شبکه است که روزمره به تعداد زیاد انجام میشود.
##### 2. Sniffing FTP Connectivity
در قدم دوم میخواهیم تمام ترافیک های FTP که از ماشین لینوکسی به سمت ماشین ویندوزی ارسال میشود را کپچر کنیم. برای اینکار >>
```sh
#Terminal 1 => Capturing ftp traffics
tcpdump -i eth0 port 21 -c 3

#Terminal 2 => Send FTP traffics from linux to windows
ftp 10.10.10.10
```
	![[Pasted image 20240620174957.png]]
	![[Pasted image 20240620175001.png]]
حال با اجرای خط اول ماشین لینوکسی به حالت FTP Listening میرود، و با اجرای خط دوم هم ترافیک های ftp را از لینوکس برای ویندوز میفرستیم تا تعداد 3 عدد از این پکت های FTP توسط tcpdump کپچر شوند.
- *آنالیز بسته های کپچر شده >>*
	- در بسته اول از ماشین کالی به ویندوز بسته FTP  با فلگ S(Sequence) ارسال میشود.
	- در بسته دوم هم از ماشین کالی به ویندوز بسته FTP  با فلگ S(Sequence) ارسال میشود.
	- در بسته سوم یک بسته ACK کپچر شده که در این بسته در آینده(در بسته های چهارم الی بعد) محتویات Authentication پروتکل قرار میگرد(یوزر و پسورد)
> میتوانیم محتویات کپچر شده را بصورت ASCI Code یا Hexadecimal هم مشاهده کنیم.  اگر بخواهیم همین Capturing بالا را بصورت ASCI Code یا Hexadecimal هم مشاهده کنیم باید >>
```sh
tcpdump -X -i eth0 port 21 -c 4
```
	![[Pasted image 20240620180042.png]]
##### 3. Sniffing Anonymous FTP by Src
میخواهیم بسته های ftp که مبدا آنها 10.10.10.20 یعنی ماشین لینوکسی است و همچنین با یوزر anonymous لاگین میکنند را کپچر کنیم. برای اینکار >>
```sh
tcpdump -a -i eth0 port 21 and src 10.10.10.20
```
حال ماشین لینوکسی به حالت Listening میرود و اگر یوزری به ftp ماشین لینوکسی با یوزر anonymous متصل شود بسته های آن توسط `tcpdump` کپچر میشوند:
```sh
ftp 10.10.10.20
Name: anonymous
Password: #empty
ftp>
```
	![[Pasted image 20240620181147.png]]
*حال در نتایج شنود میتوانیم لاگین anonymous به ftp را مشاهده کنیم. آنالیز این شنود به شرح زیر است:*
1. از بسته اول الی پنجم بسته های ارتباطی پروتکل شنود شده است.
2. در کپچر ششم، بسته ای که در آن یوزر anonymous احراز هویت شده است را مشاهده میکنیم.
3. در کپچر هفتم، بسته ای که در آن پسورد anonymous احراز هویت شده است را که یک رشته خالی است را مشاهده میکنیم. 
4. در کپچر هفتم است که `PASS` را مشاهده میکنیم که به معنای برقراری موفقیت ارتباط میان کلاینت ftp و سرور ftp است.
5. در کپچر بعدی، هم مشاهده میکنیم که یوزر anonymous به پروتکل ftp ماشین لینوکسی با موفقیت لاگین کرده است.
	1. ![[Pasted image 20240620181551.png]]
##### 4. Sniffing Custom Port
برای تولید ترافیک در پورت دلخواه از ابزار net cat(`nc`) استفاده میکنیم.
```sh
#Capturing All Traffics on 313 port
tcpdump -i lo port 313

#Generate traffics on 313 port
nc 127.0.0.1 333
```
	![[Pasted image 20240620182037.png]]
*آنالیز این کپچر به شرح زیر است:*
1. در اولین کپچر بسته tcp را با فلگ `S` Sequence که از سمت ماشین لینوکسی به سمت 127.0.0.1:333 ارسال شده است. بسته ای که با فلگ `S` ارسال میشود به معنای این است که Three Way Handshake بین این دو مبدا و مقصد در حال برقراری است.
2. در کپچر دوم مشاهده میکنیم که بسته TCP با فلگ `R` Reset از سمت 127.0.0.1:333 به سمت ماشین لینوکسی ارسال شده است. فلگ `R` نشان میدهد که Three Way Handshake بین مبدا و مقصد برقرار نشده است و به مراتب کانکشن TCP هم Reset شده است.
	![[Pasted image 20240620182614.png]]
### !