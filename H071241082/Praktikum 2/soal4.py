
penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)?: ").lower()
jenis_pengguna = input("Masukkan jenis pengguna (Personal/Bisnis): ").lower()


if penggunaan_data < 10 and waktu_penggunaan == "off peak" and jenis_pengguna == "personal":
    paket = "Paket A"
elif 10 <= penggunaan_data <= 50 and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    paket = "Paket B"
elif penggunaan_data > 50 and waktu_penggunaan == "peak" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
    paket = "Paket C"
elif penggunaan_data > 50 and waktu_penggunaan == "off peak" and jenis_pengguna == "bisnis":
    paket = "Paket D"
else:
    paket = "Tidak ada paket yang cocok"

print("Paket yang sesuai:", paket)
