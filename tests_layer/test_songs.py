from logic_layer import songs
from logic_layer import users
from logic_layer import playlists
from logic_layer import admin
import pytest

def test_add_song(resetData):
    answer = songs.addSong("A", "1", "B", "C")
    assert admin.checkAnswer(answer), f"fail to add song. status: {answer.status_code}\nerror: {answer.json()['error']}"


@pytest.mark.xfail(reason = "bug: user can vote twice")
def test_song_vote(SongUserPlaylist):
    playlists.addSongToPlaylist("yanay", "123", "myPlaylist", "C")
    answer = songs.songUpvote("yanay", "123", "myPlaylist", "C")
    assert admin.checkAnswer(answer), f"fail to upvote song. status: {answer.status_code}\nerror: {answer.json()['error']}"

    songs.addSong("X", "2", "Y", "Z")
    playlists.addSongToPlaylist("yanay", "123", "myPlaylist", "Z")
    answer = songs.songDownvote("yanay", "123", "myPlaylist", "Z")
    assert admin.checkAnswer(answer), f"fail to downvote song. status: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = songs.songDownvote("yanay", "123", "myPlaylist", "C")
    assert "error" in answer.json().keys(), "ERROR: upvote and then downvote same song"
    answer = songs.songUpvote("yanay", "123", "myPlaylist", "C")
    assert "error" in answer.json().keys(), "ERROR: upvote song twice"
    answer = songs.songUpvote("yanay", "123", "myPlaylist", "Z")
    assert "error" in answer.json().keys(), "ERROR: downvote and then upvote same song"
    answer = songs.songDownvote("yanay", "123", "myPlaylist", "Z")
    assert "error" in answer.json().keys(), "ERROR: downvote song twice"

    answer = songs.songDownvote("yanay", "123", "myPlaylist", "DD")
    assert "error" in answer.json().keys(), "ERROR: vote for song that doesn't exist"

    users.addUser("zeev", "777")
    answer = songs.songUpvote("zeev", "777", "myPlaylist", "C")
    assert admin.checkAnswer(answer), f"another user can't vote. status: {answer.status_code}\nerror: {answer.json()['error']}"


def test_initial_rank(SongUserPlaylist):
    playlists.addSongToPlaylist("yanay", "123", "myPlaylist", "C")
    answer = songs.getSong("C")
    assert answer.json()["data"]["rating"]==0, f"wrong initiel rank: {answer.json()['data']['rating']}"


def test_song_by_rank(SongUserPlaylist):
    playlists.addSongToPlaylist("yanay", "123", "myPlaylist", "C")
    answer = songs.getSongByRank("0", "eq")
    assert songs.assertGetByRank(answer, "C", True), f"song rank 0, eq 0.\nstatus: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = songs.getSongByRank("1", "less")
    assert songs.assertGetByRank(answer, "C", True), f"song rank 0, less 1.\nstatus: {answer.status_code}\nerror: {answer.json()['error']}"

    songs.songUpvote("yanay", "123", "myPlaylist", "C")

    answer = songs.getSongByRank("1", "eq")
    assert songs.assertGetByRank(answer, "C", True), f"song rank 1, eq 1.\nstatus: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = songs.getSongByRank("0", "greater")
    assert songs.assertGetByRank(answer, "C", True), f"song rank 1, greater 0.\nstatus: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = songs.getSongByRank("1", "less")
    assert songs.assertGetByRank(answer, "C",
                                 False), f"song rank 1, less 1.\nstatus: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = songs.getSongByRank("2", "eq")
    assert songs.assertGetByRank(answer, "C",
                                 False), f"song rank 1, eq 2.\nstatus: {answer.status_code}\nerror: {answer.json()['error']}"


def test_negative_rank(SongUserPlaylist):
    playlists.addSongToPlaylist("yanay", "123", "myPlaylist", "C")
    songs.songDownvote("yanay", "123", "myPlaylist", "C")
    answer = songs.getSong("C")

    assert answer.json()["data"]["rating"]>=0, f"negative rank: {answer.json()['data']['rating']}"
