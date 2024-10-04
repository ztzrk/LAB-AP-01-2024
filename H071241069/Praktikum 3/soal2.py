import random

angka_rahasia = random.randint(1,100)
max_percobaan = 5
percobaan = 0

while percobaan < max_percobaan:
    tebakan = int(input("Masukkan tebakan Anda 0 untuk berhenti: "))

    if tebakan == 0:
        print("Permainan Dihentikan")
        break

    percobaan = percobaan + 1

    if tebakan == angka_rahasia:
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar")
    else:
        print("Angka terlalu kecil")
    
    if percobaan == max_percobaan:
        print("Kesempatan anda habis")