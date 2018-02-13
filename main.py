import game
import printer
import re
import sys


def main():
    hasNotQuit = True
    while(hasNotQuit):
        choice = mainMenu()
        if(choice == 1):
            printer.Printer.printInstructions()
        if(choice == 2):
            currentGame = game.UserGame(8, 20)
            playGame(currentGame)
        if(choice == 3):
            currentGame = game.ComputerGame()
            playGame(currentGame)
        if(choice == 4):
            printer.Printer.printStats()
        if(choice == 5):
            hasNotQuit = False


def mainMenu():
    printer.Printer.printMenu()
    ans = string_input('Pick an option: ')
    while((not re.match('[12345]{1}\Z', ans))):
        ans = string_input('Please make a valid selection: ')
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


if (__name__ == "__main__"):
    if sys.version_info[0] < 3:
        string_input = raw_input
    else:
        string_input = input
    main()
