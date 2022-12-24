import random
from card import Card

class Deck(object):
    def __init__(self):
        self.closed_cards = []
        self.open_cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.closed_cards:
            print (card.to_str())

    # Generate 36 cards
    def build(self):
        for suit in ['H', 'C', 'D', 'S']:
            for val in range(6, 15):
                self.closed_cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.closed_cards)
        # breakpoint()
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.closed_cards[i], self.closed_cards[randi] = self.closed_cards[randi], self.closed_cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.closed_cards)

    # Return the top card
    def deal(self, player):
        top_card = self.closed_cards.pop()
        player.hand.append(top_card)

    def put_first_card(self):
        top_card = self.closed_cards.pop()
        self.open_cards.append(top_card)

    def check_rules(self, card):
        rules = {
            '6': 'take',
            '7': 'take 2, skip',
            '8': 'take 1',
            'Jack': 'uni',
            'Ace': 'skip'
        }

        return True
