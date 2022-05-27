from pyparsing import col


def sudoku_solver(sudokuOBJ):

    sudoku_dic = sudokuOBJ
    sudoku_size = 9

    lines = []
    columns = []
    # group = []
    groups = []

    x = 0
    y = 0

    # populate line
    for line in sudoku_dic:
        lines.append(line)

    # populate columns
    for i in range(sudoku_size):
        columns.append([])

        for line in lines:
            columns[i].append(line[i])

    # populate group
            # groups[group][x] = lines[x][0], lines[x][1], lines[x][2]

    for group in range(sudoku_size):
        # append a new group
        groups.append([])

        for y in range(sudoku_size//3):
            # append a new line in each group
            groups[group].append([0, 0, 0])

            # find the right line to interact accordingli with group position
            if group < 3:
                line = lines[y]
            if 6 > group >= 3:
                line = lines[y+3]
            if group >= 6:
                line = lines[y+6]

            # find the right group to interact accrodingli with group position
            for x in range(sudoku_size):
                column_element = line[x]

                # Append empty array
                if x < 3:
                    groups[group][y][x] = column_element
                else:
                    groups[group][y][x] = 3

                    # groups[group][y].append(column_element)

                    # append 3 elements to a line
                    # groups[group][y].append(y*3)
                    # groups[group][y].append(y*3+1)
                    # groups[group][y].append(y*3+2)

                    # print(columns)
                    # print(lines)
    print(groups[8])

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
    [0, 3, 0, 0, 7, 4, 0, 0, 6],
    [6, 9, 5, 3, 1, 2, 0, 0, 7],
    [5, 2, 6, 0, 4, 8, 0, 3, 0],
    [0, 0, 0, 5, 0, 7, 8, 6, 4],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [1, 0, 8, 0, 3, 6, 0, 0, 2],
    [0, 0, 2, 0, 5, 9, 1, 7, 8],
    [7, 5, 9, 2, 8, 1, 0, 4, 3]
])
