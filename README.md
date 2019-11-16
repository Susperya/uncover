# uncover

[![Python version: 3.x](https://img.shields.io/badge/python-3.x-blue)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/license-the_unlicense-darkviolet.svg)](https://github.com/Susperya/uncover/blob/master/LICENSE)

#### *A simple terminal app that reveals hidden users, mods and admins currently online at [Chatroom2000](https://chatroom2000.de), one of the biggest and most famous chat communities in Germany.*

>#### *Eine einfache Konsolenanwendung, die versteckte User, Moderatoren und Admins aufdeckt, welche gerade online sind bei [Chatroom2000](https://chatroom2000.de), einer der größten und bekanntesten Chat-Communities in Deutschland.*

[![screen][0]][0]

---

## Quick start

Download the repository to your computer *(and unzip the archive if downloaded as .zip)*. Navigate to the subfolder **/uncover/uncover/** and open the file **session_id.txt** *(empty .txt file)*. Leave it open.

> Laden Sie zunächst das Repository auf Ihren Computer herunter *(wenn Sie es als .zip heruntergeladen haben, entpacken Sie das Archiv bitte anschließend)*. Navigieren Sie nun zum Unterordner **/uncover/uncover/** und öffnen Sie die Datei **session_id.txt** *(leere TXT-Datei)*. Lassen Sie sie geöffnet.

---

The next step is to get the value for **PHPSESSID** from your browsers cookie. For this open your browser and log into your account *(registered user!)* on 
[Chatroom2000](https://chatroom2000.de).

> Der nächste Schritt besteht darin, den Wert für **PHPSESSID** aus Ihrem Browser-Cookie auszulesen. Öffnen Sie dazu Ihren Browser und melden Sie sich in Ihrem Account *(registrierter User!)* bei [Chatroom2000](https://chatroom2000.de) an.

---

When logged in go to **Developer tools** and open the **Web console**. 

> Nachdem Sie eingeloggt sind, öffnen Sie das Menü (s. Screenshot unten), wählen Sie dort *Entwickler-Tools* und klicken Sie dann auf *Web-Konsole*.

[![screen][1]][1]

[![screen][2]][2]

---

Select **Network analysis** and wait for network traffic to appear in the table.

> Klicken Sie nun auf *Netzwerkanalyse* und warten Sie ggf. einen Augenblick, bis der Browserverkehr in der Tabelle (s. Screenshot unten) aufgelistet wird.

[![screen][3]][3]

---

Then click on **"/chat/?ReloaderMessages"** or **"/chat/?ReloaderUserOnline"** in the table. An additional window will open to the right.

> Klicken Sie dann in der Tabelle auf die Zeile **"/chat/?ReloaderMessages"** oder **"/chat/?ReloaderUserOnline"**. Es öffnet sich rechts ein zusätzliches Fenster.

[![screen][4]][4]

---

Now click on **Cookies** and scroll down to **PHPSESSID**.

> Klicken Sie nun auf **Cookies** (s. Screenshot unten) und scrollen Sie in der Tabelle soweit nach unten, bis Sie **PHPSESSID** finden.

[![screen][5]][5]

[![screen][6]][6]

---

Copy the value right to **PHPSESSID** and paste it into the created **session_id.txt** file (*no linebreak after the value*). Finally save and close.

> Kopieren Sie den Wert rechts von **PHPSESSID** und fügen Sie ihn in die noch geöffnete **session_id.txt**-Datei ein *(kein Zeilenumbruch, nur eine Zeile mit dem eingefügten Wert)*. Dann speichern und schließen Sie die Datei.

---

Now you're able to run the app by executing **uncover.exe**.

> Jetzt können Sie die Anwendung durch Doppelklicken der Datei **uncover.exe** starten.



  [0]: /img/t7.png
  [1]: /img/t1.png
  [2]: /img/t2.png
  [3]: /img/t3.png
  [4]: /img/t4.png
  [5]: /img/t5.png
  [6]: /img/t6.png
