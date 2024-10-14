def hitung_langkah(n):
    langkah = 0
    langkah_list = []  # Untuk menyimpan setiap langkah
    while n != 1:
        langkah_list.append(float(n))  # Menyimpan langkah saat ini dalam float
        if n % 2 == 0:
            n //= 2  # bagi n dengan 2 jika genap
        else:
            n = 3 * n + 1  # kalikan n dengan 3 lalu tambahkan 1 jika ganjil
        langkah += 1
    langkah_list.append(float(1))  # Tambahkan langkah akhir, yaitu 1 dalam float
    return langkah, langkah_list

def main():
    try:
        n = int(input("Masukan angka: "))
        if n <= 0:
            print("Input tidak Valid")
            return
        
        langkah, langkah_list = hitung_langkah(n)

        # Menampilkan setiap langkah
        print("Langkah-langkah:")
        for step in langkah_list:
            print(step)
        
        print(f"Jumlah langkah: {langkah}")
        print(langkah,langkah_list)

    except ValueError:
        print("Input tidak Valid")

# Memanggil fungsi utama
main()

