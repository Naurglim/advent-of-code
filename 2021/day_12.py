DATA = 'datasets/12.txt'


def get_dataset(dt):
    f = open(dt, "r")
    return [x.strip() for x in f]


def puzzle1(ds):
    running_total = 0
    print(ds)
    return running_total


def puzzle2(ds):
    running_total = 0
    return running_total


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    