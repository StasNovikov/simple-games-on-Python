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