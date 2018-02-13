from collections import Counter
import printer
import sys

if sys.version_info[0] < 3:
    string_input = raw_input
else:
    string_input = input


class Game:
    """docstring for Game."""
    _totalGames = 0
    _totalWins = 0
    _totalGuesses = 0

    def __init__(self, codeLength=4, maxGuesses=10, symbolList=None):
        Game._totalGames += 1
        if (symbolList is None):
            self.symbolList = ['R', 'G', 'B', 'W', 'Y', 'O']
        else:
            self.symbolList = symbolList
        self.codeLength = codeLength
        self.maxGuesses = maxGuesses
        self.solution = ''
        # using a tuple ("RGBY", (1,2)) -> (code, (blackPegs, whitePegs))
        self.guesses = []
        self.didWin = False
        self.printer = printer.Printer(self)

    @staticmethod
    def compareCodes(code1, code2):
        # Finds the total amount of pegs cleverly
        totalPegs = sum((Counter(code1) & Counter(code2)).values())
        blackPegs = 0
        for i in range(0, len(code1)):
            if (code1[i] == code2[i]):
                blackPegs += 1
        whitePegs = totalPegs - blackPegs
        return blackPegs, whitePegs

    def validateGuess(self, codeGuess):
        if (len(codeGuess) != self.codeLength):
            return (False)
        for i in range(0, self.codeLength):
            if codeGuess[i] not in self.symbolList:
                return (False)
        return (True)

    def endGame(self, didWin):
        self.didWin = didWin
        if didWin:
            Game._totalWins += 1
        Game._totalGuesses += len(self.guesses)
        if(didWin):
            print("Congratulations! You Win!!")
        else:
            print("You ran out of guesses...")
            print("The correct code was: " + self.solution)
        string_input(printer.Printer.continueText)

    def generateSolution(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def makeGuess(self):
        raise NotImplementedError("Subclass must implement abstract method")


class UserGame(Game):
    """docstring for UserGame."""
    def __init__(self, codeLength=4, maxGuesses=10, symbolList=None):
        Game.__init__(self, codeLength, maxGuesses, symbolList)

    def generateSolution(self):
        import random
        codeString = ""
        for i in range(0, self.codeLength):
            codeString += random.choice(self.symbolList)
        # print(codeString)
        self.solution = codeString

    def makeGuess(self):
        codeGuess = string_input("Make a Guess:").upper()
        while not self.validateGuess(codeGuess):
            codeGuess = string_input("Invalid Guess. Try again:").upper()
        blackPegs, whitePegs = Game.compareCodes(codeGuess, self.solution)
        self.guesses.append((codeGuess, (blackPegs, whitePegs)))
        if blackPegs is self.codeLength:
            return True


class ComputerGame(Game):
    """docstring for ComputerGame."""
    def __init__(self, codeLength=4, maxGuesses=10, symbolList=None):
        Game.__init__(self, codeLength, maxGuesses, symbolList)

    def generateSolution(self):
        codeSolution = string_input("Enter a solution:").upper()
        while not self.validateGuess(codeSolution):
            codeSolution = string_input("Invalid Code. Try again:").upper()
        self.solution = codeSolution
    #
    # def makeGuess():


def test():
    game = UserGame()
    game.generateSolution()
    print(game.validateGuess(game.solution))
    print("Code Length: " + str(game.codeLength))
    print("Max Guesses: " + str(game.maxGuesses))
    print("Symbols: " + str(game.symbolList))


if (__name__ == "__main__"):
    test()
