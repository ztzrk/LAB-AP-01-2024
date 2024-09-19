nilai_akhir = int(input("Masukkan nilai akhir : "))

if nilai_akhir > 100 or kehadiran > 100:
    print("Nilai anda tidak valid")
    exit()

kehadiran = int(input("Masukkan presentase kehadiran : "))  
if kehadiran < 75:
    print("Tidak Lulus karena tidak memenuhi syarat kehadiran")
elif 75 >= kehadiran <= 100:
    if nilai_akhir >= 85 and nilai_akhir <= 100:
        predikat = "A"
    elif nilai_akhir >= 70 and nilai_akhir < 85:
        predikat = "B"
    elif nilai_akhir >= 60 and nilai_akhir < 70:
        predikat = "C"
    else:
        nilai_tugas_tambahan = int(input("Masukkan nilai rata-rata tugas tambahan : "))
        if nilai_tugas_tambahan >= 70:
            predikat = "C"
        else:
            predikat = "Tidak Lulus"
    print(f"Nilai Akhir {nilai_akhir}, Predikat : {predikat}")
else:
    print("Nilai anda tidak valid")