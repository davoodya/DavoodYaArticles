---
Category: Network
Date: 2024-03-25
Day: دوشنبه
Hijri Date: 1403-01-06
Time: "90:00"
Title: Basic & Concept
---

------------------------------------------------------------------------

### Numbers in Computers

1.  Binary
    1.  01
2.  Octa
    1.  0 to 8
3.  Decimal
    1.  0 to 10
4.  Hexadecimal
    1.  0 to F
        1.  0123456789 & ABCDEF
5.  Convert Binary to Decimal Number
    \### IP - Basic & Concepts
    \#### Definitions
6.  **Whats IP? IP Usages**
    1.  منظور از **IP** مخفف عبارت Internet Protocol یا به فارسی پروتکل اینترنت است. آدرس **آیپی** مجموعه‌ ای از اعداد است که به‌ عنوان شناسهٔ منحصر‌ به‌ فرد هر دستگاه، اجازه میدهند موبایل، کامپیوتر و... در شبکه از طریق اینترنت یا یک شبکه محلی به یکدیگر متصل شوند و داده‌‌ها را انتقال دهند.
        1.  <figure>
            <img
            src="../IP%20%26%20Mac%20Address%20-%20Concepts/69b4739024a7486c23a0a4f544de5ce002c34e2c.png"
            title="wikilink" alt="Pastedimage20240325144303.png" />
            <figcaption
            aria-hidden="true">Pastedimage20240325144303.png</figcaption>
            </figure>
    2.  آیپی ها در دو ورژن 4 و ورژن 6 عرضه میشوند. وظیفه آیپی آدرس دهی و مسیریابی در شبکه میباشند.
    3.  *آیپی ورژن 4 که ما بیشتر هم از آن استفاده میکنیم نوع آن `decimal` است و کلا 32 بیت است و دارای 4 بخش 8 بیتی است:*
        1.  IP Parts =\> `0-255, 0-255, 0-255, 0-255`
            \#### Parts of IP
7.  **IP Have 2 Part(NET IP & Broadcast IP):**
    1.  Net IP: Describe network IP
        1.  قسمتی از آیپی که مشخص کننده شبکه ایست که آیپی به آن اشاره میکند.
    2.  Host IP: Describe Host IP
        1.  قسمتی از آیپی که مشخص کننده ماشین است که در شبکه قرار دارد.
    3.  Image:
        1.  <figure>
            <img
            src="../IP%20%26%20Mac%20Address%20-%20Concepts/43cda696a1bce6bf959bf1321875786fcaf2341a.png"
            title="wikilink" alt="Pastedimage20240325144616.png" />
            <figcaption
            aria-hidden="true">Pastedimage20240325144616.png</figcaption>
            </figure>
    4.  *Note 1:* If you want machines in a same network:
        1.  برای قرار دادن ماشین ها در یک شبکه:
        2.  اول NET IP تمام ماشین های شبکه باید یکسان باشند.
        3.  همچنین HOST IP آیپی هر ماشین باید متفاوت باشد.
    5.  *Note 2:* Use Router to Connect Some Network(NET IP) together:
        1.  **نکته:** از Router ها برای اتصال چندین Net IP(یا چندین شبکه) به یکدیگر استفاده میشود.
            \#### Subnetting
            \##### Basic Subnetting
8.  **Subnet & IP:**
    1.  ساب نت عددی است که در هنگام تعریف آیپی نوشته میشود و مشخص کننده Net ID و Host ID است. عدد 0 مشخص کننده Host ID میباشد و عدد 255 و سایرین مشخص کننده Net ID میباشند.
    2.  *Subnet Pictures:*
        1.  <figure>
            <img
            src="../IP%20%26%20Mac%20Address%20-%20Concepts/2107fe859b28bf0d883f06c8abef15fee70e5855.png"
            title="wikilink" alt="Pastedimage20240325144624.png" />
            <figcaption
            aria-hidden="true">Pastedimage20240325144624.png</figcaption>
            </figure>

        2.  ![Pasted image 20240325144714.png](../IP%20%26%20Mac%20Address%20-%20Concepts/c1066d1e2a40adcc19d1bb586eab2828e3f6a7a6.png "wikilink")
            \##### Deep to Subnetting
