
n = input("Masukkan jumlah baris untuk belah ketupat: ")

if n.isdigit() != True:
    print("input haruslah angka")
    exit()
elif int(n) < 2:
    print("input haruslah melebihi 3")
    exit()
n = int(n)
if n % 2 == 0: #genapki
    for i in range(1, n, 2):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -2):
        print(" " * (n - i) + "* " * i)          
    else :
        for i in range(1, n, 2):
            print(" " * (n - i) + "* " * i)
        for i in range(n, 0, -2):
            print(" " * (n - i) + "* " * i)
