import tkinter as tk
from tkinter import font

def app_gui(title, width, height):
    root = tk.Tk()

    app_theme = "default"
    #app_theme = pick_theme()
    ui_config_lst = theme_config(app_theme)
    ui_config_dict = {
        "text_colour" : ui_config_lst[0],
        "text_bg_colour" : ui_config_lst[1],
        "bg_colour" : ui_config_lst[2]
    }

    app_font = "Helvecta"
    #app_font = pick_text_font()

    TITLE_SIZE = 40
    text_font = font.Font(family=app_font, size=TITLE_SIZE, weight="bold")
    greeting = tk.Label(text="Welcome to CubeTimer", font=text_font, fg=ui_config_dict["text_colour"], bg=ui_config_dict["text_bg_colour"]) # add bg colour
    greeting.place(relx=0.5, y=30, anchor="center")

    root.geometry(f"{width}x{height}")
    root.title(title)
    root.configure(background=ui_config_dict["bg_colour"])

    root.mainloop()

def pick_theme():
    # () -> str

    available_themes = ["default"]

    while True:
        print(f"\n{' | '.join(available_themes)}")
        chosen_theme = input("Enter the theme you want: ")
        if chosen_theme in available_themes:
            return chosen_theme

def theme_config(theme):
    # (str) -> str, str, str,...

    if theme == "default":
        text_colour = "#ffffff"
        text_bg_colour = "#1d4159"
        bg_colour = "#1d4159"
    
    return text_colour, text_bg_colour, bg_colour

def pick_text_font():
    # () -> str

    available_fonts = ["Helvecta", "Arial", "Times New Roman"]

    while True:
        print(f"\n{' | '.join(available_fonts)}")
        chosen_font = input("Enter the theme you want: ")
        if chosen_font in available_fonts:
            return chosen_font