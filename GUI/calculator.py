from tkinter import *

input_value = ""


# Function to update expression in the text entry box
def press(num):
    # point out the global expression variable
    global input_value
    input_value = input_value + str(num)

    # update the expression by using set method
    display_text.set(input_value)


# Function to evaluate the final expression
def equals():
    # Try and except statement is used
    # for handling errors like zero division etc.

    # Put that code inside the try block
    # that may generate the error
    try:
        global input_value
        total = str(eval(input_value))
        display_text.set(total)
        input_value = ""
        # If error is generated, then handle it
    # by the except block
    except:
        display_text.set(" error ")
        input_value = ""


# Function to clear the contents of text entry box
def clear():
    global input_value
    input_value = ""
    display_text.set(input_value)


window = Tk()
window.title("Calculator App")
window.geometry("312x324")
window.resizable(0, 0)
window.configure(background="grey")

display_text = StringVar()
expression_field = Entry(window, textvariable=display_text)
expression_field.grid(columnspan=4, ipadx=100, ipady=15)

button1 = Button(window, text=' 1 ', fg='white', bg='black',
                 command=lambda: press(1), height=4, width=10)
button1.grid(row=2, column=0)
button2 = Button(window, text=' 2 ', fg='white', bg='black',
                 command=lambda: press(2), height=4, width=10)
button2.grid(row=2, column=1)
button3 = Button(window, text=' 3 ', fg='white', bg='black',
                 command=lambda: press(3), height=4, width=10)
button3.grid(row=2, column=2)

button4 = Button(window, text=' 4 ', fg='white', bg='black',
                 command=lambda: press(4), height=4, width=10)
button4.grid(row=3, column=0)
button5 = Button(window, text=' 5 ', fg='white', bg='black',
                 command=lambda: press(5), height=4, width=10)
button5.grid(row=3, column=1)
button6 = Button(window, text=' 6 ', fg='white', bg='black',
                 command=lambda: press(6), height=4, width=10)
button6.grid(row=3, column=2)

button7 = Button(window, text=' 7 ', fg='white', bg='black',
                 command=lambda: press(7), height=4, width=10)
button7.grid(row=4, column=0)
button8 = Button(window, text=' 8 ', fg='white', bg='black',
                 command=lambda: press(8), height=4, width=10)
button8.grid(row=4, column=1)
button9 = Button(window, text=' 9 ', fg='white', bg='black',
                 command=lambda: press(9), height=4, width=10)
button9.grid(row=4, column=2)

button0 = Button(window, text=' 0 ', fg='white', bg='black',
                 command=lambda: press(0), height=4, width=10)
button0.grid(row=5, column=0)

button_plus = Button(window, text=' + ', fg='white', bg='black',
                     command=lambda: press("+"), height=4, width=10)
button_plus.grid(row=2, column=3)

button_minus = Button(window, text=' - ', fg='white', bg='black',
                      command=lambda: press("-"), height=4, width=10)
button_minus.grid(row=3, column=3)

button_mult = Button(window, text=' * ', fg='white', bg='black',
                     command=lambda: press("*"), height=4, width=10)
button_mult.grid(row=4, column=3)

button_div = Button(window, text=' / ', fg='white', bg='black',
                    command=lambda: press("/"), height=4, width=10)
button_div.grid(row=5, column=3)

button_clear = Button(window, text=' CL ', fg='white', bg='black',
                      command=clear, height=4, width=10)
button_clear.grid(row=5, column=1)
button_eq = Button(window, text=' = ', fg='white', bg='black',
                   command=equals, height=4, width=10)
button_eq.grid(row=5, column=2)

window.mainloop()
