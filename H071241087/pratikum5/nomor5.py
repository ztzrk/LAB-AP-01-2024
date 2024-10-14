string = input("Masukkan string yang ingin dienkripsi: ")
perpindahan = int(input("Masukkan jumlah pergeseran (shift): "))

#ini proses enskripsinya 
enskripsi_string = ""

for char in string:
    if 'a' <= char <= 'z':  # untuk huruf kecil
        new_char = chr(((ord(char) - ord('a') + perpindahan) % 26) + ord('a'))
        enskripsi_string += new_char
    elif 'A' <= char <= 'Z':  # untuk huruf besar
        new_char = chr(((ord(char) - ord('A') + perpindahan) % 26) + ord('A'))
        enskripsi_string += new_char
    else: 
        enskripsi_string += char

print("Hasil enkripsi:", enskripsi_string)

#enskripsi caesar itu setiap huruf dalam teks digeser maju dalam huruf abcd-xyz