# Mengambil input dari pengguna
try:

    n = int(input("Masukkan angka : "))
    if n <3:
        print("input harus lebih besar dari 2")
    else:
        for i in range(1, ((n+2)//2)):
            print('  ' * ((n-3)-i) + '* ' * (2*i-1))
        for i in range(((n+1)//2), 0, -1):
            print('  ' * ((n-3)-i) + '* ' * (2*i-1))
except ValueError:
    print("Input harus bertipe integer")


