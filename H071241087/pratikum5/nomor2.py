kalimat = input("Masukkan kalimat: ")

kata_kata = kalimat.split()

akronim = ''.join(kata[0].upper() for kata in kata_kata)

print("Akronim:", akronim)
#upper itu mengubah ke huruf besar