def gameHartaKarun():
    penggalian = 0
    bahaya = False

    while True:
        try:
            langkah = int(input("Masukkan jarak langkah yang ditempuh dalam meter (0 untuk berhenti): "))
            
            if langkah < 0:  # Jika langkah negatif, hentikan program
                print("Program dihentikan.")
                break
            
            if langkah == 0:  # Jika langkah adalah 0, berikan keputusan akhir
                break
            
            penggalian += langkah  # Menambahkan langkah ke total jarak
            
            if langkah > 20:  # Memeriksa langkah berbahaya
                bahaya = True
        
        except ValueError:  # Menangani input yang tidak valid
            print("Input tidak valid. Harap masukkan bilangan bulat.")
            continue

    # Menampilkan total jarak
    print(f"Total jarak: {penggalian} meter")

    # Keputusan akhir
    if bahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
        print("ada bahaya: ya")
    elif penggalian == 50:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
        print("ada bahaya: tidak")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")
        print("ada bahaya: tidak")

# Memanggil fungsi utama
gameHartaKarun()
