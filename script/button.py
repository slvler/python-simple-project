from tkinter import *



root = Tk()


def clickMe():
    mylabel = Label(root, text="button on click!")
    mylabel.pack()


myButton = Button(root, text="Click", padx=50, pady=50, command=clickMe)
myButton.pack()

root.mainloop()