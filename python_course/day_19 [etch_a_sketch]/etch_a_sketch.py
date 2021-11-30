from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_back():
    tim.back(20)


def turn_right():
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='s', fun=move_back)
screen.onkey(key='c', fun=clear)
screen.exitonclick()