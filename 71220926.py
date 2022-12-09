awal = int(input("Masukkan Awal deret : "))
akhir = int(input("Masukkan Akhir deret : "))

for i in range(awal, akhir) :
    if i % 2 == 1 :
        if i % 3 != 0 :
            if i % 6 != 0 :
                print(i,end=" ")