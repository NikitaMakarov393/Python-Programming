def find_word_in_file(file, word):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            content = file.read()
            if word in content:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
        return False
def task_1():
    list1 = []
    with (open('file4.txt', 'r', encoding='utf-8') as file):
        for line in file:
            parts = line.rsplit(' ', 1)
            name = parts[0]
            score = int(parts[1])
            list1.append((name, int(score)))
    max_score = max(score for name, score in list1)
    prizer = None
    prizer_score = None
    for name, score in list1:
        if score < max_score:
            if prizer is None or score > prizer_score:
                prizer = name
                prizer_score = score
    if prizer:
        print(f'Призер: {prizer} с баллами {prizer_score}')
    else:
        print('Нет призеров.')
def task_2():
    if find_word_in_file('file5.txt','Academy'):
        print("Слово Academy найдено в файле file5.txt")
    elif find_word_in_file('file5.txt','Academy'):
        print("Слово Academy найдено в файле file6.txt")
    else:
        print("Слово не найдено в данных файлах")
def task_3():
    main_counter = 0
    e_counter = 0
    with (open('file3.txt', 'r', encoding='utf-8') as file):
        for word in file:
            for x in range(len(word)):
                main_counter += 1
                if word[x] == 'е':
                    e_counter += 1
    print(f"Процент слов с буквой е: {(e_counter / main_counter * 100):.2f} %")
def task_4():
    try:
        a = int(input("Введите количество имен: "))
    except ValueError:
        print("Неверный формат ввода:")
    while 1:
        b = input("Введите нужный пол (м - мужской, ж - женский): ")
        if b != 'м' and b != 'ж':
            print("Введите м или ж")
            continue
        else:
            break
    if b == 'м':
        file = 'file8.txt'
    else:
        file = 'file7.txt'
    names = []
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            for line in file:
                name, percentage = line.strip().split()
                names.append((name, int(percentage)))
    names.sort(key=lambda x: x[1], reverse=True)
    names = names[:a]
    if b == 'м':
        print("Популярные мужские имена: ", end = '')
    else:
        print("Популярные женские имена: ", end = '')
    for x in names:
        print(x[0])
def task_5():
    with open('file9.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        middle = len(lines) // 2
        print("Введите текст который хотите добавить в файл")
        text = input()
        lines.insert(middle, text + '\n')
    with open('file9.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)
def task_8():
    while 1:
        try:
            n = list(map(int, input("Введите размер матрицы-змейки через пробел(3<=n,m<=50): ").split(" ")))
            if len(n) != 2:
                print("Неверный формат ввода!")
                continue
            elif 3 > n[0] or n[0] > 50 or 3 > n[1] or n[1] > 50:
                print("Неверный формат ввода!")
                continue
            else:
                break
        except ValueError:
            print("Неверный формат ввода!")
    snake_matrix = ['#'] * n[0]
    for i in range(n[0]):
        snake_matrix[i] = ['#'] * n[1]
    for i in range(n[0]):
        if i % 4 == 1:
            for j in range(n[1]-1):
                snake_matrix[i][j] = [' ']
        elif i % 4 == 3:
            for j in range(1, n[1]):
                snake_matrix[i][j] = [' ']
    for i in range(n[0]):
        for j in range(n[1]):
            print(*snake_matrix[i][j], end="")
        print()
task_5()