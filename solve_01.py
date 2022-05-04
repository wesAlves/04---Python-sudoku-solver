from multiprocessing.dummy import Array


main_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


my_sudoku_arr = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

solved_sudoku_arr = []

possible_numbers = Array

# Verify if the the number are listed in the main_numbers list and if is not, pick a number that is not in my_sudoku_arr list

usedIn_in_row = []


def Is_in_main_numbers(my_number):
    if my_number in main_numbers:
        usedIn_in_row.append(my_number)

        return my_number
    else:
        if my_number in usedIn_in_row:
            n = 0

            while n in range(len(main_numbers)):

                if main_numbers[n] in usedIn_in_row:
                    n = n+1
                else:
                    usedIn_in_row.append(main_numbers[n])
                    break

        else:
            usedIn_in_row.append(my_number)
            return 3


for row in my_sudoku_arr:
    for row_item in row:
        row_item = Is_in_main_numbers(row_item)
        # print(row_item)
print(usedIn_in_row)
