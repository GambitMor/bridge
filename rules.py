import random
# from card import Card
from player import PlayerClass
# from game import Game
from deck import Deck


class Rules(object):
    def __init__(self, player, deck):
        self.player = player
        self.myDeck = deck

    def check_rules_six(self, card):
        last_open_card = self.myDeck.open_cards[-1]
        print('last_open_card=', last_open_card)
        print('==============================')
        print('p hand=', self.player.hand)
        for c in self.player.hand:
            if c.suit == last_open_card.suit or c.value == last_open_card.value or c.value == 11: #or c.value == 6:
                return True
            else:
                self.player.take_from_deck(self.myDeck)
                print('no 6 and no jack')
                return False


    def check_rules_seven(self, card):
        last_open_card = self.myDeck.open_cards[-1]
        # last_open_card_second = self.myDeck.open_cards[-2]
        # last_open_card_third = self.myDeck.open_cards[-3]
        # last_open_card_fourth = self.myDeck.open_cards[-4]
        print(last_open_card)
        if (last_open_card.value == card.value and 
            last_open_card.value == 7 and
            self.myDeck.open_cards[-2].value == card.value == 7):
            print('2 seven detected, taking 4 cards, changing move', self.player.hand)
            # game.change_move()
            self.player.take_from_deck(self.myDeck, 4)
            # game.change_move()
            return True

        if last_open_card.value == card.value and last_open_card.value == 7:
            # game.change_move()
            self.player.take_from_deck(self.myDeck, 2)
            print('1 seven detected, took 2 cards, return true', self.player.hand)
            # game.change_move()
            return True


        if (last_open_card == card.value and 
            last_open_card.value == 7 and
            self.myDeck.open_cards[-2] == card.value and
            self.myDeck.open_cards[-3] == card.value):
            # game.change_move()
            self.player.take_from_deck(self.myDeck, 6)
            # game.change_move()
            return True

        if (last_open_card == card.value == 7 and 
            last_open_card.value == 7 and
            self.myDeck.open_cards[-2] == card.value and
            self.myDeck.open_cards[-3] == card.value and
            self.myDeck.open_cards[-4] == card.value):
            # game.change_move()
            self.player.take_from_deck(self.myDeck, 8)
            # game.change_move()
            return True
        return False

    def check_rules_ace(self, cards, game):
        last_open_card = self.open_cards[-1]
        if last_open_card == card.value(14):
            game.change_move(self)
            game.change_move(self)

    def check_rules_eight(self, cards, game):
        last_open_card = self.open_cards[-1]
        if last_open_card == card.value(8):
            game.change_move(self)
            game.current_player.take_from_deck(game.myDeck, 1)
        elif last_open_card == card.value(8) and self.open_cards[-2] == card.value(8):
            game.change_move(self)
            game.current_player.take_from_deck(game.myDeck, 2)
        elif last_open_card == card.value(8) and self.open_cards[-2] == card.value(8) and self.open_cards[-3] == card.value(8):
            game.change_move(self)
            game.current_player.take_from_deck(game.myDeck, 3)
        elif last_open_card == card.value(8) and self.open_cards[-2] == card.value(8) and self.open_cards[-3] == card.value(8)and self.open_cards[-4] == card.value(8):
            game.change_move(self)
            game.current_player.take_from_deck(game.myDeck, 4)





        # if game.current_player == game.players[0]
        # while len(player.hand) + 2













        # rules = {
        #     '6': 'take',
        #     '7': 'take 2, skip',
        #     '8': 'take 1',
        #     'Jack': 'uni',
        #     'Ace': 'skip'
    