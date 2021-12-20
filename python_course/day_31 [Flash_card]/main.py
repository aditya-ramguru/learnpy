from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ('Arial', 40, 'italic')
FONT_WORD = ('Arial', 80, 'bold')
current_card = {}
to_learn = {}
# -------------------------------------------------Reading data---------------------------------------------------------
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# -------------------------------------------------Button_logic---------------------------------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text='French', fill='black')
    canvas.itemconfig(lang_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_front_template, image=front_img)
    window.after(3000, func=flip_card)


def not_known():
    to_learn.remove(current_card)
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


def flip_card():
    canvas.itemconfig(lang_text, text='English', fill='white')
    canvas.itemconfig(lang_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_front_template, image=back_img)


# -----------------------------------------------------UI---------------------------------------------------------------
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# canvas
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
card_front_template = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
lang_text = canvas.create_text(400, 150, text='', font=FONT_LANG)
lang_word = canvas.create_text(400, 263, text='', font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=50)

# button
checkmark = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')
check_button = Button(image=checkmark, highlightthickness=0, command=next_card)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=not_known)
check_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
