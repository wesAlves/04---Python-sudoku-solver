# define an sudoku table as 3x3 and 5 in the middle

row1 = {'col1': 0, 'col2': 0, 'col3': 0}
row2 = {'col1': 0, 'col2': 0, 'col3': 0}
row3 = {'col1': 0, 'col2': 0, 'col3': 0}

# row2['col2'] = 5

my_sudoku_arr = {
    "row1": row1,
    "row2": row2,
    "row3": row3,
}

# print(my_sudoku_arr)


def write_numbers(*args):

    seted_numbers = list(args)
    print(seted_numbers)

    for i in my_sudoku_arr:
        for b in range(1, 10):
            if b not in seted_numbers:
                seted_numbers.append(b)

    print(seted_numbers)


# write_numbers(1, 2, 3)


# fisrt group 3x3 is a list, and it has 3 positions at line1(col1, col2, col3), line2(col1, col2, col3) and line3(col1, col2, col3)
