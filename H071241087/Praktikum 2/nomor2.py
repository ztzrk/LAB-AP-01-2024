usia = int(input("masukkan usia : "))

if usia < 5 : 
    harga_tiket = "gratis"
    print(f"Harga Tiket : {harga_tiket}")
else:
    status = input('apakah anda anggota(ya/tidak) : ')
    if 5 <= usia <= 12 :
        harga_tiket = 50000
    elif 13 <= usia <= 59 :
        harga_tiket = 100000
    else :
        harga_tiket = 70000

    harga_tiket_final = harga_tiket * 0.8
    print(f"Harga Tiket : Rp. {harga_tiket_final:.0f}")

