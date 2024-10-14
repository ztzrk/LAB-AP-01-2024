usia = int(input("Masukkan usia :"))

if usia < 0:
    print("Inputan tidak valid")
else:
    match usia:
       case u if u >= 5 and u <= 12:
            kategori_harga = 50000
       case u if u >= 13 and u <= 59:
            kategori_harga = 100000
       case _:
            kategori_harga = 70000

    if usia < 5:
        print("Gratis")
    else:
        keanggotaan = input("Apakah anda anggota (iya/tidak): ").lower()
        anggota = kategori_harga * 80 // 100 if keanggotaan == "iya" else kategori_harga * 1
        print(f'Harga tiket : Rp.{anggota:,}')
