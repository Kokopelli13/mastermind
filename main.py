import game
import re


def main():
    currentGame = game.Game()
    hasNotQuit = True
    while(hasNotQuit):
        choice = mainMenu(currentGame)
        if(choice == 1):
            currentGame.printer.printInstructions()
        if(choice == 2):
            userGame(currentGame)
        if(choice == 3):
            computerGame(currentGame)
        if(choice == 4):
            currentGame.printer.printStats()
        if(choice == 5):
            hasNotQuit = False


def mainMenu(currentGame):
    currentGame.printer.printMenu()
    ans = raw_input('Pick an option: ')
    while((not re.match('[12345]{1}', ans)) or len(ans) > 1):
        ans = raw_input('Please make a valid selection: ')
    return int(ans)


def userGame():
    print('user game')


def computerGame():
    print('computer game')


if (__name__ == "__main__"):
    main()
