print("Welcome to computer quiz")

playing = input("Do you want to play? ")

score = 0

if playing.lower() != "yes":
    quit()

print("Okey lets go")

answer = input("Question 1: What do you do ")

if answer.lower() == "python working":
    score += 1
    print("Successful")
else:
    print("Sorry :(")

answer = input("Question 2: What do you do ")

if answer.lower() == "math working":
    score += 1
    print("Successful")
else:
    print("Sorry :(")


print("quiz score: " + str(score))
print("quiz score: " + str((score / 2) * 100) + "%.")