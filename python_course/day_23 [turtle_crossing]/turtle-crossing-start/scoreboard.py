from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-290, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.goto(POSITION)
        self.update_level()
        self.ht()

    def update_level(self):
        self.write(f'Level :{self.level}', align='left', font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.home()
        self.write('Game Over!', align='right', font=FONT)
        self.ht()





