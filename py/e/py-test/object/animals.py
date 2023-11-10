class Animals:

    Alive = True
    def hello(self):
        print("Animals Class")



class Mouse(Animals):

    def over(self):
        self.hello()

    def hi(self):
        print("hi world")



test11 = Mouse()

test11.over()
test11.hi()