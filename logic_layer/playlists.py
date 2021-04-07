from infrastructure_layer import infrastructure

add_playlist_URL = "http://127.0.0.1:3002/users/add_playlist"
add_song_URL = "http://127.0.0.1:3002/playlists/add_song"
get_playlist_URL = "http://127.0.0.1:3002/users/get_playlist"

def buildPlaylist(userName, UserPassword, playlistName):
    playlist = {"user_name" : userName,
                "User_password" : UserPassword,
                "playlist_name" : playlistName}

    return playlist


def postPlaylist(playlist):
    answer = infrastructure.post(add_playlist_URL, playlist)
    return answer


def addPlaylist(userName, UserPassword, playlistName):
    playlist = buildPlaylist(userName, UserPassword, playlistName)
    answer = postPlaylist(playlist)
    return answer


def addSongToPlaylist(userName, userPassword, playlistName, songTitle):
    data = {"user_name" : userName,
            "user_password" : userPassword,
            "Playlist_name" : playlistName,
            "song_title" : songTitle}

    answer = infrastructure.post(add_song_URL, data)

    return answer


def getPlaylist(userName, UserPassword, playlistName):
    data = {"user_name" : userName,
            "User_password" : UserPassword,
            "playlist_name" : playlistName}

    answer = infrastructure(get_playlist_URL, data)

    return answer
