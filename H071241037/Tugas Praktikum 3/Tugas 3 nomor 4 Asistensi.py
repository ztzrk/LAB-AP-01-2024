total_harga = int(input("Masukkan total harga yang harus dibayarkan: "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan oleh pelanggan: "))

kembalian = uang_diberikan - total_harga
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if kembalian < 0:
    print("Uang yang diberikan tidak cukup.")
elif kembalian == 0:
    print("Tidak ada kembalian.")
else:
    print(f"Kembalian: {kembalian} Rupiah")
    print("Rincian pecahan uang:")
    for uang in pecahan:
        jumlah_lembar = kembalian // uang  
        if jumlah_lembar > 0:
            print(f"{jumlah_lembar} lembar uang {uang} Rupiah")
        kembalian %= uang  
