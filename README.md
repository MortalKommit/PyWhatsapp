# PyWhatsapp
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://github.com/MortalKommit/PyWhatsapp)
[![License](https://img.shields.io/github/license/MortalKommit/PyWhatsapp.svg)](https://github.com/MortalKommit/PyWhatsapp/blob/master/LICENSE)
 [![HitCount](http://hits.dwyl.io/{MortalKommit}/{PyWhatsapp}.svg)](http://hits.dwyl.io/{MortalKommit}/{PyWhatsapp})
## Automated Whatsapp messaging using Selenium &amp; Python

Pywhatsapp uses command-line arguments to send message(s) to one or more contacts. Messages may be sent following a schedule,  
or at once. Messages may contain media attachments, or documents. Contacts may be added at runtime, or be chosen from a   
contact list associated with your Whatsapp account.
Messages may contain media attachments (Video or Images). Selenium serves as the interface to send messages
, while autoit adds attachments to messages and schedule arranges them to be sent on a programme.

---

## Planned features
1. Automated responses to greetings, placeholder messages and better
scheduling functionality
2. Simple GUI, emoji support


## Installation

>$ pip install -r requirements.txt

OR

>$ pip install selenium
>
>$ pip install schedule
>
>$ pip install PyAutoIt

###### Issues installing autoit? Download it directly from the author's github:  
 [LINK](https://github.com/jacexh/pyautoit)
---

### Platform: Windows/Mac/Linux
ChromeDriver: 
Download an updated version compatible with your browser version from <a href =
"http://chromedriver.chromium.org/downloads"> Download Link </a>

Requires Chromedriver location added to the %PATH% system environment variable.

>Set ChromeDriver path in function whatsapp_login()
><a href ="https://stackoverflow.com/a/44870398/6897603">Set
>  ChromeDriver Path in MacOS</a>

---
### Sending Attachments requires AutoIt (WINDOWS ONLY/OPTIONAL):
If you have pyautoit, the autoit library is downloaded automatically.   

Autoit may be installed manually from the links below:  

<a href = "https://www.autoitscript.com/site/autoit/downloads/">Official
Website Download Webpage</a>

<a href =
"https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.exe">AutoIt Installer (x86/x64)</a>

<a href =
"https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3.zip">Self-Extracting Archive version</a>

Customize your installation as necessary

---

## Usage
### Command-Line : Windows

Sending a message to "Jay", who's in your contact list

```
PyWhatsapp.py -h

usage: PyWhatsapp.py [-h] --msg message [--schd [schedule]] [--attach] [--doc]
                     contacts [contacts ...]

Automated Whatsapp Messaging

positional arguments:
  contacts           A list of contacts (names or numbers, max:10, country code required as
                     +XX) without the +

optional arguments:
  -h, --help         show this help message and exit
  --msg message      The message to be sent to a list of contacts or groups. Use for
                     newline
  --schd [schedule]  Whether the message should be sent on a schedule or once, DEFAULT:once
                     FORMAT:DD-MM-YYYYTHH:MM:SS
  --attach           Whether to include attachments(image/video)
  --doc              Whether to include documents

Usage :python PyWhatsapp.py "Jay" --msg "Hey"

```
### Shell : bash, zsh(MacOS)

```
$ python PyWhatsapp.py -h
usage: PyWhatsapp.py [-h] --msg message [--schd [schedule]] [--attach] [--doc]
                     contacts [contacts ...]

Automated Whatsapp Messaging

positional arguments:
  contacts           A list of contacts (names or numbers, max:10, country
                     code required as +XX) without the +

optional arguments:
  -h, --help         show this help message and exit
  --msg message      The message to be sent to a list of contacts or groups.
                     Use for newline
  --schd [schedule]  Whether the message should be sent on a schedule or once,
                     DEFAULT:once FORMAT:DD-MM-YYYYTHH:MM:SS
  --attach           Whether to include attachments(image/video)
  --doc              Whether to include documents

Usage :python PyWhatsapp.py "Jay" --msg "Hey"
```
For un saved contacts, use as follows:
Enter your country code then contact number.
>Use: 919899123456
>
>Don't Use: +919899123456


### --msg
The message to be sent to contacts, use \n for newline. Sentences with spaces must be enclosed by quotes! 
Double for windows, single for UNIX-like

### --schd
To schedule a message, follow the format as specified


### --attach
Causes an attachment dialog to be opened up, hold select to choose multiple attachments 


### --doc
Causes a document dialog to be opened up, hold select to send multiple


### Input Screenshot:
<img
src="https://raw.githubusercontent.com/shauryauppal/PyWhatsapp/master/Input_Type.PNG" height=300/>

---

### Demo of Working (GIF)
<img
src="https://raw.githubusercontent.com/shauryauppal/PyWhatsapp/master/Media/Demo.gif" height=400 width=400/>


---
## License
License
Licensed as Apache 2.0, open source software.(see <a
href="https://github.com/MortalKommit/PyWhatsapp/blob/master/LICENSE">LICENSE</a>).

Usage of this program is bound by the terms and conditions specified in the 
(<a href="https://www.whatsapp.com/legal/">Whatsapp 
Terms of Service</a>).  
You should not violate any clauses or restrictions specified in the terms above.  
The author of this program is not liable for any damage, claim or action to your whatsapp account
by the use of this program.  
Use this program at your own risk.  


---

## Author:
## <a href="https://github.com/MortalKommit/">MortalKommit</a>
### Based off a fork of <a href="https://github.com/shauryauppal/PyWhatsapp">Shaurya Uppal</a>

