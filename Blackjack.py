from Models.models import BJDeck, Card, Player

def game():
    deck = BJDeck()
    dealer = Player("Dealer")
    deal_cards(players, dealer, deck)
    get_bets(players)

    print(f"Dealer has a face up {dealer.hand[0].rank} of {dealer.hand[0].suit}")
    hitting(players, deck)
    dealer_val = sum_values(dealer.hand)
    print(f"Dealer has a value of {dealer_val}")
    while dealer_val < 17:
        dealer_val = adding_cards(dealer, deck)
        print(f"Dealer now has a value of {dealer_val}")
    print("Player status:")

    for p in players:
        if (dealer_val > 21 and p.blackjack < 22) or (p.blackjack > dealer_val and p.blackjack < 22):
            p.money += p.blackjack_bet * 2
            print(f"(Won) {p.name}: ${p.money} left")
        else:
            print(f" {p.name}: ${p.money} left")
        

def get_players():

    players = []

    name = ""

    while name != "done":\
        
        if name != "" and name != "done":
            p = Player(name)
            players.append(p)
        # get player name
        name = input(f"Please enter your name player {len(players) + 1}: ")
    
    print(f"Player gathering complete. Number of players is {len(players)}")
    return players

def deal_cards (players, dealer, deck):

    # initial dealing of cards to players
    for i in range(2):
        for p in players:
            card = deck.deal()
            p.add_cards_to_hand(card)
        dealer.add_cards_to_hand(deck.deal())

def get_bets(players):
    # get players to input how much they want to bet for their hand
    for p in players:
        while True:
            try:
                bet = int(input(f"How much do you want to bet for this hand {p.name}: "))
            except ValueError:
                print("Please enter a valid number value.")
            else:
                if bet > p.money:
                    print("You can't bet that much you poor fool")
                else:
                    print(f"Roger. Betting {bet} for {p.name}")
                    p.blackjack_bet = bet
                    p.money -= bet
                    break


def hitting(players, deck):

    for p in players:
        value = sum_values(p.hand)

        # check for first blackjack
        if value == 21 and len(p.hand) == 2:
            p.money += p.blackjack_bet
            print(f"Player {p.name} got blackjack! Yay you win")
            continue
        
        hit = True
        # while loop to allow palyers to keep hitting if they want
        while hit:
            value = sum_values(p.hand)

            # show players what cards they have in their hand
            print(f"Player {p.name} your hand is: ")
            for c in p.hand:
                print(f"{c.rank} of {c.suit}")
            print(f"for a total value of {value}")

            action = input("Do you want to take another card? (Y - N): ").upper()
            if action == 'N':
                # break out of hit loop to go to next player
                hit = False
            elif action == 'Y':
                new_sum = adding_cards(p, deck)
                if new_sum > 21:
                    print("Too bad you went over")
                    break
                else:
                    p.blackjack = new_sum
            else:
                print("Invalid input")

def adding_cards(player, deck):
    
    # check if player has ace due to dynamic ace value
    have_ace = False
    for c in player.hand:
        if c.rank == "Ace":
            have_ace = True

    # drawn card
    card = deck.deal()
    print(f"{player.name} has drawn a {card.rank} of {card.suit}")
    player.add_cards_to_hand(card)
    new_sum = sum_values(player.hand)

    # modify ace value if total sum goes over 21
    # playing the 1 or 11 rule
    if have_ace and new_sum > 21:
        new_sum -= 10
    
    return new_sum

def sum_values(player_hand):
    res = 0
    for h in player_hand:
        res += h.rank_value
    
    return res

if __name__ == "__main__":
    print("Let's play some blackjack. Everone starts with $10000")
    
    players = get_players()
    play = True
    while play:
        game()
        action = input("Do you want to keep playing? (Y - N): ").upper()
        if action == 'N':
            # break out of hit loop to go to next player
            play = False
        elif action == 'Y':
            continue
        else:
            print("Invalid input")