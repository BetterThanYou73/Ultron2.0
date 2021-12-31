import os
import json
import smtplib
from email.message import EmailMessage as em

message_without_html = "Greetings Sir/Ma'am,"
message = '\n\nThe logs of the day that you asked for :\n\n'


with open('operations/subject.txt', 'r') as file:
    subject = file.read()

log_date = subject[6:]

address_log_date = f'logs/{log_date}'+'.txt'

#Exporting details to send the email
with open("details_service.bin",'r') as file:
    details = json.loads(file.read())

# Email Lists
from_addr = details['from_addr']
to_addr = details['to_addr']

subject = f'@Ultron2.0 Log of {log_date[4:]}'


try:
    with open(address_log_date,'r') as file:
        message += file.read()
except FileNotFoundError:
    message = "\n\nIf you see this message that means the date of the log file that you asked for is either deleted or spelled wrong."
    subject = 'Operation Unsuccessful'


#Compose the message
msg = em()
msg['subject'] = subject
msg['from'] = from_addr
msg['to'] = ','.join(to_addr)

#Add the strings and attach to the mail body
message_without_html += message + '\nFarewell,\n\nUltron2.0'
msg.set_content(message_without_html)

#Username, Password and server
USERNAME = details['USERNAME']
PASSWORD = details['PASSWORD']
SERVER = 'smtp.gmail.com'

# Server connection
server = smtplib.SMTP_SSL(SERVER, 465)
# Login
server.login(USERNAME, PASSWORD)
server.sendmail(from_addr, to_addr, msg.as_string())

with open('operations/subject.txt', 'w') as file:
    file.write('')
