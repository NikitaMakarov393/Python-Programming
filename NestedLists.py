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
    n = int(input("Количество сокровищ: "))
    treasure_map = [0] * n
    for i in range(n):
        treasure_map[i] = list(map(int, input(f"Введите координаты {i + 1} сокровища через пробел: ").split()))
    Sasha_position = list(map(int, input("Введите координаты Саши через пробел: ").split()))
    if len(Sasha_position) != 2:
        print("Неверный формат ввода координат Саши!")
        return
    closest_treasure = str(distance_func(treasure_map, Sasha_position, n))

    print(f"Ближайшее сокровище находится по координатам: {"".join(closest_treasure)}")