usia = int(input("Masukkan usia: "))
if usia <=0:
    print("Usia tidak valid")
elif 1 <= usia < 5:
    print("Harga tiket  Gratis")
else:
    anggota = input("Apakah Anda anggota? (ya/tidak): ")
    if 5 <= usia <= 12:
        harga = 50000
    elif 13 <= usia <= 59:
        harga = 100000
    else:
        harga = 70000
    if harga != "Gratis" and anggota == "ya":
        harga = harga * 0.8
    if harga == "Gratis":
        print("Harga tiket yang harus dibayar: Gratis")
    else:
        print(f"Harga tiket yang harus dibayar: Rp{int(harga)}")
