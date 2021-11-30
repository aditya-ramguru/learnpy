from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self,):
        self.allcars = []

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 255)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.allcars.append(new_car)

    def move(self):
        for each in self.allcars:
            each.forward(STARTING_MOVE_DISTANCE)

    def add_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += 5
        self.move()



