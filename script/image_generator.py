import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style

root = tk.Tk()
root.title("Image Generator")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False, False)
style = Style(theme="sandstone")


def image_request(category):

    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=1n7sSMtCh8Hs_MrBOjhQ1SygTDA-BJ550UdX3rwLYZQ"
    data = requests.get(url).json()

    img_data = requests.get(data["urls"]["regular"]).content
    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
    label.config(image=photo)
    label.image = photo


def enable_button(*args):
    generate_button.config(state="normal" if category_var.get() != "Choose Category" else "disabled")

def create_gui():
    global category_var, generate_button, label

    category_var = tk.StringVar(value="Choose Category")

    category_options = ["Choose Category", "Food", "Animals", "People", "Music", "Art", "Vehicles", "Random"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, sticky="nsew")
    category_dropdown.config(width=14)

    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=14)

    generate_button = ttk.Button(text="Generate Image",
                                 command=lambda: image_request("Animals"))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()


if __name__ == "__main__":
    create_gui()