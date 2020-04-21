from Test import Test, Test as test

'''
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Examples
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
'''

def valid_solution(board):
    numbers = [1,2,3,4,5,6,7,8,9]
    # Check rows
    for row in board:
        for n in numbers:
            if n not in row:
                return False
    # Check cols
    for col, val in enumerate(board[0]):
        for n in numbers:
            if n not in [board[row][col] for row in range(9)]:
                return False
    # Check 9x9 blocks
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            l = []
            for a in range(3):
                for b in range(3):
                    l.extend([board[x+a][y+b]])
            for n in numbers:
                if n not in l:
                    return False
    return True

# Cleaned up
def valid_solution(board):
    for row in board:
        for n in list(range(1,10)):
            if n not in row:
                return False
    for col, v in enumerate(board[0]):
        for n in list(range(1,10)):
            if n not in [board[row][col] for row in range(9)]:
                return False
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            for n in list(range(1,10)):
                if n not in [board[x+a][y+b] for a in range(3) for b in range(3)]:
                    return False
    return True


try:
    valid_solution = validSolution
except NameError:
    pass

test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);

test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);


test.assert_equals(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                    [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                    [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                    [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                    [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                    [9, 1, 2, 3, 4, 5, 6, 7, 8]]), False);
