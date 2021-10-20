import random
print("welcome to the guesses game! choose a number between 1 to 1000 until you guessed the right number")

botguess = random.randint(1, 1000)
userguess = None
guesses = 0

while(userguess !=botguess):
        userguess = int(input("enter the number: "))
        guesses = guesses + 1

        if (userguess == botguess):
            print(f"congrats!you guessed it right and you guessed it in {guesses} times")
        else:
            if userguess>botguess:
                print("oops you have guessed higher number pls choose a lower number:\n")
            else:
                print("higher number please: ")

'''                                       Creating Endless Loop                                                               '''

while True:
    user = input("wanna play again then type yes else type no : \n")
    if user == "yes":
        botguess = random.randint(1, 1000)
        userguess = None
        guesses = 0
    elif user == "no":
        print ("thanks")
        break

    while(userguess !=botguess):
            userguess = int(input("enter the number: "))
            guesses = guesses + 1

            if (userguess == botguess):
                print(f"congrats!you guessed it right and you guessed it in {guesses} times")
            else:
                if userguess>botguess:
                    print("oops you have guessed higher number pls choose a lower number:\n")
                else:
                    print("higher number please: ")


# else:
#      print("thanks")

