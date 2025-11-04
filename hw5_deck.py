# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.



import random
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) 
                      for suit in suits
                      for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            card = self.cards.pop()
            print(f'Drawn card: {card.value} of {card.suit}')
            return card
        else:
            print('No more cards in the deck.')
            return None
        
# Testing:
deck = Deck()
deck.shuffle()
deck.draw()
deck.draw()
deck.draw()

count = len(deck.cards)
print(f'Cards left in deck: {count}')