
total_harga = int(input("Masukkan total harga: "))
uang_ygdibayar = int(input("Masukkan uang yg dibayar: "))

kembalian = uang_ygdibayar - total_harga
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

print(f"Kembalian: {kembalian}")

for uang in pecahan:
    jumlah_lembar = kembalian // uang
    kembalian %= uang
    if jumlah_lembar > 0:
        print(f"{jumlah_lembar} lembar Rp {uang}")
    # if jumlah_lembar <  0:
    #     print("tidak valid")