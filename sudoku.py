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

def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - - ")
        
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end = "")

            if c == 8:
                print(board[r][c])
            else:
                print(str(board[r][c]) + " ", end="")