import random

def kartu_acak():
    return random.randint(1, 11)

def permainan_blackjack():
    print("Welcome to Blackjack!")
    
    kartu_pemain = []
    kartu_dealer = []
    
    kartu_pemain.append(kartu_acak())
    kartu_dealer.append(kartu_acak())
    
    print(f"Kartu anda sekarang adalah: {sum(kartu_pemain)}")

    # Proses pemain untuk mengambil kartu tambahan
    while sum(kartu_pemain) < 21:
        pilih = input("Apakah masih akan mengambil kartu? (y/n) ")
        if pilih.lower() == 'y':
            kartu_pemain.append(kartu_acak())
            print(f"Kartu anda sekarang adalah: {sum(kartu_pemain)}")
            if sum(kartu_pemain) > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        else:
            break

    print(f"Kartu dealer sekarang adalah: {sum(kartu_dealer)}")
    
    # Proses dealer mengambil kartu hingga kartu dealer >= 17
    while sum(kartu_dealer) < 17:
        kartu_dealer.append(kartu_acak())
        print(f"Kartu dealer sekarang adalah: {sum(kartu_dealer)}")
    
    # Menentukan pemenang
    if sum(kartu_dealer) > 21:
        print("Dealer melebihi 21, Anda menang!")
    elif sum(kartu_pemain) > sum(kartu_dealer):
        print("Anda menang!")
    elif sum(kartu_pemain) == sum(kartu_dealer):
        print("Seri!")
    else:
        print("Dealer menang!")

# Jalankan permainan
permainan_blackjack()
