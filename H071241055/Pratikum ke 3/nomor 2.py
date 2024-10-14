import random

hasil = random.randint(1, 100)
kesempatan = 5

while kesempatan > 0:
    try:
        tebakan = int(input("Masukkan tebakan anda (0 untuk berhenti): "))
            
        if tebakan == 0:
            print("Masih muda udah nyerah AWOKAWOK")
            break
        elif tebakan < hasil:
            print("kurrang gede bos")
            kesempatan -= 1
        elif tebakan > hasil:
            print("kurang kecil")
            kesempatan -= 1
        else:
            print("Anda Benar!")
            break
        if kesempatan == 0:
            print(f"Awokawok Cupu angkanya nih {hasil}")
            break
    except ValueError:
        print("input harus angka")
        kesempatan = kesempatan - 1
        if kesempatan == 0:
            print(f"Awokawok Cupu angkanya nih {hasil}")
            break

