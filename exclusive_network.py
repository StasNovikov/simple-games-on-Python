# Эксклюзивная сеть
# Демонстрирует составные условия и логические операторы
print("\tЭксклюзивная компьютерная сеть")
print("\tТолько для зареистрированных пользователей!\n")
security = 0
username = ""
password = ""
# Для того чтобы исключить ввод пустой строки, используем конструкцию while not
while not username:
    username = input("Логин: ")
while not password:
    password = input("Пароль: ")
if username == "M.Dawson" and password == "secret":
    print("Привет, Майк.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Здравствуй, Сид")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("Доброго времени суток, Сигеру.")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("Как дела, Уилл?")
    security = 3
elif username == "guest" or password == "guest":
    print("Добро пожаловать к нам в гости!")
    security = 1
else:
    print("Не удалось войти в систему. Должно быть, Вы не очень-то эксклюзивный гражданин.\n")
input("Press the enter key to exit.")