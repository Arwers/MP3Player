import interface
import os


def main():
    # setup
    path = get_path(input("Choose path: ").strip())

    print("Avalible themes: dark/light/secret")
    theme = get_theme(input("Choose Theme: ").strip())

    print("Avalible formats: .wav/.mp3/both")
    format = get_format(input("Choose format: ").strip())

    # launch
    app = interface.Application(path, theme, format)
    app.mainloop()


# check if theme is valid and give back dictionary
def get_theme(theme):
    themes = {
        "dark": {
            "button": "#411B5A",
            "button_on": "#1F0D2B",
            "button_fg": "#FFFFFF",
            "song_title": "#1F0D2B",
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

    if theme in themes:
        return themes[theme]
    else:
        exit("Theme doesn't exist")


# check if path exists
def get_path(path):
    if os.path.isdir(path):
        return path
    else:
        exit("Path doesn't exist")


# check if format is valid
def get_format(format):
    if format in [".mp3", ".wav"]:
        return format
    elif format == "both":
        return (".mp3", ".wav")
    else:
        exit("Format is not avalible")


if __name__ == "__main__":
    main()
