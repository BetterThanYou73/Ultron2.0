import os
import json
import imaplib
import email
from datetime import date

os.system("python file_created_check.py")

#Getting reference path of the today's log
today = date.today()
today = today.strftime('%B %d')
address = 'logs/log_'+today+".txt"

#this will create new log file everyday
with open("log_last_created.txt", 'r+') as file:
    if today != file.read():
        file1 = open("log_last_created.txt", 'w')
        file1.write(today)
        #address = 'logs/log_'+today+".txt"
        with open(address, 'w'):
            pass

#defining important indetifiers
msg_list = {}
msg_operation = []
message_date = ''
msg_subject = ''
msg_date =  ''

#define a dictionary of the details 
details_services = {}
operations_list = {}

os.system("python Ultron_Turn_on_computer.py")


#open and extract the details
with open('details_service.bin','r')  as file:
    details_services = json.loads(file.read())
    
#open and extract operations list
with open('operations_list.txt','r') as file:
    operations_list = json.loads(file.read())


#user and pass
username = details_services['USERNAME']
password = details_services['PASSWORD']


#to and from address
to_addr = details_services['to_addr']
from_addr = details_services['from_addr']


#Default Email
default_email = f'(FROM "{to_addr[0]}")'


#IMAP server url
server_url = 'imap.gmail.com'


#connecting to the server
server_connected = imaplib.IMAP4_SSL(server_url) #USE SSL for secure connection
server_connected.login(username,password) #Logging in

k = True

while k:
#Forever loop until the user requests to stop so
    os.system("python file_created_check.py")
    
#set the values to empty string again so that it wont repeat the same command
    message_date = ''
    msg_subject = ''
    msg_date =  ''
    server_connected.select('inbox') #Selecting inbox
    status, data = server_connected.search(None, 'UNSEEN', default_email) #Searching for Unseen and mails from the default email address
    
    
    with open('operations/subject.txt','w') as file:
        file.write('')
    with open('operations/date.txt','w') as file:
        file.write('')
    


#the list of the emails in the inbox that we searched for
    email_ids = []


#For all the emails in data
    for emails in data:
        email_ids += emails.split()
    

    for id in email_ids:    
        status, data = server_connected.fetch(id, '(RFC822)') #RFC822 is a internet text message format


#data here has the all the data of the particular email
        for message_encoded in data:
            if isinstance(message_encoded, tuple):
                msg = email.message_from_bytes(message_encoded[1])
        #Now we can access the parts of emails such as From, to, date, subject etc, but we only need subject and date
            msg_subject = msg["subject"]
            msg_date =  msg['date']
            
        
        #Filtering the value so it does not repeat
            if msg_subject not in msg_list:
                msg_list[msg_subject] = [msg_subject.lower(),msg_date]

            msg_operation =  msg_list[msg_subject]  
            message_date = msg_operation[1]
            message_date = message_date.replace(',',' ')
            message_date = message_date.replace(':',' ')
            message_date = message_date.replace('+',' ')
            message_date = message_date.replace(' ','_')
        

            #if else loop to determine the operation based on the subject of the fetched email
            if 'fetch_log' in msg_operation[0]:
                with open(address, 'a') as file:
                    file.write(f"\nOperation : {msg_operation[0]}, Date : {msg_operation[1]}")
                with open('operations/subject.txt','w') as file:
                    file.write(msg_operation[0])
                with open('operations/date.txt','w') as file:
                    file.write(message_date)
                open_file ='python ' + operations_list['fetch_log']
                os.system(open_file)
                break
            
            
            elif "open_" in msg_subject:
                with open(address, 'a') as file:
                    file.write(f"\nOperation : {msg_operation[0]}, Date : {msg_operation[1]}")
                with open('operations/subject.txt','w') as file:
                    file.write(msg_operation[0])
                with open('operations/date.txt','w') as file:
                    file.write(message_date)
                open_file ='python ' + operations_list['file_open']
                os.system(open_file)
                break
            
            
            elif msg_operation[0] in operations_list:
                with open(address, 'a') as file:
                    file.write(f"\nOperation : {msg_operation[0]}, Date : {msg_operation[1]}")
                with open('operations/subject.txt','w') as file:
                    file.write(msg_operation[0])
                with open('operations/date.txt','w') as file:
                    file.write(message_date)
                open_file ='python ' + operations_list[msg_operation[0]]
                os.system(open_file)
                break
            
                
            elif msg_operation[0] == 'quit':
                os.system('python message/message_quit_email.py')
                k = False
                break
            
            
            elif msg_operation[0] not in operations_list:
                os.system('python message/message_negative.py')
                break
                      