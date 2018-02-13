import game


def main():
    game1 = game.ComputerGame()
    test1 = ["R","R","B","Y"]
    test2 = ["R","R","B","Y"]
    testing = game1.compareCodes(test1,test2,game1)
    game1.makeGuess(game1)
    print(testing[0])



if (__name__ == "__main__"):
    main()
