def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")

    # Meminta input dari pengguna
    try:
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return

    operasi = input("Operasi (+,-, *, /): ")

    # Melakukan operasi sesuai input
    if operasi == '+':
        hasil = angka_pertama + angka_kedua
    elif operasi == '-':
        hasil = angka_pertama - angka_kedua
    elif operasi == '*':
        hasil = angka_pertama * angka_kedua
    elif operasi == '/':
        if angka_kedua == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        else:
            hasil = angka_pertama / angka_kedua
    else:
        print("Operasi tidak valid. Gunakan +,-, *, atau /")
        return

    print(f"Hasil: {int(hasil)}")

# Memanggil fungsi kalkulator
kalkulator()
