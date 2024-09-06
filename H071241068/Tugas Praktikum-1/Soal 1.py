#SOAL NOMOR 1
sahamKemarin = int(input('harga saham kemarin : '))

sahamSekarang = int(105)
persentase = ((sahamSekarang - sahamKemarin)/sahamKemarin)*100

print(f'Perubahan presentase harga saham: {persentase:.2f}%')


beli = persentase >5
tahan = 5>=persentase>=-3
jual = persentase<=-3

RekomendasiInvest = "Beli"*beli + "Tahan"*tahan + "Jual"*jual
print(f"Rekomendasi Investasi: {RekomendasiInvest}")
