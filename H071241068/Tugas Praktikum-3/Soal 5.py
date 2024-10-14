a = int(input("Masukkan populasi awal Serangga A: "))
b = int(input("Masukkan populasi awal Serangga B: "))
c = int(input("Masukkan jumlah hari: "))


for hari in range(1, c + 1):
    
   
    
    if hari % 2 != 0:
        a = a*1.3  
        b = b*1.5
    else:
        a = a*0.8  
        b = b*0.6

    if hari % 5 == 0:
        print(f"Hari {hari}: Predator memakan 10% populasi.")
        a = a*0.9  
        b = b*0.9
    
    if a<1:
        a = 0

    if b<1:
        b = 0

    c = int(a) if a>0 else 'telah habis'
    d = int(b) if b>0 else 'telah habis'
    print(f"Hari {hari}: {'Serangga A =' if a>0 else 'Serangga A'} {c}, {'Serangga B =' if b>0 else 'Serangga B'} {d}")
