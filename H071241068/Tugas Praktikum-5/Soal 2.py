def akronim(a):
    perkata = a.split()
    hasil = []

    for kata in perkata:
        b = kata[0]
        c = b.upper()
        hasil.append(c)
    
    print (''.join(hasil))

akronim(input('Masukkan Kalimat:'))