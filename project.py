import interface
import os
import random

def main():
    # setup
    path =input("Choose path: ")
    theme = get_theme()

    # launch
    app = interface.Application(path, theme)
    app.mainloop()


# check if theme is valid and give back dictionary
def get_theme():
    themes = {
        "dark": {
            "button": "#411B5A",
            "button_on": "#1F0D2B",
            "button_fg": "#FFFFFF",
            "song_title": "#1F0D2B",
            "bg": "dark_bg.png",
        },
        "light": {
            "button": "#BF99D8",
            "button_on": "#8449AC",
            "button_fg": "#FFFFFF",
            "song_title": "#8449AC",
            "bg": "light_bg.png",
        },
        "secret": {
            "button": "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]),
            "button_on": "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]),
            "button_fg": "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]),
            "song_title": "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]),
            "bg": "secret_bg.png",
        },
    }

    print("Avalible themes: dark/light/secret")
    while True:
        theme = input("Choose theme: ")
        if theme in themes:
            return themes[theme]
        else:
            print("Theme doesn't exist. Try again.")


if __name__ == "__main__":
    main()
