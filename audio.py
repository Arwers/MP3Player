from pygame import mixer
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
        mixer.music.set_volume(0.5)

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
        if not self.position:
            self.position = self.size - 1
        else:
            self.position -= 1

        self.play()

    def next(self):
        mixer.music.stop()
        self.state = 0
        if self.position == self.size - 1:
            self.position = 0
        else:
            self.position += 1

        self.play()

    def volume_up(self):
        temp = mixer.music.get_volume()
        mixer.music.set_volume(temp + 0.1)

    def volume_down(self):
        temp = mixer.music.get_volume()
        mixer.music.set_volume(temp - 0.1)