print("Konversi Detik ke Jam")
# input jumlah detik
detik = int(input("Masukkan jumlah detik : "))

# menghitung jam, menit dan detik
jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

# output
hasil = f"{jam:02}:{menit:02}:{detik:02}"
print(hasil)