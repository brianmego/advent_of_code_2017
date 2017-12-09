import pytest
from ..days import day_6

test_inputs = [
    ([0, 2, 7, 0], 5),
    # ([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3], 6681),
]
test_inputs_two = [
    ([0, 2, 7, 0], 4),
    # ([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3], 2392),
]


@pytest.mark.parametrize("test_input, expected", test_inputs)
def test_infinite_loop(test_input, expected):
    actual = day_6.find_infinite_loop(test_input)
    assert actual == expected

@pytest.mark.parametrize("test_input, expected", test_inputs_two)
def test_infinite_loop_size(test_input, expected):
    actual = day_6.find_infinite_loop_size(test_input)
    assert actual == expected
