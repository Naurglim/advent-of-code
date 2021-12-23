from collections import Counter

DATA = 'datasets/14.txt'


def get_dataset(dt):
    f = open(dt, "r")
    return [x.strip() for x in f]


def sustitution(polymer, instructions):
    new_polymer = ''

    for i in range(len(polymer)-1):
        segment = polymer[i:i+2]
        new_polymer += polymer[i]
        if segment in instructions.keys():
            new_polymer += instructions[segment]
    new_polymer += polymer[-1]
    return new_polymer


def puzzle_text(ds, steps=10):
    running_total = 0
    
    polymer = ds[0]
    instructions = {} # [x.split(' -> ') for x in ds[2:]]
    for rule in ds[2:]:
        x, y = rule.split(' -> ',2) 
        instructions[x] = y

    steps = 10
    for i in range(steps):
        polymer = sustitution(polymer,instructions)
    letters = Counter(polymer)
    running_total = letters.most_common()[0][1] - letters.most_common()[-1][1]
    
    return running_total


def sustitution2(pairs, instructions):
    new_pairs = Counter()
    for pair in pairs:
        new_pairs[pair[0] + instructions[pair]] += pairs[pair]
        new_pairs[instructions[pair] + pair[1]] += pairs[pair]

    return new_pairs


def puzzle_totals(ds, steps=10):
    running_total = 0
    
    polymer = ds[0]
    pairs = Counter()
    for i in range(len(polymer) - 1):
        pairs[polymer[i] + polymer[i + 1]] += 1

    instructions = {}
    for rule in ds[2:]:
        x, y = rule.split(' -> ',2) 
        instructions[x] = y

    for i in range(steps):
        pairs = sustitution2(pairs,instructions)

    letters = Counter()
    for pair in pairs:
        letters[pair[0]] += pairs[pair]
    letters[polymer[-1]] += 1
    running_total = max(letters.values()) - min(letters.values())
    
    return running_total


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle_text(d_set,10)))
    print("Answer 2: " + str(puzzle_totals(d_set,40)))
    