kata = input("masukkan nama : ")
str = '';

for i in range(len(kata) + 1) :
    for j in range(i) :
        str += kata[j]
        
    print(str)
    str = ''
    
for i in range(len(kata)) :
    for j in range(len(kata) - 1 - i) :
        str += kata[j]
        
    print(str)
    str = ''