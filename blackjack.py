import random

class Deck:
    '''Standard 52 card deck'''
    def __init__(self):
        '''Initialize all 52 cards'''
        self.suits = ['d', 'h', 's', 'c']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append((rank, suit))

    def pull(self, number_of_cards):
        your_cards = []
        for card in range(number_of_cards):
            # Randomly selecting a card
            selected_card = random.choices(self.cards)[0]
            # Adding the card to our hand
            your_cards.append(selected_card)
            self.cards.remove(selected_card)
        return your_cards
deck = Deck()
#print(deck.cards)
cards = deck.pull(2)
print(cards)
print(deck.cards)
