a = int(input("Masukkan panjang sisi pertama: "))
b = int(input("Masukkan panjang sisi kedua: "))
c = int(input("Masukkan panjang sisi ketiga: "))

if a+b > c and a+c > b and b+c > a:
    if a == b and a == c and b == c:
        print('Segitiga Sama Sisi')
    elif a == b or a == c or b == c:
        print('Segitiga Sama Kaki')
    else:
        print('Segitiga Sembarang')

elif a < 1 or b < 1 or c < 1:
    print('Inputan tidak valid')
    
else:
    print('Tidak membentuk segitiga yang valid')
