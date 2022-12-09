pembatas = int(input("Masukkan Pembatas : "))
dilarang = int(input("Masukkan Angka Yang Dilarang : "))
kaa = '';

for i in range(pembatas) :
    if i != dilarang :
        kaa = kaa + str(i) + " "
    
print(kaa)