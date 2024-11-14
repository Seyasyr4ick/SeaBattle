import copy
import random

field = [['~' for _ in range(7)] for _ in range(7)]
checker_field = copy.deepcopy(field)

def can_ship_place(size, row, column, row_index, column_index):
    if row > column:
        # Проверка вертикального размещения
        if row_index + size > 7:  # Проверка, что корабль помещается по вертикали
            return False
        for i in range(size):
            if field[row_index + i][column_index] != '~':  # Проверка на препятствия
                return False
    elif column > row:
        # Проверка горизонтального размещения
        if column_index + size > 7:  # Проверка, что корабль помещается по горизонтали
            return False
        for i in range(size):
            if field[row_index][column_index + i] != '~':  # Проверка на препятствия
                return False
    else:
        # Для 1x1 корабля
        if field[row_index][column_index] != '~':
            return False

    return True

def place_ship(size):
    while True:
        # Случайным образом выбираем ориентацию корабля
        x = [1, size]
        random.shuffle(x)
        row, column = x
        row_index = random.randint(0, 7 - row)
        column_index = random.randint(0, 7 - column)

        if can_ship_place(size, row, column, row_index, column_index):
            if row > column:
                # Вертикальное размещение
                for i in range(size):
                    field[row_index + i][column_index] = '□'
            elif column > row:
                # Горизонтальное размещение
                for i in range(size):
                    field[row_index][column_index + i] = '□'
            else:
                # Размещение корабля 1x1
                field[row_index][column_index] = '□'
            break  # Завершаем цикл, как только корабль размещен успешно

def create_ships():
    place_ship(3)
    place_ship(2)
    place_ship(2)
    for _ in range(4):
        place_ship(1)

create_ships()

# Вывод поля с заголовками
print('   A  B  C  D  E  F  G')
for i, row in enumerate(field):
    print(f"{i + 1}  " + "  ".join(row))
