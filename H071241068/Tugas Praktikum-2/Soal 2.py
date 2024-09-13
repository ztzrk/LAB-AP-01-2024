usia = int(input('Masukan usia: '))



if usia < 5 and usia > 0:
    print('Gratis')

elif usia < 0:
    print('Usia Tidak Valid')

else:
    anggota = (input('Apakah Anda Anggota (ya/tidak): '))
    if usia <= 12:
        harga = (50000)
        diskon = (20*harga)/100
        hargaAkhir = harga - diskon if anggota == 'ya' else harga 
    elif usia <= 59:
        harga = (100000)
        diskon = (20*harga)/100
        hargaAkhir = harga - diskon if anggota == 'ya' else harga 
    elif usia >= 60:
        harga = (70000)
        diskon = (20*harga)/100
        hargaAkhir = harga - diskon if anggota == 'ya' else harga 
    else:
        print('usia tidak valid')

    print(f"Harga tiket: Rp. {hargaAkhir:.0f}")
