+++
title = "(DevOps Basics & Concepts)"
slug = "devops-basics-concepts"
date = "2026-02-09T08:52:02+03:30"
lastmod = "2026-02-09T08:52:02+03:30"
draft = false

categories = ["test-articles"]
tags = ["test-articles"]
series = ["test-articles"]

description = "Episode: E1 to E4 Date: 2024-11-14T00:00:00 Is Finished?: true Practice Primary: Practice Secondary: Time: 35:00 tags: - CyberSecurity - hacking..."
keywords = ["(DevOps Basics & Concepts)", "test-articles", "e1-to-e4-devops-basics-concepts"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/test-articles/devops-basics-concepts/"

featured_image = "/images/test-articles/pasted-image-20241114170454.png"
images = ["/images/test-articles/pasted-image-20241114170454.png"]

[params.opengraph]
  title = "(DevOps Basics & Concepts)"
  description = "Episode: E1 to E4 Date: 2024-11-14T00:00:00 Is Finished?: true Practice Primary: Practice Secondary: Time: 35:00 tags: - CyberSecurity - hacking..."
  image = "/images/test-articles/pasted-image-20241114170454.png"
  url = "https://davoodya.ir/test-articles/devops-basics-concepts/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "(DevOps Basics & Concepts)"
  description = "Episode: E1 to E4 Date: 2024-11-14T00:00:00 Is Finished?: true Practice Primary: Practice Secondary: Time: 35:00 tags: - CyberSecurity - hacking..."
  image = "/images/test-articles/pasted-image-20241114170454.png"

readingTime = 9
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
+++
---
Episode: E1 to E4
Date: 2024-11-14T00:00:00
Is Finished?: true
Practice Primary: 
Practice Secondary: 
Time: 35:00
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
Next Episode: "[[E5 to E6 - (CI-Continuous Integration & CD-Continuous Delivery)]]"
---
-------
### DevOps - Basic & Concept's - E3
#### What is DevOps?
تا قبل از عرضه DevOps برای توسعه یک نرم افزار یا وبسایت نیازمند سه مرحله زیر بودیم:
1. **Development:**
	1. Project Manager Work on this Level
	2. *Level Jobs:* Coding(Back-End & Front-End)
2. **Delivery:**
	1. Operation Head Work on this Level
	2. *Level Jobs:* Network, Datacenter
3. **Service:**
	1. Support Team Work on this Level

> [!NOTE]  With DevOps 
> در هر یک از مراحل بالا نیازمند یک تیم یا کارمند مخصوص بود که وظیفه خود را برعهده داشتند.
> حال بوسیله فرایند DevOps این 3 مرحله را در واقع در یک مرحله تنظیم میکنیم.
> 
#### Software Development Process
برای توضیح بهتر و درک بهتر از مفهوم DevOps باید مراحل توسعه نرم افزار Software Development را توضیح دهیم:
1. **Information Gathering and Information Analyzing:**
	1. اولین مرحله در توسعه نرم افزار جمع آوری اطلاعات در مورد موارد زیر میباشد:
		1. Product Features
			1. ویژگی هایی که محصول باید داشته باشد.
		2. Users(Target Users)
			1. برنامه برای کدام دسته از یوزر ها طراحی بشود.
		3. Usages
			1. کاربرد دقیق برنامه را مشخص میکنیم.
		4. User Requirements 
			1. یوزر ها در این مدل از برنامه ها به چه ویژگی ها و قابلیت هایی نیازمند هستند؟
		5. Market State
			1. وضعیت فعلی بازار برای این مدل از اپ چگونه است؟
		6. *Slide:*
			1. ![[Pasted image 20241114170454.png]]
2. **Planning, What do we Want?**
	1. در این مرحله موارد زیر باید تعیین شوند:
		1. Recourses - منابع مورد نیاز برای اجرای برنامه چقدر است؟
		2. Costs - هزینه های مورد نیاز برای اجرای برنامه چقدر است؟
		3. Risks & Dangers - خطرات و ریسک های برنامه چیست؟
		4. *Slide:*
			1. ![[Pasted image 20241114170715.png]]
3. **Designing Phase:**
	1. در این مرحله طراحان برنامه **Architect Designers** ها  وارد میشوند:
		1. این طراحان بر اساس داده هایی که در فاز اول و دوم جمع آوری شده است به طراحی ساختار برنامه میپردازند.
		2. سپس طراحی خود را در قالب اسنادی بنام `Design Documents` عرضه میکنند.
		3. در واقع **Design Documents** برنامه Road Map توسعه برنامه است.
4. **Development Phase:**
	1. پس از طراحی ساختار برنامه و مشخص شدن نقشه راه تولید و توسعه به فاز کدنویسی و توسعه بنامه میرسیم که در این لول برنامه نویسان وارد کار میشوند.
	2. در این مرحله Developers ها بر اساس Road Map که Architect Designer طراحی کرده کدنویسی برنامه را انجام میدهند.
5. **Testing Phase:**
	1. پس از توسعه برنامه وارد فاز تست برنامه میشویم که در این مرحله Software Tester ها وارد کار میشوند.
	2. در این مرحله برنامه  زیر تست های مختلف قرار میگرد تا باگ های احتمالی برنامه یافت شوند و سپس گزارش شوند.
	3. پس از رفع تمام مشکلات احتمالی میتوانیم به مرحله بعدی یعنی مرحله تولید برویم.
6. **Deployment Phase:**
	1. در این مرحله برنامه توسعه داده شده برروی پلتفرمی مانند اینترنت منتشر میشوند بطوری که یوزر ها میتوانند از برنامه استفاده کنند.
	2. این مرحله به عهده سیستم ادمین System Admin هاست.
7. **Maintenance Phase:**
	1. در این مرحله نگهداری از برنامه منتشر شده صورت میگیرد. 
	2. در واقع اگر نیاز به اعمال تغییراتی باشد در این مرحله انجام میشود. 
	3. همچنین از دیگر موارد مهمی که در این مرحله بررسی میشوند `UP Time` سروری است که برنامه بر روی آن منتشر شده است.
8. **All Steps Slide:**
	1. ![[Pasted image 20241114172102.png]]
#### SDLC & SDLC Models
##### SDLC Description
به مراحل و فرآیند پردازش و تولید برنامه که در بالا توضیح دادیم به اصطلاح فرآیند SDLC گفته میشود. حال فرآیند SDLC مدل های مختلفی دارد که هر کدام روش متفاوتی را ارائه میدهند اما مقصد همگی یکی و در واقع تولید برنامه است.
- **Models in SDLC:**
	- WATERFALL
	- AGILE
	- SPIRAL
	- BIGBANG
	- ETC...
	- *Slide:*
		- ![[Pasted image 20241114172528.png]]
##### 1. Waterfall Model
در این مدل مرحله بعدی فقط پس از اتمام مرحله قبلی شروع میشود. در واقع در این مدل هر مرحله فعلی باید کاملا تمام شود تا بتوانیم مرحله بعدی را شروع کنیم. مراحل این مدل عبارتند از:
1. Requirement
2. Design
3. Implementation 
4. Testing
5. Maintenance
- *Slide:*
	- ![[Pasted image 20241114173009.png]]
> [!NOTE] Explanation
> در این مدل ابتدا باید نیازها سنجید شود، سپس طراحی انجام شود و پس از اتمام طراحی باید ویژگی ها در برنامه پیاده سازی شوند.
> پس از اتمام Implementation میتوانیم وارد فاز تست و پس از اتمام تست وارد مرحله Publish و Maintenance میشویم.
- **Dis Advantages:**
	- برگشت و تغییر کدها دشوار است، در واقع بدلیل اینکه Implementation بصورت کامل تمام شده است برای اضافه کردن ویژگی جدید باید مراحل Implementation تا Maintenance مجددا تکرار شوند.
##### 2. Agile Model
در این مدل چرخه تولید برنامه به چندین چرخه تقسیم میشود و زمان کلی پروژه بین این سه چرخه تقسیم میشود. مثلا اگر کل پروژه 12 هفته زمان نیاز داشته باشد باید برای هر چرخه 2 تا 4 هفته وقت بگذاریم:
	![[Pasted image 20241114173449.png]]
- **Advantages:**
	- در این مدل پس از اتمام هر چرخه میتوانیم برنامه تولید شده را منتشر کنیم، Feedback ها و نظرات را دریافت کنیم و سپس براساس این نظرات چرخه دوم را شروع کنیم. همین کار برای سوئیچ بین چرخه دوم ه چرخه سوم هم انجام میدهیم.
	- با اینکار در هر مرحله نظرات کاربران را بر روی برنامه پیاده سازی میکنیم.
	- بنابراین بر خلاف Waterfall Model امکان اضافه کردن ویژگی در میانه تولید برنامه وجود دارد.
- **Dis Advantages:**
	- در این مدل فرآیند های Deploying , Developing چندین مرتبه انجام میشود و در واقع تیم های Operation, Developing, System Admin, Testing باید چندین مرتبه با یکدیگر ارتباط بگیرند.
	- حال اگر باگی هم در مرحله تست پیدا شود این ارتباط ها تصاعدی بالا میرود.
	- در نتیجه این مدل استرس بیشتری به تیم وارد میکند و زمان بیشتری را هم مصرف میکند. در واقع در این مدل تمام کارمندان بیشتر کار میکنند اما خوب ویژگی هایی مانند اضاه کردن ویژگی در وسط تولید وجود دارد.
	- این امر باعث میشود برنامه دیرتر بدست کاربر اصلی برسد که باعث نارضایتی بیشتر مشتری هم میشود.
#### Dev vs Ops
1. **Operation:**
	1. میتواند ایده های خود را داشته باشد و وظیفه دارد کدی که از تیم Developer میرسد را بدرستی ب روی سرور مستقر کند.
2. **Development:**
	1. این تیم بیشتر وظایفی مشخص و معینی دارد و وظیفه دارد تغییرات مورد نیاز را به سرعت و با کیفیت بر روی پروژه اعمال کند.
3. **Issue's:**
	- در واقع تیم Development کدهای توسعه داده شده را برای تیم Operation میفرستد تا تیم Operation کدها را بر روی سرور مستقر کند.
	- حال در این فرآیند تیم Development به دیر مستقر شدن کد ایراد میگیرد و تیم Operation به کامل نبودن Instruction و Compatible نبودن کدها اشکال میگیرد:
		- ![[Pasted image 20241114174713.png]]
#### When DevOps Come?
- **When DevOps Come:**
	- DevOps => Developer is Agile but Operation is Waterfall
	- در واقع DevOps برای حل مشکل Delivery و برطرف کردن مشکلات میان دو تیم Operation و Development عرضه شده است.
- **Automation:**
	- یک متخصص DevOps وظیفه برقراری ارتباط میان دو تیم Operation و Development را برعهده دارد. 
	- همچنین از وظایف مهم دیگر یک متخصص DevOps اتوماسیون کردن تمام کارهایی است که برای تولید برنامه استفاده میشود.
	- **Automation Objects:**
		- Code Builds
		- Code Testing
		- Software Testing
		- Infra Changes
		- Deployment
		- Also Everything's used in Development and Operation
#### DevOps Life Cycle
1. Developers Commit Codes
2. Code Build, Deployable Software
	1. ![[Pasted image 20241114175541.png]]
3. Code Test, Unit and Integration Testing
4. Code Analysis, Find Vulnerabilities and Best Practice
	1. ![[Pasted image 20241114175628.png]]
5. Delivery, Deploy Changes to Stage
6. DB/Sec Changes, Every Other Changes
	1. ![[Pasted image 20241114175713.png]]
7. Software Testing, Q/A, Functional, Load, Performance Testing
8. Deploy to Prod
	1. ![[Pasted image 20241114175754.png]]
9. Go Live, User Traffic Deliver to new Changes
10. User Approval, Submit User feedbacks
	1. ![[Pasted image 20241114175838.png]]
11. Keep Monitoring
	1. ![[Pasted image 20241114175902.png]]
12. **All Steps in on Image:**
	1. ![[Pasted image 20241114175930.png]]

> [!NOTE]
> *بنابراین میتوان گفت DevOps وظیفه اتوماسیون سازی تمام مواردی را بر عهده دارد که در بین تیم های Operation, Developing, Testing, Sys Admin, etc صورت میگیرد.*
### Practice Notes - E4
این دوره، یک دوره پروژه محور است و پروژه هایی برای تمرین به دانشجو سپرده میشود.
در حل تمارین ممکن اسنت به قصد مشکلی تعبیه شده باشد که برای درک بهتر موضعات و حل مسئه است.
0. **Q/A Guides:**
	1. ![[Pasted image 20241114182058.png]]
### !