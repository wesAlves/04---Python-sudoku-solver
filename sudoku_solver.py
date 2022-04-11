# I need 3 list groups, one rows, second columns third 3X3
# each number must be unique in row, columns and 3x3 groups
# for example row1, col1, must be 1 only if there is no other 1 in row or in column
# Each row must have all numbers from 1 to 9
# Each column must have all number from 1 to 9
# Each 3x3 must have all numbers from 1 to 9

from tokenize import group


my_sudoku = {
    'group1': [
        [1, 2, 3],
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
        [None, None, None],
        [None, None, None],
        [None, None, None],
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
        [None, None, None],
        [None, None, None],
        [None, None, None],
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
        my_sudoku_lines['line1'][0],
        my_sudoku_lines['line2'][0],
        my_sudoku_lines['line3'][0],
        my_sudoku_lines['line4'][0],
        my_sudoku_lines['line5'][0],
        my_sudoku_lines['line6'][0],
        my_sudoku_lines['line7'][0],
        my_sudoku_lines['line8'][0],
        my_sudoku_lines['line9'][0],
    ],
    "column2": [
        my_sudoku_lines['line1'][1],
        my_sudoku_lines['line2'][1],
        my_sudoku_lines['line3'][1],
        my_sudoku_lines['line4'][1],
        my_sudoku_lines['line5'][1],
        my_sudoku_lines['line6'][1],
        my_sudoku_lines['line7'][1],
        my_sudoku_lines['line8'][1],
        my_sudoku_lines['line9'][1],
    ],
    "column3": [
        my_sudoku_lines['line1'][2],
        my_sudoku_lines['line2'][2],
        my_sudoku_lines['line3'][2],
        my_sudoku_lines['line4'][2],
        my_sudoku_lines['line5'][2],
        my_sudoku_lines['line6'][2],
        my_sudoku_lines['line7'][2],
        my_sudoku_lines['line8'][2],
        my_sudoku_lines['line9'][2],
    ],
    "column4": [
        my_sudoku_lines['line1'][3],
        my_sudoku_lines['line2'][3],
        my_sudoku_lines['line3'][3],
        my_sudoku_lines['line4'][3],
        my_sudoku_lines['line5'][3],
        my_sudoku_lines['line6'][3],
        my_sudoku_lines['line7'][3],
        my_sudoku_lines['line8'][3],
        my_sudoku_lines['line9'][3],
    ],
    "column5": [
        my_sudoku_lines['line1'][4],
        my_sudoku_lines['line2'][4],
        my_sudoku_lines['line3'][4],
        my_sudoku_lines['line4'][4],
        my_sudoku_lines['line5'][4],
        my_sudoku_lines['line6'][4],
        my_sudoku_lines['line7'][4],
        my_sudoku_lines['line8'][4],
        my_sudoku_lines['line9'][4],
    ],
    "column6": [
        my_sudoku_lines['line1'][5],
        my_sudoku_lines['line2'][5],
        my_sudoku_lines['line3'][5],
        my_sudoku_lines['line4'][5],
        my_sudoku_lines['line5'][5],
        my_sudoku_lines['line6'][5],
        my_sudoku_lines['line7'][5],
        my_sudoku_lines['line8'][5],
        my_sudoku_lines['line9'][5],
    ],
    "column7": [
        my_sudoku_lines['line1'][6],
        my_sudoku_lines['line2'][6],
        my_sudoku_lines['line3'][6],
        my_sudoku_lines['line4'][6],
        my_sudoku_lines['line5'][6],
        my_sudoku_lines['line6'][6],
        my_sudoku_lines['line7'][6],
        my_sudoku_lines['line8'][6],
        my_sudoku_lines['line9'][6],
    ],
    "column8": [
        my_sudoku_lines['line1'][7],
        my_sudoku_lines['line2'][7],
        my_sudoku_lines['line3'][7],
        my_sudoku_lines['line4'][7],
        my_sudoku_lines['line5'][7],
        my_sudoku_lines['line6'][7],
        my_sudoku_lines['line7'][7],
        my_sudoku_lines['line8'][7],
        my_sudoku_lines['line9'][7],
    ],
    "column9": [
        my_sudoku_lines['line1'][8],
        my_sudoku_lines['line2'][8],
        my_sudoku_lines['line3'][8],
        my_sudoku_lines['line4'][8],
        my_sudoku_lines['line5'][8],
        my_sudoku_lines['line6'][8],
        my_sudoku_lines['line7'][8],
        my_sudoku_lines['line8'][8],
        my_sudoku_lines['line9'][8],
    ],


}

print(my_sudoku_lines['line1'])
print(my_sudoku_columns['column1'])
