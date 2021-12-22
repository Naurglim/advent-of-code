from collections import defaultdict, Counter

DATA = 'datasets/13.txt'


def get_dataset(dt):
    f = open(dt, "r")
    return [x.strip() for x in f]


def puzzle1(ds):
    running_total = 0
    instructions = ds[ds.index('')+1:ds.index('')+2]
    dots = [list(map(int, item)) for item in [coordinates.split(',') for coordinates in ds[:ds.index('')]]]

    for fold in instructions:
        a, line = fold.split('=',2)
        axis = 0 if a.split()[2] == 'x' else 1
        
        for i in range(len(dots)):
            if dots[i][axis] > int(line):
                dots[i][axis] = int(line) - (dots[i][axis] - int(line))

    unique_dots = set(tuple(i) for i in dots)
    running_total = len(unique_dots)

    return running_total


def puzzle2(ds):
    running_total = 0
    
    return running_total


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    