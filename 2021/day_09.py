from collections import deque
import functools

DATA = 'datasets/9.txt'


def get_dataset(dt):
    f = open(dt, "r")
    return [list(map(int, list(x.strip()))) for x in f]


def neighbour_points(input, y, x):
    vals = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    return [(y_i, x_i) for (y_i, x_i) in vals if 0 <= y_i < len(input) and 0 <= x_i < len(input[y])]


def get_low_points(ds):
    low_points = []
    for y in range(len(ds)):
        for x in range(len(ds[y])):
            adjacent = [ds[y][x] for (y,x) in neighbour_points(ds, y, x)]
            if ds[y][x] < min(adjacent):
                low_points.append([y,x])

    return low_points


def get_basin(input, x, y):
    basin = []
    visited = set()
    queue = deque([(x,y)])
    
    while queue:
        (x_i, y_i) = queue.pop()

        if (x_i, y_i) in visited:
            continue
        else:
            visited.add((x_i, y_i))
            if input[x_i][y_i] != 9:
                basin.append((x_i, y_i))
                queue.extend([(x_j, y_j) for (x_j, y_j) in neighbour_points(input, x_i, y_i) if (x_j, y_j) not in visited])

    return basin


def puzzle1(ds):
    running_total = 0
    low_points = get_low_points(ds)

    for [y,x] in low_points:
        running_total += 1 + ds[y][x]

    return running_total


def puzzle2(ds):
    running_total = 0
    low_points = get_low_points(ds)

    basins = [get_basin(ds, x, y) for (x, y) in low_points]
    running_total = functools.reduce(lambda a,b: a*b, sorted([len(basin) for basin in basins], reverse=True)[0:3])
    
    return running_total


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    