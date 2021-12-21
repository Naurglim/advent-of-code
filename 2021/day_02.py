DATA = 'datasets/2.txt'


def get_dataset(filename):
    txt_file = open(filename, "r")
    return [x.strip() for x in txt_file.readlines()]


def puzzle1(ds):
    coord = [0, 0]  # forward, depth
    for move in ds:
        if 'forward' in move:
            coord[0] += int(move.split()[1])
        elif 'down' in move:
            coord[1] += int(move.split()[1])
        else:
            coord[1] -= int(move.split()[1])

    return str(coord[0] * coord[1])


def puzzle2(ds):
    coord = [0, 0, 0]  # forward, depth, aim
    for move in ds:
        if 'forward' in move:
            coord[0] += int(move.split()[1])
            coord[1] += int(move.split()[1]) * coord[2]
        elif 'down' in move:
            coord[2] += int(move.split()[1])
        else:
            coord[2] -= int(move.split()[1])

    return str(coord[0] * coord[1])


if __name__ == '__main__':
    d_set = get_dataset(DATA)
    print('Answer 1: ' + puzzle1(d_set))
    print('Answer 2: ' + puzzle2(d_set))
