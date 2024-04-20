from Models.models import Deck, Card, Player
# war rules
# 52 card deck shuffled and split into 2
# each player plays a card - whoever plays larger card takes both cards
# if both player plays the same value card
# both players set aside any number of cards as bets then play another card
# whoever has no cards left loses

# initializes the game by creating the players and deck objects
def initialize_game():
    deck = Deck()
    player_names = []

    # get player names - using length of player name list to get 2 names and as a limiter to keep input loop going twice
    while len(player_names) < 2:
        curr_player = len(player_names) + 1
        get_name = input(f"Please input the name for Player {curr_player}: ")
        player_names.append(get_name)
    
    print(f"Players {player_names[0].capitalize()} and {player_names[1].capitalize()} have joined the game. ")

    # instantiate player objects
    player_1 = Player(player_names[0].capitalize())
    player_2 = Player(player_names[1].capitalize())

    # deal cards to players
    deal(player_1, player_2, deck)

    # starts the game
    game(player_1, player_2)

# deals cards to players' hands
def deal(player_1, player_2, deck):

    # deal cards to players - each loop deals 2 cards that's why range is 52/2 = 26
    for i in range(26):
            player_1.add_cards_to_hand(deck.deal())
            player_2.add_cards_to_hand(deck.deal())

def get_war_num(player):

    # allows players to decide how many cards they want to bet for war
    while True:
        try:
            res = int(input(f"You currently have {len(player.hand)} cards. How many cards do you want to bet for war {player.name}: "))

        # checks to make sure players enter a number
        except ValueError:
            print("Enter a number dipshit")
        else:

            # checks if players try to bet more than they have
            if (res >= len(player.hand)):
                print(f"You can't do that {player.name} you would lose.")
            else:
                print(f"Roger. Betting {res} number of cards for {player.name}")
                return res

def game(player_1, player_2):
    
    # keeps game loop going
    game_on = True

    while game_on:

        #victory condition check
        if len(player_1.hand) == 0:
            print("Player 2 wins")
            break
        if len(player_2.hand) == 0:
            print("Player 1 wins")
            break
        
        # assumes war condition is true to make loop smoother - draw will be auto after betting of cards
        war = True

        while war:

            # drawing cards and adding them to the players' play areas
            card_1 = []
            card_1.append(player_1.play_card())
            card_2 = []
            card_2.append(player_2.play_card())


            print(f"Player {player_1.name} plays the {card_1[-1].rank} of {card_1[-1].suit} against Player {player_2.name}'s {card_2[-1].rank} of {card_2[-1].suit}")

            # checking for value between played cards
            # when a player wins a round, the palyed cards are given to the winner and war is set to false
            if card_1[-1].rank_value > card_2[-1].rank_value:
                print("Player 1 wins this round")
                player_1.add_cards_to_hand(card_1)
                player_1.add_cards_to_hand(card_2)
                war = False

            elif card_1[-1].rank_value < card_2[-1].rank_value:
                print("PLayer 2 wins this round")
                player_2.add_cards_to_hand(card_1)
                player_2.add_cards_to_hand(card_2)
                war = False
            else:

                # war condition fulfilled
                print("WARRRRRRRRRR")
                player_1_bet = get_war_num(player_1)
                player_2_bet = get_war_num(player_2)

                # add the bet cards to the play areas
                for i in range (player_1_bet):
                    card_1.append(player_1.play_card())
                for i in range (player_2_bet):
                    card_2.append(player_2.play_card())


if __name__ == '__main__':
    print("War is initializing. Please standby for violence.")
    initialize_game()
