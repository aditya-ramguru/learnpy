from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = '#9bdeac'
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
num = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label.config(text='Timer')
    num = ''
    tick.config(text=num)
    canvas.itemconfig(timer_text, text='00:00')

    global reps
    reps = 0

     
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global num
    if reps < 8:
        reps += 1

    if reps == 8:
        num += '|'
        label.config(text='Break', fg=RED, bg=YELLOW)
        tick.config(text=num, font=(FONT_NAME, 24, 'bold'))
        time = 20
    elif reps % 2 == 0:
        num += '|'
        label.config(text='Break', fg=PINK, bg=YELLOW)
        tick.config(text=num, font=(FONT_NAME, 24, 'bold'))
        time = 5
    else:
        label.config(text='Work', fg=GREEN, bg=YELLOW)
        time = 10

    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# the origin cuz (0,0) is top left of canvas, to place the image in the center and we have to use the class Photocopy
# because tkinter doesnt accept the file format

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# timer label
label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

# tick mark
tick = Label(fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)

# start button
start = Button(text='Start', command=start_timer)
start.grid(column=0, row=2)


# reset button
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
