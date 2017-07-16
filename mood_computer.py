# Компьютерный датчик настроения
# Демонстрирует работу условного оператора if: ... elif: ... else:
import random
print("Я ощущаю Вашу энергетику. От моего экрана не скрыто ни одно из Ваших чувств.")
print("Итак. Ваше настроение...")
mood = random.randint(1,3)
if mood == 1:
    # радостное
    print(
        """
        ___________
        |          |
        | O     O  |
        |    <     |
        |  ,    ,  |
        |   ...    |
        |__________|
        """
    )
elif mood == 2:
    # так себе
    print(
        """
        ___________
        |          |
        | O     O  |
        |    <     |
        |          |
        |   .....  |
        |__________|
        """
    )
elif mood == 3:
    # прескверное
    print(
        """
        ___________
        |          |
        | O     O  |
        |    <     |
        |    ..    |
        |  ..  ..  |
        |__________|
        """
    )
else:
    print("Не бывает такого настроения! (Должно быть, Вы совершенно не в себе.)")
    print("...Но это только сегодня.")
    input("\n\nPress the enter key to exit.")