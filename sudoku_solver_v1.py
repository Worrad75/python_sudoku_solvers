import sys

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):                           # takes in a board
    for i in range(len(board)):                     # len(board) reflects the height of the board
        if i % 3 == 0 and i != 0:                   # prints a break line after every 3 rows
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):              # len(board[0]) reflects the width of the board
            if j % 3 == 0 and j != 0:               # prints a break line after every 3 columns
                print(" | ", end="")
            
            digitToPrint = board[i][j] if board[i][j] != 0 else " "   # we will print 0's as spaces
            if j == 8:
                print(digitToPrint)                  # if its the last num in the row, print (with a "\n")
            else:
                print(str(digitToPrint) + " ", end="")   # otherwise, print without a new line


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return null


# print(find_empty(board))
print_board(board)