#2d array of sudoku board, each row is a list

sudokuboard = [
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [2, 0, 7, 0, 0, 9, 0, 0, 0],
    [6, 0, 0, 3, 5, 1, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 8, 2, 0, 5, 3, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 4],
    [0, 0, 6, 2, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 7, 0, 0]
]

def print_board(board): 
    #print dotted border lines after every third column
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")

    #print border lines after every third row 
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
    #print numbers 
            if j == 8: #last element in a row, doesn't need a space
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="") #includes space after printing and doesn't move to next line
                

print_board(sudokuboard)