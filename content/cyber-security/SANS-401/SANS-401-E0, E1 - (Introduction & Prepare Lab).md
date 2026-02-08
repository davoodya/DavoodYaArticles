+++
title = "SANS-401.0 Introduction & Prepare Lab"
tags = ["CyberSecurity", "Pentest"]
category = "Cyber Security"
date = "2024-06-20T12:38:14+03:30"
draft = false

+++

-------
#CyberSecurity #Security 
## E0, E1 - (Introduction & Prepare Lab)
### SANS Courses Roadmap
نقشه راه دوره های SANS به شرح زیر است:
	![Alt text](/images/cyber-security/Pastedimage20240620162926.png)
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
		1. ![Alt text](/images/cyber-security/Pastedimage20240620163247.png)
	2. `ifconfig` IP Status
		1. ![Alt text](/images/cyber-security/Pastedimage20240620163325.png)
2. Windows 10 Enterprise
	1. Laboratory Files in VM -Windows `C:\Labs\`
		1. ![Alt text](/images/cyber-security/Pastedimage20240620163445.png)
	2. `C:/Labs/401.1/`
		1. در این فولدر و دامنه ابزار های بررسی ارتباط ماشین ویندوزی با ماشین لینوکسی را مشاهده میکنیم.
			1. ![Alt text](/images/cyber-security/Pastedimage20240620163844.png)
	3. `ncpa.cpl` Check Windows IP to be same range IP with Linux machine
		1. ![Alt text](/images/cyber-security/Pastedimage20240620164103.png)
	4. Firewall Off by lab default configures. 
3. Check Connectivity
	1. From windows `ping` linux `ping 10.10.10.20`
		1. ![Alt text](/images/cyber-security/Pastedimage20240620164251.png)
	2. From linux `ping` windows `ping 10.10.10.10`
		1. ![Alt text](/images/cyber-security/Pastedimage20240620164453.png)
