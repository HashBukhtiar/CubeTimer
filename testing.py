import tkinter as tk

def on_select(option):
    label.config(text=f"Selected: {option}")

def main():
    global label  # Declare label as a global variable

    root = tk.Tk()

    options = ["Option 1", "Option 2", "Option 3"]

    selected_option = tk.StringVar()
    selected_option.set(options[0])  # Set default value

    dropdown_menu = tk.OptionMenu(root, selected_option, *options, command=on_select)
    dropdown_menu.pack()

    label = tk.Label(root, text="Selected: Option 1")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()