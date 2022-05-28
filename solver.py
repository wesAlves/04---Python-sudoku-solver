def find_next_empty(sudoku):
    # Finds the next row, col on the puzzle that's not filled yet
    # Return row, col tuple or (None, None)

    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == -1:
                return row, col

    return None, None


def is_valid(sudoku, guess, row, col):
    # Figures out whether the guess at the row/col of the puzzçe is valid guess

    # Star with row
    row_vals = sudoku[row]
    if guess in row_vals:
        # print(guess, 'value is in row')
        return False

    # Going to column
        # col_vals = []
        # for i in range(9):
        #     col_vals.append(sudoku[i][col])
    col_vals = [sudoku[i][col] for i in range(9)]
    if guess in col_vals:
        # print(guess, 'value is in col')
        return False

    # And then the square
    row_start = (row//3) * 3
    col_start = (row//3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if sudoku[r][c] == guess:
                # print(guess, 'value is in 3x3')
                return False

    return True


def sudoku_solver(sudoku):

    row, col = find_next_empty(sudoku)

    if row is None and col is None:  # Here we have solved the puzzle
        return True

    # If we have spots to fill
    for guess in range(1, 10):
        if is_valid(sudoku, guess, row, col):
            # If the guess is true put in the puzzle
            sudoku[row][col] = guess

            # Recuse unsing sudoku
            if sudoku_solver(sudoku):
                return True

        sudoku[row][col] = -1
        # sudoku_solver(sudoku)

    return False


if __name__ == '__main__':
    example = [
        [-1, 6, -1, -1, -1, -1, -1, -1, 4],
        [-1, 5, -1, -1, 7, 1, -1, 8, -1],
        [-1, 1, -1, -1, 9, -1, -1, -1, 3],
        [2, -1, -1, -1, 8, -1, -1, -1, 7],
        [-1, -1, -1, 6, -1, 4, -1, -1, -1],
        [9, -1, -1, 7, -1, -1, -1, 4, -1],
        [-1, 9, -1, -1, 7, -1, 5, -1, -1],
        [3, -1, 2, -1, 1, -1, -1, -1, 8],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]

    print(sudoku_solver(example))
    print(example)
