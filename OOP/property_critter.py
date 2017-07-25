# Демонстрирует работу со свойствами
class Critter(object):
    """ Виртуальный питомец """
    def __init__(self, name):
        print("Появилась на свет новая зверюшка")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки на может быть пустой строкой")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("\nПривет! Меня зовут ", self.name)

# основная часть
crit = Critter("Бобик")
crit.talk()

print("Мою зверюшку зовут ", end=" ")
print(crit.name)

print("Пытаюсь изменить имя на - 'Джекки'")
crit.name = "Джекки"

print("Мою зверюшку зовут ", end=" ")
print(crit.name)

print("Пытаюсь изменить имя на пустую строку")
crit.name = ""

print("Мою зверюшку зовут ", end=" ")
print(crit.name)

input("\nНажмите Enter, чтобы выйти!")