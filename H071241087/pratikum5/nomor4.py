string = input("Masukkan sebuah string: ")

for panjang in range(1, len(string) + 1):
    for i in range(len(string) - panjang + 1):
        substring = string[i:i + panjang]
        print(substring)