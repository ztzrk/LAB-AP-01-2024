#SOAL 4
C = int(input("""Konversi Suhu dari Celcius ke Kelvin, Reamur dan Farenheit
Masukkan suhu dalam Celcius: """))

K = C+273
R = C*4/5
F = (C*9/5) + 32

print(f"""Suhu dalam Kelvin: {K:.0f}K
Suhu dalam Reamur: {R:.0f}R
Suhu dalam Farenheit: {F:.0f}F""")
       