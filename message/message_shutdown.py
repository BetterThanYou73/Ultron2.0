import smtplib
import json
from email.message import EmailMessage as em

#Exporting details to send the email
with open("details_service.bin",'r') as file:
    details = json.loads(file.read())

# Email Lists
from_addr = details['from_addr']
to_addr = details['to_addr']

#Message content
a = em()
a['subject'] = '@Ultron2.0 Shutdown Warning'
a['from'] = from_addr
a['to'] = ','.join(to_addr)
a.set_content('''Greetings Sir/Ma'am,\nAs per your request I am shutting down your computer in next 10 seconds.\nFarewell\nUltron2.0''') #If the html text does not show
a.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1><font = 'Franklin Gothic', font size = 4, color = 'FF603F'>Greetings Sir/Ma'am,</h1></font>
        <font = 'Franklin Gothic', font size = 4, color = '464340'>
        <p>As per your request I am shutting down your computer in next 10 seconds.</p></font>
        <font = 'Franklin Gothic', font size = 4, color = '464340'>
        <p>Farewell</p></font>
        <font = 'Franklin Gothic', font size = 4, color = 'DA3434'>
        <b><p>Ultron 2.0</p></b></font>
    </body>
</html>
""",subtype='html')

#Username, Password and server
USERNAME = details['USERNAME']
PASSWORD = details['PASSWORD']
SERVER = 'smtp.gmail.com'

# Server connection
server = smtplib.SMTP_SSL(SERVER, 465)
# Login
server.login(USERNAME, PASSWORD)
server.sendmail(from_addr, to_addr, a.as_string())
