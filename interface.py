import tkinter as tk
from tkinter import ttk
import audio

class Application(tk.Tk):
    """GUI for player class."""
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

        #set background
        bg = tk.PhotoImage(file = "resources/bg.png")
        bg_label = tk.Label(
            self,
            image = bg,
            )
        bg_label.image = bg # keeping the reference
        bg_label.place(
            x = 0,
            y = 0, 
            relheight=1,
            relwidth=1,
            )

        # buttons
        play_button = tk.Button( 
            self, 
            text = "⏯️",
            command = self.play_button,
            font = (None, 20),
            bg = "#FFFFFF",
            activebackground='#FFFFFF',
            )
        
        next_button = tk.Button( 
            self, 
            text = "⏭️",
            command = self.next_button,
            font=(None, 20),
            bg = "#FFFFFF",
            activebackground='#FFFFFF',
            )   

        prev_button = tk.Button( 
            self, 
            text = "⏮️",
            command = self.prev_button,
            font = (None, 20),
            bg = "#FFFFFF",
            activebackground='#FFFFFF',
            )
        
        up_button = tk.Button( 
            self, 
            text = "🔼",
            command = self.player.volume_up,
            font = (None, 20),
            bg = "#FFFFFF",
            activebackground='#FFFFFF',
            )
        
        down_button = tk.Button( 
            self, 
            text = "🔽",
            command = self.player.volume_down,
            font = (None, 20),
            bg = "#FFFFFF",
            activebackground='#FFFFFF',
            )
        
        # setup label
        self.song_title = tk.Label(
            text = self.player.playlist[self.player.position],
            bg = "#F1D9FC",
            font = (None, 10),
            width = 37,
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
            columnspan = 6,
            )
        up_button.grid(
            row=1,
            column=4,
        )
        down_button.grid(
            row=1,
            column=5,
        )

        # anchor widget to the centre
        self.grid_anchor("center")
        
    # extensions for the player functions 
    def prev_button(self):
        self.player.prev()
        self.song_title.config(
            text = self.player.playlist[self.player.position],
            )

    def next_button(self):
        self.player.next()
        self.song_title.config(
            text = self.player.playlist[self.player.position],
            )

    def play_button(self):
        self.player.play()