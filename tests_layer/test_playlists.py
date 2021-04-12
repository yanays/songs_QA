from logic_layer import playlists
from logic_layer import users
from logic_layer import songs
from logic_layer import admin


def test_add_playlists(oneUser):
    users.addUser("zeev", "123")
    answer = playlists.addPlaylist("yanay", "123", "myPlaylist1")
    assert admin.checkAnswer(answer), f"fail to add first playlist. status: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = playlists.addPlaylist("yanay", "123", "myPlaylist2")
    assert admin.checkAnswer(answer), f"fail to add second playlist. status: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = playlists.addPlaylist("zeev", "123", "myPlaylist1")
    assert admin.checkAnswer(answer), f"fail to add playlist for another user. status: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = playlists.addPlaylist("yanay", "123", "myPlaylist1")
    assert "error" in answer.json().keys(), f"ERROR: added twice the same playlist."

    answer = playlists.addPlaylist("yanay", "777", "myPlaylist3")
    assert "error" in answer.json().keys(), "ERROR: add playlist with wrong password"

    playlistsList = users.getUser("yanay").json()["data"]["playlists"]

    assert "myPlaylist1" in playlistsList, "first playlist not in list"
    assert "myPlaylist2" in playlistsList, "secomd playlist not in list"
    assert "myPlaylist3" not in playlistsList, "third playlist in list"


def test_add_song_to_playlist(SongUserPlaylist):
    answer = playlists.addSongToPlaylist("yanay", "123", "myPlaylist", "C")
    assert admin.checkAnswer(answer), f"fail to add song to playlist. status: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = playlists.addSongToPlaylist("yanay", "777", "myPlaylist", "C")
    assert "error" in answer.json().keys(), "ERROR: add song to playlist with wrong password"

    answer = playlists.addSongToPlaylist("yanay", "123", "myPlaylist", "F")
    assert "error" in answer.json().keys(), "ERROR: add song that doesn't exist to playlist"