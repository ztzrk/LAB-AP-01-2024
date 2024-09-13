print("konversi detik ke jam")
total_detik = int(input("Masukkan Jumlah detik = "))
jam = total_detik // 3600
hasil = total_detik % 3600 
menit = hasil // 60
detik = total_detik % 60
print(f"{jam:02}:{menit:02}:{detik:02} ")