import copy
import random

name = input('Please, enter your name')
field = [['~' for _ in range(7)] for _ in range(7)]
checker_field = copy.deepcopy(field)
def can_ship_place(size, row, column, row_index, column_index):
    for i in range(size):
        for ii in range(-1, 2):
            for iii in range(-1, 2):
                if 0 <= i + row_index < 7 and 0 <= ii + column_index < 7 and \
                    field[i + row_index][column_index] != '~':
                    return False
        if row > column: row_index += 1
        elif column > row: column_index += 1
    return True

def place_ship(size):
    while True:
        x = [1, size]
        random.shuffle(x)
        row, column = x
        row_index = random.randint(0, 7 - row)
        column_index = random.randint(0, 7 - column)
        if can_ship_place(size, row, column, row_index, column_index):
            for i in range(size):
                if row > column:
                    for ii in range(size):
                        field[row_index][column_index] = '□'
                        row_index += 1
                elif column > row:
                    for ii in range(size):
                        field[row_index][column_index] = '□'
                        column_index += 1
                else: field[row_index][column_index] = '□'

def create_ship():
    place_ship(3)
    place_ship(2)
    place_ship(2)
    for i in range(4):
        place_ship(1)

