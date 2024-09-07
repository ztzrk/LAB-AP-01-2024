# (harga saat ini)
harga_hari_ini = 105
print (int(6/3))

# harga saham kemarin
harga_kemarin = int(input("Masukkan harga saham kemarin: "))

# Menghitung perubahan persentase harga
perubahan_persen = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

#persentase
print(f"Perubahan persentase harga saham: {perubahan_persen:}%")

rekomendasi = (perubahan_persen > 5) * "Beli" + (5 >= perubahan_persen >= -3) * "Tahan" + (perubahan_persen < -3) * "Jual"
print(f"Rekomendasi Investasi: {rekomendasi}")
