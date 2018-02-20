from enum import Enum

class Suit(Enum):
    Hearts = 'Hearts'
    Clubs = 'Clubs'
    Diamonds = 'Diamonds'
    Spades = 'Spades'


class Rank(Enum):
    Ace = 'Ace'
    Two = 'Two'
    Three = 'Three'
    Four = 'Four'
    Five = 'Five'
    Six = 'Six'
    Seven = 'Seven'
    Eight = 'Eight'
    Nine = 'Nine'
    Ten = 'Ten'
    Jack = 'Jack'
    Queen = 'Queen'
    King = 'King'
                

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    
    def toString(self):
        return str(self.rank) + ' of ' + str(self.suit)
    