import audioplayer as ap
import tkinter as tk
import os


class Player:
    def __init__(self, playlist):
        try:
            self.playlist = playlist
            # TODO: add file format filter
            self.all_tracks = os.listdir(playlist)
        except ValueError:
            exit("Failed to load playlist.")

    def __str__(self):
        return f"Object representation of playlist in {self.playlist} location."

    def print_playlist(self):
        print("Player with loaded playlist: ")
        for i, song in enumerate(self.all_tracks):
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