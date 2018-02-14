from collections import Counter
import printer
import random
import re
import sys

if sys.version_info[0] < 3:
    string_input = raw_input
else:
    string_input = input


class Game:
    """docstring for Game."""
    _totalGamesHuman = 0
    _totalWinsHuman = 0
    _totalGuessesHuman = 0
    _totalGamesPC = 0
    _totalWinsPC = 0
    _totalGuessesPC = 0

    def __init__(self, codeLength=4, maxGuesses=10, symbolList=None):
        if symbolList is None:
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
        raise NotImplementedError(printer.Printer.subclassError)

    def generateSolution(self):
        raise NotImplementedError(printer.Printer.subclassError)

    def makeGuess(self):
        raise NotImplementedError(printer.Printer.subclassError)


class UserGame(Game):
    """docstring for UserGame."""
    def __init__(self, codeLength=4, maxGuesses=10, symbolList=None):
        Game.__init__(self, codeLength, maxGuesses, symbolList)

    def generateSolution(self):
        codeString = ""
        for i in range(0, self.codeLength):
            codeString += random.choice(self.symbolList)
        # print(codeString)
        self.solution = codeString

    def makeGuess(self):
        Game._totalGuessesHuman += 1
        codeGuess = string_input(printer.Printer.codeInputHuman).upper()
        while not self.validateCode(codeGuess):
            if(codeGuess == 'H'):
                self.printer.printGame()
                print(printer.Printer.hintText + self.solution[random.randint(0,self.codeLength - 1)])
                codeGuess = string_input(printer.Printer.codeInputHuman).upper()
            else:
                codeGuess = string_input(printer.Printer.invalidInputHuman).upper()
        blackPegs, whitePegs = Game.compareCodes(codeGuess, self.solution)
        self.guesses.append((codeGuess, (blackPegs, whitePegs)))
        if blackPegs is self.codeLength:
            return True
        return False

    def endGame(self, didWin):
        self.didWin = didWin
        Game._totalGamesHuman += 1
        if(didWin):
            print(printer.Printer.winTextHuman)
            Game._totalWinsHuman += 1
        else:
            print(printer.Printer.loseTextHuman + self.solution)
            string_input(printer.Printer.continueText)


class ComputerGame(Game):
    """docstring for ComputerGame."""
    def __init__(self, codeLength=4, maxGuesses=10, symbolList=None):
        Game.__init__(self, codeLength, maxGuesses, symbolList)
        self.possibleCode = self.symbolList[:]
        self.guessSoFar = ""

    def generateSolution(self):
        codeSolution = string_input(printer.Printer.codeInputPC).upper()
        while not self.validateCode(codeSolution):
            codeSolution = string_input(printer.Printer.invalidInputPC).upper()
        self.solution = codeSolution

    def makeGuess(self):
        Game._totalGuessesPC += 1
        if len(self.guessSoFar) < self.codeLength:
            guess = self.guessSoFar
            randVal = random.choice(self.possibleCode)
            guess += randVal * (self.codeLength - len(self.guessSoFar))
            self.possibleCode.remove(randVal)
            blackPegs, whitePegs = self.compareCodes(self.solution, guess)
            self.guesses.append((guess, (blackPegs, whitePegs)))
            if blackPegs == self.codeLength:
                return True
            sumTicks = blackPegs + whitePegs
            self.guessSoFar += randVal * (sumTicks - len(self.guessSoFar))
        else:
            guessList = list(self.guessSoFar)
            random.shuffle(guessList)
            guess = ''.join(guessList)
            blackPegs, whitePegs = self.compareCodes(guess, self.solution)
            self.guesses.append((guess, (blackPegs, whitePegs)))
            if blackPegs == self.codeLength:
                return True
        string_input(printer.Printer.continueText)
        return False

    def endGame(self, didWin):
        self.didWin = didWin
        Game._totalGamesPC += 1
        if didWin:
            print(printer.Printer.winTextPC)
            Game._totalWinsPC += 1
        else:
            print(printer.Printer.loseTextPC + self.solution)
            string_input(printer.Printer.continueText)


def test():
    uGame = UserGame()
    uGame.generateSolution()
    print(uGame.validateCode(uGame.solution))
    print("Code Length: " + str(uGame.codeLength))
    print("Max Guesses: " + str(uGame.maxGuesses))
    print("Symbols: " + str(uGame.symbolList))


if (__name__ == "__main__"):
    test()
