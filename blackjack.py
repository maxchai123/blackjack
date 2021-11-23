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

def hand_value(your_cards):
    hand_value = 0
    ace = ''
    for card in your_cards:
        # Case 1:
           # Card drawn is a Face Card
        if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
            if hand_value + 10 > 21:
                if ace == '1':
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
            ace += '1'
            if hand_value + 11 > 21:
                hand_value += 1
            else:
                hand_value += 11

        # Case 3:
            # Card drawn is a numbered card
        else:
            if hand_value + card[0] > 21:
                if ace == '1':
                    # We only need to do this once since every ace drawn
                    # after the first one will always have a value of 1.
                    # We effectively have to add some random string value
                    # so that we never go back into this part of the conditional.
                    hand_value = hand_value + card[0] - 10
                    ace = 'Off'
                else:
                    hand_value += card[0]
            else:
                hand_value += card[0]

    return hand_value

def bust(hand_value):
    return hand_value > 21

def twenty_one(hand_value):
    return hand_value == 21

def main():

    print("Welcome to this simple blackjack game!")
    print()
    print("Would you like to have fun [type: 'y']?")
    start = input("Or would you like to be boring [type: 'n']?")
    print()

    if start.lower() == 'y':
        # Initializing the deck and player/dealer cards
        deck = Deck()
        player_cards = deck.pull(2)
        dealer_cards = deck.pull(2)

        # Compute initial value of dealer + player hands
        player_hand_value = hand_value(player_cards)
        dealer_hand_value = hand_value(dealer_cards)

        # Only reveal one of the dealer's cards
        print("The dealer has the following face up card:")
        print(dealer_cards[0])
        print("")

        ################### Player logic ###################
        while player_hand_value < 21:

            print("You have the following cards:")
            print(player_cards)
            print("")
            print("Your hand value is {}".format(str(player_hand_value)))

            player_decision = input(("Would you like to hit [press 'h'] "
            "or stand [press 's']?"))
            print("")

            if player_decision == 's':
                break
            else:
                player_cards = player_cards + deck.pull(1)
                player_hand_value = hand_value(player_cards)

        if win(player_hand_value):
            print("Looks like you're too good at this game!")
            print("You have 21 with the following cards:")
            print(player_cards)


        if bust(player_hand_value):
            print("Sorry you busted with the following cards:")
            print(player_cards)
            print("Your hand value of {} is greater than 21!".format(str(player_hand_value)))

        ################### Dealer logic ###################
        # Check if dealer's cards are >= 17
        if dealer_hand_value >= 17:
            if bust(player_hand_value):
                print("Sorry, the dealer won with a hand value of:")
                print(dealer_hand_value)
                print("")
                print("You had a hand value of:")
                print(player_hand_value)
            elif player_hand_value > dealer_hand_value:
                print("Amazing, you won with a hand value of:")
                print(player_hand_value)
                print("")
                print("The dealer had a hand value of:")
                print(dealer_hand_value)
            elif player_hand_value < dealer_hand_value:
                print("Sorry, the dealer won with a hand value of:")
                print(dealer_hand_value)
                print("")
                print("You had a hand value of:")
                print(player_hand_value)
            else:
                print("You and the dealer tied!")
                print("Dealer hand value: {}".format(str(dealer_hand_value)))
                print("Your hand value: {}".format(str(player_hand_value)))


    else:
        print("Thanks! Have a nice day!")


main()
