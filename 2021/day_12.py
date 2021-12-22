from collections import defaultdict, Counter

DATA = 'datasets/12.txt'
START = 'start'
END = 'end'


def mapping(ds):
    nodes = defaultdict(list)

    for line in ds:
        link = line.strip().split('-')
        for c1, c2 in zip(link, reversed(link)):
            if c2 != START:  # We can't return to start point.
                nodes[c1].append(c2)
    del nodes[END]  # We can't move back from the end point. 

    return nodes


def get_dataset(dt):
    f = open(dt, "r")
    return mapping([x.strip() for x in f])


def puzzle1(chart, route=[START]):
    running_total = 0
    for cave in chart[route[-1]]:
        if cave.isupper() or not cave in route:
            running_total += 1 if cave == END else puzzle1(chart, route + [cave])
    return running_total


def small_cave_revisited(route):
    # Create a dictionary of elements & their frequency count
    caves = dict(Counter(route))
    caves = { key:value for key, value in caves.items() if value > 1}
    
    for key in caves.keys():
        if key.islower():
            return True

    return False


def puzzle2(chart, route=[START]):
    running_total = 0
    for cave in chart[route[-1]]:

        if cave.isupper() or (not cave in route) or (not small_cave_revisited(route) and cave != START):
            running_total += 1 if cave == END else puzzle2(chart, route + [cave])
    return running_total


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    