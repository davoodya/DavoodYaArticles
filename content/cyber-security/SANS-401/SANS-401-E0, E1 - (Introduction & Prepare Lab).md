+++
title = "SANS-401-(Introduction & Prepare Lab)"
slug = "sans-401-introduction-prepare-lab"
date = "2024-06-20T09:59:19+03:30"
lastmod = "2026-02-09T09:59:19+03:30"
draft = false

categories = ["SANS-401"]
tags = ["SANS-401", "CyberSecurity", "Pentest"]
series = ["SANS-401"]

description = "نقشه راه دوره های SANS به شرح زیر است: هر دوره از مجموعه SANS از چندین دامنه تقسیم شده است که این دامنه ها بصورت زیر شماره در دامنه مشخص میشود. مثلا..."
keywords = ["SANS-401-(Introduction & Prepare Lab)", "SANS-401", "CyberSecurity", "Pentest", "sans-401-e0-e1-introduction-prepare-lab"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/SANS-401/sans-401-introduction-prepare-lab/"

featured_image = "/images/cyber-security/SANS-401.0Introduction&PrepareLab-1.png"
images = ["/images/cyber-security/SANS-401.0Introduction&PrepareLab-1.png"]

[params.opengraph]
  title = "SANS-401-(Introduction & Prepare Lab)"
  description = "نقشه راه دوره های SANS به شرح زیر است: هر دوره از مجموعه SANS از چندین دامنه تقسیم شده است که این دامنه ها بصورت زیر شماره در دامنه مشخص میشود. مثلا..."
  image = "/images/cyber-security/SANS-401.0Introduction&PrepareLab-1.png"
  url = "https://davoodya.ir/SANS-401/sans-401-introduction-prepare-lab/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "SANS-401-(Introduction & Prepare Lab)"
  description = "نقشه راه دوره های SANS به شرح زیر است: هر دوره از مجموعه SANS از چندین دامنه تقسیم شده است که این دامنه ها بصورت زیر شماره در دامنه مشخص میشود. مثلا..."
  image = "/images/cyber-security/SANS-401.0Introduction&PrepareLab-1.png"

readingTime = 2
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
+++

-------
#CyberSecurity #Security 
## E0, E1 - (Introduction & Prepare Lab)
### SANS Courses Roadmap
نقشه راه دوره های SANS به شرح زیر است:
	![SANS-401.0 Introduction & Prepare Lab-1](/images/cyber-security/SANS-401.0Introduction&PrepareLab-1.png)
هر دوره از مجموعه SANS از چندین دامنه تقسیم شده است که این دامنه ها بصورت زیر شماره در دامنه مشخص میشود. مثلا دوره SEC401 دارای 6 دامنه مجزاست که شماره آنها به شرح زیر است:
1. SANS SEC 401.1
2. SANS SEC 401.2
3. SANS SEC 401.3
4. SANS SEC 401.4
5. SANS SEC 401.5
6. SANS SEC 401.6
### Prepare SEC401 Laboratory
برای دوره SANS SEC401 دو آزمایشگاه وجود دارد که برای تمرین مباحث مطرح شده از آنها استفاده میکنیم:
1. Kali 2016.1 vm edition
	1. Hardware's
		1. ![SANS-401.0 Introduction & Prepare Lab-2](/images/cyber-security/SANS-401.0Introduction&PrepareLab-2.png)
	2. `ifconfig` IP Status
		1. ![SANS-401.0 Introduction & Prepare Lab-3](/images/cyber-security/SANS-401.0Introduction&PrepareLab-3.png)
2. Windows 10 Enterprise
	1. Laboratory Files in VM -Windows `C:\Labs\`
		1. ![SANS-401.0 Introduction & Prepare Lab-4](/images/cyber-security/SANS-401.0Introduction&PrepareLab-4.png)
	2. `C:/Labs/401.1/`
		1. در این فولدر و دامنه ابزار های بررسی ارتباط ماشین ویندوزی با ماشین لینوکسی را مشاهده میکنیم.
			1. ![SANS-401.0 Introduction & Prepare Lab-5](/images/cyber-security/SANS-401.0Introduction&PrepareLab-5.png)
	3. `ncpa.cpl` Check Windows IP to be same range IP with Linux machine
		1. ![SANS-401.0 Introduction & Prepare Lab-6](/images/cyber-security/SANS-401.0Introduction&PrepareLab-6.png)
	4. Firewall Off by lab default configures. 
3. Check Connectivity
	1. From windows `ping` linux `ping 10.10.10.20`
		1. ![SANS-401.0 Introduction & Prepare Lab-7](/images/cyber-security/SANS-401.0Introduction&PrepareLab-7.png)
	2. From linux `ping` windows `ping 10.10.10.10`
		1. ![SANS-401.0 Introduction & Prepare Lab-8](/images/cyber-security/SANS-401.0Introduction&PrepareLab-8.png)
