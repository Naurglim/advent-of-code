DATA = 'datasets/6.txt'


def get_dataset(filename):
    txt_file = open(filename, "r")
    return [x.strip() for x in txt_file.readlines()]


def puzzle1(ds):
    initial_fish = ds[0].split(',')
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        fish[i] = initial_fish.count(str(i))

    fish_progression = {0: fish}
    for i in range(1, 81):
        new_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(8, -1, -1):
            if j == 0:
                new_fish[8] += fish_progression[i-1][0]
                new_fish[6] += fish_progression[i-1][0]
            else:
                new_fish[j-1] += fish_progression[i-1][j]
        fish_progression[i] = new_fish
    return str(sum(fish_progression[80]))


def puzzle2(ds):
    initial_fish = ds[0].split(',')
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        fish[i] = initial_fish.count(str(i))

    fish_progression = {0: fish}
    for i in range(1, 257):
        new_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(8, -1, -1):
            if j == 0:
                new_fish[8] += fish_progression[i - 1][0]
                new_fish[6] += fish_progression[i - 1][0]
            else:
                new_fish[j - 1] += fish_progression[i - 1][j]
        fish_progression[i] = new_fish
    return str(sum(fish_progression[256]))


if __name__ == '__main__':
    d_set = get_dataset(DATA)
    print('Answer 1: ' + puzzle1(d_set))
    print('Answer 2: ' + puzzle2(d_set))