9.  Limit Subnet to user count == Increase Security
10. Subnets =\>
    1.  Subnet /24 ==\> `x.x.x.0-254/24`
    2.  Subnet /25 ==\> `x.x.x.0-128/25`
    3.  Subnet /26 ==\> `x.x.x.0-64/26`
    4.  Subnet /27 ==\> `x.x.x.0-32/27`
    5.  Subnet /25 ==\> `x.x.x.0-16/28`
11. Example of IP/Subnetting for A Corporations in Three Part:
    1.  `One Range IP for 3 network`
        \#### Special IPs
        چندین آیپی خاص و ویژه هستند که از پیش برای یکسری از کارها رزرو شده اند. دو عدد از این ها Net IP و Broadcast IP میباشد. برای تعریف آیپی های خاص باید یک رنج آیپی داشته باشیم. برای اینکار از آیپی `192.168.10.100` استفاده میکنیم.
12. **NET IP & Broadcast IP(In the specific Network):**
    1.  *Net IP:* `192.168.10.0`
        1.  اولین آیپی یک شبکه میباشد که مشخص کننده رنج کلی شبکه است.
        2.  `192.168.10.0`
    2.  *Broadcast IP:* `192.168.10.255`
        1.  *توضیح فرآیند Broadcast:* به فرآیند ارسال یک بسته برای تمام هاست ها(ماشین هایی) که درون یک شبکه قرار دارند Broadcasting گفته میشود.
        2.  حال Broadcast IP آخرین آیپی یک شبکه است که برای فرآیند Broadcasting از آن استفاده میشود.
        3.  `192.168.10.255`
    3.  *Note:* We cant use Net IP & Broadcast IP for Packet Src/Dst Addresses and Machines in the Network
        1.  آیپی های مبدا و مقصد یک بسته، نباید از این دو آیپی Net IP و Broadcast IP باشند.
        2.  همچنین ماشین های شبکه نیز نمیتوانند از این دو آیپی استفاده کنند.
13. Loopback =\> `127.0.0.1/8`
14. **Global Broadcast =\> `255.255.255.255`**
    1.  تفاوت این Broadcast IP با Broadcast IP یک رنج شبکه در این است که بسته ای که به این آیپی ارسال میشود برای تمام شبکه های موجود ارسال میشود.
    2.  بر خلاف مورد قبلی که بسته برای تمام هاست های یک شبکه ارسال میشد.
15. APIPA =\> `169.254.0.1-169.254.255.254`
16. Default Route =\> `0.0.0.0/0`
17. Multicast=\>`224.0.0.0/4`
    \#### Set IP on Windows
18. **Set IP:**
    0.  برای تنظیم آیپی بر روی اینترفیس های شبکه(کارت های شبکه) باید از پنجره Network and Internet Sharing Center شویم. برای وارد شدن به این پنجره روش های متفاوتی داریم:
    1.  `ncpa.cpl`
    2.  `Settings => Network & Internet Sharing Center => Change Adapter Setings => Network Interfaces`
        \#### IP Classes
19. **IP Classes:**
    1.  <figure>
        <img
        src="../IP%20%26%20Mac%20Address%20-%20Concepts/1498d1eb0efcb41741dc7cb15dc66263d899229a.png"
        title="wikilink" alt="Pastedimage20240325145116.png" />
        <figcaption
        aria-hidden="true">Pastedimage20240325145116.png</figcaption>
        </figure>

    2.  <figure>
        <img
        src="../IP%20%26%20Mac%20Address%20-%20Concepts/0b9a0937ce9260c17a4469deae6e71458b745aa7.png"
        title="wikilink" alt="Pastedimage20240325145021.png" />
        <figcaption
        aria-hidden="true">Pastedimage20240325145021.png</figcaption>
        </figure>

    3.  <figure>
        <img
        src="../IP%20%26%20Mac%20Address%20-%20Concepts/04be80d7bc2c7879a4fb6c386f77670b98a3b3de.png"
        title="wikilink" alt="Pastedimage20240325145030.png" />
        <figcaption
        aria-hidden="true">Pastedimage20240325145030.png</figcaption>
        </figure>

    4.  ![Pasted image 20240325145052.png](../IP%20%26%20Mac%20Address%20-%20Concepts/42557375ff8f1df54c2244a7bbc16aa6482eef87.png "wikilink")
        \#### IP Versions
