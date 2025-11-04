import pytest
import random


class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value
        return False


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


# Pytest-style tests for Card class
class TestCard:
    """Test suite for Card class"""
    
    def test_card_creation(self):
        """Test creating a card with suit and value"""
        card = Card("Hearts", "A")
        assert card.suit == "Hearts"
        assert card.value == "A"
    
    def test_card_suits(self):
        """Test creating cards with different suits"""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            card = Card(suit, "K")
            assert card.suit == suit
    
    def test_card_values(self):
        """Test creating cards with different values"""
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for value in values:
            card = Card("Hearts", value)
            assert card.value == value
    
    def test_card_representation(self):
        """Test card string representation"""
        card = Card("Spades", "Q")
        assert str(card) == "Q of Spades"
    
    def test_card_equality(self):
        """Test card equality comparison"""
        card1 = Card("Hearts", "A")
        card2 = Card("Hearts", "A")
        card3 = Card("Diamonds", "A")
        assert card1 == card2
        assert card1 != card3


# Pytest-style tests for Deck class
class TestDeck:
    """Test suite for Deck class"""
    
    def test_deck_initialization(self):
        """Test deck is initialized with 52 cards"""
        deck = Deck()
        assert len(deck.cards) == 52
    
    def test_deck_has_all_suits(self):
        """Test deck contains all four suits"""
        deck = Deck()
        suits = [card.suit for card in deck.cards]
        assert 'Hearts' in suits
        assert 'Diamonds' in suits
        assert 'Clubs' in suits
        assert 'Spades' in suits
    
    def test_deck_has_all_values(self):
        """Test deck contains all 13 values"""
        deck = Deck()
        values = [card.value for card in deck.cards]
        expected_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for value in expected_values:
            assert value in values
    
    def test_deck_cards_per_suit(self):
        """Test each suit has exactly 13 cards"""
        deck = Deck()
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            suit_cards = [card for card in deck.cards if card.suit == suit]
            assert len(suit_cards) == 13
    
    def test_deck_cards_per_value(self):
        """Test each value appears exactly 4 times (once per suit)"""
        deck = Deck()
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for value in values:
            value_cards = [card for card in deck.cards if card.value == value]
            assert len(value_cards) == 4
    
    def test_shuffle_changes_order(self):
        """Test shuffle changes the order of cards"""
        deck1 = Deck()
        deck2 = Deck()
        
        # Store original order
        original_order = [(c.suit, c.value) for c in deck1.cards]
        
        # Shuffle deck2
        deck2.shuffle()
        shuffled_order = [(c.suit, c.value) for c in deck2.cards]
        
        # Orders should be different (with very high probability)
        assert original_order != shuffled_order
    
    def test_shuffle_preserves_cards(self):
        """Test shuffle doesn't lose or duplicate cards"""
        deck = Deck()
        original_count = len(deck.cards)
        deck.shuffle()
        assert len(deck.cards) == original_count
        assert len(deck.cards) == 52
    
    def test_draw_returns_card(self):
        """Test draw returns a Card object"""
        deck = Deck()
        card = deck.draw()
        assert isinstance(card, Card)
    
    def test_draw_reduces_deck_size(self):
        """Test draw reduces deck size by 1"""
        deck = Deck()
        initial_size = len(deck.cards)
        deck.draw()
        assert len(deck.cards) == initial_size - 1
    
    def test_draw_multiple_cards(self):
        """Test drawing multiple cards"""
        deck = Deck()
        drawn_cards = []
        for i in range(5):
            card = deck.draw()
            drawn_cards.append(card)
        
        assert len(drawn_cards) == 5
        assert len(deck.cards) == 47
    
    def test_draw_from_empty_deck(self):
        """Test drawing from empty deck returns None"""
        deck = Deck()
        # Draw all cards
        for _ in range(52):
            deck.draw()
        
        # Try to draw from empty deck
        card = deck.draw()
        assert card is None
        assert len(deck.cards) == 0
    
    def test_draw_all_cards(self):
        """Test drawing all 52 cards"""
        deck = Deck()
        drawn_cards = []
        
        for _ in range(52):
            card = deck.draw()
            if card:
                drawn_cards.append(card)
        
        assert len(drawn_cards) == 52
        assert len(deck.cards) == 0
    
    def test_drawn_cards_are_unique(self):
        """Test all drawn cards are unique"""
        deck = Deck()
        drawn_cards = []
        
        for _ in range(52):
            card = deck.draw()
            if card:
                drawn_cards.append((card.suit, card.value))
        
        # Check all cards are unique
        assert len(drawn_cards) == len(set(drawn_cards))


