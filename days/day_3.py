# Maps of (direction, x_inc, y_inc)
DIRECTION_MAP = {
    'right': {
        'x_inc': 1,
        'y_inc': 0,
        'next_dir': 'up'
    },
    'up': {
        'x_inc': 0,
        'y_inc': 1,
        'next_dir': 'left'
    },
    'left': {
        'x_inc': -1,
        'y_inc': 0,
        'next_dir': 'down'
    },
    'down': {
        'x_inc': 0,
        'y_inc': -1,
        'next_dir': 'right'
    }
}

def spiral(target_square: int):
    square = 1
    speed = 1
    direction = 'right'
    x = y = 0
    inc_speed = False
    while square < target_square:
        map_val = DIRECTION_MAP[direction]
        counter = 0
        while counter < speed and square < target_square:
            x += map_val['x_inc']
            y += map_val['y_inc']
            counter += 1
            square += 1
        if inc_speed:
            speed += 1
            inc_speed = False
        else:
            inc_speed = True
        direction = map_val['next_dir']
    return abs(x) + abs(y)

def spiral_adj(target_square: int):
    spiral_data = {
        '0,0': 1
    }
    square = 1
    speed = 1
    direction = 'right'
    x = y = 0
    square_val = spiral_data['{},{}'.format(x, y)]
    inc_speed = False
    while square < target_square:
        map_val = DIRECTION_MAP[direction]
        counter = 0
        while counter < speed and square < target_square:
            x += map_val['x_inc']
            y += map_val['y_inc']
            counter += 1
            square += 1
            spiral_data['{},{}'.format(x, y)] = get_surrounding_squares(spiral_data, x, y)
        if inc_speed:
            speed += 1
            inc_speed = False
        else:
            inc_speed = True

        direction = map_val['next_dir']
    return spiral_data['{},{}'.format(x,y)]

def get_surrounding_squares(spiral_data, x, y):
    square_val = 0
    square_val += spiral_data.get('{},{}'.format(x - 1, y + 1), 0)
    square_val += spiral_data.get('{},{}'.format(x - 1, y), 0)
    square_val += spiral_data.get('{},{}'.format(x - 1, y - 1), 0)
    square_val += spiral_data.get('{},{}'.format(x, y - 1), 0)
    square_val += spiral_data.get('{},{}'.format(x + 1, y - 1), 0)
    square_val += spiral_data.get('{},{}'.format(x + 1, y), 0)
    square_val += spiral_data.get('{},{}'.format(x + 1, y + 1), 0)
    square_val += spiral_data.get('{},{}'.format(x, y + 1), 0)
    return square_val

