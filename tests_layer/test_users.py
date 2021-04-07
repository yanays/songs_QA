from logic_layer import users

def test_add_user(resetUsers):
    answer = users.postUser(users.defaultUser)
    assert answer.status_code==200, f"fail to add first user. status: {answer.status_code}"
    assert "error" not in answer.json().keys(), f"fail to add first user. status: {answer.status_code}"
    answer = users.addUser("yanay", "777")
    assert 'error' in answer.json().keys(), f"ERROR: added twice the same name."
    answer = users.addUser("zeev", "123")
    assert answer.status_code == 200, f"fail to add another user. status: {answer.status_code}"
    assert "error" not in answer.json().keys(), f"fail to add another user. status: {answer.status_code}"


def test_get_user(oneUser):
    answer = users.getUser("yanay")
    assert answer.status_code == 200, f"fail to get user. status: {answer.status_code}"
    assert "error" not in answer.json().keys(), f"fail to get user. status: {answer.status_code}"
    data = answer.json()["data"]
    assert "friends" in data.keys(), "missing data: friends"
    assert "playlists" in data.keys(), "missing data: playlists"
    assert "user_name" in data.keys(), "missing data: user_name"
    assert data["user_name"] == "yanay", f"wrong data: user_name = {data['user_name']} while is should be 'yanay'."


def test_add_friend(oneUser):
    answer = users.addFriend("yanay", "123", "zeev")
    assert answer.status_code == 200, f"fail to add friend. status: {answer.status_code}"
    assert "error" not in answer.json().keys(), f"fail to add friend. status: {answer.status_code}"

    answer = users.getUser("yanay")
    assert answer.json()["data"]["friends"] == ["zeev"], "friend not in friends list"

    answer = users.addFriend("yanay", "777", "zeev")
    assert "error" in answer.json().keys(), "add friend with wrong password"


