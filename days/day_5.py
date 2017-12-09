def calculate_escape_steps(arr: list):
    index = 0
    step = 0
    while index < len(arr) and index >=0:
        index_val = arr[index]
        arr[index] += 1
        index += index_val
        step += 1
    return step


def calculate_escape_steps_v2(arr: list):
    index = 0
    step = 0
    while index < len(arr) and index >=0:
        index_val = arr[index]
        if index_val >= 3:
            arr[index] -= 1
        else:
            arr[index] += 1
        index += index_val
        step += 1
    return step
