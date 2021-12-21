from collections import Counter

DATA = 'datasets/3.txt'


def get_dataset(filename):
    txt_file = open(filename, "r")
    return [x.strip() for x in txt_file.readlines()]


def get_rating(r_ds, mode='o2'):
    if mode == 'o2':
        default_value = '1'
        direction = 0
    else:
        default_value = '0'
        direction = -1

    for i in range(len(r_ds[0])):
        q = len(r_ds)

        tally = Counter([s[i] for s in r_ds]).most_common()[direction]
        if tally[1] == q / 2:
            base = default_value
        else:
            base = tally[0]

        r_ds = [s for s in r_ds if base == s[i]]
        if len(r_ds) == 1:
            return r_ds[0]
    return ''


def puzzle1(ds):
    q = len(ds)

    value_length = len(ds[0])
    zeroes = [0 for x in range(value_length)]
    for value in ds:
        for i in range(value_length):
            if value[i] == '0':
                zeroes[i] += 1

    gamma = ''.join(['0' if i > q/2 else '1' for i in zeroes])
    epsilon = ''.join(['0' if i < q/2 else '1' for i in zeroes])

    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    res = gamma_dec * epsilon_dec

    return res


def puzzle2(ds):
    o2_dec = int(get_rating(ds, 'o2'), 2)
    co2_dec = int(get_rating(ds, 'co2'), 2)
    res = o2_dec * co2_dec
    return res


if __name__ == '__main__':
    d_set = get_dataset(DATA)
    print('Answer 1: ' + str(puzzle1(d_set)))
    print('Answer 2: ' + str(puzzle2(d_set)))
