import copy
import random

field = [['~' for _ in range(7)] for _ in range(7)]
checker_field = copy.deepcopy(field)


def can_ship_place(size, ship_row, ship_column, row_index, column_index):
    for i in range(size):
        for ii in range(-1, 2):
            for iii in range(-1, 2):
                if 0 <= ii + row_index < 7 and 0 <= iii + column_index < 7 and \
                        field[ii + row_index][iii + column_index] != '~':
                    return False
        if ship_row > ship_column:
            row_index += 1
        elif ship_column > ship_row:
            column_index += 1
    return True


def place_ship(size):
    while True:
        x = [1, size]
        random.shuffle(x)
        ship_row, ship_column = x
        row_index = random.randint(0, 7 - ship_row)
        column_index = random.randint(0, 7 - ship_column)

        if can_ship_place(size, ship_row, ship_column, row_index, column_index):
            if ship_row > ship_column:
                for j in range(size):
                    field[row_index + j][column_index] = '□'
            elif ship_column > ship_row:
                for j in range(size):
                    field[row_index][column_index + j] = '□'
            else:
                field[row_index][column_index] = '□'
            break

def create_ship():
    place_ship(3)
    place_ship(2)
    place_ship(2)
    for j in range(4):
        place_ship(1)

create_ship()

print('   A  B  C  D  E  F  G')
for k, row in enumerate(field):
    print(f"{k + 1}  " + "  ".join(row))