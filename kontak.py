# kontak = open("kontak.txt", "r")

# daftar_kontak = []
# for email in kontak:
#     line = email.strip()
#     list = line.split()
#     daftar_kontak.append(list)

# kontak.close()

# print(daftar_kontak)

# with open("kontak.txt", "r") as kontak:
#     daftar_kontak = []
#     for email in kontak:
#         line = email.strip()
#         list = line.split()
#         daftar_kontak.append(list)

daftar_kontak = []

kontak = open("kontak.txt", "r")
for email in kontak:
    line = email.strip()
    list = line.split()
    daftar_kontak.append(list)

print(daftar_kontak)