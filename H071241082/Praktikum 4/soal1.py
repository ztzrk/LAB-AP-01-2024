import random

def hitung_nilai_kartu(kartu):
    total = 0
    jumlah_as = 0
    for k in kartu:
        if k == 11:  # Kartu As
            jumlah_as += 1
        total += k
    # Jika ada As dan total lebih dari 21, As dihitung sebagai 1
    while total > 21 and jumlah_as > 0:
        total -= 10
        jumlah_as -= 1
    return total

def hasil_akhir(player_total, dealer_total):
    if player_total > 21:
        print("Anda kalah, kartu anda melebihi 21.")
    elif dealer_total > 21:
        print("Anda menang, dealer melebihi 21.")
    elif player_total > dealer_total:
        print("Anda menang!")
    elif player_total < dealer_total:
        print("Dealer menang!")
    else:
        print("Seri!")

def blackjack():
    print("Welcome to SISFOOOO 24!")
    
    player_cards = [random.randint(2, 11)]
    dealer_cards = [random.randint(2, 11)]
    
    print(f"Kartu anda sekarang adalah: {player_cards[0]}")
    
    while True:
        ambil_kartu = input("Apakah masih akan mengambil kartu? (y/n) ").lower()
        if ambil_kartu == 'y':
            player_cards.append(random.randint(2, 11))
            player_total = hitung_nilai_kartu(player_cards)
            print(f"Kartu anda sekarang adalah: {player_total}")
            
            if player_total > 21:
                print("Anda kalah!")
                return
        elif ambil_kartu == 'n':
            break
    
    dealer_total = hitung_nilai_kartu(dealer_cards)
    print(f"Kartu dealer adalah: {dealer_total}")
    
    while dealer_total < 17:
        dealer_cards.append(random.randint(2, 11))
        dealer_total = hitung_nilai_kartu(dealer_cards)
        print(f"Kartu dealer sekarang adalah: {dealer_total}")
    
    hasil_akhir(hitung_nilai_kartu(player_cards), dealer_total)

blackjack()