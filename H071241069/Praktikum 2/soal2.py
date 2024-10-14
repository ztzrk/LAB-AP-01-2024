# Input
usia = int(input("Masukkan usia: "))

# harga tiket sesuai kategori usia
if usia < 0:
    print("Input tidak valid")
elif usia < 5:
    print("Harga tiket : Gratis")
else:
    anggota = input("Apakah Anda anggota (ya/tidak): ")
    if 5 <= usia <= 12:
        harga_tiket = 50000
    elif 13 <= usia <= 59:
        harga_tiket = 100000
    else:
        harga_tiket = 70000
    # diskon jika pengguna adalah anggota
    harga_tiket = harga_tiket - (harga_tiket*0.20) if anggota == "ya" else harga_tiket
    
    print(f"Harga tiket : Rp{int(harga_tiket)}")