import math

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

# board = [
#     [1,0,0,2,0,0],
#     [0,0,0,1,6,3],
#     [6,0,0,0,0,0],
#     [5,0,0,0,3,0],
#     [0,1,0,0,0,4],
#     [0,0,2,3,0,0]
# ]

# 3, 3, 8 for original
box_height = 3
box_width = 3
total_width = 8

def print_board(board):                           # takes in a board
    for i in range(len(board)):                     # len(board) reflects the height of the board
        if i % box_height == 0 and i != 0:                   # prints a break line after every 3 rows
            print("\n- - - - - - - - - - - - - ")

        for j in range(len(board[0])):              # len(board[0]) reflects the width of the board
            if j % box_width == 0 and j != 0:               # prints a break line after every 3 columns
                print(" | ", end="")
            
            digitToPrint = board[i][j] if board[i][j] != 0 else " "   # we will print 0's as spaces
            if j == total_width:
                print(digitToPrint)                  # if its the last num in the row, print (with a "\n")
            else:
                print(str(digitToPrint) + " ", end="")   # otherwise, print without a new line


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(board, number, pos): # pos is a tuple of row, col
    #check row
    for ele in range(len(board[0])):                                # loop through the row
        if board[pos[0]][ele] == number and pos[1] != ele:   # for each element, if it is equal to the num we pulled in but it isnt the actual number that we inserted, then return false
            return False
    #check column
    for ele in range(len(board)):                                   # loop through the column
        if board[ele][pos[1]] == number and pos[0] != ele:   # for each element, if it is equal to the num we pulled in but it isnt the actual number that we inserted, then return false
            return False

    # check box
    box_x = math.floor(pos[0] / 3)
    box_y = math.floor(pos[1] / 3)

    for x in range(box_x*3, box_x*3 + 3):
        for y in range(box_y*3, box_y*3 + 3):
            if board[x][y] == number and pos != (x, y):
                return False

    return True


def solve(board):
    found = find_empty(board)                   # find the next empty square
    if not found:
        return True                             # if we dont have any empty squares, we did it!
    row, col = found                            # if we do, then deconstruct the object into row and column values
    
    for i in range(1,10):                       # count from 1-9
        if valid(board, i, (row,col)):          # for each num, check if it is valid at the found pos. if it is, then...
            board[row][col] = i                 # set value at the found indicies to the valid num
            if solve(board):
                return True                     # we call solve again. If the base case (aka having no more empty squares) triggers, then it will return true. this layer in turn will return true and continue up the chain
        
            board[row][col] = 0                 # if the recursive call didn't succeed, it means we have to keep digging. We mark the current pos as "empty" by giving it value 0. This ensures that we will continue finding new empty squares

    return False

# print(find_empty(board))
print("\n\n")
print_board(board)
print("\n\n")
# pos = (5,4)
# print(valid(board, 3, pos))
solve(board)
print_board(board)