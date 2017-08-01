# Демонстрирует создание класса в оконном приложении на основе tkinter
from tkinter import *

class Application(Frame):
    """ GUI-приложение с тремя кнопками """

    def __init__(self, master):
        """ Инициализирует рамку """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создание кнопок """
        # первая кнопка
        self.btn1 = Button(self, text="Я ничего не делаю!")
        self.btn1.grid()
        # вторая кнопка
        self.btn2 = Button(self)
        self.btn2.grid()
        self.btn2.configure(text="И я тоже!")
        # третья кнопка
        self.btn3 = Button(self)
        self.btn3.grid()
        self.btn3["text"] = "И я!"

# основная часть
root = Tk()
root.title("Работа с кнопками")
root.geometry("200x150")

app = Application(root)

root.mainloop()