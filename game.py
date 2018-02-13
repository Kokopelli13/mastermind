from collections import Counter
import printer
import re
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
        # Gets a count for each color in each code
        code1ColorCount = Counter(code1)
        code2ColorCount = Counter(code2)
        # Gets a count for the colors in both
        overlap = code1ColorCount & code2ColorCount
        # Total pegs tot be shown
        totalPegs = sum(overlap.values())
        # Calculate number of black pegs
        blackPegs = 0
        for i in range(0, len(code1)):
            if (code1[i] == code2[i]):
                blackPegs += 1
        # Calculate number of white pegs
        whitePegs = totalPegs - blackPegs
        return blackPegs, whitePegs

    def validateCode(self, code):
        reString = ('[' + (''.join(self.symbolList)) + ']{'
                    + str(self.codeLength) + '}\Z')
        if re.match(reString, code):
            return True
        return False

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
        while not self.validateCode(codeGuess):
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
        while not self.validateCode(codeSolution):
            codeSolution = string_input("Invalid Code. Try again:").upper()
        self.solution = codeSolution
    #
    # def makeGuess():


def test():
    uGame = UserGame()
    uGame.generateSolution()
    print(uGame.validateCode(uGame.solution))
    print("Code Length: " + str(uGame.codeLength))
    print("Max Guesses: " + str(uGame.maxGuesses))
    print("Symbols: " + str(uGame.symbolList))


if (__name__ == "__main__"):
    test()
