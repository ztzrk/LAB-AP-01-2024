string = input("Masukkan string : ")
pergeseran = int(input("Masukkan jumlah pergeseran : "))

cipher = ""

for huruf in string:
    if 'a' <= huruf <= 'z': 
        hurufbaru = chr((ord(huruf) - ord('a') + pergeseran) % 26 + ord('a'))
        cipher += hurufbaru
    elif 'A' <= huruf <= 'Z': 
        hurufbaru = chr((ord(huruf) - ord('A') + pergeseran) % 26 + ord('A'))
        cipher += hurufbaru
    else:
        cipher += huruf

print(f"Text : {string}")
print(f"Shift : {pergeseran}")
print(f"Cipher : {cipher}")