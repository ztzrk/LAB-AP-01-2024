# harga saham hari ini
harga_saham_hari_ini = 105.0

# menginput harga saham kemarin
harga_saham_kemarin = float(input("Masukkan harga saham kemarin : "))

# perubahan persentase harga saham
perubahan_persentase = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin)*100

# rekomendasi investasi
rekomendasi = ["Tahan","Beli","Jual"]

indeks_rekomendasi = (perubahan_persentase > 5) - (perubahan_persentase < -3)

# output
print(f"Perubahan persentase harga saham : {perubahan_persentase:.2f}%")
print(f"Rekomendasi investasi : {rekomendasi[indeks_rekomendasi]}")