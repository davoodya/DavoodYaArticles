+++
# Basic
title = "Kali Linux Installing Guide"
slug = "kali-linux-installing-guide"
date = "2024-08-28T09:26:00+03:30"
lastmod = "2026-02-10T09:26:00+03:30"
draft = false

# Taxonomies
categories = ["linux"]
tags = ["linux"]
series = ["linux"]

# Badges and Filters
readingTime = 6 # integer number
difficulty = "medium" # beginner | medium | intermediate | advanced
lab_required = true
post_type_fa = "مقاله" 
# post_type_fa = "آموزشی" | "مقاله" | "اسکریپت" | "خبر" | "دستور العمل" | "معرفی" | "ابزار"

# Images
featured_image = "/images/linux/KaliLinuxInstallingGuide-1.png"
images = ["/images/linux/KaliLinuxInstallingGuide-1.png"]

# Options
toc = true
math = false
type = "posts"
# layout = "single"

# SEO
description = "0. Download & Install VM-Ware 1. Download & Install Virtual Box 2. Type of Installation 1. Using `ISO` file 2. Using `ovf/ova` files 3. Using WSL..."
keywords = ["Kali Linux Installing Guide", "linux", "kali-linux-installing-guide"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/linux/kali-linux-installing-guide/"

# Open Graph and Twitter
[params.opengraph]
  title = "Kali Linux Installing Guide"
  description = "0. Download & Install VM-Ware 1. Download & Install Virtual Box 2. Type of Installation 1. Using `ISO` file 2. Using `ovf/ova` files 3. Using WSL..."
  image = "/images/linux/KaliLinuxInstallingGuide-1.png"
  url = "https://davoodya.ir/linux/kali-linux-installing-guide/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Kali Linux Installing Guide"
  description = "0. Download & Install VM-Ware 1. Download & Install Virtual Box 2. Type of Installation 1. Using `ISO` file 2. Using `ovf/ova` files 3. Using WSL..."
  image = "/images/linux/KaliLinuxInstallingGuide-1.png"

+++
-----
### Installing Kali Linux
#### Pre-Pare Hypervisor
0. Download & Install VM-Ware
1. Download & Install Virtual Box
2. Type of Installation
	1. Using `ISO` file
	2. Using `ovf/ova` files
	3. Using WSL Microsoft Built-In Service
	4. Using vagrant(Metasploitable 2)
	5. Using Containers like Docker
#### Kali Linux Live Disk on VMWare
0. Pre-Requires
	1. Enable Virtualization in Bios Settings
	2. UEFI/Intel
		1. ![Kali Linux Installing Guide-1](/images/linux/KaliLinuxInstallingGuide-1.png)
		2. ![Kali Linux Installing Guide-2](/images/linux/KaliLinuxInstallingGuide-2.png)
	3. Bios/Intel
		1. ![Kali Linux Installing Guide-3](/images/linux/KaliLinuxInstallingGuide-3.png)
	4. AMD/SVM
		1. ![Kali Linux Installing Guide-4](/images/linux/KaliLinuxInstallingGuide-4.png)
	5. Dont Forget to Save Changes
		1. ![Kali Linux Installing Guide-5](/images/linux/KaliLinuxInstallingGuide-5.png)
1. Download VMWare Workstation Pro or VMWare Player(Free version) or Virtual Box
2. Download Kali Live CD
	1. مزیت استفاده از این نسخه در این است که هر بار ماشین را ریست میکنیم تمام اطلاعات(State) ماشین حذف و ریست میشود که این امکان در تست بسیار مفید است.
	2. همچنین میتوانیم نسخه *ISO* و یا نسخه مخصوص ماشین مجازی را هم دانلود و نصب کنیم.
	3. پیشنهاد میشود بر روی VMWare نسخه 32 بیتی کالی را نصب کنید.
3. Create new virtual machine
	1. Select `Kali2023.3-x86.iso` 
	2. in version selected wizard select `Ubuntu` for 32bit installation and select `Ubuntu 64` for 64bit installation
		1. ![Kali Linux Installing Guide-6](/images/linux/KaliLinuxInstallingGuide-6.png)
	3. Install on Multiple storage for more speed.
4. Kali Hardware Configures
	1. Memory: 2Gb
	2. if don't select iso file in installation wizard, Select ISO file in CD/DVD section
		1. ![Kali Linux Installing Guide-7](/images/linux/KaliLinuxInstallingGuide-7.png)
	3. Network: Bridged
		1. در این حالت کارت شبکه ماشین بصورت مستقل و جدا از کارت شبکه هاست اصلی کار میکند .
		2. در واقع کارت شبکه Kali آیپی مجزا از رنج شبکه و هاست اصلی هم آیپی مجزا از رنج همان شبکه دارد.
5. Power On Machine and in Live CD Boot Menu 
	1. Select `Live System(686-pae)` or `Live System(686-pae fail-safe mode)` to Start live kali OS
		1. ![Kali Linux Installing Guide-8](/images/linux/KaliLinuxInstallingGuide-8.png)
6. Now Check machine IPs `ifconfig`
	1. ![Kali Linux Installing Guide-9](/images/linux/KaliLinuxInstallingGuide-9.png)
#### Kali Linux as a Bootable USB Drive
##### Instruction
میتواینیم کالی لینوکس را بر روی حافظه فلش بصورت Bootable منتقل کنیم و سپس از آن فلش برای نصب Kali استفاده کنیم:
1. *Tools Needed*
	1. Kali Linux ISO
	2. Rufus or Ventoy for Create Bootable flash disk
2. Download 2 above tools
3. in Rufus for Kali 32bit installation iso file
	1. بدلیل اینکه ممکن است ماشین تارگت قدیمی باشد بهتر است در اینجا از فرمت های قدیمی `MBR` بر روی `Bios or UEFI` استفاده کنیم. همچنین دیسک USB را در Fat32 با `Cluster Size 8192` فرمت میکنیم.
		1. ![Kali Linux Installing Guide-10](/images/linux/KaliLinuxInstallingGuide-10.png)
4. Plugin in USB to machine and reboot machine to boot with USB
5. *Note:* Disable `Secure Boot` from `Bios Settings` 
	1. برای اینکه ماشین جدید بتواند این فلش را خواند باید `Secure Boot` را تنظیمات `Bios` ماشین جدید غیر فعال کنیم تا بتوانیم دیوایس Bootable با فرمت `Mbr` را به ماشین جدید هم متصل کنیم.
##### Demo
1. Download Live Boot Kali x86 Linux File 
	1. ![Kali Linux Installing Guide-11](/images/linux/KaliLinuxInstallingGuide-11.png)
2. Download Rufus
3. Open Rufus
	1. Select USB Drive
	2. Select Kali Linux iso file
	3. Select `MBR` as Partition scheme
	4. Select `Bios or UEFI` as Target systems
	5. File System `Fat32` on `8192 bytes` Cluster sizes
	6. `Start`
		1. ![Kali Linux Installing Guide-12](/images/linux/KaliLinuxInstallingGuide-12.png)
4. Connect USB Drive to Machine
	1. Reset machine and press `ESC` or `F12` or `DEL` to enter boot menu
	2. Select USB Disk(Removable Drive) in Boot Menu and booting machine on USB Disk
	3. Select `Live System(686-pae)` or `Live System(686-pae fail-safe mode)` in *Kali Linux Live Menu* 
		1. ![Kali Linux Installing Guide-13](/images/linux/KaliLinuxInstallingGuide-13.png)
Default Credential `User: kali, Password: kali
#### Pre-Built Kali Linux in VMWare
##### Instruction & Definitions
میتوانیم از نسخه Kali که از پیش آماده شده و مخصوص ماشین مجازی است استفاده کنیم. 
0. Download Pre-Built Kali Linux for VM Edition
	1. https://www.kali.org/get-kali/#kali-virtual-machines
		1. ![Kali Linux Installing Guide-14](/images/linux/KaliLinuxInstallingGuide-14.png)
1. Download VMWare and Open Pre-Built Kali Linux in VMWare
	1. ![Kali Linux Installing Guide-15](/images/linux/KaliLinuxInstallingGuide-15.png)
##### Demo
1. Download Pre-Built Kali Linux based on your Virtual Machine
	1. ![Kali Linux Installing Guide-16](/images/linux/KaliLinuxInstallingGuide-16.png)
2. Now Extracted `.7z` downloaded file
3. `VMWare Workstation => File => New Virtual Machine ` Import Pre-Built Kali
	1. Select kali linux virtual machine file from extracted folder
		1. ![Kali Linux Installing Guide-17](/images/linux/KaliLinuxInstallingGuide-17.png)
	2. Kali Linux Hardware
		1. ![Kali Linux Installing Guide-18](/images/linux/KaliLinuxInstallingGuide-18.png)
	3. Power ON Machine and use this
	4. Default Credential `User: kali, Password: kali
#### Installing WSL
#### VMWare Networking
1. VM-Ware Networking
	1. NAT Network
	2. Bridge Network
	3. Lan Segments
	4. Host Only
	5. Custom
		1. vmnet0 to vmnet20
	6. VM
2. Networking Windows on VM
	7. Connect two windows together using Lan segments
		1. Set Computer Name & WORKGROUP
		2. Set IP
		3. Create User for sharing
	8. Networking PC1-VM to main PC and share folder from PC to PC1-VM using Host only network or custom bridged
