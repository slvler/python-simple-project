import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import time

ram_usage = []

def update_graph():
    ram_percent = psutil.virtual_memory().percent
    ram_usage.append(ram_percent)

    if len(ram_usage) > 50:
        ram_usage.pop(0)

    ax.clear()
    ax.plot(ram_usage, marker='o', linestyle='-', color='green', label="RAM (%)")
    ax.set_ylim(0, 100)
    ax.set_title("RAM")
    ax.legend()

    canvas.draw()
    root.after(1000, update_graph)

root = tk.Tk()
root.title("RAM")

fig = Figure(figsize=(5, 3), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

update_graph()
root.mainloop()
