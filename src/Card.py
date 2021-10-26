import sys

import NumberSet


class Card():
    IdNum = ""
    Size = 0
    Col = []
    Info = []
    set = NumberSet.NumberSet(0)

    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.IdNum = idnum
        self.Size = size
        self.Col = [size]
        self.Info = [size]
        self.set = numberSet = NumberSet.NumberSet(size)


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.IdNum

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.Size

    def getSquare(self, row, col):
        """Return the value in the Bingo square at (row, col) """
        temp = self.Info[row]
        return temp[col]

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
