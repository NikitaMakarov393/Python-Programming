import random
def distance_func(a, b, n):
    min_distance = float('inf')
    d = 0
    for i in range(n):
        distance = 0
        for j in range(2):
            vector = a[i][j] - b[j]
            distance += vector ** 2
        distance = distance ** 0.5
        if distance < min_distance:
            min_distance = distance
            d = i
    return a[d]
def func(x):
    return x**2/(10+x**3)
def task_1():
    a = -2
    b = 5
    n = 1000
    h = (b - a) / n
    f = []
    i = a
    while i < b:
        f.append(func(i))
        i += h
    sum = 0
    for i in f:
        sum += h * i
    print(f"{sum:.2f}")
def task_2():
    def generate_magic_square(n):
        if n < 3:
            print("Магический квадрат можно создать только для n >= 3.")
            return None
        magic_square = [0] * n
        for i in range(n):
            magic_square[i] = [0] * n
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i][j] = num
            new_i = (i - 1) % n
            new_j = (j + 1) % n
            if magic_square[new_i][new_j] != 0:
                i = (i + 1) % n
            else:
                i, j = new_i, new_j
        return magic_square
    n = int(input("Введите размер магического квадрата: "))
    magic_square = generate_magic_square(n)
    for i in range (n):
        for j in range (n):
            print(f"{magic_square[i][j]}",end=" ")
        print("")


def task_3():
    n = int(input("Количество сокровищ: "))
    treasure_map = [0] * n
    for i in range(n):
        treasure_map[i] = list(map(int, input(f"Введите координаты {i + 1} сокровища через пробел: ").split()))
    Sasha_position = list(map(int, input("Введите координаты Саши через пробел: ").split()))
    if len(Sasha_position) != 2:
        print("Неверный формат ввода координат Саши!")
        return
    closest_treasure = distance_func(treasure_map, Sasha_position, n)

    print("Ближайшее сокровище находится по координатам: ", *closest_treasure)

def task_4():
    menu = [
        ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
        ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
        ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
    ]
    g = len(menu)
    while 1:
        print("-" * 40)
        print("Меню")
        print("1 - отобразить название блюд меню")
        print("2 - отобразить инградиенты блюда")
        print("3 - посмотреть стоимость блюда")
        print("4 - поменять цену блюда")
        print("5 - Добавить новое блюдо")
        print("6 - выход")
        print("-" * 40)
        n = int(input("Введите номер действия: "))
        if n == 1:
            print("Меню: ")
            for i in range(g):
                print(menu[i][0])
        elif n == 2:
            name = input("Введите название блюда инградиенты которые вы хотите увидеть: ")
            for i in range (g):
                if menu[i][0] == name:
                    print("Инградиенты блюда ", name, ": ", *menu[i][1])
        elif n == 3:
            name = input("Введите название блюда цену которого вы хотите увидеть: ")
            for i in range (g):
                if menu[i][0] == name:
                    print("Цена блюда ", name, ": ", menu[i][2])
        elif n == 4:
            name = input("Введите название блюда цену которого вы хотите изменить: ")
            for i in range (g):
                cost = int(input("Введите новую цену: "))
                if menu[i][0] == name:
                    menu[i][2] = cost
                    print("Новая цена блюда ", name, ": ", menu[i][2])
                    break
        elif n == 5:
            name = input("Введите название нового блюда: ")
            flag = 0
            for i in range(n):
                if menu[i][0] == name:
                    print("Такое имя блюда уже существует( Придумайте новое )")
                    flag = 1
                    break
            if flag == 0:
                recipe = list(map(str, input("Введите рецепт нового блюда: ")))
                cost = int(input("Введите цену нового блюда: "))
                menu.append([name, recipe, cost])
                g = len(menu)
        elif n == 6:
            return 0
