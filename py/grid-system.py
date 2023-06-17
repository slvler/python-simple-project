from tkinter import *


root = Tk()


label1 = Label(root, text="Label - 1 section", fg="red")
label2 = Label(root, text="Label - 2 section")
label3 = Label(root, text="Label - 3 section", fg="black", font=("Helvetica", 18))

label1.grid(row=0, column=0)
label2.grid(row=1, column=5)
label3.grid(row=2, column=2)

root.mainloop()