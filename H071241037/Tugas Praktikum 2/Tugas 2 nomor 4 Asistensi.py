penggunaan_data = int(input("Masukkan penggunaan data per bulan (dalam GB): "))
waktu_penggunaan = input("Masukkan waktu penggunaan data (Peak/Off-Peak): ")
jenis_pengguna = input("Masukkan jenis pengguna (Personal/Bisnis): ")

if penggunaan_data < 10:
    if waktu_penggunaan == "Off-Peak" and jenis_pengguna == "Personal":
        paket = "Paket A"
    else:
        paket = "Tidak ada paket yang cocok"
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == "Peak" and jenis_pengguna == "Personal":
        paket = "Paket B"
    else:
        paket = "Tidak ada paket yang cocok"
else:  
    if waktu_penggunaan == "Peak":
        if jenis_pengguna == "Personal" or jenis_pengguna == "Bisnis":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    elif waktu_penggunaan == "Off-Peak":
        if jenis_pengguna == "Bisnis":
            paket = "Paket D"
        else:
            paket = "Tidak ada paket yang cocok"
    else:
        paket = "Tidak ada paket yang cocok"
        
print("Paket yang sesuai:", paket)
