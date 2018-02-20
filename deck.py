from card import Card
from card import Rank
from card import Suit
import random


class Deck(object):
    
    def __init__(self):
        self.deck = []
        for suit in Suit:
            for rank in Rank:
                self.deck.append(Card(suit.value, rank.value))

    
    def shuffle(self):
        random.shuffle(self.deck)


    def  size(self):
        return len(self.deck)


    def dealCard(self):
        if self.size() <= 0:
            print('Deck is empty!!')
            return

        card = self.deck[0]
        del self.deck[0]
        return card

deck = Deck()
deck.shuffle()
print(deck.size(), deck.dealCard().toString(), deck.size())

