import os
import pytest
from ..days import day_4

THIS_PATH = os.path.dirname(__file__)
test_passphrase_inputs = [
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True),
]

test_anagram_inputs = [
    ('abcde fghij', True),
    ('abcde xyz ecdab', False),
    ('a ab abc abd abf abj', True),
    ('iiii oiii ooii oooi oooo', True),
    ('oiii ioii iioi iiio', False)
]


@pytest.mark.parametrize("test_input, expected", test_passphrase_inputs)
def test_passphrase(test_input, expected):
    actual = day_4.validate_passphrase(test_input)
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", test_anagram_inputs)
def test_passphrase(test_input, expected):
    actual = day_4.validate_passphrase(test_input, allow_anagrams=False)
    assert actual == expected


def test_db_passphrases():
    valid_passphrase_count = 0
    invalid_passphrase_count = 0
    with open(os.path.join(THIS_PATH, 'data', 'day_4_data.txt')) as handle:
        lines = handle.readlines()
    for line in lines:
        if day_4.validate_passphrase(line):
            valid_passphrase_count += 1
        else:
            invalid_passphrase_count += 1
    assert valid_passphrase_count == 386
    assert invalid_passphrase_count == 126


def test_db_anagrams():
    valid_passphrase_count = 0
    invalid_passphrase_count = 0
    with open(os.path.join(THIS_PATH, 'data', 'day_4_data.txt')) as handle:
        lines = handle.readlines()
    for line in lines:
        if day_4.validate_passphrase(line, allow_anagrams=False):
            valid_passphrase_count += 1
        else:
            invalid_passphrase_count += 1
    assert valid_passphrase_count == 208
    assert invalid_passphrase_count == 304
