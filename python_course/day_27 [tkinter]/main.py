from tkinter import *


def button_clicked():
    # new_text = val.get()
    my_label.config(text=val.get())


# new window
window = Tk()      # capital T
window.title('My First GUI')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = Label(text='New label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

# Entry
val = Entry(width=10)
val.insert(END, string='Some text to begin with')
print(val.get())
val.grid(column=3, row=2)

# button
button = Button(text='Click me',  command=button_clicked)
button.grid(column=1,row=1)

# second button
button = Button(text='Duplicate', command=button_clicked)
button.grid(column=2, row=0)
window.mainloop()