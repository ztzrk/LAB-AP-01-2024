kata = input('kata : ')
#ini caranya menguji membalikkan kata
reversedKata = "".join(kata.split()).lower()

if reversedKata == reversedKata[::-1]: #slicing itu kyak mengambil kata misal -1 ambil dri blkng
    print("kata palindrom")
else:
    print("bukan kata palindrom")
