def getBlockRowCol(row, col):
    startRow = row - (row % 3)
    startCol = col - (col % 3)

    return startRow, startCol

def isValid(board, row, col, num):
    # Check if the number is already present in the row
    if num in board[row]:
        return False
    
    # Check if the number is already present in the column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Get start row and start col in current 3x3 block
    startRow, startCol = getBlockRowCol(row, col)

    # Check if the number is already present in the 3x3 grid
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False
    
    return True

# Function to solve sudoku using backTracking
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if isValid(board, i, j, num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Function to print board
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Example Sudoku board (0 represents empty cells)
board1 = [
    [0, 1, 3, 8, 0, 0, 4, 0, 5],
    [0, 2, 4, 6, 0, 5, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 9, 0, 3],
    [4, 9, 0, 3, 0, 6, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 7, 0, 1, 0, 9, 3],
    [0, 6, 9, 0, 0, 0, 7, 4, 0],
    [0, 0, 0, 2, 0, 7, 6, 8, 0],
    [1, 0, 2, 0, 0, 8, 3, 5, 0]
]

board2 = [
    [0, 0, 2, 0, 0, 0, 0, 4, 1],
    [0, 0, 0, 0, 8, 2, 0, 7, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9],
    [2, 0, 0, 0, 0, 7, 9, 3, 0],
    [0, 1, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 6, 8, 1, 0, 0, 0, 4],
    [1, 0, 0, 0, 9, 0, 0, 0, 0],
    [0, 6, 0, 4, 3, 0, 0, 0, 0],
    [8, 5, 0, 0, 0, 0, 4, 0, 0]
]

board3 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print("Sudoku puzzle:")
print_board(board3)
print("\nSolving...\n")

if solve(board3):
    print("Sudoku solved:")
    print_board(board3)
else:
    print("No solution exists.")
