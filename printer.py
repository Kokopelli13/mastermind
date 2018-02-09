import sys
import game

class Printer:
    """docstring"""
    # Menu
    menu = """
1) How to play
2) Play as code breaker
3) Play as mastermind
4) Game statistics
5) Quit
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
    stat1 = "Total number of games played: "
    stat2 = "Total number of games won: "
    stat3 = "Total number of guesses: "
    stat4 = "Average number of guesses per game: "
    # Board
    boardTopBottom = "-"*20
    boardSide = "|"
    whitePeg = "-"
    blackPeg = "+"

    def __init__(self, game):
        self.game = game

    @staticmethod
    def printMenu():
        print(Printer.menu)

    #prints the game board using the guesses[] array from the gaem object
    def printGame(self):
        #header
        print('Mastermind')
        print('Turn #' + str(len(self.game.guesses)))
        #top of the board
        print(' ' + Printer.boardTopBottom)
        #lines with guesses
        for guess, pegs in self.game.guesses:
            #left side
            sys.stdout.write(' ' + Printer.boardSide)
            #the guessed code
            for i in range(0, len(guess)):
                sys.stdout.write(' ' + guess[i])
            sys.stdout.write(' ' + Printer.boardSide)
            #pegs
            for i in range(0, pegs[0]):
                sys.stdout.write(' ' + Printer.whitePeg)
            for i in range(0, pegs[1]):
                sys.stdout.write(' ' + Printer.blackPeg)
            for i in range(0, 4 - (pegs[0] + pegs[1])):
                sys.stdout.write('  ')
            print(' ' + Printer.boardSide)
        #remaining blank lines
        for i in range(0, self.game.maxGuesses - len(self.game.guesses)):
            print(' ' + Printer.boardSide + ' '*19 + Printer.boardSide)
        #board bottom
        print(' ' + Printer.boardTopBottom)

    @staticmethod
    def printInstructions():
        print(Printer.instructions)
        raw_input("Press Enter to continue...")

    @staticmethod
    def printStats():
        if(game.Game._totalGames == 0):
            print("You have not played any games")
            raw_input("Press Enter to continue...")
        else:
            print('')
            print(Printer.stat1 + str(game.Game._totalGames))
            print(Printer.stat2 + str(game.Game._totalWins))
            print(Printer.stat3 + str(game.Game._totalGuesses))
            print(Printer.stat4 + str(1.0*game.Game._totalGuesses/game.Game._totalGames))
            print('')
            raw_input("Press Enter to continue...")

    def printTurn(self):
        print('a')


def test():
    import game
    game1 = game.Game()
    printer = Printer(game1)
    printer.printMenu()
    printer.printInstructions()
    printer.printStats()
    game1.guesses.append(('RGBW', (1,2)))
    printer.printGame()


if (__name__ == "__main__"):
    test()
