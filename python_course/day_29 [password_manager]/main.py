from tkinter import *
from tkinter import messagebox  # message box is not a class and thus has to be imported
from random import choice, randint, shuffle
import pyperclip  # helps in copying to clipboard
import json

FONT = ('Arial', 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbol = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_list = password_numbers + password_symbol + password_letters

    shuffle(password_list)

    g_password = "".join(password_list)
    password_entry.insert(0, g_password)
    pyperclip.copy(g_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = web_entry.get()
    username = user_entry.get()
    password = password_entry.get()
    # file_text = f"{website} | {username} | {password}\n"
    new_data = {
        website: {
            'email': username,
            'password': password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        # showinfo allows only one option which is ok.
        messagebox.showinfo(title='OOPS!', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', mode='r') as file:
                # reading old data
                data = json.load(file)  # .load converts data to python dictionary
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                # creating the file
                json.dump(data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open('data.json', mode='w') as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            clear_text(web_entry, password_entry)


def find_password():
    website = web_entry.get()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,message=f'Email:{email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')


def clear_text(*args):
    for word in args:
        word.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.minsize(width=240, height=240)
window.config(padx=50, pady=50)

# image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(50, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website
web_label = Label(text='Website:', font=FONT)
web_label.grid(column=0, row=1)
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

# email/username
user_label = Label(text='Email/Username:', font=FONT)
user_label.grid(column=0, row=2)
user_entry = Entry(width=35)
user_entry.insert(0, 'aditya.ramguru@gmail.com')
user_entry.grid(column=1, row=2, columnspan=2)

# password
password_label = Label(text='Password:', font=FONT)
password_label.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

# generate password button
generate_button = Button(text='Generate Password', width=36, command=generate)
generate_button.grid(column=1, row=5, columnspan=2)

# generate add button
add_button = Button(text='Add', width=36, command=add)
add_button.grid(column=1, row=6, columnspan=2)

# generate search button
search_button = Button(text='Search',width=36, command=find_password)
search_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
