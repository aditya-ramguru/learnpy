from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral")


def turtle_shape(side):
    for i in range(side):
        tim.forward(100)
        angle = 360/side
        tim.right(angle)


i = 3
while 11 > i:
    r = random.random()
    g = random.random()
    b = random.random()
    tim.pencolor((r,g,b))
    turtle_shape(i)
    i += 1




my_screen = Screen()
my_screen.exitonclick()


