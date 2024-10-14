#Celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")
print("CELCIUS KE SATUAN LAIN")
celcius = float(input("Masukkan suhu dalam celcius : "))
print(f'suhu celcius adalah :{celcius}C')

#REAMUR
reamur = (4/5)*celcius
print (f'hasil konversi dari {celcius} derajat Celcius ke Reamur adalah : {reamur}R')

#FAHRENHEIT
fahrenheit = ((9/5) * celcius) + 32
print (f'hasil konversi dari {celcius} derajat Celcius ke Fahrenheit adalah : {fahrenheit}F')

#KELVIN
kelvin = celcius + 273
print(f'hasil konversi dari {celcius} derajat Celcius ke Kelvin adalah : {kelvin}K')

