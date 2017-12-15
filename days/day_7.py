def get_tower_shape(tower: dict):
    balanced = []
    bases = []
    for line in tower:
        bases.append(line[:line.find('(') - 1])
        if '->' in line:
            split_line = line.split('->')[1]
            balanced.extend(split_line.strip().split(', '))
    for base in bases:
        if base not in balanced:
            return base

