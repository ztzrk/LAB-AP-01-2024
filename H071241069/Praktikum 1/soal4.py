print("Konersi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")

celcius = float(input("Masukkan Suhu dalam Celcius : "))

kelvin = celcius + 273.15
reamur = 4/5*celcius
fahrenheit = (celcius*9/5) + 32

print(f"Hasil Konversi dari{celcius} derajat Celcius ke Kelvin adalah : {kelvin}K")
print(f"Hasil Konversi dari{celcius} derajat Celcius ke Reamur adalah : {reamur}R")
print(f"Hasil Konversi dari{celcius} derajat Celcius ke Fahrenheit adalah : {fahrenheit}F")