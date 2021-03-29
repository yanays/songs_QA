from infrastructure_layer import infrastructure

add_user_URL = "https://github.com/theadamzaft/song-server-swagger/users/add_user"
get_user_URL = "https://github.com/theadamzaft/song-server-swagger/users/get_user"


def buildUser(name, password):
    user = {"user_name" : name,
            "user_password" : password}

    return user


def postUser(user):
    answer = infrastructure.post(add_user_URL, user)
    return answer


def addSong(name, password):
    user = buildUser(name, password)
    answer = postUser(user)
    return answer


def getUser(name):
    data = {"user_name" : name}
    answer = infrastructure.get(get_user_URL, data)
    return answer