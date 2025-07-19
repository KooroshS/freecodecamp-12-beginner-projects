def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None,) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None # meaning there is no space left in the puzzle

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is valid
    # if -> valid return True, else: False

    # let's start the the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now the column
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False
    
    # and then the square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if all these checks have passed then
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if the solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    # step 2: if there's a place to put a number, then make a guess from 1-9
    for guess in range(1, 10):
        # step 3: check if the guess is valid
        if is_valid(puzzle, guess, row, col):
            # step 3.1: If this is a vlid guess, then place it on the board
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # backtrack and try a new number
        puzzle[row][col] = -1 # reset the game

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!
    return False