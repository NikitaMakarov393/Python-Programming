# 1 Вариант работы на 4
while 1:
    print("-" * 2, "ТЕЛЕФОННАЯ КНИЖКА", "-" * 2)
    print("1 - Добавить контакт")
    print("2 - Удалить контакт")
    print("3 - Изменить контакт")
    print("4 - Поиск контакта")
    print("5 - Вывод телефонной книжки")
    print("6 - Выход")
    print("-" * 22)
    choise = int(input('Выберите номер действия: '))
    if choise < 1 or choise > 5:
        continue
    if choise == 1:
        name = input("Введите имя: ")
        try:
            number = int(input("Введите номер телефона: "))
        except ValueError:
            print('Номер телефона должен содержать только цифры')
            continue
        with open('Телефонная книжка.txt', 'a') as file:
            file.write(f"{name} {number}\n")
        print("Контакт добавлен!")
    if choise == 2:
        name_to_delete = input("Введите имя контакта для удаления: ")
        contacts = []
        with open('Телефонная книжка.txt', 'r') as file:
            contacts = file.readlines()
        found = False
        with open('Телефонная книжка.txt', 'w') as file:
            for contact in contacts:
                name, phone = contact.strip().split(' ', 1)
                if name != name_to_delete:
                    file.write(contact)
                else:
                    found = True
    if choise == 3:
        name_to_edit = input("Введите имя контакта для изменения: ")
        contacts = []

        with open('Телефонная книжка.txt', 'r') as file:
            contacts = file.readlines()

        found = False
        with open('Телефонная книжка.txt', 'w') as file:
            for contact in contacts:
                name, phone = contact.strip().split(' ', 1)
                if name == name_to_edit:
                    new_name = input("Введите новое имя: ")
                    new_phone = input("Введите новый номер телефона: ")
                    file.write(f"{new_name} {new_phone}\n")
                    found = True
                    print("Контакт изменён!")
                else:
                    file.write(contact)

        if not found:
            print("Контакт не найден!")
    if choise == 4:
        name_to_search = input("Введите имя контакта для поиска: ")
        found = False

        with open('Телефонная книжка.txt', 'r') as file:
            for line in file:
                name, phone = line.strip().split(' ', 1)
                if name == name_to_search:
                    print(f"Имя: {name}, Телефон: {phone}")
                    found = True

        if not found:
            print("Контакт не найден!")
    if choise == 5:
        print("\nСписок контактов:")
        with open('Телефонная книжка.txt', 'r') as file:
            contacts = file.readlines()
            if not contacts:
                print("Контактов нет.")
                exit()
            for contact in contacts:
                name, phone = contact.strip().split(' ', 1)
                print(f"Имя: {name}, Телефон: {phone}")
    if choise == 6:
        break
