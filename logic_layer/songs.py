from infrastructure_layer import infrastructure
from logic_layer import logicconfig

def buildSong(genre, year, performer, title):
    song = {"song_genre" : genre,
            "song_year" : year,
            "song_performer" : performer,
            "song_title" : title}

    return song


def postSong(song):
    answer = infrastructure.post(logicconfig.add_song_URL, song)
    return answer


def addSong(genre, year, performer, title):
    song = buildSong(genre, year, performer, title)
    answer = postSong(song)
    return answer


def songVote(URL, userName, password, playlistName, songTitle):
    data = {"user_name" : userName,
            "user_password" : password,
            "playlist_name" : playlistName,
            "song_title" : songTitle}

    answer = infrastructure.put(URL, data)
    return answer


def songUpvote(userName, password, playlistName, songTitle):
    answer = songVote(logicconfig.upvote_URL, userName, password, playlistName, songTitle)
    return answer


def songDownvote(userName, password, playlistName, songTitle):
    answer = songVote(logicconfig.downvote_URL, userName, password, playlistName, songTitle)
    return answer


def getSongByRank(rank, op):
    data = {"rank" : rank,
            "op" : op}

    answer = infrastructure.get(logicconfig.ranked_songs_URL, data)
    return answer


def getSong(songTitle):
    data = {"song_title" : songTitle}
    answer = infrastructure.get(logicconfig.get_song_URL, data)

    return answer

def assertGetByRank(answer, song, shouldAppear):
    if "error" in answer.json().keys(): return False
    if shouldAppear and song not in answer.json()["data"]:
        answer.json()["error"] = "song not appear"
        return False
    if (not shouldAppear) and song in answer.json()["data"]:
        answer.json()["error"] = "song appear while shouldn't"
        return False
    return True


defaultSong = {"song_genre" : "A",
                "song_year" : "1",
                "song_performer" : "B",
                "song_title" : "C"}