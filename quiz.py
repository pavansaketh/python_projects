print("welcome to the quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")

score = 0

answer = input("what is cpu stands for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score = score + 1
else:
    print("incorrect!")

answer = input("what is Gpu stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score = score + 1
else:
    print("incorrect!")

answer = input("what is ram stands for? ")
if answer.lower() == "random access memeory":
    print("correct")
    score = score + 1
else:
    print("incorrect!")

answer = input("what is rom stands for? ")
if answer.lower() == "read only memory":
    print("correct")
    score = score + 1
else:
    print("incorrect!")

answer = input("what is http stands for? ")
if answer.lower() == "hyper text transfer protocol":
    print("correct")
    score = score + 1
else:
    print("incorrect!")

print("you got " + str(score) + " questions correct!")
