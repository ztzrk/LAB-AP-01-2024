

import random
x = random.randint(1, 100)
percobaan = 0
maxPercobaan = 5

while percobaan < maxPercobaan+1:
    if percobaan == maxPercobaan:
        print(f"Permainan berakhir. Angka yang benar adalah {x}.")
        break
    try:
        a = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    
    except ValueError:
        print('Input bukan angka')
        percobaan += 1
        continue
    

    if a == 0:
        print("Permainan dihentikan.")
        break

    percobaan += 1

    if a<1 or a>=100:
        print("Angka tidak valid.")
        
    elif a > x:
        print("Angka terlalu besar.")
    elif a < x:
        print("Angka terlalu kecil.")
    else:
        print("Selamat! Anda menebak angka dengan benar.")
        break


