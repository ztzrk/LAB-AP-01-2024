nilai_akhir = int(input("Masukkan nilai akhir: "))
if nilai_akhir < 0 or nilai_akhir > 100:
    print("Nilai tidak valid")
else:
    kehadiran = int(input("Masukkan persentase kehadiran: "))
    tugas_tambahan = int(input("Masukkan nilai tugas tambahan: "))

    if kehadiran < 75:
        hasil = "Tidak Lulus (Kehadiran kurang dari 75%)"
    elif nilai_akhir >= 85:
        hasil = "Lulus dengan Predikat A"
    elif nilai_akhir >= 70:
        hasil = "Lulus dengan Predikat B"
    elif nilai_akhir >= 60:
        hasil = "Lulus dengan Predikat C"
    else:
        if tugas_tambahan >= 70:
            hasil = "Lulus dengan Predikat C (karena tugas tambahan baik)"
        else:
            hasil = "Tidak Lulus"
    print("Hasil:", hasil)
