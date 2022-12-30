# DB_HOST = "192.168.0.1"
# DB_NAME = "second one"
# DB_USER = "third one"
# DB_PASS = "fourth one"
# import psycopg2

# connect = psycopg2.connect(dbhost = DB_HOST, dbname = DB_NAME, dbuser = DB_USER, dbpass = DB_PASS)


# imports
# import pdb
from deck import Deck
from player import PlayerClass
from rules import Rules

# preparation
# move
# end move
class Game(object):
    def __init__(self):
        self.myDeck = Deck() # initialize game
        self.bob = PlayerClass("Bob")
        self.sam = PlayerClass("Sam")
        self.rules = Rules(self.bob, self.myDeck)
        self.myDeck.shuffle()
        self.players = [self.sam, self.bob] # should extend
        # take initial cards
        self.players[0].take_from_deck(self.myDeck, 4)
        self.players[1].take_from_deck(self.myDeck, 5)
        self.current_player = self.players[0]

    def start(self):
        i = 0
        self.myDeck.put_first_card()

        while len(self.sam.hand) > 0 or len(self.bob.hand) > 0:
            print('===================================================================')
            self.sam.showHand()
            print("Deck ({}): | {}".format(len(self.myDeck.closed_cards), self.myDeck.open_cards)) # print deck
            self.bob.showHand()

            print(">>> Current Player: {}".format(self.current_player.name)) # should show which player turn is now

            move_str = str(input('>>> Put a card: ')) # should validate input move is string
            # check if valid name of card
            self.rules.check_rules_six()
            if move_str == '/take':
                self.current_player.take_from_deck(self.myDeck, 1)
            if move_str == '/end':
                # end move
                i = self.change_move(i)
            else:
                self.current_player.make_move(self.myDeck, move_str, self.rules)


    def change_move(self, i=1):
        # players will change
        i = int(i % 2)
        self.current_player = self.players[i]
        i = i + 1
        return i



if __name__ == '__main__':
    g = Game()
    g.start()

# connect.close()
