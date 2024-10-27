import random

top = input("type a number: ")
if top.isdigit():
    top = int(top)

    if top <= 0:
        print("please type a number greater than zero")
        quit()
        
else:
    print("please type a number next time")
    quit()

random_number = random.randint(0, top)
guesses = 0

while True:
    guesses = guesses + 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("please type a number next time")
        continue


    if user_guess == random_number:
        print("you got it!")
        break

    elif user_guess > random_number:
            print("you are above the number")
    else:
            print("you are below the number")

print("you got it " + str(guesses) + " guesses")