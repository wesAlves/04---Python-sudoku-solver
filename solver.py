from pyparsing import col


def sudoku_solver(sudokuOBJ):

    sudoku_size = 9
    group_size = 3

    # Create arrays for line, column and 3X3 square
    lines = {}
    columns = {}
    group = {}

    i_line = 0
    i_column = 0
    i_group = 0

    for line in sudokuOBJ:
        lines[f'line_{i_line}'] = line
        i_line += 1

    for i_column in range(sudoku_size):
        current_column = columns[f'column_{i_column}'] = []

        for i in range(len(lines)):
            current_column.append(lines[f'line_{i}'][i_column])

    print('group', group)


sudoku_solver([[8, 7, 4, 6, 9, 5, 0, 2, 0],
               [0, 3, 0, 0, 7, 4, 0, 0, 6],
               [6, 9, 5, 3, 1, 2, 0, 0, 7],
               [5, 2, 6, 0, 4, 8, 0, 3, 0],
               [0, 0, 0, 5, 0, 7, 8, 6, 4],
               [0, 0, 0, 9, 0, 0, 0, 0, 0],
               [1, 0, 8, 0, 3, 6, 0, 0, 2],
               [0, 0, 2, 0, 5, 9, 1, 7, 8],
               [7, 5, 9, 2, 8, 1, 0, 4, 3]])
