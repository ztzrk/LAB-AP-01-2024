N = int(input('Masukkan angka: '))
M = int(input('Masukkan angka: '))

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            print(f"MOVE to ({i}, {j})")
    else:
        for j in range(M - 1, -1, -1):
            print(f"MOVE to ({i}, {j})")
