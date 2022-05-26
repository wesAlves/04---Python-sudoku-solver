def sudoku_solver(sudokuOBJ):

    sudoku_row_size = 9
    sudoku_col_size = 9
    group_size = 3

    # Create arrays for line, column and 3X3 square
    lines = {}

    columns = {}

    i_line = 0
    i_column = 0

    for line in sudokuOBJ:
        lines[f'line_{i_line}'] = line
        i_line += 1

    for i_column in range(sudoku_col_size):
        current_column = columns[f'column_{i_column}'] = []

        for i in range(len(lines)):
            current_column.append(lines[f'line_{i}'][i_column])

    # print('linhas', lines)
    print('colunas', columns)


sudoku_solver([[8, 7, 4, 6, 9, 5, 0, 2, 0],
               [7, 5, 9, 2, 8, 1, 0, 4, 3]])
