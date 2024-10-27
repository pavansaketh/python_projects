name = input("type your name: ")
print("welcome", name, " to this adventure")

answer = input("which way do you want to go left or right: ").lower()

if answer == "left":
    answer = input("you come to  a river, you can walk around or swim accross?")

    if answer == "swim":
        print("you swam and were eaten by crocodile")
    elif answer == "walk":
        print("you ran for miles an died")
    else:
        print("not a valid option. you lost")


elif answer == "right":
    answer = input("you come to bridge. you want to cross it or go back? ")
    if answer == "back":
        print("you go back and lost")
    elif answer == "cross":
        answer = input("you cross a brigde and met someone. you want to talk? yes or no ")
        if answer == "yes":
            print("you won")
        else:
            print("you lost")


else:
    print("not a valid option. you lost")

print("thank you", name)