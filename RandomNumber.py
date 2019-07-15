#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
Num = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = 0

guess = input("Guess a number between 1 and 20 (inclusive) ==> ")

i = 0
while i < 5 or (guess != Num):

    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    	print("That's not a positive whole number, try again!")

    else:
    	guess = int(guess) # converts a string to an integer
#different thingie
    if (guess == Num):
        print ("You got it!! Yay!")
        break

    elif (guess > Num):
        print ("Go lower!")
        i +=1
        guess = input("Guess again! ==> ")

    else:
        print ("Go higher!")
        i += 1
        guess = input("Guess again! ==> ")

    if i == 5:
        print ("")
        print ("Out of guesses :( the answer was ==> ", Num, "!!!!!!")
        break

print ("Let's play again!")

guess = input("Guess a number between 1 and 20 (inclusive) ==> ")

for i in range (5):

        if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        	print("That's not a positive whole number, try again!")

        else:
        	guess = int(guess) # converts a string to an integer
    #different thingie
        if (guess == Num):
            print ("You got it!! Yay!")
            break

        elif (guess > Num):
            print ("Go lower!")
            i +=1
            guess = input("Guess again! ==> ")

        else:
            print ("Go higher!")
            i += 1
            guess = input("Guess again! ==> ")

        if i == 5:
            print ("")
            print ("Out of guesses :( the answer was ==> ", Num, "!!!!!!")
            break
