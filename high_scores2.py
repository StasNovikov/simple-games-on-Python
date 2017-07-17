# Рекорды 2.0
# Демонстрирует вложенные последовательности
scores = []
choise = None
while choise != "0":
    print(
        """
        Рекорды 2.0
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорды
        """
    )

    choise = input("Ваш выбор: ")
    print()

    # выход
    if choise == "0":
        print("До свидания")
    # вывод таблицы рекордов
    elif choise == "1":
        print("Рекорды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    # добавление рекорда
    elif choise == "2":
        name = input("Введите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score,name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] # в списке остается только 5 рекордов
    else:
       print("Извините, в меню нет пункта ", choise)

input("Press the Enter key to exit")