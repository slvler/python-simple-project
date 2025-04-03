from tkinter import Tk, Canvas
import psutil

def ram_usage():
    ram_percent = psutil.virtual_memory().percent
    canvas.delete("all")

    width = 200
    height = 30
    fill_width = (ram_percent / 100) * width

    canvas.create_rectangle(5, 5, width + 5, height + 5, outline="green", width=2)

    canvas.create_rectangle(5, 5, fill_width + 5, height + 5, fill="black")

    canvas.create_text(width // 2, height // 2, text=f"{ram_percent:.2f}%", font=("Arial", 12, "bold"), fill="white")

    root.after(1000, ram_usage)

root = Tk()
root.title("RAM Visualization")

canvas = Canvas(root, width=210, height=40)
canvas.pack()

ram_usage()

root.mainloop()