# uncover

[![Python version: 3.x](https://img.shields.io/badge/python-3.x-blue)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/license-the_unlicense-darkviolet.svg)](https://github.com/Susperya/uncover/blob/master/LICENSE)

#### *A simple terminal app that reveals hidden users, mods and admins currently online at [Chatroom2000](https://chatroom2000.de), one of the biggest and most famous chat communities in Germany.*

[![screen][0]][0]

---

## Installation

Clone or download the repository to your computer and unzip the archive if needed. Navigate to the downloaded folder and create an empty simple text file named **session_id.txt** inside it.

## Requirements

The next step is to get the value for **PHPSESSID** from your browsers cookie. For this open your browser and log into your account *(registered user!)* on 
[Chatroom2000](https://chatroom2000.de). 

When logged in go to **Developer tools** and open the **Web console**. 

[![screen][1]][1]

[![screen][2]][2]

Select **Network analysis** and wait for network traffic to appear in the table.

[![screen][3]][3]

Then click on **"/chat/?ReloaderMessages"** or **"/chat/?ReloaderUserOnline"** in the table so that the window expands to the right.

[![screen][4]][4]

Now click on **Cookies** and scroll down to **PHPSESSID**.

[![screen][5]][5]

Copy the value right to **PHPSESSID** and paste it into the created **session_id.txt** file (*no linebreak after the value*). Finally save and close.

[![screen][6]][6]

---


  [0]: /img/t7.png
  [1]: /img/t1.png
  [2]: /img/t2.png
  [3]: /img/t3.png
  [4]: /img/t4.png
  [5]: /img/t5.png
  [6]: /img/t6.png
