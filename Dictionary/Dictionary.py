import PySimpleGUI as pg
import random
def task_1():
    keypad = {
        '1': '.,?!:',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '
    }
    message = input("Введите текст: ")
    message = message.lower()
    result = []
    for char in message:
        for key, chars in keypad.items():
            if char in chars:
                presses = chars.index(char) + 1
                result.append(key * presses)
                break
    keys = ''.join(result)
    print(keys)
def task_2():
    letters = {
        '1': 'AEILNORSTU',
        '2': 'DG',
        '3': 'BCMP',
        '4': 'FHVWY',
        '5': 'K',
        '8': 'JX',
        '10': 'QZ'
    }
    word = input('Введите слово: ').upper()
    result = 0
    for char in word:
        for key, chars in letters.items():
            if char in chars:
                result += int(key)
    print(result)
def task_3():
    emails = {'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
    'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
    'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
    'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
    'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']
    }
    for key, chars in emails.items():
        for x in range(len(chars)):
            print(chars[x] + '@' + key)
def task_4():
    image = [[pg.Image("cubes.png", background_color='Black')]]
    input = [
        [pg.Text("Введите наименьшее число диапазона"), pg.Input(size=(10, 0), key="minimum")],
        [pg.Text("Введите наибольшее число диапазона"), pg.Input(size=(10, 0), key="maximum")],
        [pg.Text("Рандомное число вашего диапазона"),pg.Input(size=(10, 0), key="random", readonly=True)],
        [pg.Button("Рассчитать", font='Arial 20')]
    ]


    layout = [
        [pg.Column(image),pg.Column(input, justification='right')]
    ]
    pg.theme("Black")

    window = pg.Window('Randomizer', layout)


    while True:
        event, value = window.read()


        if event == pg.WIN_CLOSED:
            break


        if event == "Рассчитать":

            try:
                minimum = int(value["minimum"])
                maximum = int(value["maximum"])
                number = random.randint(minimum, maximum)
                window["random"].update(number)
            except ValueError:
                pg.popup("Пожалуйста введите корректное числовое значение")


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
    elif a == 4:
        task_4()

task_choise()