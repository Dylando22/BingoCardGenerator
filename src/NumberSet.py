import random


class NumberSet():
    NumberList = []
    Count = 0
    Size = 0
    def __init__(self, size):
        """NumberSet constructor"""
        self.Size = size
        random.seed()
        # print(f"The Size of the NumList {self.Size}")
        self.NumberList = []
        j = 0
        while j < size:
            num = random.randint(1,size)
            while num in self.NumberList:
                num = random.randint(1, size)
            self.NumberList.append(num)
            j += 1
        # print(f"New number list {self.NumberList}")



    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.Size
    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if index > self.Size or index < 0:
            return None
        else:
            return self.NumberList[index]
    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.NumberList)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        if self.Count >= self.Size:
            return None
        else:
            x = self.NumberList[self.Count]
            # print(f"the number {x} is at spot {self.Count} in the NumberList")
            self.Count += 1
            return x
