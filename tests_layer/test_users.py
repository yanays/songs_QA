from logic_layer import users
from logic_layer import admin
import pytest

def test_add_user(resetUsers):
    answer = users.postUser(users.defaultUser)
    assert admin.checkAnswer(answer), f"fail to add first user. status: {answer.status_code}\nerror: {answer.json()['error']}"
    answer = users.addUser("yanay", "777")
    assert 'error' in answer.json().keys(), f"ERROR: added twice the same user."
    answer = users.addUser("zeev", "123")
    assert admin.checkAnswer(answer), f"fail to add another user. status: {answer.status_code}\nerror: {answer.json()['error']}"


def test_get_user(oneUser):
    answer = users.getUser("yanay")
    assert admin.checkAnswer(answer), f"fail to get user. status: {answer.status_code}\nerror: {answer.json()['error']}"
    data = answer.json()["data"]
    assert "friends" in data.keys(), "missing data: friends"
    assert "playlists" in data.keys(), "missing data: playlists"
    assert "user_name" in data.keys(), "missing data: user_name"
    assert data["user_name"] == "yanay", f"wrong data: user_name = {data['user_name']} while is should be 'yanay'."


@pytest.mark.xfail(reason = "bug: it is possible to add friend that doesn't exist")
def test_add_friend(oneUser):
    answer = users.addFriend("yanay", "123", "zeev")
    assert "error" in answer.json().keys(), "ERROR: add friend that doesn't exist"

    users.addUser("zeev", "777")
    answer = users.addFriend("yanay", "123", "zeev")
    assert admin.checkAnswer(answer), f"fail to add friend. status: {answer.status_code}\nerror: {answer.json()['error']}"

    answer = users.getUser("yanay")
    assert answer.json()["data"]["friends"] == ["zeev"], "friend not in friends list"

    answer = users.addFriend("yanay", "777", "zeev")
    assert "error" in answer.json().keys(), "ERROR: add friend with wrong password"


