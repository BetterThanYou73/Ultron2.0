import os
import smtplib
import json
from email.mime.multipart import MIMEMultipart as mmp
from email.mime.text import MIMEText as mt
from email.mime.image import MIMEImage as mi

is_installed = ''

with open("operations/date.txt", 'r') as file:
    name = file.read()

import pyautogui

address_save = "screenshots/"+f"{name}"+".png"
myScreenshot = pyautogui.screenshot()
myScreenshot.save(address_save)


with open("details_service.bin",'r') as file:
    details = json.loads(file.read())

# Email Lists
from_addr = details['from_addr']
to_addr = details['to_addr']

#Message content
msg_root = mmp('related')
msg_root['subject'] = '@Ultron2.0 Screenshot'
msg_root['from'] = from_addr
msg_root['to'] = ','.join(to_addr)


msg_alter = mmp('alternative')
msg_root.attach(msg_alter)


msg_without_html = mt('''Greetings Sir/Ma'am,\nAs per your request I am sending you the screenshot..\nFarewell\nUltron2.0''') #If the html text does not show
msg_alter.attach(msg_without_html)

msg = mt("""\
<html>
    <body>
        <h1><font = 'Franklin Gothic', font size = 4, color = 'FF603F'>Greetings Sir/Ma'am,</h1></font>
        <font = 'Franklin Gothic', font size = 4, color = '464340'>
        <p>As per your request I am sending you the screenshot.</p></font>
        <font = 'Franklin Gothic', font size = 4, color = '464340'>
        <p>Farewell</p></font>
        <font = 'Franklin Gothic', font size = 4, color = 'DA3434'>
        <b><p>Ultron 2.0</p></b></font>
    </body>
</html>
""", 'html')

msg_alter.attach(msg)

with open(address_save,'rb') as image:
    img = mi(image.read())
msg_root.attach(img)

#Username, Password and server
USERNAME = details['USERNAME']
PASSWORD = details['PASSWORD']
SERVER = 'smtp.gmail.com'

# Server connection
server = smtplib.SMTP_SSL(SERVER, 465)
# Login
server.login(USERNAME, PASSWORD)
server.sendmail(from_addr, to_addr, msg_root.as_string())

with open("operations/date.txt", 'w') as file:
    file.write("")