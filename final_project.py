import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#basic
server = "smtp.gmail.com"
port = 587
sender = input("Masukkan Email: ")
pword = getpass.getpass(prompt="Masukkan Password: ", stream=None)
message = "semoga bisa dikirim amin."

#Buat dafatar kontak
daftar_kontak = []

kontak = open("kontak.txt", "r")
for alamat in kontak:
    line = alamat.strip()
    list = line.split()
    daftar_kontak.append(list)

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing email address 
msg['From'] = sender
msg['Subject'] = "Final Project"

#body email
body = message
msg.attach(MIMEText(body, 'plain'))

#attachment
filename = "photo.jpg"
attachment = open("D:\ML Project\Basic Python\Final-Project\photo.jpg", "rb")

#encode
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
# attach the instance 'p' to instance 'msg'
msg.attach(p)

#loop untuk mengirim email sesuai daftar penerima
for email in daftar_kontak:
    s = smtplib.SMTP(server, port)
    s.starttls()
    s.login(sender, pword)
    text = msg.as_string()
    s.sendmail(sender, email, text)
    s.quit()