import gui

def main():
    print("App Initialized")

    WINDOW_TITLE = "CubeTimer by Hashim B"
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600
    APP_FONT = "Helvecta"
    
    gui.app_gui(WINDOW_TITLE, DEFAULT_WIDTH, DEFAULT_HEIGHT, APP_FONT)

if __name__ == "__main__":
    main()