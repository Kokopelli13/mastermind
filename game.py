from collections import Counter
import printer


class Game:
    """docstring for Game."""
    _totalGames = 0

    def __init__(self, codeLength=4, maxGuesses=10, symbolList=None):
        Game._totalGames += 1
        if (symbolList is None):
            self.symbolList = ['R', 'G', 'B', 'W', 'Y', 'O']
        else:
            self.symbolList = symbolList
        self.codeLength = codeLength
        self.maxGuesses = maxGuesses
        self.solution = ''
        # using a tuple for now ("RGBY", (1,2)) -> (code, (whitePegs, blackPegs))
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

    @staticmethod
    def validateGuess(codeGuess,self):
        import re
        pattern = r'[^RBGYPO]'
        if (len(codeGuess) != self.codeLength):
            return (False)
        for i in range(0, 4):
            if (re.search(pattern, codeGuess[i])):
                return (False)
        return (True)

    @staticmethod
    def generateSolution(self):
        import random
        codeString = ["", "", "", ""]
        for i in range(0, 4):
            codeString[i] = random.choice(self.symbolList)
        print(codeString)
        return (codeString)

    def makeGuess():
        raise NotImplementedError("Subclass must implement abstract method")


class UserGame(Game):
    """docstring for UserGame."""
    def __init__(self):
        super(UserGame, self).__init__()

    # def validateGuess(codeGuess):
    #
    #
    # def generateSolution():
    #
    #
    # def makeGuess():


class ComputerGame(Game):
    """docstring for ComputerGame."""
    def __init__(self):
        super(ComputerGame, self).__init__()

    # def validateGuess(codeGuess):
    #
    #
    # def generateSolution():
    #
    #
    # def makeGuess():


def test():
    game = Game()
    print("Code Length: " + str(game.codeLength))
    print("Max Guesses: " + str(game.maxGuesses))
    print("Symbols: " + str(game.symbolList))


if (__name__ == "__main__"):
    test()
