nilai_akhir = int(input("masukka nilai akhir : "))
persentase_kehadiran = int(input("persentase kehadiran : "))
tugastambahan = int(input('Masukkan Nilai Tambahan: '))

if nilai_akhir > 100:
    print('tidak valid')
else:
    if 85 <= nilai_akhir <= 100 and persentase_kehadiran >= 75: 
        predikat = 'Lulus dengan Predikat A'
    elif 70 <= nilai_akhir <= 84 and persentase_kehadiran >= 75:
        predikat = 'Lulus dengan Predikat B'
    elif 60 <= nilai_akhir <= 69 and persentase_kehadiran >= 75:
        predikat = 'Lulus dengan Predikat C'
    elif nilai_akhir < 60 and persentase_kehadiran >= 75:
        syaratkelulusan = (nilai_akhir + tugastambahan)/2
        predikat = 'Lulus dengan Predikat C'
    else :
        predikat = 'Tidak Lulus'

    print(predikat)