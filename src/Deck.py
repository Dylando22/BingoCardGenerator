import sys
import Card
import NumberSet


class Deck():
    CardsInDeck = []
    CardSets = []
    Cardsize = 0
    MaxNum = 0
    CardCount = 0
    def __init__(self, cardSize, cardCount, numberMax):
        """Deck constructor"""
        self.Cardsize = cardSize
        self.CardCount = cardCount
        self.MaxNum = numberMax
        self.CardsInDeck = []
        set = NumberSet.NumberSet(numberMax)
        i = 0
        while i < cardCount:
            set.randomize()
            self.CardSets.append(set)
            self.CardsInDeck.append(Card.Card(i,cardSize,set))
            i += 1

    def getCardCount(self):
        """Return an integer: the number of cards in this deck"""
        return self.CardCount

    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1
        if 0 <= n < self.getCardCount():
            card = self.CardsInDeck[n]
        return card

    def print(self, file=sys.stdout, idx=None):
        """void function: Print cards from the Deck

        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:
            for idx in range(1, self.CardCount + 1):
                c = self.getCard(idx)
                c.print(file)
            print('', file=file)
        else:
            self.getCard(idx).print(file)
