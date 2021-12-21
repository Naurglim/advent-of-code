import collections

DATA = 'datasets/5.txt'


def get_dataset(dt):
    f = open(dt, "r")
    lines = [x.split(' -> ') for x in [x.strip() for x in f]]
    return lines


def puzzle1(ds):
    coord_set = []
    for i in range(len(ds)):
        start = ds[i][0].split(',')
        end = ds[i][1].split(',')
        min_x = min(int(start[0]), int(end[0]))
        max_x = max(int(start[0]), int(end[0]))
        min_y = min(int(start[1]), int(end[1]))
        max_y = max(int(start[1]), int(end[1]))
        if min_x == max_x or min_y == max_y:
            for j in range(min_x, max_x + 1):
                for z in range(min_y, max_y + 1):
                    coord_set.append(str(j) + ',' + str(z))
    
    return len([item for item, count in collections.Counter(coord_set).items() if count > 1])


def get_valid_lines(start, end):
    return start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1])


def puzzle2(ds):
    coord_set = []
    for i in range(len(ds)):
        start = [int(x) for x in ds[i][0].split(',')]
        end = [int(x) for x in ds[i][1].split(',')] 

        if get_valid_lines(start, end):
            tope = max(abs(start[0]-end[0]), abs(start[1]-end[1]))
            for i in range(0, tope + 1):
                x = start[0]
                y = start[1]

                if start[0] < end[0]:
                    x += i
                elif start[0] > end[0]:
                    x -= i

                if start[1] < end[1]:
                    y += i
                elif start[1] > end[1]:
                    y -= i

                coord_set.append(str(x) + ',' + str(y))
    
    return len([item for item, count in collections.Counter(coord_set).items() if count > 1])


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    