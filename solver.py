#2d array of a sudoku board, each row is a list

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
            print("------------------------")

    #print border lines after every third row 
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
    #print numbers 
            if j == 8: #last element in a row, doesn't need a space
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="") #includes space after printing and doesn't move to next line
                

def is_valid_position(board, number, position):
    #check ROW
    #check each element in the row to see if there are any duplicates within the ROW 
    for i in range(len(board[0])): 
        if board[position[0]][i] == number: 
            return False 
        
    #check COLUMN
    #check each element in the column to see if there are any duplicates within the COLUMN
    for i in range(len(board)):
        if board[i][position[1]] == number: 
            return False 
        
    #check BOX 
    #check each element in the box to see if there are any duplicates within the BOX
    box_x = position[0] // 3 
    box_y = position[1] // 3

    for i in range(box_x * 3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False 
            
    return True 


def find_empty_square(board): 
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] == 0: 
                return (i, j) #row and column of the empty sqaure 
            
    return False


def solve(board): 
    emptysquare = find_empty_square(board)
    if not emptysquare: 
        return True 
    
    row,column = emptysquare

    for i in range(1,10): 
        if is_valid_position(board, i, (row, column)): #check if adding the number 1-9 is a valid placement
            board[row][column] = i #if valid, then we add to the board 

            if solve(board): #RECURSIVELY try to finish the solution 
                return True 
            
            board[row][column] = 0 #didnt work, have to backtrack, reset position

    return False 

    

print_board(sudokuboard)

solve(sudokuboard)

print("\n\n")

print_board(sudokuboard)