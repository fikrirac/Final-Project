kontak = open("kontak.txt", "r")

daftar_kontak = []
for email in kontak:
    line = email.strip()
    list = line.split()
    daftar_kontak.append(list)

kontak.close()

print(daftar_kontak)