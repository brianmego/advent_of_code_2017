
import pytest
from ..days import day_3

test_spiral_inputs = [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
    (325489, 552),
]

test_spiral_adj_inputs = [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 5),
    (61, 312453),
    (62, 330785),
]

@pytest.mark.parametrize("test_input,expected", test_spiral_inputs)
def test_spiral(test_input, expected):
    actual = day_3.spiral(test_input)
    assert actual == expected

@pytest.mark.parametrize("test_input,expected", test_spiral_adj_inputs)
def test_spiral_adj(test_input, expected):
    actual = day_3.spiral_adj(test_input)
    assert actual == expected
