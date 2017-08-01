# Простейший GUI
# Демонстрирует создание окна
from tkinter import *

# создание окна
root = Tk()

# изменение окна
root.title("Простейший GUI")
root.geometry("200x100")

# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()

# создание метки внутри рамки
lbl = Label(app, text="Тестовая метка")
lbl.grid()

# создание первой кнопки внутри рамки
btn1 = Button(app, text="Ничего не делаю!")
btn1.grid()

# создание второй кнопки внутри рамки
btn2 = Button(app)
btn2.grid()
btn2.configure(text="И я тоже")

# создание третьей кнопки внутри рамки
btn3 = Button(app)
btn3.grid()
btn3["text"] = "И я!"

# старт событийного цикла
root.mainloop()