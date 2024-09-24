
populasi_a = int(input("Masukkan populasi awal Serangga A: "))
populasi_b = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

# Prediksi populasi selama N hari
for hari in range(1, jumlah_hari + 1):
    # Cek apakah hari adalah kelipatan 5, jika ya, predator memakan 10%
    if hari % 5 == 0:
        populasi_a *= 0.9
        populasi_b *= 0.9
        print(f"Hari {hari}: Predator memakan 10% populasi.")
    
    # Hari ganjil: pertumbuhan serangga+
    elif hari % 2 == 1:
        populasi_a *= 1.3
        populasi_b *= 1.5
    
    # Hari genap: penurunan populasi serangga
    else:
        populasi_a *= 0.8
        populasi_b *= 0.6
    
    if populasi_a < 1:
        populasi_a = 0
        
    if populasi_b < 1:
        populasi_b = 0
    
    # Tampilkan hasil untuk setiap hari
    print(f"Hari {hari}: Serangga A = {int(populasi_a)} Serangga B = {int(populasi_b)}")
