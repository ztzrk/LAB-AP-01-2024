sahamToday = 105.0
sahamYesterday = float(input("Masukkan harga saham kemarin : "))

perubahanPersentase = ((sahamToday - sahamYesterday) / sahamToday) * 100
rekomendasiDict = {
    "Beli": perubahanPersentase > 5,
    "Tahan": perubahanPersentase < 5 and perubahanPersentase > -3,
    "Jual" : perubahanPersentase < -3,
}

for temp in rekomendasiDict:
    if rekomendasiDict[temp]:
        rekomendasi = temp
        break

print(f"perubahan persentase : {perubahanPersentase:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")