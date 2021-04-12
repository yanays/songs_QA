import pytest
import logic_layer.admin as admin
import logic_layer.songs as songs
import logic_layer.users as users
import logic_layer.playlists as playlists

@pytest.fixture
def resetSongs():
    admin.deleteAllSomgs()


@pytest.fixture
def resetUsers():
    admin.deleteAllUsers()


@pytest.fixture
def resetData():
    admin.deleteAllSomgs()
    admin.deleteAllUsers()


@pytest.fixture
def oneSong():
    admin.deleteAllSomgs()
    admin.deleteAllUsers()
    songs.postSong(songs.defaultSong)


@pytest.fixture
def oneUser():
    admin.deleteAllSomgs()
    admin.deleteAllUsers()
    users.postUser(users.defaultUser)


@pytest.fixture
def oneSongAndUser():
    admin.deleteAllSomgs()
    admin.deleteAllUsers()
    songs.postSong(songs.defaultSong)
    users.postUser(users.defaultUser)

@pytest.fixture
def SongUserPlaylist():
    admin.deleteAllSomgs()
    admin.deleteAllUsers()
    songs.postSong(songs.defaultSong)
    users.postUser(users.defaultUser)
    playlists.postPlaylist(playlists.defaultPlaylist)