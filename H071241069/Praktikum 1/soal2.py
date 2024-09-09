# input
karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

hasil = karakter in kalimat
# output
print((f'{karakter} tidak ditemukan dalam "{kalimat}"',f'{karakter} merupakan bagian dari "{kalimat}"')[hasil])