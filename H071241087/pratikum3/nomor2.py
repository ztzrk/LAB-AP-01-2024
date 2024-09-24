import random

angka_rahasia = random.randint(1, 100)
percobaan = 5

print("Tebak angka antara 1 hingga 100. Anda punya 5 kesempatan.")

for i in range(percobaan):  
    try:
        tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): ")) 
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        continue
    if tebakan == 0:
        print("Permainan dihentikan.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    elif tebakan < angka_rahasia:
        print("Angka terlalu kecil.")
    else:
        print("Selamat! Anda menebak angka dengan benar.")
        break
else:
    print(f"Kesempatan habis! Angka yang benar adalah {angka_rahasia}.")