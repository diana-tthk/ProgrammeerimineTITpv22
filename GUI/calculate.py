from tkinter import *
from tkinter import ttk


def calculate():
    n1 = float(number1.get())
    n2 = float(number2.get())
    res = n1 * n2
    answer = ttk.Label(window, text=str(res))
    answer.place(x=20, y=90)


window = Tk()
window.title("Calculator")
window.geometry("300x150")

labela = ttk.Label(window, text="Number 1")
labela.place(x=5, y=5)
number1 = ttk.Entry(window)
number1.place(x=70, y=5, width=30)

labelb = ttk.Label(window, text="Number 2")
labelb.place(x=125, y=5)
number2 = ttk.Entry(window)
number2.place(x=190, y=5, width=30)

btn = ttk.Button(window, text="Calculate", command=calculate)
btn.place(x=5, y=40, width=150)
label_answer = ttk.Label(window, text="Answer: ")
label_answer.place(x=5, y=70)
window.mainloop()
