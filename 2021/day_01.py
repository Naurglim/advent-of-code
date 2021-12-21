DATA = 'datasets/1.txt'


def get_dataset(filename):
    txt_file = open(filename, "r")
    return [int(x) for x in txt_file.readlines()]


def puzzle1(df):
    ds = get_dataset(df)
    inc = 0

    for i in range(1, len(ds)):
        if ds[i] > ds[i-1]:
            inc += 1

    return str(inc)


def puzzle2(df):
    ds = get_dataset(df)
    inc = 0

    for i in range(3, len(ds)):
        if ds[i] > ds[i - 3]:
            inc += 1

    return str(inc)


if __name__ == '__main__':
    res = puzzle1(DATA)
    print('Answer 1: ' + res)

    res = puzzle2(DATA)
    print('Answer 2: ' + res)
