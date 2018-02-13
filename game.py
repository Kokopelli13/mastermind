from collections import Counter
import printer
import random


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
        # using a tuple for now ("RGBY", (1,2)) -> (code, (whitePegs, blackPegs))
        self.guesses = []
        self.didWin = False
        self.printer = printer.Printer(self)

    @staticmethod
    def compareCodes(code1, code2, self):
        # Finds the total amount of pegs cleverly
        totalPegs = sum((Counter(code1) & Counter(code2)).values())
        blackPegs = 0
        for i in range(0, len(code1)):
            if (code1[i] == code2[i]):
                blackPegs += 1
        whitePegs = totalPegs - blackPegs
        if(blackPegs==4):
            self.didWin = True
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
        codeString = ["","","",""]
        for i in range(0, 4):
            codeString[i] = random.choice(self.symbolList)
        print(codeString)
        return (codeString)
    @staticmethod
    def makeGuess(self):
        #Just for test
        solution = ["R","Y","B","B"]
        guess = ["","","",""]
        guesses = 0
        randVal = random.choice(self.possibleCode)
        knownCode = []
        ticksHad= 0
        for i in range(0,4):
            guess[i] = randVal
            whiteBlacks = self.compareCodes(solution,guess,self)
            sumTicks = whiteBlacks[0]+whiteBlacks[1]
        while (guesses !=self.maxGuesses):
            #prints comps last guess and increments guess
            print(guess)
            guesses+=1
            #removes previous value from the list to avoid repeats
            if(self.possibleCode):
                self.possibleCode.remove(randVal)
            #If the comp doesnt have all the right colors yet
            if(sumTicks < 4 and sumTicks != 0):
                #adds correct number of given color to known code
                for i in range(0,sumTicks):
                    knownCode.append(randVal)
                    ticksHad +=1

            #When its zero it shuffles if not correct or closes if correct
            elif(sumTicks ==0):
                if(guess == solution):
                    print("comp Won")
                    guesses = self.maxGuesses
                else:
                    random.shuffle(guess)

            if(self.possibleCode):

                #if there are still codes in possible codes it makes a new random choice
                #Adds random choice onto the partially correct guess
                randVal = random.choice(self.possibleCode)

                for i in range(len(knownCode),4):
                    guess[i] = randVal
                #Sum of ticks minus the amount already known
                whiteBlacks = self.compareCodes(solution, guess, self)
                sumTicks = (whiteBlacks[0] + whiteBlacks[1])-ticksHad

        print("You won i think")

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
        self.possibleCode = ['R', 'G', 'B', 'W', 'Y', 'O']
        self.notCodes = []
        self.knownCodes = []

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
