from infrastructure_layer import infrastructure
delete_all_users_URL = "http://127.0.0.1:3002/admin/delete_all_users"
delete_all_songs_URL = "http://127.0.0.1:3002/admin/delete_all_songs"
set_songs_URL = "http://127.0.0.1:3002/admin/set_songs"
set_users_URL = "http://127.0.0.1:3002/admin/set_songs"


def deleteAllUsers():
    return infrastructure.delete(delete_all_users_URL)


def deleteAllSomgs():
    return infrastructure.delete(delete_all_songs_URL)


def setSongsIntoTheDB(songsList):
    data = {"List of songs objects" : songsList}
    return infrastructure.post(set_songs_URL, data)


def setUsersIntoTheDB(userObject):
    data = {"Object of user objects" : userObject}
    return infrastructure.post(set_users_URL, data)


def checkAnswer(answer):
    if not answer.status_code == 200: return False
    if "error" in answer.json().keys(): return False
    return True
