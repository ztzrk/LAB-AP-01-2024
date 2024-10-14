while True:
    try:
        serangga_A = int(input('Masukkan populasi awal Serangga A: '))
        serangga_B = int(input('Masukkan populasi awal Serangga B: '))
        hari = int(input('Masukkan jumlah hari: '))
        if serangga_A < 0 or serangga_B < 0 or hari < 0:
            print("Populasi dan jumlah hari harus bernilai positif.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")

for i in range(1, hari + 1, 1):
    if i % 2 == 1:
        serangga_A = (serangga_A * 130) // 100
        serangga_B = (serangga_B * 150) // 100
        if i != 5:
            print(f'Hari {i}: Serangga A = {serangga_A:.0f}, Serangga B = {serangga_B:.0f}')
    else:
        serangga_A = (serangga_A * 80) // 100
        serangga_B = (serangga_B * 60) // 100
        print(f'Hari {i}: Serangga A = {serangga_A:.0f}, Serangga B = {serangga_B:.0f}')

    if i % 5 == 0:
        serangga_A = (serangga_A * 90) // 100
        serangga_B = (serangga_B * 90) // 100
        print(f'Hari {i}: Predator memakan 10% populasi')
        print(f'Hari {i}: Serangga A = {serangga_A:.0f}, Serangga B: {serangga_B:.0f}')
    if serangga_A <= 0 and serangga_B <= 0:
        print(f"Populasi serangga A atau B habis pada hari {i}. Menghentikan program.")
        break

if serangga_A > 0 and serangga_B > 0:
    print("Proses selesai. Berikut populasi terakhir:")
    print(f'Serangga A = {serangga_A:.0f}, Serangga B = {serangga_B:.0f}')