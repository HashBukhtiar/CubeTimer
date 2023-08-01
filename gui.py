import tkinter as tk
from tkinter import font

def app_gui(title, width, height, app_font):
    root = tk.Tk()

    root.geometry(f"{width}x{height}")
    root.title(title)

    TITLE_SIZE = 40
    text_font = font.Font(family=app_font, size=TITLE_SIZE, weight="bold")
    greeting = tk.Label(text="Welcome to CubeTimer", font=text_font)
    greeting.place(relx=0.5, y=30, anchor="center")

    root.mainloop()
