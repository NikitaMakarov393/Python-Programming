import random
import string
def task_7():

    length = int(input("Введите длину пароля: "))
    a = input("Нужны ли заглавные буквы (да/нет): ").strip().lower()
    b = input("Нужны ли строчные буквы (да/нет): ").strip().lower()
    c = input("Нужны ли цифры (да/нет): ").strip().lower()
    d = input("Нужны ли специальные символы (да/нет): ").strip().lower()
    if a != "да" and b != "да" and c != "да" and d != "да":
        print("Ошибка: Выберите хотя бы один тип символов для генерации пароля.")
    else:
        characters = ""
        if a == "да":
            characters += string.ascii_uppercase
        if b == "да":
            characters += string.ascii_lowercase
        if c == "да":
            characters += string.digits
        if d == "да":
            characters += string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Ваш пароль: ", password)
def task_8():
    print("Введите команды и счет ( в формате команда 1-команда 2 счет )\n")
    a = input("").split("-")
    team_1 = a[0]
    team_2_score = a[1].split(" ")
    score = team_2_score[1].split(":")
    score_1 = int(score[0])
    score_2 = int(score[1])
    team_2 = team_2_score[0]
    if score_1 == score_2:
        print("Ничья")
    elif score_1 < score_2:
        print(team_2)
    else:
        print(team_1)
