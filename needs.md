# Sudoku solver
    - Need to find the number that metches the place based on
        - Each number must be unique in a set of 9 in a row
        - Each number must be unique in a set of 9 in a collumn
        - Each number must be unique ina group of 3X3 square
        - All mentioned above must fill a set of number that goes from 1 to 9, no matter the order.
            - The sum of each row, columns or 3x3 square must be 45.
            - All rows sum must be equal to 45X9 (405)
            - All columns sum must be equal to 45X9
            - The whole set of numbers in place must sum to 45X9(rows) + 45X9(columns)
            - Each occurency number must not share same column or row with other instances of that number
            - Each number will have 9 instances

    - The algorithim needs to look each row and each columns and finaly each group 3X3 to find the matches place for each number