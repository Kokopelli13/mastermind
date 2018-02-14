import game
import printer
import re
import sys
import pickle
import os


def main():
    loadStats()
    hasNotQuit = True
    while(hasNotQuit):
        choice = mainMenu()
        if(choice == 1):
            printer.Printer.printInstructions()
        if(choice == 2):
            currentGame = game.UserGame()
            playGame(currentGame)
        if(choice == 3):
            currentGame = game.ComputerGame()
            playGame(currentGame)
        if(choice == 4):
            printer.Printer.printStats()
        if(choice == 5):
            resetStats()
        if(choice == 6):
            saveStats()
            hasNotQuit = False


def mainMenu():
    printer.Printer.printMenu()
    ans = string_input(printer.Printer.menuInput)
    while((not re.match('[123456]{1}\Z', ans))):
        ans = string_input(printer.Printer.menuError)
    return int(ans)


def playGame(currentGame):
    didWin = False
    currentGame.generateSolution()
    for x in range(currentGame.maxGuesses):
        currentGame.printer.printGame()
        didWin = currentGame.makeGuess()
        if didWin:
            break
    currentGame.printer.printGame()
    currentGame.endGame(didWin)


def saveStats():
    stats = [game.Game._totalGamesHuman, game.Game._totalWinsHuman, game.Game._totalGuessesHuman, game.Game._totalGamesPC, game.Game._totalWinsPC, game.Game._totalGuessesPC]
    pickle.dump(stats, open('savedStats.p', 'wb'))


def loadStats():
    if(os.path.exists('savedStats.p')):
        stats = pickle.load(open('savedStats.p', 'rb'))
        game.Game._totalGamesHuman = stats[0]
        game.Game._totalWinsHuman = stats[1]
        game.Game._totalGuessesHuman = stats[2]
        game.Game._totalGamesPC = stats[3]
        game.Game._totalWinsPC = stats[4]
        game.Game._totalGuessesPC = stats[5]


def resetStats():
    game.Game._totalGamesHuman = 0
    game.Game._totalWinsHuman = 0
    game.Game._totalGuessesHuman = 0
    game.Game._totalGamesPC = 0
    game.Game._totalWinsPC = 0
    game.Game._totalGuessesPC = 0
    print('\n' + printer.Printer.statReset)


if (__name__ == "__main__"):
    if sys.version_info[0] < 3:
        string_input = raw_input
    else:
        string_input = input
    main()
