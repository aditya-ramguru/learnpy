from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Agency FB', 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.playerscore = 0
        self.computerscore = 0
        self.line()
        self.player_score()
        self.computer_score()
        self.ht()

    def line(self):
        self.goto(x=0, y=290)
        print(self.position())
        self.setheading(270)
        self.dotted_line()

    def dotted_line(self):
        while self.ycor() > -290:
            self.pencolor('white')
            self.pensize(width=4)
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

    def player_score(self):
        self.speed('fastest')
        self.penup()
        self.goto(x=50, y=230)
        self.pencolor('white')
        self.pensize(width=3)
        self.update_score()

    def computer_score(self):
        self.goto(x=-50, y=230)
        self.pendown()
        self.pencolor('white')
        self.pensize(width=3)
        self.update_score()

    def update_score(self):
        self.penup()
        self.goto(50, 230)
        self.write(f'{self.playerscore}', align=ALIGNMENT, font=FONT)
        self.goto(-50, 230)
        self.write(f'{self.computerscore}', align=ALIGNMENT, font=FONT)
        self.ht()

    def add_pscore(self):
        self.playerscore += 1
        self.reset()
        self.line()
        self.update_score()

    def add_compscore(self):
        self.computerscore += 1
        self.reset()
        self.line()
        self.update_score()

    def game_over(self):
        self.home()
        self.write('Game over!', align=ALIGNMENT, font=('Courier', 28, 'italic'))
