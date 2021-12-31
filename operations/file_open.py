import os
import smtplib
import json
from email.message import EmailMessage as em

message_without_html = "Greetings Sir/Ma'am,\n\nThe following are the procedures of using the commands :\n\n"
message = []

with open("details_service.bin",'r') as file:
    details = json.loads(file.read())

# Email Lists
from_addr = details['from_addr']
to_addr = details['to_addr']

with open('operations/subject.txt', 'r') as file:
    subject = file.read()

program_open = subject[5:]
program_open = program_open.lower()    
programs = ''


with open('program_list.txt', 'r') as file :
    programs_list = json.loads(file.read())
    print(subject[5:])
    print(programs_list)

if program_open == "list":

    with open('program_list.txt', 'r') as file :
        programs = file.read()
        message = programs.strip("{")
        message = message.strip("}")
    
    msg = em()
    msg['subject'] = '@Ultron2.0 Program List'
    msg['from'] = from_addr
    msg['to'] = ','.join(to_addr)
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
                               
elif program_open in programs_list:
    os.system('python message/message_positive.py')
    os.startfile(programs_list[program_open])

else:
    os.system('python message/message_negative.py')

with open('operations/subject.txt', 'w') as file:
    file.write('')
