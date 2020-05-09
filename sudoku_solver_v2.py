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

#
box_height = 3
box_width = 3
total_width = 8

def print_board(board):
    for i in range(len(board)):
        if i % box_height == 0 and i != 0:
            print("\n- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % box_width == 0 and j != 0:
                print(" | ", end="")
            
            digitToPrint = board[i][j] if board[i][j] != 0 else " "
            if j == total_width:
                print(digitToPrint)                  
            else:
                print(str(digitToPrint) + " ", end="")   


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  
    return None

def valid(board, number, pos): 
    
    for ele in range(len(board[0])):                                
        if board[pos[0]][ele] == number and pos[1] != ele:   
            return False
    
    for ele in range(len(board)):                                   
        if board[ele][pos[1]] == number and pos[0] != ele:   
            return False

    
    box_x = math.floor(pos[0] / 3)
    box_y = math.floor(pos[1] / 3)

    for x in range(box_x*3, box_x*3 + 3):
        for y in range(box_y*3, box_y*3 + 3):
            if board[x][y] == number and pos != (x, y):
                return False

    return True


def solve(board):
    found = find_empty(board)                   
    if not found:
        return True                             
    row, col = found                            
    
    for i in range(1,10):                       
        if valid(board, i, (row,col)):          
            board[row][col] = i                 
            if solve(board):
                return True                     
        
            board[row][col] = 0                 

    return False


# print(find_empty(board))
print("\n\n")
print_board(board)
print("\n\n")
# pos = (5,4)
# print(valid(board, 3, pos))
solve(board)
print_board(board)