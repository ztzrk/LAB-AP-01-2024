def sandi_kaisar(teks, geser):
    hasil = ""
    for karakter in teks:
        if karakter.isalpha():  # Periksa apakah karakter adalah huruf
            offset_ascii = 65 if karakter.isupper() else 97  # Nilai ASCII 'A' atau 'a'
            hasil += chr((ord(karakter) - offset_ascii + geser) % 26 + offset_ascii)
        else:
            hasil += karakter  # Karakter non-alfabetik tetap tidak berubah
    return hasil

teks = input("Masukkan String: ")
geser = int(input("Masukkan jumlah pergeseran: "))
print("Teks :", teks)
print("Geser:", geser)
print("Sandi:", sandi_kaisar(teks, geser))