import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    choice = input("Rock/Paper/Scissors or Q to Quit:  ").lower()
    if choice == "q":
        break

    if choice not in options:
        continue

    randmNumber = random.randint(0, 2)
    computer_choice = options[randmNumber]
    print("Compouter Choice:" + computer_choice)

    if choice == "rock" and computer_choice == "scissors":
        print("User won")
        user_score += 1
        continue

    elif choice == "paper" and computer_choice == "rock":
        print("User won")
        user_score += 1
        continue

    elif choice == "scissors" and computer_choice == "paper":
        print("User won")
        user_score += 1
        continue

    else:
        print("You Lost")
        computer_score += 1


print("Total round " + str(int(user_score + computer_score )))
print("You won " + str(user_score) + " times.")
print("Computer won " + str(computer_score) + " times.")