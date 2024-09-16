usia = int(input("Masukkan usia : "))
keanggotaan = input("Apakah Anda anggota (ya/tidak) ? ")

if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000


if keanggotaan == "ya" or keanggotaan == "tidak":
    harga_diskon = harga * (0.8 if keanggotaan.lower() == "ya" else 1)
    if harga_diskon == 0:
        print("tiket anda gratis")
    else:
        print(f"Harga tiket adalah Rp {int(harga_diskon):,}")
else:
    print("Input keanggotaan salah")

    

