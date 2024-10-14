print("Konversi suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")
Celcius = float(input("Masukkan suhu Celcius yang akan dikonversi:"))
Kelvin = Celcius + 273.15
Reamur = Celcius * 4/5
Fahrenheit = Celcius * 9/5 + 32
print(f"Hasil konversi dari suhu derajat {Celcius} Celcius ke Kelvin adalah : {Kelvin}K")
print(f"Hasil konversi dari suhu derajat {Celcius} Celcius ke Reamur adalah : {Reamur}R")
print(f"Hasil konversi dari suhu derajat {Celcius} Celcius ke Fahrenheit adalah : {Fahrenheit}F")