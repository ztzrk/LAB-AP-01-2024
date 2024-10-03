import random

angka_rahasia = random.randint(1, 100)
percobaan = 0
max_percobaan = 5
kesalahan_input = 0
max_kesalahan_input = 5

print("Tebak angka kisaran 1 sampai 100, kamu hanya punya 5 percobaan.")
print("Ketik '0' untuk berhenti.")

while percobaan < max_percobaan and kesalahan_input < max_kesalahan_input:
    try:
        tebak = int(input("Masukkan tebakan Anda: "))
        if tebak == 0:
            print("Permainan dihentikan.")
            break
        elif tebak < 1 or tebak > 100:
            print("Angka tebakan hanya dari 1 sampai 100.")
        elif tebak > angka_rahasia:              
            print("Angka terlalu besar.")
        elif tebak < angka_rahasia:
            print("Angka terlalu kecil.")
        else:
            print("Selamat! Anda menebak angka yang benar!")
            break
        
        percobaan += 1
        print(f"Sisa percobaan: {max_percobaan - percobaan}")

    except ValueError:
        kesalahan_input += 1
        print(f"Tolong masukkan angka, bukan huruf atau karakter lain. Kesalahan input: {kesalahan_input}/{max_kesalahan_input}")
        
if percobaan == max_percobaan and tebak != angka_rahasia:
    print(f"Kesempatan habis, angka rahasia adalah {angka_rahasia}.")
elif kesalahan_input == max_kesalahan_input:
    print("Terlalu banyak kesalahan input, permainan dihentikan.")
