from infrastructure_layer import infrastructure

add_user_URL = "https://github.com/theadamzaft/song-server-swagger/users/add_user"
get_user_URL = "https://github.com/theadamzaft/song-server-swagger/users/get_user"
add_friend_URL = "https://github.com/theadamzaft/song-server-swagger/users/add_friend"
change_password_URL ="https://github.com/theadamzaft/song-server-swagger/users/change_password"

def buildUser(name, password):
    user = {"user_name" : name,
            "user_password" : password}

    return user


def postUser(user):
    answer = infrastructure.post(add_user_URL, user)
    return answer


def addUser(name, password):
    user = buildUser(name, password)
    answer = postUser(user)
    return answer


def getUser(name):
    data = {"user_name" : name}
    answer = infrastructure.get(get_user_URL, data)
    return answer


def addFriend(userName, password, friendName):
    data = {"user_name" : userName,
            "user_password" : password,
            "friend_name" : friendName}

    answer = infrastructure.get(add_friend_URL, data)

    return answer


def changePassword(userName, userPassword, userNewPassword):
    data = {"user_name" : userName,
            "user_password" : userPassword,
            "user_new_password" : userNewPassword}

    answer = infrastructure.put(change_password_URL, data)

    return answer