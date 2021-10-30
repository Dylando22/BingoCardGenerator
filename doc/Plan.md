# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

The purpose of this program is to efficiently make a deck of bingo cards that are all different, and let the user interact
with the program to decide the dimensions and style of bingo cards they would like. The problem is making sure to give clear
instruction for the user to know what to do, and to makes sure to check for human input error so the user knows when they did
something wrong. We have some starter code that we can use to make this solution possible. 

A good solution we have clear instructions on what the user needs to input and how, also a clear output of the bingo cards
with different options (Print to screen, Save into a file, Print whole deck, or a certin card, ect.). The cards sholud look 
like normal bingo cards when finished, and if there is an incorrect input, we should handel the error and have the user retry
instead of letting the program crash. 

Know how to do:
- Print out to the screen
- Get input from a user
- Store information
- Handel errors 
- Interact with multiple classes and methods.

Challenges:
- Getting the right types
- Connecting all the classes together 
- Writing to a file as output
- Randomizing bingo cards and keeping track of the information
- Making the program clear for any user to use

## Phase 1: System Analysis *(10%)*

Data used in program:
1. Input from user for size, numbers insde the cards, and number of cards for each deck
2. Commands received from the user on what they would like the program to do. 
3. Hard coded commands and prompts for the menus on what the user can do. 
4. Randomized numbers to store inside the bingo card, this will hard coded
5. Dictionary to store all the bingo cards and their corresponding card index, the information on the cards will come from Random, but the number of cards will come from the user.
6. Interacting classes

The output will either be in a .txt file, or printed out to the screen. This will be a mix '-' and '+' characters to make the 
boarder of the cards. Also integers will be stored inside the deck and card information as well.

List of formulae and descriptions:
UserInterface.py gets Deck.py and Menu.py 
- run() Present the main menu to the user and repeatedly prompt for a valid command
- __createDeck()*private* Get cardSize, MaxNumber, and NumberOfCards, create the deck, Display interactive menu. 
- __getIntegerInput(self, prompt, m, n) Prompt user for and integer in range [m,n] inclusive and convert to int and return
- __getStringInput(self, prompt)
- __deckMenu(self) Presnets the menu to the screen 
- __printCard(self) Asks user for the card number and prints that card 
- __saveDeck(self) Saves deck to a file

Deck.py gets Card.py and NumberSet.py
+ Constructor(cardSize, cardCount, numberMax) sets the objects to their values in Deck 
+ getCardCount() returns the number of cards in the deck 
+ getCard(n) returns a card n from the deck.  
+ print(sys.stdout, idx = none)

Menu.py gets MenuOption.py
+ Constructor(self, header) Sets the header from input, optCount to 0, and an options list 
+ addOption(self, command,description) Adds an OptionsMenu object into a list, with the inputed command and description. Then increases count by 1.  
+ isValidCommand(self,command) Checks if commands are valid, returns True or False 
+ getOption(self,optionIndex) Returns the option that is stored in the options list. 
+ getHeader() Returns the Header initialized in constructor 
+ getOptionCount() Returns the optionCount
+ show() Returns command. Prints out the menu and gets the command wanted from the user, does not stop until valid command is given by user

MenuOption.py is a base class. 
+ Constructor(self, command, description) Sets the given command and description in object
+ getCommand() returns the command given to the Constructor
+ detDescription() returns the description given to the Constructor.

Card.py gets NumberSet.py 
+ getId() Returns an int, the ID number of the card
+ getSize()	Returns an int, the size of one demension of a card ex. 3x3 will return 3
+ getSquare(self,row,col) Returns int value of sqaure at row, col. 
+ print(self,sys.stdout) Prints a card to screen

NumberSet.py is a base class 
+ getSize returns int, 
+ get(self, index) Returns the number stored in the index 
+ randomize(), Shuffles numbers, returns null 
+ getNext() returns an int. Recursivly returns all the values in the set, until the end, then none is returned. 


## Phase 2: Design *(30%)*

General Pseudocode:
1. Print out welcome to bingo with Main menu
2. Get C for create or X or exit, if anything else, place menu on screen again
3. If C is inserted: 
    1. get the CardSize from user and store in Card.CardSize
    2. get the number of cards wanted and store in Deck.DeckSize
    3. Get the max value and store in Card.MaxNumber
    4. Use Random to create the cards and store in dictionary, make sure they are unique. If CardSize is odd, have free space in center, if not just do the numbers. 
    5. Go to the next menu, DeckMenu. 
4. With Deck Menu Open Have user input P(Print), S(Save), D(Deck), or X(Exit)
    1. If the user inputs P:
       - Ask the user for which card number they want put on the screen, if not in the range, ask again. 
       - Save number as index, and call getCard(index) and print to screen.
       - pop up Deck Menu again 
    2. If the user inputs D:
       - Loop through each Card in the deck dictionary
       - Print out the Card number and card to the screen
       - pop up Deck Menu again
    3. If the user inputs S:
       - Ask the user for a file to save the deck to, if it is not a .txt file, have user try again, also if it does not exist make one. 
       - Open file for writing, and loop through each card in deck and print out the card number and card.
       - Close the file
       - pop up Deck Menu again
    4. If the user inputs X, exit the program.
    5. If the user types in anything else, pop up deck menu again
