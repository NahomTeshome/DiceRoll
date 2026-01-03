import random
gamestart = input("Welcome type 'roll' to begin the game ")
playerScore = 0
computerScore = 0


def computeRolls():
    if playerScore < int(maxScore) and computerScore < int(maxScore):
        roll = input("Press 'r' to roll ")
        if roll.lower() == 'r':
            val = random.randint(1,int(maxScore))
            print("You rolled a ",val)



if gamestart.lower() == "roll":
    maxScore = input("Would you like the winning score to be 10, 50 or 100? (Type one of the three)")
    if maxScore == "10":
        print("The max score will be ",maxScore)
        computeRolls()
    if maxScore == "50":
        print("The max score will be ",maxScore)
        computeRolls()
    if maxScore == "100":
        print("The max score will be ",maxScore)
        computeRolls()


