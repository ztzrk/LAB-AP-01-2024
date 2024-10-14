
a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))


if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("Segitiga tersebut adalah Segitiga Sama Sisi.")
    elif a == b or a == c or b == c:
        print("Segitiga tersebut adalah Segitiga Sama Kaki.")
    else:
        print("Segitiga tersebut adalah Segitiga Sembarang.")
else:
    print("Input tidak membentuk segitiga yang valid.")