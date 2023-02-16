from tkinter import *

input_value = ""


def press(num):
    return


def equals():
    return


def clear():
    return


window = Tk()
window.title("Calculator App")
window.geometry("312x324")
window.resizable(0, 0)
window.configure(background="grey")

display_text = StringVar()
expression_field = Entry(window, textvariable=display_text)
expression_field.grid(columnspan=4, ipadx=100)

button1 = Button(window, text=' 1 ', fg='white', bg='black',
                 command=lambda: press(1), height=4, width=10)
button1.grid(row=2, column=0)
button2 = Button(window, text=' 2 ', fg='white', bg='black',
                 command=lambda: press(2), height=4, width=10)
button2.grid(row=2, column=1)
button3 = Button(window, text=' 3 ', fg='white', bg='black',
                 command=lambda: press(3), height=4, width=10)
button3.grid(row=2, column=2)

button_plus = Button(window, text=' + ', fg='white', bg='black',
                     command=lambda: press("+"), height=4, width=10)
button_plus.grid(row=2, column=3)

window.mainloop()
