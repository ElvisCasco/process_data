




























#Test 2.1 

from hw5_deck import Card

def test_card_initialization():
    card = Card("Hearts", "A")

    assert card.suit == "Hearts"
    assert card.value == "A"


def test_multiple_cards():
    
    card1 = Card("Hearts", "K")
    card2 = Card("Spades", "2")

    assert card1.suit != card2.suit
    assert card1.value != card2.value

#Test 2.2 

from hw5_deck import Card, Deck

def test_deck_initialization():
    deck = Deck()

    # Must have 52 cards
    assert len(deck.cards) == 52

    assert all(isinstance(card, Card) for card in deck.cards)


def test_deck_shuffle():
    deck = Deck()
    original_order = [(card.suit, card.value) for card in deck.cards]

    deck.shuffle()
    shuffled_order = [(card.suit, card.value) for card in deck.cards]

    assert original_order != shuffled_order


def test_deck_draw_removes_card():
    deck = Deck()
    initial_count = len(deck.cards)

    drawn_card = deck.draw()

    assert isinstance(drawn_card, Card)

    assert len(deck.cards) == initial_count - 1


def test_deck_draw_empty_deck():
    deck = Deck()

    for _ in range(52):
        deck.draw()

    assert deck.draw() is None


