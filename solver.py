def sudoku_solver(sudokuOBJ):

    # Create arrays for line, column and 3X3 square
    lines = {}

    columns = []

    i_line = 0
    i_column = 0

    for line in sudokuOBJ:
        lines['line_%s' % i_line] = line
        i_line += 1

    # for key in lines:
    #     print(len(lines[key]))
    #     print(key)

    # print('linhas', lines)
    # print('colunas', columns)


sudoku_solver([[8, 7, 4, 6, 9, 5, 0, 2, 0],
               [7, 5, 9, 2, 8, 1, 0, 4, 3]])
