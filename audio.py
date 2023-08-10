from pygame import mixer
import os

class Player:
    """
    A class representation for a music player.

    Attributes:
    -----------
    path: str
        Path to the playlist
    playlist: list
        List of all files in .wav and .mp3 format from provided path.
    size: int
        Size of playlist (how many songs)
    position: int
        Current track index in playlist.
    state: bool
        Show if the song is loaded.
        True: loaded (play() ---> start a new song)
        False: not loaded (play() ---> pause/unpause song)
        Changes how play() works.
        
    Methods:
    --------
    print_playlist()
        Print all songs in playlist.
    play()
        Pause/unpause current song.
    prev()
        Play previous song. If song is first, play last one in playlist.
    next()
        Play next song. If song is last, play first one in playlist.
    volume_up()
        Turn volume up by 0.1 (max is 1.0).
    volume_down()
        Turn volume down by 0.1 (min is 0).
    """    
    def __init__(self, path: str):
        """
        Constructs all necessary attributes for the player object.
        Parameters
        ----------
        path: str
            Path to the playlist.
        """
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
        self.state = False

        mixer.init()
        mixer.music.set_volume(0.5)

    def __str__(self):
        """
        Prints info about object.
        """
        return f"Object representation of playlist in {self.path} location."

    def print_playlist(self):
        """
        Print all songs in playlist.
        """
        print("Player with loaded playlist: ")
        for i, song in enumerate(self.playlist):
            print(f"{i+1}. {song}")
    
    def play(self):
        """
        Pause/unpause current song.
        """
        if mixer.music.get_busy():
            mixer.music.pause()
        elif not self.state:
            try:
                mixer.music.load(f"{self.path}\{self.playlist[self.position]}")
                self.state = True
                mixer.music.play()
            except RuntimeError:
                exit("Failed to load and play track.")
        else:
            mixer.music.unpause()

    def prev(self):
        """
        Play previous song. If song is first, play last one in playlist.
        """
        mixer.music.stop()
        self.state = False
        if not self.position:
            self.position = self.size - 1
        else:
            self.position -= 1

        self.play()

    def next(self):
        """
        Play next song. If song is last, play first one in playlist.
        """
        mixer.music.stop()
        self.state = False
        if self.position == self.size - 1:
            self.position = 0
        else:
            self.position += 1

        self.play()

    def volume_up(self):
        """
        Turn volume up by 0.1 (max is 1.0).
        """
        temp = mixer.music.get_volume()
        mixer.music.set_volume(temp + 0.1)

    def volume_down(self):
        """
        Turn volume down by 0.1 (min is 0).
        """
        temp = mixer.music.get_volume()
        mixer.music.set_volume(temp - 0.1)