

password_pwd = input("What is the master password? ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line)


def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("password.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("set password type: ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()