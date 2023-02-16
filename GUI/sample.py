from tkinter import *
from tkinter import ttk, messagebox


def greet():
    greeting = "Hello, " + name.get()
    # label2 = ttk.Label(root, text=greeting)
    # label2.place(x=70, y=70)
    messagebox.showinfo(message=greeting)


root = Tk()
root.title("Greeter")
root.geometry("300x100")

label = ttk.Label(root, text="Name")
label.place(x=5, y=5)

name = ttk.Entry(root)
name.place(x=70, y=5, width=150)

btn = ttk.Button(root, text="Greet!", command=greet)
btn.place(x=70, y=40, width=150)

root.mainloop()
