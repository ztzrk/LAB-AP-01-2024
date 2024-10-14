def main():
    try:
        n = int(input("Masukan angka: "))
        
        if n <= 0:
            raise ValueError
        
        steps = []
        hitung_langkah = 0
        
        while n != 1: #gnp
            if n % 2 == 0:
                n //= 2
            else: #gnjl
                n = 3 * n + 1
            
            steps.append(float(n))
            hitung_langkah += 1
        
        for step in steps:
            print(step)
        print(f"Jumlah langkah: {hitung_langkah}")

    except ValueError:
        print("Input tidak Valid")

main()
