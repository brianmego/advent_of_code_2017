import pytest
import os
from ..days import day_7

THIS_PATH = os.path.dirname(__file__)
with open(os.path.join(THIS_PATH, 'data', 'day_7_data.txt')) as handle:
    input_1 = handle.readlines()

with open(os.path.join(THIS_PATH, 'data', 'day_7_data_2.txt')) as handle:
    input_2 = handle.readlines()

test_inputs = [
    (input_1, 'tknk'),
    (input_2, 'veboyvy')
]

@pytest.mark.parametrize("test_input, expected", test_inputs)
def test_tower_shape(test_input, expected):
    actual = day_7.get_tower_shape(test_input)
    assert actual == expected
