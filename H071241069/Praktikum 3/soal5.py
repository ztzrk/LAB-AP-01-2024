# Input
populasi_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_B = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

for i in range(1, jumlah_hari + 1):
    if i % 2 != 0:  # Hari ganjil
        populasi_A = int(1.30 * populasi_A)
        populasi_B = int(1.50 * populasi_B)
    else:  # Hari genap
        populasi_A = int(0.80 * populasi_A)
        populasi_B = int(0.60 * populasi_B)
        
    # setiap 5 hari predator datang
    if i % 5 == 0:
        populasi_A = int(0.90 * populasi_A)
        populasi_B = int(0.90 * populasi_B)
        print(f"Hari {i}: Predator memakan 10% populasi.")
        
    print(f"Hari {i}: Serangga A = {populasi_A}, Serangga B = {populasi_B}")

