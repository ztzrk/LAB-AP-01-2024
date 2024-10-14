karakter = str(input("Masukkan Karakter : "))
kalimat = str(input("Masukkan Kalimat : "))
jawaban = ["tidak ditemukan dalam", "ditemukan dalam kalimat"]

hasil = jawaban[karakter in kalimat]

print(f'{karakter} {hasil} "{kalimat}"')