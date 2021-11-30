from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.pensize(1)
tim.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)  # another way of generating random colors
    g = random.randint(0, 255)  # turtle.colormode() , turtle is the module
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

# can use .setheading() as well
for i in range(36):
    tim.pencolor(random_color())
    tim.right(10)
    tim.circle(75)

my_screen = Screen()
my_screen.exitonclick()
