from tkinter import *

# new window
window = Tk()      # capital T
window.title('My First GUI')
window.minsize(width=500, height=300)

# label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()

# Entry
val = Entry(width=10)
val.insert(END, string='Some text to begin with')
val.pack()

# TEXT
text = Text(height=5, width=30)
# puts cursor in textbox
text.focus()
# adds some line to begin with
text.insert(END, 'Example of multiline text entry')
# gets current value in textbox at line 1, character 0
print(text.get('1.0', END))
text.pack()


# spinbox
def spinbox_used():
    # gets value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=10, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # prints one if button is used and 0 otherwise.
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text='Is on?', variable=checked_state, command=checkbutton_used())
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used())
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used())
radiobutton1.pack()
radiobutton2.pack()


# listbox
def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ['apple', 'pear', 'mango', 'orange']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()


# button
def button_clicked():
    # new_text = val.get()
    my_label.config(text=val.get())


button = Button(text='Click me',  command=button_clicked)
button.pack()
window.mainloop()