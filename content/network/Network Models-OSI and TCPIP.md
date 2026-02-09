+++
title = "Network Models-OSI and TCPIP"
slug = "network-models-osi-and-tcpip"
date = "2024-03-25T15:41:10+03:30"
lastmod = "2026-02-09T15:41:10+03:30"
draft = false

categories = ["network"]
tags = ["network"]
series = ["network"]

description = "1. Port & Protocol Definitions 2. Whats OSI(Open System Interconnection) Model? 1. Physical 2. Data Link (Switches-Ethernet) 3. Network (Routers-IP)..."
keywords = ["Network Models-OSI and TCPIP", "network", "network-models-osi-and-tcpip"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/network/network-models-osi-and-tcpip/"

featured_image = "/images/network/NetworkModels-OSIandTCPIP-1.png"
images = ["/images/network/NetworkModels-OSIandTCPIP-1.png"]

[params.opengraph]
  title = "Network Models-OSI and TCPIP"
  description = "1. Port & Protocol Definitions 2. Whats OSI(Open System Interconnection) Model? 1. Physical 2. Data Link (Switches-Ethernet) 3. Network (Routers-IP)..."
  image = "/images/network/NetworkModels-OSIandTCPIP-1.png"
  url = "https://davoodya.ir/network/network-models-osi-and-tcpip/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Network Models-OSI and TCPIP"
  description = "1. Port & Protocol Definitions 2. Whats OSI(Open System Interconnection) Model? 1. Physical 2. Data Link (Switches-Ethernet) 3. Network (Routers-IP)..."
  image = "/images/network/NetworkModels-OSIandTCPIP-1.png"

readingTime = 7
difficulty = "medium"
toc = true
math = false
lab_required = true
post_type_fa = "مقاله"

# layout = "single"
type = "posts"
+++
### OSI Model
#### OSI Models Concept(Need Notebook) 
1. Port & Protocol Definitions
2. Whats OSI(Open System Interconnection) Model?
	1. Physical
	2. Data Link (Switches-Ethernet)
	3. Network (Routers-IP)
	4. Transportation(TCP-UDP)
	5. Session (Connection Session)
	6. Presentation (Encryption)
	7. Application (Users & Communications)
3. OSI Images =>
	1. ![Network Models-OSI and TCPIP-1](/images/network/NetworkModels-OSIandTCPIP-1.png)
	2. ![Network Models-OSI and TCPIP-2](/images/network/NetworkModels-OSIandTCPIP-2.png)
4. Protocols in Layers.
	1. ![Network Models-OSI and TCPIP-3](/images/network/NetworkModels-OSIandTCPIP-3.png)
5. `Layer 7-Application`  
	1. Definitions & Usages
		1. ![Network Models-OSI and TCPIP-4](/images/network/NetworkModels-OSIandTCPIP-4.png)
	2. Protocols in Layer7
		1. ![Network Models-OSI and TCPIP-5](/images/network/NetworkModels-OSIandTCPIP-5.png)
	3. Describe Protocols in Layer7.
6. Presentation Layer
	1. Encryption and Decryption
7. Session Layer
	1. Session Layer Duties:
		1. Create Connection
		2. Connection Management
		3. Close Connection
	2. Session Layer Protocols:
		1. NetBios
		2. PPTP, L2TP
	3. Image:
		1. ![Network Models-OSI and TCPIP-6](/images/network/NetworkModels-OSIandTCPIP-6.png)
8. Transportation Layer
	1. Create Logical Connection in two model: TCP & UDP
	2. TCP Connection Oriented: Send packet with src ack & dst ack
	3. UDP Connection Less: Send Packet without ACK from SRC or DST
	4. Image:
		1. ![Network Models-OSI and TCPIP-7](/images/network/NetworkModels-OSIandTCPIP-7.png)
9. Network Layer
	1. وظیفه مسیریابی بسته ها و مشخص کردن اینکه بسته ها چگونه از مبدا به مقصد برسند.
	2. وظیفه دوم مدیریت خطا و نوبت دهی برای بسته های حجیم
	3. مشخص کردن لایه مجازی Virtual Circuit 
	4. ![Network Models-OSI and TCPIP-8](/images/network/NetworkModels-OSIandTCPIP-8.png)
## E16
1. Data Link Layer
	1. Data Link Layer have two Part: LLC & MAC
	2. Whats MAC Address؟
	3. Whats LLC(Logic Link Control)
	4. Data to bit,  bit to Data 
	5. ![Network Models-OSI and TCPIP-9](/images/network/NetworkModels-OSIandTCPIP-9.png)
2. Physical Layer
	1. ![Network Models-OSI and TCPIP-10](/images/network/NetworkModels-OSIandTCPIP-10.png)
	2. ![Network Models-OSI and TCPIP-11](/images/network/NetworkModels-OSIandTCPIP-11.png)
#### OSI Layers Description(Need Notebook)
##### Layer 7 - Application
1. **FTP:**
	- FTP(21) 
	- FTP Definitions
		- File Zilla
		- Win-SCP
	- FTPS => FTP + SSL Cert 
	- TFTP(69) 
		- SolarWinds TFTP Server
2. **FTP Softwares & Practically**
	- *Win-SCP*
		- Definition Win-SCP
		- Installation Win-SCP
		- Usage of Win-SCP
	- *Initialize FTP Connection(Android/Windows) - FTP Server Pro Android*
		- Install FTP Server on Android
		- Install FTP Client(WinSCP) on Windows
		- Access to android device files from Windows via FTP 
	- *Initialize FTP Connection(Windows/Windows) - FileZilla*
		- Install FileZilla Server on Windows 1
		- Install FileZilla Client on Windows 2
	- *Access to FTP Server*
		- Access to Windows 1 files from Windows 2 via FTP using *FileZilla*
		- Access to Windows 1 files from Windows 2 via FTP using *WinSCP*
		- Access to Windows 1 files from Windows 2 via FTP using *File Explorer*
	- *TFTP(69) => Simple and CLI*
		- Solar Winds TFTP Server
3. **Email Protocols:**
	- SMTP(25)
		- SMTPs(465, 587)
	- POP3(110)
	- IMAP4(143)
	- SNMP(161)
		- MIB
	- Mail Spring
		- Definition and Installation Mail Spring
		- Add SNMP and IMAP Email Account
		- Add G-Mail/Outlook Account
4. **HTTP & HTTPS:**
	1. HTTP Definitions
	2. HTTP Messages
	3. HTTP Request and Response
	4. HTTP Methods
		- GET
		- POST
		- PUT
		- DELETE
	5. HTTPS => HTTP + SSL Certificate
	6. URL Structure
	7. *Note HTTPS:* HTTPS == HTTP + SSL Certificate
		1. بنابراین در واقع HTTPS در لایه ششم 6 شبکه فعالیت میکند زیرا که به رمزنگاری SSL نیازمند است.
5. **HTTP Server:**
	1. Python HTTP Server
		-  `python3 -m http.server`
		- `python3 -m http.server --bind 192.168.180.130 8000` 
6. **Telnet Protocol:**
	1. Telnet Definitions
	2. Add Telnet feature to Windows
	3. `telnet` command 
7. **SNMP(161-udp):**
	- SNMP Usage
		- برای مشاهده کانفیگ ها و اطلاعات ماشین های بر بستر شبکه و همچنین اعمال یکسری از کانفیگ ها بر بستر شبکه استفاده میشود.
	- SNMP Server & SNMP Agent
##### Layer 6 - Presentation
1. Definition of Layer 6
2. **Terminal Connectivity Protocols:**
	- SSH(22)
		- SSH Definitions
			- Telnet + SSL Encryption
		- 3 Way Handshake Definition
			- Syn, Syn|Ack, Ack
		- `ssh` commands
		- `ssh davoodya@192.168.10.1`
3. **Terminal Connectivity Softwares:**
	- PuTTY
		- Putty Definition
		- Installation of Putty
		- Usage of Putty
	- mRemoteNG
		- Definition & Installation MRemoteNG
##### Layer 5 - Session
1. Definitions
	1. Full Duplex & Half Duplex 
	2. Dialog Control
	3. Token Managing
	4. Synchronization
2. Usage of Session Layer
##### Layer 4 - Transportation
1. Definitions
	1. Segmentation & Re Assembling
	2. Multiplexing
	3. Error Detection  Correction
	4. Port Addressing
	5. Connection Control
	6. Flow Control
	7. Data Integrity
##### Layer 3 - Network
1. Layer 3 Protocols => ARP, IP, RIP, ICMP, ...
2. IP(Internet Protocol)
	1. Definition of IP
	2. IPv4 Header 
		1. ![Network Models-OSI and TCPIP-12](/images/network/NetworkModels-OSIandTCPIP-12.png)
3. ICMP(Internet Control Message Protocol)
	1. ICMP Definition
	2. , Echo Request & Echo Replay(No using SYN/ACK)
	3. *ICMP use this Parameters of Headers IP*:
		1. Version: ipv4 or ipv6?
		2. TOS == 0
		3. TTL => Differ base on Destination OS
	4. `Ping` use *ICMP*
4. ARP(Address Resolution Protocol)
	1. Definition of ARP
	2. ARP Packets(Arp Request & Arp Replay) & ARP Tables
	3. IP  use ARP for sending packet from Layer 3 to Layer 2
	4. ICMP also use ARP for converting IP to Mac(Layer 3 to Layer 2)
	5. for work Machine with Switches => Need ARP
	6. ARP in Mikrotik
5. IGMP(Internet Group Management Protocol)
	1. Differs between Broadcast & Multicast
	2. IGMP all versions using Multicast
	3. IGMP join users in a group for establish Multicast Connection
	4. User join or Leave groups by =>
		1. Send Request to 224.0.0.1 => Join
		2. Send Request to 224.0.0.2 => Leave
		3. Machines use above IP's to Join or Leave Groups
		4. in version1 users only can Joined groups but in version 2 and 3 users can Join or Leave groups
6. RIP
	1. Routing Protocol
##### Layer 2 - Data Link
1. Layer 2 Description
2. Mac addr
#### TCP/IP Model
1. TCP/IP Layers
	1. Application (Telnet, http, ftp, smtp, ..)
	2. Transport (UDP, TCP)
	3. Network, Internet (ICMP, ARP, IP)
	4. Network Interface (Mac Address)
	5. Image =>
		1. ![Network Models-OSI and TCPIP-13](/images/network/NetworkModels-OSIandTCPIP-13.png)
	6. a Packet details =>
		1. ![Network Models-OSI and TCPIP-14](/images/network/NetworkModels-OSIandTCPIP-14.png)
### !