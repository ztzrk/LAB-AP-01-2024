# X = int(input("X = "))
# Y = int(input("y = "))

# for i in range(X):
#     if i % 2 == 0:
#         for j in range(Y):
#             print(f"MOVE to ({i},{j})")
#     else:
#         for j in range(Y-1, -1, -1):
#             print(f"MOVE to ({i},{j})")

X = int(input("X = "))
Y = int(input("Y = "))

# Tentukan arah iterasi untuk X dan Y
if X > 0:
    range_X = range(0, X)  # Iterasi dari 0 ke X jika positif
else:
    range_X = range(0, X, -1)  # Iterasi dari 0 ke X jika negatif

if Y > 0:
    range_Y_forward = range(0, Y)  # Iterasi maju jika Y positif
    range_Y_backward = range(Y-1, -1, -1)  # Iterasi mundur
else:
    range_Y_forward = range(0, Y, -1)  # Iterasi mundur jika Y negatif
    range_Y_backward = range(Y+1, 1)  # Iterasi maju (menuju nol)

# Loop utama
for i in range_X:
    if i % 2 == 0:
        for j in range_Y_forward:
            print(f"MOVE to ({i},{j})")
    else:
        for j in range_Y_backward:
            print(f"MOVE to ({i},{j})")
