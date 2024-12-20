import copy
import random
import os, platform

def clear_console():
    os_platform = platform.system()
    os.system('cls') if os_platform == "Windows" else 'clear'

while True:
    name = input('Please, enter your name: ')
    field = [['~' for _ in range(7)] for _ in range(7)]
    display_field = copy.deepcopy(field)
    final_field = copy.deepcopy(field)
    rating = {}

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
        for i in range(4):
            place_ship(1)


    create_ship()

    print("Let's get acquainted with the rules:\n"
          "▧- hit\n"
          "x - miss\n"
          "■ - sank\n"
          "you have to move along the coordinate, enter the letter (A-G)\n"
          "and then the number (1-7)\n"
          "example of hit: B 2\n"
          "Let's start!\n"
          ""
          "That's the field:")

    print('   A  B  C  D  E  F  G')
    for row_count, row in enumerate(display_field):
        print(f"{row_count + 1}  " + "  ".join(row))

    destroyed_ships = 0
    count_of_moves = 0
    while True:
        try:
            letter, num = input('Enter coordinate: ').split()
            count_of_moves += 1
            print(destroyed_ships)
            col_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            row_values = ['1', '2', '3', '4', '5', '6', '7']
            if not letter in col_values:
                print('Please enter the correct coordinate:')
                continue
            if not num in row_values:
                print('Please enter the correct coordinate:')
                continue
            index_to_hit_row = 0
            index_to_hit_col = 0
            for l in col_values:
                if l == letter:
                    break
                index_to_hit_col += 1
            for l in row_values:
                if l == num:
                    break
                index_to_hit_row += 1

            if field[index_to_hit_row][index_to_hit_col] == 'X':
                print('You have already hit this coordinate, choose another one.')
                print('   A  B  C  D  E  F  G')
                for row_count, row in enumerate(display_field):
                    print(f"{row_count + 1}  " + "  ".join(row))
                clear_console()

                continue

            checking_list = []
            if field[index_to_hit_row][index_to_hit_col] == '□':
                field[index_to_hit_row][index_to_hit_col] = 'X'
                display_field[index_to_hit_row][index_to_hit_col] = '▧'
                final_field[index_to_hit_row][index_to_hit_col] = '■'
                for k in range(-1, 2):
                    for r in range(-1, 2):
                        if 0 <= k + index_to_hit_row < 7 and 0 <= r + index_to_hit_col < 7:
                            checking_list.append(field[index_to_hit_row + k][index_to_hit_col + r])
                if not '□' in checking_list:
                    destroyed_ships += 1
                    clear_console()
                    print('   A  B  C  D  E  F  G')
                    for row_count, row in enumerate(final_field):
                        print(f"{row_count + 1}  " + "  ".join(row))
                    display_field = copy.deepcopy(final_field)
                    if destroyed_ships == 7:
                        rating[name] = count_of_moves
                        print(f'The game is over!\n'
                              f'The number of your moves: {count_of_moves}')
                        break

                    continue
                else:
                    clear_console()
                    print('   A  B  C  D  E  F  G')
                    for row_count, row in enumerate(display_field):
                        print(f"{row_count + 1}  " + "  ".join(row))
                        continue

            if field[index_to_hit_row][index_to_hit_col] == '~':
                field[index_to_hit_row][index_to_hit_col] = 'X'
                display_field[index_to_hit_row][index_to_hit_col] = 'X'
                final_field[index_to_hit_row][index_to_hit_col] = 'X'
                clear_console()
                print('   A  B  C  D  E  F  G')
                for row_count, row in enumerate(display_field):
                    print(f"{row_count + 1}  " + "  ".join(row))
                    continue
            continue
        except ValueError:
            print('Please enter the correct coordinate:')
            continue

    while True:
        answer = int(input('would you like to start a new game?\n'
                           '1 - Yes\n'
                           '2 - No\n'
                           ': '))
        if answer == 1:
            break
        if answer == 2:
            clear_console()
            for key, move in sorted(rating.items(), key=lambda item: item[1]):
                print(f"rating of players:\n"
                      f"name : number of moves\n"
                      f"{key}: {move}")
                exit()