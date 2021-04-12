from infrastructure_layer import infrastructure
from logic_layer import logicconfig
import json

def deleteAllUsers():
    return infrastructure.delete(logicconfig.delete_all_users_URL)


def deleteAllSomgs():
    return infrastructure.delete(logicconfig.delete_all_songs_URL)


def setSongsIntoTheDB(songsList):
    data = {"List of songs objects" : songsList}
    return infrastructure.post(logicconfig.set_songs_URL, data)


def setUsersIntoTheDB(userObject):
    data = {"Object of user objects" : userObject}
    return infrastructure.post(logicconfig.set_users_URL, data)


def checkAnswer(answer):
    if not answer.status_code == 200: return False
    if "error" in answer.json().keys(): return False
    return True


def getDB(file = "users"):
    if file == "users":
        usersFile = open(logicconfig.users_path, "r")
    elif file == "songs":
        usersFile = open(logicconfig.songs_path, "r")

    if file == "users" or file == "songs":
        return json.load(usersFile)
    else:
        return None