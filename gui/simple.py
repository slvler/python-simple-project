from tkinter import Tk, Label, Button
class Simple:

    def __init__(self, root):
        root.title("Basic Tkinter")
        root.geometry("300x200")

        self.label = Label(root, text="Hello World")
        self.label.pack(pady=20)

        button = Button(root, text="Click", command=self.btnClick)
        button.pack(pady=10)

    def btnClick(self):
        self.label.config(text="Button Clicked!")


root = Tk()
simple = Simple(root)
root.mainloop()