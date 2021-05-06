import smtplib
import csv

smtp_server = "smtp@gmail.com"
port = 587
sender = input("Masukkan Email: ")
password = input("Masukkan Password: ")
message = "Hello, nice to meet you."

#membuat list email
# kontak = open("kontak.txt", "r")

# daftar_kontak = []
# for email in kontak:
#     line = email.strip()
#     list = line.split()
#     daftar_kontak.append(list)

# kontak.close()

#loop untuk mengirim email sesuai daftar penerima
s = smtplib.SMTP(smtp_server, port)
s.starttls()
s.login(sender, password)
daftar_kontak = []
for email in kontak:
    line = email.strip()
    list = line.split()
    daftar_kontak.append(list)
    for email in daftar_kontak:
        s.sendmail(sender, email, message)
        s.quit()


# with smtplib.SMTP(smtp_server, port) as server:
#     s.starttls()
#     s.login(sender, password)
#     with open("kontak.csv") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for name, email in reader:
#             s.sendmail(
#                 sender,
#                 email,
#                 message.format(name=name)
#             )