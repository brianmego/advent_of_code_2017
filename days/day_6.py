
def find_infinite_loop(input_arr: list):
    known_states = []
    cycles = 0
    arr_length = len(input_arr)
    while input_arr not in known_states:
        known_states.append(list(input_arr))
        max_index = 0
        max_index_val = 0
        for i in range(arr_length):
            if input_arr[i] > max_index_val:
                max_index = i
                max_index_val = input_arr[i]
        input_arr[max_index] = 0
        distribute_rate = round(max_index_val / arr_length)
        for i in range(1, arr_length + 1):
            update_index = (max_index + i) % arr_length
            amt_to_add = min(distribute_rate, max_index_val)
            input_arr[update_index] = input_arr[update_index] + amt_to_add
            max_index_val -= amt_to_add
        cycles += 1

    return cycles

def find_infinite_loop_size(input_arr: list):
    """
    Since the input_arr is mutable, calling find_infinite_loop
    the first time is going to set input_arr to the new start
    state. Handy! Probably wouldn't do this in a real world
    because side effects or whatever, but convenient for this
    exercise
    """
    find_infinite_loop(input_arr)
    return find_infinite_loop(input_arr)
