def move_robot(N, M):
    for i in range(N):
        if i % 2 == 0:  # Jika baris genap, bergerak ke kanan
            for j in range(M):
                print(f"MOVE to ({i},{j})")
        else:  # Jika baris ganjil, bergerak ke kiri
            for j in range(M - 1, -1, -1):
                print(f"MOVE to ({i},{j})")

# Contoh penggunaan
N = 3
M = 4
move_robot(N, M)
