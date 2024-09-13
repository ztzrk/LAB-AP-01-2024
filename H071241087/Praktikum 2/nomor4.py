jumlah_data = int(input("masukkan jumlah data yg digunakan(GB) : "))
penggunaan_waktu = input("offpeak or peak? : ")
status = input("personal or bisnis? : ")

if jumlah_data < 10 and penggunaan_waktu == "offpeak" and status == "personal":
    print("paket A") 
elif 10 <= jumlah_data <= 50 and penggunaan_waktu == "peak" and status == "personal":
    print("paket B")
elif jumlah_data > 50 and penggunaan_waktu == "peak" and status == ("personal" or "bisnis"):
    print("paket C")
elif jumlah_data > 50 and penggunaan_waktu == "offpeak" and status == "bisnis":
    print("paket D")

else :
    print("tidak ada paket yang cocok")
    
