def is_valid_dialog(messages):
    questions = 0
    answers = 0
    for x in range(len(messages)):
        if messages[x] == 'q':
            questions += 1
        elif messages[x] == 'a':
            answers += 1
    return questions == answers
def task_1():
    n = int(input("Введите количество членов экипажа: "))
    crew = []
    for x in range(n):
        name, status = input().split()
        crew.append((name, status))
    women_children = []
    men = []
    captain = None
    for name, status in crew:
        if status == "woman" or status == "child":
            women_children.append((name))
        elif status == "man":
            men.append((name))
        elif status == "captain":
            captain = (name)
    order = women_children + men
    if captain:
        order.append(captain)
    for member in order:
        print(member[0])
def task_2():
    a = "qa"
    n = int(input("Введите количество сообщений: "))
    while 1:
        messages = input('Введите вопросы и ответы: ').lower()
        for x in range(len(messages)):
            if messages[x] not in a:
                print('К вводу допускаются только q и a')
                continue
        if n == len(messages):
            break
    if is_valid_dialog(messages):
        print("+")
    else:
        print("-")
