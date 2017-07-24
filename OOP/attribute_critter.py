# Зверюшка с атрибутами
# Демонстрирует создание атрибутов объекта и доступ к ним
class Critter(object):
    """ Виртуальный питомец """

    def __init__(self, name):
        print("Появилась новая зверюшка!")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep

    def talk(self):
        print("Привет! Меня зовут ", self.name, "\n")

# Основная часть
crit1 = Critter("Бобик")
crit1.talk()
crit2 = Critter("Манька")
crit2.talk()
print("Вывод объекта crit1 на экран")
print(crit1)
print("\nВывод объекта crit2 на экран")
print(crit2)
print("\nНепосредственный доступ к атрибуту crit1.name")
print(crit1.name)
input("\nPress the Enter key to exit")