import PySimpleGUI as sg
import random
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
def task_3():
    c_image = [[sg.Image("bio.png")]]
    c_input = [
        [sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
        [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
        [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
        [sg.Button("Рассчитать", font="Arial 20")]]

    layout = [
        [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
    ]

    window = sg.Window("Калькулятор бактерий", layout)

    while 1:

        event, value = window.read()

        if event == sg.WIN_CLOSED:
            break

        micro = int(value["micro"])
        count = int(value["count"])

        for x in range(count):
            b = random.randint(0, 4)
            micro = 2 * micro + b

        if event == "Рассчитать":
            window["res"].update(micro)

    window.close()
def task_choise():
    while 1:
        try:
            a = int(input("Введите номер задания: "))
            if a < 1 or a > 4:
                print("К вводу допускаются цифры в промежутке от 1 до 4")
                continue
            else:
                break
        except ValueError:
            print('К вводу допускаются только цифры')
    if a == 1:
        task_1()
    elif a == 2:
        task_2()
    elif a == 3:
        task_3()
task_choise()