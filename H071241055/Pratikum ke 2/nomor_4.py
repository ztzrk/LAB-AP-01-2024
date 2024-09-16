penggunaan_data = int(input("Masukkan penggunaan data per bulan (GB): "))
waktu_penggunaan = input("Masukkan waktu penggunaan (Off-Peak/peak): ").lower()
jenis_pengguna = input("Masukkan jenis pengguna (Personal/Bisnis): ").lower()

if penggunaan_data < 10 and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
    print(f"paket yang sesuai: paket A")
elif 10 <= penggunaan_data <= 50 and jenis_pengguna == "personal":
    print(f"paket yang sesuai: paket B")
elif penggunaan_data > 50 and waktu_penggunaan == "peak" and  (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
    print(f"paket yang sesuai: paket C")
elif penggunaan_data > 50 and waktu_penggunaan == "off-peak" and jenis_pengguna == "bisnis":
    print(f"paket yang sesuai: paket D")
else:
    print("Tidak ada paket yang cocok")