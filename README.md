# Music player
#### Video Demo:  https://youtu.be/Fv9n0z_MJ9A
#### Description: Basic music player.
#### Required: tkinter and pygame
Music player in which we can set up path to the playlist,\
choose one of three themes - dark, light and secret\
and choose file format/formats.

After set up, window pops up. Now we can use five buttons to\
navigate throught playlist. We can play/pause/unpause songs,\
go for the next/previous one or change the volume.

<p align="center">
  <img src="http://some_place.com/image.png](https://github.com/Arwers/Music-player/assets/52626118/bf65c2e1-190b-4657-95c8-e17be80ee96d" />
</p>

#### project file
    Main file used to setup app before opening window.
    Methods:
    --------
    get_path(path)
        check if the path is valid. If so, returns it.

    get_theme(theme)
        check if the theme is avalible. If so, returns dictionary\
        with instructions for specific theme.

    get_format(format)
        check if format is correct. If so, returns format or \
        tuple with formats.
#### audio file
##### Player class
    A class representation for a music player.

    Attributes:
    -----------
    path: str
        Path to the playlist
    playlist: list
        List of all files in .wav and/or .mp3 format from provided path.
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
#### interface file
##### Application class
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
