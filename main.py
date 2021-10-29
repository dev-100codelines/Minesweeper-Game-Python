from random import randrange

BOARD = []
IS_GAME_OVER = False
MINE_COUNT = -1


def print_board(show_mines):
    for i in range(MINE_COUNT):
        for _ in range(MINE_COUNT):
            print('+---', end='')
        print('+')
        for j in range(MINE_COUNT):
            if not show_mines:
                if BOARD[i][j] == 'X':
                    print('!   ', end='')
                    continue
            print('| ' + BOARD[i][j] + ' ', end='')
        print('|')
    for _ in range(MINE_COUNT):
        print('+---', end='')
    print('+')


def generate_board():
    global MINE_COUNT
    while MINE_COUNT < 10:
        try:
            MINE_COUNT = int(input('Enter number of mines you want? (minimum is 10) : '))
        except ValueError:
            print('Please enter a number')
    print('\n')
    global BOARD
    BOARD = [[' ' for _ in range(MINE_COUNT)] for _ in range(MINE_COUNT)]
    for _ in range(MINE_COUNT):
        BOARD[randrange(MINE_COUNT)][randrange(MINE_COUNT)] = 'X'


def game():
    generate_board()
    global IS_GAME_OVER
    while not IS_GAME_OVER:
        print('Please enter row and column')
        row = -1
        while row < 0 or row > MINE_COUNT - 1:
            try:
                print('Please enter value between 0-9')
                row = int(input('\tRow: '))
            except ValueError:
                print('Please enter a number')
        column = -1
        while column < 0 or column > MINE_COUNT - 1:
            try:
                print('Please enter value between 0-9')
                column = int(input('\tColumn: '))
            except ValueError:
                print('Please enter a number')
        if BOARD[row][column] == 'X':
            print_board(True)
            IS_GAME_OVER = True
            print('\033[93mGame Over\033[93m')
            print('\033[91mYou Lose..!\033[91m')
        else:
            if BOARD[row][column] == ' ':
                BOARD[row][column] = 'C'
                is_win = True
                for i in range(MINE_COUNT):
                    for j in range(MINE_COUNT):
                        if BOARD[i][j] == ' ':
                            is_win = False
                if is_win:
                    print_board(True)
                    IS_GAME_OVER = True
                    print('\033[93mGame Over\033[93m')
                    print('\033[94mYou Win..!\033[94m')
                else:
                    mines = 0
                    for i in range(max(row - 1, 0), min(row + 1, MINE_COUNT - 1) + 1):
                        for j in range(max(column - 1, 0), min(column + 1, MINE_COUNT - 1) + 1):
                            if BOARD[i][j] == 'X':
                                mines += 1
                    BOARD[row][column] = str(mines)
                    print_board(False)
            else:
                print('\033[93mYou already clicked that box\033[93m')


game()
