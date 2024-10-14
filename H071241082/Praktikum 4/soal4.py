def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")

    try:
        angka1 = float(input("Angka pertama: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return

    try:
        angka2 = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return

    operasi = input("Operasi (+, -, *, /): ")

    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        hasil = angka1 / angka2
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /")
        return
    hasil = int(hasil)
    print(f"Hasil: {hasil}")

kalkulator()

