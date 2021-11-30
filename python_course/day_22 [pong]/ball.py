from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.ymove = 10
        self.xmove = 10
        self.move_speed = 0.09

    def reset(self):
        self.home()
        self.move_speed = 0.09
        self.x_bounce()

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def y_bounce(self):
        self.ymove *= -1

    def x_bounce(self):
        self.xmove *= -1
        self.move_speed *= 0.9




