data = int(input('Masukkan jumlah data yang digunakan (GB): '))
jam = (input('Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? '))
pengguna = (input('Apakah Anda pengguna Personal atau Bisnis? '))

if data < 10:
    penggunaan = 'Ringan'
elif data < 50:
    penggunaan = 'Sedang'
elif data >= 50:
    penggunaan = 'Berat'

if penggunaan == 'Ringan' and jam == 'off-peak' and pengguna == 'personal':
    paket ='Paket yang sesuai: Paket A'
elif penggunaan == 'Sedang' and jam == 'peak' and pengguna == 'personal':
    paket ='Paket yang sesuai: Paket B'
elif penggunaan == 'Berat' and jam == 'peak':
    paket ='Paket yang sesuai: Paket C'
elif penggunaan == 'Berat' and jam == 'off-peak' and pengguna == 'bisnis':
    paket ='Paket yang sesuai: Paket D'
else:
    paket = 'Tidak ada paket yang cocok'

print(paket)
