N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))


for i in range(N):
    if i % 2 == 0:  # Baris genap
        for j in range(M):
            print(f"Posisi ke ({i},{j})")
    else:  # Baris ganjil
        for j in range(M-1, -1, -1):
            print(f"Posisi ke ({i},{j})")

