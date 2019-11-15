# uncover

[![Python version: 3.x](https://img.shields.io/badge/python-3.x-blue)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/license-the_unlicense-darkviolet.svg)](https://github.com/Susperya/uncover/blob/master/LICENSE)

#### *A simple terminal app that reveals hidden users, mods and admins currently online at [Chatroom2000.de](https://chatroom2000.de), one of the biggest and most famous chat communities in Germany.*

---

## Requirements

Clone or download the repository to your computer and unzip the archive if needed. Navigate to the downloaded folder and create an empty simple text file named `session_id.txt` inside it.

The next step is to get the value for `PHPSESSID` from your browsers cookie. For this open your browser and log into your account (registered user!) on 
[Chatroom2000](https://chatroom2000.de). 

When logged in go to developer tools and open the web console. 

[![enter image description here][1]][1]

  [1]: /img/t1.png

[![enter image description here][2]][2]

  [2]: /img/t2.png

Then select `network analysis` and wait for network traffic.

[![enter image description here][3]][3]

  [3]: /img/t3.png

Then click on `/chat/?ReloaderMessages` or `/chat/?ReloaderUserOnline` in the table so that the window expands to the right.

[![enter image description here][4]][4]

  [4]: /img/t4.png

Now click on `Cookies` and scroll down to `PHPSESSID`.

[![enter image description here][5]][5]

  [5]: /img/t5.png

Copy the value right to `PHPSESSID` and paste it on the first line of the created file `session_id.txt` (*no linebreak after the value*). Finally save and close the file.

[![enter image description here][6]][6]

  [6]: /img/t6.png

---
