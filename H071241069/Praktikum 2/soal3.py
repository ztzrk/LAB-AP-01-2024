# input
nilai_akhir = int(input("Masukkan nilai akhir: "))

# menentukan kriteria kelulusan
if 0 <= nilai_akhir <= 100:
    persentase_kehadiran = int(input("Masukkan persentase kehadiran: "))
    if 85 <= nilai_akhir <= 100 and persentase_kehadiran >= 75:
        print("Lulus dengan Predikat A")
    elif 70 <= nilai_akhir <= 84 and persentase_kehadiran >= 75:
        print("Lulus dengan Predikat B")
    elif 60 <= nilai_akhir <= 69 and persentase_kehadiran >= 75:
        print("Lulus dengan Predikat C")
    elif nilai_akhir < 60 and persentase_kehadiran >= 75:
        tugas_tambahan = int(input("Masukkan nilai tugas tambahan: "))
        if tugas_tambahan > 70:
            print("Lulus dengan Predikat C")
        else:
            print("Tidak Lulus")
else:
    print("Input tidak valid")

