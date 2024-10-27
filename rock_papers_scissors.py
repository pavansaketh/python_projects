import random

user_wins = 0
compuer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type rock/paper/scissors or q to quit ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #  rock:1,  paper: 2, scissors: 3
    computer_pick = options[random_number]
    print("computer picked ", computer_pick + ".")


    if user_input == "rock" and computer_pick == "scissors":
        print("you win")
        user_wins = user_wins + 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you win")
        user_wins = user_wins + 1 

    elif user_input == "scissors" and computer_pick == "paper":
        print("you win")
        user_wins = user_wins + 1

    else:
        print("you lost")
        compuer_wins = compuer_wins + 1



print("you won " + str(user_wins) + " times.")
print("computer won " + str(compuer_wins) + " times.")
print("goodbye!")