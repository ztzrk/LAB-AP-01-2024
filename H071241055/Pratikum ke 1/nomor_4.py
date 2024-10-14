print("Konversi suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
celcius = int(input("Masukkan suhu dalam celcius : "))

kelvin = int(celcius + 273.15)
reamur = int((4/5)*celcius)
fahrenheit = int((9/5)*celcius + 32)

print(f"Hasil koversi suhu {celcius} derajat celcius ke Kelvin = {kelvin}K")
print(f"Hasil koversi suhu {celcius} derajat celcius ke Reamur = {reamur}R")
print(f"Hasil koversi suhu {celcius} derajat celcius ke Fahrenheit = {fahrenheit}F")