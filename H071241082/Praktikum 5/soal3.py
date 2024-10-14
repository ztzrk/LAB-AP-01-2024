# Menghitung Jumlah Minimum Penghapusan Karakter untuk Membuat Anagram

def jumlah_penghapusan_minimum(s1, s2):
    # Menghitung frekuensi karakter untuk setiap string
    frekuensi_s1 = {}
    frekuensi_s2 = {}
    for karakter in s1:
        if karakter in frekuensi_s1:
            frekuensi_s1[karakter] += 1
        else:
            frekuensi_s1[karakter] = 1
    for karakter in s2:
        if karakter in frekuensi_s2:
            frekuensi_s2[karakter] += 1
        else:
            frekuensi_s2[karakter] = 1

    # Menghitung perbedaan frekuensi antara dua string
    jumlah_penghapusan = 0
    for karakter in frekuensi_s1:
        if karakter in frekuensi_s2:
            jumlah_penghapusan += abs(frekuensi_s1[karakter] - frekuensi_s2[karakter])
        else:
            jumlah_penghapusan += frekuensi_s1[karakter]
    for karakter in frekuensi_s2:
        if karakter not in frekuensi_s1:
            jumlah_penghapusan += frekuensi_s2[karakter]

    return jumlah_penghapusan

# Input dari user
string_pertama = input("Masukkan string pertama: ")
string_kedua = input("Masukkan string kedua: ")

# Menghitung jumlah minimum penghapusan karakter
jumlah_penghapusan = jumlah_penghapusan_minimum(string_pertama, string_kedua)

print("Jumlah minimum penghapusan karakter untuk membuat anagram:", jumlah_penghapusan)