def acronym(kalimat):
    kata = kalimat.split()
    akronim = ''.join([kata[0]for kata in kata])
    return akronim

inputan = input("Masukkan kalimat: ")
print("Akronim:", acronym(inputan))
