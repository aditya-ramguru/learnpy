from tkinter import *


def conversion(x):
    km = x*1.609
    return round(km, 2)


def button_click():
    km.config(text=f'{conversion(float(val.get()))}')


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=100)

# # empty label
# empty = Label()
# empty.grid(column=0, row=0)

# Entry
val = Entry(width=10)
val.grid(column=1, row=0)

# label 1
m = Label(text='Miles')
m.grid(column=2, row=0)

# label 2
label2 = Label(text='is equal to')
label2.grid(column=0, row=1)

# kmvalue
km = Label(text='0')
km.grid(column=1, row=1)

# label3
lab3 = Label(text='Km')
lab3.grid(column=2, row=1)

# button
button = Button(text='Calculate', command=button_click)
button.grid(column=1, row=2)

window.mainloop()
