from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()

player_paddle = Paddle(370, 0)
computer_paddle = Paddle(-370, 0)
screen.onkeypress(key='Up', fun=player_paddle.up)
screen.onkeypress(key='Down', fun=player_paddle.down)
screen.onkeypress(key='w', fun=computer_paddle.up)
screen.onkeypress(key='s', fun=computer_paddle.down)
ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        # needs to bounce
        ball.y_bounce()

    if ball.distance(player_paddle) < 50 and ball.xcor() > 340 or ball.distance(
            computer_paddle) < 50 and ball.xcor() < -340:
        ball.x_bounce()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_pscore()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_compscore()

    if scoreboard.playerscore == 4 or scoreboard.computerscore == 4:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()