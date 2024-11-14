import random
def task_1():
    task1_list = list(map(str, input("Введите данные списка через пробел: ").split(" ")))
    print("Ваш список: ", task1_list, end="\n")
    digits_list = []
    letters_list = []
    for element in task1_list:
        if element.isalpha():
            letters_list.append(element)
        if element.isdigit():
            digits_list.append(element)
    del task1_list
    print("Буквы: ", letters_list, end="\n")
    print("Цифры: ", digits_list, end="\n")
def task_2():
    random_number_list = []
    t = 0
    for x in range(6):
        random_number_list.append(random.randrange(1, 50))
    print("Выигрышный билет: ", random_number_list)
def task_3():
    task3_list = list(map(int, input("Введите список чисел через пробел: ").split(" ")))
    task3_list_2 = []
    print("Ваш список: ", task3_list, end="\n")
    for x in range(1, len(task3_list)):
        if task3_list[x] > task3_list[x-1]:
            task3_list_2.append(task3_list[x])
    print("Числа которые больше предыдущего: ", task3_list_2, end="\n")
def task_4():
    task4_list = list(map(int, input("Введите числа списка через пробел: ").split(" ")))
    sred = 0
    lower_numbers = []
    bigger_numbers = []
    for x in range(len(task4_list)):
        sred += task4_list[x]
    sred /= len(task4_list)
    print("Среднее арифметическое чисел списка: ", sred, end="\n")
    for x in range (len(task4_list)):
        if task4_list[x] <= sred:
            lower_numbers.append(task4_list[x])
        else:
            bigger_numbers.append(task4_list[x])
    print("Числа меньшие либо равные среднему арифметическому: ", lower_numbers)
    print("Числа большие среднего арифметического: ", bigger_numbers)
def task_5():
    task5_list = list(map(int, input("Введите список роста каждого человека строя через пробел: ").split(" ")))
    rost_Andreya = int(input("Введите рост Андрея: "))
    task5_list.append(rost_Andreya)
    nomer_Andreya = len(task5_list)
    sorted_list = sorted(task5_list, reverse = True)
    for x in range (len(task5_list)-1, -1, -1):
        if rost_Andreya > sorted_list[x]:
            nomer_Andreya -= 1
        else:
            break
    print(sorted_list)
    print("Номер андрея в списке: ", nomer_Andreya)
def task_6():
    consecutive_heads = 0
    consecutive_tails = 0
    task6_list =[]
    while consecutive_heads < 3 and consecutive_tails < 3:
        toss = random.choice(['О', 'Р'])
        task6_list.append(toss)
        if toss == 'О':
            consecutive_heads += 1
            consecutive_tails = 0
        else:
            consecutive_tails += 1
            consecutive_heads = 0

    print(task6_list,f"(попыток: {len(task6_list)})")
def task_7():
    card_number = list(map(int, input("Введите номер карты: ")))
    chet_summ = 0
    nech_summ = 0
    for x in range(1,len(card_number), 2):
        chet_summ += card_number[x]
    for x in range(0, len(card_number), 2):
        if card_number[x] * 2 > 9:
            nech_summ +=card_number[x] * 2 - 9
        else:
            nech_summ += card_number[x] * 2
    if (nech_summ + chet_summ) % 10 == 0:
        print("Корректный номер!")
    else:
        print("Некорректный номер!")
def task_8():
    def main():
        task8_list = list(map(str, input("Введите слово: ")))
        for x in task8_list:
            if x.isdigit():
                print("Это не слово!")
                return 0
        if len(task8_list) > 10:
            print(f"Ваше слово :{task8_list[0]}{len(task8_list) - 2}{task8_list[len(task8_list) - 1]}")
        else:
            print(f"Ваше слово: {''.join(task8_list)} ")
    main()
def task_9():
    k = 0
    n = int(input("Введите число комнат: "))
    while n > 0:
        room =list(map(int, input("Введите колличество человек проживающих в комнате и их допустимое число через пробел: ").split(" ")))
        if len(room) > 2:
            print("Ошибка! Недопустимый формат ввода.")
            return 0
        elif room[0] > room[1]:
            print("Ошибка! Колличество человек проживающих в комнате больше допустимого колличества.")
            return 0
        if room[1] - room[0] == 2:
            k += 1
        n -= 1
    print(f"Колличество комнат подхонящих для заселения Юры и Коли: {k}")