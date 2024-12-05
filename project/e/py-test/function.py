# def hello():
#     print("hello world")

# def message(name):
#     print("hello " + name)
#
# #hello()
# #message("Bro")
#
#
# def text(text1, text2):
#     return text1+' '+ text2
#
#
#
# def plus(number1, number2):
#     return number1 + number2
#
#
# name = text("hello", "world")
# print(name)
#
#
# total = plus(5,7)
# print(total)
# def approval(first_name, middle_name, last_name):
#     print("hello " + first_name + ' ' + middle_name + ' ' + last_name)
#
# approval(first_name="defne",middle_name="makbule",last_name="selviler")
# value = round(float(input("enter to a value: ")))
# print(value)



# def plus(*args):
#     return sum(args)
#
#
# total = plus(1,2,3,4,56,7,8,9)
#
# print(total)
#
#
# def gather(*args):
#     t = 1
#     for i in args:
#         t *= i
#     return t
#
#
# yx = gather(1,2,3)
#
# print(yx)




def message(**kwargs):
    #print("Hello " + kwargs['first_name'] + " " + kwargs['last_name'])
    for key,value in kwargs.items():
        print(value)


message(first_name="hicri", last_name="selviler")





