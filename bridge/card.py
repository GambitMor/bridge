class Card(object):
    def __init__(self, suit, val):
        self.suit = suit #str
        self.value = val # int

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.to_str()
    def __str__(self):
        return self.to_str()
    def __repr__(self):
        return self.to_str()

    def to_str(self):
        if self.value == 14:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value
        return "{} of {}".format(val, self.suit)

    def check_match(self, deck):
        last_open_card = deck.open_cards[-1]
        if self.suit == last_open_card.suit or self.value == last_open_card.value:
            return True
        else:
            return False
