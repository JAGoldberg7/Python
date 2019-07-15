# --- Define your functions below! ---
import random

def intro():

    print("Hi! My name is Chatbot! Let's have a DMC ;)")
    print()
    name = input ("What is your name? ==> ")
    print()
    print("Hello ", name, "!")
    print()
    answer = input("How are you today? ==> ")
    yourday(answer)

def yourday(answer):
    if (answer == ("good" or "great")):
        print("YAY YOU ARE FAB WOOOOOOO")

    elif (answer == ("bad" or "horrible")):
        print("thAT's SAD i am sorry :(")

    else:
        print("LOLLLLLLLLLLL nice :-)")

# --- Put your main program below! ---
def inspire(answer):

    print()
    if (answer == ("mom")):
        print ("Aw that is SO CUTE :')")
        print()

    game = input("Would you like to hear a 'riddle' or a 'joke'? ==> ")
    if game == "riddle":
        riddle()

def riddle():
    print("Let's hear a riddle!")
    print()
    print("What goes up but doesn't go down?")
    guess = ""
    answer = "age"
    print()

    while answer != guess:

        guess = input("GUESS ==> ")

        if guess == "age":
            print ("Yay you got it!")
            break

        elif guess != "age":
            print("guess again!!")
            print()
    numbers()

def main():
    answer = input ("What is your favorite icecream? ==> ")
    print("No way! That's my favorite too!")
    print()
    who = input ("Who inspires you? ")
    inspire(who)

def inList(num, guess):
    if (num == guess):
        return True
    else:
        return False


def numbers():

    guess = ""

    guess = input("Guess the number! (1-9) ==> ")

    myList = [1,2,3,4,5,6,7,8,9]

    num = random.choice(myList)

    if inList(num, guess):
        print()
        print ("You got it!")
    else:
        print()
        print ("Nope, the number wasssssss... ", num)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    intro()
    main()
