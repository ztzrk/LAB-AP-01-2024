
nilai = int(input("Masukkan nilai akhir: "))

if nilai < 0 or nilai > 100:
    print("Inputan nilai tidak valid!")
else:
    kehadiran = int(input("Masukkan persentase kehadiran: "))

    if kehadiran < 0 or kehadiran > 100:
        print("Inputan kehadiran tidak valid!")
    elif kehadiran < 75:
        print("Tidak Lulus karena kehadiran kurang dari 75%")
    else:
        match nilai:
            case n if 85 <= n <= 100:
                predikat = 'A'
                print(f"Lulus dengan Predikat {predikat}")
            case n if 70 <= n <= 84:
                predikat = 'B'
                print(f"Lulus dengan Predikat {predikat}")
            case n if 60 <= n <= 69:
                predikat = 'C'
                print(f"Lulus dengan Predikat {predikat}")
            case n if n < 60:
                tugas_tambahan = input("Apakah semua tugas tambahan diselesaikan dengan baik? (iya/tidak): ")
                if tugas_tambahan.lower() == 'iya':
                    predikat = 'C'
                    print(f"Lulus dengan Predikat {predikat} karena tugas tambahan diselesaikan dengan baik")
                else:
                    print("Nilai akhir anda kurang dari 60 dan tugas tambahan tidak diselesaikan dengan baik. Anda tidak lulus!!")



