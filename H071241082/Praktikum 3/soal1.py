
# n = int(input("Masukkan Jumlah Baris: "))

# # Bagian atas belah ketupat
# for i in range(n):
#     print("5" * (n - i - 1) + "* " * (i + 1))

# # Bagian bawah belah ketupat
# for i in range(n - 1):
#     print("5" * (i + 1) + "* " * (n - i - 1))

jumlah_baris = int(input("masukkan jumlah baris : "))

bintang = "* "

if jumlah_baris <= 0:
    print("masukkan angka yang benar")

elif jumlah_baris % 2 == 0:
    for i in range(jumlah_baris // 2):
        print("  " * (jumlah_baris - i - 4) + bintang * (2 * i + 1) )

    for i in  range((jumlah_baris // 2) - 1, -1, -1): 
        print("  " * (jumlah_baris - i - 4) + bintang * (2 * i + 1) )

elif jumlah_baris %  2 != 0:
    for i in range((jumlah_baris // 2) + 1 ):
        print("  " * (jumlah_baris - i - 4) + bintang * (2 * i + 1) )

    for i in  range((jumlah_baris // 2) - 1, -1, -1):
        print("  " * (jumlah_baris - i - 4) + bintang * (2 * i + 1) )