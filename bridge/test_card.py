import unittest
from deck import Deck
from card import Card
from player import PlayerClass

class TestCard(unittest.TestCase):

    def test_to_str(self):
        dummy_card = Card('S', 13)
        self.assertEqual(dummy_card.to_str(), 'King of S')
        dummy_card = Card('H', 14)
        self.assertEqual(dummy_card.to_str(), 'Ace of H')
        dummy_card = Card('C', 12)
        self.assertEqual(dummy_card.to_str(), 'Queen of C')
        dummy_card = Card('D', 11)
        self.assertEqual(dummy_card.to_str(), 'Jack of D')

    def test_check_match_true(self):
        dummy_card_open_cards = Card('D', 14)
        dummy_card_hand = Card('D', 8)
        dummy_player = PlayerClass('bob')
        dummy_deck = Deck()
        # dummy_deck.open_cards[-1] = dummy_card.to_str('8 of D')
        # self.check_match(dummy_player.hand, dummy_card.to_str())
        dummy_deck.open_cards.append(dummy_card_open_cards)
        dummy_player.hand.append(dummy_card_hand)

        result = dummy_card_hand.check_match(dummy_deck)
        self.assertEqual(result, True)

    def test_check_match_false(self):
        dummy_card_open_cards = Card('S', 11)
        dummy_card_hand = Card('D', 12)
        dummy_player = PlayerClass('bob')
        dummy_deck = Deck()

        dummy_deck.open_cards.append(dummy_card_open_cards)
        dummy_player.hand.append(dummy_card_hand)

        result = dummy_card_hand.check_match(dummy_deck)
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()
