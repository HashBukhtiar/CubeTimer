import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def app_gui(title, width, height):

    root = tk.Tk()

    app_theme = "default"
    #app_theme = pick_theme()
    ui_config_lst = theme_config(app_theme)
    ui_config_dict = {
        "text_colour1" : ui_config_lst[0],
        "text_bg_colour1" : ui_config_lst[1],
        "bg_colour" : ui_config_lst[2],
        "text_colour2" : ui_config_lst[3]
    }

    app_font = "Helvecta"
    #app_font = pick_text_font()

    TITLE_SIZE = 40
    SECTION_HEADING_SIZE = 25
    SUBTITLE_SIZE = 15
    heading1 = font.Font(family=app_font, size=TITLE_SIZE, weight="bold")
    heading2 = font.Font(family=app_font, size=SECTION_HEADING_SIZE, weight="bold")
    heading3 = font.Font(family=app_font, size=SUBTITLE_SIZE)
    
    greeting = tk.Label(text="Welcome to CubeTimer", font=heading1, fg=ui_config_dict["text_colour1"], bg=ui_config_dict["text_bg_colour1"])
    greeting.place(relx=0.5, y=35, anchor="center")

    byline = tk.Label(text="by Hashim Bukhtiar", font=heading3, fg=ui_config_dict["text_colour2"], bg=ui_config_dict["text_bg_colour1"])
    byline.place(relx=0.5, y=75, anchor="center")

    SESSIONS_FRAME_X_DIST = 50
    SESSIONS_FRAME_Y_DIST = 150
    SESSIONS_FRAME_WIDTH = 400
    SESSIONS_FRAME_HEIGHT = 300
    SESSIONS_FRAME_BG = "#999999"
    sessions_frame = tk.Frame(root, bg=SESSIONS_FRAME_BG, relief=tk.SUNKEN, borderwidth=2, width=SESSIONS_FRAME_WIDTH, height=SESSIONS_FRAME_HEIGHT)
    sessions_frame.pack(fill=tk.BOTH, expand=True, padx=SESSIONS_FRAME_X_DIST, pady=SESSIONS_FRAME_Y_DIST)

    sessions_text = tk.Label(sessions_frame, text="Sessions", font=heading2, fg=ui_config_dict["text_colour2"], bg=SESSIONS_FRAME_BG)
    sessions_text.pack(side=tk.LEFT, padx=10, pady=10, anchor="nw")

    plus_icon = Image.open("assets/plus_icon.png").resize((20, 20))
    plus_icon_in_button = ImageTk.PhotoImage(plus_icon)
    BUTTON_FONT_SIZE = 12
    create_session_button = tk.Button(sessions_frame, text=" Create New Session ", bg="lightgray", 
                                      font=(app_font, BUTTON_FONT_SIZE), image=plus_icon_in_button, compound="left", borderwidth=2, 
                                      relief="raised", cursor="hand2")
    create_session_button.pack(side=tk.RIGHT, anchor=tk.NE, padx=20, pady=20)

    root.geometry(f"{width}x{height}")
    root.title(title)
    root.configure(background=ui_config_dict["bg_colour"])

    root.mainloop()

def pick_theme():
    # () -> str

    available_themes = ["default"]

    while True:
        print(f"\n{' | '.join(available_themes)}")
        chosen_theme = input("Enter the theme you want: ") # change to dropdown menu
        if chosen_theme in available_themes:
            return chosen_theme

def theme_config(theme):
    # (str) -> str, str, str,...

    if theme == "default":
        text_colour1 = "#ffffff"
        text_bg_colour1 = "#87CEEB"
        bg_colour = "#87CEEB"
        text_colour2 = "#343578"
    
    return text_colour1, text_bg_colour1, bg_colour, text_colour2

def pick_text_font():
    # () -> str

    available_fonts = ["Helvecta", "Arial", "Times New Roman"]

    while True:
        print(f"\n{' | '.join(available_fonts)}")
        chosen_font = input("Enter the font you want: ") # change to dropdown menu
        if chosen_font in available_fonts:
            return chosen_font