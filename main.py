import interface


def main():
    path = input("Path to tle playlist: ").strip()
    app = interface.Application(path)
    app.mainloop()


if __name__ == "__main__":
    main()