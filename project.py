from pygame import mixer
import tkinter as tk
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


class Application(tk.Tk):
    def __init__(self, path):
        player = Player(path)
        tk.Tk.__init__(self)
        self.title("Music player")

        #buttons
        play = tk.Button( 
            self, 
            text = "play",
            command = player.play
            )
        play.pack()

        pause = tk.Button( 
            self, 
            text = "pause",
            command = player.pause
            )
        pause.pack()
        
        unpause = tk.Button( 
            self, 
            text = "unpause",
            command = player.unpause
            )
        unpause.pack()        


def main():
    app = Application("C:\MyFiles\Projects\Python\project\playlist1")
    app.mainloop()


if __name__ == "__main__":
    main()