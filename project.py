from pygame import mixer
import tkinter as tk
from tkinter import ttk
import os


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
        self.state = 0
        mixer.init()

    def __str__(self):
        return f"Object representation of playlist in {self.path} location."

    def print_playlist(self):
        print("Player with loaded playlist: ")
        for i, song in enumerate(self.playlist):
            print(f"{i+1}. {song}")
    
    def play(self):
        if mixer.music.get_busy():
            mixer.music.pause()
        elif not self.state:
            try:
                mixer.music.load(f"{self.path}\{self.playlist[self.position]}")
                self.state = 1
                mixer.music.play()
            except RuntimeError:
                exit("Failed to load and play track.")
        else:
            mixer.music.unpause()

    def prev(self):
        mixer.music.stop()
        self.state = 0
        if self.position:
            self.position = self.size - 1
            self.play()
        else:
            self.position -= 1

    def next(self):
        mixer.music.stop()
        self.state = 0
        if self.position == self.size - 1:
            self.position = 0
            self.play()
        else:
            self.position += 1


class Application(tk.Tk):
    def __init__(self, path):
        player = Player(path)
        
        # standard setup
        tk.Tk.__init__(self)
        self.title("Music player")
        self.geometry("500x200")
        self.configure(bg='#3A3A3A')

        # buttons
        play = tk.Button( 
            self, 
            text = "⏯️",
            command = player.play,
            font = (None, 20),
            bg = "#656565",
            activebackground='#747474',
            )
        
        next = tk.Button( 
            self, 
            text = "⏭️",
            command = player.next,
            font=(None, 20),
            bg = "#656565",
            activebackground='#747474',
            )   

        prev = tk.Button( 
            self, 
            text = "⏮️",
            command = player.prev,
            font = (None, 20),
            bg = "#656565",
            activebackground='#747474',
            )
        
        # pack the buttons
        prev.pack()
        play.pack()
        next.pack()


def main():
    app = Application("C:\MyFiles\Projects\Python\project\playlist1")
    app.mainloop()


if __name__ == "__main__":
    main()