5. End the program

Important Functions:
randomize(), Shuffles numbers, returns null
    - do list.shuffle() until it is unique

Card.print(self,sys.stdout) Prints a card to screen:
    - Print out top boarder of table,
    - Print out columns and spaces to put numbers in center
    - If size is odd, print free space in the center, else just numbers

Deck.print(sys.stdout, idx = none) Prints out the deck of cards
    - Loops through every card in the deck and prints it to the screen

run() Present the main menu to the user and repeatedly prompt for a valid command
    - Opens up Main Menu until valid prompt is given.
    - If C, run createDeck
    - If X, exit program

__createDeck()*private* Get cardSize, MaxNumber, and NumberOfCards, create the deck, Display interactive menu. 
    - Get the user to specify the card size, max number, and number of cards
    - Save info in a new Deck object, and have Deck set up all random bingo cards 
    - Print out Deck Menu repeatedly until a correct input is given

__printCard(self) Asks user for the card number and prints that card
    - Gets input from user on which card to print to screen 
    - Runs getCard(input)
    - Prints that card

__saveDeck(self) Saves deck to a file
    - Prompts user for a filename to save output to
    - open the file for writing
    - loops through cards in deck and writes them in the file
    - closes file

*** The rest are getter and setter functions and are described in the above phase ***

With good input, everything should run and work smoothly. If there is an invalid prompt the program will not crash, but the menu will
pop up again. If there is bad input, for example an int instead of a string, we can simply re send out any prompt and have the user try again.

## Phase 3: Implementation *(15%)*


Worked on python code and lots of debugging. I had the hardest time understaning why my design was not working and the classes were not getting the correct information. I realized I needed to declare certain variables and to use a NumberSet in the deck and then randomize it and assign it to each Card in the deck.

While writing the code I learned how important it was to find the flow of information before writing code. What really helped me was going to the UserInterface class and following each method and variable to see where it went

Another reason I got stuck was trying to implement the NumberSet class with the input of size being the size of the card. when I did this every time I would get a random number, it would end up being the exact same for each card. I ended up making a NumberSet with all the numbers in a random order up to size(which was the Max number input by the user) and then shuffling the set. 



## Phase 4: Testing & Debugging *(30%)*


I personally tested the program personally, trying to do incoreect inputs, and looking at the output from the cards to look for errors. 
I also rand the following test cases that passed:

1. test_getID -- Assert that card ID number is as expected ... ok
2. test_getSize -- Assert that card size is as expected ... ok
3. test_hasFreeSquares -- Ensure that odd-numbered cards have 1 "Free!" square in the center ... ok
4. test_noDuplicates -- Ensure that cards do not contain duplicate numbers ... ok
5. test_getCard -- Ensure that Cards can be accessed from within a Deck ... ok
6. test_getCardCount -- Ensure that Decks contain expected number of cards ... ok
7. test_addOption -- Ensure that options can be added to a Menu ... ok
8. test_getHeader -- Ensure that Menu headers are stored and may be retrieved ... ok
9. test_getOption -- Ensure that menu options can be retrieved from Menus ... ok
10. test_getOptionCount -- Ensure that a Menu retains the correct number of options ... ok
11. test_get -- Ensure that a NumberSet's gracefully handles requests for out-of-bounds numbers ... ERROR (This happend becasue I use a counter to make sure it is in the index)
12. test_getNext -- Ensure that a NumberSet's .getNext() method can be safely called more times than the quantity of nubmers it contains ... ok
13. test_getSize -- Ensure that a NumberSet's size is as expected ... ok
14. test_noDuplicates -- Ensure that a NumberSet contains no duplicates ... ok



## Phase 5: Deployment *(5%)*


Pushed everything up to GitLab


## Phase 6: Maintenance


*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    * What parts of your program are sloppily written and hard to understand?
    - The getting random numbers is very sloppy, and also I have commented out code to get the test cases to run proplerly, and I didn't want to get rid of all my hard work, so I left it.
        * Are there parts of your program which you aren't quite sure how/why they work?
      - Not really, in order to get it running proplery from the errors and bugs I was having, I had to take a step back and really understand all aspects. 
        * If a bug is reported in a few months, how long would it take you to find the cause?
        - depends on the bug, but it would probably consist of changing how things are printed to the screen, so not very long.
    * Will your documentation make sense to
        * anybody besides yourself?
      - Probalby not if they do not understand the program and all the classes. But the user will be able to use it easily 
        * yourself in six month's time?
        -I think I will be able to understand it
    * How easy will it be to add a new feature to this program in a year?
    - The program seems pretty obsolete, but if random functions are added, you can improve that aspect.
    * Will your program continue to work after upgrading
        * your computer's hardware?
        * the operating system?
        * to the next version of Python?
      - Yes, yes and yes 
