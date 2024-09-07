karakter = input("Masukkan karakter : ")
kalimat = input("Masukkan kalimat : ")

hasil = karakter in kalimat

print((f'{karakter} tidak ditemukan dalam "{kalimat}"', f'{karakter} ditemukan dalam "{kalimat}"')[hasil])




