from infrastructure_layer import infrastructure

add_song_URL = "https://github.com/theadamzaft/song-server-swagger/songs/add_song"
upvote_URL = "https://github.com/theadamzaft/song-server-swagger/songs/upvote"
downvote_URL = "https://github.com/theadamzaft/song-server-swagger/songs/downvote"
ranked_songs_URL = "https://github.com/theadamzaft/song-server-swagger/songs/ranked_songs"


def buildSong(genre, year, performer, title):
    song = {"song_genre" : genre,
            "song_year" : year,
            "song_performer" : performer,
            "song_title" : title}

    return song


def postSong(song):
    answer = infrastructure.post(add_song_URL, song)
    return answer


def addSong(genre, year, performer, title):
    song = buildSong(genre, year, performer, title)
    answer = postSong(song)
    return answer


def songVote(URL, userName, password, playlistName, songTitle):
    data = {"user_name" : userName,
            "password" : password,
            "playlist_name" : playlistName,
            "song_title" : songTitle}

    answer = infrastructure.put(URL, data)
    return answer


def songUpvote(userName, password, playlistName, songTitle):
    answer = songVote(upvote_URL, userName, password, playlistName, songTitle)
    return answer


def songDownvote(userName, password, playlistName, songTitle):
    answer = songVote(downvote_URL, userName, password, playlistName, songTitle)
    return answer


def getSongByRank(rank, op):
    data = {"rank" : rank,
            "op" : op}

    answer = infrastructure.get(ranked_songs_URL, data)
    return answer
