sisiA = int(input("Masukkan panjang sisi pertama : "))
sisiB = int(input("Masukkan panjang sisi kedua : "))
sisiC = int(input("Masukkan panjang sisi ketiga : "))

if sisiA + sisiB > sisiC and sisiA + sisiC > sisiB and sisiB + sisiC > sisiA:
    if sisiA == sisiB == sisiC :
        print("Segitiga sama sisi")
    elif sisiA == sisiB or sisiA == sisiC or sisiB == sisiC:
        print("Segitiga sama kaki")
    else:
        print("segitiga sembarang")
else:
    print("Segitiga tidak valid")