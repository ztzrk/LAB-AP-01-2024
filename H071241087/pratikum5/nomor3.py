string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")

# Menghitung frekuensi karakter dari string pertama
freq1 = {}
for char in string1:
    if char in freq1:
        freq1[char] += 1
    else:
        freq1[char] = 1

# Menghitung frekuensi karakter dari string kedua
freq2 = {}
for char in string2:
    if char in freq2:
        freq2[char] += 1
    else:
        freq2[char] = 1

# Menghitung jumlah karakter yang perlu dihapus
deletions = 0

# Mengambil semua karakter unik dari kedua string
all_chars = set(freq1.keys()).union(set(freq2.keys()))

# Menghitung penghapusan yang diperlukan
for char in all_chars:
    count1 = freq1.get(char, 0)
    count2 = freq2.get(char, 0)
    deletions += abs(count1 - count2)

# Menampilkan hasil
print("Jumlah minimum penghapusan karakter:", deletions)