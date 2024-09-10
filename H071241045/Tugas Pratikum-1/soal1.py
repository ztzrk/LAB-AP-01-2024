harga_saham_hari_ini       = float("105.0")
harga_saham_kemarin        = int(input("Masukkan harga saham kemarin: "))
perubahan_persentase_harga = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100
print(f"perubahan persentase harga saham: {perubahan_persentase_harga:.2f}%")
rekomendasi_investasi = ["jual", "tahan", "beli"]
rekomendasi = rekomendasi_investasi [(perubahan_persentase_harga > -3) + (perubahan_persentase_harga > 5)]
print(f"rekomendasi investasi: {rekomendasi}")