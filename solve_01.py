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
        # print(usedIn_in_row)
        return my_number
    else:
        if my_number in usedIn_in_row:
            print("already in used try another")
            n = 0
            while my_number not in usedIn_in_row:
                my_number = main_numbers[n]

                if my_number not in usedIn_in_row:
                    usedIn_in_row.append(my_number)
                    print(my_number)
                    print("ends here")

                n = n+1

        # else:
        #     print("Is not in the list adding now")
        #     usedIn_in_row.append(my_number)
        # return my_number
        # for row in my_sudoku_arr:
        #     for row_item in row:

        # print('No it is not')


for row in my_sudoku_arr:
    for row_item in row:
        row_item = Is_in_main_numbers(row_item)
        # print(row_item)
