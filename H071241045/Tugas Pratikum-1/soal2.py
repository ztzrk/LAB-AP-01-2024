karakter = (input("masukkan karakter : "))
kalimat  = (input("masukkan kalimat : "))
pesan    = (karakter in kalimat) * (karakter + " Termasuk dalam Kata ") + (karakter not in kalimat) * (karakter + " Tidak Termasuk dalam kata ") + (kalimat)
print(pesan) 