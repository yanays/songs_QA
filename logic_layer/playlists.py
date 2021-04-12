from infrastructure_layer import infrastructure
from logic_layer import logicconfig

def buildPlaylist(userName, userPassword, playlistName):
    playlist = {"user_name" : userName,
                "user_password" : userPassword,
                "playlist_name" : playlistName}

    return playlist


def postPlaylist(playlist):
    answer = infrastructure.post(logicconfig.add_playlist_URL, playlist)
    return answer


def addPlaylist(userName, UserPassword, playlistName):
    playlist = buildPlaylist(userName, UserPassword, playlistName)
    answer = postPlaylist(playlist)
    return answer


def addSongToPlaylist(userName, userPassword, playlistName, songTitle):
    data = {"user_name" : userName,
            "user_password" : userPassword,
            "playlist_name" : playlistName,
            "song_title" : songTitle}

    answer = infrastructure.post(logicconfig.add_song_to_playlist_URL, data)

    return answer


def getPlaylist(userName, UserPassword, playlistName):
    data = {"user_name" : userName,
            "User_password" : UserPassword,
            "playlist_name" : playlistName}

    answer = infrastructure(logicconfig.get_playlist_URL, data)

    return answer


defaultPlaylist = {"user_name" : "yanay",
                    "user_password" : "123",
                    "playlist_name" : "myPlaylist"}