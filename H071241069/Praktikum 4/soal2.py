import random

def HartaKarun():
    total_jarak = 0
    bahaya = False

    
    while True:
        try:
            jarak = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if jarak <= 0:
                break
        
            if jarak > 20:
                bahaya = True
                print("Bruh anda menginjak jalan yang berbahaya")
            else:
                total_jarak += jarak
                print(f"Total jarak: {total_jarak} meter")
            
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
            
    if bahaya:
        print("Ada bahaya : Ya")
        print("Keputusan : Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Ada bahaya : Tidak")
        print("Keputusan : Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Keputusan : Tidak menemukan harta karun. Coba lagi!")

HartaKarun()