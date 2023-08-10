import tkinter as tk
from tkinter import ttk
import audio

class Application(tk.Tk):
    def __init__(self, path):
        player = audio.Player(path)
        
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

    def prev_button():
        ...
    def play_button():
        ...
    def next_button():
        ...