import random

class Deck(object):
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for x in ['Hearts','Diamonds','Spades','Clubs']:
            for y in range(1,14):
                self.cards.append(Card(x,y))

    def show(self):
        for z in self.cards:
            z.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()