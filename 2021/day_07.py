DATA = 'datasets/7.txt'


def get_dataset(dt):
    f = open(dt, "r")
    row = [x.strip().split(',') for x in f][0]
    dat = [int(x) for x in row]
    return dat


def puzzle1(ds):
    min_value = min(ds)
    max_value = max(ds)
    fuel_costs = {}

    for i in range(min_value, max_value+1):
        fuel_costs[i] = 0
        for value in ds:
            fuel_costs[i] += abs(i - value)

    return fuel_costs[min(fuel_costs, key=fuel_costs.get)]


def puzzle2(ds):
    min_value = min(ds)
    max_value = max(ds)
    fuel_costs = {}

    for i in range(min_value, max_value+1):
        fuel_costs[i] = 0
        for value in ds:
            fuel_costs[i] += sum(range(abs(i - value) + 1))

    return fuel_costs[min(fuel_costs, key=fuel_costs.get)]


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    