DATA = 'datasets/10.txt'

OPEN = ['(','[','{','<']
CLOSE = [')',']','}','>']
VALUES = [3,57,1197,25137]


def get_dataset(dt):
    f = open(dt, "r")
    
    return [x.strip() for x in f]


def puzzle1(ds):
    running_total = 0
    for line in ds:
        opens = []
        for c in line:
            if c in OPEN:
                opens.append(c)
                continue
            ix = CLOSE.index(c)
            if opens.pop() != OPEN[ix]:
                running_total += VALUES[ix]
                break

    return running_total


def puzzle2(ds):
    line_values =[]
    for line in ds:
        running_total = 0
        opens = []
        for c in line:
            if c in OPEN:
                opens.append(c)
            else:
                if opens.pop() != OPEN[CLOSE.index(c)]:
                    opens.clear()
                    break
        
        while opens:
            running_total *= 5
            running_total += OPEN.index(opens.pop()) + 1

        if running_total > 0:
            line_values.append(running_total)

    line_values.sort()
    res = line_values[int(round((len(line_values)-1)/2))]
    
    return res


if __name__ == "__main__":
    d_set = get_dataset(DATA)
    print("Answer 1: " + str(puzzle1(d_set)))
    print("Answer 2: " + str(puzzle2(d_set)))
    