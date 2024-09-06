#SOAL NOMOR 2
A = (input('Masukkan karakter: '))
B = (input('Masukkan kalimat: '))

ada = (A in B)
tidakAda = (A not in B)
output = "Ditemukan"*ada + "Tidak Ditemukan"*tidakAda
print(f"{A} {output} dalam {B}")
 