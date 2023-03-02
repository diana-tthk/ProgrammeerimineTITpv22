# Kirjutage programm, mis küsib kasutajalt '
# positiivse täisarvu ning kontrollib,
# kas sisestatud tekst on numbriline.
# Kui jah, siis kuvatakse antud arvu ruut,
# vastasel juhul kuvatakse veatead.
from tkinter import *
from tkinter import messagebox

def is_number(num):
    #    if type(num) == int or type(num) == float:
    #       return True
    #    else:
    #        return False
    try:
        int(num)
        return True
    except:
        return False


def calculate():
    answer.config(text="")
    num = number.get()
    if is_number(num):
        num = int(num)
        sq = num * num
        answer.config(text=str(sq))
    else:
        messagebox.showinfo(message="Error: Please enter a number!")


window = Tk()
window.title("Square with check")
window.geometry("350x150")

question = Label(window, text="Please enter a positive number:")
question.place(x=5, y=5)

number = Entry(window)
number.place(x=100, y=40, width=150)

btn = Button(window, text="Calculate square!", command=calculate)
btn.place(x=100, y=75, width=150)

answer = Label(window, text="")
answer.place(x=160, y=110)

window.mainloop()
