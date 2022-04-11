# I need 3 list groups, one rows, second columns third 3X3
# each number must be unique in row, columns and 3x3 groups
# for example row1, col1, must be 1 only if there is no other 1 in row or in column
# Each row must have all numbers from 1 to 9
# Each column must have all number from 1 to 9
# Each 3x3 must have all numbers from 1 to 9

from tokenize import group


my_sudoku = {
    'group1': [
        ["Col1 row 1", 2, 3],
        ["Col1 row 2", None, None],
        ["Col1 row 3", None, None],
    ],
    'group2': [
        [4, 5, 6],
        [None, None, None],
        [None, None, None],
    ],
    'group3': [
        [7, 8, 9],
        [None, None, None],
        [None, None, None],
    ],
    'group4': [
        ["Col1 row 4", None, None],
        ["Col1 row 5", None, None],
        ["Col1 row 6", None, None],
    ],
    'group5': [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ],
    'group6': [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ],
    'group7': [
        ["Col1 row 7", None, None],
        ["Col1 row 8", None, None],
        ["Col1 row 9", None, None],
    ],
    'group8': [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ],
    'group9': [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ],
}

my_sudoku_lines = {
    'line1': [
        my_sudoku['group1'][0],
        my_sudoku['group2'][0],
        my_sudoku['group3'][0],
    ],
    'line2': [
        my_sudoku['group1'][1],
        my_sudoku['group2'][1],
        my_sudoku['group3'][1],
    ],
    'line3': [
        my_sudoku['group1'][2],
        my_sudoku['group2'][2],
        my_sudoku['group3'][2],
    ],
    'line4': [
        my_sudoku['group4'][0],
        my_sudoku['group5'][0],
        my_sudoku['group6'][0],
    ],
    'line5': [
        my_sudoku['group4'][1],
        my_sudoku['group5'][1],
        my_sudoku['group6'][1],
    ],
    'line6': [
        my_sudoku['group4'][2],
        my_sudoku['group5'][2],
        my_sudoku['group6'][2],
    ],
    'line7': [
        my_sudoku['group7'][0],
        my_sudoku['group8'][0],
        my_sudoku['group9'][0],
    ],
    'line8': [
        my_sudoku['group7'][1],
        my_sudoku['group8'][1],
        my_sudoku['group9'][1],
    ],
    'line9': [
        my_sudoku['group7'][2],
        my_sudoku['group8'][2],
        my_sudoku['group9'][2],
    ],
}


my_sudoku_columns = {
    "column1": [
        my_sudoku['group1'][0][0],
        my_sudoku['group1'][1][0],
        my_sudoku['group1'][2][0],
        my_sudoku['group4'][0][0],
        my_sudoku['group4'][1][0],
        my_sudoku['group4'][2][0],
        my_sudoku['group7'][0][0],
        my_sudoku['group7'][1][0],
        my_sudoku['group7'][2][0]
    ],
    "column2": [
        my_sudoku['group1'][0][1],
        my_sudoku['group1'][1][1],
        my_sudoku['group1'][2][1],
        my_sudoku['group4'][0][1],
        my_sudoku['group4'][1][1],
        my_sudoku['group4'][2][1],
        my_sudoku['group7'][0][1],
        my_sudoku['group7'][1][1],
        my_sudoku['group7'][2][1]
    ],
    "column3": [
        my_sudoku['group1'][0][2],
        my_sudoku['group1'][1][2],
        my_sudoku['group1'][2][2],
        my_sudoku['group4'][0][2],
        my_sudoku['group4'][1][2],
        my_sudoku['group4'][2][2],
        my_sudoku['group7'][0][2],
        my_sudoku['group7'][1][2],
        my_sudoku['group7'][2][2]
    ],
    "column4": [
        my_sudoku['group2'][0][0],
        my_sudoku['group2'][1][0],
        my_sudoku['group2'][2][0],
        my_sudoku['group5'][0][0],
        my_sudoku['group5'][1][0],
        my_sudoku['group5'][2][0],
        my_sudoku['group8'][0][0],
        my_sudoku['group8'][1][0],
        my_sudoku['group8'][2][0]
    ],
    "column5": [
        my_sudoku['group2'][0][1],
        my_sudoku['group2'][1][1],
        my_sudoku['group2'][2][1],
        my_sudoku['group5'][0][1],
        my_sudoku['group5'][1][1],
        my_sudoku['group5'][2][1],
        my_sudoku['group8'][0][1],
        my_sudoku['group8'][1][1],
        my_sudoku['group8'][2][1]
    ],
    "column6": [
        my_sudoku['group2'][0][2],
        my_sudoku['group2'][1][2],
        my_sudoku['group2'][2][2],
        my_sudoku['group5'][0][2],
        my_sudoku['group5'][1][2],
        my_sudoku['group5'][2][2],
        my_sudoku['group8'][0][2],
        my_sudoku['group8'][1][2],
        my_sudoku['group8'][2][2]
    ],
    "column7": [
        my_sudoku['group3'][0][0],
        my_sudoku['group3'][1][0],
        my_sudoku['group3'][2][0],
        my_sudoku['group6'][0][0],
        my_sudoku['group6'][1][0],
        my_sudoku['group6'][2][0],
        my_sudoku['group9'][0][0],
        my_sudoku['group9'][1][0],
        my_sudoku['group9'][2][0]
    ],
    "column8": [
        my_sudoku['group3'][0][1],
        my_sudoku['group3'][1][1],
        my_sudoku['group3'][2][1],
        my_sudoku['group6'][0][1],
        my_sudoku['group6'][1][1],
        my_sudoku['group6'][2][1],
        my_sudoku['group9'][0][1],
        my_sudoku['group9'][1][1],
        my_sudoku['group9'][2][1]
    ],
    "column9": [
        my_sudoku['group3'][0][2],
        my_sudoku['group3'][1][2],
        my_sudoku['group3'][2][2],
        my_sudoku['group6'][0][2],
        my_sudoku['group6'][1][2],
        my_sudoku['group6'][2][2],
        my_sudoku['group9'][0][2],
        my_sudoku['group9'][1][2],
        my_sudoku['group9'][2][2]
    ],


}

print(my_sudoku_lines['line1'])
print(my_sudoku_columns['column1'])
