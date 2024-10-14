def hitungLangkah(n):
    langkah = 0  

    while n != 1:
        if n % 2 == 0:  
            n = n // 2
            print(float(n))
        else: 
            n = 3 * n + 1
            print(float(n))
        langkah += 1  

    return langkah


def hasil():
    try:
        
        n = int(input("Masukkan bilangan bulat positif: "))
        if n <= 0:
            print("Input tidak Valid")
        else:
            jumlahLangkah = hitungLangkah(n)
            print(f"Jumlah langkah: {jumlahLangkah}")

    except ValueError:
        print("Input tidak Valid")

hasil()
