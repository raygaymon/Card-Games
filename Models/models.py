from random import shuffle

# static values for card and deck creation purposes
VALUES = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 11, 'Queen' : 12, 'King' : 13, 'Ace' : 14}
BLACKJACK_VALUES = {'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10, 'Ace' : 11}
SUITS = ("Diamond", "Clubs", "Hearts", "Spades")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card():

    def __init__(self, suit : str, rank : str):
        self.suit = suit
        self.rank = rank.capitalize()
        self.rank_value = VALUES[rank]
    
    def __str__ (self):
        return f"Card is the {self.rank} of {self.suit}"

class BJDeck(Card):
    
    def __init__(self):
        self.deck = []
        # using the suit and rank tuples to create all 52 needed cards then adding them to the deck list
        for s in SUITS:
            for r in RANKS:
                bjc = Card(s, r)
                bjc.rank_value = BLACKJACK_VALUES[bjc.rank]
                self.deck.append(bjc)
        shuffle(self.deck)

    def __str__ (self):
        print(f"Current deck order is:\n{self.deck}")
    

    def shuffle_deck(self):
        shuffle(self.deck)
        print("Deck shuffled")

    # to deal cards to players from the top of the deck
    def deal(self):
        return self.deck.pop()   

class Deck(Card):
    
    def __init__(self):
        self.deck = []

        # using the suit and rank tuples to create all 52 needed cards then adding them to the deck list
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        shuffle(self.deck)

    def __str__ (self):
        print(f"Current deck order is:\n{self.deck}")
    

    def shuffle_deck(self):
        shuffle(self.deck)
        print("Deck shuffled")

    # to deal cards to players from the top of the deck
    def deal(self):
        return self.deck.pop()


class Player():
    
    def __init__ (self, name : str):
        self.name = name
        self.hand = []
        self.blackjack = 0
        self.money = 10000
        self.blackjack_bet = 0
    
    def __str__ (self):
        print(f"Player {self.name} has entered the chat with {len(self.hand)} cards left")
    
    # to add dealt cards or played cards to the players' hand
    def add_cards_to_hand(self, pile):
        if type(pile) == type([]):
            self.hand.extend(pile)
        # extend add list to existing list without creating a new list
        else:
            self.hand.append(pile)
    
    # to play the card onto the field
    def play_card(self):
        return self.hand.pop()