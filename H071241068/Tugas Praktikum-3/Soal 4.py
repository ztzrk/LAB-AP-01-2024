a = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

harga = int(input("Masukkan total harga: "))
uang = int(input("Masukkan uang yang diberikan: "))


kembalian = uang - harga

if uang<harga:
    print('uang anda kurang')  

else: 
    for i in a:
        lembar = kembalian // i  
        if lembar > 0:
            print(f"{lembar} lembar Rp {i:,}")
        kembalian %= i 