from pyparsing import col


def sudoku_solver(sudokuOBJ):

    sudoku_dic = sudokuOBJ
    sudoku_size = 9

    lines = []
    columns = []
    group = [[0] * 3] * 3
    groups = [group] * 9

    # populate line
    for line in sudoku_dic:
        lines.append(line)

    # populate columns
    for i in range(sudoku_size):

        columns.append([])

        for line in lines:
            columns[i].append(line[i])

    print(columns)
    print(lines)

    # go by line
    # for line in sudoku_dic:
    #     for i in range(len(line)):
    #         if line[i] == 0:
    #             for p in range(1, 10):
    #                 if p not in line:
    #                     # call function here to solve the line
    #                     print(p)

    # # go by column
    # for column in columns:
    #     for i in range(len(columns)):
    #         if column[i] == 0:
    #             for p in range(1, 10):
    #                 if p not in column:
    #                     # call function here to solve the column
    #                     print(p)

    # # go by group
    # for line in group:
    #     for i in range(len(group)):
    #         if line[i] == 0:
    #             for p in range(1, 10):
    #                 if p not in line:
    #                     print(p)


sudoku_solver([
    [8, 7, 4, 6, 9, 5, 0, 2, 0],
    #    [0, 3, 0, 0, 7, 4, 0, 0, 6],
    #    [6, 9, 5, 3, 1, 2, 0, 0, 7],
    #    [5, 2, 6, 0, 4, 8, 0, 3, 0],
    #    [0, 0, 0, 5, 0, 7, 8, 6, 4],
    #    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    #    [1, 0, 8, 0, 3, 6, 0, 0, 2],
    #    [0, 0, 2, 0, 5, 9, 1, 7, 8],
    [7, 5, 9, 2, 8, 1, 0, 4, 3]])
