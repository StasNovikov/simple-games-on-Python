# Счётчик нажатий
# Демонстрирует связывание событий с обработчиками
from tkinter import *

class Application(Frame):
    """ GUI-приложение, которое подсчитывает количество нажатий кнопки """
    def __init__(self, master):
        """ Инициализирует рамку """
        super(Application, self).__init__(master)
        self.grid()
        # кол-во нажатий
        self.btn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        """ Создает кнопку, на которой отображается количество совершённых нажатий """
        self.btn = Button(self)
        self.btn["text"] = "Количество щелчков: 0"
        self.btn["command"] = self.update_count
        self.btn.grid()

    def update_count(self):
        """ Увеличивает количество нажатий кнопки на единицу и отображает его """
        self.btn_clicks += 1
        self.btn["text"] = "Количество щелчков: " + str(self.btn_clicks)

# основная часть
root = Tk()
root.title("Количество нажатий")
root.geometry("300x250")
app = Application(root)
root.mainloop()