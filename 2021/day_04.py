import copy

DATA = 'datasets/4.txt'


def get_dataset(filename):
    txt_file = open(filename, "r")
    return [x.strip() for x in txt_file.readlines()]


def get_numbers(ds):
    return ds[0].split(',')


def get_boards(ds):
    j = 0
    boards = {}
    board = []
    for i in range(2, len(ds)):
        if ds[i] == '':
            boards[j] = board
            board = []
            j += 1
            continue
        board.append([x for x in ds[i].split(' ') if x != ''])

    return boards


def check_win(board, numbers):

    for line in board:
        check = all(item in numbers for item in line)
        if check:
            return True
    return False


def get_winning_combinations(board):
    wc = copy.deepcopy(board)
    for j in range(5):
        new_line = []
        for i in range(5):
            new_line.append(board[i][j])
        wc.append(new_line)
    return wc


def get_win(board, numbers):
    winning_combinations = get_winning_combinations(board)
    for i in range(5, len(numbers)):
        current_stack = numbers[:i]
        if check_win(winning_combinations, current_stack):
            return i


def get_winning_board(boards, numbers):
    wins = {}
    for board in boards.items():
        wins[board[0]] = get_win(board[1], numbers)
    earlier_win = wins[0]
    winner = 0
    for i in wins.items():
        if i[1] < earlier_win:
            winner = i[0]
            earlier_win = i[1]
    return winner, earlier_win


def get_loser_board(boards, numbers):
    earlier_wins = {}
    for board in boards.items():
        earlier_wins[board[0]] = get_win(board[1], numbers)
    latest_win = earlier_wins[0]
    winner = 0
    for i in earlier_wins.items():
        if i[1] > latest_win:
            winner = i[0]
            latest_win = i[1]
    return winner, latest_win


def get_score(board, numbers):
    winning_number = int(numbers[-1])
    score = 0
    for line in board:
        score += sum([int(x) for x in line if x not in numbers])
    return str(score * winning_number)


def puzzle1(ds):
    res = ''
    numbers = get_numbers(ds)
    boards = get_boards(ds)

    winner, winning_number = get_winning_board(boards, numbers)
    res = get_score(boards[winner], numbers[:winning_number])

    return res


def puzzle2(ds):
    res = ''
    numbers = get_numbers(ds)
    boards = get_boards(ds)

    winner, winning_number = get_loser_board(boards, numbers)
    res = get_score(boards[winner], numbers[:winning_number])

    return res


if __name__ == '__main__':
    d_set = get_dataset(DATA)
    print('Answer 1: ' + puzzle1(d_set))
    print('Answer 2: ' + puzzle2(d_set))
