# Арсенал героя 2.0
# Демонстрирует работу с кортежами
# Создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory = (
    "меч",
    "кольчуга",
    "щит",
    "целебное снадобье"
)

print("\nИтак, в Вашем арсенале: ")
for item in inventory:
    print(item)
input("\nPress the enter key to exit")

#найдем длину кортежа
print("\nСейчас в Вашем распоряжении ", len(inventory), " предмета/-ов.")
input("\nPress the enter key to exit")

# Вывод одного предмета с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом ", index, " в арсенале находится ", inventory[index])

# отобразим срез
start = int(input("\nВведите начальный индекс среза: "))
finish = int(input("\nВведите конечный индекс среза: "))
print("Срез inventory[", start, ":", finish, "] - это ", inventory[start:finish])
input("\nPress the enter key to exit")

# соединим два кортежа
chest = ("золото", "драгоценные камни")
print("Вы нашди ларец. Его содержимое: ", chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении: ")
print(inventory)
input("\nPress the enter key to exit")