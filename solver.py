from pyparsing import col


def sudoku_solver(sudokuOBJ):

    sudoku_dic = sudokuOBJ

    # go by line
    for line in sudoku_dic:
        for i in range(len(line)):
            if line[i] == 0:
                for p in range(1, 10):
                    if p not in line:
                        print(p)


sudoku_solver([
    # [8, 7, 4, 6, 9, 5, 0, 2, 0],
    #    [0, 3, 0, 0, 7, 4, 0, 0, 6],
    #    [6, 9, 5, 3, 1, 2, 0, 0, 7],
    #    [5, 2, 6, 0, 4, 8, 0, 3, 0],
    #    [0, 0, 0, 5, 0, 7, 8, 6, 4],
    #    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    #    [1, 0, 8, 0, 3, 6, 0, 0, 2],
    #    [0, 0, 2, 0, 5, 9, 1, 7, 8],
    [7, 5, 9, 2, 8, 1, 0, 4, 3]])