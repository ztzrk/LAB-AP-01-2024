Karakter = input('Masukkan karakter :')
Kalimat = input('Masukkan kalimat: ')

result = f"{Karakter} Ditemukan dalam {Kalimat}" * (Karakter in Kalimat) + \
         f"{Karakter} Tidak ditemukan dalam {Kalimat}" * (Karakter not in Kalimat)   
print(result)