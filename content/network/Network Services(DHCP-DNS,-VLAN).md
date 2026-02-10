+++
# title = "Network Services(DHCP-DNS,-VLAN)"
title = "مطالبی که برای یادگیری VLAN , DHCP , DNS باید آموخت؟"
slug = "network-servicesdhcp-dns-vlan"
date = "2024-03-25T15:41:10+03:30"
lastmod = "2026-02-09T15:41:10+03:30"
draft = false

# Taxonomies
categories = ["Network", "Network-Services"]
tags = ["Network", "Network-Services" ,"DHCP", "DNS", "VLAN", "Network+"]
series = ["Network", "Network-Services"]

# Badges and Filters
readingTime = 4
difficulty = "beginner" # beginner | medium | intermediate | advanced
lab_required = false 
post_type_fa = "دستور العمل" # "آموزشی" | "مقاله" | "اسکریپت" | "خبر" | "دستور العمل" | "معرفی" | "ابزار"

# Options
toc = true
math = false
type = "posts"
# layout = "single"

# SEO
description = "1. Broadcast Domain 2. Collision 3. V-Lan 1. V-Lan Definition 2. V-Lan Notes 3. Default V-Lan 4. Normal V-Lan 4. Routing Protocols 1. Definition of..."
keywords = ["Network Services(DHCP-DNS,-VLAN)", "network", "network-servicesdhcp-dns-vlan"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/network/network-servicesdhcp-dns-vlan/"

featured_image = "/images/network/NetworkServices(DHCP-DNS,-VLAN)-1.png"
images = ["/images/network/NetworkServices(DHCP-DNS,-VLAN)-1.png"]

[params.opengraph]
  title = "Network Services(DHCP-DNS,-VLAN)"
  description = "1. Broadcast Domain 2. Collision 3. V-Lan 1. V-Lan Definition 2. V-Lan Notes 3. Default V-Lan 4. Normal V-Lan 4. Routing Protocols 1. Definition of..."
  image = "/images/network/NetworkServices(DHCP-DNS,-VLAN)-1.png"
  url = "https://davoodya.ir/network/network-servicesdhcp-dns-vlan/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Network Services(DHCP-DNS,-VLAN)"
  description = "1. Broadcast Domain 2. Collision 3. V-Lan 1. V-Lan Definition 2. V-Lan Notes 3. Default V-Lan 4. Normal V-Lan 4. Routing Protocols 1. Definition of..."
  image = "/images/network/NetworkServices(DHCP-DNS,-VLAN)-1.png"


+++
---
### V-Lan
#### Definitions
1. Broadcast Domain
2. Collision
3. V-Lan
	1. V-Lan Definition
	2. V-Lan Notes
	3. Default V-Lan
	4. Normal V-Lan
4. Routing Protocols
	1. Definition of Routing Protocols
	2. Routing Tables Types
		1. Dynamic Routing
		2. Static Routing
		3. Advantage & Disadvantage of this types
	3. Dynamic Routing Protocols
		1. EIGRP
		2. OSPF
		3. RIP
		4. BGP
	4. Static Routing 
	5. *Note:* Usage of Default Gateway
### Routing Protocols
### DHCP
#### DHCP Definitions
1. DHCP Definition
2. What is IP Pool ?
3. DORA Packets
	1. D(Discovery)
	2. O(Offer)
	3. R(Request)
	4. A(Acknowledge)
	5. Image
		1. ![Network Services(DHCP-DNS,-VLAN)-1](/images/network/NetworkServices(DHCP-DNS,-VLAN)-1.png)
4. *DHCP Example:*
	1. DHCP Server on Home Router(Mikrotik-HEX)
### DNS
#### DNS Definitions
1. Describe DNS Usage
2. DNS Port & Protocol
3. FQDN
	1. What is FQDN(Fully Qualified Domain Name)?
	2. FQDN Parts
		1. `HostName.DomainName`
		2. *davoodya.home*
			1. davoodya => Host Name
			2. home => Domain Name
4. DNS Working Levels
	1. First Level Domain
		1. *.eu , .ir , .com , ...*
	2. Second Level Domain
		1. *google , yahoo , varzesh3*
	3. Third Level Domain
		1. *mail , it , test*
	4. Example
		1. mail.google.com
			1. mail is third level
			2. google is second level
			3. com is first level
		2. test.yahoo.net
			1. test is third level
			2. yahoo is second level
			3. net is first level
5. DNS Records
	1. A Record
	2. PTR Record
	3. CName-Record
	4. MX-Record
	5. SRV-Record
	6. NS-Record
6. Public DNS
	1. Usage of Public DNS
	2. Some Public DNS
		1. 8.8.8.8
		2. 9.9.9.9
		3. 4.2.2.4
		4. etc ...
7. Static (Manual) DNS
	1. Usage of static DNS
	2. `Winbox => DNS Server ` Set a Static for private ip
## END