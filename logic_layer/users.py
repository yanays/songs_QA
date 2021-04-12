from infrastructure_layer import infrastructure
from logic_layer import logicconfig

def buildUser(name, password):
    user = {"user_name" : name,
            "user_password" : password}

    return user


def postUser(user):
    answer = infrastructure.post(logicconfig.add_user_URL, user)
    return answer


def addUser(name, password):
    user = buildUser(name, password)
    answer = postUser(user)
    return answer


def getUser(name):
    data = {"user_name" : name}
    answer = infrastructure.get(logicconfig.get_user_URL, data)
    return answer


def addFriend(userName, password, friendName):
    data = {"user_name" : userName,
            "user_password" : password,
            "friend_name" : friendName}

    answer = infrastructure.put(logicconfig.add_friend_URL, data)

    return answer


def changePassword(userName, userPassword, userNewPassword):
    data = {"user_name" : userName,
            "user_password" : userPassword,
            "user_new_password" : userNewPassword}

    answer = infrastructure.put(logicconfig.change_password_URL, data)

    return answer


defaultUser = {"user_name" : "yanay",
               "user_password" : "123"}

