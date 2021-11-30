# import colorgram
#
# colors = colorgram.extract('damien-hirst-spot-painting.jpg',100)
#
# rgb_val = []
# for each in colors:
#     r = each.rgb.r
#     g = each.rgb.g
#     b = each.rgb.b
#     new_color = (int(r), int(g) ,int(b))
#     rgb_val.append(new_color)
# print(rgb_val)
import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.pensize(20)
tim.speed(5)
color_list = [(211, 154, 98), (53, 107, 131), (210, 109, 246), (135, 240, 144),
              (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130),
              (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143),
              (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22),
              (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72),
              (183, 190, 204), (78, 66, 42), (23, 99, 96)]
y = -250
x = -250
tim.penup()
tim.setposition(x, y)
no_of_rows = 0
while no_of_rows < 10:
    for i in range(10):
        tim.pencolor(random.choice(color_list))
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(50)
    no_of_rows += 1
    y += 50
    tim.setposition(x, y)


my_screen = Screen()
my_screen.exitonclick()

