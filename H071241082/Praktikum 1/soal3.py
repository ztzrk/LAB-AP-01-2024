waktu = int(input("Masukkan Detik : "))

jam = waktu // 3600
menit = (waktu % 3600 ) // 60
detik = waktu % 60

print(f'{jam:2}:{menit:02}:{detik:02}')

