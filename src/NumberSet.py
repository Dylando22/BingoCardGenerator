import random


class NumberSet():
    Size = 0;
    MaxNumber = 0
    NumberList = []
    def __init__(self, size):
        """NumberSet constructor"""
        self.Size = size * size
        i = 0
        random.seed(1)
        while i < size:
            num = random.random()
            num = num * size
            self.NumberList.append(num)
            i += 1
        pass

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.Size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        return self.NumberList[index]

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        pass

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        pass
