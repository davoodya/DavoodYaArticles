+++
title = "(Pre-Requires Tools & Accounts for DevOps Course)"
slug = "pre-requires-tools-accounts-for-devops-course"
date = "2026-02-09T08:52:02+03:30"
lastmod = "2026-02-09T08:52:02+03:30"
draft = false

categories = ["test-articles"]
tags = ["test-articles"]
series = ["test-articles"]

description = "Episode: E9 to E14 Date: 2024-11-15T00:00:00 Is Finished?: true Practice Primary: false Practice Secondary: Time: 45:00 tags: - CyberSecurity -..."
keywords = ["(Pre-Requires Tools & Accounts for DevOps Course)", "test-articles", "e9-to-e14-pre-requires-tools-accounts-for-devops-course"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/test-articles/pre-requires-tools-accounts-for-devops-course/"

featured_image = "/images/test-articles/pasted-image-20241115172128.png"
images = ["/images/test-articles/pasted-image-20241115172128.png"]

[params.opengraph]
  title = "(Pre-Requires Tools & Accounts for DevOps Course)"
  description = "Episode: E9 to E14 Date: 2024-11-15T00:00:00 Is Finished?: true Practice Primary: false Practice Secondary: Time: 45:00 tags: - CyberSecurity -..."
  image = "/images/test-articles/pasted-image-20241115172128.png"
  url = "https://davoodya.ir/test-articles/pre-requires-tools-accounts-for-devops-course/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "(Pre-Requires Tools & Accounts for DevOps Course)"
  description = "Episode: E9 to E14 Date: 2024-11-15T00:00:00 Is Finished?: true Practice Primary: false Practice Secondary: Time: 45:00 tags: - CyberSecurity -..."
  image = "/images/test-articles/pasted-image-20241115172128.png"

readingTime = 8
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
+++
---
Episode: E9 to E14
Date: 2024-11-15T00:00:00
Is Finished?: true
Practice Primary: false
Practice Secondary: 
Time: 45:00
tags:
  - CyberSecurity
  - hacking
Category:
  - Cyber Security
  - Programming
  - Network
  - DevOps
  - Operation System
banner: 
Home: "[[Table of Content - Hacking & Security]]"
Pervious Episode: "[[E5 to E6 - (CI-Continuous Integration & CD-Continuous Delivery)]]"
Next Episode: "[[E15 to E - (AWS Setup and Start Virtualization)]]"
---
-------
### Tools Perquisite Information - E9
#### Basics & Concepts
در این جلسه به توضیح و معرفی پیش نیازهایی میپردازیم که برای راه اندازی ابزار ها و آزمایشگاه دوره به آنها نیاز داریم.
- **We Need Below Things for this Course:**
	- Install Tools on Computer
	- Create Some Account's
	- AWS Setup for Cloud Computing
#### Course Repositories
- **Project Repository(Main): Codes/Scripts/Tools used in Projects:**
	- در این ریپوزیتوری فایل های پروژه هایی که در طول دوره انجام میدهیم ذخیره میشوند.
	- https://github.com/devopshydclub/vprofile-project
		- ![[Pasted image 20241115172128.png]]
	- این ریپوزیتوری دارای Branch های مختلف است که در هر برنچ فایل های بک پروژه از دوره ذخیره شده است:
		- ![[Pasted image 20241115172242.png]]
	- در واقع ریپوزیتوری اصلی این دوره و پروژه های دوره همین ریپوزیتوری است.
- **Course Files Repository:**
	- در این ریپوزیتوری فایل های دوره و آموزشی ذخیره شده اند.
	- https://github.com/imnowdevops/ddc-material
#### Needed Tools
0. **OS-System Tools:**
	1. Oracle Virtual Box
	2. Git Bash
	3. Vagrant
	4. Chocolaty(Windows) - Brew(Mac)
		1. ![[Pasted image 20241115172827.png]]
1. **Development Tools:**
	1. JDK8
	2. Maven
	3. IntelliJ or another IDE like VS-Code
	4. Sublime Text Editor 
	5. AWS Cli
	6. Terraform
		1. ![[Pasted image 20241115173044.png]]
#### Needed Accounts
0. Github
1. We need purchase a Domain(Go Daddy, IRNIC, ...)
2. Docker Hub Account
3. Sonar Cloud
#### AWS Requisites
0. Create Free Tier Account
1. Setup I Am with MFA(Multi Factor Authentication)
2. Initialize Billing Alarm
3. Certificate Setup to Use HTTPS Secure Connection
	1. ![[Pasted image 20241115173414.png]]
### Install Requisite Tools - E10 to E12
#### Install Chocolatey - E10
##### What is Chocolatey?
ابزاری برای نصب نرم افزار ها بر روی ویندوز از خط فرمان میباشد، این ابزار میتواند نصب نرم افزار را بسیار سرعتر و بهینه تر انجام دهد:
- `choco install notepad++`
##### Install Chocolatey
برای نصب کافیست به وبسایت اصلی ابزار مراجعه کنیم و سپس کامند Powershell نصب ابزار را کپی کرده و در پاورشل ویندوز پیست و اجرا کنیم:
- https://chocolatey.org/install
	- ![[Pasted image 20241115173949.png]]
0. **نکته:** قبل از نصب ابزار باید`Execution Policy` را بررسی کنیم و اگر بر روی `Restricted` تنظیم بود آنرا بر روی `All Signed` تنظیم کنیم:
	- ![[Pasted image 20241115174126.png]]
```powershell
Get-ExecutionPolicy
#if Set on Restricted
Set-ExecutionPolicy AllSigned #or
Set-ExecutionPolicy Bypass -Scope Process
```
1. پس از بررسی `Execution Policy` میتوانیم ابزار را نصب کنیم:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
- **نکته:** 
	- اگر خطایی که در تصویر زیر مشاهده میکنید را دریافت کردیم بدین معناست که آنتی ویروس نصب ابزار را از این روش بلاک کرده است:
		- ![[Pasted image 20241115174550.png]]
	- بنابراین اگر آنتی ویروس فعال است باید برای مدتی Disable شود تا نصب انجام و تمام شود و سپس مجددا فعال گردد.
##### After Installing
پس از نصب ابزار میتوانیم در مخزن Chocolatey جستجو کنیم و کامند نصب ابزاری که نیاز داریم را پیدا و سپس اجرا کنیم:
- مثلا برای نصب Virtual Box میتوانیم از کامند `choco install virtualbox` استفاده کنیم:
	- ![[Pasted image 20241115174805.png]]
- و یا IntelliJ را نیز با کامند `choco install intellijidea-edu` میتوانیم نصب کنیم:
	- ![[Pasted image 20241115174915.png]]
#### Install Brew on Mac - E11
- goto https://homebrew.sh
- Copy Installation Command
- Run Command in terminal to install brew
	- ![[Pasted image 20241115175129.png]]
- After that Add below env variable to `.zprofile`:
	- ![[Pasted image 20241115175200.png]]
- Now we can search in the Brew Repository and find installation command of any software exist in there:
	- `brew install -cask vagrant`
		- ![[Pasted image 20241115175307.png]]
#### Install Other Requisite Softwares - E12
##### `prereqs` Branch
فایل های این قسمت دوره که مربوط به نصب ابزار ها و نرم افزار های مورد نیاز است را در برنچ `prereqs` در ریپوزیتوری https://github.com/devopshydclub/vprofile-project میتوان یافت.
- **`prereqs` Branch Link:**
	- https://github.com/devopshydclub/vprofile-project/tree/prereqs
- **Files in `prereqs` Branch:**
	- در این برنچ هم فایل داکیومنت نصب پیش نیاز ها در فرمت های مختلف مانند `docx, pdf, md, rtf` وجود دارد:
		- ![[Pasted image 20241115182345.png]]
- `Prereqs_doc.md`
	- در این فایل راهنمای نصب ابزارها و نرم افزارهایی که برای تمارین دوره نیاز داریم را مشاهده میکنیم:
		- ![[Pasted image 20241115182526.png]]
##### Start Installing Software's
- **Disclaimer:**
	- **نکته:** حتما نرم افزار ها را با همین ورژن های مشخص شده نصب کنید. 
	- در واقع بدلیل اینکه ممکن است ورژنهای جدید باگ های بیشتری و Stability کمتر نسب به نسخه های قبلی داشته باشد از ورژنهای مشخص شده استفاده میکنیم که اطمینان از این موضوع حاصل شود.
- Open Powershell(Terminal) as Administrator
- **Start Installing:**
	1. Virtual Box 7.0.8
		1. ![[Pasted image 20241115183238.png]]
	2. Vagrant 2.3.4
		1. ![[Pasted image 20241115183248.png]]
	3. Git
		1. ![[Pasted image 20241115183421.png]]
	4. Corretto11jdk
		1. ![[Pasted image 20241115183426.png]]
	5. Maven
		1. ![[Pasted image 20241115183535.png]]
	6. awscli
		1. ![[Pasted image 20241115183532.png]]
	7. intellijidea-community
		1. ![[Pasted image 20241115183730.png]]
	8. vscode
		1. ![[Pasted image 20241115183736.png]]
	9. sublimetext3.app
		1. ![[Pasted image 20241115183752.png]]
1. **Installation Note:**
	1. ممکن است در نصب بعضی از ابزار ها به مشکلی برخوریم که در اینصورت میتوانیم از سوئیچ `force--` برای نصب نرم افزار استفاده کنیم.
```powershell
choco install virtualbox --version=7.0.8 -y

choco install virtualbox --version=2.3.4 -y

choco install git -y

choco install corretto11jdk -y

choco install maven -y

choco install awscli -y

choco install intellijidea-community -y

choco install vscode -y

choco install sublimetext3.app -y #if got error when installing sublime =>
choco install sublimetext3.app --force -y
```
- After Installation Complete **Reboot** your Windows to apply all new configures.
### Create Requires Accounts - E14
1. Create Github Account
2. **Buy a Domain:**
	1. پیشنهاد میشود که دامنه ارزان و دائمی خریداری شود تا بتوانیم تست های و تمارین را راحت تر انجام دهیم.
	2. دامنه های `ir, xyz` جز دامنه های ارزان بشمار میروند.
3. **Create Docker Hub Account:**
	1. https://hub.docker.com
	2. Continue with Free Plan
4. **Create Sonar Cloud:**
	1. https://sonarcloud.io
	2. Signup with your Github Account
### !
