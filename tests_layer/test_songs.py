from logic_layer import songs

def test_add_song(resetData):
    answer = songs.addSong("A", "1", "B", "C")
    assert answer.status_code == 200, f"fail to add song. status: {answer.status_code}"
    assert "error" not in answer.json().keys(), f"fail to add song. status: {answer.status_code}"


