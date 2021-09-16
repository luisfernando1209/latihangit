import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

email_user = str(input("Sebutkan email anda: "))
email_password = getpass.getpass("Password: ")

email_send = ['luis.fernando002@binus.ac.id','ferluiz899@gmail.com']
for i in email_send :

    


    subject = 'subject'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = i
    msg['Subject'] = subject

    body = 'Hi there, sending this email from Python!'
    msg.attach(MIMEText(body,'plain'))

    filename='C:\\Users\\Cranel\\Downloads\\referensi buat email python.txt'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,i,text)
    server.quit()