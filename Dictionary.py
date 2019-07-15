def main():
    dictionary = open("dictionary.txt","r")
    in_dictionary = False

    print("Can your password survive a dictionary attack?")

    print()

    #Take input from the keyboard, storing in the variable test_password
    #NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    password = input("Type in a trial password: ")

    for word in dictionary:
        #password = find_password(password)
        if word.strip() == password.strip():
            in_dictionary = True
            wordstrip = word.strip()
            if wordstrip == wordstrip.vary():
                print("ERROR!!! Password not strong enough...You just got hacked")
                break

    if not in_dictionary:
        # dict.strip() == password.strip()
        print("------------------------")
        print("|      You pass!       |")
        print("------------------------")
        print("Your password is ==> ", password)
        print()


# def find_password(password):
#     return password

def vary(password):
    password  = password.replace("1", "l")
    password  = password.replace("@", "a")
    password  = password.replace("$", "s")
    password  = password.replace("0", "o")
    password  = password.replace("5", "s")
    password  = password.replace("!", "i")
    password  = password.replace("!", "l")
    password  = password.replace("/", "l")
    password  = password.replace("#", "h")
    password  = password.replace("3", "e")
    password  = password.replace("2", "L")
    password  = password.replace("8", "B")


if __name__ == '__main__':
    main()
