import random


while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)

    my_choice = None

    while my_choice not in choices:
        my_choice = input("rock ? paper ? scissors: ").lower()


    if my_choice == computer:
        print("Computer choice: ", computer)
        print("My choice: ", my_choice)
        print("Bravo")
    else:
        print("Computer choice: ", computer)
        print(":(")
        print("Try")

    status = input("okey ? yes/no").lower()

    if status == "yes":
        break

print("Bye")