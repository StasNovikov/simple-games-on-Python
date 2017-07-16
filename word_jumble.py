# Анаграммы (Word Jumble)
#
# Компьютер выбирает какое-либо слово и хаотически переставляет его буквы
# Задача игрока - восстановить исходное слово
import random

# Создадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "догадка")

# Случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
correct = word

# создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# начало игры
print(
    """
       Добро пожаловать в игру 'Анаграммы'
      Надо перествавить буквы так, чтобы получилось осмысленное слово
    (Для выхода нажмите Enter, не вводя своей версии.)
    """
)
print("Вот анаграмма: ", jumble)

guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != "" and guess != correct:
    print("К сожалению, Вы неправы!")
    guess = input("Попробуйте отгадать исходное слово: ")

if guess == correct:
    print("Да, именно так!")

print("Спасибо за игру!")

input("Press the enter key to exit")