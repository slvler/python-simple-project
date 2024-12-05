def addition(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def extraction(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiplication(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def division(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Extraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choise: ")

    if choice == "a" or choice == "A":
        print("Addition")
        firstNumber = int(input('input first number: '))
        secondNumber = int(input('input second number: '))
        addition(firstNumber, secondNumber)
    if choice == "b" or choice == "B":
        print('Extraction')
        firstNumber = int(input('input first number: '))
        secondNumber = int(input('input second number: '))
        extraction(firstNumber,secondNumber)
    if choice == "c" or choice == "C":
        print('multiplication')
        firstNumber = int(input('input first number: '))
        secondNumber = int(input('input second number: '))
        multiplication(firstNumber,secondNumber)
    if choice == "d" or choice == "D":
        print('Division')
        firstNumber = int(input('input first number: '))
        secondNumber = int(input('input second number: '))
        division(firstNumber, secondNumber)
    if choice == "e" or choice == "E":
        print("program ended")
        quit()