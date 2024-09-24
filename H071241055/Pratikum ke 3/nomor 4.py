# Daftar pecahan uang yang tersedia, diurutkan dari terbesar ke terkecil
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

print("=== Program Penghitung Kembalian ===")

# Input Total Harga
while True:

# Input Jumlah Uang yang Diberikan
    try:
        total_harga = int(input("Masukkan total harga yang harus dibayarkan (Rp): "))
        if total_harga < 0:
            print("Total harga tidak bisa negatif. Silakan masukkan angka yang valid.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Masukkan angka integer.")
while True:
    try:
        uang_diberikan = int(input("Masukkan jumlah uang yang diberikan oleh pelanggan (Rp): "))
        if uang_diberikan < 0:
            print("Jumlah uang tidak bisa negatif. Silakan masukkan angka yang valid.")
            continue
        if uang_diberikan < total_harga:
            print("Uang yang diberikan kurang dari total harga. Silakan masukkan jumlah yang cukup.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Masukkan angka integer.")

# Menghitung Kembalian
kembalian = uang_diberikan - total_harga

print("\n--- Rincian Kembalian ---")
print(f"Total Kembalian: Rp {kembalian:,}")

if kembalian == 0:
    print("Tidak ada kembalian yang perlu diberikan.")
else:
    print("Jumlah lembaran uang yang harus diberikan:")

    # Menghitung jumlah lembaran untuk setiap pecahan uang
    for pecahan in pecahan_uang:
        jumlah = kembalian // pecahan
        if jumlah > 0:
            print(f"Rp {pecahan} :, x {jumlah} lembar")
            kembalian -= pecahan * jumlah

    # Jika masih ada sisa kembalian yang tidak dapat dikembalikan dengan pecahan yang tersedia
    if kembalian > 0:
        print(f"\nSisa kembalian yang tidak dapat dikembalikan: Rp {kembalian:,}")
