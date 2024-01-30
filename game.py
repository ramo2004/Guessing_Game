import random
import sys
gameChoice = input("Would you like to play the Guessing game? (yes or no)")
if(gameChoice=="yes"):
    print("Okay lets play. The computer will try and guess your number. ")
    lowerRand=0
    upperRand=100
    firstGuess = (random.randint(lowerRand,upperRand))
    print(f"The computer's first guess is: {firstGuess}")

    close1 = input("Is the number too high, too low, or correct? (high, low, correct) ")
    while (close1!='correct'):
        if (close1=='low'):
            lowerRand=firstGuess+1

        elif (close1=='high'):
            upperRand=firstGuess-1
        else:
            print("Invalid Input, enter either: low, high, or correct. ")
    
        firstGuess = (random.randint(lowerRand,upperRand))
        print(f"The computers next guess is {firstGuess}")
        close1 = input("Is the number too high, too low, or correct? ")
    print(f"Your number is {firstGuess}!")
    

else:
    sys.exit("Bye Bye")
