import tkinter as tk
from tkinter import ttk
import audio

class Application(tk.Tk):
    def __init__(self, path):
        self.player = audio.Player(path)
        
        # standard setup
        tk.Tk.__init__(self)
        self.title("Music player")
        
        # Adjust size
        self.geometry("500x200")
        
        # set minimum window size value
        self.minsize(500, 200)
        
        # set maximum window size value
        self.maxsize(500, 200)

        # set background color
        self.configure(bg='#3A3A3A')

        # buttons
        play_button = tk.Button( 
            self, 
            text = "⏯️",
            command = self.play_button,
            font = (None, 20),
            bg = "#656565",
            activebackground='#747474',
            )
        
        next_button = tk.Button( 
            self, 
            text = "⏭️",
            command = self.next_button,
            font=(None, 20),
            bg = "#656565",
            activebackground='#747474',
            )   

        prev_button = tk.Button( 
            self, 
            text = "⏮️",
            command = self.prev_button,
            font = (None, 20),
            bg = "#656565",
            activebackground='#747474',
            )
        
        # setup label
        self.song_title = tk.Label(
            self,
            text = self.player.playlist[self.player.position],
            bg = "#FFFFFF",
            font = (None, 10),
            width = 22,
            anchor="w"
            )

        # setup grid
        prev_button.grid(
            row = 1,
            column = 0,
            )
        play_button.grid(
            row = 1,
            column = 1,
            )
        next_button.grid(
            row = 1,
            column = 2,
            )
        self.song_title.grid(
            row = 0,
            column = 0,
            columnspan = 3,
            )

        # anchor widget to the centre
        self.grid_anchor("center")
        

    def prev_button(self):
        self.player.prev()
        self.song_title.config(
            text = self.player.playlist[self.player.position],
            )

    def play_button(self):
        self.player.play()

    def next_button(self):
        self.player.next()
        self.song_title.config(
        text = self.player.playlist[self.player.position],
        )