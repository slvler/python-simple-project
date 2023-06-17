from tkinter import *

root = Tk()
root.title('Input variable')
root.geometry("400x400")

e = Entry(root, width=50)
e.pack()
e.insert(0, 'What Your Name: ')

l = Label(root, text="what's up")
l.pack()


def clickFun():
    values = "My Name is " + e.get()
    l.configure(text=values)


button = Button(root, text="Click", command=clickFun)
button.pack(padx=50, pady=50)

root.mainloop()
