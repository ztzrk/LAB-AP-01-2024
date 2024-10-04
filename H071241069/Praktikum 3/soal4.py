total_harga = int(input("Masukkan total harga: "))
uang = int(input("Masukkan uang yang diberikan: "))

kembalian = uang - total_harga

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

for pecahan in pecahan_uang:
    jumlah_uang = kembalian // pecahan
    if jumlah_uang > 0:
        print(f"{jumlah_uang} lembar Rp. {pecahan:,}")
        kembalian %= pecahan