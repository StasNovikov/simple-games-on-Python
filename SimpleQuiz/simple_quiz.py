# Викторина
# Игра на выбор правильного варианта ответа,
# вопросы которой читаются из текстового файла
import sys

def open_file(file_name, mode):
    """ Открывает файл """
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл ", file_name, ". Работа программы будет завершена.\n", e)
        input("\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """ Возвращает в отформатированном виде очередную строку игрового файла """
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    """ Возвращает очередной блок данных из игрового файла """
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = int(next_line(the_file))
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """ Приветствует игрока и сообщает тему игры. """
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")


def main():
    trivia_file = open_file("trivia.txt","r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # извлечение первого блока
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # вывод на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, " - ", answers[i])

        # получение ответа
        answer = int(input("Ваш ответ: "))
        if answer == correct:
            print("\nДа")
            score += 1
        else:
            print("\nНет")

        print("\n",explanation)
        print("Счет: ", score, "\n\n")

        # переход к следующему вопросу
        try:
            category, question, answers, correct, explanation = next_block(trivia_file)
        except ValueError:
            category = ""

    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашем счету ", score, " очк(а/ов)")

main()

input("Нажмите Enter, чтобы выйти.")