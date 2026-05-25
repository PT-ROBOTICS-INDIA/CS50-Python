from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("hello!") == "hll!"
