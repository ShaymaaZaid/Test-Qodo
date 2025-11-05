# test_sample.py
# Unit tests for test_file.py using pytest.

from test_file import add_numbers, greet

def test_add_numbers():
    assert add_numbers(3, 4) == 7
    assert add_numbers(-2, 5) == 3

def test_greet():
    assert greet("Issra") == "Hello, Issra! Welcome to the project."
