totalLangkah = []

def hartaKarun():
    adaBahaya = False
    while True:
        try:
            a = int(input('Masukkan langkah (meter) atau 0 untuk selesai: '))  
        except ValueError:
            print("Masukkan angka yang valid.")
            continue
        
        if a > 20:
            adaBahaya = True
            #
        if a == 0:
            break
        
        totalLangkah.append(a)

    totalJarak = sum(totalLangkah)
    print(f'Total jarak: {totalJarak} meter')  
    print(f'Ada bahaya: {'Ada' if adaBahaya else 'Tidak Ada'}')

    if adaBahaya:
       print('Tidak aman untuk menggali harta karun. Coba lagi!') 
    elif totalJarak == 50:
        print('Aman! Kamu tepat menemukan harta karun dan menang!')
    else:
        print('Tidak menemukan harta karun. Coba lagi!')


hartaKarun()
