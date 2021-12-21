DATA = 'datasets/11.txt'


def get_dataset(dt):
    f = open(dt, "r")
    return [list(map(int, list(x.strip()))) for x in f]


def adjacent_octopi(ds, y, x):
    vals = [(y-1, x), (y+1, x), (y, x-1), (y, x+1), (y-1, x-1), (y+1, x+1), (y-1, x+1), (y+1, x-1)]
    return [(y_i, x_i) for (y_i, x_i) in vals if 0 <= y_i < len(ds) and 0 <= x_i < len(ds[y])]


def run_step(ds):
    flashed = set()
    for y in range(len(ds)):
        for x in range(len(ds[y])):
            ds = flash(ds,[[y, x]])
    
    clear = False
    while not clear:
        clear = True
        for y in range(len(ds)):
            for x in range(len(ds[y])):
                if ds[y][x] > 9 and (y, x) not in flashed:
                    clear = False
                    flashed.add((y, x))
                    ds = flash(ds,adjacent_octopi(ds,y,x))
    
    # Clean-up flashed:
    flashes = len(flashed)
    for [y, x] in flashed:
        ds[y][x] = 0

    return [ds, flashes]


def flash(ds, neighbours):
    for [y, x] in neighbours:
        ds[y][x] += 1
    return ds


def puzzle1(ds):
    running_total = 0

    for i in range(100):
        ds, flashes = run_step(ds)
        running_total += flashes

    return running_total


def puzzle2(ds):
    running_total = 0

    while True:
        running_total += 1
        ds, flashes = run_step(ds)
        if flashes == 100:
            print(ds)
            break
        if running_total > 1000:
            break

    return running_total


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    