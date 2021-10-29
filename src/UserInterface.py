import Deck
import Menu


class UserInterface():
    deck = Deck.Deck(1,1,1)
    def __init__(self):
        pass

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __createDeck(self):
        """Command to create a new Deck"""
        # TODO: Get the user to specify the card size, max number, and number of cards
        size = self.__getIntegerInput("Please Enter the card size",3,16)
        lowerLim = size*size*2
        UpperLim = int(3.9*size*size)
        MaxNum = self.__getIntegerInput("Enter the max number on card",lowerLim,UpperLim)
        CardCount = self.__getIntegerInput("Enter number of cards to generate",2,8192)
        # TODO: Create a new deck
        self.deck = Deck.Deck(size,CardCount,MaxNum)
        # TODO: Display a deck menu and allow use to do things with the deck
        menu = self.__deckMenu()

        pass

    def __getIntegerInput(self, prompt, m, n):
        """
        Prompt the user for an integer in the range [m, n] INCLUSIVE
        If the provided input is NOT an integer NOR in the range, repeat the prompt
        Otherwise, convert the user's value to an integer and return it.
        """
        KeepRunning = True
        while KeepRunning:
            x = input(f'{prompt}[{m}-{n}]:\n')
            if x.isdigit() and int(x) <= n and int(x) >= m:
                KeepRunning = False
                return int(x)
            else:
                x = input(f'{prompt}[{m}-{n}]:\n')

    def __getStringInput(self, prompt):
        """
        Prompt the user for a string and return it
        """
        x = input(f'{prompt}\n')
        return x

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.deck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getIntegerInput("Id of card to print", 1, self.deck.getCardCount())
        if cardToPrint > 0:
            print()
            self.deck.print(idx=cardToPrint)

    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self.deck.print(outputStream)
            outputStream.close()
            print("Done!")
