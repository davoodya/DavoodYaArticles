---
Episode: E0 to E6
Date: 2024-06-25
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
Pervious Episode: "[[E8, E9 - Password Cracking]]"
Next Episode: "[[E7 to E15 - (Bypassing & Resetting Windows Password)]]"
---
-------
#CyberSecurity #hacking 
## E0 to E7- Introduction & Installation Kali Linux
- [Course Briefly Description](#Course%20Briefly%20Description)
- [Install Kali Linux Ways](#Install%20Kali%20Linux%20Ways)
	- [Kali Linux Live Disk on VMWare](#Kali%20Linux%20Live%20Disk%20on%20VMWare)
	- [Kali Linux as a Bootable USB Drive](#Kali%20Linux%20as%20a%20Bootable%20USB%20Drive)
		- [Instruction](#Instruction)
		- [Demo](#Demo)
	- [Kali Linux in AWS with GUI](#Kali%20Linux%20in%20AWS%20with%20GUI)
		- [Instruction & Definitions](#Instruction%20&%20Definitions)
			- [AWS Basics](#AWS%20Basics)
			- [Install Kali on AWS](#Install%20Kali%20on%20AWS)
			- [Install Requirement Tools on Kali Instance](#Install%20Requirement%20Tools%20on%20Kali%20Instance)
			- [Established VNC Connection](#Established%20VNC%20Connection)
		- [Practical Demo](#Practical%20Demo)
	- [Pre-Built Kali Linux in VMWare](#Pre-Built%20Kali%20Linux%20in%20VMWare)
		- [Instruction & Definitions](#Instruction%20&%20Definitions)
		- [Demo](#Demo)
-----
### Course Briefly Description
1. در این دوره روش های دسترسی به یک ماشین را بطور هدفمند یاد خواهیم گرفت.
2. کرک پسورد ها را یاد خواهیم گرفت.
3. شکستن پسورد و کرک فایل های Word, Rar, Power Point Excel , ....
4. همچنین هک شبکه های وایرلسی را نیز خواهیم آموخت.
5. با بهترین ابزار های هک در دنیا کار خواهیم کرد.
6. *تصویر*
	1. ![[Pasted image 20240625162805.png]]
7. مدارکی که مدرس دوره دارد:
	1. ![[Pasted image 20240625163346.png]]
### Install Kali Linux Ways
#### Kali Linux Live Disk on VMWare
1. Download VMWare Workstation Pro or VMWare Player(Free version) or Virtual Box
2. Download Kali Live CD
	1. مزیت یا عیب استفاده از این نسخه در این است که هر بار ماشین را ریست میکنیم تمام اطلاعات(State) ماشین حذف و ریست میشود که این امکان در تست بسیار مفید است.
	2. همچنین میتوانیم نسخه *ISO* و یا نسخه مخصوص ماشین مجازی را هم دانلود و نصب کنیم.
	3. پیشنهاد میشود بر روی VMWare نسخه 32 بیتی کالی را نصب کنید.
3. Create new virtual machine
	1. Select `Kali2023.3-x86.iso` 
	2. in version selected wizard select `Ubuntu` for 32bit installation and select `Ubuntu 64` for 64bit installation
		1. ![[Pasted image 20240625164355.png]]
	3. Install on Multiple storage for more speed.
4. Kali Hardware Configures
	1. Memory: 2Gb
	2. if don't select iso file in installation wizard, Select ISO file in CD/DVD section
		1. ![[Pasted image 20240625164829.png]]
	3. Network: Bridged
		1. در این حالت کارت شبکه ماشین بصورت مستقل و جدا از کارت شبکه هاست اصلی کار میکند .
		2. در واقع کارت شبکه Kali آیپی مجزا از رنج شبکه و هاست اصلی هم آیپی مجزا از رنج همان شبکه دارد.
5. Power On Machine and in Live CD Boot Menu 
	1. Select `Live System(686-pae)` or `Live System(686-pae fail-safe mode)` to Start live kali OS
		1. ![[Pasted image 20240625165040.png]]
6. Now Check machine IPs `ifconfig`
	1. ![[Pasted image 20240625165250.png]]
#### Kali Linux as a Bootable USB Drive
##### Instruction
میتواینیم کالی لینوکس را بر روی حافظه فلش بصورت Bootable منتقل کنیم و سپس از آن فلش برای نصب Kali استفاده کنیم:
1. *Tools Needed*
	1. Kali Linux ISO
	2. Rufus or Ventoy for Create Bootable flash disk
2. Download 2 above tools
3. in Rufus for Kali 32bit installation iso file
	1. بدلیل اینکه ممکن است ماشین تارگت قدیمی باشد بهتر است در اینجا از فرمت های قدیمی `MBR` بر روی `Bios or UEFI` استفاده کنیم. همچنین دیسک USB را در Fat32 با `Cluster Size 8192` فرمت میکنیم.
		1. ![[Pasted image 20240625165754.png]]
4. Plugin in USB to machine and reboot machine to boot with USB
5. *Note:* Disable `Secure Boot` from `Bios Settings` 
	1. برای اینکه ماشین جدید بتواند این فلش را خواند باید `Secure Boot` را تنظیمات `Bios` ماشین جدید غیر فعال کنیم تا بتوانیم دیوایس Bootable با فرمت `Mbr` را به ماشین جدید هم متصل کنیم.
##### Demo
1. Download Live Boot Kali x86 Linux File 
	1. ![[Pasted image 20240625170641.png]]
2. Download Rufus
3. Open Rufus
	1. Select USB Drive
	2. Select Kali Linux iso file
	3. Select `MBR` as Partition scheme
	4. Select `Bios or UEFI` as Target systems
	5. File System `Fat32` on `8192 bytes` Cluster sizes
	6. `Start`
		1. ![[Pasted image 20240625171002.png]]
4. Connect USB Drive to Machine
	1. Reset machine and press `ESC` or `F12` or `DEL` to enter boot menu
	2. Select USB Disk(Removable Drive) in Boot Menu and booting machine on USB Disk
	3. Select `Live System(686-pae)` or `Live System(686-pae fail-safe mode)` in *Kali Linux Live Menu* 
		1. ![[Pasted image 20240625171239.png]]
#### Kali Linux in AWS with GUI
##### Instruction & Definitions
###### AWS Basics
از سرویس ابری آمازون برای دازش های ابری استفاده میشود. نصب و راه اندازی و استفاده از ماشین های مجازی هم جز سرویس های معروف AWS است.
آمازون AWS یک طرح رایگان `Free Tier`  بنام `EC2` دارد که در آن میتوانیم یک ماشین مجازی را در Cloud AWS به مدت 12 ماه بصورت کاملا رایگان نگهداری و استفاده کنیم. برای استفاده از این طرح نیاز است که اطلاعات کارت اعتباری را وارد کنید اما هزینه در بر ندارد.
	![[Pasted image 20240625171841.png]]
در ایران بدلیل اینکه استفاده از AWS دشوار است میتوانیم از سایر هاست ها و شرکت هایی که هاست ارئه میدهند استفاده کنیم.
*داشتن ماشین Kali در Cloud مزیت های زیادی دارد >>*
1. پیاده سازی حملات از راه دور بصورت Remote
2. محافظت از Location اصلی و لو نرفتن آن
> هنگامیکه ماشین Kali را در Cloud نصب میکنیم بصورت CLI نصب میشود و باید بصورت دستی GUI بر روی ماشین Kali نصب شود.
*اهداف این آموزش >>*
1. نصب ماشین Kali در AWS
2. نصب GUI بر روی Kali Aws
	1. ![[Pasted image 20240625172102.png]]
###### Install Kali on AWS
1. Launch EC2 Instance
	1. برای راه اندازی کنسول AWS EC2 برای بالا آوردن ماشین کالی به وبسایت رسمی با آدرس زیر بروید:
	2. https://aws.amazon.com/
		1. ![[Pasted image 20240625172411.png]]
2. Connect to Kali via SSH
	1. `ssh -i "kali2.pm" kali@34.219.54.138`
		1. ![[Pasted image 20240625172526.png]]
	2. از فلگ `i` برای معرفی Private SSH Key استفاده میشود.
###### Install Requirement Tools on Kali Instance
1. Install `XFCE4` Desktop Environment and `tightVNC Server` 
```sh
sudo apt-get install xfce4 xfce4-goodies tightvncserver
sudo apt-get install gnome-core kali-defaults kali-root-login desktop-base
```
	![[Pasted image 20240625172849.png]]
###### Established VNC Connection
1. Setup `tightVNC Server` Geometry(resolution)
```sh
tightvncserver -geometry 1024x728 #x is not *
```
	![[Pasted image 20240625173051.png]]
2. Check VNC Server Running or Not
	1. کامند زیر را اجرا کنید و مطمئن شوید سرویس `xtightvnc` در حال اجراست و بر روی کدام پورت در اینجا 5901 کار میکند.
```sh
netstat -tulpn
```
	![[Pasted image 20240625173310.png]]
3. Download tight VNC Client for Windows
	1. https://www.tightvnc.com/download.php
4. Open VNC Viewer on Windows and connect to VNC Server(Kali on AWS EC2)
	1. *Connect to:*  KALI-IP:PORT => `34.219.54.138:5901`
		1. ![[Pasted image 20240625180211.png]]
###### if VNC Server Got Gray Screen
A gray screen in VNC usually indicates that the VNC server started successfully but the window manager or desktop environment didn't start. This can happen if the VNC server is not properly configured to start a desktop environment.
To fix this issue, you need to ensure that your `xstartup` file in the `~/.vnc` directory is correctly configured to start a desktop environment. Here are the steps to set up your VNC server correctly:

ممکن است در اولین اتصال به VNC Server با صفحه gray Screen مواجه شویم که این مشکل به این دلیل رخ میدهد که Desktop Environemnt با VNC Server اجرا نمیشود. برای رفع این چالش >>
1. Edit the `xstartup` file:
	1. `nano ~/.vnc/xstartup`
2. Modify the `xstartup` file:
	1. Replace the contents of the `xstartup` file with the following lines. This example assumes you want to start the Xfce desktop environment, which is lightweight and commonly used in VNC sessions:
```sh
#!/bin/sh 
unset SESSION_MANAGER 
unset DBUS_SESSION_BUS_ADDRESS 
startxfce4 &
```
3. If you prefer to use a different desktop environment like GNOME or KDE, you can replace `startxfce4` with the appropriate command. For example, for GNOME:
```sh
#for Gnome
#!/bin/sh 
unset SESSION_MANAGER 
unset DBUS_SESSION_BUS_ADDRESS 
gnome-session &

#for KDE
#!/bin/sh 
unset SESSION_MANAGER 
unset DBUS_SESSION_BUS_ADDRESS 
startkde &
```
4. Make the `xstartup` file executable:
	1. `chmod +x ~/.vnc/xstartup`
5. Restart the VNC server:
```sh
vncserver -kill :1 
vncserver -geometry 1440x900 :1
#we can use vncserver instead of tightvncserver command
```
##### Practical Demo
1. `AWS Dashboard => EC2 Dashboard`
	1. در اولین قدم در داشبورد AWS گزینه EC2 را باز میکنیم و یا در قسمت جستجو EC2 را جستجو میکنیم:
		1. ![[Pasted image 20240625180503.png]]
	2. در داشبورد EC2 بر روی EC2 کلیک میکنیم:
		1. ![[Pasted image 20240625180753.png]]
	3. در صفحه باز شده در قسمت *Launch Instance* بر روی `launch instance` کلیک میکنیم.
		1. ![[Pasted image 20240625180854.png]]
2. *Launch new EC2 Instance*
	1. Select name, Tag for Instance
		1. ![[Pasted image 20240625181027.png]]
	2. *Application & ISO Images(Amazon Machine Images)*
		1. Search *Kali*
			1. ![[Pasted image 20240625181233.png]]
		2. Select *Kali Linux* in search results & Click on `Continue`
			1. ![[Pasted image 20240625181307.png]]
		3. Select CPU Architecture
			1. ![[Pasted image 20240625181427.png]]
			2. ![[Pasted image 20240625181618.png]]
		4. *Instance type*
			1. در اینجا نمونه `t2.micro` را انتخاب میکنیم که نسخه رایگان است.
				1. ![[Pasted image 20240625181650.png]]
		5. *Key Pair login*
			1. در ابتدا یک نام `kali2` برای کلید انتخاب میکنیم و سپس بر روی `Create new key pair` کلیک میکنیم.
				1. ![[Pasted image 20240625181813.png]]
			2. سپس در پنجره باز شده name, type, format کلید را برابر مقادیر زیر قرار میدهیم:
				1. Name: `Kali`
				2. Key Pair Type: `RSA`
				3. Private Key File Format: `.pem`
					1. ![[Pasted image 20240625181958.png]]
			3. سپس فایل `kali.pem` که Private Key ماشین است و بصورت خودکار در این مرحله دانلود میشود را در محلی امن ذخیره میکنیم.
		6. *Network Settings*
			1. Main Configure Image
				1. ![[Pasted image 20240625182216.png]]
			2. Allow SSH, HTTP, HTTPS traffics from the internet(anywhere)
				1. ![[Pasted image 20240625182328.png]]
			3. برای افزایش امنیت میتوانیم Allow SSH را برای آیپی های خودمان تنظیم کنیم.
		7. *Configure Storage*
			1. ![[Pasted image 20240625182430.png]]
		8. *Summary* Click on Launch Instance
			1. ![[Pasted image 20240625182527.png]]
	3. After Launch Click on Instance to launch
			1. ![[Pasted image 20240625182740.png]]
3. `EC2 => Instances => Click on Kali Instance =>` Add Firewall rules and then launch Kali 
	1. Kali Instance IPs
		1. ![[Pasted image 20240625182927.png]]
	2. *Security(Firewall) Settings*
		1. in bottom of page go `Security` tab to see *Security Rules* 
			1. ![[Pasted image 20240625183100.png]]
		2. Click on Security Group to add or remove any inbound or outbound rules
			1. ![[Pasted image 20240625183144.png]]
			2. ![[Pasted image 20240625183227.png]]
		3. در اینجا میخواهیم قانونی اضافه کنیم که به تمام ترافیک هایی که از سمت اینترنت می آیند اجازه عبور بدهد. بنابراین به `Inbound Rules => Edit Inbound Rules` میرویم و سپس بر روی `Add Rule` کلیک میکنیم:
			1. ![[Pasted image 20240625183520.png]]
		4. *New Rule Details:*
			1. `All Traffics` from `All Protocols` in `All Ports` from `Anywhere` 
				1. ![[Pasted image 20240625183648.png]]
			2. Click on Save Rules and back to `EC2 Dashboard`
		5. اگر بخواهیم امنیت سرور را بالا ببریم باید در اینجا فقط اجازه عبور ترافیک آیپی های مجاز را صادر کنیم.
4. *Check Connection to Kali*
	1. `EC2 Dashboards => Instances => Click on Kali Instance => ` Copy Kali Instance Public IP Address
		1. ![[Pasted image 20240625184018.png]]
		3. ![[Pasted image 20240625184059.png]]
	2. Ping Kali Instance from local machine `ping 34.219.54.138`
		1. ![[Pasted image 20240625184413.png]]
5. *Established SSH Connection to Kali Instance*
	1. ابتدا به پوشه ای که فایل کلید `kali.pem` را ذخیره کردیم میرویم و Powershell را در آنجا باز میکنیم:
		1. ![[Pasted image 20240625184708.png]]
	2. حال میتوانیم به ماشین کالی بوسیله SSH متصل شویم:
	3. `ssh -i kali.pem kali@34.219.54.138`
		1. ![[Pasted image 20240625184911.png]]
6. *Install Requires Tools on Kali Instance and Run VNC Server*
```sh
sudo apt update && sudo apt upgrade
#Install Desktop Envirnments and VNC Server
sudo apt-get install xfce4 xfce4-goodies tightvncserver
#Install Desktop Environment Requirements
sudo apt-get install gnome-core kali-defaults kali-root-login desktop-base

#Start tightVNC Server Geometry
tightvncserver -geometry 1024x728 # x not *
"""
Enter Server Informations
Select Password & verify that
View Only No
New X Desktop is kali:1
"""
#Check VNC Server Running on port 5901
netstat -tulpn

```
	![[Pasted image 20240625185753.png]]
7. Connect to Kali Instance from Windows Machine
	1. Download *Real VNC Viewer Client* in Windows machine
	2. Enter Kali Instance IP on 5901 port to connect Kali Instance `34.219.54.138:5901`
		1. ![[Pasted image 20240625190016.png]]
	3. Click Continue to accept Unencrypted connection risks
		1. ![[Pasted image 20240625190053.png]]
	4. Enter Password and Click `Ok`
		1. ![[Pasted image 20240625190135.png]]
	5. Now we can connect to Kali Instance Desktop
		1. ![[Pasted image 20240625190158.png]]
	6. we can use Kali Instance Same as Ordinary Kali 
	7. `ifconfig` Check Kali Instance IP Addresses
		1. ![[Pasted image 20240625190256.png]]
#### Pre-Built Kali Linux in VMWare
##### Instruction & Definitions
میتوانیم از نسخه Kali که از پیش آماده شده و مخصوص ماشین مجازی است استفاده کنیم. 
0. Download Pre-Built Kali Linux for VM Edition
	1. https://www.kali.org/get-kali/#kali-virtual-machines
		1. ![[Pasted image 20240625235408.png]]
1. Download VMWare and Open Pre-Built Kali Linux in VMWare
	1. ![[Pasted image 20240625200802.png]]
##### Demo
1. Download Pre-Built Kali Linux based on your Virtual Machine
	1. ![[Pasted image 20240625200927.png]]
2. Now Extracted `.7z` downloaded file
3. `VMWare Workstation => File => New Virtual Machine ` Import Pre-Built Kali
	1. Select kali linux virtual machine file from extracted folder
		1. ![[Pasted image 20240625201253.png]]
	2. Kali Linux Hardware
		1. ![[Pasted image 20240625201528.png]]
	3. Power ON Machine and use this
	4. Default Credential `User: kali, Password: kali`
### !

