def next_digit(input_str):
    input_str = str(input_str)
    total = 0
    for i in range(len(input_str)):
        compare_index = i + 1
        if compare_index >= len(input_str):
            compare_index -= len(input_str)
        if input_str[i] == input_str[compare_index]:
            total += int(input_str[i])
    return total

def halfway_digit(input_str):
    input_str = str(input_str)
    total = 0
    for i in range(len(input_str)):
        compare_index = i + int(len(input_str) / 2)
        if compare_index >= len(input_str):
            compare_index -= len(input_str)
        if input_str[i] == input_str[compare_index]:
            total += int(input_str[i])
    return total
