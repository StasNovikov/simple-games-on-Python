# моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться
class Critter(object):
    """ Виртуальный питомец """
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "Неплохо"
        elif 11 <= unhappiness <= 15:
            m = "Не сказать чтобы хорошо"
        else:
            m = "Ужасно"
        return m

    def talk(self):
        print("Меня зовут ", self.name, " и сейчас я чувстую себя ", self.mood, "\n")
        self.__pass_time()


    def eat(self, food = 4):
        print("Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("=)")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как вы назовёте свою зверюшку?: ")
    crit = Critter(crit_name)

    choise = None
    while choise != "0":
        print(
            """
            Мой питомец
            0 - Выйти
            1 - Узнать о самочувствии
            2 - Покормить питомца
            3 - Поиграть с питомцем
            """
        )

        choise = input("Ваш выбор: ")
        print()
        if choise == "0":
            print("До свидания.")
        elif choise == "1":
            crit.talk()
        elif choise == "2":
            crit.eat()
        elif choise == "3":
            crit.play()
        else:
            print("Извините, в меню нет такого пункта")

# Запуск игры
main()
input("\nPress the Enter key to exit")