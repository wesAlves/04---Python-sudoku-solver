from ast import IsNot


def write_numbers(*args):

    for i in range(1, 10):
        if i not in args:
            print(i)

    print(f'Hello {args}')


write_numbers(1, 2, 3)