20. **IP Versions:**
    1.  در کل دو ورژن آیپی یعنی IPv4 و IPv6 داریم.
    2.  *IPv4 Structure:*
        1.  `xxx.xxx.xxx.xxx`
        2.  که هر پارت xxx میتواند بین 0 تا 255 باشد.
        3.  در کل آیپی ورژن 4 ترکیبی از اعداد Decimal میباشد.
    3.  *IPv6 Structure:*
        1.  `xxxx.xxxx.xxxx.xxxx.xxxx.xxxx`
        2.  هر پارت xxxx میتواند بین 0 تا F باشد.
        3.  یعنی آیپی ورژن 6 از نوع Hexadecimal میباشد.
    4.  *Image:*
        1.  <figure>
            <img
            src="../IP%20%26%20Mac%20Address%20-%20Concepts/3326bb7ad5e24e4eedb42f30edf58d86778a4023.png"
            title="wikilink" alt="Pastedimage20240325145331.png" />
            <figcaption
            aria-hidden="true">Pastedimage20240325145331.png</figcaption>
            </figure>
21. **IPv6 vs IPv4:**
    1.  IPv6 VS IPv4 Image
        1.  <figure>
            <img
            src="../IP%20%26%20Mac%20Address%20-%20Concepts/352a2b7970e6609e5956ca27f5a48fd67e8d350d.png"
            title="wikilink" alt="Pastedimage20240325145329.png" />
            <figcaption
            aria-hidden="true">Pastedimage20240325145329.png</figcaption>
            </figure>
22. **Loopbacks(Localhost) in IPv4 & IPv6**
    \### MAC Address
    \#### Definitions
23. **MAC Address:**
    1.  مک آدرس (**MAC address**) یا آدرس‌‌ کنترل دسترسی رسانه (Media Access Control) شناسه‌ ای منحصر به‌ فرد محسوب می‌شود که سازنده به یک کارت شبکه (NIC) اختصاص داده است.
    2.  ساختار مک آدرس `xx.xx.xx.xx.xx.xx` میباشد و در کل `48bit` میباشد.
    3.  هر بخش `xx` شامل اعداد Hexadecimal میباشد:
        ![Pasted image 20240325150746.png](../IP%20%26%20Mac%20Address%20-%20Concepts/65a60bcfffe785611e9b3e43dedf144d241bb56d.png "wikilink")
        ![Pasted image 20240325150755.png](../IP%20%26%20Mac%20Address%20-%20Concepts/a69f5227eca20f400a9ecc683292203b43de1965.png "wikilink")
    4.  مک آدرس ها توسط سازنده دیوایس سخت افزاری به دیوایس تعلق میگیرد البته به روش هایی قابل تغییر است که جلوتر توضیح میدهیم.
        \#### MAC Table & See MAC
24. Mac Addr Save to Mac tables. Switches Work with Mac Tables
    1.  <figure>
        <img
        src="../IP%20%26%20Mac%20Address%20-%20Concepts/8cb831e47d02a3afd546787f484751c8944a2993.png"
        title="wikilink" alt="Pastedimage20240406230317.png" />
        <figcaption
        aria-hidden="true">Pastedimage20240406230317.png</figcaption>
        </figure>
25. See Mac Addr on windows =\> `getmac` & `ipconfig -all`
    \#### Changing MAC Address
26. مک آدرس را با روش های امنیتی و برای انجام کارهای امنیتی میتوانیم با استفاده از ابزارهایی مانند `macchanger, ifconfig, ip link, ...` تغییر دهیم.
27. مثلا برای حملاتی که از MAC Filtering وایرلس عبور میکند و آنرا دور میزند از این ابزارها استفاده میکنیم.
    \#### Attack Through MAC Address
28. Mac Flooding
29. Mac Spoofing

### !
