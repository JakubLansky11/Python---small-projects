# Python project - game Bulls & Cows
# Author - Jakub Lánský

indent = "-" * 120
from numpy import random as rnd

# Start of the game
print("Hi there!")
print(indent)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(indent)

# Generating of number
numbers = range(0, 10)
while True:
    number = rnd.choice(numbers, replace=False, size=4)
    if number[0] == 0:
        continue
    else:
        break
solution = str(number[0]) + str(number[1]) + str(number[2]) + str(number[3])

# Playing the game
print(indent)
guesses = 0
while True:
    choice = input("Enter a number: ")
    if len(choice) != 4:
        print("Bad number lenghth!")
        continue
    elif choice[0] == "0":
        print("It can´t starts with 0!")
        continue
    elif (not choice[0].isnumeric() or not choice[1].isnumeric() or not choice[2].isnumeric() or not choice[3].isnumeric()):
        print("Entered non-numeric symbol!")
        continue
    elif (choice[0] == choice[1] or choice[0]  == choice[2] or choice[0]  == choice[3] or choice[1] == choice[2] or choice[1] == choice[3] or choice[2] == choice[3]):
        print("All numbers have to be unique!")
        continue
    elif choice == solution and guesses == 0:
        print(indent)
        print("It´s amazing! You needed only 1 guess!")
        break
    elif choice != solution:
        print(indent)
        print(">>> ", choice)
        guesses += 1
        bulls = 0
        cows = 0
        ind = 0
        while ind in range(0, 4):
            if (choice[ind] in solution and choice[ind] == solution[ind]):
                    bulls += 1
            elif (choice[ind] in solution and choice[ind] != solution[ind]):
                    cows += 1
            ind += 1
            continue
        if (bulls == 1 and cows != 1):
            print("1 bull, ",  cows, "cows")
        elif (bulls == 1 and cows == 1):
            print("1 bull, 1 cow")
        elif (bulls != 1 and cows == 1):
            print(bulls, "bulls, ", "1 cow")
        elif (bulls != 1 and cows != 1):
            print(bulls, "bulls, ", cows, "cows")  
        print("Number of guesses: ", guesses)
        print(indent)
        continue
    elif choice == solution:
        guesses += 1
        print("Correct, you've guessed the right number in ", guesses, "guesses!")
        print(indent)
        if guesses in range (2, 6):
            print("Perfect!")
        elif guesses in range (6, 10):
            print("Very good!")
        elif guesses in range (10, 20):
            print("Average.")
        elif guesses in range (20, 30):
            print("Not so good!")
        elif guesses >= 30:
            print("Very bad!")
    break
bye = input("You finished game. Thank you for playing. Press enter to leave.")

