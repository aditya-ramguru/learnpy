import random
from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral")
tim.pensize(15)
tim.speed("fastest")

# turtle.colormode(255)
# def random_color():
#     r = random.randint(0,255)   #another way of generating random colors
#     g = random.randint(0,255)   #turtle.colormode() , turtle is the module
#     b = random.randint(0,255)
#     color_tuple = (r, g, b)
#     return color_tuple


directions = [0, 90, 180, 270]
for i in range(200):
    tim.pencolor((random.random(), random.random(), random.random()))
    tim.forward(30)
    tim.setheading(random.choice(directions))















my_screen = Screen()
my_screen.exitonclick()