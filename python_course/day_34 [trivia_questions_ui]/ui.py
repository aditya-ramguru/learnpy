from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # the : adds datatype
    def __init__(self, quiz_brain: QuizBrain):  # quiz brain's type is Quiz brain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('The quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score label
        self.label = Label(text='Score:0', bg=THEME_COLOR, fg='white')
        self.label.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.ques_text = self.canvas.create_text(150,
                                                 125,
                                                 width=280,
                                                 text='some text here',
                                                 font=('Arial', 20, 'italic')
                                                 )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.get_next_question()
        # button
        tick_image = PhotoImage(file='./images/true.png')
        self.tbutton = Button(image=tick_image, highlightthickness=0, command=self.true)
        self.tbutton.grid(column=0, row=2)

        wrong_image = PhotoImage(file='./images/false.png')
        self.wbutton = Button(image=wrong_image, highlightthickness=0, command=self.false)
        self.wbutton.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            # self.canvas.config(bg='white')
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You've reached the end of the quiz!")
            self.tbutton.config(state='disabled')
            self.wbutton.config(state='disabled')

    def true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self,is_right:bool):
        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')

        self.label.config(text=f'Score:{self.quiz.score}')
        self.window.after(1000, self.get_next_question)



