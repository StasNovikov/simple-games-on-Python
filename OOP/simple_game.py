# Простая игра
# Демонстрирует импорт модулей
import games, random
print("Добро пожаловать в самую простую игру!\n")
again = None
while again != "n":
    players = []
    num = games.ask_number(question = "Сколько игроков участвует? (2-5): ", low = 2, high = 5)

    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)

    print("\nВот результаты игры: ")
    for player in players:
        print(player)

    again = games.ask_yes_no("\nХотите сыграть ещё раз? (y/n): ")
input("\nPress the enter key to exit")