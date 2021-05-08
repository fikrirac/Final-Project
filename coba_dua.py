import smtplib
import getpass

server = "smtp.gmail.com"
port = 587
sender = input("Masukkan Email: ")
password = getpass.getpass(prompt="Masukkan Password: ", stream=None)
message = "Hello, nice to meet you."

daftar_kontak = []

kontak = open("kontak.txt", "r")
for alamat in kontak:
    line = alamat.strip()
    list = line.split()
    daftar_kontak.append(list)

#loop untuk mengirim email sesuai daftar penerima
for email in daftar_kontak:
    s = smtplib.SMTP(server, port)
    s.starttls()
    s.login(sender, password)
    s.sendmail(sender, email, message)
    s.quit()

#loop untuk mengirim email sesuai daftar penerima
# with smtplib.SMTP(smtp_server, port) as server:
#     s.starttls()
#     s.login(sender, password)
#     with open("kontak.txt", "r") as kontak:
#         daftar_kontak = []
#         for email in kontak:
#             line = email.strip()
#             list = line.split()
#             daftar_kontak.append(list)
#             for email in daftar_kontak:
#                 s.sendmail(sender, email, message)
#     s.quit()