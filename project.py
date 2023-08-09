from pygame import mixer
import tkinter as tk
import os
import time


class Player:
    def __init__(self, path: str):
        # get list of all files in folder
        try:
            all_files = os.listdir(path)
        except ValueError:
            exit("Failed to load playlist.")

        # filter out wrong file types
        self.playlist = [s for s in all_files if s.endswith((".mp3", ".wav"))]
        if not self.playlist:
            exit("Provided playlist is empty.")
        
        self.path = path
        self.size = len(self.playlist)
        self.position = 0
        mixer.init()

    def __str__(self):
        return f"Object representation of playlist in {self.path} location."

    def print_playlist(self):
        print("Player with loaded playlist: ")
        for i, song in enumerate(self.playlist):
            print(f"{i+1}. {song}")
    
    def play(self):
        try:
            mixer.music.load(f"{self.path}\{self.playlist[self.position]}")
            mixer.music.play()
        except RuntimeError:
            exit("Failed to load and play track.")

    def pause(self):
        if mixer.music.get_busy:
            mixer.music.pause()

    def unpause(self):
        mixer.music.unpause()

    def volume(self):
        ...
    def prev(self):
        ...
    def skip(self):
        ...


class Window:
    ...

def main():
    player = Player("C:\MyFiles\Projects\Python\project\playlist1")
    player.print_playlist()
    player.play()
    time.sleep(2)
    player.pause()
    time.sleep(2)
    print(player)
    root = tk.Tk()
    root.mainloop()


if __name__ == "__main__":
    main()