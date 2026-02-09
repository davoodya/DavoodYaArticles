+++
title = "Dockerfile Basic & Syntax"
slug = "dockerfile-basic-syntax"
date = "2025-07-03T09:51:33+03:30"
lastmod = "2026-02-09T09:51:33+03:30"
draft = false

categories = ["test-articles", "Cyber Security", "Programming"]
tags = ["test-articles", "CyberSecurity", "hacking"]
series = ["test-articles"]

description = "🔴 Hi there, it's been a while since I decided to share my handouts as articles. I wrote this handout in the Markdown format, so it's better to copy..."
keywords = ["Dockerfile Basic & Syntax", "test-articles", "CyberSecurity", "hacking", "Cyber Security", "Programming", "e1-dockerfile-basic-syntax"]
author = "Davood Yahay"
robots = "index, follow"
canonical = "https://davoodya.ir/test-articles/dockerfile-basic-syntax/"

featured_image = "/images/test-articles/pasted-image-20250703195036.png"
images = ["/images/test-articles/pasted-image-20250703195036.png"]

[params.opengraph]
  title = "Dockerfile Basic & Syntax"
  description = "🔴 Hi there, it's been a while since I decided to share my handouts as articles. I wrote this handout in the Markdown format, so it's better to copy..."
  image = "/images/test-articles/pasted-image-20250703195036.png"
  url = "https://davoodya.ir/test-articles/dockerfile-basic-syntax/"
  type = "article"

[params.twitter]
  card = "summary_large_image"
  title = "Dockerfile Basic & Syntax"
  description = "🔴 Hi there, it's been a while since I decided to share my handouts as articles. I wrote this handout in the Markdown format, so it's better to copy..."
  image = "/images/test-articles/pasted-image-20250703195036.png"

readingTime = 3
difficulty = "medium"
toc = true
math = false
lab_required = true

# layout = "single"
type = "posts"
+++
-------
### Dockerfile
#### Introduction
🔴 Hi there, it's been a while since I decided to share my handouts as articles. I wrote this handout in the Markdown format, so it's better to copy it into Obsidian or Notion , or another software support Markdown format and then read it. i hope you enjoy. 😊
#### What is Dockerfile?
فایل Dockerfile یک فایل متنی ساده است که شامل دستوراتی با Syntax مشخص است که Docker با استفاده از آنها یک ایمیج سفارشی که میتواند دستورات خاصی را اجرا کند میسازد.
1. **Dockerfile Usages**:
	1. Install Security Tools like `nmap, metasploit, sqlmap, ...`
	2. Set Testing Environment with Especial Configurations
	3. Automate Peneteration Tests
#### Dockerfile Basic Syntax
##### Dockerfile Sample
```Dockerfile
#1. Select Prebuilt Image
FROM ubuntu:220.4

#2. Information about Developer
LABEL maintainer="davoodya40@gmail.com"

#3. Run Commands, here Update & Upgrade System
RUN apt update && apt upgrade
#4. Install Necessary Tools
RUN apt install -y nmap curl git 

#5. Copy file from Local machine to Container
COPY ./script.sh /opt/script.sh

#6. Set Working Directory
WORKDIR /opt

#7. Run command to Set Executable Permission to Script
RUN chmod +x ./script.sh

#8. this Command run after Container running
CMD ["./script.sh"]
```
##### Syntax Description
- `FROM`
	- پایه‌ سیستم‌ عامل کانتینر (مثل Ubuntu یا Alpine)
- `LABEL`
	- اطلاعات Metadata درباره نویسنده یا پروژه
- `RUN`
	- اجرای دستورات در زمان ساخت ایمیج
- `COPY`
	- انتقال فایل از سیستم میزبان به کانتینر
- `WORKDIR`
	- تنظیم دایرکتوری کاری داخل کانتینر
- `CMD`
	- دستور پیش‌ فرضی که پس از اجرای کانتینر اجرا می‌شود (فقط یکبار می‌تواند استفاده شود)
#### Simple Practice 1
##### Practice Description
1. در این تمرین میخواهیم یک Dockerfile ساده بسازیم که از Base image Alpine استفاده کند.
2. سپس repository خود را آپدیت کند و curl را نصب کند.
3. سپس درخواست curl به سمت `"https://ifconfig.me"` بزند تا آیپی عمومی ماشین یافت شود.
##### Practice Dockerfile
1. Write Dockerfile
```Dockerfile
FROM alpine
RUN apk update && apk add curl

CMD ["curl", "https://ifconfig.me"]
```
2. Build & Run Dockerfile
```sh
docker build -t mycurl .
docker run mycurl
```
#### Simple Practice 2
##### Practice Description
1. در این تمرین میخواهیم از Base Image بنام `kalilinux/kali-rolling` استفاده کنیم.
2. سپس میخواهیم `apt-get update && apt-get install -y nmap` را نصب کنیم.
3. سپس اسکریپتی را برای انجام اسکن nmap بنویسیم و آنرا به کانتینر Copy کنیم.
4. سپس همان اسکریپت را در کانتینر  اجرا کنیم.
##### Nmap Scanning Script
```sh
#!/bin/bash

if [ -z "$1" ]; then
  echo "Enter Target for Scan in Argument"
  echo "./scan.sh 192.168.1.1"
  exit 1
fi

echo "Start Scanning Target $1"
nmap -sV -T4 "$1"

```
##### Writing Dockerfile
```Dockerfile
#1. Select Base Image
FROM kalilinux/kali-rolling
LABEL maintainer="DavoodSec@davoodya.ir"

#2. Fix GPG Key Error
RUN echo 'Acquire::AllowInsecureRepositories "true";' > /etc/apt/apt.conf.d/99insecure
#3. Update apt repo & install nmap
RUN apt-get update && apt-get install -y --allow-unauthenticated nmap

#4. Copy scan.sh to Container
RUN mkdir tools
COPY ./scan.sh /tools/scan.sh

#5. Set Working Directory
WORKDIR /tools/

#6. Set Executable Permission of scan.sh
RUN chmod +x ./scan.sh

CMD ["sh", "./scan.sh", "192.168.10.100"]
```
- *Image:*
	- ![[Pasted image 20250703195036.png]]
2. Run & Build Dockerfile
```sh
docker build -t nmap_scan .
docker run nmap_scan
```
#### !