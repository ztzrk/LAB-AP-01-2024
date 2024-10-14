try:
    n = int(input("Masukkan jumlah baris: "))

    if n <= 2:
        print("Angka harus lebih dari 2")
        exit()
    else:
        mid = n // 2
# Bagian atas pola
    for i in range(mid + (n % 2)):
        print("  " * (mid - i) + "* " * (2 * i + 1))

# Bagian bawah pola
    for i in range(mid - 1, -1, -1):
        print("  " * (mid - i) + "* " * (2 * i + 1))
except ValueError:
    print("Input haruslah integer")