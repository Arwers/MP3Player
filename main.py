import interface
import os


def main():
    # setup
    path = get_path()
    theme = get_theme()
    format = get_format()

    # launch
    app = interface.Application(path, theme, format)
    app.mainloop()


# choose theme
def get_theme():
    themes = {
        "dark": {
            "button": "#0A0A0A",
            "button_on": "#1C1C1C",
            "button_fg": "#FFFFFF",
            "song_title": "#1C1C1C",
            "bg": "dark_bg.png",
        },
        "light": {
            "button": "#FFFFFF",
            "button_on": "#DBDBDB",
            "button_fg": "#0A0A0A",
            "song_title": "#DBDBDB",
            "bg": "light_bg.png",
        },
        "secret": {
            "button": "#FFFFFF",
            "button_on": "#DBDBDB",
            "button_fg": "#0A0A0A",
            "song_title": "#DBDBDB",
            "bg": "secret_bg.png",
        },
    }
    print("options: dark/light/secret")
    while True:
        choice = input("Choose Background: ").strip()
        if choice in themes:
            return themes[choice]


# get path
def get_path():
    while True:
        path = input("Path to the playlist: ").strip()
        if os.path.isdir(path):
            return path


def get_format():
    print("options: .mp4/.wav/all")
    while True:
        format = input("Choose format: ").strip()
        if format in [".mp4", ".wav"]:
            return format
        elif format == "all":
            return (".mp4", ".wav")


if __name__ == "__main__":
    main()
