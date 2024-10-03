def kalkulator():
    
    try:
        angka1 = float(input("Angka pertama: "))
        angka2 = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return
   
    operasi = input("Masukkan operasi (+, -, *, /): ")
    
    if operasi == "+":
        hasil = angka1 + angka2
        print(f"Hasil: {hasil:.0f}")
    elif operasi == "-":
        hasil = angka1 - angka2
        print(f"Hasil: {hasil:.0f}")
    elif operasi == "*":
        hasil = angka1 * angka2
        print(f"Hasil: {hasil:.0f}")
    elif operasi == "/":
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {hasil}")
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /.")

kalkulator()
