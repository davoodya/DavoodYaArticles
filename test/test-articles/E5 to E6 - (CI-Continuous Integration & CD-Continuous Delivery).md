+++
title = "(CI-Continuous Integration & CD-Continuous Delivery)"
slug = "ci-continuous-integration-cd-continuous-delivery"
date = "2026-02-09T08:52:02+03:30"
lastmod = "2026-02-09T08:52:02+03:30"
draft = false

categories = ["test-articles"]
tags = ["test-articles"]
series = ["test-articles"]

description = "Episode: E1 to E Date: 2024-11-14T00:00:00 Is Finished?: true Practice Primary: Practice Secondary: Time: 45:00 tags: - CyberSecurity - hacking..."
keywords = ["(CI-Continuous Integration & CD-Continuous Delivery)", "test-articles", "e5-to-e6-ci-continuous-integration-cd-continuous-delivery"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/test-articles/ci-continuous-integration-cd-continuous-delivery/"

featured_image = "/images/test-articles/pasted-image-20241114182702.png"
images = ["/images/test-articles/pasted-image-20241114182702.png"]

[params.opengraph]
  title = "(CI-Continuous Integration & CD-Continuous Delivery)"
  description = "Episode: E1 to E Date: 2024-11-14T00:00:00 Is Finished?: true Practice Primary: Practice Secondary: Time: 45:00 tags: - CyberSecurity - hacking..."
  image = "/images/test-articles/pasted-image-20241114182702.png"
  url = "https://davoodya.ir/test-articles/ci-continuous-integration-cd-continuous-delivery/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "(CI-Continuous Integration & CD-Continuous Delivery)"
  description = "Episode: E1 to E Date: 2024-11-14T00:00:00 Is Finished?: true Practice Primary: Practice Secondary: Time: 45:00 tags: - CyberSecurity - hacking..."
  image = "/images/test-articles/pasted-image-20241114182702.png"

readingTime = 10
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
+++
---
Episode: E1 to E
Date: 2024-11-14T00:00:00
Is Finished?: true
Practice Primary: 
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
Pervious Episode: "[[E4 & E5 - (Build Advance Key Logger with Deliver Logged Keys to a Gmail Feature)]]"
Next Episode:
---
-------
### Continuous Integration(CI) - E5
#### Basic & Concepts
فرآیند Continuous Integration قسمتی از DevOps است که وظیفه تولید نرم افزار و اضافه کردن ویژگی ها به نرم افزار را در سریعترین شکل ممکن دارد.
#### Software Development with DevOps
##### Description
1. **Developers Writing Codes and Push it to Github:**
	1. در این فرآیند برنامه نویسان کدهای مربوط به خود را توسعه میدهند.
	2. سپس تمام آنها را به یک مرجع اصلی که در اینجا Github است به اصطلاح کامیت Commit میکنند تا تمام کدها در یک محل تجمیع و متمرکز باشد:
		1. ![[Pasted image 20241114182702.png]]
	3. به این ریپوزیتوری Code Repository گفته میشود.
2. **Move Pushed Codes from Github to Build Server:** 
	1. در مرحله دوم کدهای توسعه داده شده به Build Server منتقل میشوند.
	2. در Build Server ابتدا کدها ساخته Build میشوند، سپس نیز تست و ارزیابی بر روی آنها انجام میشود.
	3. در آخر کدهای تست شده و سالم در یک ریپوزیتوری دیگر بنام Software(ARTIFACT) Repository ذخیره میشوند:
		1. ![[Pasted image 20241114183307.png]]
	4. در واقع در  Software(ARTIFACT) Repository آرشیوی از فایل های Build شده برنامه که براساس کدهای Code Repository هستند قرار دارد:
	   - ![[Pasted image 20241114183415.png]]
	1. فایل هایی که درون Software(ARTIFACT) Repository قرار دارند اصولا پسوند های `zip, jar, msi, exe, dll` دارند:
		1. ![[Pasted image 20241114183553.png]]
1. **Do More Tests:**
	1. در این مرحله Software Tester ها تست های بیشتری را بر روی نسخه های منتشر شده در Software(ARTIFACT) Repository انجام میدهند تا در صورت یافت شدن خطا گزارش ارسال گردد.
	2. پس از اتمام کار Software Tester ها و تایید نهایی آنها برنامه میتواند به **Build(Production) Servers** ها منتقل شود:
		1. ![[Pasted image 20241114183846.png]]
##### Describe a Problem
1. فرض کنید تیم Developing سه هفته بر روی کدها کارکرده است و نسخه از برنامه را منتشر کرده.
2. حال بطور اتوماتیک با راه اندازی DevOps کدها توسط Build Server دریافت Fetch میشود و فرآیند تست کدها توسط Tester Team شروع میشود.
3. حال فرض کنید Tester Team خطاهای متعددی را پیدا کرده است که این خطاها باید توسط تیم Developing برطرف شوند:
	1. ![[Pasted image 20241114184248.png]]
4. در اینجا تیم Developing باید مجددا چندین هفته زمان بگذارد و در واقع در این حالت چندین برابر تیم Tester کار کرده است.
5. حال فرض کنید اگر مشکل در همان مراحل ابتدایی یافت میشد و همان اول مشکل برطرف میشد دیگر این زمان زیاد از تیم Developing گرفته نمیشد.
##### Describe Solution
1. برای حل این مشکل باید پس از هر کامیت که توسط تیم Developing زده میشود کد Build و سپس Test شود:
	1. ![[Pasted image 20241114184734.png]]
2. با پیاده سازی این مورد در هر ویژگی که اضافه میشود برنامه تست میشود و در نتیجه مشکلی که توضیح دادیم پیش نمیاید و تمام تیم ها باهم و به یک اندازه کار میکنند.
3. در این مدل توسعه دهنده متعهد میشود که چندین بار در روز Commit کدهایی که مینویسند را انجام دهند و پس از کامیت برنامه Build و Test میشود.
4. مراحل ارسال کدها بین ریپوزیتوری ها، Build کردن و Testing در DevOps همگی باید بصورت اتوماسیون پیاده سازی شوند:
	1. ![[Pasted image 20241114184948.png]]
5. در این سناریو به محض یافت شدن مشکل جدید، Notification برای Developer Team ارسال میشود تا تیم توسعه دهنده مشکل را برطرف کند.
6. سپس مجددا کد برای Build , Test میرود.

> [!NOTE] All Steps should be Automation
> در پروسه DevOps تمام مراحلی که در بالا توضیح دادیم بصورت اتوماسیون و خودکار انجام میشود.
##### All Steps in 1 Image
- **Image:**
	- ![[Pasted image 20241114190809.png]]
#### DevOps Software Development Life Cycle(CI)
به این چرخه تولید و طراحی نرم افزار که بصورت اتوماسیون انجام و پیاده سازی میشود به اصطلاح Continuous Integration یا CI گفته میشود که در این مدل تمام مراحل توسع بصورت اتوماسیون انجام میشود.
- **Image 1:**
	![[Pasted image 20241114185345.png]]
- **Image 2:**
	- ![[Pasted image 20241114185547.png]]
هدف فرآیند `CI` یافتن مشکلات توسعه نرم افزار و رفع آنها در مراحل اولیه و بصورت خودکار Automation است که اینکار میتواند فرایند توسعه را سریعتر و بهبود ببخشد:
	![[Pasted image 20241114185726.png]]
- برای راه اندازی فرآیند CI یا Continuous Integration از ابزارهایی مانند `jenkins` استفاده میکنیم:
	- ![[Pasted image 20241114190059.png]]
#### DevOps Tools
0. **IDE's**
	1. Eclipse
	2. VS Code
	3. Atom
	4. PyCharm
	5. Many Others
		1. ![[Pasted image 20241114190205.png]]
1. **Version Controllers**
	1. GIT
	2. SVN
	3. TFS
	4. PERFORCE
	5. etc..
		1. ![[Pasted image 20241114190300.png]]
2. **Build Tools:**
	1. MAVEN, ANT, Gradle
	2. MS-Build, Visual Build
	3. IBM Urban Code
	4. MAKE
	5. Grunt
		1. ![[Pasted image 20241114190412.png]]
3. **Software Repositories:**
	1. SONATYPE Nexus
	2. JFROG Artifactory
	3. Archiva
	4. CLOUD SMITH Package
	5. Grunt
		1. ![[Pasted image 20241114190548.png]]
4. **CI Tools:**
	1. JENKINS
	2. CIRCLE CI
	3. TEAM CITY
	4. BAMBOO CI
	5. Cruise Control
		1. ![[Pasted image 20241114190656.png]]
### Continuous Delivery(CD) - E6
#### Basic & Concepts
0. با پیاده سازی CI که هدف آن یافتن مشکلات و عیوب برنامه در مراحل اولیه است تا اینجا کدهایی که توسط Developer Team توسعه داده شده است بصورت خودکار Build و Test میشوند.
1. پس از رفع مشکلات اولیه برنامه بر روی Software Repository منتشر میشود. 
2. به محصولی که Build و Test بر روی آنها انجام میشود و در Software Repository ذخیره میشوند به اصطلاح Artifact یا مصنوعه(سازه) گفته میشود.
#### CD(Continues Delivery)
##### Delivery Process
فرض کنید کل تیم بر روی یک برنامه کار میکنند. Developer Team ویژگی را به برنامه اضافه کرده اند. بنابراین برنامه برای Operation Team تیم ارسال میشود تا بر روی سرورها Deploy شود.
1. حال اگر مشکلی در برنامه یافت شود، هر دو Developer Team و Operation Team باید بایکدیگر همکاری کنند تا این مشکل برطرف شود.
2. در واقع منتشر کردن Deploy برنامه فقط استقرار برنامه بر روی سرور نیست و بلکه بسیاری از کارهای دیگر نیز باید در کنار Deploy کردن بر روی سرور انجام شود.
##### Deployment Process
- پروسه انتشار Deploy برنامه بر روی سرور شامل مراحل زیر میشود:
	1. Server Provisioning
	2. Install Dependency
	3. Configure Changes
	4. Network Adjustment
	5. **Final Step:** Deploy Artifact into Server
	6. ETC...
		1. ![[Pasted image 20241115164557.png]]
- در واقع مشاهده میکنیم که قبل از Deploy برنامه سرور باید برای Deploy آماده شود.
- حال فرض کنید برای هر اضافه کردن هر ویژگی اینکار ها باید انجام شود تا بتوانیم فرآیندهای Build و Test را بر روی Artifact انجام دهیم.
##### Issue
0. در اینجا کارهای CI که مربوط به Developer Team میباشد بصورت اتوماسیون انجام میشود اما کارهای Operation Team هنوز اتوماسیون نشده اند.
2. در نتیجه بدلیل اینکه کار های Operation Team اتوماسیون نشده است، کارهای Operation Team زمان زیادتری نسبت Developer Team میگیرد:
	1. ![[Pasted image 20241115165003.png]]
3. مشکل دیگری که وجود دارد پس از Deploy برنامه محصول باید به تیم تست Q/A Team برسد تا تست های لازم انجام شود و سپس دوباره برنامه باید برای Operation Team باز پس فرستاده شود.
4. در نتیجه دخالت دست در این عملیات بسیار زیاد مشاهده میشود که این امر هم میتواند زمانبر و خسته کننده باشد.
##### Solution
- اگر بخواهیم راه حل را در یک کلمه توضیح دهیم **Automation اتوماسیون** کلمه مناسبی است:
	- ![[Pasted image 20241115165414.png]]
- در واقع برای حل این مشکلات باید کارهایی که Operation Team انجام میدهد را بصورت اتوماسیون دربیاوریم. 
- **کارهایی که باید در Operation Team اتوماسیون شوند عبارتند از:**
	- Server Provisioning
	- Dependencies
	- Configure Changes
	- Network Adjustment 
	- Artifact Deployment
	- ETC ...
		- ![[Pasted image 20241115165602.png]]
##### CD(Continues Delivery) All Steps 
- *Image:*
	-![[Pasted image 20241115170621.png]] 
#### Automation Tools
0. **System and Network Automation:**
	1. Ansible, Puppet, Chef
1. **Cloud Infrastructure Automation:**
	1. Terraform, C-Formation
2. **CI/CD Automation:**
	1. Jenkins, Octopus Deploy
3. **Other:**
	1. Helm Charts
	2. Code Deploy
	3. ETC ...
#### Automation Software Testing
- بخش دیگری از پروسه تولید که باید اتوماسیون شود Software Testing است. در واقع قسمت هایی از برنامه که درزیر توضیح میدهیم باید بصورت خودکار تست و آنالیز شوند:
	0. Functional
	1. Load
	2. Performance
	3. DB
	4. Security
	5. ETC ...
		1. ![[Pasted image 20241115170051.png]]
#### Automation Process
در فرآیند اتوماسیون تیم های مجموعه وظیفه زیر را برعهده دارند:
1. **Operation Team:**
	1. وظیفه نوشتن و طراحی کدهای مربوط به اتوماسیون سازی کارهای مربوط به Deployment(CD) برنامه را به عهده دارند.
2. **Developer Team:**
	1. وظیفه نوشتن و طراحی کدهای مربوط به اتوماسیون سازی کارهای مربوط به Development(CI) توسعه برنامه را به عهده دارند.
3. **Q/A Team:**
	1. وظیفه نوشتن و طراحی کدهای مربوط به اتوماسیون سازی کارهای مربوط به Testing برنامه را به عهده دارند.
4. *Slide:*
	1. ![[Pasted image 20241115170358.png]]
- **Note:**
	-  هر سه تیم باید با یکدیگر هماهنگ و Sync باشند و کدهای اتوماسیون سازی همگی در یک مرجع اصلی ریپوزیتوری ذخیره شوند:
		- ![[Pasted image 20241115170512.png]]
- **CD(Continues Delivery) Automation All Steps:**
	- ![[Pasted image 20241115170724.png]]
### !