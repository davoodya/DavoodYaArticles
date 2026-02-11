+++
# Basics
title = "راه اندازی شبکه ویندوز"
slug = "windows-networking"
date = "2024-03-25T15:41:10+03:30"
lastmod = "2026-02-09T15:41:10+03:30"
draft = false

# Taxonomies
categories = ["Network", "Windows"]
tags = ["Network", "Windows", "Network+"]
series = ["Network"]

# Badges and Filters
readingTime = 6
difficulty = "medium" # beginner | medium | intermediate | advanced
lab_required = true 
post_type_fa = "آموزشی" # "آموزشی" | "مقاله" | "اسکریپت" | "خبر" | "دستور العمل" | "معرفی" | "ابزار"

# Options
toc = true
math = false
type = "posts"
# layout = "single"

# Images
featured_image = "/images/network/WindowsNetworking-1.png"
images = ["/images/network/WindowsNetworking-1.png"]

# SEO
description = "1. Connect to Windows together 1. Set IP 2. Set Network On Private Enable File Printer Sharing & Network Discovery 3. Create User for sharing + Set..."
keywords = ["Windows Networking", "network", "Windows-Network-Configuration"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/network/windows-networking/"


[params.opengraph]
  title = "Windows Networking"
  description = "1. Connect to Windows together 1. Set IP 2. Set Network On Private Enable File Printer Sharing & Network Discovery 3. Create User for sharing + Set..."
  image = "/images/network/WindowsNetworking-1.png"
  url = "https://davoodya.ir/network/windows-networking/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Windows Networking"
  description = "1. Connect to Windows together 1. Set IP 2. Set Network On Private Enable File Printer Sharing & Network Discovery 3. Create User for sharing + Set..."
  image = "/images/network/WindowsNetworking-1.png"

+++
-----
### Connect Windows Machines Together - Step by Step
#### Briefly Description
1. Connect to Windows together
	1. Set IP
	2. Set Network On Private Enable File Printer Sharing & Network Discovery 
	3. Create User for sharing + Set Permissions
	4. Create Share Folder
	5. Add File Sharing and Network Discovery to Allow App Features through Windows Firewall
#### Complete and Described Step by Steps
1. Ensure that the *Windows operating system is up to date* with the latest updates and patches.
	1. اطمینان حاصل کنید که سیستم عامل ویندوز با آخرین به روز رسانی ها و وصله ها به روز است.
	2. `Windows Settings => Windows Update`
2. *Set up a unique computer name* for each Windows machine on the network. then Set up a workgroup or domain for the Windows machines.
	1. یک نام کامپیوتر منحصر به فرد برای هر دستگاه ویندوز در شبکه تنظیم کنید. سپس یک گروه کاری  یا دامنه برای پیوستن و ارتباط ماشین های ویندوز با یکدیگر تنظیم کنید.
	2. `Advance System Settings`
3. Configure the *network settings, including the IP address, subnet mask, and default gateway*.
	1. تنظیمات شبکه از جمله آدرس IP و subnet mask و default gateway را پیکربندی کنید.
	2. `ncpa.cpl => Set ip and more`
4. *Install and configure network adapters and drivers* for each Windows machine.
	1. آداپتور ها و درایور های شبکه را برای هر دستگاه ویندوز نصب و پیکربندی کنید.
	2. `Windows Device Manager => NIC Cards`
	3. `ncpa.cpl => Click on Interface => Configures => Advance tab`p
5. Enable *File and Printer sharing & Network Discovery* on the Windows machines that need to access shared resources. then Configure network discovery and sharing settings to allow the Windows machines to be visible and accessible on the network.
	1. اشتراک‌ گذاری فایل و چاپگر را در دستگاه‌ های Windows که نیاز به دسترسی به منابع مشترک دارند، فعال کنید. سپس تنظیمات کشف و اشتراک گذاری شبکه را پیکربندی کنید تا به ماشین های ویندوز اجازه دهید در شبکه قابل مشاهده و در دسترس باشند.
	2. `Windows Settings => Network & Internet => Advance network settings`
6. *Create and configure user accounts and permissions* to control access to shared resources.
	1. ایجاد و پیکربندی حساب های کاربری و مجوزها برای کنترل دسترسی به منابع مشترک.
	2. `Computer managment => Local User and Groups `
	3. `Control Panel => User Accounts`
7. *Install and configure any necessary network services, such as DNS, DHCP, Telnet, TCP/IP*, ... or Active Directory, depending on the network requirements.
	1. بسته به نیاز شبکه، هر گونه سرویس شبکه ضروری مانند DNS، DHCP یا Active Directory را نصب و پیکربندی کنید.
	2. `appwiz.cpl => Turn Windows Feature On/Off`
8. *Test the network connectivity* and ensure that the Windows machines can communicate with each other and access shared resources.
	1. اتصال شبکه را آزمایش کنید و اطمینان حاصل کنید که ماشین های ویندوز می توانند با یکدیگر ارتباط برقرار کنند و به منابع مشترک دسترسی داشته باشند.
	2. `Ping` IP
	3. `Traceroute` Network Routing
	4. `nslookup` DNS
9. *Configure Basic Firewalls* Based on Your Network.
	1. در این مرحله قوانین اولیه فایروال را تنظیم میکنیم و قوانین پیشرفته فایروال را در مبحثی جدا توضیح میدهیم.
	2. `firewall.cpl`
	3. `Windows Security => Firewall tab `
	4. Config Additional Settings for network like proxy, vpn, ...
10. Other Internet & Network Settings
	1. *Create New Connection(VPN)*
		1. `Control Panel => Network & Internet Sharing => Setup New Connection`
			1. Setup new network 
			2. Manually connect to wireless network
			3. Connect to Workspace(VPN)
	2. `Windows Settings => Network & Internet => VPN`
	3. `Windows Settings => Airplane mode ` 
	4. `Windows Settings => Proxy` 
		1. Set Proxy on windows
	5. `Windows Settings => Mobile Hotspot` 
		1. Enable Hotspot
		2. Config Hotspot
	6. `Windows Settings => Advance Network Settings`
		1. Data Usage and Set Limitation on ethernet
		2. Network Reset Configuration
		3. Hardware and Connection Properties 
11. `Internet Options => Connections tab`
### Disable Auto Update in Registry
To block automatic updates in Windows registry, follow these steps:

1. Press the Windows key + R on your keyboard to open the Run dialog box.

2. Type "regedit" and press Enter to open the Registry Editor.

3. Navigate to the following key in the Registry Editor: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows

4. Right-click on the "Windows" key and select New > Key to create a new key. Name the key "WindowsUpdate" (without quotes).

5. Right-click on the newly created "WindowsUpdate" key and select New > Key to create another new key. Name this key "AU" (without quotes).

6. Right-click on the "AU" key and select New > DWORD (32-bit) Value to create a new DWORD value. Name the DWORD value "NoAutoUpdate" (without quotes).

7. Double-click on the "NoAutoUpdate" value and change its value data to 1 to disable automatic updates. If you want to enable automatic updates later on, change the value data to 0.

8. Close the Registry Editor and restart your computer for the changes to take effect.

By following these steps, you can block automatic updates in Windows registry. Be cautious when making changes to the registry, as incorrect modifications can cause system instability or other issues.
### File & Printer Sharing
1. **File Sharing** 
	1. Enable File Sharing
		1. `Control Panel => Network and Internet => Advance sharing settings`
	2. Create User 
	3. Share a folder
	4. give access to user
2. **Printer Sharing**
	1. Set Network Type on on Private or enable file and printer sharing for all profile
		1. `Network & Internet => Ethernet => Set Private`
			1. ![راه اندازی شبکه ویندوز-1](/images/network/WindowsNetworking-1.png)
	2. Enable Printer Sharing
		1. `Control Panel => Network and Internet => Advance sharing settings`
	3. Enable Printer Sharing
		1. `Control Panel => Devices & Printer => Click on Printer => Properties => Sharing tab => Enable Share this Printer`
	4. Enable Printer Sharing on Windows 2
	5. Now see Shared Printer in Device & Printer.
	6. if don't see => `Devices & Printer => Add new Printer Manulay`
		1. ![راه اندازی شبکه ویندوز-2](/images/network/WindowsNetworking-2.png)
	7. Additional Printer Driver
