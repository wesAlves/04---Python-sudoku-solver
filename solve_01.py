main_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


my_sudoku_arr = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]

solved_sudoku_arr = []

for row in my_sudoku_arr:
    n = 0

    for row_item in row:
        if row_item not in main_numbers:
            # Need to pick one from the list and then test it against all numbers in this list to chekc if it is are not repeting itself

            temp_number = 0

            for n in range(len(main_numbers)):
                temp_number = main_numbers[n]
                n = n+1

            if temp_number in row:
                print('it already in the list')

                # if temp_number < 9:
                #     temp_number = temp_number + 1
                # else:
                #     temp_number = 0

                print(temp_number)
            else:
                print('it is not')
                print(temp_number)

            # row_item = main_numbers[2]
            # print(row_item)
            # print("is not")
        # else:
        #     print(row_item)
        #     print("it is")

    #     row_item = n
        # print(row_item)
