import random
playerScore = 0
computerScore = 0


def playerRolls(maxScore):
    global playerScore
    if playerScore < int(maxScore) and computerScore < int(maxScore):
        roll = input("Press 'r' to roll ")
        if roll.lower() == 'r':
            val = random.randint(1,int(maxScore))
            playerScore += val
            print("You rolled a ",val)
            print("Your score is",playerScore)

def computerRolls(maxScore):
    global computerScore
    if playerScore < int(maxScore) and computerScore < int(maxScore):
        val = random.randint(1,int(maxScore))
        computerScore += val
        print("Computer rolled a",val)
        print("The computer's score is",computerScore)


def startGame():
    gamestart = input("Welcome type 'roll' to begin the game")

    if gamestart.lower() == "roll":
        maxScore = input("Would you like the winning score to be 10, 50 or 100? (Type one of the three)")
        if maxScore == "10":
            print("The max score will be",maxScore)
            playerRolls(int(maxScore))
            computerRolls(int(maxScore))
        if maxScore == "50":
            print("The max score will be",maxScore)
            playerRolls(int(maxScore))
            computerRolls(int(maxScore))

        if maxScore == "100":
            print("The max score will be",maxScore)
            playerRolls(int(maxScore))
            computerRolls(int(maxScore))


startGame()
