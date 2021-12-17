import smtplib
import json
from email.message import EmailMessage as em

message_without_html = "Greetings Sir/Ma'am,\n\nThe following are the procedures of using the commands :\n\n"
message = ''
#Exporting details to send the email
with open("details_service.bin",'r') as file:
    details = json.loads(file.read())

# Email Lists
from_addr = details['from_addr']
to_addr = details['to_addr']

#Compose the message
msg = em()
msg['subject'] = '@Ultron2.0 Help'
msg['from'] = from_addr
msg['to'] = ','.join(to_addr)


with open("operations_list_help.txt", "r") as file:
    help_dict = json.loads(file.read())
    
help_list = list(help_dict)

num = len(help_list)
for i in range(0,num):
    address = f'{help_list[i]}'
    with open(help_dict[address], 'r') as file:
        message += f"""{help_list[i]}\n{file.read()}\n\n"""
        
message_without_html += message + 'Farewell,\n\nUltron2.0'

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