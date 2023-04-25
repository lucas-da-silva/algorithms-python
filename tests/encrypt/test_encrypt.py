from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    odd_num = 3
    even_num = 2
    non_existent_id = 10
    message = "hello"
    encrypted_odd_message = "leh_ol"
    encrypted_even_message = "oll_eh"
    reverse_message = "olleh"

    assert encrypt_message(message, odd_num) == encrypted_odd_message
    assert encrypt_message(message, even_num) == encrypted_even_message
    assert encrypt_message(message, non_existent_id) == reverse_message

    with pytest.raises(TypeError):
        encrypt_message(non_existent_id, message)
