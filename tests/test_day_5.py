import os
import pytest
from ..days import day_5

THIS_PATH = os.path.dirname(__file__)

test_escape_steps = [
    ([0, 3, 0, 1, -3], 5),
]
test_escape_steps_v2 = [
    ([0, 3, 0, 1, -3], 10),
]

@pytest.mark.parametrize("test_input, expected", test_escape_steps)
def test_calculate_escape(test_input, expected):
    actual = day_5.calculate_escape_steps(test_input)
    assert actual == expected

@pytest.mark.parametrize("test_input, expected", test_escape_steps_v2)
def test_calculate_escape_steps_v2(test_input, expected):
    actual = day_5.calculate_escape_steps_v2(test_input)
    assert actual == expected

def test_file_escape_steps():
    input_jumps = []
    with open(os.path.join(THIS_PATH, 'day_5_data.txt')) as handle:
        for line in handle:
            input_jumps.append(int(line))
    actual = day_5.calculate_escape_steps(input_jumps)
    assert actual == 374269

# def test_file_escape_steps_v2():
#     input_jumps = []
#     with open(os.path.join(THIS_PATH, 'day_5_data.txt')) as handle:
#         for line in handle:
#             input_jumps.append(int(line))
#     actual = day_5.calculate_escape_steps_v2(input_jumps)
#     assert actual == 27720699

