+++
title = "کامند های شبکه"
slug = "network-commands-file-printer-sharing"
date = "2024-03-25T15:41:10+03:30"
lastmod = "2026-02-09T15:41:10+03:30"
draft = false

# Taxonomies
categories = ["Network", "Network+"]
tags = ["Network", "Network Commands" ,"Windows", "Linux", "Network+"]
series = ["Network", "Network+"]

# Badges and Filters
readingTime = 10
difficulty = "intermediate" # beginner | medium | intermediate | advanced
lab_required = true 
post_type_fa = "آموزشی" # "آموزشی" | "مقاله" | "اسکریپت" | "خبر" | "دستور العمل" | "معرفی" | "ابزار"

# Options
toc = true
math = false
type = "posts"
# layout = "single"

# SEO
description = "1. `ping` 1. Ping used ICMP Packets 2. Ping Flags 1. `-t` Ping with Infinity ICMP Packet 2. `-n` Count of ICMP Packets 3. `-a` Resolve IP to Host in..."
keywords = ["Network Commands & File Printer Sharing", "network", "network-commands-file-printer-sharing"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/network/network-commands-file-printer-sharing/"

featured_image = "/images/network/Ping_iputils.png"
images = ["/images/network/Ping_iputils.png"]

[params.opengraph]
  title = "Network Commands & File Printer Sharing"
  description = "1. `ping` 1. Ping used ICMP Packets 2. Ping Flags 1. `-t` Ping with Infinity ICMP Packet 2. `-n` Count of ICMP Packets 3. `-a` Resolve IP to Host in..."
  image = "/images/network/Ping_iputils.png"
  url = "https://davoodya.ir/network/network-commands-file-printer-sharing/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Network Commands & File Printer Sharing"
  description = "1. `ping` 1. Ping used ICMP Packets 2. Ping Flags 1. `-t` Ping with Infinity ICMP Packet 2. `-n` Count of ICMP Packets 3. `-a` Resolve IP to Host in..."
  image = "/images/network/Ping_iputils.png"

+++
-----
### Windows Networking Commands
1. `ping`
	1. Ping used ICMP Packets
	2. *Ping Flags*
		1. `-t` Ping with Infinity ICMP Packet 
		2. `-n` Count of ICMP Packets
		3. `-a` Resolve IP to Host in ping
		4. `-l 200` byte of each ICMP Packet commonly used in DOS Attacks
		5. `-S` SRC Address use n Ping
		6. `-i` Specify ICMP TTL(Time to Leave)
		7. `-v` Don't Change TOS(Type of Service) Field
		8. `-f` Dont Fragment
	3. *DOS Attack using ping*:
		1. Whats DOS(Denial of Service) Attack?
		2. What DDOS(Distributed Denial of Service) Attack?
		3. `ping 10.129.131.23 -l 1600 -t`
		4. in advance version you can hide your ip =>
		5. `ping 10.129.131.23 -l 1600 -t -S 10.83.30.21`
	4. *Ping Outputs Meaning*
		1. Replay from Dst IP => Connection is OK
		2. Destination Host unreachable => Host not found in network
		3. Request Timeout => Host Founded but Can't Replay
		4. Transmit Failed, General Failure => Problem in Layer 3 or 2 TCP/IP like NIC or Cable
2. `tracert`
	1. `tracert` use *ICMP* Packets and able to show 30 Next Hope of a ip address.
	2. https://ipgeolocation.io/ => Show IP Geography Information
	3. https://www.ip2location.io/ => Show IP Detailed Information
3. `ipconfig`
	1. `ipconfig -flushdns`
	2. `ipconfig -all`
4. `netsh`
	1. `netsh interface ipv4 set address 'Wlan1' static 192.168.100.10 255.255.255.0 192.168.100.1`
	2. `netsh interface ipv4 set dns 'Wlan1' static 8.8.8.8`
	3. `netsh interface ipv4 add dns 'Wlan1' 4.2.2.4 index=2`
5. *Other Network Commands *
	1. `getmac` Show mac address of all NIC in machine
	2. `route print` Show Routing Table of Windows Machine CMD Version
	3. `Get-NetRoute` Show Routing Table of Windows Machine Powershell Version
### Set IP on Windows in CLI
#### Using Netsh Command
1. *Set IP Steps*
	0. Open Command Prompt or PowerShell as an `administrator`.
	1. Run `ipconfig` to identify network adapter want set ip on this
	2. After identified interface, run following command to set ip on this
	3. `netsh interface ipv4 set address "Your Network Adapter Name" static YOUR_IP_ADDRESS SUBNET_MASK GATEWAY`
	4. *for example*:
	5. `netsh interface ipv4 set address "Ethernet" static 192.168.1.100 255.255.255.0 192.168.1.1`
2. *Set DNS Steps*
	1. after set ip, we should set DNS by run following commands
	2. `netsh interface ipv4 set dns "Your Network Adapter Name" static DNS_SERVER_ADDRESS`
	3. *for example*:
		1. ` netsh interface ipv4 set dns "Ethernet" static 8.8.8.8`
	4. *Add Secondary DNS* :
		1. `netsh interface ipv4 add dns 'Ethernet' 4.2.2.4 index=2`
3. `ipconfig` Confirm the changes
	1. After entering the commands, you can confirm the changes by running the `ipconfig` command again
4. Change back IP settings to DHCP mode
	1. `netsh interface ipv4 set address 'Wlan1' dhcp`
	2. `netsh interface ipv4 set dns 'Wlan1' dhcp`
---
```powershell
#set ip syntax
netsh interface ipv4 set address "Your Network Adapter Name" static YOUR_IP_ADDRESS SUBNET_MASK GATEWAY
#example of set ip
netsh interface ipv4 set address "Ethernet" static 192.168.1.100 255.255.255.0 192.168.1.1

#Set Primary DNS syntax
netsh interface ipv4 set dns "Your Network Adapter Name" static DNS_SERVER_ADDRESS
#Example of set dns
netsh interface ipv4 set dns "Ethernet" static 8.8.8.8
#Add Secondary DNS
netsh interface ipv4 add dns 'Ethernet' 4.2.2.4 index=2 #2

#Change Adapter Settings to DHCP Mode
netsh interface ipv4 set address 'Wlan1' dhcp
netsh interface ipv4 set dns 'Wlan1' dhcp
```
#### Set IP Using **1 File & 1Click**
## !