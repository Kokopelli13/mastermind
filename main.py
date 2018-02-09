import game
import printer
import re


def main():
    hasNotQuit = True
    while(hasNotQuit):
        choice = mainMenu()
        if(choice == 1):
            printer.Printer.printInstructions()
        if(choice == 2):
            currentGame = game.Game()
            userGame(currentGame)
        if(choice == 3):
            currentGame = game.Game()
            computerGame(currentGame)
        if(choice == 4):
            printer.Printer.printStats()
        if(choice == 5):
            hasNotQuit = False


def mainMenu():
    printer.Printer.printMenu()
    ans = raw_input('Pick an option: ')
    while((not re.match('[12345]{1}', ans)) or len(ans) > 1):
        ans = raw_input('Please make a valid selection: ')
    return int(ans)


def userGame(currentGame):
    print('user game')


def computerGame(currentGame):
    print('computer game')


if (__name__ == "__main__"):
    main()
