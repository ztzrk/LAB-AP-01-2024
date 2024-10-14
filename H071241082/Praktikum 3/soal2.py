import random

angka_rahasia = random.randint(1, 100)
percobaan = 5


i = 0  

while i < percobaan:
    tebakan = input(f"Percobaan ke-{i+1}, masukkan angka tebakan: ")
    
    if tebakan == '0':
        print("Permainan dihentikan. Terima kasih telah bermain!")
        break

    try:
        tebakan = int(tebakan)
    except ValueError:
        print("Input tidak valid! Masukkan angka antara 1 hingga 100.")
        i += 1
        if i == percobaan:
            print(f"Percobaan habis. Angka rahasianya adalah {angka_rahasia}.")
        continue 

    if tebakan < 1 or tebakan > 100:
        print("Hanya angka antara 1 hingga 100.")
        i += 1
        if i == percobaan:
            print(f"Percobaan habis. Angka rahasianya adalah {angka_rahasia}.")
        continue 

    i += 1  

    if tebakan == angka_rahasia:
        print("Selamat! Tebakan kamu benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
    
    if i == percobaan:
        print(f"Percobaan habis. Angka rahasianya adalah {angka_rahasia}.")
