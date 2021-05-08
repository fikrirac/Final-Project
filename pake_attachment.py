import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#basic
server = "smtp@gmail.com"
port = 587
sender = input("Masukkan Email: ")
password = input("Masukkan Password: ")
message = "semoga bisa dikirim amin."
receiver = "iniakuniseng.dua@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing email address 
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "Final Project"

#body email
body = message
msg.attach(MIMEText(body, 'plain'))

#attachment
filename = "foto.jpg"
attachment = open("D:\ML Project\Basic Python\Final-Project", "rb")

#encode
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
# attach the instance 'p' to instance 'msg'
msg.attach(p)
  
# creates SMTP session
s = smtplib.SMTP(server, port)
s.starttls()
s.login(sender, password)
text = msg.as_string()
s.sendmail(sender, receiver, text)

s.quit()