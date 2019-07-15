import random

# A list of words that
list = ["harry", "hermione", "ron", "wand", "gryffindor", "wizard", "magic"]

word = random.choice(list)

# Use to test your code:
print(word)

# Converts the word to lowercase
word = word.lower()

place = list.index(word)


# Make it a list of letters for someone to guess
spaces = ['_ _ _ _ _', '_ _ _ _ _ _ _ _', '_ _ _', '_ _ _ _', '_ _ _ _ _ _ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _'] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 10
fails = 0

wordspaces = spaces[place]

while fails < maxfails:
    print(spaces[place])

    guess = input("Guess a letter: ")

    	# check if the guess is valid: Is it one letter? Have they already guessed it?
    if guess in word:
        letterplace = word.index(guess)

        word.replace (wordspaces[letterplace], guess)

    fails = fails+1
    print("You have " + str(maxfails - fails) + " tries left!")

print()
if fails == maxfails:
    print ("You're out of guesses nOoooOOOOOOOoOoOooOOOooOOOOoOOoOOooOo!!!!")
elif guess == words:
    print ("YAY YOU GOT IT YA GENIUS WOOOOOO!!")

    	# check if the guess is correct: Is it in the word? If so, reveal the letters!
