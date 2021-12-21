DATA = 'datasets/8.txt'


def get_dataset(dt):
    f = open(dt, "r")
    
    return [x.strip() for x in f]


def puzzle1(ds):
    lines = [x.split('|')[1].strip() for x in ds]
    segments = []
    for line in lines:
        segments.extend([x for x in line.split() if len(x) in [2,3,4,7]])
    return len(segments)


def puzzle2(ds):
    running_total = 0

    for line in ds:
        segments = line.split('|')  # output: segments[1]
        blocks = segments[0].split()
        output = segments[1].strip().split()
        numbers = {}
        numbers[1] = [x for x in blocks if len(x) == 2]
        numbers[4] = [x for x in blocks if len(x) == 4]
        numbers[7] = [x for x in blocks if len(x) == 3]
        numbers[8] = [x for x in blocks if len(x) == 7]
        numbers[9] = [x for x in blocks if len(x) == 6 and (0 not in [c in x for c in [y for y in numbers[4][0]]])]
        numbers[0] = [x for x in blocks if len(x) == 6 and (0 not in [c in x for c in [y for y in numbers[7][0]]]) and (x != numbers[9][0])]
        numbers[6] = [x for x in blocks if len(x) == 6 and (x not in [numbers[9][0], numbers[0][0]])]
        numbers[3] = [x for x in blocks if len(x) == 5 and (0 not in [c in x for c in [y for y in numbers[1][0]]])]
        numbers[5] = [x for x in blocks if len(x) == 5 and (x != numbers[3][0]) and (0 not in [c in numbers[9][0] for c in [y for y in x]])]
        numbers[2] = [x for x in blocks if len(x) == 5 and (x not in [numbers[3][0], numbers[5][0]])]

        digits = ''
        for code in output:
            for i in range(0,10):
                if set(code) == set(numbers[i][0]):
                    digits += str(i)
        running_total += int(digits)
   
    return running_total


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    