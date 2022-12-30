import unittest
from rules import Rules
from deck import Deck
from card import Card
from player import PlayerClass
from game import Game

class TestDeck(unittest.TestCase):

	# def test_check_rules_six_true(self):
	# 	dummy_deck = Deck()
	# 	dummy_player = PlayerClass('sam')
	# 	dummy_card = Card(suit = 'S', val = 6)

	# 	while len(dummy_deck.open_cards) <= 4:
	# 		dummy_deck.put_first_card()

	# 	dummy_deck.open_cards.append(dummy_card)
	# 	last_open_card = dummy_deck.open_cards[-1]
	# 	# dummy_deck.closed_cards.append('S', 7)
	# 	dummy_player.take_from_deck(dummy_deck, 1)
	# 	dummy_six_d = Card(suit = 'D', val = 6)
	# 	dummy_player.hand.append(dummy_six_d)
	# 	self.assertEqual(len(dummy_player.hand), 2)
	# 	# last_open_card = dummy_card
	# 	dummy_rules = Rules(dummy_player, dummy_deck)
	# 	result = dummy_rules.check_rules_six()

	# 	self.assertEqual(result, True)

		

	# def test_check_rules_six_false(self):
	# 	dummy_deck = Deck()
	# 	dummy_player = PlayerClass('sam')
	# 	dummy_card = Card(suit = 'S', val = 10)
	# 	dummy_deck.shuffle(num=1)

	# 	while len(dummy_deck.open_cards) <= 4:
	# 		dummy_deck.put_first_card()

	# 	dummy_deck.open_cards.append(dummy_card)
	# 	last_open_card = dummy_deck.open_cards[-1]
	# 	# dummy_deck.closed_cards.append('S', 7)
	# 	dummy_player.take_from_deck(dummy_deck, 2)
	# 	self.assertEqual(len(dummy_player.hand), 2)
	# 	print('dummy_player.hand', dummy_player.hand)
	# 	# last_open_card = dummy_card
	# 	dummy_rules = Rules(dummy_player, dummy_deck)
	# 	result = dummy_rules.check_rules_six()

	# 	self.assertEqual(result, False)
	# 	self.assertEqual(len(dummy_player.hand), 3)

	def test_check_rules_seven_true(self):
		dummy_deck = Deck()
		dummy_player = PlayerClass('sam')
		bob = PlayerClass('bob')
		dummy_card = Card(suit = 'S', val = 7)
		dummy_card_second = Card(suit = 'C', val = 7)
		dummy_deck.shuffle(num=1)
		dummy_game = Game()

		# dummy_deck.put_first_card()
		dummy_deck.open_cards.append(dummy_card)
		dummy_deck.open_cards.append(dummy_card_second)
		dummy_player.take_from_deck(dummy_deck, 5)
		dummy_rules = Rules(dummy_player, dummy_deck)
		dummy_rules.check_rules_seven(dummy_card)
		result = dummy_rules.check_rules_seven(dummy_card_second)

		self.assertEqual(result, True)

		self.assertEqual(len(dummy_player.hand), 9)









		# self.assertEqual(len(dummy_player.hand), 2)
		# self.assertEqual(len(dummy_deck.closed_cards), 23)




if __name__ == '__main__':
	unittest.main()