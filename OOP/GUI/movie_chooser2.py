# киноман-2
# Демонстрирует переключатель
from tkinter import *

class Application(Frame):
    """ GUI-приложение, позволяющее выбрать один любимый жанр кино """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает элементы, с помощью которых пользователь будет выбирать """
        # Метка описание
        Label(self, text="Укажите ваш любимый жанр кино").grid(row=0, column=0, sticky=W)
        # Метка-инструкиця
        Label(self, text="Выберите ровно один:").grid(row=1, column=0, sticky=W)
        # переменная для хранения сведений о единственном любимом жанре
        self.favorite = StringVar()
        self.favorite.set(None)
        # положение "Комедия" переключателя
        Radiobutton(self, text="Комедия", variable=self.favorite, value="комедия.", command=self.update_text).grid(
            row=2, column=0, sticky=W)
        # положение "Драма" переключателя
        Radiobutton(self, text="Драма", variable=self.favorite, value="драма.", command=self.update_text).grid(
            row=3, column=0, sticky=W)
        # положение "Кино о любви" переключателя
        Radiobutton(self, text="Кино о любви", variable=self.favorite, value="кино о любви.", command=self.update_text).grid(
            row=4, column=0, sticky=W)
        # текстовая область с результатами
        self.resut_text = Text(self, width=40, height=5, wrap=WORD)
        self.resut_text.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """ Обновляя текстовую область, вписывает в нее любимый жанр """
        message = "Ваш любимый киножанр: "
        message += self.favorite.get()
        self.resut_text.delete(0.0, END)
        self.resut_text.insert(0.0, message)

# Основная частт
root = Tk()
root.title("Киноман-2")
root.geometry("350x150")
app = Application(root)
root.mainloop()