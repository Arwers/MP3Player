from audio import Player
import pytest


def test_wrong_path():
    with pytest.raises(SystemExit):
        player = Player("notexistplaylist/test")


def test_path_songs():
    player = Player("playlists/playlist")
    assert bool(player.size) == True


def test_path_wrong_playlist():
    with pytest.raises(SystemExit):
        player = Player("playlists/wrong_playlist")


def test_path_empty_playlist():
    with pytest.raises(SystemExit):
        player = Player("playlists/empty_playlist")


def test_path_mixed_playlist():
    player = Player("playlists/mixed_playlist")
    assert player.size == 1
