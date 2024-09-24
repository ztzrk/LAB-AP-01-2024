print("=== Program Prediksi Populasi Serangga ===\n")

try:
    populasi_a = int(input("Masukkan populasi awal Serangga A: ") or 0)
    populasi_b = int(input("Masukkan populasi awal Serangga B: ") or 0)

    if populasi_a < 0 or populasi_b < 0:
        raise ValueError("Input haruslah angka yang tidak negatif.")

    N = int(input("Masukkan jumlah hari (N) yang ingin diprediksi: ") or 0)

    if N < 0:
        raise ValueError("Input haruslah angka yang tidak negatif.")

    print(f"Hari 0: Serangga A = {int(populasi_a)}, Serangga B = {int(populasi_b)}")

    # Prediksi Populasi per Hari
    for hari in range(1, N + 1):
        if hari % 5 == 0:
            populasi_a *= 0.90
            populasi_b *= 0.90
            print(f"Hari {hari}: Predator datang! Populasi menurun 10%.")
        if hari % 2 == 1:  # Hari Ganjil
            populasi_a *= 1.30
            populasi_b *= 1.50
        else:  # Hari Genap
            populasi_a *= 0.80
            populasi_b *= 0.60


        if populasi_a == 0:
            populasi_a = "Serangga Telah Habis"
        if populasi_b == 0:
            populasi_b = "Serangga Telah Habis"
        
        print(f"Hari {hari}: Serangga A = {int(populasi_a)}, Serangga B = {int(populasi_b)}")

    # Hasil Akhir
    print(f"Setelah {N} hari, Populasi Serangga A = {int(populasi_a)}, Serangga B = {int(populasi_b)}")

except ValueError:
    print("Input haruslah bertipe integer.")

finally:
    print("Program selesai !")