string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")

hapus = 0

for i in string1:
    if i in string2:
        string2 = string2.replace(i, "", 1)
    else:
        hapus += 1

hapus += len(string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hapus}")