# Parametrized tests
@pytest.mark.parametrize("suit", ['Hearts', 'Diamonds', 'Clubs', 'Spades'])
@pytest.mark.parametrize("value", ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
def test_all_card_combinations(suit, value):
    """Test creating all possible card combinations"""
    card = Card(suit, value)
    assert card.suit == suit
    assert card.value == value


@pytest.mark.parametrize("num_draws", [1, 5, 10, 26, 52])
def test_draw_multiple_times(num_draws):
    """Test drawing various numbers of cards"""
    deck = Deck()
    drawn = []
    
    for _ in range(num_draws):
        card = deck.draw()
        if card:
            drawn.append(card)
    
    assert len(drawn) == num_draws
    assert len(deck.cards) == 52 - num_draws


# Fixtures
@pytest.fixture
def fresh_deck():
    """Fixture providing a fresh deck"""
    return Deck()


@pytest.fixture
def shuffled_deck():
    """Fixture providing a shuffled deck"""
    deck = Deck()
    deck.shuffle()
    return deck


@pytest.fixture
def sample_card():
    """Fixture providing a sample card"""
    return Card("Hearts", "A")


# Tests using fixtures
def test_fixture_fresh_deck(fresh_deck):
    """Test fresh deck fixture"""
    assert len(fresh_deck.cards) == 52


def test_fixture_shuffled_deck(shuffled_deck):
    """Test shuffled deck fixture"""
    assert len(shuffled_deck.cards) == 52


def test_fixture_sample_card(sample_card):
    """Test sample card fixture"""
    assert sample_card.suit == "Hearts"
    assert sample_card.value == "A"


def test_draw_from_fresh_deck(fresh_deck):
    """Test drawing from fresh deck using fixture"""
    card = fresh_deck.draw()
    assert card is not None
    assert len(fresh_deck.cards) == 51


def test_draw_from_shuffled_deck(shuffled_deck):
    """Test drawing from shuffled deck using fixture"""
    card = shuffled_deck.draw()
    assert card is not None
    assert len(shuffled_deck.cards) == 51


# Integration tests
class TestCardDeckIntegration:
    """Integration tests for Card and Deck classes"""
    
    def test_deck_contains_card_objects(self):
        """Test deck contains Card objects"""
        deck = Deck()
        for card in deck.cards:
            assert isinstance(card, Card)
    
    def test_shuffle_and_draw(self):
        """Test shuffling then drawing cards"""
        deck = Deck()
        deck.shuffle()
        
        first_card = deck.draw()
        second_card = deck.draw()
        
        assert first_card != second_card
        assert len(deck.cards) == 50
    
    def test_multiple_decks_independent(self):
        """Test multiple decks are independent"""
        deck1 = Deck()
        deck2 = Deck()
        
        deck1.draw()
        
        assert len(deck1.cards) == 51
        assert len(deck2.cards) == 52


if __name__ == "__main__":
    # Run manual verification
    print("=" * 60)
    print("Manual Verification of Card and Deck Classes")
    print("=" * 60)
    
    # Test Card
    print("\nTesting Card class:")
    card1 = Card("Hearts", "A")
    print(f"✓ Created card: {card1}")
    
    card2 = Card("Spades", "K")
    print(f"✓ Created card: {card2}")
    
    # Test Deck
    print("\nTesting Deck class:")
    deck = Deck()
    print(f"✓ Deck created with {len(deck.cards)} cards")
    
    print("\nTesting shuffle:")
    original_top = deck.cards[-1]
    deck.shuffle()
    shuffled_top = deck.cards[-1]
    print(f"✓ Original top card: {original_top}")
    print(f"✓ After shuffle top card: {shuffled_top}")
    
    print("\nTesting draw:")
    for i in range(3):
        card = deck.draw()
        print(f"✓ Drew card {i+1}")
    print(f"✓ Remaining cards: {len(deck.cards)}")
    
    print("\n" + "=" * 60)
    print("All manual checks passed")
    print("\nRun with: pytest test_hw5_card.py -v")
    print("=" * 60)