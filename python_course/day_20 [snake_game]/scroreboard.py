from turtle import Turtle
FONT = ('Courier', 22, "normal")
ALIGNMENT = 'center'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open('data.txt') as file:
            self.highscore = int(file.read())
        self.goto(0, 270)
        self.color('white')
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} high score: {self.highscore}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.update_score()

    # def game_over(self):
    #     self.color('white')
    #     self.home()
    #     self.penup()
    #     self.ht()
    #     self.write(f'Game Over!', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt',mode='w') as file:
                file.write(f'{self.highscore}')
        self.score = 0
        self.update_score()