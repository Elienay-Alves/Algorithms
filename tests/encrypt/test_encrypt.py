import pytest
from challenges.challenge_encrypt_message import encrypt_message


KEY_ERROR_MSG = "tipo inválido para key"
MSG_ERROR_MSG = "tipo inválido para message"


def test_encrypt_message():
    assert encrypt_message(message="abcd", key=3) == "cba_d"
    assert encrypt_message(message="abcd", key=2) == "dc_ba"
    assert encrypt_message(message="abcd", key=5) == "dcba"
    assert encrypt_message("dcba", 5) != "dcba"

    with pytest.raises(TypeError, match=KEY_ERROR_MSG):
        encrypt_message("abcc", "abcd")

    with pytest.raises(TypeError, match=MSG_ERROR_MSG):
        encrypt_message(2, 2)
