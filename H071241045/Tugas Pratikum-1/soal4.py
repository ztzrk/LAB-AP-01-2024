suhu =int(input("konversi suhu dari celcius ke kelvin, reamur dan fahrenheit\n masukkan suhu dalam celcius : "))
reamur = 4/5 * suhu
kelvin = suhu + 273.15
fahrenheit = (9/5 * suhu) + 32
reamur = round(reamur)
kelvin = round(kelvin)
fahrenheit = round(fahrenheit)
print(f"hasil konversi dari suhu {suhu} derajat celcius ke kelvin adalah : {kelvin}K")
print(f"hasil konversi dari suhu {suhu} derajat celcius ke reamur adalah : {reamur}R")
print(f"hasil konversi dari suhu {suhu} derajat celcius ke fahrenheit adalah : {fahrenheit}F")