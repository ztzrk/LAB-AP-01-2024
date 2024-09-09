total_detik = int(input("Masukkan total detik : "))

jam = int(total_detik // 3600)
menit = int(( total_detik % 3600 ) // 60)
detik = int( total_detik % 60)

print(f'{jam:02d}:{menit:02d}:{detik:02d}')