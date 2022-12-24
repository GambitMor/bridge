import unittest
from deck import Deck
from card import Card
from player import PlayerClass

class TestDeck(unittest.TestCase):

    def test_build(self):
        # dummy_card = Card(suit = 'S', val = 13)
        dummy_deck = Deck()
        # dummy_deck.build()
        self.assertEqual(len(dummy_deck.open_cards), 0)
        self.assertEqual(len(dummy_deck.closed_cards), 36)

    # def test_shuffle(self):
    #     # dummy_card = Card(suit = 'S', val = 13)
    #     dummy_deck = Deck()
    #     dummy_deck_one = dummy_deck.shuffle()
    #     self.assertEqual(dummy_deck.closed_cards, dummy_deck_one.closed_cards)

    # How to write that [i][j] != [i][j] after shuffle ?


    def test_deal(self):
        dummy_card = Card(suit = 'S', val = 13)
        dummy_deck = Deck()
        dummy_player = PlayerClass('bob')


        self.assertEqual(len(dummy_deck.closed_cards), 36)
        self.assertEqual(len(dummy_player.hand), 0)

        dummy_deck.deal(dummy_player)
        self.assertEqual(len(dummy_deck.closed_cards), 35)
        self.assertEqual(len(dummy_player.hand), 1)

    def test_put_first_card(self):
        dummy_card = Card(suit = 'S', val = 13)
        dummy_deck = Deck()
        dummy_player = PlayerClass('bob')
        print(dummy_deck.closed_cards)

        dummy_deck.deal(dummy_player)

        self.assertEqual(len(dummy_deck.closed_cards), 35)
        self.assertEqual(len(dummy_deck.open_cards), 0)

        dummy_deck.put_first_card()


        self.assertEqual(len(dummy_deck.closed_cards), 34)
        self.assertEqual(len(dummy_deck.open_cards), 1)







if __name__ == '__main__':
    unittest.main()
