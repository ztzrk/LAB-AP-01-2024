string_input = input("Masukkan string Anda: ")

substrings = []

for panjang in range(1, len(string_input) + 1):
    for i in range(len(string_input) - panjang + 1):
        substring = string_input[i:i + panjang]
        substrings.append(substring)

# Mencetak semua substring yang ditemukan
print("Substring yang ditemukan:")
for substring in substrings:
    print(substring)