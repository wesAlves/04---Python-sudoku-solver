# define an sudoku table as 3x3 and 5 in the middle

line1 = [0] * 3
line2 = [0] * 3
line3 = [0] * 3

line2[1] = 5

my_sudoku_arr = line1 + line2 + line3


def write_numbers(*args):

    seted_numbers = list(args)
    print(seted_numbers)

    for i in my_sudoku_arr:
        for b in range(1, 10):
            if b not in seted_numbers:
                seted_numbers.append(b)

    print(seted_numbers)


write_numbers(1, 2, 3)


# fisrt group 3x3 is a list, and it has 3 positions at line1(col1, col2, col3), line2(col1, col2, col3) and line3(col1, col2, col3)
