usia = int(input("Masukkan usia : "))

if usia <= 0:
    print("Usia tidak valid")
elif usia < 5:
    print("Tiket anda Gratis")
else:
    keanggotaan = input("Apakah Anda anggota (ya/tidak) ? ")
    if 5 <= usia <= 12:
        if keanggotaan == "ya":
            harga = 50000 * 0.8
        else:
            harga = 50000
    elif 13 <= usia <= 59:
        if keanggotaan == "ya":
            harga = 100000 * 0.8
        else:
            harga = 100000
        
    else:
        if keanggotaan == "ya":
            harga = 70000 * 0.8
        else:
            harga = 70000
        
    print(int(harga))