def task_5():
    matrix_size = list(map(int, input("Введите размер матрицы через пробел: ").split(" ")))
    matrix = matrix_size[0] * [0]
    for i in range(len(matrix)):
        matrix[i] = [0] * matrix_size[1]
    k = 11
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            matrix[i][j] = k
            k += 1
        k += 10 - len(matrix) - 1
    print("Ваша матрица: ")
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            print(matrix[i][j], end=" ")
        print()
    t_matrix = matrix_size[1] * [0]
    for i in range(len(t_matrix)):
        t_matrix[i] = [0] * matrix_size[0]
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            t_matrix[j][i] = matrix[i][j]
    print("Ваша матрица после транспонирования: ")
    for i in range(matrix_size[1]):
        for j in range(matrix_size[0]):
            print(t_matrix[i][j], end=" ")
        print()
def task_6():
    size = int(input("Введите размер КВАДРАТНОЙ матрицы: "))
    matrix = [0] * size
    for i in range(size):
        matrix[i] = list(map(int, input(f"Введите данные стоки {i+1} матрицы через пробел: ").split(" ")))
    for i in range(size):
        PZ = matrix[i][i]
        matrix[i][i] = matrix[size - i - 1][i]
        matrix[size - i - 1][i] = PZ
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print()
def task_7():
    size = list(map(int, input("Введите размер кинотеатра через пробел: ").split(" ")))
    cinema = [0] * size[0]
    random_list = [0, 0, 1]
    for i in range(size[0]):
        cinema[i] = [0] * size[1]
    for i in range(size[0]):
        for j in range(size[1]):
            cinema[i][j] = random.choice(random_list)
    print("Места кинотеатра(1 - занятые, 0 - свободные): ")
    for i in range(size[0]):
        for j in range(size[1]):
            print(cinema[i][j] ,end=" ")
        print()
    line = 1
    number_of_people = int(input("Введите колличетсво человек: "))
    for i in range(size[0]):
        k = 0
        for j in cinema[i]:
            if j == 0:
                k += 1
                if k == number_of_people:
                    print(f"Подходящий ряд: {line}")
                    return 0
            else:
                k = 0
        line += 1
    print("Не нашлось подходящих рядов")
def task_8():
    size = list(map(int, input("Введите размер матрицы через пробел: ").split(" ")))
    matrix = [1] * size[0]
    for i in range(size[0]):
        matrix[i] = [1] * size[1]
    for i in range(1, size[0]):
        for j in range(1, size[1]):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    for i in range(size[0]):
        for j in range(size[1]):
            print(f"{matrix[i][j]: 6.0f}", end=" ")
        print()
def task_9():
    battle_field = ['.'] * 4
    for i in range(4):
        battle_field[i] = ['.'] * 4
    board = ['X'] * 4
    for i in range(4):
        board[i] = ['X'] * 4
    k = 0
    while(k < 4):
        x = random.randrange(0, 4)
        y = random.randrange(0, 4)
        if (board[x][y]) == 'X':
            board[x][y] = 'S'
            k += 1
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()
    guesses = 0
    shots_number = 0
    while 1:
        for i in range(4):
            for j in range(4):
                print(battle_field[i][j], end=" ")
            print()
        try:
            shot = list(map(int, input("Введите координаты выстрела: ").split(" ")))
            x = shot[0] - 1
            y = shot[1] - 1
            if len(shot) != 2:
                print("Неверный формат ввода!(Введите только 2 координаты)")
                continue
            if 0 > x or x > 5 or 0 > y or y > 5:
                print("Неверный формат ввода!(Координаты должны принадлежать промежутку от 0 до 4)")
                continue
            if board[x][y] == 'X':
                print("Промах!")
                battle_field[x][y] = board[x][y]
                shots_number += 1
                continue
            elif board[x][y] == 'S':
                print("Попадение!")
                battle_field[x][y] = board[x][y]
                shots_number += 1
                guesses += 1
            if guesses == 4:
                print("Поздравляем! Вы победили!")
                print(f"Было потрачено {shots_number} выстрелов на уничтожение всех кораблей.")
                return 0
            else:
                continue
        except ValueError:
            print("Неверный формат ввода!(К вводу допускаются только цифры)")
