# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except
try:
    num = float(input("Введите число"))
except ValueError:
    print("Похоже, это не число!")

# обработка исключений нескольких разных типов
print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже, это не число!")

# Другой вариант обработки исключений
print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError:
        print("Я умею преобразовывать только строки, составленные из цифр!")

# получение аргумента
print()
try:
    num = float(input("\nВведите число: "))
except ValueError as e:
    print("Это не число!")
    print(e)

# try/except/else
try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Это не число!")
else:
    print("Вы введи число ", num)

input("Press the enter key to exit!")