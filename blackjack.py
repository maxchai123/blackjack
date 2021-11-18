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
            # Since the choices method returns a list, we add the [0]
                # to get the value in the list
                # Now, we'll get just the tuple
            selected_card = random.choices(self.cards)[0]
            # Adding the card to our hand
            your_cards.append(selected_card)
            self.cards.remove(selected_card)
        return your_cards

def hand_value(self, your_cards):
    hand_value = 0
    ace = ''
    for card in your_cards:
        # Case 1:
           # Card drawn is a Face Card
        if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
            if hand_value + 10 > 21:
                if ace == 'y':
                    # We don't add anything because we would add 10
                    # for the face card and then subtract 10
                    # to reduce the ace's value from 11 to 1
                    pass
                else:
                    hand_value += 10
            else:
                hand_value += 10

        # Case 2:
            # Card drawn is an Ace
        elif card[0] == 'A':
            ace = 'y'
            if hand_value + 11 > 21:
                hand_value += 1
            else:
                hand_value += 11

        # Case 3:
            # Card drawn is a numbered card
        else:
            if hand_value + card[0] > 21:
                if ace == 'y':
                    hand_value = hand_value + card[0] - 10
                else:
                    hand_value += card[0]
            else:
                hand_value += card[0]
                
    return hand_value




deck = Deck()
print(deck.cards)
print()
#cards = deck.pull(2)
test_cards = [('A','d'), ('K', 'h'), (5,'d')]
#print(cards)
#print()
#print(deck.cards)
print(deck.hand_value(test_cards))
