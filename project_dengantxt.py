import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass
import os
import os.path

def mendaftarEmail():
        inputJumlah = int(input("Sebutkan jumlah email yang ingin disimpan: "))
        i = 0
        for i in range(inputJumlah):
            inputEmail = str(input("Sebutkan email ke {} yang ingin disimpan: ".format(i+1)))
            f = open("receiver_list_new.txt","a")
            f.write('{}\n'.format(inputEmail))
            f.close()
    

def membacaEmail():
    if os.path.isfile("receiver_list_new.txt"):
            f = open("receiver_list_new.txt","r")
            buka_list_email = f.read()
            print(buka_list_email)
    else :
        print("Contact is not exist!!! Please register email list first")

def mengirimEmail(inputPengirim,inputSubject,inputSurat):
    email_user = str(input("Sebutkan email anda: "))
    email_password = getpass.getpass("Password: ")

    email_send = []
    with open('receiver_list_new.txt') as f :
        lines = [line.rstrip() for line in f]

    for i in lines :

        


        subject = 'subject'

        msg = MIMEMultipart()
        msg['From'] = inputPengirim
        msg['To'] = i
        msg['Subject'] = inputSubject

        body = inputSurat
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

while True :
    
    try :
        print('''
        -----------------------
        Aplikasi Mengirim Email
        -----------------------
        1. Lihat Email Yang Terdaftar
        2. Daftar Email
        3. Mengirim Email
        4. Exit
        ''')

        jawaban = int(input("Sebutkan menu yang ingin anda pilih: "))
        print("\n\n")
        print("------------")
        if jawaban == 1 :
            membacaEmail()
        elif jawaban == 2:
            mendaftarEmail()
        elif jawaban == 3:
            inputPengirim = str(input("Input Nama Pengirim (Bukan Email): "))
            inputSubject = str(input("Subject untuk Email anda: "))
            inputSurat = str(input("Isi Surat Anda: "))
            mengirimEmail(inputPengirim,inputSubject,inputSurat)
        elif jawaban == 4:
            print('\n')
            print("THANK YOU FOR USING THE APPS!!!")
            break
        else :
            print("Jawaban anda salah, silahkan coba lagi")
    except (ValueError) : print("Jawaban anda kurang tepat, silahkan coba lagi!!!")
