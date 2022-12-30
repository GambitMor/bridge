import unittest
from player import PlayerClass
from deck import Deck
from card import Card

class TestPlayer(unittest.TestCase):

    def test_take_from_deck(self):
        dummy_player = PlayerClass('bob')
        dummy_deck = Deck()
        dummy_player.take_from_deck(dummy_deck, 2)
        self.assertEqual(len(dummy_player.hand), 2)

    def test_sayHello(self):
        dummy_player = PlayerClass('bob')
        self.assertEqual(dummy_player.name, 'bob')
        self.assertEqual(dummy_player.hand, [])
        self.assertEqual(dummy_player.sayHello(), 'Hi! My name is bob')

    def test_put_card_on_table(self):
        dummy_player = PlayerClass('bob')
        dummy_deck = Deck()
        dummy_card = Card('S', 14)

        dummy_deck.deal(dummy_player)
        self.assertEqual(len(dummy_player.hand), 1)
        self.assertEqual(len(dummy_deck.open_cards), 0)

        dummy_player.put_card_on_table(dummy_deck, dummy_card)
        self.assertEqual(len(dummy_player.hand), 0)
        self.assertEqual(len(dummy_deck.open_cards), 1)

        # dummy_player.take_from_deck(dummy_deck, 5)
        # dummy_player.put_card_on_table(dummy_deck, dummy_card)
        # self.assertEqual(len(dummy_player.hand), 5)
        # self.assertEqual(len(dummy_deck.open_cards), 4)

    def test_find_card_by_name(self):
        dummy_card = Card('S', 14)
        dummy_player = PlayerClass('sam')
        dummy_player.hand.append(dummy_card)
        card = dummy_player.find_card_by_name('Ace of S')

        self.assertEqual(dummy_card.value, card.value)
        self.assertEqual(dummy_card.suit, card.suit)

    def test_make_move(self):
        dummy_deck = Deck()
        dummy_card = Card('C', 14)
        dummy_player = PlayerClass('bob')
        dummy_player.hand.append(dummy_card)

        self.assertEqual(len(dummy_player.hand), 1)
        self.assertEqual(len(dummy_deck.open_cards), 0)
        dummy_player.make_move(dummy_deck, dummy_card.to_str())

        self.assertEqual(len(dummy_player.hand), 0)
        self.assertEqual(len(dummy_deck.open_cards), 1)



if __name__ == '__main__':
    unittest.main()
