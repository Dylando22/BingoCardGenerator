import sys

import NumberSet


class Card():
    IdNum = ""
    Size = 0
    CardInfo = []

    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.IdNum = idnum
        self.Size = size
        self.CardInfo = []
        for i in range (0,size):
            nums = []
            for j in range (0,size):
                x = numberSet.getNext()
                if x != None:
                    nums.append(x)
                else:
                    x = numberSet.getNext()
                    nums.append(x)
            self.CardInfo.append(nums)
        if self.Size % 2 == 1:
            free = self.CardInfo[int((self.Size/2))]
            free[int((self.Size/2))] = "Free!"
        numberSet.Count = 0
        # print(self.CardInfo)


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
        x = self.CardInfo[row]
        ans = x[col]
        return ans

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        print(f"Card Number: {self.IdNum}",file=file)
        # if self.Size % 2 == 0:
        for i in range(0,self.Size):
            count = 0
            while count < self.Size:
                print("+------",file=file,end="")
                count += 1
            print("+",file=file)
            row = self.CardInfo[i]
            for col in row:
                if len(str(col)) == 1:
                    print(f"|  {col}   ",file=file,end='')
                elif len(str(col)) == 2:
                    print(f"|  {col}  ",file=file,end='')
                elif len(str(col)) == 3:
                    print(f"| {col}  ",file=file,end='')
                elif len(str(col)) == 5:
                    print(f"| {col}",file=file,end='')
            print("|",file=file)
        count = 0
        while count < self.Size:
            print("+------", file=file, end="")
            count += 1
        print("+", file=file)
        print()
        # else:
        #     for i in range(0,self.Size):
        #         count = 0
        #         while count < self.Size:
        #             print("+------",file=file,end="")
        #             count += 1
        #         print("+",file=file)
        #         row = self.CardInfo[i]
        #         j = 0
        #         for col in row:
        #             if int((self.Size/2)) == i and int((self.Size/2)) == j:
        #                 col = "Free!"
        #                 print(f"| {col} ",file=file, end='')
        #                 j += 1
        #             else:
        #                 print(f"|  {col}  ",file=file,end='')
        #                 j += 1
        #         print("|",file=file)