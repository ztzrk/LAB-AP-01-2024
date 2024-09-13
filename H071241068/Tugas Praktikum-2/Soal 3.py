nilai = int(input('Masukan nilai akhir: '))


if nilai < 101:
    kehadiran = int(input('Apakah persentase kehadiran: '))
    if kehadiran >= 75 :
        if nilai >= 85:
            predikat = "Lulus dengan predikat: A"
        elif nilai >= 70:
            predikat = "Lulus dengan predikat: B"
        elif nilai >= 60:
            predikat = "Lulus dengan predikat: C"
        elif nilai <= 60:
            nilaiT = int(input('Nilai semua tugas tambahan: '))
            predikat = 'Lulus dengan predikat: C' if nilaiT >= 70 else 'Tidak Lulus'
        print(predikat)


    elif kehadiran < 75:
        print('Tidak Lulus')

else:
    print('Nilai tidak valid')

    
    