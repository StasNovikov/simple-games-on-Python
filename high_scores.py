# Рекорды
# Демонстрирует списочные методы
scores = []
choice = None

while choice != "0":
    print(
        """

        Рекорды
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        3 - Удалить рекорд
        4 - Сортировать список
        """
    )

    choice = input("Ваш выбор: ")
    print()

    # Выход
    if choice == "0":
        print("До свидания")
    # вывод лучших результатов на экран
    elif choice == "1":
        for score in scores:
            print(score)
    # Добавление рекорда
    elif choice == "2":
        score = int(input("Впишите свой рекорд: "))
        scores.append(score)
    # Удаление рекорда
    elif choice == "3":
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат ", score, " не содержится в списке рекордов.")
    # Сортировка рекордов
    elif choice == "4":
        scores.sort(reverse=True)
        print(scores)
    # Непонятный пользовательский ввод
    else:
        print("Извините, в меню нет выбранного пункта ", choice)

input("\nPress the Enter key to exit")