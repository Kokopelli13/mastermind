import sys
import game

# Use the correct input for python 2 and 3
if sys.version_info[0] < 3:
    string_input = raw_input
else:
    string_input = input


class Printer:
    """Prints game components to the terminal"""

    # Menu
    menu = """
1) How to play
2) Play as code breaker
3) Play as mastermind
4) Game statistics
5) Reset statistics
6) Quit
"""
    # Instructions
    instructions = """
How to play:

1) The mastermind selects a combination of colored pegs (a code) and the code
breaker attemps to guess that code in fewer than the specified number of turns.

2) The code may be any combination of the six peg colors (R, G, B, W, Y, O)

3) For each guess made by the code breaker the mastermind will place up to four
white (-) and black pegs (+) next to it to show the correctness of their guess.
A white peg means one of the guessed pegs is the correct color, but not in the
correct location. A black peg means that one of the guessed pegs has both the
correct color and location.

4) The code breaker wins if he can guess the correct code before he runs out of
turns, otherwise the mastermind wins.
"""
    # Stats
    statHeaderHuman = "Games won as the code breaker: "
    statHeaderPC = "Games won as the mastermind: "
    stat1 = "  Total number of games played: "
    stat2 = "  Total number of guesses: "
    stat3 = "  Average number of guesses per game: "
    statReset = "Statistics have been reset"
    # Board
    boardTopBottom = " " + ("-" * 19)
    boardSide = "|"
    whitePeg = "-"
    blackPeg = "+"
    # Game
    continueText = "Press Enter to continue..."
    winTextHuman = "Congratulations! You Win!!"
    loseTextHuman = """You ran out of guesses...
    The correct code was: """
    winTextPC = "The computer guessed your code!"
    loseTextPC = """The computer ran out of guesses...
    The computer couldn't guess your code: """
    hintText = "One of the colors is: "
    # Input
    codeInputHuman = """Type H for a hint
Make a Guess: """
    invalidInputHuman = "Invalid Guess. Try again: "
    codeInputPC = "Enter a solution: "
    invalidInputPC = "Invalid Code. Try again: "
    # Other
    menuInput = 'Pick an option: '
    menuError = 'Please make a valid selection: '
    subclassError = "Subclass must implement abstract method"

    # Constructor
    def __init__(self, game):
        self.game = game
        self.width = (4 * self.game.codeLength + 3)
        Printer.boardTopBottom = " " + ("-" * self.width)

    @staticmethod
    def printMenu():
        print(Printer.menu)

    # prints the game board using the guesses[] array from the game object
    def printGame(self):
        # header
        print('Mastermind')
        print('Turn #' + str(len(self.game.guesses)))
        print('Colors: ' + ' '.join(map(str,self.game.symbolList)))
        print('Code Length: ' + str(self.game.codeLength))
        # top of the board
        print(' ' + Printer.boardTopBottom)
        # lines with guesses
        for guess, pegs in self.game.guesses:
            # left side
            sys.stdout.write(' ' + Printer.boardSide)
            # the guessed code
            for i in range(0, len(guess)):
                sys.stdout.write(' ' + guess[i])
            sys.stdout.write(' ' + Printer.boardSide)
            # pegs
            for i in range(0, pegs[0]):
                sys.stdout.write(' ' + Printer.blackPeg)
            for i in range(0, pegs[1]):
                sys.stdout.write(' ' + Printer.whitePeg)
            for i in range(0, self.game.codeLength - (pegs[0] + pegs[1])):
                sys.stdout.write('  ')
            print(' ' + Printer.boardSide)
        # remaining blank lines
        for i in range(0, self.game.maxGuesses - len(self.game.guesses)):
            print(' ' + Printer.boardSide +
                  ' ' * self.width + Printer.boardSide)
        # board bottom
        print(' ' + Printer.boardTopBottom)

    @staticmethod
    def printInstructions():
        print(Printer.instructions)
        string_input(Printer.continueText)

    # prints game stats
    @staticmethod
    def printStats():
        # Let them know if they haven't played yet
        if(game.Game._totalGamesHuman + game.Game._totalGamesPC == 0):
            print("You have not played any games")
            string_input(Printer.continueText)
        else:
            # Else print out the stats
            # Codebreaker stats
            print('')
            print(Printer.statHeaderHuman + str(game.Game._totalWinsHuman))
            print(Printer.stat1 + str(game.Game._totalGamesHuman))
            print(Printer.stat2 + str(game.Game._totalGuessesHuman))
            # avoid divide by zero
            if(game.Game._totalGamesHuman == 0):
                print(Printer.stat3 + '0.0')
            else:
                print(Printer.stat3 +
                  str(1.0 * game.Game._totalGuessesHuman / game.Game._totalGamesHuman))
            # Mastermind stats
            print('')
            print(Printer.statHeaderPC + str(game.Game._totalWinsPC))
            print(Printer.stat1 + str(game.Game._totalGamesPC))
            print(Printer.stat2 + str(game.Game._totalGuessesPC))
            # avoid divide by zero
            if(game.Game._totalGamesPC == 0):
                print(Printer.stat3 + '0.0')
            else:
                print(Printer.stat3 +
                  str(1.0 * game.Game._totalGuessesPC / game.Game._totalGamesPC))
            print('')
            string_input(Printer.continueText)

# self test
def test():
    import game
    game1 = game.Game()
    printer = Printer(game1)
    printer.printMenu()
    printer.printInstructions()
    printer.printStats()
    game1.guesses.append(('RGBW', (1, 2)))
    printer.printGame()


if (__name__ == "__main__"):
    test()
