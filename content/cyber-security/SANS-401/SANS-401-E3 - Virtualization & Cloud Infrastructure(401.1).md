+++
tags:
  - CyberSecurity
  - Pentest
Category: Cyber Security
date = '2024-06-21T12:38:14+03:30'
draft = true
title = 'SANS-401.2 Virtualization & Cloud Infrastructure'
+++

-------
## E3 - Virtualization & Cloud Infrastructure(401.1)
- [Basic & Concepts](#Basic%20&%20Concepts)
- [Virtualization](#Virtualization)
	- [Definitions](#Definitions)
	- [Attacks against Virtualization](#Attacks%20against%20Virtualization)
	- [Defenses against Virtualization](#Defenses%20against%20Virtualization)
	- [Advance Virtualization](#Advance%20Virtualization)
- [Cloud Infrastructure](#Cloud%20Infrastructure)
	- [Definitions](#Definitions)
	- [Attacks against Cloud Infrastructure](#Attacks%20against%20Cloud%20Infrastructure)
	- [Advance Cloud Infrastructure](#Advance%20Cloud%20Infrastructure)
-----
### Basic & Concepts
### Virtualization
#### Definitions
0. Virtual Machines
	1. ![[Pasted image 20240620183121.png]]
1. Virtualization Overview
	1. ![[Pasted image 20240620183204.png]]
2. How Virtualization Works?
	1. ![[Pasted image 20240620183227.png]]
3. Benefits & Users
	1. ![[Pasted image 20240620183242.png]]
4. Virtual Machines Attacks
	1. ![[Pasted image 20240620183352.png]]
#### Attacks against Virtualization
1. *Hyperjacking*
	1. *Takes Control of Hypervisor:*
		1. در این حملات، Attacker با نفوذ به Host اصلی سعی میکند کنترل Hypervisor را بدست بگیرد و سپس تا از این طریق بتواند به ماشین های مجازی درون دسترسی بگیرد.
	2. *Gain Access to all VMs:*
		1. در این حملات، Attacker با نفوذ به Host اصلی سعی میکند کنترل تمام VM ها را بدست بگیرد و در واقع به تمام ماشین های مجازی دسترسی داشته باشد.
		2. در واقع این نوع از حملات به یک لایه بالاتر نسب به حمله نوع اول انجام میشود:
			1. ![[Pasted image 20240620184519.png]]
2. *VM Escapes*
	1. *Guest OS Escaped Sandbox:*
		1. در این حملات Attacker سعی میکند کنترل VM ها را در محیطی ایزوله در اختیار بگیرد.
	2. *Take over the hypervisor:*
		1. در این نوع هم Attacker سعی میکند کنترل Hypervisor را در محیطی ایزوله بدست بگیرد.
3. *DoS(Denial of Services)*
	1. *DoS:*
		1. در این نوع Attacker با فرستادن پکت ها و یا پردازش های جعلی سعی میکند منابع VM را درگیر کند تا در خدمات رسانی آن اخلال ایجاد کند.
	2. *Either host or guest:*
		1. در این نوع Attacker سعی میکند خدمات رسانی Host اصلی و یا Guest یعنی یکی از VM ها را از کار بیندازد.
4. *Isolation Error*
	1. *Poor Isolation of guest operation systems:*
		1. در این حمله Attacker سعی میکند از طریق ضعف های سیستم عامل Guest به VM ها نفوذ کند.
	2. *Bridged Systems are also vulnerable:*
		1. اگر Guest ها و Host بصورت Bridge به هم متصل شده باشند هم آسیب پذیری برای ایجاد این نوع حملات بوجود می آید.
5. *Inherent Vulnerabilities* 
	1. *Linked flaws between host and guest*
		1. در این نوع حملات، Attacker با استفاده از آسیب پذیری هایی که در لایه بین Guest, Host قرار دارد برای نفوذ استفاده میکند
	2. *Multiple sets of vulnerabilities* 
		1. در این لایه میانی چندین آسیب پذیری وجود دارد که با استفاده از آن Attacker نفوذ خود را انجام میدهد.
			1. ![[Pasted image 20240620194028.png]]
		2. تصویر
			1. ![[Pasted image 20240620194123.png]]
6. *Other Attacks*
	1. Hyper Jumping
	2. Rowhammer
	3. Blue Pill
		1. ![[Pasted image 20240620194240.png]]
#### Defenses against Virtualization
متدهایی که بوسیله آن میتوانیم Host و Guest ها را امن تر کنیم به شرح زیر است:
1. logical Isolation
	1. ایزوله کردن ماشین های مجازی را با هاست اصلی بصورت منظقی و استاندارد انجام دهید.
2. Patching
3. Guest & Host OS
	1. موارد امن سازی را در سیستم عامل Guest & Host انجام دهید.
4. Physical Isolation
	1. استفاده از سخت افزار های مجزا تا ارتباطات ماشین های مجازی هم جدا شوند و اگر به یک شبکه آنها حمله شد شبکه دیگری آسیب نبیند.
5. Separate NIC,s for each VM Network
	1. استفاده از کارت شبکه مجزا برای هر شبکه VM ها
6. Separate hosts
	1. جدا کردن هاست اصلی برای هر شبکه VM ها
7. Use Private VLAN,s
	1. استفاده از VLAN برای شبکه های VM ها
8. Image
	1. ![[Pasted image 20240620194553.png]]
#### Advance Virtualization
1. VM Traffic Monitoring
	1. از کارهای دیگری که میتوانیم برای افزایش امنیت VM ها انجام دهیم، مانیتورینگ ترافیک ورودی/خروجی به ماشین های مجازی است
2. Virtual Network Devices
	1. استفاده از دیوایس های شبکه مجازی مانند روتر مجازی، سوئیچ مجازی، فایروال مجازی هم باعث افزایش امنیت Guest & Host مجازی ساز ما میشود.
3. Image
	1. ![[Pasted image 20240620195702.png]]
### Cloud Infrastructure
#### Definitions
امروزه از Cloud Infrastructure یا همان پردازش ابری بسیار استفاده میشود اما در ایران بدلیل امنیت از این سرویس ها هنوز استفاده زیادی نمیشود. نوع Cloud Types ها به شرح زیر است:
1. *Public*
	1. کلاد های عمومی که توسط شرکت های بزرگ مانند Google, Azure, Amazon, ... عرضه میشوند.
2. *Private*
	1. کلاد های شخصی برای استفاده های شخصی
3. *Hybrid*
	1. این نوع از کلاد ها ترکیبی از دو نوع Public و Private میباشند.
4. *Big Data Cloud*
	1. این نوع از کلاد ها برای نگهدای Large Scale Data استفاده میشود.
#### Attacks against Cloud Infrastructure
1. *VM Traffic Sniffing*
	1. در این نوع حملات Attacker ترافیک های ورودی/خروجی به VM ها را Sniff میکند.
2. *Insecure Cryptography*
	1. در این نوع حملات Attacker از رمزنگاری ضعیف سو استفاده میکند و دریچه نفوذ را از این طریق باز میکند.
	2. رمزنگاری ضعیف باعث بسیاری از حملات در Cloud Infrastructure هاست.
3. *API Attacks*
	1. در این مدل Attacker از طریق نفوذ به API هاست اصلی یا Hypervisor دسترسی خود را میگرد.
4. *Shared Infrastructure*
	1. در این نوع حملات Attacker آسیب پذیری زیر ساخت های اشتراکی را میابد و دسترسی خود را از این طریق حاصل میکند.
	2. به اسیب پذیری ها در زیر ساخت های Share شده *Air Gap* گفته میشود.
5. *Hardware Flaws*
	1. در این مدل Attacker از طریق آسیب پذیری هایی که در سخت افزار اصلی Cloud Computing وجود دارد دسترسی خود را میگیرد. 
	2. مثلا Attacker سعی میکند به دیتاسنتر اصلی شرکت بصورت فیزیکی حمله کند که اکثر این نوع حملات بوسیله Insider Attacker ها انجام میشود.
	3. دو نمونه از حمله های معروف این مدل *Specter and Meltdown* میباشد.
6. *DoS*
	1. حملات DoS هم به Cloud Infrastructure ها زیاد انجام میشود و از حملات شایع محسوب میشود.
7. *Supply Chains Attacks*
	1. به حملات تو در تو گفته میشود. فرض کنید ده ها وب سایت بر روی یک سرور هاست قرار دارند. حال Attacker به هر کدام از این وبسایت ها که نفوذ کند، از آن طریق میتواند به هاست اصلی نفوذ کند و سپس از آن طریق به تمام وبسایت های درون آن سرور دسترسی میگیرد.
8. *Insider Threats*
	1. تهدیدات داخلی یک سازمان و ارگان که روش قدیمی اما محبوب است.
	2. مثلا Attacker کامندی درون سازمانی است و حمله را بصورت فیزیکی انجام میدهد.
9. *Account Hijacking*
	1. در این نوع از حملات Attacker با سرقت اطلاعات یوزر VM و یا یوزر Hypervisor خود را بجای کاربر اصلی جا میزند و دسترسی خود را به VM یا Hypervisor میگیرد.
	2. حملات Hijacking ]م از حملات شایعی است که Cloud Infrastructure ها انجام میشود.
10. Image
	1. ![[Pasted image 20240620200538.png]]
	2. ![[Pasted image 20240620201106.png]]
	3. 
#### Advance Cloud Infrastructure
از کارهایی که میتوانیم برای نظارت بر Cloud Infrastructure ها انجام دهیم تا در صورتیکه حمله ای به آنها صورت گرفت بتوانیم اقدامات لازم را انجام دهیم به شرح زیر هستند:
1. *VM Traffic Monitoring*
	1. مانیتور کردن ترافیک های ورودی و خروجی به Cloud Infrastructure
2. *API*
	1. امن سازی API های سرویس Cloud Infrastructure بسیار مهم هستند.
3. Image
	1. ![[Pasted image 20240620202009.png]]
### !