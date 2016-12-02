import numpy as np
import matplotlib.pyplot as plt


def create_board():
    return np.zeros((3, 3))


def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    return board


def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))


def random_place(board, player):
    positions = possibilities(board)
    if (len(positions) > 0):
        index = np.random.randint(0, len(positions))
        position = positions[index]
        place(board, player, position)

# -------------------------------------------

def check_row(row, player):
    for marker in row:
        if marker != player:
            return False
    return True 


def row_win(board, player):
    for row in board:
        if check_row(row, player):
            return True
    return False


def col_win(board, player):
    for row in board.T:
        if check_row(row, player):
            return True
    return False


def diag_win(board, player):
    main_diag = board.diagonal()
    anti_diag = np.flipud(board).diagonal()[::-1]
    return check_row(main_diag, player) or check_row(anti_diag, player)
    
# -----------------------------------------------


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player) or diag_win(board, player) or col_win(board, player):
            return player
    if np.all(board != 0):
        winner = -1
    return winner


def play_game():
    board = create_board()
    while True:
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result


ITERATIONS = 1000
result = []
for i in range(ITERATIONS):
    result.append(play_game())

print(result[:100])

plt.hist(result)







