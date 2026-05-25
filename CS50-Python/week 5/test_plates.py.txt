from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start():
    assert is_valid("1ABC") == False
    assert is_valid("AB123") == True

def test_numbers():
    assert is_valid("AB12C") == False
    assert is_valid("AB012") == False

def test_symbols():
    assert is_valid("AB@12") == False
