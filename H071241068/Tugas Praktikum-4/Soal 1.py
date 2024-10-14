import random

def blackjack():
    print("Welcome to Blackjack!")

    deck = [1,2,3,4,5,6,7,8,9,10,11]

    kartuPemain = [random.choice(deck)]
    kartuDealer = [random.choice(deck)]

    while True:
        print(f"Kartu anda sekarang adalah: {sum(kartuPemain)}")
        if sum(kartuPemain) > 21:
            print("Anda kalah!")
            return
        
        pilihan = input("Apakah masih akan mengambil kartu? (y/n): ")
        if pilihan == 'y' or pilihan == 'Y':
            if not deck:
                print("Tidak ada kartu tersisa di deck!")
                break
            kartuBaru = random.choice(deck)
            kartuPemain.append(kartuBaru)
            deck.remove(kartuBaru)  
        elif pilihan == 'n' or pilihan == 'N':
            break
        else:
            print('Masukkan y/n')


    print(f"Kartu dealer adalah: {sum(kartuDealer)}")
    
    while sum(kartuDealer) < 17:
        if not deck:
            print("Tidak ada kartu tersisa di dek!")
            break
        kartuBaru = random.choice(deck)
        kartuDealer.append(kartuBaru)
        deck.remove(kartuBaru)
        print(f"Kartu dealer sekarang adalah: {sum(kartuDealer)}")


    totalPemain = sum(kartuPemain)
    totalDealer = sum(kartuDealer)

    if totalDealer > 21 or totalPemain > totalDealer:
        print("Anda menang!")
    elif totalPemain == totalDealer:
        print("Seri!")
    else:
        print("Anda kalah!")


blackjack()
