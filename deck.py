import random
from card import Card
from player import PlayerClass
# from game import Game

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
        random.shuffle(self.closed_cards)

    
        # for _ in range(num):
        #     # This is the fisher yates shuffle algorithm
        #     for i in range(length-1, 0, -1):
        #         randi = random.randint(0, i)
        #         if i == randi:
        #             continue
        #         self.closed_cards[i], self.closed_cards[randi] = self.closed_cards[randi], self.closed_cards[i]
        #     # You can also use the build in shuffle method

    # Return the top card
    def deal(self, player):
        top_card = self.closed_cards.pop()
        player.hand.append(top_card)

    def put_first_card(self):
        top_card = self.closed_cards.pop()
        self.open_cards.append(top_card)

    # def check_rules_six(self, card, player):
    #     last_open_card = self.open_cards[-1]
    #     if last_open_card == card.value(6)ß
    #         for c in player.hand
    #             if c == last_open_card.suit or c == last_open_card.value(6) or c == last_open_card.value(11)
    #                 return True
    #             else:
    #                 player.take_from_deck()


    # def check_rules_seven(self, card, game):
    #     last_open_card = self.open_cards[-1]
    #     if last_open_card == card.value(7)
    #         game.change_move(self)
    #         game.take_from_deck(game.myDeck, 2)
    #         game.change_move(self)

    #     elif last_open_card == card.value(7) and self.open_cards[-2] == card.value(7)
    #         game.change_move(self)
    #         game.take_from_deck(game.myDeck, 4)
    #         game.change_move(self)

    #     elif last_open_card == card.value(7) and self.open_cards[-2] == card.value(7) and self.open_cards[-3] == card.value(7)
    #         game.change_move(self)
    #         game.take_from_deck(game.myDeck, 6)
    #         game.change_move(self)

    #     elif last_open_card == card.value(7) and self.open_cards[-2] == card.value(7) and self.open_cards[-3] == card.value(7)and self.open_cards[-4] == card.value(7)
    #         game.change_move(self)
    #         game.take_from_deck(game.myDeck, 8)
    #         game.change_move(self)

    # def check_rules_ace(self, cards, game)
    #     last_open_card = self.open_cards[-1]
    #     if last_open_card == card.value(14)
    #         game.change_move(self)
    #         game.change_move(self)

    # def check_rules_eight(self, cards, game)
    #     last_open_card = self.open_cards[-1]
    #     if last_open_card = card.value(8)
    #         game.change_move(self)
    #         game.current_player.take_from_deck(game.myDeck, 1)
    #     elif last_open_card == card.value(8) and self.open_cards[-2] == card.value(8)
    #         game.change_move(self)
    #         game.current_player.take_from_deck(game.myDeck, 2)
    #     elif last_open_card == card.value(8) and self.open_cards[-2] == card.value(8) and self.open_cards[-3] == card.value(8)
    #         game.change_move(self)
    #         game.current_player.take_from_deck(game.myDeck, 3)
    #     elif last_open_card == card.value(8) and self.open_cards[-2] == card.value(8) and self.open_cards[-3] == card.value(8)and self.open_cards[-4] == card.value(8)
    #         game.change_move(self)
    #         game.current_player.take_from_deck(game.myDeck, 4)





    #     # if game.current_player == game.players[0]
    #     # while len(player.hand) + 2













    #     # rules = {
    #     #     '6': 'take',
    #     #     '7': 'take 2, skip',
    #     #     '8': 'take 1',
    #     #     'Jack': 'uni',
    #     #     'Ace': 'skip'
    #     # }
