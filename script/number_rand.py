import random


answer = input("Please enter a number ")

if answer.isdigit():
    answer = int(answer)
    if answer <= 0:
        print("please enter a number greater than zero ")
        quit()
else:
    print("please enter a number! ")
    quit()


random_number = random.randint(0, answer)

guesses = 0

while True:
    guesses += 1
    user_answer = input("Answer:" )
    if user_answer.isdigit():
        user_answer = int(user_answer)
    else:
        print("Error")

    if user_answer == random_number:
        print("-------- Success  ----------")
        break
    else:
        if user_answer > random_number:
            print(">>>>>")
        else:
            print("<<<<<")

print(guesses, "you know at the end of the try ")


