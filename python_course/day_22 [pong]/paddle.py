from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,x_position, y_position):
        super().__init__()
        self.create(x_position, y_position)

    def create(self,x_position, y_position):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x_position, y_position)

    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        else:
            pass

    def down(self):
        if self.ycor() > -228:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            pass







