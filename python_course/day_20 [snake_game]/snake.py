from turtle import Turtle
# constants are always capital
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_seg(position)

    def add_seg(self,position):
        new_box = Turtle(shape='square')
        new_box.color('white')
        new_box.penup()
        new_box.goto(position)
        self.segments.append(new_box)

    def extend(self):
        self.add_seg(self.segments[-1].pos())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def left(self):
        if not self.head.heading() == 0:
            self.segments[0].setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]




