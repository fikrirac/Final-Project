#Fungsi untuk membaca kontak dari daftar
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode="r", encoding="utf-8") as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split([1]))
    return names, emails

#Fungsi untuk membaca & return template file
from string import Template

def read_template(filename):
    with open(filename, "r", encoding="utf-8") as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

#Fungsi import & setup SMTP server
import smtplib

s = smtplib.SMTP(host="smtp.gmaill.com", port=587) #host & port bisa disesuaikan sama website yg ingin digunakan
s.starttls() #start TLS for security
s.login(MY_ADDRESS, PASSWORD) #autentikasi

names, emails = get_contacts("kontak.txt")
message_template = read_template("message.txt")

#import packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Untuk tiap kontak, kirim pesan
for name, email in zip(names, emails):
    msg = MIMEMultipart()

    #add in the actual person name to the message
    message = message_template.substitute(PERSON_NAME=name.title())

    #setup the parameters of the message
    msg["from"]=MY_ADDRESS
    msg["To"]=email
    msg['Subject']="This is TEST"

    #add in the message body
    msg.attach(MIMEText(message, "plain"))

    #send the message via the server set up earlier
    s.send_message(msg)

    del msg