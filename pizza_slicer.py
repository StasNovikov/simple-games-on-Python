# Резчик пиццы
# Демонстрирует срезы строки

word = "пицца"

print(
    """
    Памятка
    0   1   2   3   4   5
    +---+---+---+---+---+
    | п | и | ц | ц | а |
    +---+---+---+---+---+
   -5  -4  -3  -2  -1   0
    """
)

print("Введите начальный и конечный индексы для того среза 'пиццы', который хотите получит.")
print("Для выхода нажмите Enter, не вводя начальную позицию")

start = None
while start != "":
    start = input("\nНачальная позиция: ")
    if start:
        start = int(start)
        finish = int(input("Конечная позиция: "))
        print("Срез word[", start, ":", finish, "] выглядит как ", word[start:finish])
input("\nPress the enter key to exit")