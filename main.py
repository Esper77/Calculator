from tkinter import *

window = Tk()

text = StringVar()
numbers = StringVar()

label = Label(window, text="Введите выражение", width=25, height=5)
label.pack()

def summ():
    text.set("Результат вычислений: " + str(eval(numbers.get())))


entry = Entry(window, textvariable=numbers)
entry.pack()

label = Label(window, textvariable=text, width=25, height=5)
label.pack()

window.title("Калькулятор")

# Добавляем кнопки
Button(window, text="1", width=10, height=5).grid(row=0, column=0)
Button(window, text="2", width=10, height=5).grid(row=0, column=1)
Button(window, text="3", width=10, height=5).grid(row=0, column=2)
Button(window, text="4", width=10, height=5).grid(row=1, column=0)
Button(window, text="5", width=10, height=5).grid(row=1, column=1)
Button(window, text="6", width=10, height=5).grid(row=1, column=2)
Button(window, text="7", width=10, height=5).grid(row=2, column=0)
Button(window, text="8", width=10, height=5).grid(row=2, column=1)
Button(window, text="9", width=10, height=5).grid(row=2, column=2)
Button(window, text=, command=summ)
Button(window, text="0", width=10, height=5).grid(row=3, column=1)

mainloop()

window.mainloop()