from main import *
import pytest


def test_pos_get_path():
    assert get_path("playlists/playlist") == "playlists/playlist"
    assert get_path("playlists/mixed_playlist") == "playlists/mixed_playlist"


def test_neg_get_path():
    with pytest.raises(SystemExit):
        get_path("definitely_oesnt/exist")
        get_path("")


def test_pos_get_theme():
    assert get_theme("dark") == {
        "button": "#411B5A",
        "button_on": "#1F0D2B",
        "button_fg": "#FFFFFF",
        "song_title": "#1F0D2B",
        "bg": "dark_bg.png",
    }


def test_neg_get_theme():
    with pytest.raises(SystemExit):
        get_theme("shiny")
        get_theme("")


def test_pos_get_format():
    assert get_format(".mp3") == ".mp3"
    assert get_format("both") == (".mp3", ".wav")


def test_neg_get_format():
    with pytest.raises(SystemExit):
        get_format(".py")
        get_format(".mp4")
