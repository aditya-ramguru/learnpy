from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
x1 = -230
y1 = -125

for i in color_list:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(i)
    new_turtle.penup()
    all_turtles.append(new_turtle)
    new_turtle.setposition(x=x1, y=y1)
    y1 += 50

user_input = screen.textinput(title='Make a bet',prompt='Which turtle do you think is going to win? Enter a color: ')
if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_input:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()