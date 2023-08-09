import audioplayer as ap
import tkinter as tk
import os


class Player:
    def __init__(self, path):
        try:
            all_files = os.listdir(path)
        except ValueError:
            exit("Failed to load playlist.")

        self.path = path
        self.playlist = [s for s in all_files if s.endswith((".mp3", ".wav"))]
        if not self.playlist:
            exit("Provided playlist is empty.")

    def __str__(self):
        return f"Object representation of playlist in {self.path} location."

    def print_playlist(self):
        print("Player with loaded playlist: ")
        for i, song in enumerate(self.playlist):
            print(f"{i+1}. {song}")
    
    def play(self, song):
        # !
        try:
            self.player = ap.AudioPlayer(f"{self.playlist}/{song}").play()
        except FileNotFoundError:
            exit("Song not found in a playlist.")
    def stop(self, current_track):
        ...
    def volume(self, current_track):
        ...
    def prev(self):
        ...
    def skip(self):
        ...


class Window:
    ...

def main():
    player = Player("./playlist1")
    player.print_playlist()
    print(player)


if __name__ == "__main__":
    main()