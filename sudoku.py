import time

example_board = [
    [7,8,0,0,5,0,0,0,3],
    [0,0,0,2,0,0,1,0,0],
    [0,9,1,0,0,0,6,0,5],
    [1,6,0,3,0,2,0,0,0],
    [0,0,0,0,1,7,3,0,0],
    [0,0,7,0,0,0,0,0,8],
    [0,1,3,8,2,5,4,7,0],
    [8,4,6,0,9,1,5,3,0],
    [0,0,0,6,0,0,8,9,0]
]


def solve(board):
    if not find_empty(board):
        return True
    else:
        row, col = find_empty(board)

    for guess in range(1, 10):
        if valid(board, guess, row, col):
            board[row][col] = guess

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, row, col):
    # Check row
    for i in range(9):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    # Check box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != (row,col):
                return False

    return True


def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("——————————————————————— ")

        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")

            if c == 8:
                print(board[r][c])
            else:
                print(str(board[r][c]) + " ", end="")


def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c  # row, col

    return None

start = time.time()
solve(example_board)
end = time.time()
print_board(example_board)
print("Time taken to solve puzzle: ", (end-start))