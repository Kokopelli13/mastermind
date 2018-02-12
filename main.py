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
            currentGame = game.UserGame()
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
    while((not re.match('[12345]{1}', ans)) or len(ans) > 1):
        ans = string_input('Please make a valid selection: ')
    return int(ans)


def playGame(currentGame):
    currentGame.generateSolution()
    for x in range(currentGame.maxGuesses):
        currentGame.printer.printGame()
        currentGame.makeGuess()
        if(currentGame.didWin):
            break
    currentGame.printer.printGame()
    if(currentGame.didWin):
        print("Congratulations! You Win!!")
    else:
        print("You ran out of guesses...")
        print("The correct code was: " + currentGame.solution)
    if sys.version_info[0] < 3:
        raw_input(printer.Printer.continueText)
    else:
        input(printer.Printer.continueText)


if (__name__ == "__main__"):
    if sys.version_info[0] < 3:
        string_input = raw_input
    else:
        string_input = input
    main()
