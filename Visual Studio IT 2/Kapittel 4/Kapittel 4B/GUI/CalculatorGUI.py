from tkinter import *
from tkinter import ttk


def gange():
    try:
        svar = float(tall_1.get()) * float(tall_2.get())
    except ValueError:
        tall_1.delete(0, END)
        tall_2.delete(0, END)
        resultat.configure(text="")
    else:
        resultat.configure(text=f"{svar:.0f}")


def addisjon():
    try:
        svar = float(tall_1.get()) + float(tall_2.get())
    except ValueError:
        tall_1.delete(0, END)
        tall_2.delete(0, END)
        resultat.configure(text="")
    else:
        resultat.configure(text=f"{svar:.0f}")


def minus():
    try:
        svar = float(tall_1.get()) - float(tall_2.get())
    except ValueError:
        tall_1.delete(0, END)
        tall_2.delete(0, END)
        resultat.configure(text="Error")
    else:
        resultat.configure(text=f"{svar:.0f}")


def deling():
    try:
        svar = float(tall_1.get()) / float(tall_2.get())
    except ValueError:
        tall_1.delete(0, END)
        tall_2.delete(0, END)
        resultat.configure(text="")
    except ZeroDivisionError:
        resultat.configure(text="Error")
    else:
        resultat.configure(text=f"{svar:.0f}")



root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0) #, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


tall_1 = Spinbox(root, from_=0, to=10, increment=1,
                    width=5)
tall_1.grid(row=0, column=0, padx=10, pady=10)

arithmetic_operators = ttk.Combobox(root, values=["+", "-", "*", "/"], width=5)
arithmetic_operators.grid(row=0, column=1, padx=10, pady=10)

tall_2 = Spinbox(root, from_=0, to=10, increment=1,
                    width=5)
tall_2.grid(row=0, column=2, padx=10, pady=10)



def command():
    operator = arithmetic_operators.get()
    if operator == "+":
        addisjon()
    elif operator == "-":
        minus()
    elif operator == "*":
        gange()
    elif operator == "/":
        deling()


Button(root, text="=", command=command, width=5) \
    .grid(row=0, column=3, padx=10, pady=10)


resultat = Label(root, width=5)
resultat.grid(row=0, column=4, padx=10, pady=10)


root.mainloop()