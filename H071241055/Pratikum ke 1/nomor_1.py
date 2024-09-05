harga_sekarang = float(input("Masukkan harga sekarang :"))
harga_kemarin = 105.0
pilihan = ['jual', 'tahan', 'beli']

persentasi = ((harga_sekarang - harga_kemarin)/harga_kemarin)*100
hasil = pilihan[(persentasi > -3) + (persentasi > 5)]

print(f"Perubahan persentasi harga saham adalah : {persentasi:.3f} %")
print(f"Rekomendasi Investasi : {hasil}")