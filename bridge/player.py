class PlayerClass(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def take_from_deck(self, deck, num=1):
        for _ in range(num):
            deck.deal(self)

    def handToStr(self):
        hand = []
        for card in self.hand:
            hand.append(card.to_str())
        return hand

    # Display all the cards in the players hand
    def showHand(self):
        print ("{} ({}): {}".format(self.name, len(self.hand), self.handToStr()))
        return self

    def put_card_on_table(self, deck, card):
        # find index of card and remove it from hand
        # return removed card e.g. return hand[card_index]
        for c in self.hand:
            if card.suit == c.suit and card.value == c.value:
                self.hand.remove(c)

        deck.open_cards.append(card)

    def find_card_by_name(self, card_str):
        # find card object in hand by given str, return card object
        # print('find_card_by_name str', card_str)
        for card in self.hand:
            if card_str == card.to_str():
                return card
        return False

    def make_move(self, deck, card_str):
        # put selected card from player hand into deck open cards
        # move_str = str(input('put a card: '))
        card = self.find_card_by_name(card_str)
        # print('>>> Make move', card)
        if card:
            result = card.check_match(deck) and deck.check_rules(card)
            if result:
                self.put_card_on_table(deck, card)
                return True
            else:
                print('>>> WRONG MOVE!')
                return False
        else:
            print('>>> WRONG CARD!')
            return False
