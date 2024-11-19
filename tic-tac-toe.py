# Создаем функцию для вывода поля, чтобы не пришлось каждый раз копировать часть кода
def view_field(field):
    print('\n'.join('\t'.join(map(str, row)) for row in field))
#создаем функцию для проверки, является ли ход выигрышным.
def check_win():
    win_cord = (((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)),
                ((1, 3), (2, 2), (3, 1)), ((1, 1), (2, 2), (3, 3)), ((1, 1), (2, 1), (3, 1)),
                ((1, 2), (2, 2), (3, 2)), ((1, 3), (2, 3), (3, 3)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл O!")
            return True
    return False



# создаем поле для игры
field = [['', 0, 1, 2],
         [0, '-', '-', '-'],
         [1, '-', '-', '-'],
         [2, '-', '-', '-' ]]
view_field(field)

# создаем цикл. В нем будет проходить игра
while True:
    print(f'O, ваш ход! Напишите координату, в которую хотите поставить О.')
    # Заметка: координата вводится в формате "x, y".
    move = input()
    #Проверка ввода нечислового значения
    if not move[0].isdigit() or not move[-1].isdigit():
        break
    else:
        x = int(move[0])
        y = int(move[-1])
    # Проверяем, занята ли координата
    while True:
        if field[x+1][y+1] != '-':
            continue
        else:
            field[x+1][y+1] = "O"
            view_field(field)
            break
    # Проверяем, является ли ход выигрышным. Если игрок побеждает, цикл прерывается
    if check_win():
        break

    print(f'X, ваш ход! Напишите координату, в которую хотите поставить X.')
    move = input()
    if not move[0].isdigit() or not move[-1].isdigit():
        break
    else:
        x = int(move[0])
        y = int(move[-1])
    # Проверяем, занята ли координата
    while True:
        if field[x + 1][y + 1] != '-':
            continue
        else:
            field[x + 1][y + 1] = "X"
            view_field(field)
            break
    if check_win():
        break


