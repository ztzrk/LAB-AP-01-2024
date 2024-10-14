kalimat = input("Masukkan kalimat: ")
    
kata = kalimat.split()

akronim = ""

for i in kata:
    akronim = akronim + i[0].upper() 

print(akronim)