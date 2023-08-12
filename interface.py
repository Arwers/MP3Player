import tkinter as tk
import audio


class Application(tk.Tk):
    """
    A class representation of GUI made for player class.

    Attributes:
    -----------
    player: Player
        Player object.

    Methods:
    --------
    play_button()
        play the song.
    next_button()
        play next song and change label.
    prev_button()
        play previous song and change label.
    """

    def __init__(self, path, theme, format):
        """
        Constructs all necessary attributes for the application object.

        Parameters:
        -----------
        path: str
            Path to the playlist.
        """
        # Make player object
        self.player = audio.Player(path, format)

        # Make Tk object
        tk.Tk.__init__(self)

        # Change window title
        self.title("Music player")

        # Adjust size
        self.geometry("500x200")

        # set minimum window size value
        self.minsize(500, 200)

        # set maximum window size value
        self.maxsize(500, 200)

        # set background
        bg = tk.PhotoImage(file=f"resources/{theme['bg']}")
        bg_label = tk.Label(
            self,
            image=bg,
        )
        bg_label.image = bg  # keeping the reference
        bg_label.place(
            x=0,
            y=0,
            relheight=1,
            relwidth=1,
        )

        # buttons
        play_button = tk.Button(
            self,
            text="⏯️",
            command=self.play_button,
            font=(None, 20),
            bg=theme["button"],
            activebackground=theme["button_on"],
            fg=theme["button_fg"],
        )

        next_button = tk.Button(
            self,
            text="⏭️",
            command=self.next_button,
            font=(None, 20),
            bg=theme["button"],
            activebackground=theme["button_on"],
            fg=theme["button_fg"],
        )

        prev_button = tk.Button(
            self,
            text="⏮️",
            command=self.prev_button,
            font=(None, 20),
            bg=theme["button"],
            activebackground=theme["button_on"],
            fg=theme["button_fg"],
        )

        up_button = tk.Button(
            self,
            text="🔼",
            command=self.player.volume_up,
            font=(None, 20),
            bg=theme["button"],
            activebackground=theme["button_on"],
            fg=theme["button_fg"],
        )

        down_button = tk.Button(
            self,
            text="🔽",
            command=self.player.volume_down,
            font=(None, 20),
            bg=theme["button"],
            activebackground=theme["button_on"],
            fg=theme["button_fg"],
        )

        # setup label
        self.song_title = tk.Label(
            text=self.player.playlist[self.player.position],
            bg=theme["song_title"],
            fg=theme["button_fg"],
            font=(None, 10),
            width=37,
            
        )

        # Set buttons on the grid
        prev_button.grid(
            row=1,
            column=0,
        )
        play_button.grid(
            row=1,
            column=1,
        )
        next_button.grid(
            row=1,
            column=2,
        )
        up_button.grid(
            row=1,
            column=4,
        )
        down_button.grid(
            row=1,
            column=5,
        )

        # Set labels on the grid
        self.song_title.grid(
            row=0,
            column=0,
            columnspan=6,
        )

        # Anchor grid to the centre
        self.grid_anchor("center")

    def prev_button(self):
        """Get previous song and update label"""
        self.player.prev()
        self.song_title.config(
            text=self.player.playlist[self.player.position],
        )

    def next_button(self):
        """Get next song and update label"""
        self.player.next()
        self.song_title.config(
            text=self.player.playlist[self.player.position],
        )

    def play_button(self):
        """Play the song. Not really usefull atm, made for the future updates."""
        self.player.play()
