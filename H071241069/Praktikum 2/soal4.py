# Input
penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (Off-Peak) atau di jam sibuk (Peak)? ")
jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis? ")

# Menentukan paket yang cocok
if penggunaan_data < 10 and waktu_penggunaan == "Off-Peak" and jenis_pengguna == "Personal":
    paket = "Paket A"
elif 10 <= penggunaan_data <= 50 and waktu_penggunaan == "Peak" and jenis_pengguna == "Personal":
    paket = "Paket B"
elif penggunaan_data > 50 and waktu_penggunaan == "Peak" and (jenis_pengguna == "Personal" or jenis_pengguna == "Bisnis"):
    paket = "Paket C"
elif penggunaan_data > 50 and waktu_penggunaan == "Off-Peak" and jenis_pengguna == "Bisnis":
    paket = "Paket D"
else:
    paket = "Tidak ada paket yang cocok"

# Output
print(f"Paket yang sesuai: {paket}")